"""
Kompleksowy test regresji wieloźródłowej dla architektury ELT (Bronze -> Silver -> Gold).
Sprawdza jednoczesne zasilenie bazy z 6 źródeł:
- Otodom (Commercial i Direct)
- Adresowo
- Gratka
- Morizon
- Nieruchomosci-online
- OLX
Oraz poprawność transformacji w Silver, deduplikacji w Gold i audytu run_audit.
"""
import unittest
import tempfile
import shutil
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager
from src.deduplicator import Deduplicator
from src.config import CriteriaConfig

class TestMultiPortalRegression(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.db_file = os.path.join(self.temp_dir, "test_multi_regression.db")
        self.db = DatabaseManager(db_path=self.db_file)
        self.run_id = "test_multi_run_001"

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_simultaneous_all_portals_ingestion_and_silver_extraction(self):
        """Weryfikacja wstawienia i transformacji w silver_listings dla wszystkich 6 portali"""
        # 1. Otodom
        self.db.insert_bronze_listing(
            source_portal="otodom",
            external_id="otodom_101",
            city="Warszawa",
            chunk_name="warszawa_ursynow_otodom",
            raw_payload={
                "id": "otodom_101",
                "title": "Mieszkanie Otodom Ursynów",
                "slug": "mieszkanie-otodom-ursynow-101",
                "totalPrice": {"value": 1020000},
                "areaInSquareMeters": 58.5,
                "roomsNumber": "THREE",
                "floorNumber": "SECOND",
                "total_floors": 5,
                "hasElevator": 1,
                "isPrivateOwner": 0,
                "location": {
                    "city": "Warszawa",
                    "district": "Ursynów",
                    "coordinates": {"latitude": 52.145, "longitude": 21.045}
                }
            },
            run_id=self.run_id
        )

        # 2. Adresowo
        self.db.insert_bronze_listing(
            source_portal="adresowo",
            external_id="ad_202",
            city="Warszawa",
            chunk_name="warszawa_ursynow_adresowo",
            raw_payload={
                "id": "ad_202",
                "title": "Mieszkanie Adresowo Ursynów",
                "url": "https://adresowo.pl/o/ad_202",
                "price_pln": 1020000,
                "area_m2": 58.5,
                "rooms": 3,
                "floor": 2,
                "total_floors": 5,
                "has_elevator": 1,
                "seller_type": "Bezpośrednio",
                "location": {
                    "city": "Warszawa",
                    "district": "Ursynów",
                    "coordinates": {"latitude": 52.145, "longitude": 21.045}
                }
            },
            run_id=self.run_id
        )

        # 3. Gratka
        self.db.insert_bronze_listing(
            source_portal="gratka",
            external_id="gratka_303",
            city="Warszawa",
            chunk_name="warszawa_ursynow_gratka",
            raw_payload={
                "id": "gratka_303",
                "title": "Mieszkanie Gratka Ursynów",
                "url": "https://gratka.pl/nieruchomosci/ob/gratka_303",
                "price_pln": 1020000,
                "area_m2": 58.5,
                "rooms": 3,
                "floor": 2,
                "total_floors": 5,
                "has_elevator": 1,
                "seller_type": "Agencja",
                "location": {
                    "city": "Warszawa",
                    "district": "Ursynów",
                    "coordinates": {"latitude": 52.145, "longitude": 21.045}
                }
            },
            run_id=self.run_id
        )

        # 4. Morizon
        self.db.insert_bronze_listing(
            source_portal="morizon",
            external_id="morizon_404",
            city="Warszawa",
            chunk_name="warszawa_ursynow_morizon",
            raw_payload={
                "id": "morizon_404",
                "title": "Mieszkanie Morizon Ursynów",
                "url": "https://www.morizon.pl/oferta/morizon_404",
                "price_pln": 1020000,
                "area_m2": 58.5,
                "rooms": 3,
                "floor": 2,
                "total_floors": 5,
                "has_elevator": 1,
                "seller_type": "Agencja",
                "location": {
                    "city": "Warszawa",
                    "district": "Ursynów",
                    "coordinates": {"latitude": 52.145, "longitude": 21.045}
                }
            },
            run_id=self.run_id
        )

        # 5. Nieruchomosci-online
        self.db.insert_bronze_listing(
            source_portal="nieruchomosci_online",
            external_id="nol_505",
            city="Warszawa",
            chunk_name="warszawa_ursynow_nieruchomosci_online",
            raw_payload={
                "id": "nol_505",
                "title": "Mieszkanie Nieruchomosci-online Ursynów",
                "url": "https://www.nieruchomosci-online.pl/mieszkanie,nol_505.html",
                "price_pln": 1020000,
                "area_m2": 58.5,
                "rooms": 3,
                "floor": 2,
                "total_floors": 5,
                "has_elevator": 1,
                "seller_type": "Agencja",
                "location": {
                    "city": "Warszawa",
                    "district": "Ursynów",
                    "coordinates": {"latitude": 52.145, "longitude": 21.045}
                }
            },
            run_id=self.run_id
        )

        # 6. OLX
        self.db.insert_bronze_listing(
            source_portal="olx",
            external_id="olx_606",
            city="Warszawa",
            chunk_name="warszawa_ursynow_olx",
            raw_payload={
                "id": "olx_606",
                "title": "Mieszkanie OLX Ursynów",
                "url": "https://www.olx.pl/d/oferta/olx_606.html",
                "price_pln": 1020000,
                "area_m2": 58.5,
                "rooms": 3,
                "floor": 2,
                "total_floors": 5,
                "has_elevator": 1,
                "seller_type": "Bezpośrednio",
                "location": {
                    "city": "Warszawa",
                    "district": "Ursynów",
                    "coordinates": {"latitude": 52.145, "longitude": 21.045}
                }
            },
            run_id=self.run_id
        )

        conn = self.db.get_connection()
        try:
            silver_rows = conn.execute("SELECT * FROM silver_listings WHERE run_id = ?;", (self.run_id,)).fetchall()
            self.assertEqual(len(silver_rows), 6)

            for row in silver_rows:
                self.assertEqual(row["price_pln"], 1020000.0)
                self.assertEqual(row["area_m2"], 58.5)
                self.assertEqual(row["rooms"], 3)
                self.assertEqual(row["floor"], 2)
                self.assertEqual(row["has_elevator"], 1)
                self.assertEqual(row["district"], "Ursynów")
                self.assertIsNotNone(row["lat"])
                self.assertIsNotNone(row["lon"])

            # Weryfikacja deduplikacji w gold_listings: Wszystkie 6 portali opisują to samo mieszkanie
            gold_rows = conn.execute("SELECT * FROM gold_listings WHERE run_id = ?;", (self.run_id,)).fetchall()
            self.assertEqual(len(gold_rows), 1)
            gold_record = dict(gold_rows[0])
            self.assertEqual(gold_record["portal_occurrences_count"], 6)
            self.assertIn("otodom", gold_record["source_portals_list"])
            self.assertIn("adresowo", gold_record["source_portals_list"])
            self.assertIn("gratka", gold_record["source_portals_list"])
            self.assertIn("morizon", gold_record["source_portals_list"])
            self.assertIn("nieruchomosci_online", gold_record["source_portals_list"])
            self.assertIn("olx", gold_record["source_portals_list"])

        finally:
            conn.close()

    def test_run_audit_multi_source(self):
        """Weryfikacja tabeli run_audit dla wszystkich 6 portali"""
        portals = ["otodom", "adresowo", "gratka", "morizon", "nieruchomosci_online", "olx"]
        for p in portals:
            self.db.save_run_audit(self.run_id, p, expected_total=50, saved_bronze=48)

        audits = self.db.get_run_audits(self.run_id)
        self.assertEqual(len(audits), 6)
        for a in audits:
            self.assertEqual(a["expected_total"], 50)
            self.assertEqual(a["saved_bronze"], 48)
            self.assertEqual(a["completeness_pct"], 96.0)

if __name__ == "__main__":
    unittest.main()
