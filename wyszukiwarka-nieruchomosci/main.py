#!/usr/bin/env python3
"""
Główny skrypt uruchomieniowy serwisu wyszukiwarka-nieruchomosci.
Odświeża listę ofert na żądanie na podstawie kryteria.md, integruje z RCN Warszawa i zapisuje nowy plik w historia/.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import CriteriaConfig
from src.providers.commercial import CommercialProvider
from src.providers.direct import DirectProvider
from src.deduplicator import Deduplicator
from src.rcn_client import RCNClient
from src.report_generator import ReportGenerator

def format_num_or_any(val):
    if val is None:
        return "Dowolny"
    return f"{val:,}"

def main():
    print("🏠 Uruchamianie Serwisu Wyszukiwarka Nieruchomości Warszawa...")
    
    # 1. Odczyt konfiguracji z kryteria.md
    config = CriteriaConfig()
    print(f"✅ Załadowano kryteria z: {config.filepath}")
    print(f"   Dzielnice: {', '.join(config.districts)}")
    
    min_p_str = format_num_or_any(config.min_price)
    max_p_str = format_num_or_any(config.max_price)
    print(f"   Zakres cenowy: {min_p_str} - {max_p_str} PLN")

    # 2. Pobieranie ofert z providerów
    comm_provider = CommercialProvider(config)
    direct_provider = DirectProvider(config)

    raw_listings = []
    comm_listings = comm_provider.fetch_listings()
    direct_listings = direct_provider.fetch_listings()

    raw_listings.extend(comm_listings)
    raw_listings.extend(direct_listings)
    print(f"✅ Pobrano {len(raw_listings)} ofert z portali (Otodom, OLX, Morizon, Adresowo, Sprzedajemy, Lento).")

    # 3. Deduplikacja
    dedup = Deduplicator()
    unique_listings = dedup.deduplicate(raw_listings)
    print(f"✅ Zredukowano duplikaty do {len(unique_listings)} unikalnych ofert.")

    # 4. Integracja z RCN Warszawa & Generowanie Raportu
    rcn_client = RCNClient()
    generator = ReportGenerator(config, rcn_client)
    report_file = generator.generate_report(unique_listings)

    print(f"\n🎉 Wygenerowano nowy raport historii w:")
    print(f"👉 {report_file}")

if __name__ == "__main__":
    main()
