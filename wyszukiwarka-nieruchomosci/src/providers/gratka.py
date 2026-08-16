"""
Provider pobierający surowe oferty z serwisu Gratka.pl (Warstwa Bronze).
Dwufazowa ekstrakcja (List + Detail) z buforem czasowym, pełnym zestawem nagłówków Chromium macOS
oraz pre-normalizacją kluczy pierwszego poziomu w raw_payload.
"""
import urllib.request
import urllib.error
import re
import json
import time
from typing import Optional, List, Dict, Any, Tuple
from src.db import DatabaseManager

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}

def slugify(text: str) -> str:
    """
    Konwertuje tekst z polskimi znakami diakrytycznymi na bezpieczny slug URL.
    """
    if not text:
        return ""
    trans = str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')
    s = text.translate(trans).lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s

class GratkaProvider:
    def __init__(self, config, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()
        self.max_pages = 5
        self.request_timeout = 10
        self.delay_between_details = 0.20

    def build_search_url(self, city_slug: str, district_slug: str, page: int = 1) -> str:
        """
        Buduje URL wyszukiwania na Gratka.pl (szeroki zrzut dla danej lokalizacji).
        """
        c_slug = slugify(city_slug) or "warszawa"
        d_slug = slugify(district_slug)
        if d_slug:
            base = f"https://gratka.pl/nieruchomosci/mieszkania/{c_slug}/{d_slug}/sprzedaz"
        else:
            base = f"https://gratka.pl/nieruchomosci/mieszkania/{c_slug}/sprzedaz"

        if page > 1:
            return f"{base}?page={page}"
        return base

    def parse_listing_page(self, html: str) -> Tuple[Optional[int], List[Dict[str, str]]]:
        """
        Ekstrahuje całkowitą liczbę ogłoszeń z nagłówka oraz odnośniki do ofert ze strony listy.
        Zwraca (expected_total, list_of_offers_info).
        """
        expected_total = None
        # Wyciąganie całkowitej liczby ofert z nagłówka h1 lub tekstu strony
        header_match = re.search(r'<h1[^>]*>.*?(\d+[\s\d\xa0]*)\s*(?:ogłoszeń|ogłoszenia|ofert).*?</h1>', html, re.DOTALL | re.IGNORECASE)
        if not header_match:
            header_match = re.search(r'(\d+[\s\d\xa0]*)\s*(?:ogłoszeń|ogłoszenia|ofert)', html, re.IGNORECASE)
        if header_match:
            raw_num = header_match.group(1).replace(' ', '').replace('\xa0', '').strip()
            if raw_num.isdigit():
                expected_total = int(raw_num)

        # Odnośniki do ofert z formatem /ob/<id> lub /ob-<id>
        offers = []
        seen_ids = set()

        # Wzorzec 1: standardowe odnośniki href="/nieruchomosci/.../ob/12345"
        matches = re.findall(r'href=[\"\']((?:https?://gratka\.pl)?/nieruchomosci/[^\"\']*/ob[/-](\d+)[^\"\']*)[\"\']', html, re.IGNORECASE)
        for href, ext_id in matches:
            if ext_id not in seen_ids:
                seen_ids.add(ext_id)
                full_url = href if href.startswith('http') else f"https://gratka.pl{href}"
                offers.append({"id": ext_id, "url": full_url})

        # Wzorzec 2: fallback na dowolny link z /ob/ w ścieżce
        if not offers:
            generic_matches = re.findall(r'href=[\"\']((?:https?://gratka\.pl)?/nieruchomosci/[^\"\']+/ob/([a-zA-Z0-9_-]+))[\"\']', html, re.IGNORECASE)
            for href, ext_id in generic_matches:
                if ext_id not in seen_ids:
                    seen_ids.add(ext_id)
                    full_url = href if href.startswith('http') else f"https://gratka.pl{href}"
                    offers.append({"id": ext_id, "url": full_url})

        return expected_total, offers

    def parse_detail_page(self, html: str, detail_url: str, ext_id: str, default_district: str = "Ursynów") -> Dict[str, Any]:
        """
        Parsuje stronę szczegółów ogłoszenia Gratka.pl:
        Ekstrahuje JSON-LD, tabelę parametrów/cech oraz pre-normalizuje słownik raw_payload.
        """
        # 1. Parsowanie JSON-LD
        json_lds = re.findall(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', html, re.DOTALL | re.IGNORECASE)
        offer_ld = {}
        place_ld = {}
        all_json_ld = []

        for j_str in json_lds:
            try:
                data_j = json.loads(j_str.strip())
                all_json_ld.append(data_j)
                graph = data_j.get('@graph', [data_j]) if isinstance(data_j, dict) else (data_j if isinstance(data_j, list) else [])
                for node in graph:
                    if not isinstance(node, dict):
                        continue
                    node_type = node.get('@type', '')
                    if node_type in ('Offer', 'AggregateOffer'):
                        offer_ld = node
                    elif node_type in ('Place', 'Apartment', 'SingleFamilyResidence', 'Product', 'RealEstateListing', 'Residence', 'Accommodation'):
                        place_ld = node
                        if not offer_ld and 'offers' in node and isinstance(node['offers'], dict):
                            offer_ld = node['offers']
            except Exception:
                pass

        # 2. Ekstrakcja parametrów/cech z HTML (tabela, listy definicji lub span/div)
        features_dict = {}
        # Wzorzec list parametrów np. <li><span>Piętro</span><b>3/10</b></li> lub <dt>/<dd>
        param_pairs = re.findall(r'<(?:li|div|dt|span)[^>]*class=[\"\'][^\"\']*(?:parameter|feature|attribute)[^\"\']*[\"\'][^>]*>.*?<(?:span|dt|b|p)[^>]*>(.*?)</(?:span|dt|b|p)>.*?<(?:b|dd|span|p)[^>]*>(.*?)</(?:b|dd|span|p)>', html, re.DOTALL | re.IGNORECASE)
        for label, val in param_pairs:
            clean_label = re.sub(r'<[^>]+>', '', label).strip().lower().replace(':', '')
            clean_val = re.sub(r'<[^>]+>', '', val).strip()
            if clean_label and clean_val:
                features_dict[clean_label] = clean_val

        # Fallback regex dla par klucz-wartość w tekście
        if not features_dict:
            generic_pairs = re.findall(r'<(?:span|b|dt)[^>]*>([^<:]+):?\s*</(?:span|b|dt)>\s*<(?:span|b|dd)[^>]*>([^<]+)</(?:span|b|dd)>', html, re.IGNORECASE)
            for label, val in generic_pairs:
                clean_l = label.strip().lower()
                clean_v = val.strip()
                if len(clean_l) < 30 and clean_v:
                    features_dict[clean_l] = clean_v

        # 3. Tytuł ogłoszenia
        title = place_ld.get('name') or offer_ld.get('name')
        if not title:
            h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL | re.IGNORECASE)
            title = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else f"Mieszkanie Warszawa {default_district}"

        # 4. Cena PLN
        price_val = None
        if offer_ld.get('price'):
            try:
                price_val = float(offer_ld['price'])
            except (ValueError, TypeError):
                pass
        if price_val is None:
            for k in ('cena', 'cena całkowita', 'price'):
                if k in features_dict:
                    clean_p = re.sub(r'[^\d.]', '', features_dict[k].replace(',', '.').replace(' ', '').replace('\xa0', ''))
                    if clean_p:
                        try:
                            price_val = float(clean_p)
                            break
                        except ValueError:
                            pass
        if price_val is None:
            price_match = re.search(r'class=[\"\'][^\"\']*price[^\"\']*[\"\'][^>]*>.*?([\d\s\xa0]+(?:[.,]\d+)?)\s*zł', html, re.DOTALL | re.IGNORECASE)
            if price_match:
                clean_p = price_match.group(1).replace(' ', '').replace('\xa0', '').replace(',', '.')
                try:
                    price_val = float(clean_p)
                except ValueError:
                    pass

        # 5. Powierzchnia m²
        area_val = None
        for k, v in features_dict.items():
            if 'powierzchnia' in k or 'metraż' in k or 'area' in k:
                m_area = re.search(r'(\d+([.,]\d+)?)', v)
                if m_area:
                    try:
                        area_val = float(m_area.group(1).replace(',', '.'))
                        break
                    except ValueError:
                        pass
        if area_val is None:
            if place_ld.get('floorSize', {}).get('value'):
                try:
                    area_val = float(place_ld['floorSize']['value'])
                except (ValueError, TypeError):
                    pass
            elif place_ld.get('floorSize'):
                m_area = re.search(r'(\d+([.,]\d+)?)', str(place_ld['floorSize']))
                if m_area:
                    area_val = float(m_area.group(1).replace(',', '.'))
        if area_val is None:
            area_match = re.search(r'(\d+([.,]\d+)?)\s*m[²2]', html, re.IGNORECASE)
            if area_match:
                try:
                    area_val = float(area_match.group(1).replace(',', '.'))
                except ValueError:
                    pass

        # 6. Liczba pokoi
        rooms_val = None
        for k, v in features_dict.items():
            if 'pokoj' in k or 'pokój' in k or 'rooms' in k:
                m_rooms = re.search(r'(\d+)', v)
                if m_rooms:
                    rooms_val = int(m_rooms.group(1))
                    break
        if rooms_val is None:
            if place_ld.get('numberOfRooms'):
                try:
                    rooms_val = int(place_ld['numberOfRooms'])
                except (ValueError, TypeError):
                    pass
        if rooms_val is None:
            rooms_match = re.search(r'(\d+)\s*(?:[- ]pokojowe|pokoi|pokoje|pok\.)', title + " " + html, re.IGNORECASE)
            if rooms_match:
                rooms_val = int(rooms_match.group(1))

        # 7. Piętro i Całkowita liczba pięter
        floor_val = None
        total_floors_val = None

        for k, v in features_dict.items():
            if 'piętro' in k or 'pietro' in k or 'floor' in k:
                if 'parter' in v.lower():
                    floor_val = 0
                else:
                    m_f = re.search(r'(\d+)(?:\s*/\s*(\d+)|\s*z\s*(\d+))?', v, re.IGNORECASE)
                    if m_f:
                        floor_val = int(m_f.group(1))
                        if m_f.group(2):
                            total_floors_val = int(m_f.group(2))
                        elif m_f.group(3):
                            total_floors_val = int(m_f.group(3))
            elif 'liczba pięter' in k or 'liczba pieter' in k or 'total_floors' in k:
                m_tf = re.search(r'(\d+)', v)
                if m_tf:
                    total_floors_val = int(m_tf.group(1))

        if floor_val is None:
            if 'parter' in title.lower() or 'parter' in html.lower()[:2000]:
                floor_val = 0
            else:
                floor_match = re.search(r'(\d+)\s*piętro', title, re.IGNORECASE)
                if floor_match:
                    floor_val = int(floor_match.group(1))

        # 8. Winda (has_elevator)
        has_elevator = 0
        for k, v in features_dict.items():
            if 'winda' in k or 'elevator' in k or 'dźwig' in k:
                v_lower = str(v).lower()
                if v_lower in ('tak', 'true', '1', 'jest', 'tak / jest'):
                    has_elevator = 1
                elif v_lower in ('nie', 'false', '0', 'brak'):
                    has_elevator = 0
                else:
                    has_elevator = 1
                break
        if not has_elevator:
            # Sprawdzenie w opisie i pełnym tekście
            html_lower = html.lower()
            if 'winda' in html_lower or 'windą' in html_lower or 'windy' in html_lower:
                if 'brak windy' not in html_lower and 'bez windy' not in html_lower:
                    has_elevator = 1

        # 9. Rok budowy
        build_year = None
        for k, v in features_dict.items():
            if 'rok budowy' in k or 'rok' in k or 'build_year' in k:
                m_yr = re.search(r'(19\d{2}|20\d{2})', v)
                if m_yr:
                    build_year = int(m_yr.group(1))
                    break
        if build_year is None:
            m_yr = re.search(r'rok budowy[:\s]+(19\d{2}|20\d{2})', html, re.IGNORECASE)
            if m_yr:
                build_year = int(m_yr.group(1))

        # 10. Typ ogłoszeniodawcy (seller_type)
        seller_type = "Agencja"
        for k, v in features_dict.items():
            if 'forma' in k or 'ogłoszeniodawca' in k or 'typ' in k or 'sprzedawca' in k:
                v_lower = str(v).lower()
                if any(x in v_lower for x in ('prywatn', 'bezpośredni', 'bezposredni', 'właściciel')):
                    seller_type = "Bezpośrednio"
                    break
        if seller_type == "Agencja":
            if 'bez pośredników' in html.lower() or 'bezposrednio' in html.lower() or 'bezpośrednio' in html.lower():
                seller_type = "Bezpośrednio"

        # 11. Lokalizacja i Koordynaty GPS
        geo_node = place_ld.get('geo', {}) if isinstance(place_ld, dict) else {}
        lat = None
        lon = None
        if geo_node and isinstance(geo_node, dict):
            try:
                lat = float(geo_node.get('latitude')) if geo_node.get('latitude') is not None else None
                lon = float(geo_node.get('longitude')) if geo_node.get('longitude') is not None else None
            except (ValueError, TypeError):
                pass

        if lat is None or lon is None:
            # Szukanie w skryptach / atrybutach HTML
            geo_match = re.search(r'[\"\'](?:latitude|lat)[\"\']\s*:\s*([0-9.]+)\s*,\s*[\"\'](?:longitude|lon|lng)[\"\']\s*:\s*([0-9.]+)', html, re.IGNORECASE)
            if geo_match:
                try:
                    lat = float(geo_match.group(1))
                    lon = float(geo_match.group(2))
                except ValueError:
                    pass

        addr_node = place_ld.get('address', {}) if isinstance(place_ld, dict) else {}
        city_val = "Warszawa"
        district_val = default_district
        street_val = ""

        if isinstance(addr_node, dict):
            city_val = addr_node.get('addressLocality') or city_val
            street_val = addr_node.get('streetAddress') or ""

        # Dzielnica z adresu lub tytułu
        for d in ("Ursynów", "Mokotów", "Wilanów", "Wola", "Ochota", "Śródmieście", "Bielany", "Bemowo", "Żoliborz", "Praga-Południe", "Praga-Północ", "Targówek", "Białołęka", "Wawer", "Włochy", "Ursus", "Rembertów", "Wesoła"):
            if d.lower() in title.lower() or d.lower() in detail_url.lower():
                district_val = d
                break

        # 12. Opis tekstowy
        desc_match = re.search(r'<(?:div|section)[^>]*class=[\"\'][^\"\']*(?:description|opis)[^\"\']*[\"\'][^>]*>(.*?)</(?:div|section)>', html, re.DOTALL | re.IGNORECASE)
        description_text = ""
        if desc_match:
            description_text = re.sub(r'<[^>]+>', ' ', desc_match.group(1)).strip()
        if not description_text:
            description_text = place_ld.get('description') or offer_ld.get('description') or ""

        # Budowa znormalizowanego słownika raw_payload
        raw_payload = {
            "id": str(ext_id),
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
            "market": "wtorny",
            "location": {
                "city": city_val,
                "district": district_val,
                "street": street_val,
                "coordinates": {
                    "latitude": lat,
                    "longitude": lon
                }
            },
            "features": features_dict,
            "description_text": description_text,
            "json_ld": all_json_ld[0] if all_json_ld else (offer_ld or place_ld)
        }
        return raw_payload

    def fetch_listings(self, run_id: Optional[str] = None) -> int:
        """
        Główna metoda pobierająca szeroki strumień ogłoszeń z Gratka.pl do warstwy Bronze.
        """
        city = getattr(self.config, 'city', None) or "Warszawa"
        city_slug = slugify(city)
        districts = getattr(self.config, 'districts', None) or ["Ursynów"]

        saved_count = 0
        expected_total_gratka = None

        for district in districts:
            district_slug = slugify(district)
            chunk_name = f"{city_slug}_{district_slug}_gratka"

            page = 1
            while page <= self.max_pages:
                url = self.build_search_url(city_slug, district_slug, page=page)
                req = urllib.request.Request(url, headers=HEADERS)

                try:
                    with urllib.request.urlopen(req, timeout=self.request_timeout) as resp:
                        html = resp.read().decode('utf-8')

                    expected_total, offers = self.parse_listing_page(html)
                    if expected_total_gratka is None and expected_total is not None:
                        expected_total_gratka = expected_total

                    if not offers:
                        break

                    for offer_info in offers:
                        ext_id = offer_info["id"]
                        detail_url = offer_info["url"]

                        try:
                            req_d = urllib.request.Request(detail_url, headers=HEADERS)
                            with urllib.request.urlopen(req_d, timeout=self.request_timeout) as resp_d:
                                html_d = resp_d.read().decode('utf-8')

                            raw_payload = self.parse_detail_page(html_d, detail_url, ext_id, default_district=district)

                            self.db_manager.insert_bronze_listing(
                                source_portal="gratka",
                                external_id=str(ext_id),
                                city=city,
                                chunk_name=chunk_name,
                                raw_payload=raw_payload,
                                run_id=run_id
                            )
                            saved_count += 1
                            time.sleep(self.delay_between_details)

                        except Exception as e_d:
                            print(f"Błąd pobierania szczegółów Gratka {ext_id} ({detail_url}): {e_d}")

                except urllib.error.HTTPError as e_http:
                    print(f"Błąd HTTP {e_http.code} pobierania listy Gratka dla {district} (strona {page}): {e_http}")
                    if e_http.code in (403, 429):
                        # Exponential backoff / graceful degradation
                        time.sleep(2.0)
                    break
                except Exception as e:
                    print(f"Błąd pobierania listy Gratka dla {district} (strona {page}): {e}")
                    break

                if expected_total_gratka and saved_count >= expected_total_gratka:
                    break

                page += 1

        if expected_total_gratka is not None and run_id:
            self.db_manager.save_run_audit(
                run_id=run_id,
                source_portal="gratka",
                expected_total=expected_total_gratka,
                saved_bronze=saved_count
            )

        return saved_count
