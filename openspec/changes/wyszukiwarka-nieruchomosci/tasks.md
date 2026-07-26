# Tasks: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

## 1. Structure & Configuration Setup

- [x] 1.1 Utworzenie katalogu `wyszukiwarka-nieruchomosci/` z podkatalogami `historia/` i `src/`
- [x] 1.2 Utworzenie domyślnego pliku parametrów `wyszukiwarka-nieruchomosci/kryteria.md` z zakresem filtrowania dla Warszawy

## 2. Listing Scrapers & Providers Implementation

- [x] 2.1 Stworzenie parsera konfiguracyjnego `src/config.py` odczytującego `kryteria.md`
- [x] 2.2 Implementacja providera dla głównych portali (`src/providers/commercial.py` - Otodom, OLX, Morizon)
- [x] 2.3 Implementacja providera dla ogłoszeń bezpośrednich (`src/providers/direct.py` - Adresowo, Sprzedajemy, Lento)
- [x] 2.4 Stworzenie modułu deduplikacji i konsolidacji ofert (`src/deduplicator.py`)

## 3. RCN Transactional Data & Analysis Integration

- [x] 3.1 Implementacja modułu integracji z RCN Warszawa (`src/rcn_client.py` - pobieranie i wyliczanie średnich cen transakcyjnych m² w dzielnicach)
- [x] 3.2 Implementacja kalkulatora odchyleń cenowych (% odchylenia od RCN) i weryfikacji opłacalności

## 4. Report Generation & AI Recommendations

- [x] 4.1 Implementacja silnika generowania raportu `src/report_generator.py` z nazywaniem plików `YYYY-MM-DD-HH24MISS-oferty.md` w katalogu `historia/`
- [x] 4.2 Formułowanie sekcji **Rekomendacji AI** (Top 3 okazyjnych ofert, ocena potencjału negocjacyjnego vs RCN, analiza ryzyk)
- [x] 4.3 Przeprowadzenie uruchomienia na żądanie i weryfikacja wygenerowanego pliku historii
