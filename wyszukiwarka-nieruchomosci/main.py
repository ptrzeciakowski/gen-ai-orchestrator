#!/usr/bin/env python3
"""
Główny skrypt uruchomieniowy serwisu wyszukiwarka-nieruchomosci (Architektura ELT Bronze / Silver / Gold).
Odświeża listę ofert na podstawie kryteria.md, integruje z RCN Warszawa i zapisuje raport w historia/.

Obsługuje tryb inteligentnego buforowania (ELT Caching):
- Na poziomie providerów pobiera szeroki zrzut ofert wyłącznie po lokalizacji (np. Warszawa Ursynów).
- Filtry biznesowe (cena, metraż, pokoje, piętro, winda) są aplikowane w warstwie SQL (Gold).
- Umożliwia błyskawiczne przeliczanie raportów na istniejącej bazie bez ponownego scrapowania.
"""
import sys
import os
import argparse
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import CriteriaConfig
from src.db import DatabaseManager
from src.providers.commercial import CommercialProvider
from src.providers.direct import DirectProvider
from src.providers.adresowo import AdresowoProvider
from src.providers.gratka import GratkaProvider
from src.providers.morizon import MorizonProvider
from src.providers.nieruchomosci_online import NieruchomosciOnlineProvider
from src.providers.olx import OLXProvider
from src.deduplicator import Deduplicator
from src.rcn_client import RCNClient
from src.report_generator import ReportGenerator

def format_num_or_any(val):
    if val is None:
        return "Dowolny"
    return f"{val:,}"

def main():
    parser = argparse.ArgumentParser(description="Wyszukiwarka Nieruchomości Warszawa (Architektura ELT)")
    parser.add_argument("-r", "--refresh", action="store_true", help="Wymuś ponowne pobranie ofert z serwisów internetowych do warstwy Bronze")
    parser.add_argument("-c", "--cache", action="store_true", help="Użyj istniejącego zrzutu z warstwy Bronze bez scrapowania sieci")
    parser.add_argument("--info", action="store_true", help="Pokaż informacje o aktualnym stanie bazy danych Bronze")
    args = parser.parse_args()

    config = CriteriaConfig()
    db_manager = DatabaseManager()

    if args.info:
        info = db_manager.get_latest_bronze_info(city=config.city)
        if info:
            print(f"📊 Ostatni zrzut w Bronze: {info['last_scraped_at']} (run_id: {info['run_id']})")
            print(f"   Łącznie ofert w Bronze: {info['total_listings']}")
            for p, cnt in info['portals'].items():
                print(f"   - {p}: {cnt} ofert")
        else:
            print("ℹ️ Brak zrzutów w warstwie Bronze.")
        return

    print(f"🏠 Wyszukiwarka Nieruchomości Warszawa (ELT Pipeline)")
    print(f"✅ Baza danych SQLite: {db_manager.db_path}")
    print(f"✅ Załadowano kryteria z: {config.filepath}")
    print(f"   Lokalizacja (filtr bazowy): {config.city or 'Warszawa'} -> {', '.join(config.districts)}")
    
    min_p_str = format_num_or_any(config.min_price)
    max_p_str = format_num_or_any(config.max_price)
    print(f"   Filtry biznesowe Gold: {min_p_str} - {max_p_str} PLN, pokoje: {config.min_rooms or 'dowolnie'}-{config.max_rooms or 'dowolnie'}, winda: {'Tak' if config.elevator else 'Dowolnie'}")

    latest_info = db_manager.get_latest_bronze_info(city=config.city)
    should_scrape = False

    if args.refresh:
        should_scrape = True
    elif args.cache:
        should_scrape = False
    elif latest_info and latest_info["total_listings"] > 0:
        # Automatyczne wykrycie istniejących danych w bazie
        print(f"\n📦 Znaleziono istniejący zrzut w warstwie Bronze:")
        print(f"   - Data i czas zrzutu: {latest_info['last_scraped_at']} (run_id: {latest_info['run_id']})")
        print(f"   - Liczba zapisanych ofert: {latest_info['total_listings']} (rozkład: {latest_info['portals']})")
        print(f"   ⚡ Przeliczanie raportu na istniejących danych (0.1s)...")
        print(f"   💡 (Aby pobrać nowe dane z internetu, uruchom: python3 wyszukiwarka-nieruchomosci/main.py --refresh)")
        should_scrape = False
    else:
        should_scrape = True

    if should_scrape:
        run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        print(f"\n🌐 Pobieranie szerokiego strumienia ogłoszeń z serwisów (Bronze Ingestion: {run_id})...")
        
        comm_provider = CommercialProvider(config, db_manager=db_manager)
        direct_provider = DirectProvider(config, db_manager=db_manager)
        adresowo_provider = AdresowoProvider(config, db_manager=db_manager)
        gratka_provider = GratkaProvider(config, db_manager=db_manager)
        morizon_provider = MorizonProvider(config, db_manager=db_manager)
        nol_provider = NieruchomosciOnlineProvider(config, db_manager=db_manager)
        olx_provider = OLXProvider(config, db_manager=db_manager)

        comm_saved = comm_provider.fetch_listings(run_id=run_id)
        direct_saved = direct_provider.fetch_listings(run_id=run_id)
        adresowo_saved = adresowo_provider.fetch_listings(run_id=run_id)
        try:
            gratka_saved = gratka_provider.fetch_listings(run_id=run_id)
        except Exception as e_g:
            print(f"⚠️ Gratka.pl: {e_g}")
            gratka_saved = 0

        try:
            morizon_saved = morizon_provider.fetch_listings(run_id=run_id)
        except Exception as e_m:
            print(f"⚠️ Morizon.pl: {e_m}")
            morizon_saved = 0

        try:
            nol_saved = nol_provider.fetch_listings(run_id=run_id)
        except Exception as e_n:
            print(f"⚠️ Nieruchomosci-online.pl: {e_n}")
            nol_saved = 0

        try:
            olx_saved = olx_provider.fetch_listings(run_id=run_id)
        except Exception as e_o:
            print(f"⚠️ OLX.pl: {e_o}")
            olx_saved = 0

        total_saved = comm_saved + direct_saved + adresowo_saved + gratka_saved + morizon_saved + nol_saved + olx_saved
        print(f"✅ Zapisano {total_saved} surowych ogłoszeń do Bronze (Otodom: {comm_saved + direct_saved}, Adresowo: {adresowo_saved}, Gratka: {gratka_saved}, Morizon: {morizon_saved}, Nieruchomosci-online: {nol_saved}, OLX: {olx_saved}).")

        # Audyt Kompletności
        audits = db_manager.get_run_audits(run_id=run_id)
        for a in audits:
            portal = a.get('source_portal', '').capitalize()
            saved = a.get('saved_bronze', 0)
            expected = a.get('expected_total', 0)
            pct = a.get('completeness_pct', 100.0)
            print(f"📊 Audyt Kompletności {portal}: {saved}/{expected} ({pct}% kompletności w Bronze)")
    else:
        run_id = latest_info["run_id"]

    # 3. Transformacja w widoku Silver i rygorystyczna selekcja w widoku Gold
    print(f"\n⚙️ Aplikowanie filtrów biznesowych w warstwie Gold...")
    dedup = Deduplicator(config=config, db_manager=db_manager)
    gold_listings = dedup.get_gold_listings(run_id=run_id)
    print(f"✅ Wyselekcjonowano {len(gold_listings)} unikalnych ofert spełniających kryteria z {run_id}.")

    # 4. Integracja z RCN Warszawa & Generowanie Raportu
    rcn_client = RCNClient()
    generator = ReportGenerator(config, rcn_client)
    report_file = generator.generate_report(gold_listings)

    print(f"\n🎉 Wygenerowano raport w:")
    print(f"👉 {report_file}")

if __name__ == "__main__":
    main()
