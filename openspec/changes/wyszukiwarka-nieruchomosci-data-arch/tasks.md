# Plan Wdrożeniowy OpenSpec (Tasks): Architektura Danych ELT (MVP Opcja 1)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-data-arch`  
**Data**: 27 Lipca 2026  
**Status**: Plan Wdrożeniowy (Tasks)  
**Dokumenty Referencyjne**:
- `file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-data-arch/design.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-data-arch/proposal.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`

---

## 🏗️ Faza 1: Warstwa Bazy Danych i Funkcje Pomocnicze SQLite

- [ ] **Moduł Bazy Danych (`wyszukiwarka-nieruchomosci/src/db.py`)**
  - Stwórz plik `wyszukiwarka-nieruchomosci/src/db.py` zawierający klasę `DatabaseManager`.
  - Zaimplementuj metodę `get_connection()` z obsługą automatycznego tworzenia bazy `wyszukiwarka-nieruchomosci/data/listings.db` oraz katalogu parent.
  - Zarejestruj customową funkcję matematyczną `haversine_m(lat1, lon1, lat2, lon2)` oraz `regexp(pattern, text)` w połączeniu SQLite (`conn.create_function`).
  - **Kryterium Akceptacji**: `haversine_m(52.148, 21.033, 52.150, 21.035)` zwraca dystans w metrach z dokładnością do 1m.
  - **Weryfikacja**: `python -c "from src.db import DatabaseManager; db = DatabaseManager(); print(db.test_connection())"`

- [ ] **DDL Tabeli Bronze (`bronze_listings`)**
  - W `wyszukiwarka-nieruchomosci/src/db.py` zaimplementuj tworzenie tabeli `bronze_listings` ze stałym kluczem unikalnym `UNIQUE(source_portal, external_id) ON CONFLICT REPLACE`.
  - Dodaj indeks B-drzewa na kolumnach `(source_portal, external_id)`.
  - **Kryterium Akceptacji**: Ponowne wstawienie oferty o tym samym `external_id` aktualizuje payload i timestamp zamiast wyrzucać błąd unikalności.
  - **Weryfikacja**: Test jednostkowy SQLite DDL.

- [ ] **DDL Widoków Silver (`silver_listings`) i Gold (`gold_listings`)**
  - W `wyszukiwarka-nieruchomosci/src/db.py` zaimplementuj inicjalizację widoku `silver_listings` wykorzystującego `json_extract()` i dynamiczną aplikację parametrów z `kryteria.md`.
  - Zaimplementuj widok `gold_listings` realizujący grupowanie i deduplikację międzyserwisową po unikalnym hahu geolokalizacyjno-metrażowym.
  - **Kryterium Akceptacji**: Zapytanie `SELECT COUNT(*) FROM silver_listings` zwraca wyłącznie rekordy spełniające filtry z `kryteria.md`.

---

## 🌐 Faza 2: Refaktoryzacja Ekstrakcji i Ładowania (Extract & Load - Bronze)

- [ ] **Szerokie Pobieranie w CommercialProvider (`wyszukiwarka-nieruchomosci/src/providers/commercial.py`)**
  - Przerób metodę `fetch_listings()` w `CommercialProvider` tak, aby zapisywała surowe obiekty JSON do tabeli `bronze_listings` via `DatabaseManager`.
  - Wdrożyć strategię *Extraction Chunks* (pobieranie po szerokim parametrze miasto Warszawa, podzielone na pod-strumienie rynek pierwotny / wtórny).
  - Usunąć wstępną filtrację cenową, wykluczanie parterów i sprawdzanie wind w kodzie Pythona – przenieść całą odpowiedzialność do bazy danych.
  - **Kryterium Akceptacji**: Każda pobrana odpowiedź JSON ląduje w tabeli `bronze_listings` bez modyfikacji.
  - **Weryfikacja**: Sprawdzenie liczby rekordów: `sqlite3 data/listings.db "SELECT count(*) FROM bronze_listings;"`

- [ ] **Obsługa Surowych Obiektów w DirectProvider (`wyszukiwarka-nieruchomosci/src/providers/direct.py`)**
  - Dostosuj interfejs `DirectProvider` do spójnego zapisu rekordów w tabeli `bronze_listings`.

---

## 📊 Faza 3: Warstwa Analityki, Deduplikacji i Raportowania (Transform & Reporting)

- [ ] **Deduplikacja via Widok Gold (`wyszukiwarka-nieruchomosci/src/deduplicator.py`)**
  - Przeprojektuj `Deduplicator` tak, aby odczytywał gotowe pogrupowane wyniki bezpośrednio z widoku `gold_listings` bazy SQLite zamiast przetwarzać tablice w pamięci RAM Pythona.
  - **Kryterium Akceptacji**: Wynik deduplikacji jest w 100% spójny z zapytaniem SQL `SELECT * FROM gold_listings`.

- [ ] **Orkiestracja i Raportowanie (`wyszukiwarka-nieruchomosci/src/report_generator.py` & `main.py`)**
  - Zaktualizuj `main.py` oraz `report_generator.py` do pobierania przetworzonych ofert bezpośrednio z SQLite z warstwy Gold.
  - Zachowaj integrację z klientem RCN Warszawa (`rcn_client.py`) do wzbogacania danych o średnie ceny transakcyjne z danej dzielnicy.
  - Zapisz wygenerowany raport HTML / Markdown w katalogu `wyszukiwarka-nieruchomosci/historia/`.
  - **Kryterium Akceptacji**: Uruchomienie `python wyszukiwarka-nieruchomosci/main.py` generuje poprawny plik w `historia/`.

---

## ✅ Faza 4: Weryfikacja End-to-End i Audyt Zgodności

- [ ] **Testy Jednostkowe i Integracyjne (`wyszukiwarka-nieruchomosci/tests/`)**
  - Stwórz pakiet testowy `tests/test_elt_pipeline.py` weryfikujący poprawność działania widoku `silver_listings` na przygotowanych próbkach surowych JSON-ów.
  - Przetestuj zachowanie przy braku pola `total_floors` oraz z uszkodzonymi obiektami JSON.
  - **Weryfikacja**: `pytest wyszukiwarka-nieruchomosci/tests/` lub uruchomienie dedykowanego runnera testów.

- [ ] **Empiryczna Weryfikacja Działania Pipeline'u**
  - Uruchomienie pełnego odświeżenia: `python wyszukiwarka-nieruchomosci/main.py`.
  - Upewnienie się, że brak jest wyciętych błędów runtime i że spadek wydajności zapytań w widoku Silver wynosi <200ms.
