"""
Moduł deduplikacji i konsolidacji ofert pochodzących z różnych źródeł.
"""

class Deduplicator:
    def deduplicate(self, listings):
        unique_listings = []
        seen_keys = set()

        for item in listings:
            # Tworzenie klucza unikalnego na podstawie: dzielnica, pow. (+/- 0.5 m2), pokoje, piętro
            area_rounded = round(item["area_m2"], 0)
            key = f"{item['district']}_{area_rounded}_{item['rooms']}_{item['floor']}"

            if key not in seen_keys:
                seen_keys.add(key)
                unique_listings.append(item)
            else:
                # Jeśli trafiamy na duplikat, to jeśli nowy jest Bezpośrednio a stary Agencja - nadpisujemy
                for idx, existing in enumerate(unique_listings):
                    existing_key = f"{existing['district']}_{round(existing['area_m2'], 0)}_{existing['rooms']}_{existing['floor']}"
                    if existing_key == key:
                        if item["seller_type"] == "Bezpośrednio" and existing["seller_type"] == "Agencja":
                            unique_listings[idx] = item
                        break

        return unique_listings
