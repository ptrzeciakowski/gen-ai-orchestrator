"""
Provider pobierający surowe oferty z serwisu Nieruchomosci-online.pl (Warstwa Bronze).
Wyciąga ustrukturyzowane metadane z formatu pozycyjnego URL, JSON-LD oraz tabeli parametrów technicznych HTML.
"""
import urllib.request
import urllib.error
import re
import json
import time
import random
from src.db import DatabaseManager

class NieruchomosciOnlineProvider:
    def __init__(self, config, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()
        self.max_pages = 5

    def _normalize_slug(self, text: str) -> str:
        """
        Normalizuje nazwę miasta/dzielnicy do postaci sluga bez polskich znaków diakrytycznych.
        """
        if not text:
            return ""
        trans_map = str.maketrans({
            'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
            'Ą': 'a', 'Ć': 'c', 'Ę': 'e', 'Ł': 'l', 'Ń': 'n', 'Ó': 'o', 'Ś': 's', 'Ź': 'z', 'Ż': 'z'
        })
        slug = text.translate(trans_map).lower().strip()
        slug = re.sub(r'[\s_]+', '-', slug)
        slug = re.sub(r'[^a-z0-9\-]', '', slug)
        return slug.strip('-')

    def build_search_url(self, city: str, district: str = "", page: int = 1) -> str:
        """
        Buduje adres URL w formacie pozycyjnym portalu Nieruchomosci-online.pl (szeroki zrzut dla danej lokalizacji).
        """
        city_norm = self._normalize_slug(city) if city else "warszawa"
        dist_norm = self._normalize_slug(district) if district else ""
        loc_slot = f"{city_norm}:{dist_norm}" if dist_norm else city_norm

        # 8 slotów pozycyjnych: tryb 3, mieszkanie, sprzedaz, rynek dowolny, lokalizacja, cena dowolna, metraż dowolny, pokoje dowolne
        slots = ["3", "mieszkanie", "sprzedaz", "", loc_slot, "", "", ""]
        base_query = ",".join(slots)
        url = f"https://www.nieruchomosci-online.pl/szukaj.html?{base_query}"
        if page > 1:
            url += f"&p={page}"
        return url

    def parse_listing_html(self, html: str):
        """
        Wyciąga całkowitą liczbę ogłoszeń oraz unikalne linki do ofert z kodu HTML listy.
        """
        expected_total = None
        # Wyszukiwanie deklarowanej liczby ofert
        m_total = (
            re.search(r'znaleziono\s*<strong>\s*(\d+)\s*</strong>\s*ogłosze', html, re.IGNORECASE)
            or re.search(r'(\d+)\s*ogłosze(?:ń|nia|nie)', html, re.IGNORECASE)
            or re.search(r'znaleziono\s*(\d+)\s*ogłosze', html, re.IGNORECASE)
            or re.search(r'liczba\s*ogłoszeń:\s*<strong>(\d+)</strong>', html, re.IGNORECASE)
        )
        if m_total:
            try:
                expected_total = int(m_total.group(1))
            except (ValueError, TypeError):
                pass

        # Ekstrakcja linków do ogłoszeń
        raw_hrefs = re.findall(r'href=["\']((?:https?://[a-zA-Z0-9.-]*nieruchomosci-online\.pl)?/[^"\'\s]*?(\d+)\.html)["\']', html)
        offer_urls = []
        seen = set()
        for href_tuple in raw_hrefs:
            href = href_tuple[0] if isinstance(href_tuple, tuple) else href_tuple
            if href.startswith('/'):
                href = "https://www.nieruchomosci-online.pl" + href
            if href not in seen and "/szukaj" not in href:
                seen.add(href)
                offer_urls.append(href)

        return expected_total, offer_urls

    def parse_detail_html(self, html: str, url: str, default_city: str = "Warszawa", default_district: str = "Ursynów"):
        """
        Parsuje stronę szczegółową ogłoszenia i zwraca ustrukturyzowany słownik raw_payload.
        """
        # 1. ID ogłoszenia
        ext_id_match = re.search(r'(\d+)\.html', url) or re.search(r'/(\d+)', url)
        ext_id = ext_id_match.group(1) if ext_id_match else str(abs(hash(url)))

        # 2. JSON-LD
        json_lds = re.findall(r'<script [^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
        offer_ld = {}
        place_ld = {}
        apartment_ld = {}
        all_json_ld = []

        for j in json_lds:
            try:
                data_j = json.loads(j.strip())
                all_json_ld.append(data_j)
                graph = data_j.get('@graph', [data_j]) if isinstance(data_j, dict) else [data_j]
                for node in graph:
                    if not isinstance(node, dict):
                        continue
                    ntype = str(node.get('@type', '')).lower()
                    if 'offer' in ntype:
                        offer_ld = node
                    elif 'place' in ntype:
                        place_ld = node
                    elif any(k in ntype for k in ['apartment', 'product', 'singlefamilyresidence', 'residence', 'realestatelisting']):
                        apartment_ld = node
            except Exception:
                pass

        # 3. Tytuł i Opis
        title = None
        if place_ld.get('name'):
            title = place_ld.get('name')
        elif apartment_ld.get('name'):
            title = apartment_ld.get('name')
        elif offer_ld.get('name'):
            title = offer_ld.get('name')
        
        if not title:
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
            if h1_match:
                title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip()
        if not title:
            title = f"Mieszkanie {default_city} {default_district}"

        description = (
            place_ld.get('description')
            or apartment_ld.get('description')
            or offer_ld.get('description')
            or ""
        )
        if not description:
            desc_match = re.search(r'<(?:div|section|p)[^>]*(?:id|class)=["\'][^"\']*(?:description|opis|text)[^"\']*["\'][^>]*>(.*?)</(?:div|section|p)>', html, re.DOTALL | re.IGNORECASE)
            if desc_match:
                description = re.sub(r'<[^>]+>', ' ', desc_match.group(1)).strip()

        # 4. Cena (PLN)
        price_val = None
        if offer_ld.get('price'):
            try:
                price_val = float(str(offer_ld.get('price')).replace(' ', '').replace(',', '.'))
            except (ValueError, TypeError):
                pass
        elif apartment_ld.get('offers', {}).get('price'):
            try:
                price_val = float(str(apartment_ld['offers']['price']).replace(' ', '').replace(',', '.'))
            except (ValueError, TypeError):
                pass

        if price_val is None:
            p_match = re.search(r'(\d[\d\s]*[,\.]?\d*)\s*(?:zł|PLN)', html, re.IGNORECASE)
            if p_match:
                try:
                    p_clean = p_match.group(1).replace(' ', '').replace('\xa0', '').replace(',', '.')
                    price_val = float(p_clean)
                except (ValueError, TypeError):
                    pass

        # 5. Współrzędne geograficzne
        lat = None
        lon = None
        geo_ld = place_ld.get('geo') or apartment_ld.get('geo') or {}
        if isinstance(geo_ld, dict):
            lat = geo_ld.get('latitude')
            lon = geo_ld.get('longitude')

        if lat is None or lon is None:
            coord_match = re.search(r'["\']?latitude["\']?\s*:\s*([0-9\.]+)\s*,\s*["\']?longitude["\']?\s*:\s*([0-9\.]+)', html, re.IGNORECASE)
            if not coord_match:
                coord_match = re.search(r'lat["\']?\s*:\s*([0-9\.]+)\s*,\s*["\']?lng["\']?\s*:\s*([0-9\.]+)', html, re.IGNORECASE)
            if coord_match:
                try:
                    lat = float(coord_match.group(1))
                    lon = float(coord_match.group(2))
                except (ValueError, TypeError):
                    pass

        # 6. Parametry techniczne (metraż, pokoje, piętro, rok budowy, winda)
        clean_text = re.sub(r'<[^>]+>', ' ', html)
        clean_text = re.sub(r'\s+', ' ', clean_text)

        # Powierzchnia (area_m2)
        area_val = None
        if apartment_ld.get('floorSize', {}).get('value'):
            try:
                area_val = float(apartment_ld['floorSize']['value'])
            except (ValueError, TypeError):
                pass
        if area_val is None:
            area_match = re.search(r'(\d+([.,]\d+)?)\s*m[²2]', html, re.IGNORECASE)
            if area_match:
                try:
                    area_val = float(area_match.group(1).replace(',', '.'))
                except (ValueError, TypeError):
                    pass

        # Pokoje (rooms)
        rooms_val = None
        if apartment_ld.get('numberOfRooms'):
            try:
                rooms_val = int(apartment_ld['numberOfRooms'])
            except (ValueError, TypeError):
                pass
        if rooms_val is None:
            rooms_match = re.search(r'(\d+)\s*(?:pokoje|pokoi|pokój|pok\b)', html, re.IGNORECASE)
            if rooms_match:
                try:
                    rooms_val = int(rooms_match.group(1))
                except (ValueError, TypeError):
                    pass

        # Piętro i Całkowita Liczba Pięter
        floor_val = None
        total_floors_val = None

        if re.search(r'\bparter\b', clean_text, re.IGNORECASE) and not re.search(r'piętro\s*:\s*[1-9]', clean_text, re.IGNORECASE):
            floor_val = 0

        floor_slash_match = re.search(r'piętro\s*[:\s]*(\d+)\s*(?:z|/)\s*(\d+)', clean_text, re.IGNORECASE)
        if floor_slash_match:
            floor_val = int(floor_slash_match.group(1))
            total_floors_val = int(floor_slash_match.group(2))
        else:
            if floor_val is None:
                floor_single_match = re.search(r'piętro\s*[:\s]*(\d+)', clean_text, re.IGNORECASE)
                if floor_single_match:
                    floor_val = int(floor_single_match.group(1))
            
            tot_match = re.search(r'liczba\s*pięter\s*[:\s]*(\d+)', clean_text, re.IGNORECASE) or re.search(r'piętr(?:owy|ach|ach w budynku)\s*[:\s]*(\d+)', clean_text, re.IGNORECASE)
            if tot_match:
                total_floors_val = int(tot_match.group(1))

        # Rok budowy
        build_year = None
        if apartment_ld.get('yearBuilt'):
            try:
                build_year = int(apartment_ld['yearBuilt'])
            except (ValueError, TypeError):
                pass
        if build_year is None:
            year_match = re.search(r'rok\s*budowy\s*[:\s]*(\d{4})', clean_text, re.IGNORECASE)
            if year_match:
                build_year = int(year_match.group(1))

        # Winda (rozszerzona detekcja: 'winda', 'dźwig osobowy', 'cichobieżna')
        elevator_pattern = re.compile(r'(winda|windą|windy|dźwig osobowy|cichobieżna|cichobieżny|cichobieżne)', re.IGNORECASE)
        has_elevator = 1 if elevator_pattern.search(clean_text) else 0

        # Typ ogłoszeniodawcy
        seller_type = "Agencja"
        if re.search(r'(bez\s*pośredników|bezpośrednio|ogłoszenie\s*prywatne|właściciel)', clean_text, re.IGNORECASE):
            seller_type = "Bezpośrednio"

        # Lokalizacja (miasto, dzielnica, ulica)
        address_ld = place_ld.get('address') or apartment_ld.get('address') or {}
        city_val = default_city
        district_val = default_district
        street_val = ""

        if isinstance(address_ld, dict):
            city_val = address_ld.get('addressLocality') or default_city
            district_val = address_ld.get('addressRegion') or default_district
            street_val = address_ld.get('streetAddress') or ""

        # Wyciąganie dzielnicy z tytułu jeśli nie ma w JSON-LD
        dist_match = re.search(rf'{default_city}\s+([A-ZĄĆĘŁŃÓŚŹŻa-ząćęłńóśźż]+)', title, re.IGNORECASE)
        if dist_match and district_val == default_district:
            candidate_district = dist_match.group(1).strip()
            if candidate_district.lower() not in ["mieszkanie", "dom", "sprzedam", "kawalerka"]:
                district_val = candidate_district

        raw_payload = {
            "id": ext_id,
            "title": title,
            "url": url,
            "price_pln": price_val,
            "area_m2": area_val,
            "rooms": rooms_val,
            "floor": floor_val,
            "total_floors": total_floors_val,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "description_text": description,
            "location": {
                "city": city_val,
                "district": district_val,
                "street": street_val,
                "coordinates": {
                    "latitude": lat,
                    "longitude": lon
                }
            },
            "technical_details": {
                "has_elevator": bool(has_elevator),
                "build_year": build_year,
                "floor": floor_val,
                "total_floors": total_floors_val
            },
            "json_ld": all_json_ld
        }

        return raw_payload

    def fetch_listings(self, run_id=None) -> int:
        """
        Dwufazowe pobieranie ogłoszeń z serwisu Nieruchomosci-online.pl do warstwy Bronze.
        """
        city = self.config.city if self.config.city else "Warszawa"
        city_slug = self._normalize_slug(city)
        districts = self.config.districts if self.config.districts else ["Ursynów"]

        saved_count = 0
        total_expected_sum = 0
        has_any_expected = False

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

        for district in districts:
            district_slug = self._normalize_slug(district)
            chunk_name = f"{city_slug}_{district_slug}_nieruchomosci_online"

            page = 1
            district_expected = None
            district_saved = 0

            while page <= self.max_pages:
                search_url = self.build_search_url(city=city, district=district, page=page)
                req = urllib.request.Request(search_url, headers=headers)

                html = None
                # Obsługa pobierania listy z retry (Exponential backoff dla 429/403)
                for attempt in range(3):
                    try:
                        with urllib.request.urlopen(req, timeout=10) as resp:
                            html = resp.read().decode('utf-8', errors='replace')
                        break
                    except urllib.error.HTTPError as e_http:
                        if e_http.code in (429, 403):
                            time.sleep(1.0 * (2 ** attempt))
                        else:
                            print(f"Błąd HTTP {e_http.code} podczas pobierania listy Nieruchomosci-online ({district}, strona {page}): {e_http}")
                            break
                    except Exception as e:
                        print(f"Błąd pobierania listy Nieruchomosci-online ({district}, strona {page}): {e}")
                        break

                if not html:
                    break

                # Faza 1: Ekstrakcja liczby ofert i linków
                exp_count, offer_urls = self.parse_listing_html(html)
                if page == 1 and exp_count is not None:
                    district_expected = exp_count
                    total_expected_sum += exp_count
                    has_any_expected = True

                if not offer_urls:
                    break

                # Faza 2: Pobieranie kart szczegółowych
                for offer_url in offer_urls:
                    ext_id_match = re.search(r'(\d+)\.html', offer_url) or re.search(r'/(\d+)', offer_url)
                    ext_id = ext_id_match.group(1) if ext_id_match else str(abs(hash(offer_url)))

                    # Politeness delay
                    time.sleep(random.uniform(0.2, 0.4))

                    html_detail = None
                    req_detail = urllib.request.Request(offer_url, headers=headers)
                    try:
                        with urllib.request.urlopen(req_detail, timeout=5) as resp_d:
                            html_detail = resp_d.read().decode('utf-8', errors='replace')
                    except Exception as e_detail:
                        print(f"Błąd pobierania szczegółów Nieruchomosci-online {offer_url}: {e_detail}")
                        continue

                    if not html_detail:
                        continue

                    raw_payload = self.parse_detail_html(
                        html=html_detail,
                        url=offer_url,
                        default_city=city,
                        default_district=district
                    )

                    self.db_manager.insert_bronze_listing(
                        source_portal="nieruchomosci_online",
                        external_id=ext_id,
                        city=city,
                        chunk_name=chunk_name,
                        raw_payload=raw_payload,
                        run_id=run_id
                    )
                    saved_count += 1
                    district_saved += 1

                if district_expected and district_saved >= district_expected:
                    break

                page += 1

        if has_any_expected and run_id:
            self.db_manager.save_run_audit(run_id, "nieruchomosci_online", total_expected_sum, saved_count)

        return saved_count
