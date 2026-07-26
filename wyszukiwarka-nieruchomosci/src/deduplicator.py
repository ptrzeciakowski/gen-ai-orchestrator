"""
Moduł deduplikacji i konsolidacji ofert nieruchomości pochodzących z różnych źródeł (Otodom, OLX, Morizon, Adresowo).
Scalanie bazuje na unikalnej kombinacji: Dzielnica + Powierzchnia m² (zaokrąglona do 1m²) + Pokoje + Piętro.
W przypadku wykrycia tej samej oferty na kilku portalach, priorytetyzowana jest wersja "Bezpośrednio" od właściciela.
"""

class Deduplicator:
    def deduplicate(self, listings):
        unique_dict = {}

        for item in listings:
            district = item.get("district", "Inna")
            try:
                area_rounded = round(float(item.get("area_m2", 0)), 0)
            except (ValueError, TypeError):
                area_rounded = 0
            
            rooms = item.get("rooms", 0)
            floor = item.get("floor", 0)
            
            key = f"{district}_{area_rounded}_{rooms}_{floor}"

            if key not in unique_dict:
                unique_dict[key] = item
            else:
                existing = unique_dict[key]
                # Jeśli nowe ogłoszenie jest bezpośrednio od właściciela, a istniejące nie – podmień na bezpośrednie
                if item.get("seller_type") == "Bezpośrednio" and existing.get("seller_type") != "Bezpośrednio":
                    unique_dict[key] = item

        return list(unique_dict.values())
