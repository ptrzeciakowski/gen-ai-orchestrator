#!/usr/bin/env python3
"""
Główny skrypt uruchomieniowy serwisu wyszukiwarka-nieruchomosci (Architektura ELT Bronze / Silver / Gold).
Odświeża listę ofert na żądanie na podstawie kryteria.md, integruje z RCN Warszawa i zapisuje nowy plik w historia/.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import CriteriaConfig
from src.db import DatabaseManager
from src.providers.commercial import CommercialProvider
from src.providers.direct import DirectProvider
from src.deduplicator import Deduplicator
from src.rcn_client import RCNClient
from src.report_generator import ReportGenerator

from datetime import datetime

def format_num_or_any(val):
    if val is None:
        return "Dowolny"
    return f"{val:,}"

def main():
    run_id = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    print(f"🏠 Uruchamianie Serwisu Wyszukiwarka Nieruchomości Warszawa (ELT Run: {run_id})...")
    
    # 1. Odczyt konfiguracji z kryteria.md i inicjalizacja bazy danych SQLite
    config = CriteriaConfig()
    db_manager = DatabaseManager()
    
    # Czyszczenie starych danych Bronze przed nowym uruchomieniem dla zachowania czystości izolacji
    db_manager.clear_bronze()
    print("🧹 Wyczyszczono warstwę Bronze przed nowym pobraniem.")
    print(f"✅ Baza danych SQLite gotowa w: {db_manager.db_path}")
    print(f"✅ Załadowano kryteria z: {config.filepath}")
    print(f"   Dzielnice: {', '.join(config.districts)}")
    
    min_p_str = format_num_or_any(config.min_price)
    max_p_str = format_num_or_any(config.max_price)
    print(f"   Zakres cenowy: {min_p_str} - {max_p_str} PLN")

    # 2. Pobieranie szerokiego strumienia ogłoszeń do warstwy Bronze (Extract & Load)
    comm_provider = CommercialProvider(config, db_manager=db_manager)
    direct_provider = DirectProvider(config, db_manager=db_manager)

    comm_saved = comm_provider.fetch_listings(run_id=run_id)
    direct_saved = direct_provider.fetch_listings(run_id=run_id)
    total_saved = comm_saved + direct_saved

    print(f"✅ Zapisano {total_saved} surowych realnych ogłoszeń z Otodom do Bronze (run_id: {run_id}).")

    # 3. Transformacja w widoku Silver i deduplikacja w widoku Gold
    dedup = Deduplicator(config=config, db_manager=db_manager)
    gold_listings = dedup.get_gold_listings()
    print(f"✅ Odczytano {len(gold_listings)} zdeduplikowanych i przefiltrowanych ofert z warstwy Gold (gold_listings).")

    # 4. Integracja z RCN Warszawa & Generowanie Raportu
    rcn_client = RCNClient()
    generator = ReportGenerator(config, rcn_client)
    report_file = generator.generate_report(gold_listings)

    print(f"\n🎉 Wygenerowano nowy raport historii w:")
    print(f"👉 {report_file}")

if __name__ == "__main__":
    main()
