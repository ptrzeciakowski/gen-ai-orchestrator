"""
Provider pobierający surowe oferty z serwisu Morizon.pl (Warstwa Bronze).
Dwufazowe pobieranie (List -> Detail), ekstrakcja Schema.org JSON-LD i DOM fallback.
"""
import urllib.request
import re
import json
import time
import random
from src.db import DatabaseManager

class MorizonProvider:
    def __init__(self, config, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()
        self.max_pages = 5
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'no-cache',
            'Pragma': 'no-cache',
            'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1'
        }

    def normalize_slug(self, text):
        """
        Konwertuje nazwy miast i dzielnic na poprawne slugi Morizon (usuwa polskie znaki diakrytyczne).
        """
        if not text:
            return ""
        trans = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
        normalized = text.translate(trans).lower().strip()
        normalized = re.sub(r'[^a-z0-9]+', '-', normalized).strip('-')
        return normalized

    def build_search_url(self, city, district=None, page=1):
        """
        Buduje adres URL wyszukiwania Morizon z tablicowymi parametrami ps[...] oraz paginacją.
        """
        city_slug = self.normalize_slug(city) if city else "warszawa"
        district_slug = self.normalize_slug(district) if district else ""

        if district_slug:
            base_url = f"https://www.morizon.pl/mieszkania/sprzedaz/{city_slug}/{district_slug}/"
        else:
            base_url = f"https://www.morizon.pl/mieszkania/sprzedaz/{city_slug}/"

        params = []
        if self.config:
            if getattr(self.config, 'min_price', None) is not None:
                params.append(f"ps[price_from]={int(self.config.min_price)}")
            if getattr(self.config, 'max_price', None) is not None:
                params.append(f"ps[price_to]={int(self.config.max_price)}")
            if getattr(self.config, 'min_rooms', None) is not None:
                params.append(f"ps[number_of_rooms_from]={int(self.config.min_rooms)}")
            if getattr(self.config, 'max_rooms', None) is not None:
                params.append(f"ps[number_of_rooms_to]={int(self.config.max_rooms)}")
            if getattr(self.config, 'min_area', None) is not None:
                params.append(f"ps[living_area_from]={int(self.config.min_area)}")
            if getattr(self.config, 'max_area', None) is not None:
                params.append(f"ps[living_area_to]={int(self.config.max_area)}")
            if getattr(self.config, 'market_type', None) and str(self.config.market_type).lower() != "dowolny":
                market_val = self.normalize_slug(str(self.config.market_type))
                params.append(f"ps[market_type]={market_val}")

        if page > 1:
            params.append(f"page={page}")

        if params:
            return f"{base_url}?{'&'.join(params)}"
        return base_url

    def parse_listing_detail(self, html_d, detail_url, default_city="Warszawa", default_district="Ursynów"):
        """
        Parsuje stronę szczegółów oferty wyciągając JSON-LD Schema.org oraz selektory DOM fallback.
        Zwraca krotkę (external_id, raw_payload).
        """
        # Ekstrakcja ID z URL
        clean_url = detail_url.split('?')[0].split('#')[0].rstrip('/')
        last_segment = clean_url.split('/')[-1]
        m = re.search(r'(?:mz|morizon[-_]?)?(\d+)[^0-9]*$', last_segment, re.IGNORECASE)
        if m:
            raw_id = m.group(1)
        else:
            raw_id = last_segment if last_segment else str(hash(detail_url) % 10000000)
        ext_id = f"morizon_{raw_id}" if not str(raw_id).startswith("morizon_") else str(raw_id)

        # 1. Ekstrakcja Schema.org JSON-LD
        json_lds = re.findall(r'<script [^>]*type=[\'"]application/ld\+json[\'"][^>]*>(.*?)</script>', html_d, re.DOTALL)
        
        main_ld = {}
        offer_ld = {}
        place_ld = {}
        raw_json_ld_list = []

        for j in json_lds:
            try:
                data_j = json.loads(j.strip())
                raw_json_ld_list.append(data_j)
                graph = data_j.get('@graph', [data_j]) if isinstance(data_j, dict) else (data_j if isinstance(data_j, list) else [])
                for node in graph:
                    if not isinstance(node, dict):
                        continue
                    node_type = node.get('@type', '')
                    if node_type in ['Apartment', 'SingleFamilyResidence', 'House', 'Product', 'RealEstateListing', 'Accommodation']:
                        main_ld = node
                    elif node_type == 'Offer':
                        offer_ld = node
                    elif node_type == 'Place':
                        place_ld = node
            except Exception:
                pass

        # Jeśli offer lub place są zagnieżdżone w main_ld
        if not offer_ld and isinstance(main_ld.get('offers'), dict):
            offer_ld = main_ld.get('offers')
        elif not offer_ld and isinstance(main_ld.get('offers'), list) and len(main_ld.get('offers')) > 0:
            offer_ld = main_ld.get('offers')[0]

        # Tytuł
        title = main_ld.get('name') or main_ld.get('headline') or place_ld.get('name')
        if not title:
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_d, re.DOTALL | re.IGNORECASE)
            title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else f"Mieszkanie {default_city} {default_district}"

        # Cena
        price_val = None
        if offer_ld.get('price'):
            try:
                price_val = float(str(offer_ld.get('price')).replace(' ', '').replace(',', '.'))
            except (ValueError, TypeError):
                pass
        if price_val is None and main_ld.get('price'):
            try:
                price_val = float(str(main_ld.get('price')).replace(' ', '').replace(',', '.'))
            except (ValueError, TypeError):
                pass
        if price_val is None:
            price_match = re.search(r'(\d+[\s\d]*)\s*zł', html_d, re.IGNORECASE)
            if price_match:
                try:
                    price_val = float(re.sub(r'\s+', '', price_match.group(1)))
                except (ValueError, TypeError):
                    pass

        # Metraż (area_m2)
        area_val = None
        floor_size = main_ld.get('floorSize')
        if isinstance(floor_size, dict):
            area_val = floor_size.get('value')
        elif isinstance(floor_size, (int, float, str)):
            area_val = floor_size
        if area_val:
            try:
                area_val = float(str(area_val).replace(',', '.'))
            except (ValueError, TypeError):
                area_val = None

        if area_val is None:
            area_match = re.search(r'(\d+(?:[.,]\d+)?)\s*m[²2]', html_d, re.IGNORECASE)
            if area_match:
                try:
                    area_val = float(area_match.group(1).replace(',', '.'))
                except (ValueError, TypeError):
                    pass

        # Liczba pokoi (rooms)
        rooms_val = None
        if main_ld.get('numberOfRooms'):
            try:
                rooms_val = int(main_ld.get('numberOfRooms'))
            except (ValueError, TypeError):
                pass
        if rooms_val is None:
            rooms_match = re.search(r'(\d+)\s*pok', html_d, re.IGNORECASE)
            if rooms_match:
                try:
                    rooms_val = int(rooms_match.group(1))
                except (ValueError, TypeError):
                    pass

        # Piętro (floor)
        floor_val = None
        if re.search(r'\bparter\b', html_d, re.IGNORECASE):
            floor_val = 0
        else:
            floor_match = (
                re.search(r'piętro\s*:\s*(\d+)', html_d, re.IGNORECASE) or
                re.search(r'(\d+)\s*\.?\s*piętro', html_d, re.IGNORECASE) or
                re.search(r'piętro\s*(\d+)', html_d, re.IGNORECASE)
            )
            if floor_match:
                try:
                    floor_val = int(floor_match.group(1))
                except (ValueError, TypeError):
                    pass

        # Całkowita liczba pięter (total_floors)
        total_floors_val = None
        if main_ld.get('numberOfStories'):
            try:
                total_floors_val = int(main_ld.get('numberOfStories'))
            except (ValueError, TypeError):
                pass

        if total_floors_val is None:
            total_floors_match = (
                re.search(r'liczba\s*pięter\s*:\s*(\d+)', html_d, re.IGNORECASE) or
                re.search(r'piętro\s*\d+\s*z\s*(\d+)', html_d, re.IGNORECASE) or
                re.search(r'(?:z\s*|budynek\s*\d+\s*z\s*)(\d+)\s*pięt', html_d, re.IGNORECASE) or
                re.search(r'(\d+)\s*[- ]piętrow', html_d, re.IGNORECASE)
            )
            if total_floors_match:
                try:
                    total_floors_val = int(total_floors_match.group(1))
                except (ValueError, TypeError):
                    pass

        # Winda (has_elevator)
        has_elevator = 0
        elevator_patterns = [
            r'winda\s*:\s*tak',
            r'winda\s*:\s*1',
            r'\"elevator\"\s*:\s*true',
            r'\"elevator\"\s*:\s*1',
            r'\bwindą\b',
            r'\bwinda\b',
            r'dźwig\s*osobowy'
        ]
        html_lower = html_d.lower()
        if any(re.search(pat, html_lower) for pat in elevator_patterns):
            has_elevator = 1

        # Rok budowy (build_year)
        build_year = None
        year_match = re.search(r'(?:rok budowy\s*:\s*|rok budowy\s*|z\s*)(\d{4})(?:\s*roku|\s*r\.|\b)', html_d, re.IGNORECASE)
        if year_match:
            try:
                y = int(year_match.group(1))
                if 1900 <= y <= 2035:
                    build_year = y
            except (ValueError, TypeError):
                pass

        # Typ ogłoszeniodawcy (seller_type)
        seller_type = "Agencja"
        if re.search(r'\b(?:bez pośredników|prywatne|oferta bezpośrednia|ogłoszenie prywatne)\b', html_lower):
            seller_type = "Bezpośrednio"

        # Opis (description_text)
        description_text = main_ld.get('description') or place_ld.get('description') or ''
        if not description_text:
            desc_match = re.search(r'<div[^>]*class=[\'"][^\'"]*description[^\'"]*[\'"][^>]*>(.*?)</div>', html_d, re.DOTALL | re.IGNORECASE)
            if desc_match:
                description_text = re.sub(r'<[^>]+>', '', desc_match.group(1)).strip()

        # Lokalizacja i Współrzędne GPS
        lat_val = None
        lon_val = None
        geo_node = main_ld.get('geo') or place_ld.get('geo') or {}
        if isinstance(geo_node, dict):
            lat_val = geo_node.get('latitude')
            lon_val = geo_node.get('longitude')
        
        if lat_val is None or lon_val is None:
            # Fallback na atrybuty data-lat / data-lng lub regex
            lat_match = re.search(r'data-lat=[\'"]([0-9\.]+)[\'"]', html_d, re.IGNORECASE) or re.search(r'latitude\s*:\s*([0-9\.]+)', html_d, re.IGNORECASE)
            lon_match = re.search(r'data-lng=[\'"]([0-9\.]+)[\'"]', html_d, re.IGNORECASE) or re.search(r'longitude\s*:\s*([0-9\.]+)', html_d, re.IGNORECASE)
            if lat_match:
                lat_val = lat_match.group(1)
            if lon_match:
                lon_val = lon_match.group(1)

        try:
            lat_val = float(lat_val) if lat_val is not None else None
            lon_val = float(lon_val) if lon_val is not None else None
        except (ValueError, TypeError):
            lat_val, lon_val = None, None

        # Dzielnica i Ulica
        address_node = main_ld.get('address') or place_ld.get('address') or {}
        city_val = default_city
        district_val = default_district
        street_val = ""

        if isinstance(address_node, dict):
            if address_node.get('addressLocality'):
                city_val = address_node.get('addressLocality')
            if address_node.get('addressRegion'):
                district_val = address_node.get('addressRegion')
            if address_node.get('streetAddress'):
                street_val = address_node.get('streetAddress')

        raw_payload = {
            "id": ext_id,
            "title": title,
            "url": detail_url,
            "price_pln": price_val,
            "area_m2": area_val,
            "rooms": rooms_val,
            "floor": floor_val,
            "total_floors": total_floors_val,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "description_text": description_text,
            "location": {
                "city": city_val,
                "district": district_val,
                "street": street_val,
                "coordinates": {
                    "latitude": lat_val,
                    "longitude": lon_val
                }
            },
            "raw_json_ld": raw_json_ld_list
        }

        return ext_id, raw_payload

    def fetch_listings(self, run_id=None):
        """
        Pobiera strumień ogłoszeń z serwisu Morizon.pl dla zdefiniowanych w kryteriach dzielnic.
        Zapisuje surowe obiekty do bronze_listings oraz metrykę audytową do run_audit.
        """
        city = self.config.city if self.config and self.config.city else "Warszawa"
        districts = self.config.districts if self.config and self.config.districts else ["Ursynów"]

        saved_count = 0
        total_expected_morizon = 0

        for district in districts:
            district_slug = self.normalize_slug(district)
            chunk_name = f"{self.normalize_slug(city)}_{district_slug}_morizon"
            district_expected = None
            district_saved = 0

            page = 1
            while page <= self.max_pages:
                search_url = self.build_search_url(city, district, page=page)
                req = urllib.request.Request(search_url, headers=self.headers)

                try:
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        html = resp.read().decode('utf-8')

                    # Ekstrakcja liczby ofert z nagłówka
                    if district_expected is None:
                        m_total = re.search(r'(\d+[\s\d]*)\s*(?:ogłoszeń|ofert|wyników|mieszkań)', html, re.IGNORECASE)
                        if m_total:
                            cleaned_num = re.sub(r'\s+', '', m_total.group(1))
                            if cleaned_num.isdigit():
                                district_expected = int(cleaned_num)
                                total_expected_morizon += district_expected

                    # Ekstrakcja odnośników do ofert
                    href_matches = re.findall(r'href=[\'"](https?://(?:www\.)?morizon\.pl)?(/oferta/[^\'"]+)[\'"]', html, re.IGNORECASE)
                    unique_hrefs = []
                    for _, path_part in href_matches:
                        clean_path = path_part.split('?')[0].split('#')[0]
                        if clean_path.startswith('/oferta/') and clean_path not in unique_hrefs:
                            unique_hrefs.append(clean_path)

                    if not unique_hrefs:
                        break

                    for clean_href in unique_hrefs:
                        detail_url = "https://www.morizon.pl" + clean_href if not clean_href.startswith("http") else clean_href
                        try:
                            req_d = urllib.request.Request(detail_url, headers=self.headers)
                            with urllib.request.urlopen(req_d, timeout=5) as resp_d:
                                html_d = resp_d.read().decode('utf-8')

                            ext_id, raw_payload = self.parse_listing_detail(html_d, detail_url, default_city=city, default_district=district)

                            self.db_manager.insert_bronze_listing(
                                source_portal="morizon",
                                external_id=ext_id,
                                city=city,
                                chunk_name=chunk_name,
                                raw_payload=raw_payload,
                                run_id=run_id
                            )
                            saved_count += 1
                            district_saved += 1

                            # Politeness delay
                            time.sleep(random.uniform(0.15, 0.25))

                        except Exception as e_d:
                            print(f"Błąd pobierania szczegółów Morizon ({detail_url}): {e_d}")

                except Exception as e:
                    print(f"Błąd pobierania listy Morizon dla {district} (strona {page}): {e}")
                    break

                if district_expected and district_saved >= district_expected:
                    break

                page += 1

        if total_expected_morizon > 0 and run_id:
            self.db_manager.save_run_audit(run_id, "morizon", total_expected_morizon, saved_count)
        elif run_id:
            # W przypadku braku nagłówka expected zapisujemy liczbę pobraną
            self.db_manager.save_run_audit(run_id, "morizon", saved_count, saved_count)

        return saved_count
