"""
Provider pobierający surowe oferty z serwisu OLX.pl (Warstwa Bronze).
Wdrożona strategia:
- Generowanie precyzyjnych zapytań URL (cena, pokoje, dzielnica, paginacja).
- Wielowariantowy parser stanu SSR (__PRERENDERED_STATE__, JSON-LD, Link Harvester).
- Pre-normalizacja O(1) w Pythonie spłaszczająca parametry do korzenia słownika.
- Zapis do bazy danych bronze_listings oraz rejestracja audytu kompletności (run_audit).
"""
import urllib.request
import urllib.error
import re
import json
import time
from src.db import DatabaseManager

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="124", "Not(A:Brand";v="24", "Google Chrome";v="124"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

class OLXProvider:
    def __init__(self, config=None, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()
        self.max_pages = 5

    def _slugify(self, text):
        """Pomocnicza funkcja normalizująca polskie znaki do slugów URL."""
        if not text:
            return ""
        t = str(text).lower().strip()
        trans = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
        t = t.translate(trans)
        t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
        return t

    def build_search_url(self, city="Warszawa", district=None, page=1):
        """
        Buduje adres URL zapytania do OLX.pl na podstawie kryteriów wyszukiwania.
        """
        city_slug = self._slugify(city) if city else "warszawa"
        if district:
            district_slug = self._slugify(district)
            base_url = f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/{city_slug}/q-{district_slug}/"
        else:
            base_url = f"https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/{city_slug}/"

        params = []
        if page and page > 1:
            params.append(f"page={page}")

        if self.config:
            if self.config.min_price is not None:
                params.append(f"search[filter_float_price:from]={int(self.config.min_price)}")
            if self.config.max_price is not None:
                params.append(f"search[filter_float_price:to]={int(self.config.max_price)}")

            room_mapping = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
            if self.config.min_rooms is not None and self.config.max_rooms is not None:
                if self.config.min_rooms == self.config.max_rooms:
                    r_val = room_mapping.get(int(self.config.min_rooms), str(int(self.config.min_rooms)))
                    params.append(f"search[filter_enum_rooms][0]={r_val}")
                else:
                    for idx, r in enumerate(range(int(self.config.min_rooms), int(self.config.max_rooms) + 1)):
                        r_val = room_mapping.get(r, str(r))
                        params.append(f"search[filter_enum_rooms][{idx}]={r_val}")
            elif self.config.min_rooms is not None:
                r_val = room_mapping.get(int(self.config.min_rooms), str(int(self.config.min_rooms)))
                params.append(f"search[filter_enum_rooms][0]={r_val}")

        if params:
            return f"{base_url}?{'&'.join(params)}"
        return base_url

    def _extract_ads_and_meta(self, html, default_city="Warszawa", default_district="Ursynów"):
        """
        Wielowariantowy parser stanu SSR i struktury HTML serwisu OLX.
        Zwraca tuple: (ads_list, expected_total).
        """
        ads = []
        expected_total = None

        # 1. Wzorzec Główny: <script id="__PRERENDERED_STATE__"[^>]*>(.*?)</script>
        m_state = re.search(r'<script\s+id=[\'"]__PRERENDERED_STATE__[\'"][^>]*>(.*?)</script>', html, re.DOTALL)
        if m_state:
            try:
                raw_json = m_state.group(1).strip()
                if raw_json.startswith('"') and raw_json.endswith('"'):
                    raw_json = json.loads(raw_json)
                state_data = json.loads(raw_json) if isinstance(raw_json, str) else raw_json
                ads, expected_total = self._parse_state_dict(state_data)
                if ads:
                    return ads, expected_total
            except Exception:
                pass

        # 2. Wzorzec Alternatywny 1: window.__PRERENDERED_STATE__ = ...
        m_win = re.search(r'window\.__PRERENDERED_STATE__\s*=\s*(?:\"(\{.*?\})\"|(\{.*?\}));', html, re.DOTALL)
        if m_win:
            try:
                raw_content = m_win.group(1) or m_win.group(2)
                if raw_content:
                    state_data = json.loads(raw_content)
                    ads, expected_total = self._parse_state_dict(state_data)
                    if ads:
                        return ads, expected_total
            except Exception:
                pass

        # 3. Wzorzec Alternatywny 2: JSON-LD Schema.org
        json_lds = re.findall(r'<script\s+[^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>', html, re.DOTALL)
        for j in json_lds:
            try:
                ld_data = json.loads(j)
                graph = ld_data.get('@graph', [ld_data]) if isinstance(ld_data, dict) else (ld_data if isinstance(ld_data, list) else [])
                for node in graph:
                    if isinstance(node, dict) and node.get('@type') in ('ItemList', 'SearchResultsPage'):
                        items = node.get('itemListElement', [])
                        for it in items:
                            item_node = it.get('item', it) if isinstance(it, dict) else {}
                            if item_node:
                                ads.append(item_node)
                    elif isinstance(node, dict) and node.get('@type') in ('Product', 'Offer', 'SingleFamilyResidence', 'Apartment'):
                        ads.append(node)
            except Exception:
                pass

        if ads:
            return ads, expected_total

        # 4. Fallback Link Harvester: regex href="/d/oferta/..."
        matches = re.findall(r'href=[\'"](/d/oferta/[^\'"]+)[\'"]', html)
        unique_hrefs = []
        for match_item in matches:
            clean_m = match_item.split('?')[0]
            if clean_m.startswith('/d/oferta/') and clean_m not in unique_hrefs:
                unique_hrefs.append(clean_m)

        for clean_href in unique_hrefs:
            ext_id = clean_href.replace('/d/oferta/', '').split('.')[0].split('-')[-1]
            ads.append({
                "id": ext_id,
                "title": f"Mieszkanie {default_city} {default_district}",
                "url": "https://www.olx.pl" + clean_href,
                "description": ""
            })

        # Próba wyciągnięcia liczby ogłoszeń z tekstu HTML
        if expected_total is None:
            m_total = re.search(r'(\d+[\s\d]*)\s*(?:ogłosze|ofert)', html, re.IGNORECASE)
            if m_total:
                num_str = re.sub(r'\s+', '', m_total.group(1))
                if num_str.isdigit():
                    expected_total = int(num_str)

        return ads, expected_total

    def _parse_state_dict(self, state_data):
        """Pomocnicze przeszukiwanie struktury słownika stanu SSR w poszukiwaniu ogłoszeń i metadanych."""
        ads = []
        expected_total = None

        if not isinstance(state_data, dict):
            return ads, expected_total

        # Ścieżki w OLX SSR
        data_section = (
            state_data.get('props', {}).get('pageProps', {}).get('data', {}) or
            state_data.get('pageProps', {}).get('data', {}) or
            state_data.get('data', {}) or
            state_data
        )

        ad_search = (
            data_section.get('adSearch', {}) or
            data_section.get('listing', {}) or
            data_section.get('searchAds', {}) or
            state_data.get('adSearch', {}) or
            state_data.get('listing', {})
        )

        if isinstance(ad_search, dict):
            expected_total = (
                ad_search.get('totalElements') or
                ad_search.get('totalCount') or
                ad_search.get('total_elements') or
                ad_search.get('total_count')
            )
            raw_ads = ad_search.get('data') or ad_search.get('ads') or ad_search.get('items')
            if isinstance(raw_ads, list):
                ads.extend(raw_ads)

        # Alternatywne przeszukanie kluczy korzenia
        if not ads:
            for k in ('ads', 'data', 'items'):
                if isinstance(data_section.get(k), list):
                    ads.extend(data_section.get(k))
                    break

        return ads, expected_total

    def _normalize_ad_payload(self, raw_item, default_city="Warszawa", default_district="Ursynów"):
        """
        Pre-normalizacja parametrów O(1) w Pythonie.
        Spłaszcza parametry z tablicy params do korzenia słownika przed zapisem do Bronze.
        """
        if not isinstance(raw_item, dict):
            return {}

        # 1. Zbudowanie mapy parametrów params
        param_dict = {}
        for p in raw_item.get('params', []):
            if not isinstance(p, dict):
                continue
            k = p.get('key') or p.get('name')
            if not k:
                continue
            v = p.get('value')
            param_dict[k] = v

        def extract_param_val(k):
            val_obj = param_dict.get(k)
            if val_obj is None:
                return None
            if isinstance(val_obj, dict):
                return val_obj.get('value', val_obj.get('key'))
            return val_obj

        def extract_param_key(k):
            val_obj = param_dict.get(k)
            if val_obj is None:
                return None
            if isinstance(val_obj, dict):
                return val_obj.get('key', val_obj.get('value'))
            return str(val_obj)

        def extract_param_label(k):
            val_obj = param_dict.get(k)
            if val_obj is None:
                return None
            if isinstance(val_obj, dict):
                return val_obj.get('label')
            return str(val_obj)

        # Identyfikator
        ext_id = str(raw_item.get('id') or raw_item.get('external_id') or "")
        if not ext_id and raw_item.get('url'):
            m_id = re.search(r'ID([a-zA-Z0-9]+)', raw_item.get('url'))
            ext_id = m_id.group(1) if m_id else str(abs(hash(raw_item.get('url'))))

        # Tytuł
        title = raw_item.get('title') or f"Mieszkanie {default_city} {default_district}"

        # URL
        url = raw_item.get('url') or raw_item.get('link') or ""
        if url and url.startswith('/'):
            url = f"https://www.olx.pl{url}"
        elif not url:
            url = f"https://www.olx.pl/d/oferta/{ext_id}.html"

        # Opis
        description_text = raw_item.get('description_text') or raw_item.get('description') or ""
        if description_text:
            description_text = re.sub(r'<[^>]+>', ' ', description_text).strip()

        # Cena (PLN)
        price_pln = raw_item.get('price_pln')
        if price_pln is None:
            price_obj = raw_item.get('price')
            if isinstance(price_obj, dict):
                price_pln = price_obj.get('value', price_obj.get('regularPrice', {}).get('value'))
            elif price_obj is not None:
                price_pln = price_obj
            else:
                price_pln = extract_param_val('price')

        if price_pln is not None:
            try:
                price_pln = float(str(price_pln).replace(' ', '').replace(',', '.'))
            except (ValueError, TypeError):
                price_pln = None

        # Powierzchnia (m²)
        area_m2 = raw_item.get('area_m2')
        if area_m2 is None:
            area_obj = raw_item.get('area')
            if isinstance(area_obj, dict):
                area_m2 = area_obj.get('value')
            elif area_obj is not None:
                area_m2 = area_obj
            else:
                area_m2 = extract_param_val('m') or extract_param_val('area') or extract_param_val('surface')

        if area_m2 is not None:
            try:
                area_m2 = float(str(area_m2).replace(' ', '').replace(',', '.'))
            except (ValueError, TypeError):
                area_m2 = None

        # Pokoje (rooms)
        rooms = raw_item.get('rooms')
        if rooms is None:
            rooms_raw = extract_param_key('rooms') or extract_param_val('rooms') or raw_item.get('roomsNumber')
            if rooms_raw is not None:
                r_str = str(rooms_raw).lower()
                room_map = {
                    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                    'six': 6, 'seven': 7, 'eight': 8, 'more': 5
                }
                if r_str in room_map:
                    rooms = room_map[r_str]
                else:
                    m_r = re.search(r'\d+', r_str)
                    rooms = int(m_r.group()) if m_r else None

        # Piętro (floor)
        floor = raw_item.get('floor')
        if floor is None:
            floor_raw = (
                extract_param_key('floor_select') or
                extract_param_val('floor_select') or
                extract_param_key('floor') or
                extract_param_val('floor') or
                raw_item.get('floorNumber')
            )
            if floor_raw is not None:
                f_str = str(floor_raw).lower()
                if f_str in ('floor_0', 'parter', 'ground', 'ground_floor', '0'):
                    floor = 0
                elif f_str.startswith('floor_'):
                    f_num = f_str.replace('floor_', '')
                    if f_num == 'higher':
                        floor = 12
                    elif f_num.isdigit():
                        floor = int(f_num)
                elif f_str == 'poddasze':
                    floor = 11
                else:
                    m_f = re.search(r'\d+', f_str)
                    floor = int(m_f.group()) if m_f else None

        # Liczba pięter w budynku (total_floors)
        total_floors = raw_item.get('total_floors')
        if total_floors is None:
            tf_raw = (
                extract_param_val('total_floors') or
                extract_param_val('number_of_floors') or
                extract_param_val('floors_in_building') or
                extract_param_val('building_floors_num')
            )
            if tf_raw is not None:
                try:
                    total_floors = int(str(tf_raw).strip())
                except (ValueError, TypeError):
                    pass
            if total_floors is None and description_text:
                m_tf = re.search(r'piętro\s*\d+\s*z\s*(\d+)', description_text, re.IGNORECASE) or re.search(r'w\s*(\d+)[ -]piętrowym', description_text, re.IGNORECASE)
                if m_tf:
                    total_floors = int(m_tf.group(1))

        # Winda (has_elevator)
        has_elevator = raw_item.get('has_elevator')
        if has_elevator is None:
            elev_raw = extract_param_key('elevator') or extract_param_val('elevator')
            if elev_raw is not None:
                e_str = str(elev_raw).lower()
                if e_str in ('yes', 'tak', '1', 'true'):
                    has_elevator = 1
                elif e_str in ('no', 'nie', '0', 'false'):
                    has_elevator = 0

            if has_elevator is None:
                full_text = f"{title} {description_text}".lower()
                if re.search(r'\b(winda|windą|windy|windzie)\b', full_text):
                    has_elevator = 1
                else:
                    has_elevator = 0

        # Rok budowy (build_year)
        build_year = raw_item.get('build_year')
        if build_year is None:
            by_raw = extract_param_val('build_year') or extract_param_val('builttype_year') or extract_param_val('rok_budowy') or extract_param_val('builtyear')
            if by_raw is not None:
                try:
                    build_year = int(str(by_raw).strip())
                except (ValueError, TypeError):
                    pass
            if build_year is None and description_text:
                m_yr = re.search(r'\brok\s*(?:budowy)?\s*(\d{4})\b', description_text, re.IGNORECASE)
                if m_yr:
                    build_year = int(m_yr.group(1))

        # Typ ogłoszeniodawcy (seller_type)
        seller_type = raw_item.get('seller_type')
        if seller_type is None:
            user_obj = raw_item.get('user', {})
            if isinstance(user_obj, dict) and 'is_business' in user_obj:
                seller_type = "Agencja" if user_obj['is_business'] else "Bezpośrednio"
            else:
                pb_val = extract_param_key('private_business') or extract_param_val('private_business')
                if pb_val:
                    seller_type = "Bezpośrednio" if 'private' in str(pb_val).lower() else "Agencja"
                else:
                    full_text = f"{title} {description_text}".lower()
                    if "bez pośredników" in full_text or "osoba prywatna" in full_text or "sprzedaż bezpośrednia" in full_text:
                        seller_type = "Bezpośrednio"
                    else:
                        seller_type = "Agencja"

        # Lokalizacja i Współrzędne
        loc_obj = raw_item.get('location') or {}
        city_name = default_city
        district_name = default_district

        if isinstance(loc_obj, dict):
            c_val = loc_obj.get('city')
            if isinstance(c_val, dict):
                city_name = c_val.get('name', default_city)
            elif isinstance(c_val, str) and c_val:
                city_name = c_val

            d_val = loc_obj.get('district')
            if isinstance(d_val, dict):
                district_name = d_val.get('name', default_district)
            elif isinstance(d_val, str) and d_val:
                district_name = d_val

        map_obj = raw_item.get('map') or {}
        lat = None
        lon = None
        if isinstance(map_obj, dict):
            lat = map_obj.get('lat')
            lon = map_obj.get('lon')

        if lat is None or lon is None:
            coord_obj = loc_obj.get('coordinates') if isinstance(loc_obj, dict) else {}
            if isinstance(coord_obj, dict):
                lat = lat or coord_obj.get('latitude') or coord_obj.get('lat')
                lon = lon or coord_obj.get('longitude') or coord_obj.get('lon')

        if lat is None or lon is None:
            geo_obj = raw_item.get('geo') or {}
            if isinstance(geo_obj, dict):
                lat = lat or geo_obj.get('latitude') or geo_obj.get('lat')
                lon = lon or geo_obj.get('longitude') or geo_obj.get('lon')

        try:
            lat = float(lat) if lat is not None else None
            lon = float(lon) if lon is not None else None
        except (ValueError, TypeError):
            lat, lon = None, None

        normalized_payload = {
            "id": ext_id,
            "title": title,
            "url": url,
            "price_pln": price_pln,
            "area_m2": area_m2,
            "rooms": rooms,
            "floor": floor,
            "total_floors": total_floors,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "description_text": description_text,
            "location": {
                "city": city_name,
                "district": district_name,
                "coordinates": {
                    "latitude": lat,
                    "longitude": lon
                }
            },
            "raw_olx_data": raw_item
        }

        return normalized_payload

    def fetch_listings(self, run_id=None):
        """
        Główna pętla pobierająca ogłoszenia z OLX.pl, pre-normalizująca dane i zapisująca do tabeli bronze_listings.
        """
        city = self.config.city if self.config and self.config.city else "Warszawa"
        districts = self.config.districts if self.config and self.config.districts else ["Ursynów"]

        saved_count = 0
        expected_total_olx = None

        for district in districts:
            district_slug = self._slugify(district)
            chunk_name = f"{self._slugify(city)}_{district_slug}_olx"

            page = 1
            while page <= self.max_pages:
                url = self.build_search_url(city=city, district=district, page=page)
                req = urllib.request.Request(url, headers=HEADERS)

                html = None
                max_retries = 2
                for attempt in range(max_retries + 1):
                    try:
                        with urllib.request.urlopen(req, timeout=10) as resp:
                            html = resp.read().decode('utf-8')
                        break
                    except urllib.error.HTTPError as e_http:
                        if e_http.code in (403, 429) and attempt < max_retries:
                            backoff = 1.5 * (attempt + 1)
                            time.sleep(backoff)
                            continue
                        else:
                            print(f"Błąd HTTP OLX dla {district} (strona {page}): {e_http}")
                            break
                    except Exception as e:
                        if attempt < max_retries:
                            time.sleep(1.0)
                            continue
                        else:
                            print(f"Błąd sieciowy OLX dla {district} (strona {page}): {e}")
                            break

                if not html:
                    break

                ads, exp_total = self._extract_ads_and_meta(html, default_city=city, default_district=district)
                if exp_total is not None and expected_total_olx is None:
                    expected_total_olx = exp_total

                if not ads:
                    break

                for ad in ads:
                    normalized_ad = self._normalize_ad_payload(ad, default_city=city, default_district=district)
                    ext_id = str(normalized_ad.get("id"))
                    if not ext_id:
                        continue

                    self.db_manager.insert_bronze_listing(
                        source_portal="olx",
                        external_id=ext_id,
                        city=city,
                        chunk_name=chunk_name,
                        raw_payload=normalized_ad,
                        run_id=run_id
                    )
                    saved_count += 1

                time.sleep(0.2)
                page += 1

        if expected_total_olx is not None and run_id:
            self.db_manager.save_run_audit(run_id, "olx", expected_total_olx, saved_count)

        return saved_count
