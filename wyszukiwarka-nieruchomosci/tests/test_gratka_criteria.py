"""
Dedykowany zestaw testów jednostkowych i walidacji kryteriów z kryteria.md dla GratkaProvider i warstwy ELT.
"""
import unittest
import sqlite3
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager
from src.deduplicator import Deduplicator
from src.config import CriteriaConfig
from src.providers.gratka import GratkaProvider, slugify

class TestGratkaCriteria(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "test_gratka_listings.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db_manager = DatabaseManager(db_path=self.db_path)
        self.conn = self.db_manager.get_connection()
        self.run_id = "test_run_gratka_001"

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def insert_sample_gratka_raw(self, ext_id, title, price, area, rooms, floor, total_floors, has_elevator, build_year, seller_type, district="Ursynów", lat=None, lon=None):
        if lat is None or lon is None:
            idx = hash(ext_id) % 1000
            lat = 52.14 + (idx * 0.001)
            lon = 21.05 + (idx * 0.001)

        raw = {
            "id": ext_id,
            "title": title,
            "url": f"https://gratka.pl/nieruchomosci/mieszkanie-warszawa-{district.lower()}/ob/{ext_id}",
            "price_pln": price,
            "area_m2": area,
            "rooms": rooms,
            "floor": floor,
            "total_floors": total_floors,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "market": "wtorny",
            "location": {
                "city": "Warszawa",
                "district": district,
                "street": "ul. Testowa",
                "coordinates": {"latitude": lat, "longitude": lon}
            },
            "features": {
                "winda": bool(has_elevator),
                "pietro": f"{floor}/{total_floors}" if floor is not None else None
            },
            "description_text": f"Opis testowy mieszkania {title} z windą" if has_elevator else f"Opis testowy mieszkania {title}"
        }
        self.db_manager.insert_bronze_listing(
            source_portal="gratka",
            external_id=ext_id,
            city="Warszawa",
            chunk_name=f"warszawa_{district.lower()}_gratka",
            raw_payload=raw,
            run_id=self.run_id
        )

    def test_url_builder_and_criteria_mapping(self):
        """Test generowania URL z parametrami w notacji dwukropkowej Gratki oraz slugifikacji"""
        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.min_area = 50
        cfg.max_area = 80

        provider = GratkaProvider(config=cfg, db_manager=self.db_manager)
        url_page1 = provider.build_search_url("Warszawa", "Ursynów", page=1)
        url_page2 = provider.build_search_url("Warszawa", "Śródmieście", page=2)

        self.assertEqual("https://gratka.pl/nieruchomosci/mieszkania/warszawa/ursynow/sprzedaz", url_page1)
        self.assertNotIn("page=", url_page1)

        self.assertEqual("https://gratka.pl/nieruchomosci/mieszkania/warszawa/srodmiescie/sprzedaz?page=2", url_page2)

    def test_html_and_json_ld_parsing(self):
        """Test parsowania mocka strony listy i detalu Gratka.pl"""
        cfg = CriteriaConfig()
        provider = GratkaProvider(config=cfg, db_manager=self.db_manager)

        # 1. Mock strony listy
        mock_listing_html = """
        <!DOCTYPE html>
        <html>
        <head><title>Mieszkania na sprzedaż</title></head>
        <body>
            <h1>Warszawa, Ursynów: 24 ogłoszenia mieszkań na sprzedaż</h1>
            <div class="teaserList">
                <a href="/nieruchomosci/mieszkanie-warszawa-ursynow-imielin/ob/28941032" class="teaserLink">Mieszkanie 1</a>
                <a href="https://gratka.pl/nieruchomosci/mieszkanie-warszawa-ursynow-natolin/ob/28941033" class="teaserLink">Mieszkanie 2</a>
            </div>
        </body>
        </html>
        """
        expected_total, offers = provider.parse_listing_page(mock_listing_html)
        self.assertEqual(expected_total, 24)
        self.assertEqual(len(offers), 2)
        self.assertEqual(offers[0]["id"], "28941032")
        self.assertEqual(offers[0]["url"], "https://gratka.pl/nieruchomosci/mieszkanie-warszawa-ursynow-imielin/ob/28941032")
        self.assertEqual(offers[1]["id"], "28941033")

        # 2. Mock strony szczegółów
        mock_detail_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "Place",
                "name": "3 pokoje z windą i balkonem, Ursynów Imielin",
                "description": "Jasne, 3-pokojowe mieszkanie z windą na 3 piętrze.",
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": 52.1456,
                    "longitude": 21.0392
                },
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": "Warszawa",
                    "streetAddress": "ul. Dereniowa"
                }
            }
            </script>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@type": "Offer",
                "price": 1025000,
                "priceCurrency": "PLN"
            }
            </script>
        </head>
        <body>
            <h1>3 pokoje z windą i balkonem, Ursynów Imielin</h1>
            <div class="priceInfo"><span class="price">1 025 000 zł</span></div>
            <ul class="parameters">
                <li class="parameter"><span>Powierzchnia:</span><b>58.5 m²</b></li>
                <li class="parameter"><span>Liczba pokoi:</span><b>3</b></li>
                <li class="parameter"><span>Piętro:</span><b>3/10</b></li>
                <li class="parameter"><span>Winda:</span><b>Tak</b></li>
                <li class="parameter"><span>Rok budowy:</span><b>1982</b></li>
                <li class="parameter"><span>Typ ogłoszeniodawcy:</span><b>Biuro nieruchomości</b></li>
            </ul>
        </body>
        </html>
        """
        payload = provider.parse_detail_page(mock_detail_html, "https://gratka.pl/nieruchomosci/ob/28941032", "28941032", default_district="Ursynów")

        self.assertEqual(payload["id"], "28941032")
        self.assertEqual(payload["title"], "3 pokoje z windą i balkonem, Ursynów Imielin")
        self.assertEqual(payload["price_pln"], 1025000.0)
        self.assertEqual(payload["area_m2"], 58.5)
        self.assertEqual(payload["rooms"], 3)
        self.assertEqual(payload["floor"], 3)
        self.assertEqual(payload["total_floors"], 10)
        self.assertEqual(payload["has_elevator"], 1)
        self.assertEqual(payload["build_year"], 1982)
        self.assertEqual(payload["location"]["coordinates"]["latitude"], 52.1456)
        self.assertEqual(payload["location"]["coordinates"]["longitude"], 21.0392)
        self.assertEqual(payload["location"]["district"], "Ursynów")

    def test_gratka_price_filtering(self):
        """Test filtracji ceny min/max (1,000,000 - 1,050,000 PLN) dla ofert z Gratki"""
        self.insert_sample_gratka_raw("gr_cheap", "Za tanie mieszkanie", 950000, 55, 3, 2, 4, 1, 1990, "Agencja")
        self.insert_sample_gratka_raw("gr_target", "Właściwa oferta Gratka", 1025000, 58, 3, 3, 10, 1, 1982, "Agencja")
        self.insert_sample_gratka_raw("gr_expensive", "Za drogie mieszkanie", 1100000, 65, 3, 4, 10, 1, 2005, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "gr_target")
        self.assertEqual(results[0]["price_pln"], 1025000.0)

    def test_gratka_rooms_and_elevator(self):
        """Test wymogu 3 pokoi oraz obecności windy (has_elevator = 1)"""
        self.insert_sample_gratka_raw("gr_ok", "Mieszkanie 3 pokoje z windą", 1020000, 58, 3, 3, 8, 1, 1985, "Agencja")
        self.insert_sample_gratka_raw("gr_no_elevator", "Mieszkanie 3 pokoje bez windy", 1020000, 58, 3, 3, 4, 0, 1985, "Agencja")
        self.insert_sample_gratka_raw("gr_2rooms", "Mieszkanie 2 pokoje z windą", 1020000, 48, 2, 3, 8, 1, 1985, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.elevator = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "gr_ok")
        self.assertEqual(results[0]["rooms"], 3)
        self.assertEqual(results[0]["has_elevator"], 1)

    def test_gratka_ground_floor_exclusion(self):
        """Test wykluczenia parteru (floor > 0) dla ofert z Gratki"""
        self.insert_sample_gratka_raw("gr_ground", "Mieszkanie na parterze", 1020000, 58, 3, 0, 8, 1, 1985, "Agencja")
        self.insert_sample_gratka_raw("gr_floor2", "Mieszkanie na 2. piętrze", 1020000, 58, 3, 2, 8, 1, 1985, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.exclude_ground_floor = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "gr_floor2")
        self.assertEqual(results[0]["floor"], 2)

    def test_gratka_cross_portal_deduplication(self):
        """Test deduplikacji międzyserwisowej (Gratka + Otodom / Adresowo) w widoku Gold"""
        lat, lon = 52.148, 21.033
        area = 60.0
        rooms = 3

        # Oferta z Gratki
        self.insert_sample_gratka_raw("gr_dup_1", "3 pok Ursynów Dereniowa", 1020000, area, rooms, 3, 10, 1, 1980, "Agencja", lat=lat, lon=lon)

        # Ta sama oferta z Otodom (identyczne GPS + metraż + pokoje)
        self.db_manager.insert_bronze_listing(
            source_portal="otodom",
            external_id="ot_dup_1",
            city="Warszawa",
            chunk_name="warszawa_ursynow_wtorny",
            raw_payload={
                "title": "Przestronne 3 pokoje Ursynów Dereniowa",
                "price": {"value": 1020000},
                "area": {"value": area},
                "rooms": rooms,
                "floor": 3,
                "total_floors": 10,
                "features": {"elevator": 1},
                "location": {"city": "Warszawa", "district": "Ursynów", "coordinates": {"latitude": lat, "longitude": lon}},
                "seller_type": "Agencja"
            },
            run_id=self.run_id
        )

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        gold = results[0]
        self.assertEqual(gold["portal_occurrences_count"], 2)
        self.assertIn("gratka", gold["source_portals_list"])
        self.assertIn("otodom", gold["source_portals_list"])

    def test_gratka_novelty_detection_flag(self):
        """Test wykrywania nowości (is_new_listing) dla ofert Gratki między uruchomieniami"""
        run1 = "run_hist_001"
        run2 = self.run_id

        # Poprzednie uruchomienie
        self.insert_sample_gratka_raw("gr_old", "Stara oferta Gratka", 1020000, 58, 3, 2, 4, 1, 2010, "Agencja")
        conn = self.db_manager.get_connection()
        conn.cursor().execute("UPDATE bronze_listings SET run_id = ?, scraped_at = '2026-08-01 10:00:00' WHERE external_id = 'gr_old';", (run1,))
        conn.commit()

        # Bieżące uruchomienie (stara oferta powtórzona + nowa oferta)
        self.insert_sample_gratka_raw("gr_old", "Stara oferta Gratka", 1020000, 58, 3, 2, 4, 1, 2010, "Agencja")
        self.insert_sample_gratka_raw("gr_new", "Nowa oferta Gratka", 1030000, 62, 3, 4, 10, 1, 2015, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=run2)

        res_map = {r["external_id"]: r["is_new_listing"] for r in results}
        self.assertEqual(res_map.get("gr_old"), 0)
        self.assertEqual(res_map.get("gr_new"), 1)

    def test_gratka_completeness_audit(self):
        """Test zapisu i odczytu metryk w tabeli run_audit dla portalu Gratka"""
        self.db_manager.save_run_audit(
            run_id=self.run_id,
            source_portal="gratka",
            expected_total=45,
            saved_bronze=45
        )

        audits = self.db_manager.get_run_audits(self.run_id)
        gratka_audits = [a for a in audits if a["source_portal"] == "gratka"]
        self.assertEqual(len(gratka_audits), 1)
        self.assertEqual(gratka_audits[0]["expected_total"], 45)
        self.assertEqual(gratka_audits[0]["saved_bronze"], 45)
        self.assertEqual(gratka_audits[0]["completeness_pct"], 100.0)

if __name__ == "__main__":
    unittest.main()
