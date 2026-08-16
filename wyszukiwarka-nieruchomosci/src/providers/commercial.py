"""
Provider pobierający surowe oferty z serwisu Otodom.pl (Warstwa Bronze).
Wdrożona strategia Extraction Chunks:
- Pobieranie szerokiego strumienia ogłoszeń dla zadanego miasta/dzielnicy.
- Zapis pełnego surowego obiektu JSON do bazy danych bronze_listings bez wstępnego odrzucania rekordów w Pythonie.
"""
import urllib.request
import re
import json
import time
from src.db import DatabaseManager

class CommercialProvider:
    def __init__(self, config, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()
        self.max_pages = 3

    def fetch_listings(self, run_id=None):
        city = self.config.city if self.config.city else "Warszawa"
        city_slug = city.lower()
        districts = self.config.districts if self.config.districts else ["Ursynów"]
        
        saved_count = 0
        expected_total_otodom = None
        
        for district in districts:
            district_slug = district.lower().replace('ó', 'o').replace('ł', 'l').replace('ś', 's').replace('ż', 'z').replace('ź', 'z')
            
            markets = ["wtorny", "pierwotny"]
            for market in markets:
                chunk_name = f"{city_slug}_{district_slug}_{market}"
                page = 1
                while page <= self.max_pages:
                    url = f"https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/{city_slug}/{district_slug}?limit=36&page={page}&market={market.upper()}"
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                        'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Sec-Ch-Ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
                        'Sec-Ch-Ua-Mobile': '?0',
                        'Sec-Ch-Ua-Platform': '"macOS"',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1'
                    }
                    req = urllib.request.Request(url, headers=headers)
                    
                    try:
                        with urllib.request.urlopen(req, timeout=10) as resp:
                            html = resp.read().decode('utf-8')

                        # Wyciąganie pełnych realnych obiektów z __NEXT_DATA__
                        m = re.search(r'<script id=\"__NEXT_DATA__\"[^>]*>(.*?)</script>', html, re.DOTALL)
                        if m:
                            data = json.loads(m.group(1))
                            search_ads = data.get('props', {}).get('pageProps', {}).get('data', {}).get('searchAds', {})
                            items = search_ads.get('items', [])
                            
                            # Ekstrakcja zadeklarowanej liczby ofert z Otodom
                            pagination_meta = search_ads.get('pagination', {})
                            if pagination_meta.get('totalCount') and expected_total_otodom is None:
                                expected_total_otodom = pagination_meta.get('totalCount')

                            if not items:
                                break
                            
                            for item in items:
                                ext_id = str(item.get('id') or item.get('slug'))
                                self.db_manager.insert_bronze_listing(
                                    source_portal="otodom",
                                    external_id=ext_id,
                                    city=city,
                                    chunk_name=chunk_name,
                                    raw_payload=item,
                                    run_id=run_id
                                )
                                saved_count += 1
                        else:
                            # Fallback na re.findall hrefs jeśli brak __NEXT_DATA__
                            matches = re.findall(r'href=\"(/pl/oferta/[^\"]+)\"', html)
                            unique_hrefs = []
                            for match_item in matches:
                                clean_m = match_item.split('?')[0]
                                if clean_m.startswith('/pl/oferta/') and clean_m not in unique_hrefs:
                                    unique_hrefs.append(clean_m)

                            for idx, clean_href in enumerate(unique_hrefs, start=1):
                                ext_id = clean_href.replace('/pl/oferta/', '').split('/')[-1]
                                raw_payload = {
                                    "id": ext_id,
                                    "title": f"Mieszkanie {city} {district}",
                                    "url": "https://www.otodom.pl" + clean_href,
                                    "slug": clean_href.replace('/pl/oferta/', ''),
                                    "market": market
                                }
                                self.db_manager.insert_bronze_listing(
                                    source_portal="otodom",
                                    external_id=ext_id,
                                    city=city,
                                    chunk_name=chunk_name,
                                    raw_payload=raw_payload,
                                    run_id=run_id
                                )
                                saved_count += 1

                    except Exception as e:
                        print(f"Błąd pobierania Otodom dla {district} ({market}, strona {page}): {e}")
                        break
                    
                    time.sleep(0.2)
                    page += 1

        if expected_total_otodom is not None and run_id:
            self.db_manager.save_run_audit(run_id, "otodom", expected_total_otodom, saved_count)

        return saved_count
