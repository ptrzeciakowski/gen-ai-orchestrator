"""
Provider dla głównych portalów nieruchomościowych (Otodom, OLX, Morizon).
Generuje lub odczytuje zebrane oferty dopasowane do kryteriów.
"""
import random

class CommercialProvider:
    def __init__(self, config):
        self.config = config

    def fetch_listings(self):
        listings = []
        sources = ["Otodom.pl", "OLX.pl", "Morizon.pl"]
        
        sample_titles = [
            ("Słoneczne 2 pokoje przy stacji metra Mokotów", "Mokotów", 52.5, 780000, 2, 3, "Otodom.pl", "Agencja"),
            ("Wykończone mieszkanie 3-pokojowe z tarasem", "Ursynów", 64.0, 890000, 3, 2, "Otodom.pl", "Agencja"),
            ("Rozkładowe mieszkanie po remoncie blisko Parku", "Ochota", 48.0, 720000, 2, 4, "OLX.pl", "Bezpośrednio"),
            ("Modernistyczne mieszkanie w sercu Woli", "Wola", 58.0, 920000, 3, 5, "Otodom.pl", "Agencja"),
            ("Przestronny apartament przy Parku Żeromskiego", "Żoliborz", 68.0, 945000, 3, 3, "Morizon.pl", "Agencja"),
            ("Ciche mieszkanie 2-pokojowe z miejscem w garażu", "Bemowo", 50.0, 695000, 2, 1, "OLX.pl", "Bezpośrednio"),
        ]

        for idx, (title, district, area, price, rooms, floor, source, seller) in enumerate(sample_titles, start=1):
            if district in self.config.districts:
                price_per_m2 = round(price / area, 2)
                if price <= self.config.max_price and price_per_m2 <= self.config.max_price_per_m2:
                    listings.append({
                        "id": f"comm-{idx}",
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
