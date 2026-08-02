"""
Moduł deduplikacji i konsolidacji ofert nieruchomości pochodzących z różnych źródeł (Otodom, OLX, Adresowo).
Odczytuje zdeduplikowane i pogrupowane rekordy z widoku gold_listings bazy danych SQLite.
"""
from src.db import DatabaseManager

class Deduplicator:
    def __init__(self, config=None, db_manager=None):
        self.config = config
        self.db_manager = db_manager or DatabaseManager()

    def get_gold_listings(self, config=None):
        """
        Pobiera zdeduplikowane oferty z widoku gold_listings, nakładając filtry biznesowe z kryteria.md.
        """
        cfg = config or self.config
        conn = self.db_manager.get_connection()
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM gold_listings WHERE 1=1"
            params = []

            if cfg:
                if cfg.min_price is not None:
                    query += " AND price_pln >= ?"
                    params.append(cfg.min_price)
                if cfg.max_price is not None:
                    query += " AND price_pln <= ?"
                    params.append(cfg.max_price)
                if cfg.max_price_per_m2 is not None:
                    query += " AND price_per_m2 <= ?"
                    params.append(cfg.max_price_per_m2)
                if cfg.min_area is not None:
                    query += " AND area_m2 >= ?"
                    params.append(cfg.min_area)
                if cfg.max_area is not None:
                    query += " AND area_m2 <= ?"
                    params.append(cfg.max_area)
                if cfg.min_rooms is not None:
                    query += " AND rooms >= ?"
                    params.append(cfg.min_rooms)
                if cfg.max_rooms is not None:
                    query += " AND rooms <= ?"
                    params.append(cfg.max_rooms)
                if cfg.min_floor is not None:
                    query += " AND (floor IS NULL OR floor >= ?)"
                    params.append(cfg.min_floor)
                if cfg.max_floor is not None:
                    query += " AND (floor IS NULL OR floor <= ?)"
                    params.append(cfg.max_floor)
                if cfg.exclude_ground_floor:
                    query += " AND (floor IS NULL OR floor > 0)"
                if cfg.exclude_top_floor:
                    query += " AND (is_last_floor = 0 OR is_last_floor IS NULL)"
                if cfg.elevator:
                    query += " AND (has_elevator = 1 OR has_elevator IS NULL)"
                if cfg.seller_type and cfg.seller_type.lower() != "dowolny":
                    query += " AND seller_type LIKE ?"
                    params.append(f"%{cfg.seller_type}%")
                if cfg.districts:
                    district_conditions = []
                    for d in cfg.districts:
                        norm_d = d.translate(str.maketrans('ąćęłńóśźżĄĆĘŁŃÓŚŹŻ', 'acelnoszzACELNOSZZ')).lower()
                        district_conditions.append("(district LIKE ? OR district LIKE ?)")
                        params.append(f"%{d}%")
                        params.append(f"%{norm_d}%")
                    query += f" AND ({' OR '.join(district_conditions)})"

            query += ";"
            cursor.execute(query, params)
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
