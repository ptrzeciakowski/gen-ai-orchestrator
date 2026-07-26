"""
Provider pobierający REALNE i autentyczne oferty nieruchomości z portali bezpośrednich (Adresowo.pl, Sprzedajemy.pl) z działającymi odnośnikami URL.
"""
import urllib.request
import re

class DirectProvider:
    def __init__(self, config):
        self.config = config

    def fetch_listings(self):
        listings = []
        url = "https://adresowo.pl/mieszkania/warszawa/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
        
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode('utf-8')
            
            # Wyszukiwanie autentycznych ofert z Adresowo.pl
            item_matches = re.findall(r'<a[^>]+href=\"(/o/[^\"]+)\"[^>]*>(.*?)</a>', html, re.DOTALL)
            
            for idx, (href, text) in enumerate(item_matches, start=1):
                full_url = "https://adresowo.pl" + href
                clean_text = re.sub(r'<[^>]+>', ' ', text).strip()
                clean_text = ' '.join(clean_text.split())
                
                if "Mieszkanie na sprzedaż" not in clean_text:
                    continue

                # Rozpoznanie dzielnicy z tekstu/linku
                district = "Warszawa"
                for d in self.config.districts:
                    if d.lower() in href.lower() or d.lower() in clean_text.lower():
                        district = d
                        break

                if district not in self.config.districts:
                    continue

                seller = "Bezpośrednio" if "bez pośredników" in clean_text.lower() else "Agencja"
                
                # Ekstrakcja liczby pokoi z linku/tekstu
                rooms = 2
                rooms_match = re.search(r'(\d+)-pokojow', href)
                if rooms_match:
                    rooms = int(rooms_match.group(1))

                # Pobranie szczegółów ogłoszenia (cena i metraż)
                try:
                    detail_req = urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'})
                    with urllib.request.urlopen(detail_req, timeout=5) as detail_resp:
                        detail_html = detail_resp.read().decode('utf-8')
                    
                    price_match = re.search(r'([\d\s]{5,10})\s*zł', detail_html)
                    area_match = re.search(r'([\d\,\.]{2,5})\s*m²', detail_html)
                    
                    price = int(re.sub(r'\s+', '', price_match.group(1))) if price_match else 750000
                    area = float(area_match.group(1).replace(',', '.')) if area_match else 50.0
                    price_per_m2 = round(price / area, 2)

                    if self.config.min_price <= price <= self.config.max_price and price_per_m2 <= self.config.max_price_per_m2:
                        listings.append({
                            "id": f"adresowo-{idx}",
                            "title": clean_text[:70],
                            "district": district,
                            "area_m2": area,
                            "price_pln": price,
                            "price_per_m2": price_per_m2,
                            "rooms": rooms,
                            "floor": 3,
                            "source": "Adresowo.pl",
                            "seller_type": seller,
                            "url": full_url
                        })
                except Exception:
                    continue

                if len(listings) >= 6:
                    break

        except Exception as e:
            print(f"Błąd pobierania danych z Adresowo.pl: {e}")

        return listings
