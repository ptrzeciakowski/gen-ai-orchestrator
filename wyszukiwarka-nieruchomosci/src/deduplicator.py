"""
Moduł deduplikacji i konsolidacji ofert nieruchomości pochodzących z różnych źródeł (Otodom, OLX, Adresowo).
Odczytuje zdeduplikowane i pogrupowane rekordy z widoku gold_listings bazy danych SQLite.
"""
from src.db import DatabaseManager

class Deduplicator:
    def __init__(self, db_manager=None):
        self.db_manager = db_manager or DatabaseManager()

    def get_gold_listings(self):
        """
        Pobiera zdeduplikowane oferty bezpośrednio z widoku gold_listings.
        """
        conn = self.db_manager.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gold_listings;")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()

    def deduplicate(self, listings=None):
        """
        Zwraca zdeduplikowaną listę ofert na bazie widoku gold_listings.
        """
        if listings is not None and len(listings) > 0:
            unique_dict = {}
            for item in listings:
                key = f"{item.get('district')}_{round(float(item.get('area_m2', 0)), 0)}_{item.get('rooms')}_{item.get('floor')}"
                if key not in unique_dict or (item.get("seller_type") == "Bezpośrednio" and unique_dict[key].get("seller_type") != "Bezpośrednio"):
                    unique_dict[key] = item
            return list(unique_dict.values())
        
        return self.get_gold_listings()
