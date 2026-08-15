"""
Dedykowany zestaw testów jednostkowych i walidacji kryteriów z kryteria.md dla OLXProvider i warstwy ELT.
"""
import unittest
import os
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.db import DatabaseManager
from src.deduplicator import Deduplicator
from src.config import CriteriaConfig
from src.providers.olx import OLXProvider

class TestOLXCriteria(unittest.TestCase):
    def setUp(self):
        self.db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "test_olx_listings.db")
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        self.db_manager = DatabaseManager(db_path=self.db_path)
        self.conn = self.db_manager.get_connection()
        self.run_id = "test_run_olx_001"

    def tearDown(self):
        self.conn.close()
        if os.path.exists(self.db_path):
            try:
                os.remove(self.db_path)
            except Exception:
                pass

    def insert_sample_olx_raw(self, ext_id, title, price, area, rooms, floor, total_floors, has_elevator, build_year, seller_type, district="Ursynów", lat=52.1485, lon=21.0452):
        """Pomocnicze wstawianie znormalizowanego ogłoszenia OLX do tabeli Bronze."""
        norm_payload = {
            "id": ext_id,
            "title": title,
            "url": f"https://www.olx.pl/d/oferta/{ext_id}.html",
            "price_pln": float(price) if price is not None else None,
            "area_m2": float(area) if area is not None else None,
            "rooms": int(rooms) if rooms is not None else None,
            "floor": int(floor) if floor is not None else None,
            "total_floors": int(total_floors) if total_floors is not None else None,
            "has_elevator": int(has_elevator) if has_elevator is not None else 0,
            "build_year": int(build_year) if build_year is not None else None,
            "seller_type": seller_type,
            "description_text": f"Opis ogłoszenia {title} na Ursynowie",
            "location": {
                "city": "Warszawa",
                "district": district,
                "coordinates": {
                    "latitude": lat,
                    "longitude": lon
                }
            },
            "raw_olx_data": {
                "id": ext_id,
                "title": title,
                "params": [
                    {"key": "price", "value": {"value": price}},
                    {"key": "m", "value": {"value": area}},
                    {"key": "rooms", "value": {"key": "three" if rooms == 3 else str(rooms)}},
                    {"key": "floor_select", "value": {"key": f"floor_{floor}" if floor is not None else "parter"}},
                    {"key": "elevator", "value": {"key": "yes" if has_elevator else "no"}}
                ]
            }
        }
        self.db_manager.insert_bronze_listing(
            source_portal="olx",
            external_id=ext_id,
            city="Warszawa",
            chunk_name=f"warszawa_{district.lower()}_olx",
            raw_payload=norm_payload,
            run_id=self.run_id
        )

    def test_olx_url_generation(self):
        """Test 1: Weryfikacja generowania URL z parametrami cenowymi, liczbą pokoi i paginacją."""
        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3

        provider = OLXProvider(config=cfg, db_manager=self.db_manager)

        # Strona 1
        url_p1 = provider.build_search_url(city="Warszawa", district="Ursynów", page=1)
        self.assertEqual("https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/q-ursynow/", url_p1)
        self.assertNotIn("page=1", url_p1)

        # Strona 2
        url_p2 = provider.build_search_url(city="Warszawa", district="Ursynów", page=2)
        self.assertEqual("https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa/q-ursynow/?page=2", url_p2)

    def test_olx_payload_normalization(self):
        """Test 2: Weryfikacja spłaszczania parametrów params do korzenia słownika O(1)."""
        provider = OLXProvider(db_manager=self.db_manager)

        raw_sample = {
            "id": "918273645",
            "title": "Mieszkanie 3 pokoje Ursynów Imielin blisko metra",
            "url": "/d/oferta/mieszkanie-3-pokoje-ursynow-imielin-CID3-ID12345.html",
            "description": "<p>Sprzedam bezpośrednio 3-pokojowe mieszkanie na Ursynowie. Budynek posiada nową windę. Rok budowy 1985.</p>",
            "params": [
                {"key": "price", "value": {"value": 1020000, "label": "1 020 000 zł"}},
                {"key": "m", "value": {"value": 58.5, "label": "58.5 m²"}},
                {"key": "rooms", "value": {"key": "three", "label": "3 pokoje"}},
                {"key": "floor_select", "value": {"key": "floor_2", "label": "2"}},
                {"key": "elevator", "value": {"key": "yes", "label": "Tak"}},
                {"key": "total_floors", "value": {"value": 10}},
                {"key": "build_year", "value": {"value": 1985}}
            ],
            "user": {
                "is_business": False
            },
            "location": {
                "city": {"name": "Warszawa"},
                "district": {"name": "Ursynów"}
            },
            "map": {
                "lat": 52.1485,
                "lon": 21.0452
            }
        }

        norm = provider._normalize_ad_payload(raw_sample)

        self.assertEqual(norm["id"], "918273645")
        self.assertEqual(norm["title"], "Mieszkanie 3 pokoje Ursynów Imielin blisko metra")
        self.assertEqual(norm["url"], "https://www.olx.pl/d/oferta/mieszkanie-3-pokoje-ursynow-imielin-CID3-ID12345.html")
        self.assertEqual(norm["price_pln"], 1020000.0)
        self.assertEqual(norm["area_m2"], 58.5)
        self.assertEqual(norm["rooms"], 3)
        self.assertEqual(norm["floor"], 2)
        self.assertEqual(norm["total_floors"], 10)
        self.assertEqual(norm["has_elevator"], 1)
        self.assertEqual(norm["build_year"], 1985)
        self.assertEqual(norm["seller_type"], "Bezpośrednio")
        self.assertEqual(norm["location"]["city"], "Warszawa")
        self.assertEqual(norm["location"]["district"], "Ursynów")
        self.assertEqual(norm["location"]["coordinates"]["latitude"], 52.1485)
        self.assertEqual(norm["location"]["coordinates"]["longitude"], 21.0452)
        self.assertIn("raw_olx_data", norm)

    def test_olx_price_and_rooms_filtering(self):
        """Test 3: Filtracja ofert z OLX po cenie (1.0M - 1.05M PLN) oraz liczbie pokoi (3 pokoje)."""
        # Oferta za tania (950k)
        self.insert_sample_olx_raw("olx_cheap", "Tanie mieszkanie", 950000, 55, 3, 2, 4, 1, 2010, "Bezpośrednio", lat=52.141, lon=21.041)
        # Oferta właściwa (1020k, 3 pokoje)
        self.insert_sample_olx_raw("olx_ok", "Właściwe mieszkanie", 1020000, 58, 3, 2, 4, 1, 2010, "Bezpośrednio", lat=52.142, lon=21.042)
        # Oferta za droga (1100k)
        self.insert_sample_olx_raw("olx_expensive", "Drogie mieszkanie", 1100000, 65, 3, 2, 4, 1, 2010, "Bezpośrednio", lat=52.143, lon=21.043)
        # Oferta 2-pokojowa w cenie (1020k)
        self.insert_sample_olx_raw("olx_2rooms", "2 pokoje mieszkanie", 1020000, 48, 2, 2, 4, 1, 2010, "Bezpośrednio", lat=52.144, lon=21.044)

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "olx_ok")
        self.assertEqual(results[0]["price_pln"], 1020000.0)
        self.assertEqual(results[0]["rooms"], 3)

    def test_olx_ground_floor_and_elevator_filtering(self):
        """Test 4: Wykluczenie parteru (floor = 0) oraz wymóg obecności windy (has_elevator = 1)."""
        # Oferta parter z windą (powinna odpaść przez exclude_ground_floor)
        self.insert_sample_olx_raw("olx_parter", "Parter z windą", 1020000, 58, 3, 0, 4, 1, 2010, "Bezpośrednio", lat=52.145, lon=21.045)
        # Oferta 2 piętro bez windy (powinna odpaść przez brak windy)
        self.insert_sample_olx_raw("olx_no_lift", "2 piętro bez windy", 1020000, 58, 3, 2, 4, 0, 2010, "Bezpośrednio", lat=52.146, lon=21.046)
        # Oferta 2 piętro z windą (spełnia wszystkie kryteria)
        self.insert_sample_olx_raw("olx_valid", "2 piętro z windą", 1020000, 58, 3, 2, 4, 1, 2010, "Bezpośrednio", lat=52.147, lon=21.047)

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3
        cfg.exclude_ground_floor = True
        cfg.elevator = True

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["external_id"], "olx_valid")

    def test_olx_cross_portal_deduplication(self):
        """Test 5: Scalenie oferty występującej równolegle na Otodom, Adresowo i OLX do 1 rekordu w Gold."""
        lat = 52.1485
        lon = 21.0452
        area = 58.5
        rooms = 3
        price = 1020000

        # 1. Wpis Otodom
        self.db_manager.insert_bronze_listing(
            source_portal="otodom",
            external_id="otodom_101",
            city="Warszawa",
            chunk_name="warszawa_ursynow_wtorny",
            raw_payload={
                "id": "otodom_101",
                "title": "Mieszkanie 3 pokoje Ursynów",
                "price": {"value": price},
                "area": {"value": area},
                "rooms": rooms,
                "floor": 2,
                "total_floors": 10,
                "has_elevator": 1,
                "location": {"city": "Warszawa", "district": "Ursynów", "coordinates": {"latitude": lat, "longitude": lon}},
                "seller_type": "Agencja"
            },
            run_id=self.run_id
        )

        # 2. Wpis Adresowo
        self.db_manager.insert_bronze_listing(
            source_portal="adresowo",
            external_id="adresowo_202",
            city="Warszawa",
            chunk_name="warszawa_ursynow_adresowo",
            raw_payload={
                "id": "adresowo_202",
                "title": "Mieszkanie 3 pokoje Ursynów",
                "price_pln": price,
                "area_m2": area,
                "rooms": rooms,
                "floor": 2,
                "total_floors": 10,
                "has_elevator": 1,
                "location": {"city": "Warszawa", "district": "Ursynów", "coordinates": {"latitude": lat, "longitude": lon}},
                "seller_type": "Agencja"
            },
            run_id=self.run_id
        )

        # 3. Wpis OLX
        self.insert_sample_olx_raw(
            ext_id="olx_303",
            title="Mieszkanie 3 pokoje Ursynów OLX",
            price=price,
            area=area,
            rooms=rooms,
            floor=2,
            total_floors=10,
            has_elevator=1,
            build_year=1985,
            seller_type="Bezpośrednio",
            district="Ursynów",
            lat=lat,
            lon=lon
        )

        cfg = CriteriaConfig()
        cfg.min_price = 1000000
        cfg.max_price = 1050000
        cfg.min_rooms = 3
        cfg.max_rooms = 3

        dedup = Deduplicator(config=cfg, db_manager=self.db_manager)
        results = dedup.get_gold_listings(run_id=self.run_id)

        self.assertEqual(len(results), 1)
        gold = results[0]
        self.assertEqual(gold["portal_occurrences_count"], 3)
        self.assertIn("otodom", gold["source_portals_list"])
        self.assertIn("adresowo", gold["source_portals_list"])
        self.assertIn("olx", gold["source_portals_list"])

    def test_olx_completeness_audit(self):
        """Test 6: Zapis i odczyt metryk kompletności z tabeli run_audit dla portalu OLX."""
        self.db_manager.save_run_audit(
            run_id=self.run_id,
            source_portal="olx",
            expected_total=54,
            saved_bronze=50
        )

        audits = self.db_manager.get_run_audits(self.run_id)
        olx_audits = [a for a in audits if a["source_portal"] == "olx"]

        self.assertEqual(len(olx_audits), 1)
        self.assertEqual(olx_audits[0]["expected_total"], 54)
        self.assertEqual(olx_audits[0]["saved_bronze"], 50)
        self.assertEqual(olx_audits[0]["completeness_pct"], 92.6)

    def test_olx_ssr_parser_multi_pattern(self):
        """Test 7: Test wielowariantowego parsera stanu SSR (__PRERENDERED_STATE__, window var, JSON-LD, Fallback)."""
        provider = OLXProvider(db_manager=self.db_manager)

        # Wariant 1: __PRERENDERED_STATE__ tag
        sample_state = {
            "props": {
                "pageProps": {
                    "data": {
                        "adSearch": {
                            "totalElements": 42,
                            "data": [
                                {
                                    "id": 111,
                                    "title": "Mieszkanie SSR 1",
                                    "url": "/d/oferta/mieszkanie-ssr-1-ID111.html",
                                    "params": [{"key": "price", "value": {"value": 1020000}}]
                                }
                            ]
                        }
                    }
                }
            }
        }
        html_script = f'<html><head><script id="__PRERENDERED_STATE__">{json.dumps(sample_state)}</script></head><body></body></html>'
        ads, exp_total = provider._extract_ads_and_meta(html_script)
        self.assertEqual(len(ads), 1)
        self.assertEqual(exp_total, 42)
        self.assertEqual(str(ads[0]["id"]), "111")

        # Wariant 2: window.__PRERENDERED_STATE__ assignment
        html_win = f'<html><head><script>window.__PRERENDERED_STATE__ = {json.dumps(sample_state)};</script></head></html>'
        ads2, exp_total2 = provider._extract_ads_and_meta(html_win)
        self.assertEqual(len(ads2), 1)
        self.assertEqual(exp_total2, 42)

        # Wariant 3: Fallback link harvester
        html_fallback = '<html><body><a href="/d/oferta/super-mieszkanie-ursynow-ID999.html">Oferta</a> Znaleziono 15 ogłoszeń</body></html>'
        ads3, exp_total3 = provider._extract_ads_and_meta(html_fallback)
        self.assertEqual(len(ads3), 1)
        self.assertEqual(ads3[0]["id"], "ID999")
        self.assertEqual(exp_total3, 15)

if __name__ == "__main__":
    unittest.main()
