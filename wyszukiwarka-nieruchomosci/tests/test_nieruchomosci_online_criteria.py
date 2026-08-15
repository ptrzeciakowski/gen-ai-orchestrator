"""
Dedykowany zestaw testów jednostkowych i walidacji kryteriów z kryteria.md dla NieruchomosciOnlineProvider i warstwy ELT.
"""
import unittest
import os
import sys
import json
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager
from src.deduplicator import Deduplicator
from src.config import CriteriaConfig
from src.providers.nieruchomosci_online import NieruchomosciOnlineProvider

class TestNieruchomosciOnlineCriteria(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "test_nol_listings.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db_manager = DatabaseManager(db_path=self.db_path)
        self.conn = self.db_manager.get_connection()
        self.run_id = "test_run_nol_001"

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def insert_sample_nol_raw(self, ext_id, title, price, area, rooms, floor, total_floors, has_elevator, build_year, seller_type, district="Ursynów", lat=None, lon=None):
        if lat is None or lon is None:
            idx = abs(hash(ext_id)) % 1000
            lat = 52.14 + (idx * 0.001)
            lon = 21.05 + (idx * 0.001)
        raw = {
            "id": ext_id,
            "title": title,
            "url": f"https://www.nieruchomosci-online.pl/mieszkanie-na-sprzedaz/{ext_id}.html",
            "price_pln": price,
            "area_m2": area,
            "rooms": rooms,
            "floor": floor,
            "total_floors": total_floors,
            "has_elevator": has_elevator,
            "build_year": build_year,
            "seller_type": seller_type,
            "finish_status": "Do zamieszkania",
            "legal_status": "Pełna własność",
            "description_text": f"Opis ogłoszenia {title}",
            "location": {
                "city": "Warszawa",
                "district": district,
                "street": "ul. Przykładowa",
                "coordinates": {"latitude": lat, "longitude": lon}
            },
            "technical_details": {
                "has_elevator": bool(has_elevator),
                "build_year": build_year,
                "floor": floor,
                "total_floors": total_floors
            },
            "json_ld": []
        }
        self.db_manager.insert_bronze_listing(
            source_portal="nieruchomosci_online",
            external_id=ext_id,
            city="Warszawa",
            chunk_name=f"warszawa_{district.lower()}_nieruchomosci_online",
            raw_payload=raw,
            run_id=self.run_id
        )

    def test_build_search_url_positional_format(self):
        """Weryfikacja 8 slotów pozycyjnych URL dla szerokiej lokalizacji (Bronze)"""
        cfg = CriteriaConfig()
        provider = NieruchomosciOnlineProvider(cfg, db_manager=self.db_manager)
        
        # Test 1: Lokalizacja i strona 1
        url_p1 = provider.build_search_url("Warszawa", "Ursynów", page=1)
        self.assertTrue(url_p1.startswith("https://www.nieruchomosci-online.pl/szukaj.html?"))
        query_part = url_p1.split("?")[1]
        self.assertNotIn("&p=", query_part)
        
        slots = query_part.split(",")
        self.assertEqual(len(slots), 8, f"URL musi zawierać dokładnie 8 slotów pozycyjnych, otrzymano: {slots}")
        self.assertEqual(slots[0], "3")  # mode
        self.assertEqual(slots[1], "mieszkanie")
        self.assertEqual(slots[2], "sprzedaz")
        self.assertEqual(slots[4], "warszawa:ursynow")

        # Test 2: Paginacja strona 2
        url_p2 = provider.build_search_url("Warszawa", "Ursynów", page=2)
        self.assertTrue(url_p2.endswith("&p=2"))

        # Test 3: Normalizacja znaków diakrytycznych w dzielnicach i miastach
        url_srodmiescie = provider.build_search_url("Kraków", "Śródmieście", page=1)
        q_srodmiescie = url_srodmiescie.split("?")[1]
        slots_srod = q_srodmiescie.split(",")
        self.assertEqual(slots_srod[4], "krakow:srodmiescie")

        url_bialoleka = provider.build_search_url("Warszawa", "Białołęka", page=1)
        q_bialoleka = url_bialoleka.split("?")[1]
        slots_bial = q_bialoleka.split(",")
        self.assertEqual(slots_bial[4], "warszawa:bialoleka")

    def test_parse_listing_html(self):
        """Test parsowania kodu HTML listy wyników wyszukiwania (nagłówek i linki do ofert)"""
        html_sample = """
        <!DOCTYPE html>
        <html>
        <head><title>Mieszkania na sprzedaż</title></head>
        <body>
            <div class="search-header">
                znaleziono <strong>42</strong> ogłoszeń mieszkania na sprzedaż
            </div>
            <div class="results-list">
                <a href="/mieszkanie-na-sprzedaz/24598123.html">Oferta 1</a>
                <a href="https://warszawa.nieruchomosci-online.pl/mieszkanie-na-sprzedaz/24598124.html">Oferta 2</a>
                <a href="/szukaj.html?3,mieszkanie">Inny link</a>
                <a href="/mieszkanie-na-sprzedaz/24598123.html">Duplikat linku</a>
            </div>
        </body>
        </html>
        """
        cfg = CriteriaConfig()
        provider = NieruchomosciOnlineProvider(cfg, db_manager=self.db_manager)
        expected_total, offer_urls = provider.parse_listing_html(html_sample)

        self.assertEqual(expected_total, 42)
        self.assertEqual(len(offer_urls), 2)
        self.assertIn("https://www.nieruchomosci-online.pl/mieszkanie-na-sprzedaz/24598123.html", offer_urls)
        self.assertIn("https://warszawa.nieruchomosci-online.pl/mieszkanie-na-sprzedaz/24598124.html", offer_urls)

    def test_parse_detail_html_with_json_ld_and_table(self):
        """Test parsowania szczegółów oferty z JSON-LD, tabeli technicznej i synonimów windy"""
        html_sample = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>3 pokoje z cichobieżną windą, Ursynów</title>
            <script type="application/ld+json">
            {
                "@context": "https://schema.org",
                "@graph": [
                    {
                        "@type": "Place",
                        "name": "Przestronne 3 pokoje Warszawa Ursynów",
                        "description": "Piękne mieszkanie na 3 piętrze z cichobieżną windą.",
                        "address": {
                            "@type": "PostalAddress",
                            "addressLocality": "Warszawa",
                            "addressRegion": "Ursynów",
                            "streetAddress": "ul. Dereniowa 10"
                        },
                        "geo": {
                            "@type": "GeoCoordinates",
                            "latitude": 52.1445,
                            "longitude": 21.0421
                        }
                    },
                    {
                        "@type": "Offer",
                        "price": "1025000",
                        "priceCurrency": "PLN"
                    },
                    {
                        "@type": "Apartment",
                        "floorSize": {
                            "@type": "QuantitativeValue",
                            "value": 56.4
                        },
                        "numberOfRooms": 3,
                        "yearBuilt": 1982
                    }
                ]
            }
            </script>
        </head>
        <body>
            <h1>Przestronne 3 pokoje Warszawa Ursynów</h1>
            <div class="technical-table">
                <span>Piętro: 3 z 10</span>
                <span>Rok budowy: 1982</span>
                <span>Winda: dzwig osobowy</span>
                <span>Ogłoszenie prywatne - bez pośredników</span>
            </div>
        </body>
        </html>
        """
        cfg = CriteriaConfig()
        provider = NieruchomosciOnlineProvider(cfg, db_manager=self.db_manager)
        payload = provider.parse_detail_html(
            html=html_sample,
            url="https://warszawa.nieruchomosci-online.pl/mieszkanie-na-sprzedaz/24598123.html",
            default_city="Warszawa",
            default_district="Ursynów"
        )

        self.assertEqual(payload["id"], "24598123")
        self.assertEqual(payload["price_pln"], 1025000.0)
        self.assertEqual(payload["area_m2"], 56.4)
        self.assertEqual(payload["rooms"], 3)
        self.assertEqual(payload["floor"], 3)
        self.assertEqual(payload["total_floors"], 10)
        self.assertEqual(payload["has_elevator"], 1)
        self.assertEqual(payload["build_year"], 1982)
        self.assertEqual(payload["seller_type"], "Bezpośrednio")
        self.assertEqual(payload["location"]["city"], "Warszawa")
        self.assertEqual(payload["location"]["district"], "Ursynów")
        self.assertEqual(payload["location"]["coordinates"]["latitude"], 52.1445)
        self.assertEqual(payload["location"]["coordinates"]["longitude"], 21.0421)

    def test_price_range_filtering(self):
        """Test filtracji ceny min/max w warstwie Gold dla ofert Nieruchomosci-online"""
        self.insert_sample_nol_raw("nol_1", "Za tanie", 950000, 50, 3, 2, 4, 1, 2010, "Agencja")
        self.insert_sample_nol_raw("nol_2", "W sam raz", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja")
        self.insert_sample_nol_raw("nol_3", "Za drogie", 1100000, 60, 3, 2, 4, 1, 2010, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "nol_2")
        self.assertEqual(results[0]["source_portal"], "nieruchomosci_online")

    def test_rooms_and_elevator_filtering(self):
        """Test liczby pokoi (3 pokoje) oraz obecności windy (winda/dźwig osobowy)"""
        # Oferta 3 pokoje Z windą
        self.insert_sample_nol_raw("nol_lift", "3 pokoje z windą", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja")
        # Oferta 3 pokoje BEZ windy
        self.insert_sample_nol_raw("nol_nolift", "3 pokoje bez windy", 1020000, 55, 3, 2, 3, 0, 2010, "Agencja")
        # Oferta 2 pokoje Z windą
        self.insert_sample_nol_raw("nol_2rooms", "2 pokoje z windą", 1020000, 45, 2, 2, 4, 1, 2010, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.elevator = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "nol_lift")

    def test_ground_floor_exclusion(self):
        """Test wykluczenia parteru (floor > 0) w warstwie Gold"""
        self.insert_sample_nol_raw("nol_parter", "Parter", 1020000, 55, 3, 0, 4, 1, 2010, "Agencja")
        self.insert_sample_nol_raw("nol_pietro", "Piętro 2", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.exclude_ground_floor = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "nol_pietro")

    def test_cross_portal_deduplication(self):
        """Test deduplikacji międzyserwisowej między Otodom, Adresowo a Nieruchomosci-online"""
        # Oferta Otodom
        self.db_manager.insert_bronze_listing(
            source_portal="otodom",
            external_id="oto_100",
            city="Warszawa",
            chunk_name="warszawa_ursynow_otodom",
            raw_payload={
                "title": "Mieszkanie 3 pokoje Ursynów Imielin",
                "price_pln": 1020000,
                "area_m2": 56.4,
                "rooms": 3,
                "floor": 3,
                "total_floors": 10,
                "has_elevator": 1,
                "location": {"city": "Warszawa", "district": "Ursynów", "coordinates": {"latitude": 52.1445, "longitude": 21.0421}},
                "seller_type": "Agencja"
            },
            run_id=self.run_id
        )

        # Ta sama oferta na Nieruchomosci-online (te same koordynaty, metraż, pokoje)
        self.insert_sample_nol_raw(
            ext_id="nol_24598123",
            title="3 pokoje z balkonem i windą, Ursynów",
            price=1025000,  # nieznacznie inna cena na portalu
            area=56.4,
            rooms=3,
            floor=3,
            total_floors=10,
            has_elevator=1,
            build_year=1982,
            seller_type="Agencja",
            district="Ursynów",
            lat=52.1445,
            lon=21.0421
        )

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        # Obie oferty powinny zostać skonsolidowane do 1 wiersza w Gold
        self.assertEqual(len(results), 1)
        gold_item = results[0]
        self.assertEqual(gold_item["portal_occurrences_count"], 2)
        self.assertIn("otodom:oto_100", gold_item["source_portals_list"])
        self.assertIn("nieruchomosci_online:nol_24598123", gold_item["source_portals_list"])
        self.assertEqual(gold_item["min_price_pln"], 1020000.0)
        self.assertEqual(gold_item["max_price_pln"], 1025000.0)

    def test_completeness_audit_cumulative(self):
        """Test rejestracji i sumowania audytu kompletności (run_audit) dla wielu dzielnic"""
        cfg = CriteriaConfig()
        cfg.districts = ["Ursynów", "Mokotów"]
        provider = NieruchomosciOnlineProvider(cfg, db_manager=self.db_manager)
        provider.max_pages = 1

        mock_listing_ursynow = """
        <html><body>
            znaleziono <strong>25</strong> ogłoszeń
            <a href="/mieszkanie-na-sprzedaz/111.html">O1</a>
            <a href="/mieszkanie-na-sprzedaz/222.html">O2</a>
        </body></html>
        """
        mock_listing_mokotow = """
        <html><body>
            znaleziono <strong>35</strong> ogłoszeń
            <a href="/mieszkanie-na-sprzedaz/333.html">O3</a>
        </body></html>
        """
        mock_detail = """
        <html><body>
            <h1>Mieszkanie testowe</h1>
            <span>Cena: 1 020 000 zł</span>
            <span>Powierzchnia: 55 m²</span>
            <span>3 pokoje</span>
            <span>Winda: tak</span>
        </body></html>
        """

        def mock_urlopen(req, timeout=None):
            url = req.full_url if hasattr(req, 'full_url') else str(req)
            m_resp = MagicMock()
            if "ursynow" in url:
                m_resp.read.return_value = mock_listing_ursynow.encode('utf-8')
            elif "mokotow" in url:
                m_resp.read.return_value = mock_listing_mokotow.encode('utf-8')
            else:
                m_resp.read.return_value = mock_detail.encode('utf-8')
            m_resp.__enter__.return_value = m_resp
            return m_resp

        with patch('urllib.request.urlopen', side_effect=mock_urlopen):
            with patch('time.sleep', return_value=None):
                saved = provider.fetch_listings(run_id=self.run_id)

        self.assertEqual(saved, 3)
        audits = self.db_manager.get_run_audits(self.run_id)
        self.assertEqual(len(audits), 1)
        audit_entry = audits[0]
        self.assertEqual(audit_entry["source_portal"], "nieruchomosci_online")
        self.assertEqual(audit_entry["expected_total"], 60)  # 25 (Ursynów) + 35 (Mokotów) = 60
        self.assertEqual(audit_entry["saved_bronze"], 3)
        self.assertEqual(audit_entry["completeness_pct"], 5.0)

    def test_novelty_detection_flag(self):
        """Test flagi nowości is_new_listing dla ofert Nieruchomosci-online"""
        run1 = "run_nol_hist_001"
        run2 = "run_nol_curr_002"

        # Uruchomienie 1: Oferta A
        self.insert_sample_nol_raw("nol_old", "Stara oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja")
        conn = self.db_manager.get_connection()
        conn.cursor().execute("UPDATE bronze_listings SET run_id = ?, scraped_at = '2026-08-01 10:00:00' WHERE external_id = 'nol_old';", (run1,))
        conn.commit()

        # Uruchomienie 2: Oferta A (powtórzona w nowym runie) oraz Oferta B (nowa)
        self.insert_sample_nol_raw("nol_old", "Stara oferta", 1020000, 55, 3, 2, 4, 1, 2010, "Agencja")
        self.insert_sample_nol_raw("nol_new", "Nowa oferta", 1030000, 58, 3, 3, 4, 1, 2012, "Agencja")

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        res_map = {r["external_id"]: r["is_new_listing"] for r in results}
        self.assertEqual(res_map.get("nol_old"), 0)
        self.assertEqual(res_map.get("nol_new"), 1)

if __name__ == "__main__":
    unittest.main()
