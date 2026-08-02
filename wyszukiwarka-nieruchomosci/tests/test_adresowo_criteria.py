"""
Dedykowany zestaw testów jednostkowych i walidacji kryteriów z kryteria.md dla AdresowoProvider i warstwy ELT.
"""
import unittest
import sqlite3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager
from src.deduplicator import Deduplicator
from src.config import CriteriaConfig

class TestAdresowoCriteria(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "test_listings.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db_manager = DatabaseManager(db_path=self.db_path)
        self.conn = self.db_manager.get_connection()
        self.run_id = "test_run_001"

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def insert_sample_adresowo_raw(self, ext_id, title, price, area, rooms, floor, total_floors, has_elevator, build_year, seller_type, district="Ursynów"):
        # Generujemy unikalne koordynaty na podstawie ext_id
        idx = hash(ext_id) % 1000
        lat = 52.14 + (idx * 0.001)
        lon = 21.05 + (idx * 0.001)
        raw = {
            "id": ext_id,
            "title": title,
            "url": f"https://adresowo.pl/o/{ext_id}",
            "price_pln": price,
            "area_m2": area,
            "rooms": rooms,
            "floor": floor,
            "total_floors": total_floors,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "location": {
                "city": "Warszawa",
                "district": district,
                "coordinates": {"latitude": lat, "longitude": lon}
            }
        }
        self.db_manager.insert_bronze_listing(
            source_portal="adresowo",
            external_id=ext_id,
            city="Warszawa",
            chunk_name=f"warszawa_{district.lower()}_adresowo",
            raw_payload=raw,
            run_id=self.run_id
        )

    def test_price_range_filtering(self):
        """Test filtracji ceny min/max (1,000,000 - 1,050,000 PLN)"""
        self.insert_sample_adresowo_raw("ad_1", "Tania oferta", 950000, 50, 3, 2, 4, 1, 2010, "Bezpośrednio")
        self.insert_sample_adresowo_raw("ad_2", "Właściwa oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Bezpośrednio")
        self.insert_sample_adresowo_raw("ad_3", "Droga oferta", 1100000, 60, 3, 2, 4, 1, 2010, "Bezpośrednio")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "ad_2")

    def test_rooms_and_elevator_filtering(self):
        """Test liczby pokoi (3 pokoje) oraz obecności windy (has_elevator = 1)"""
        # Oferta 3 pokoje Z windą
        self.insert_sample_adresowo_raw("ad_ok", "Oferta z windą", 1020000, 55, 3, 2, 4, 1, 2010, "Bezpośrednio")
        # Oferta 3 pokoje BEZ windy
        self.insert_sample_adresowo_raw("ad_no_lift", "Oferta bez windy", 1020000, 55, 3, 2, 3, 0, 2010, "Bezpośrednio")
        # Oferta 2 pokoje Z windą
        self.insert_sample_adresowo_raw("ad_2rooms", "Oferta 2 pokoje", 1020000, 50, 2, 2, 4, 1, 2010, "Bezpośrednio")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.elevator = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "ad_ok")

    def test_ground_floor_exclusion(self):
        """Test wykluczenia parteru (floor > 0)"""
        self.insert_sample_adresowo_raw("ad_parter", "Mieszkanie parter", 1020000, 55, 3, 0, 4, 1, 2010, "Bezpośrednio")
        self.insert_sample_adresowo_raw("ad_pietro2", "Mieszkanie 2 piętro", 1020000, 55, 3, 2, 4, 1, 2010, "Bezpośrednio")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.exclude_ground_floor = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "ad_pietro2")

    def test_novelty_detection_flag(self):
        """Test wykrywania nowości (is_new_listing) między uruchomieniami"""
        run1 = "run_historical_001"
        run2 = "run_current_002"

        # Uruchomienie 1: Oferta A
        self.insert_sample_adresowo_raw("ad_old", "Stara oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Bezpośrednio")
        # Zmieniamy run_id na run1 dla pierwszej oferty
        conn = self.db_manager.get_connection()
        conn.cursor().execute("UPDATE bronze_listings SET run_id = ?, scraped_at = '2026-08-01 10:00:00' WHERE external_id = 'ad_old';", (run1,))
        conn.commit()

        # Uruchomienie 2: Oferta A (powtórzona) + Oferta B (nowa)
        self.insert_sample_adresowo_raw("ad_old", "Stara oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Bezpośrednio")
        self.insert_sample_adresowo_raw("ad_new", "Nowa oferta", 1030000, 58, 3, 3, 4, 1, 2012, "Bezpośrednio")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        res_map = {r["external_id"]: r["is_new_listing"] for r in results}
        self.assertEqual(res_map.get("ad_old"), 0)  # Powtórzona oferta nie jest nowa
        self.assertEqual(res_map.get("ad_new"), 1)  # Całkowicie nowa oferta ma flagę 1

if __name__ == "__main__":
    unittest.main()
