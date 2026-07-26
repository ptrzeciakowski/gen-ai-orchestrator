# Tasks: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

## 1. Structure & Configuration Setup

- [x] 1.1 Utworzenie katalogu `wyszukiwarka-nieruchomosci/` z podkatalogami `historia/` i `src/`
- [x] 1.2 Utworzenie pliku parametrów `wyszukiwarka-nieruchomosci/kryteria.md` z zakresem filtrowania dla Warszawy oraz filtrem typu ogłoszeniodawcy (`Bezpośrednio` vs `Agencja`)

## 2. Listing Scrapers & Providers Implementation

- [x] 2.1 Stworzenie parsera konfiguracyjnego `src/config.py` odczytującego `kryteria.md` z obsługą słów kluczowych odmianowych ("dowolny", "dowolna", "dowolne", "brak limitu") i wczytywaniem raw_content
- [x] 2.2 Implementacja providera dla głównych portali (`src/providers/commercial.py` - Otodom, OLX, Morizon) z odczytem autentycznych, klikalnych linków URL i elastycznym filtrowaniem `None`
- [x] 2.3 Implementacja providera dla ogłoszeń bezpośrednich bez pośredników (`src/providers/direct.py` - Adresowo, Sprzedajemy, Lento) z odczytem żywych linków i elastycznym filtrowaniem
- [x] 2.4 Stworzenie modułu deduplikacji i konsolidacji ofert (`src/deduplicator.py`) z priorytetyzacją ofert bezpośrednich

## 3. RCN Transactional Data & Analysis Integration

- [x] 3.1 Implementacja modułu integracji z RCN Warszawa (`src/rcn_client.py` - pobieranie danych z aktów notarialnych m.st. Warszawy dla dzielnic oraz obszarów MSI np. Kabaty, Natolin, Służew, Filtry z fallbackiem dla całej dzielnicy)
- [x] 3.2 Implemetacja 7-elementowej analizy kwantylowej RCN ($N$ transakcji, Średnia, P10, P25, Mediana P50, P75, P90, P95, P99)
- [x] 3.3 Dodanie próbek surowych wpisów z aktów notarialnych RCN (ulica, m², cena PLN, cena PLN/m², nr aktu notarialnego) dla pełnej weryfikacji rzetelności danych
- [x] 3.4 Implementacja kalkulatora odchyleń cenowych (% odchylenia od RCN) i weryfikacji opłacalności

## 4. Report Generation, TOC & Formatting Audit Trail

- [x] 4.1 Implementacja silnika generowania raportu `src/report_generator.py` ze spisem treści (TOC), czytelnym meandrycznym czasem HH:MM:SS i bezpośrednim wklejeniem surowej zawartości `kryteria.md`
- [x] 4.2 Przeniesienie sekcji **Statystyki RCN Warszawa** na sam koniec dokumentu (po sekcji Rekomendacji AI)
- [x] 4.3 Formułowanie sekcji **Rekomendacji AI** (Top 3 okazyjnych ofert, ocena potencjału negocjacyjnego vs kwantyle RCN, analiza ryzyk prawnych i budowlanych)
- [x] 4.4 Przeprowadzenie uruchomienia na żądanie i weryfikacja wygenerowanego pliku historii z działającymi linkami, ofertami rynkowymi i próbką notarialną RCN
