# Zadania Wdrożeniowe (Tasks): Integracja Portalu Nieruchomosci-online.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-nieruchomosci-online`  
**Status**: Gotowe do Realizacji (Ready for Implementation)  
**Dokument Powiązany**: [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-nieruchomosci-online/design.md)  

---

## Faza 1: Weryfikacja i Przygotowanie Schematu Bazy Danych (`src/db.py`)

- [x] **1.1. Weryfikacja Widoków `silver_listings` i `gold_listings` w SQLite**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/db.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py)
  - **Opis**: Upewnienie się, że widok `silver_listings` poprawnie mapuje znormalizowane klucze pierwszego poziomu (`price_pln`, `area_m2`, `rooms`, `floor`, `total_floors`, `has_elevator`, `build_year`, `seller_type`, `location.coordinates`) dla źródła `source_portal = 'nieruchomosci_online'` bez wprowadzania zmian łamiących dla Otodom i Adresowo.
  - **Kryteria Akceptacji**: Widoki tworzą się poprawnie w metodzie `init_db()`, a testy bazy danych przechodzą bez błędów.

---

## Faza 2: Implementacja Modułu `NieruchomosciOnlineProvider` (`src/providers/nieruchomosci_online.py`)

- [x] **2.1. Utworzenie Klasy `NieruchomosciOnlineProvider` i Generatora URL**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py)
  - **Opis**: Implementacja metody `build_search_url(city, district, page)` generującej adresy w autorskim schemacie pozycyjnym (`szukaj.html?3,mieszkanie,sprzedaz,[rynek],[miasto:dzielnica],[cena_min-cena_max],[metraz_min-metraz_max],[pokoje_min-pokoje_max]&p=N`) z zachowaniem 8 slotów pozycyjnych oraz metody `_normalize_slug()` usuwającej polskie znaki diakrytyczne.
  - **Kryteria Akceptacji**: Poprawne formatowanie URL dla dowolnej kombinacji parametrów z `kryteria.md`.

- [x] **2.2. Implementacja Pętli Pobierania Listingu (Faza 1 Ekstrakcji)**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py)
  - **Opis**: Pobieranie stron wyników wyszukiwania, obsługa paginacji (`&p=1`, `&p=2`, ...), ekstrakcja unikalnych linków do ofert oraz parsowanie zadeklarowanej liczby ogłoszeń (`expected_total`) z nagłówka wyników.
  - **Kryteria Akceptacji**: Ekstrakcja linków do ofert i zadeklarowanej liczby ofert dla każdej dzielnicy z `config.districts`.

- [x] **2.3. Implementacja Parsowania Szczegółów Ofert i JSON-LD (Faza 2 Ekstrakcji)**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py)
  - **Opis**: Pobranie pojedynczej karty ogłoszenia, ekstrakcja danych ze znaczników `application/ld+json` (`Offer`, `Place`, `Apartment`), tabeli parametrów technicznych w DOM (piętro, liczba pięter, rok budowy, winda, stan wykończenia) oraz rozszerzona detekcja windy z synonimami (`dźwig osobowy`, `cichobieżna winda`).
  - **Kryteria Akceptacji**: Budowa ustandaryzowanego obiektu `raw_payload` i zapis do tabeli `bronze_listings` metodą `db_manager.insert_bronze_listing()`.

- [x] **2.4. Zabezpieczenia Antybotowe, Odporność Sieciowa i Rejestracja Audytu**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py)
  - **Opis**: Wdrożenie pełnego zestawu nagłówków Chromium macOS, opóźnień czasowych (`time.sleep(0.2 - 0.4s)`), obsługi błędów HTTP 429/403 (Exponential Backoff), timeoutów oraz wywołania `save_run_audit` z sumaryczną liczbą ofert dla wszystkich sprawdzonych dzielnic.
  - **Kryteria Akceptacji**: Zapis audytu do `run_audit` bez przerywania działania pipeline'u w razie pojedynczego błędu sieciowego.

---

## Faza 3: Integracja w Pipeline Głównym (`main.py`)

- [x] **3.1. Rejestracja `NieruchomosciOnlineProvider` w `main.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/main.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/main.py)
  - **Opis**: Zaimportowanie i wywołanie `NieruchomosciOnlineProvider(config, db_manager).fetch_listings(run_id)` obok istniejących providerów (Otodom, Adresowo).
  - **Kryteria Akceptacji**: Poprawne pobranie zrzutu Nieruchomosci-online do Bronze i wyświetlenie audytu kompletności w konsoli.

---

## Faza 4: Testy Jednostkowe i Walidacja Kryteriów Biznesowych

- [x] **4.1. Przygotowanie Zestawu Testów Jednostkowych**
  - **Plik**: [`wyszukiwarka-nieruchomosci/tests/test_nieruchomosci_online_criteria.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/tests/test_nieruchomosci_online_criteria.py)
  - **Opis**: Utworzenie zestawu testów pokrywającego:
    1. `test_build_search_url_positional_format`: Weryfikacja 8 slotów pozycyjnych URL dla różnych wariantów kryteriów.
    2. `test_price_range_filtering`: Weryfikacja odcięcia cen min/max w warstwie Gold.
    3. `test_rooms_and_elevator_filtering`: Sprawdzenie reguły 3 pokoi oraz obecności windy (z JSON-LD i z opisu tekstowego).
    4. `test_ground_floor_exclusion`: Sprawdzenie odrzucenia parteru (`floor = 0`).
    5. `test_cross_portal_deduplication`: Sprawdzenie konsolidacji oferty występującej równolegle na Otodom i Nieruchomosci-online w widoku `gold_listings`.
    6. `test_completeness_audit_cumulative`: Sprawdzenie zapisu i sumowania metryk w tabeli `run_audit`.
  - **Kryteria Akceptacji**: Wszystkie testy jednostkowe przechodzą pomyślnie (`python3 -m unittest tests/test_nieruchomosci_online_criteria.py`).

---

## Faza 5: Weryfikacja Końcowa End-to-End

- [x] **5.1. Uruchomienie Pipeline'u i Weryfikacja Raportu**
  - **Komenda**: `python3 main.py`
  - **Opis**: Wykonanie pełnego cyklu ELT, sprawdzenie zapisu w `bronze_listings`, `silver_listings`, `gold_listings`, tabeli `run_audit` oraz wygenerowania raportu w katalogu `historia/`.
  - **Kryteria Akceptacji**: Nowy plik raportu w `historia/` zawiera zdeduplikowane oferty z portalu Nieruchomosci-online.pl.
