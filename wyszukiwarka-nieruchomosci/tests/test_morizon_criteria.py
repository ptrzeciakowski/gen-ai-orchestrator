"""
Dedykowany zestaw testów jednostkowych i walidacji kryteriów z kryteria.md dla MorizonProvider i warstwy ELT.
"""
import unittest
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager
from src.deduplicator import Deduplicator
from src.config import CriteriaConfig
from src.providers.morizon import MorizonProvider

class TestMorizonCriteria(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "test_morizon_listings.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db_manager = DatabaseManager(db_path=self.db_path)
        self.conn = self.db_manager.get_connection()
        self.run_id = "test_run_morizon_001"

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def insert_sample_morizon_raw(self, ext_id, title, price, area, rooms, floor, total_floors, has_elevator, build_year, seller_type, district="Ursynów", lat=52.148, lon=21.045, run_id=None):
        rid = run_id or self.run_id
        raw = {
            "id": ext_id,
            "title": title,
            "url": f"https://www.morizon.pl/oferta/{ext_id}",
            "price_pln": price,
            "area_m2": area,
            "rooms": rooms,
            "floor": floor,
            "total_floors": total_floors,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "description_text": f"Jasne mieszkanie w dzielnicy {district}, winda: {'tak' if has_elevator else 'brak'}",
            "location": {
                "city": "Warszawa",
                "district": district,
                "street": "al. Komisji Edukacji Narodowej",
                "coordinates": {"latitude": lat, "longitude": lon}
            }
        }
        self.db_manager.insert_bronze_listing(
            source_portal="morizon",
            external_id=ext_id,
            city="Warszawa",
            chunk_name=f"warszawa_{district.lower()}_morizon",
            raw_payload=raw,
            run_id=rid
        )

    def test_build_search_url(self):
        """Test budowania URL wyszukiwania Morizon i mapowania parametrów ps[...]"""
        cfg = CriteriaConfig()
        cfg.city = "Warszawa"
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.min_area = 50
        cfg.max_area = 70

        provider = MorizonProvider(config=cfg, db_manager=self.db_manager)

        # Test normalizacji slugów
        self.assertEqual(provider.normalize_slug("Mokotów"), "mokotow")
        self.assertEqual(provider.normalize_slug("Praga-Południe"), "praga-poludnie")
        self.assertEqual(provider.normalize_slug("Śródmieście"), "srodmiescie")
        self.assertEqual(provider.normalize_slug("Ursynów"), "ursynow")

        # Test generowania URL dla Ursynowa (strona 1)
        url_p1 = provider.build_search_url("Warszawa", "Ursynów", page=1)
        self.assertTrue(url_p1.startswith("https://www.morizon.pl/mieszkania/sprzedaz/warszawa/ursynow/"))
        self.assertIn("ps[price_from]=1000000", url_p1)
        self.assertIn("ps[price_to]=1050000", url_p1)
        self.assertIn("ps[number_of_rooms_from]=3", url_p1)
        self.assertIn("ps[number_of_rooms_to]=3", url_p1)
        self.assertIn("ps[living_area_from]=50", url_p1)
        self.assertIn("ps[living_area_to]=70", url_p1)
        self.assertNotIn("page=", url_p1)

        # Test generowania URL ze stroną 2
        url_p2 = provider.build_search_url("Warszawa", "Ursynów", page=2)
        self.assertIn("page=2", url_p2)

    def test_morizon_raw_payload_parsing(self):
        """Test wielowarstwowego parsera JSON-LD i DOM fallback dla Morizona"""
        cfg = CriteriaConfig()
        provider = MorizonProvider(config=cfg, db_manager=self.db_manager)

        sample_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Mieszkanie 3 pokojowe Warszawa Ursynów</title>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "Apartment",
                        "name": "Przestronne 3 pokoje z windą przy metrze Imielin",
                        "numberOfRooms": 3,
                        "floorSize": {
                            "@type": "QuantitativeValue",
                            "value": 58.5
                        },
                        "description": "Oferujemy nowoczesne mieszkanie z windą w budynku 4-piętrowym.",
                        "geo": {
                            "@type": "GeoCoordinates",
                            "latitude": 52.1482,
                            "longitude": 21.0451
                        },
                        "address": {
                            "@type": "PostalAddress",
                            "addressLocality": "Warszawa",
                            "addressRegion": "Ursynów",
                            "streetAddress": "al. KEN"
                        },
                        "offers": {
                            "@type": "Offer",
                            "price": 1025000,
                            "priceCurrency": "PLN"
                        }
                    }
                ]
            }
            </script>
        </head>
        <body>
            <h1>Przestronne 3 pokoje z windą przy metrze Imielin</h1>
            <div class="parameters">
                <span>Piętro: 2</span>
                <span>Liczba pięter: 4</span>
                <span>Rok budowy: 2011</span>
                <span>Winda: tak</span>
                <span>Typ ogłoszenia: Biuro Nieruchomości</span>
            </div>
        </body>
        </html>
        """

        detail_url = "https://www.morizon.pl/oferta/sprzedaz-mieszkanie-warszawa-ursynow-mz12345678"
        ext_id, payload = provider.parse_listing_detail(sample_html, detail_url, default_city="Warszawa", default_district="Ursynów")

        self.assertEqual(ext_id, "morizon_12345678")
        self.assertEqual(payload["title"], "Przestronne 3 pokoje z windą przy metrze Imielin")
        self.assertEqual(payload["price_pln"], 1025000.0)
        self.assertEqual(payload["area_m2"], 58.5)
        self.assertEqual(payload["rooms"], 3)
        self.assertEqual(payload["floor"], 2)
        self.assertEqual(payload["total_floors"], 4)
        self.assertEqual(payload["has_elevator"], 1)
        self.assertEqual(payload["build_year"], 2011)
        self.assertEqual(payload["location"]["city"], "Warszawa")
        self.assertEqual(payload["location"]["district"], "Ursynów")
        self.assertEqual(payload["location"]["coordinates"]["latitude"], 52.1482)
        self.assertEqual(payload["location"]["coordinates"]["longitude"], 21.0451)

        # Zapis do bazy Bronze i weryfikacja Silver
        self.db_manager.insert_bronze_listing(
            source_portal="morizon",
            external_id=ext_id,
            city="Warszawa",
            chunk_name="warszawa_ursynow_morizon",
            raw_payload=payload,
            run_id=self.run_id
        )

        conn = self.db_manager.get_connection()
        try:
            silver_row = conn.execute("SELECT * FROM silver_listings WHERE external_id = ?", (ext_id,)).fetchone()
            self.assertIsNotNone(silver_row)
            self.assertEqual(silver_row["price_pln"], 1025000.0)
            self.assertEqual(silver_row["rooms"], 3)
            self.assertEqual(silver_row["has_elevator"], 1)
            self.assertEqual(silver_row["is_last_floor"], 0)
            self.assertAlmostEqual(silver_row["price_per_m2"], round(1025000.0 / 58.5, 2))
        finally:
            conn.close()

    def test_price_range_filtering(self):
        """Test filtracji ceny min/max (1,000,000 - 1,050,000 PLN) dla ofert Morizon"""
        self.insert_sample_morizon_raw("mor_1", "Tania oferta", 950000, 50, 3, 2, 4, 1, 2010, "Agencja", lat=52.141, lon=21.041)
        self.insert_sample_morizon_raw("mor_2", "Właściwa oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja", lat=52.142, lon=21.042)
        self.insert_sample_morizon_raw("mor_3", "Droga oferta", 1100000, 60, 3, 2, 4, 1, 2010, "Agencja", lat=52.143, lon=21.043)

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "mor_2")

    def test_rooms_and_elevator_filtering(self):
        """Test liczby pokoi (3 pokoje) oraz obecności windy (has_elevator = 1)"""
        # Oferta 3 pokoje Z windą
        self.insert_sample_morizon_raw("mor_ok", "Oferta z windą", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja", lat=52.141, lon=21.041)
        # Oferta 3 pokoje BEZ windy
        self.insert_sample_morizon_raw("mor_no_lift", "Oferta bez windy", 1020000, 55, 3, 2, 3, 0, 2010, "Agencja", lat=52.142, lon=21.042)
        # Oferta 2 pokoje Z windą
        self.insert_sample_morizon_raw("mor_2rooms", "Oferta 2 pokoje", 1020000, 50, 2, 2, 4, 1, 2010, "Agencja", lat=52.143, lon=21.043)

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.elevator = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "mor_ok")

    def test_ground_floor_exclusion(self):
        """Test wykluczenia parteru (floor > 0)"""
        self.insert_sample_morizon_raw("mor_parter", "Mieszkanie parter", 1020000, 55, 3, 0, 4, 1, 2010, "Agencja", lat=52.141, lon=21.041)
        self.insert_sample_morizon_raw("mor_pietro2", "Mieszkanie 2 piętro", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja", lat=52.142, lon=21.042)

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.exclude_ground_floor = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "mor_pietro2")

    def test_cross_portal_deduplication(self):
        """Test scalania ofert wystawionych równolegle na Morizon, Otodom i Adresowo"""
        shared_lat = 52.1485
        shared_lon = 21.0455
        shared_area = 58.4
        shared_rooms = 3

        # 1. Oferta z Morizona
        self.insert_sample_morizon_raw(
            "mor_dup_1", "Mieszkanie Morizon", 1030000, shared_area, shared_rooms, 2, 4, 1, 2011, "Agencja",
            lat=shared_lat, lon=shared_lon
        )

        # 2. Oferta z Otodom (te same współrzędne, pokoje, metraż)
        otodom_raw = {
            "title": "Mieszkanie Otodom",
            "price": {"value": 1025000},
            "area": {"value": shared_area},
            "rooms": shared_rooms,
            "floor": 2,
            "total_floors": 4,
            "features": {"elevator": 1},
            "location": {
                "city": "Warszawa",
                "district": "Ursynów",
                "coordinates": {"latitude": shared_lat, "longitude": shared_lon}
            },
            "seller_type": "Agencja"
        }
        self.db_manager.insert_bronze_listing(
            source_portal="otodom",
            external_id="oto_dup_1",
            city="Warszawa",
            chunk_name="warszawa_ursynow_otodom",
            raw_payload=otodom_raw,
            run_id=self.run_id
        )

        # 3. Oferta z Adresowo
        adresowo_raw = {
            "title": "Mieszkanie Adresowo",
            "price_pln": 1020000,
            "area_m2": shared_area,
            "rooms": shared_rooms,
            "floor": 2,
            "total_floors": 4,
            "has_elevator": 1,
            "location": {
                "city": "Warszawa",
                "district": "Ursynów",
                "coordinates": {"latitude": shared_lat, "longitude": shared_lon}
            },
            "seller_type": "Bezpośrednio"
        }
        self.db_manager.insert_bronze_listing(
            source_portal="adresowo",
            external_id="adr_dup_1",
            city="Warszawa",
            chunk_name="warszawa_ursynow_adresowo",
            raw_payload=adresowo_raw,
            run_id=self.run_id
        )

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        # Po deduplikacji powinien być dokładnie 1 rekord
        self.assertEqual(len(results), 1)
        gold = results[0]
        self.assertEqual(gold["portal_occurrences_count"], 3)
        self.assertIn("morizon:", gold["source_portals_list"])
        self.assertIn("otodom:", gold["source_portals_list"])
        self.assertIn("adresowo:", gold["source_portals_list"])
        self.assertEqual(gold["min_price_pln"], 1020000.0)
        self.assertEqual(gold["max_price_pln"], 1030000.0)

    def test_novelty_detection_flag(self):
        """Test flagi is_new_listing dla ofert Morizon w kolejnych zrzutach"""
        run1 = "run_morizon_hist_001"
        run2 = "run_morizon_curr_002"

        # Zrzut 1: Oferta A
        self.insert_sample_morizon_raw("mor_old", "Stara oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja", lat=52.141, lon=21.041, run_id=run1)
        
        conn = self.db_manager.get_connection()
        conn.cursor().execute("UPDATE bronze_listings SET scraped_at = '2026-08-01 10:00:00' WHERE external_id = 'mor_old';")
        conn.commit()
        conn.close()

        # Zrzut 2: Oferta A (ponownie pobrana) + Oferta B (całkowicie nowa)
        self.insert_sample_morizon_raw("mor_old", "Stara oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja", lat=52.141, lon=21.041, run_id=run2)
        self.insert_sample_morizon_raw("mor_new", "Nowa oferta", 1035000, 58, 3, 3, 4, 1, 2015, "Agencja", lat=52.149, lon=21.049, run_id=run2)

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=run2)

        res_map = {r["external_id"]: r["is_new_listing"] for r in results}
        self.assertEqual(res_map.get("mor_old"), 0)
        self.assertEqual(res_map.get("mor_new"), 1)

    def test_morizon_audit_logging(self):
        """Test rejestracji i wyliczania wskaźnika kompletności w tabeli run_audit"""
        self.db_manager.save_run_audit(
            run_id=self.run_id,
            source_portal="morizon",
            expected_total=50,
            saved_bronze=48
        )

        audits = self.db_manager.get_run_audits(run_id=self.run_id)
        self.assertEqual(len(audits), 1)
        morizon_audit = audits[0]
        self.assertEqual(morizon_audit["source_portal"], "morizon")
        self.assertEqual(morizon_audit["expected_total"], 50)
        self.assertEqual(morizon_audit["saved_bronze"], 48)
        self.assertEqual(morizon_audit["completeness_pct"], 96.0)

if __name__ == "__main__":
    unittest.main()
