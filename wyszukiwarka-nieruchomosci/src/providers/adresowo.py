"""
Provider pobierający surowe oferty z serwisu Adresowo.pl (Warstwa Bronze).
Wyciąga ustrukturyzowane metadane z JSON-LD oraz właściwości HTML.
"""
import urllib.request
import re
import json
import time
from src.db import DatabaseManager

class AdresowoProvider:
    def __init__(self, config, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()
        self.max_pages = 5

    def fetch_listings(self, run_id=None):
        city = self.config.city if self.config.city else "Warszawa"
        city_slug = city.lower()
        districts = self.config.districts if self.config.districts else ["Ursynów"]

        saved_count = 0
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pl-PL,pl;q=0.9,en;q=0.8'
        }

        for district in districts:
            district_slug = district.lower().replace('ó', 'o').replace('ł', 'l').replace('ś', 's').replace('ż', 'z').replace('ź', 'z')
            district_slug_q = f"{district_slug}-Q"
            chunk_name = f"{city_slug}_{district_slug}_adresowo"

            for page in range(1, self.max_pages + 1):
                page_suffix = f"_l{page}" if page > 1 else ""
                url = f"https://adresowo.pl/mieszkania/{city_slug}/{district_slug_q}/{page_suffix}"
                req = urllib.request.Request(url, headers=headers)

                try:
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        html = resp.read().decode('utf-8')

                    # Odnośniki do konkretnych ofert /o/...
                    offer_hrefs = list(set(re.findall(r'href=\"(/o/[^\"]+)\"', html)))
                    
                    for clean_href in offer_hrefs:
                        ext_id = clean_href.split('/')[-1]
                        detail_url = "https://adresowo.pl" + clean_href

                        try:
                            req_d = urllib.request.Request(detail_url, headers=headers)
                            with urllib.request.urlopen(req_d, timeout=5) as resp_d:
                                html_d = resp_d.read().decode('utf-8')

                            # Wyciągamy JSON-LD (Place i Offer)
                            json_lds = re.findall(r'<script [^>]*type=\"application/ld\+json\"[^>]*>(.*?)</script>', html_d, re.DOTALL)
                            offer_ld = {}
                            place_ld = {}
                            for j in json_lds:
                                try:
                                    data_j = json.loads(j)
                                    graph = data_j.get('@graph', [data_j])
                                    for node in graph:
                                        if node.get('@type') == 'Offer':
                                            offer_ld = node
                                        elif node.get('@type') == 'Place':
                                            place_ld = node
                                except Exception:
                                    pass

                            # Wyciągamy czyste znaczniki tekstu
                            spans = re.findall(r'<span[^>]*>(.*?)</span>', html_d, re.DOTALL)
                            clean_spans = [re.sub(r'<[^>]+>', '', s).strip() for s in spans if s.strip()]

                            # Parsowanie roku budowy
                            build_year = None
                            for idx, s in enumerate(clean_spans):
                                if s.lower() == 'rok budowy' and idx > 0 and clean_spans[idx-1].isdigit():
                                    build_year = int(clean_spans[idx-1])

                            # Winda
                            has_elevator = 1 if any('winda' in s.lower() for s in clean_spans) or 'winda' in html_d.lower() else 0

                            # Typ ogłoszeniodawcy (bez pośredników = Bezpośrednio)
                            seller_type = "Bezpośrednio" if any("bez pośredników" in s.lower() for s in clean_spans) else "Agencja"

                            # Metraż, pokoje, piętro i dzielnica z tytułu JSON-LD Place
                            name_str = place_ld.get('name', '')
                            district_val = district
                            dist_match = re.search(r'Warszawa\s+([^,]+)', name_str, re.IGNORECASE)
                            if dist_match:
                                district_val = dist_match.group(1).strip()

                            floor_match = re.search(r'(\d+)\s*piętro', name_str, re.IGNORECASE)
                            floor_val = int(floor_match.group(1)) if floor_match else None
                            if 'parter' in name_str.lower():
                                floor_val = 0

                            area_match = re.search(r'(\d+([.,]\d+)?)\s*m²', name_str, re.IGNORECASE)
                            area_val = float(area_match.group(1).replace(',', '.')) if area_match else None

                            rooms_match = re.search(r'(\d+)\s*pok', name_str, re.IGNORECASE)
                            rooms_val = int(rooms_match.group(1)) if rooms_match else None

                            # Całkowita liczba pięter w budynku
                            total_floors_match = re.search(r'piętro\s*z\s*(\d+)', html_d, re.IGNORECASE)
                            total_floors_val = int(total_floors_match.group(1)) if total_floors_match else None

                            raw_payload = {
                                "id": ext_id,
                                "title": name_str or f"Mieszkanie {city} {district_val}",
                                "url": detail_url,
                                "price_pln": float(offer_ld.get('price', 0)) if offer_ld.get('price') else None,
                                "area_m2": area_val,
                                "rooms": rooms_val,
                                "floor": floor_val,
                                "total_floors": total_floors_val,
                                "has_elevator": has_elevator,
                                "build_year": build_year,
                                "seller_type": seller_type,
                                "description_text": place_ld.get('description', ''),
                                "location": {
                                    "city": city,
                                    "district": district_val,
                                    "street": place_ld.get('address', {}).get('streetAddress', ''),
                                    "coordinates": {
                                        "latitude": place_ld.get('geo', {}).get('latitude'),
                                        "longitude": place_ld.get('geo', {}).get('longitude')
                                    }
                                },
                                "place_ld": place_ld,
                                "offer_ld": offer_ld
                            }

                            self.db_manager.insert_bronze_listing(
                                source_portal="adresowo",
                                external_id=ext_id,
                                city=city,
                                chunk_name=chunk_name,
                                raw_payload=raw_payload,
                                run_id=run_id
                            )
                            saved_count += 1
                            time.sleep(0.05)

                        except Exception as e_d:
                            print(f"Błąd pobierania szczegółów Adresowo {ext_id}: {e_d}")

                except Exception as e:
                    print(f"Błąd pobierania listy Adresowo dla {district} (strona {page}): {e}")

        return saved_count
