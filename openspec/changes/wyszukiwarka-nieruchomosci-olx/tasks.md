# Plan Implementacji i Zadania: Integracja Serwisu OLX.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-olx`  
**Status**: Zaplanowane (Ready for Implementation)  
**Dokumenty Referencyjne**:
- [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-olx/proposal.md)
- [design.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-olx/design.md)
- [kryteria.md](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md)
- [db.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py)

---

## 📋 Lista Zadań Wdrożeniowych (Task Breakdown)

### Faza 1: Moduł Providera OLX (`src/providers/olx.py`)

- [ ] **1.1. Konstrukcja klasy `OLXProvider` i generatora URL (`build_search_url`)**
  - Implementacja klasy `OLXProvider(config, db_manager)` przyjmującej obiekt konfiguracji i instancję bazy danych.
  - Metoda `build_search_url(city_slug, district_slug, page)` generująca adres URL z filtrami:
    - `search[filter_float_price:from]` i `search[filter_float_price:to]`
    - `search[filter_enum_rooms][0]=three` (oraz odpowiedniki dla innych konfiguracji pokoi)
    - Paginacja `page=N`

- [ ] **1.2. Wielowariantowy parser stanu SSR i ekstrakcja danych (`_extract_ads_and_meta`)**
  - Pobieranie strony z nagłówkami przeglądarki Chrome na macOS (`User-Agent`, `Sec-Ch-Ua`, `Accept`).
  - Łańcuch parserów:
    1. Znacznik `<script id="__PRERENDERED_STATE__"[^>]*>(.*?)</script>`
    2. Przypisanie `window.__PRERENDERED_STATE__\s*=\s*"?(\{.*?\})"?;`
    3. Bloki JSON-LD Schema.org
    4. Fallback link harvester `href="(/d/oferta/[^"]+)"`
  - Ekstrakcja deklarowanej liczby ofert (`totalElements`) do zmiennej audytowej `expected_total_olx`.

- [ ] **1.3. Pre-normalizacja parametrów $O(1)$ w Pythonie (`_normalize_ad_payload`)**
  - Spłaszczenie tablicy `params` z OLX do zunifikowanych kluczy w korzeniu słownika przed zapisem do Bronze:
    - `price_pln` (z `price.value` lub `params.price`)
    - `area_m2` (z `params.m`)
    - `rooms` (mapowanie: `one` -> 1, `two` -> 2, `three` -> 3, `four` -> 4, `five` -> 5)
    - `floor` (mapowanie: `floor_0` -> 0, `floor_1` -> 1, ..., `floor_higher` -> 12, parter -> 0)
    - `has_elevator` (z `params.elevator` lub regex opisu `winda`)
    - `seller_type` (`user.is_business == 0` -> 'Bezpośrednio', `user.is_business == 1` -> 'Agencja')
    - `location.coordinates` (`latitude`, `longitude`)
  - Zachowanie pełnego oryginalnego obiektu OLX w gałęzi `raw_olx_data`.

- [ ] **1.4. Pętla pobierania, obsługa błędów i rejestracja audytu (`fetch_listings`)**
  - Pętla po zdefiniowanych dzielnicach i stronach (do `max_pages`).
  - Obsługa Exponential Backoff na kody HTTP 429 i 403.
  - Zapis surowych znormalizowanych obiektów do `bronze_listings` za pomocą `db_manager.insert_bronze_listing`.
  - Rejestracja audytu kompletności: `db_manager.save_run_audit(run_id, "olx", expected_total_olx, saved_count)`.

---

### Faza 2: Integracja z Bazą Danych i Pipeline Głównym

- [ ] **2.1. Aktualizacja widoku `silver_listings` w `src/db.py`**
  - Weryfikacja i dostosowanie widoku `silver_listings` pod kątem zoptymalizowanego odczytu pól pierwszego poziomu.
  - Zapewnienie pełnej kompatybilności wstecznej dla providerów `otodom` i `adresowo`.

- [ ] **2.2. Wpięcie `OLXProvider` w `main.py`**
  - Import `OLXProvider` w `main.py`.
  - Inicjalizacja i wywołanie `olx_provider.fetch_listings(run_id=run_id)` w procesie zasilania warstwy Bronze.
  - Zliczenie i prezentacja całkowitego wolumenu pobranych ogłoszeń oraz wyświetlenie metryki z `run_audit`.

---

### Faza 3: Testy Jednostkowe i Walidacja Kryteriów

- [ ] **3.1. Utworzenie pliku testów `tests/test_olx_criteria.py`**
  - **Test 1 (`test_olx_url_generation`)**: Weryfikacja poprawności generowania URL z filtrami cenowymi i pokojami.
  - **Test 2 (`test_olx_payload_normalization`)**: Walidacja spłaszczania parametrów `params` do kluczy pierwszego poziomu ($O(1)$).
  - **Test 3 (`test_olx_price_and_rooms_filtering`)**: Weryfikacja odrzucania ofert spoza zakresu 1.0M - 1.05M PLN oraz mieszkań innych niż 3-pokojowe.
  - **Test 4 (`test_olx_ground_floor_and_elevator_filtering`)**: Weryfikacja wykluczenia parteru (`floor = 0`) oraz wymogu windy (`has_elevator = 1`).
  - **Test 5 (`test_olx_cross_portal_deduplication`)**: Sprawdzenie scalenia oferty występującej równolegle na Otodom, Adresowo i OLX do pojedynczego wiersza w `gold_listings` ze wskaźnikiem `portal_occurrences_count = 3`.
  - **Test 6 (`test_olx_completeness_audit`)**: Sprawdzenie poprawności zapisu metryk do tabeli `run_audit`.

- [ ] **3.2. Wykonanie całego zestawu testów**
  - Uruchomienie `python3 -m unittest discover tests` i potwierdzenie 100% zaliczonych testów bez regresji.

---

### Faza 4: Weryfikacja End-to-End i Dokumentacja

- [ ] **4.1. Uruchomienie pełnego przebiegu `main.py`**
  - Potwierdzenie zasilenia bazy danych SQLite, poprawnego działania audytu w konsoli i wygenerowania raportu w katalogu `historia/`.
- [ ] **4.2. Gotowość do archiwizacji zmiany (`/opsx-archive`)**
  - Przygotowanie podsumowania wdrożenia.
