"""
Testy jednostkowe i integracyjne dla architektury ELT (Bronze / Silver / Gold).
"""
import unittest
import tempfile
import shutil
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager, haversine_m, regexp

class TestELTPipeline(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_file = os.path.join(self.temp_dir, "test_listings.db")
        self.db = DatabaseManager(db_path=self.db_file)

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_haversine_m(self):
        dist = haversine_m(52.148, 21.033, 52.150, 21.035)
        self.assertIsNotNone(dist)
        self.assertTrue(250 < dist < 270)

    def test_regexp_function(self):
        self.assertTrue(regexp(r"winda|windą", "Mieszkanie z windą na Ursynowie"))
        self.assertTrue(regexp(r"winda|windy|windą", "Brak windy"))
        self.assertFalse(regexp(r"garaż", "Mieszkanie na Ursynowie"))

    def test_database_manager_pipeline(self):
        # 1. Wstawienie rekordów do Bronze
        self.db.insert_bronze_listing(
            source_portal="otodom",
            external_id="test-1",
            city="Warszawa",
            chunk_name="test_chunk",
            raw_payload={
                "title": "Mieszkanie 3 pokoje Ursynów",
                "price": {"value": 900000},
                "area": {"value": 60.0},
                "rooms": 3,
                "floor": 2,
                "total_floors": 4,
                "features": {"elevator": 1},
                "location": {"city": "Warszawa", "district": "Ursynów", "coordinates": {"latitude": 52.148, "longitude": 21.033}},
                "seller_type": "Bezpośrednio"
            }
        )
        
        self.db.insert_bronze_listing(
            source_portal="olx",
            external_id="test-1-dup",
            city="Warszawa",
            chunk_name="test_chunk",
            raw_payload={
                "title": "Duplikat mieszkania 3 pokoje Ursynów",
                "price": {"value": 900000},
                "area": {"value": 60.0},
                "rooms": 3,
                "floor": 2,
                "total_floors": 4,
                "features": {"elevator": 1},
                "location": {"city": "Warszawa", "district": "Ursynów", "coordinates": {"latitude": 52.148, "longitude": 21.033}},
                "seller_type": "Agencja"
            }
        )

        # 2. Odczyt z Silver
        conn = self.db.get_connection()
        try:
            silver_rows = conn.execute("SELECT * FROM silver_listings;").fetchall()
            self.assertEqual(len(silver_rows), 2)
        finally:
            conn.close()

        # 3. Odczyt z Gold (deduplikacja z 2 do 1 ze względu na tę samą geolokalizację, metraż i pokoje)
        conn = self.db.get_connection()
        try:
            gold_rows = conn.execute("SELECT * FROM gold_listings;").fetchall()
            self.assertEqual(len(gold_rows), 1)
            gold = dict(gold_rows[0])
            self.assertEqual(gold["district"], "Ursynów")
            self.assertEqual(gold["portal_occurrences_count"], 2)
        finally:
            conn.close()

if __name__ == "__main__":
    unittest.main()
