"""
Moduł zarządzania bazą danych SQLite dla architektury ELT (Bronze / Silver / Gold).
Rozszerzenie JSON1 oraz rejestracja customowych funkcji geolokalizacyjnych i regex.
"""
import os
import sqlite3
import math
import re
import json

def haversine_m(lat1, lon1, lat2, lon2):
    """
    Oblicza odległość ortodromiczną w metrach między dwoma punktami na Ziemi.
    """
    if None in (lat1, lon1, lat2, lon2):
        return None
    try:
        lat1, lon1, lat2, lon2 = float(lat1), float(lon1), float(lat2), float(lon2)
    except (ValueError, TypeError):
        return None
    
    R = 6371000.0  # Promień Ziemi w metrach
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 1)

def regexp(pattern, text):
    """
    Sprawdza czy tekst pasuje do wzorca regex.
    """
    if text is None or pattern is None:
        return False
    return bool(re.search(pattern, str(text), re.IGNORECASE))

class DatabaseManager:
    def __init__(self, db_path=None):
        if db_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            db_path = os.path.join(base_dir, "data", "listings.db")
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def get_connection(self):
        """
        Tworzy połączenie z bazą SQLite i rejestruje funkcje pomocnicze.
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        conn.create_function("haversine_m", 4, haversine_m)
        conn.create_function("regexp", 2, regexp)
        return conn

    def init_db(self):
        """
        Inicjalizuje schemat bazy danych: tabela bronze_listings oraz widoki silver_listings i gold_listings.
        """
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            
            # 1. Tabela Bronze
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS bronze_listings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_portal TEXT NOT NULL,
                external_id TEXT NOT NULL,
                city TEXT NOT NULL DEFAULT 'Warszawa',
                chunk_name TEXT,
                raw_payload JSON NOT NULL,
                scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(source_portal, external_id) ON CONFLICT REPLACE
            );
            """)
            
            cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_bronze_source_ext 
            ON bronze_listings(source_portal, external_id);
            """)

            # 2. Widok Silver (MVP Opcja 1: JSON1 Views)
            cursor.execute("""
            CREATE VIEW IF NOT EXISTS silver_listings AS
            WITH extracted_data AS (
                SELECT 
                    b.id AS bronze_id,
                    b.source_portal,
                    b.external_id,
                    b.scraped_at,
                    json_extract(b.raw_payload, '$.title') AS title,
                    json_extract(b.raw_payload, '$.url') AS url,
                    COALESCE(json_extract(b.raw_payload, '$.location.city'), b.city) AS city,
                    json_extract(b.raw_payload, '$.location.district') AS district,
                    CAST(json_extract(b.raw_payload, '$.price.value') AS REAL) AS price_pln,
                    CAST(json_extract(b.raw_payload, '$.area.value') AS REAL) AS area_m2,
                    CAST(json_extract(b.raw_payload, '$.rooms') AS INTEGER) AS rooms,
                    CAST(json_extract(b.raw_payload, '$.floor') AS INTEGER) AS floor,
                    CAST(json_extract(b.raw_payload, '$.total_floors') AS INTEGER) AS total_floors,
                    
                    COALESCE(
                        CAST(json_extract(b.raw_payload, '$.features.elevator') AS INTEGER),
                        CASE 
                            WHEN json_extract(b.raw_payload, '$.description') LIKE '%winda%' 
                              OR json_extract(b.raw_payload, '$.description') LIKE '%windą%' THEN 1 
                            ELSE 0 
                        END
                    ) AS has_elevator,
                    
                    CAST(json_extract(b.raw_payload, '$.location.coordinates.latitude') AS REAL) AS lat,
                    CAST(json_extract(b.raw_payload, '$.location.coordinates.longitude') AS REAL) AS lon,
                    json_extract(b.raw_payload, '$.seller_type') AS seller_type,
                    json_extract(b.raw_payload, '$.description') AS description_text,
                    b.raw_payload
                FROM bronze_listings b
            )
            SELECT 
                e.*,
                CASE WHEN e.area_m2 > 0 THEN ROUND(e.price_pln / e.area_m2, 2) ELSE NULL END AS price_per_m2,
                CASE 
                    WHEN e.total_floors IS NOT NULL AND e.floor = e.total_floors AND e.floor > 0 THEN 1 
                    ELSE 0 
                END AS is_last_floor
            FROM extracted_data e;
            """)

            # 3. Widok Gold (Deduplikacja międzyserwisowa)
            cursor.execute("""
            CREATE VIEW IF NOT EXISTS gold_listings AS
            WITH deduplicated AS (
                SELECT 
                    COALESCE(
                        ROUND(lat, 3) || '_' || ROUND(lon, 3) || '_' || ROUND(area_m2, 1) || '_' || rooms,
                        district || '_' || ROUND(area_m2, 1) || '_' || rooms || '_' || floor
                    ) AS dedup_fingerprint,
                    MIN(bronze_id) AS primary_bronze_id,
                    GROUP_CONCAT(source_portal || ':' || external_id, ', ') AS source_portals_list,
                    MIN(price_pln) AS min_price_pln,
                    MAX(price_pln) AS max_price_pln,
                    COUNT(*) AS portal_occurrences_count,
                    title,
                    url,
                    district,
                    price_pln,
                    area_m2,
                    price_per_m2,
                    rooms,
                    floor,
                    total_floors,
                    has_elevator,
                    seller_type,
                    lat,
                    lon,
                    scraped_at
                FROM silver_listings
                GROUP BY dedup_fingerprint
            )
            SELECT * FROM deduplicated;
            """)
            conn.commit()
        finally:
            conn.close()

    def insert_bronze_listing(self, source_portal, external_id, city, chunk_name, raw_payload):
        """
        Wstawia surowy obiekt JSON ogłoszenia do tabeli bronze_listings.
        """
        payload_str = json.dumps(raw_payload, ensure_ascii=False) if isinstance(raw_payload, dict) else raw_payload
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT OR REPLACE INTO bronze_listings (source_portal, external_id, city, chunk_name, raw_payload)
            VALUES (?, ?, ?, ?, ?)
            """, (source_portal, external_id, city, chunk_name, payload_str))
            conn.commit()
        finally:
            conn.close()

    def test_connection(self):
        """
        Przeprowadza test sprawdzający poprawność połączenia i customowych funkcji SQLite.
        """
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT haversine_m(52.148, 21.033, 52.150, 21.035) AS dist;")
            row = cursor.fetchone()
            dist = row["dist"] if row else None
            return {
                "status": "OK",
                "haversine_test_m": dist,
                "db_path": self.db_path
            }
        finally:
            conn.close()
