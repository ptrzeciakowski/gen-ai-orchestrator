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
        if self.db_path != ":memory:" and os.path.dirname(self.db_path):
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
                run_id TEXT,
                source_portal TEXT NOT NULL,
                external_id TEXT NOT NULL,
                city TEXT NOT NULL DEFAULT 'Warszawa',
                chunk_name TEXT,
                raw_payload JSON NOT NULL,
                scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(run_id, source_portal, external_id) ON CONFLICT REPLACE
            );
            """)
            
            # Próba dodania kolumny run_id dla istniejących baz
            try:
                cursor.execute("ALTER TABLE bronze_listings ADD COLUMN run_id TEXT;")
            except Exception:
                pass
            
            cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_bronze_source_ext 
            ON bronze_listings(source_portal, external_id);
            """)

            # 2. Widok Silver (Obsługa pasywna schematu syntetycznego, natywnego Otodom __NEXT_DATA__ oraz Adresowo.pl)
            cursor.execute("DROP VIEW IF EXISTS silver_listings;")
            cursor.execute("""
            CREATE VIEW silver_listings AS
            WITH extracted_data AS (
                SELECT 
                    b.id AS bronze_id,
                    b.run_id,
                    b.source_portal,
                    b.external_id,
                    b.scraped_at,
                    COALESCE(
                        json_extract(b.raw_payload, '$.title'),
                        json_extract(b.raw_payload, '$.place_ld.name')
                    ) AS title,
                    
                    COALESCE(
                        json_extract(b.raw_payload, '$.url'),
                        CASE 
                            WHEN json_extract(b.raw_payload, '$.slug') IS NOT NULL 
                            THEN 'https://www.otodom.pl/pl/oferta/' || json_extract(b.raw_payload, '$.slug')
                            ELSE 'https://www.otodom.pl/pl/oferta/' || b.external_id
                        END
                    ) AS url,
                    
                    COALESCE(
                        json_extract(b.raw_payload, '$.location.city'),
                        json_extract(b.raw_payload, '$.location.address.city.name'),
                        b.city
                    ) AS city,
                    
                    COALESCE(
                        json_extract(b.raw_payload, '$.location.district'),
                        json_extract(b.raw_payload, '$.location.address.district.name'),
                        (
                            SELECT json_extract(value, '$.name')
                            FROM json_each(b.raw_payload, '$.location.reverseGeocoding.locations')
                            WHERE json_extract(value, '$.locationLevel') = 'district'
                            LIMIT 1
                        ),
                        b.chunk_name
                    ) AS district,

                    CAST(COALESCE(
                        json_extract(b.raw_payload, '$.price_pln'),
                        json_extract(b.raw_payload, '$.price.value'),
                        json_extract(b.raw_payload, '$.totalPrice.value')
                    ) AS REAL) AS price_pln,
                    
                    CAST(COALESCE(
                        json_extract(b.raw_payload, '$.area_m2'),
                        json_extract(b.raw_payload, '$.area.value'),
                        json_extract(b.raw_payload, '$.areaInSquareMeters')
                    ) AS REAL) AS area_m2,
                    
                    CAST(COALESCE(
                        json_extract(b.raw_payload, '$.rooms'),
                        CASE json_extract(b.raw_payload, '$.roomsNumber')
                            WHEN 'ONE' THEN 1
                            WHEN 'TWO' THEN 2
                            WHEN 'THREE' THEN 3
                            WHEN 'FOUR' THEN 4
                            WHEN 'FIVE' THEN 5
                            ELSE CAST(json_extract(b.raw_payload, '$.roomsNumber') AS INTEGER)
                        END
                    ) AS INTEGER) AS rooms,
                    
                    CAST(COALESCE(
                        json_extract(b.raw_payload, '$.floor'),
                        CASE json_extract(b.raw_payload, '$.floorNumber')
                            WHEN 'GROUND_FLOOR' THEN 0
                            WHEN 'FIRST' THEN 1
                            WHEN 'SECOND' THEN 2
                            WHEN 'THIRD' THEN 3
                            WHEN 'FOURTH' THEN 4
                            WHEN 'FIFTH' THEN 5
                            WHEN 'SIXTH' THEN 6
                            WHEN 'SEVENTH' THEN 7
                            WHEN 'EIGHTH' THEN 8
                            WHEN 'NINTH' THEN 9
                            WHEN 'TENTH' THEN 10
                            ELSE NULL
                        END
                    ) AS INTEGER) AS floor,
                    
                    CAST(json_extract(b.raw_payload, '$.total_floors') AS INTEGER) AS total_floors,
                    
                    COALESCE(
                        CAST(json_extract(b.raw_payload, '$.has_elevator') AS INTEGER),
                        CAST(json_extract(b.raw_payload, '$.features.elevator') AS INTEGER),
                        CAST(json_extract(b.raw_payload, '$.hasElevator') AS INTEGER),
                        CASE 
                            WHEN json_extract(b.raw_payload, '$.target.Extras_types') LIKE '%lift%' THEN 1
                            WHEN json_extract(b.raw_payload, '$.description') LIKE '%winda%' 
                              OR json_extract(b.raw_payload, '$.description') LIKE '%windą%'
                              OR json_extract(b.raw_payload, '$.shortDescription') LIKE '%winda%'
                              OR json_extract(b.raw_payload, '$.shortDescription') LIKE '%windą%' THEN 1 
                            ELSE 0 
                        END
                    ) AS has_elevator,
                    
                    CAST(COALESCE(
                        json_extract(b.raw_payload, '$.location.coordinates.latitude'),
                        json_extract(b.raw_payload, '$.place_ld.geo.latitude')
                    ) AS REAL) AS lat,
                    
                    CAST(COALESCE(
                        json_extract(b.raw_payload, '$.location.coordinates.longitude'),
                        json_extract(b.raw_payload, '$.place_ld.geo.longitude')
                    ) AS REAL) AS lon,
                    
                    COALESCE(
                        json_extract(b.raw_payload, '$.seller_type'),
                        CASE WHEN json_extract(b.raw_payload, '$.isPrivateOwner') = 1 THEN 'Bezpośrednio' ELSE 'Agencja' END
                    ) AS seller_type,
                    
                    COALESCE(
                        json_extract(b.raw_payload, '$.description_text'),
                        json_extract(b.raw_payload, '$.description'),
                        json_extract(b.raw_payload, '$.shortDescription')
                    ) AS description_text,
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

            # 3. Widok Gold (Deduplikacja międzyserwisowa i flaga nowości is_new_listing)
            cursor.execute("DROP VIEW IF EXISTS gold_listings;")
            cursor.execute("""
            CREATE VIEW gold_listings AS
            WITH deduplicated AS (
                SELECT 
                    COALESCE(
                        ROUND(lat, 3) || '_' || ROUND(lon, 3) || '_' || ROUND(area_m2, 1) || '_' || rooms,
                        district || '_' || ROUND(area_m2, 1) || '_' || rooms || '_' || floor || '_' || CAST(price_pln AS INT)
                    ) AS dedup_fingerprint,
                    MIN(bronze_id) AS primary_bronze_id,
                    MIN(external_id) AS external_id,
                    MIN(source_portal) AS source_portal,
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
                    is_last_floor,
                    seller_type,
                    lat,
                    lon,
                    scraped_at,
                    run_id
                FROM silver_listings
                GROUP BY dedup_fingerprint, run_id
            )
            SELECT 
                d.*,
                CASE 
                    WHEN NOT EXISTS (
                        SELECT 1 FROM silver_listings s_prev 
                        WHERE s_prev.run_id != d.run_id 
                          AND s_prev.scraped_at < d.scraped_at 
                          AND COALESCE(
                              ROUND(s_prev.lat, 3) || '_' || ROUND(s_prev.lon, 3) || '_' || ROUND(s_prev.area_m2, 1) || '_' || s_prev.rooms,
                              s_prev.district || '_' || ROUND(s_prev.area_m2, 1) || '_' || s_prev.rooms || '_' || s_prev.floor || '_' || CAST(s_prev.price_pln AS INT)
                          ) = d.dedup_fingerprint
                    ) THEN 1 ELSE 0 
                END AS is_new_listing
            FROM deduplicated d;
            """)
            conn.commit()
        finally:
            conn.close()

    def clear_bronze(self, source_portal=None):
        """
        Czyści dane z tabeli bronze_listings.
        """
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if source_portal:
                cursor.execute("DELETE FROM bronze_listings WHERE source_portal = ?;", (source_portal,))
            else:
                cursor.execute("DELETE FROM bronze_listings;")
            conn.commit()
        finally:
            conn.close()

    def insert_bronze_listing(self, source_portal, external_id, city, chunk_name, raw_payload, run_id=None):
        """
        Wstawia surowy obiekt JSON ogłoszenia do tabeli bronze_listings.
        """
        payload_str = json.dumps(raw_payload, ensure_ascii=False) if isinstance(raw_payload, dict) else raw_payload
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
            INSERT OR REPLACE INTO bronze_listings (run_id, source_portal, external_id, city, chunk_name, raw_payload)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (run_id, source_portal, external_id, city, chunk_name, payload_str))
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
