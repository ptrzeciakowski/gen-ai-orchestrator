"""
Provider dla serwisów z przewagą ofert bezpośrednich od właścicieli (Adresowo, Sprzedajemy, Lento).
"""

class DirectProvider:
    def __init__(self, config):
        self.config = config

    def fetch_listings(self):
        listings = []
        sample_direct = [
            ("BEZ POŚREDNIKÓW! Wykończone mieszkanie 2-pok", "Mokotów", 49.0, 715000, 2, 2, "Adresowo.pl", "Bezpośrednio"),
            ("Prywatnie: Ustawne 3 pokoje na Ursynowie z KW", "Ursynów", 61.5, 840000, 3, 4, "Sprzedajemy.pl", "Bezpośrednio"),
            ("Sprzedam bezpośrednio mieszkanie po odświeżeniu", "Ochota", 53.0, 765000, 2, 3, "Lento.pl", "Bezpośrednio"),
            ("Bezpośrednio od pierwszego właściciela Wola Metro", "Wola", 55.0, 860000, 2, 2, "Adresowo.pl", "Bezpośrednio"),
        ]

        for idx, (title, district, area, price, rooms, floor, source, seller) in enumerate(sample_direct, start=101):
            if district in self.config.districts:
                price_per_m2 = round(price / area, 2)
                if price <= self.config.max_price and price_per_m2 <= self.config.max_price_per_m2:
                    listings.append({
                        "id": f"dir-{idx}",
                        "title": title,
                        "district": district,
                        "area_m2": area,
                        "price_pln": price,
                        "price_per_m2": price_per_m2,
                        "rooms": rooms,
                        "floor": floor,
                        "source": source,
                        "seller_type": seller,
                        "url": f"https://www.{source.lower()}/oferta/{district.lower()}-{idx}"
                    })
        return listings
