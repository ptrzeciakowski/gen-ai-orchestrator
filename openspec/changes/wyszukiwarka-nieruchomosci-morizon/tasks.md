# Plan Wdrożeniowy (Tasks): Integracja Serwisu Morizon.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-morizon`  
**Data Utworzenia**: 15 Sierpnia 2026  
**Status**: Plan Zaakceptowany do Implementacji (Ready for Implementation)  
**Dokumenty Powiązane**:
- Projekt Techniczny: [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-morizon/design.md)
- Propozycja Biznesowa: [`proposal.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-morizon/proposal.md)
- Kryteria Wyszukiwania: [`kryteria.md`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md)
- Peer Review: [`design-peer-review.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-morizon/design-peer-review.md)

---

## 📋 Lista Zadań Implementacyjnych

### Faza 1: Baza Danych i Kontrakt Danych (Database & Data Contracts)

- [ ] **1.1. Weryfikacja i Dostosowanie Widoku `silver_listings` w `src/db.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/db.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py)
  - **Opis**: Upewnić się, że widok `silver_listings` prawidłowo i wydajnie parsuje znormalizowane pola pierwszego poziomu z `raw_payload` (w tym `title`, `url`, `price_pln`, `area_m2`, `rooms`, `floor`, `total_floors`, `has_elevator`, `build_year`, `seller_type`, `location.coordinates`), a także fallbacki specyficzne dla JSON-LD Morizon.
  - **Kryteria Akceptacji**: Widok poprawnie wyciąga wszystkie atrybuty i wylicza `price_per_m2` oraz `is_last_floor`.
  - **Weryfikacja**: `python -m unittest tests/test_elt_pipeline.py`

---

### Faza 2: Implementacja Modułu `MorizonProvider`

- [ ] **2.1. Utworzenie Klasy i Generatora Adresów URL w `src/providers/morizon.py`**
  - **Plik**: `wyszukiwarka-nieruchomosci/src/providers/morizon.py`
  - **Opis**: Utworzenie szkieletu klasy `MorizonProvider(config, db_manager)` wraz z metodą pomocniczą `build_search_url(city_slug, district_slug, page=1)`. Zaimplementowanie normalizacji polskich znaków diakrytycznych w slugach dzielnic oraz mapowania parametrów `ps[price_from]`, `ps[price_to]`, `ps[number_of_rooms_from]`, `ps[number_of_rooms_to]`, `ps[living_area_from]`, `ps[living_area_to]`.
  - **Kryteria Akceptacji**: Poprawne formatowanie adresów URL dla zadanych dzielnic (np. `https://www.morizon.pl/mieszkania/sprzedaz/warszawa/ursynow/?ps[price_from]=1000000&ps[price_to]=1050000&ps[number_of_rooms_from]=3&ps[number_of_rooms_to]=3`).
  - **Weryfikacja**: Test jednostkowy generatora URL w `tests/test_morizon_criteria.py`.

- [ ] **2.2. Implementacja Dwufazowego Pobierania z Politeness Throttling i Nagłówkami HTTP**
  - **Plik**: `wyszukiwarka-nieruchomosci/src/providers/morizon.py`
  - **Opis**: Implementacja pętli paginacji (faza 1: pobranie listy linków) oraz pobierania podstron szczegółowych ofert (faza 2) z nagłówkami przeglądarkowymi Chromium oraz buforem `time.sleep(0.15 - 0.25s)`.
  - **Kryteria Akceptacji**: Pobieranie nie rzuca niespójnych wyjątków przy kodach błędów sieciowych (graceful degradation na błędy 403/429/timeout).
  - **Weryfikacja**: Uruchomienie próbnego pobrania pojedynczego chunka.

- [ ] **2.3. Implementacja Wielowarstwowego Parsera JSON-LD Schema.org i DOM Fallback**
  - **Plik**: `wyszukiwarka-nieruchomosci/src/providers/morizon.py`
  - **Opis**: Ekstrakcja danych ze znaczników `<script type="application/ld+json">` (`Apartment`, `SingleFamilyResidence`, `Place`, `Offer`) oraz wyrażeń regularnych dla cech technicznych (piętro, liczba pięter, winda, rok budowy, typ ogłoszeniodawcy). Zbudowanie znormalizowanego obiektu `raw_payload` i zapis do tabeli `bronze_listings`.
  - **Kryteria Akceptacji**: Każdy rekord w `bronze_listings` posiada kompletne metadane, współrzędne GPS oraz poprawny `source_portal = 'morizon'`.
  - **Weryfikacja**: Test parsowania syntetycznego HTML w `tests/test_morizon_criteria.py`.

- [ ] **2.4. Integracja Audytu Kompletności w `run_audit`**
  - **Plik**: `wyszukiwarka-nieruchomosci/src/providers/morizon.py`
  - **Opis**: Wyodrębnienie zadeklarowanej liczby ogłoszeń z nagłówka wyników (`expected_total`), oczyszczenie wartości liczbowej z separatorów i spacji oraz wywołanie `self.db_manager.save_run_audit(run_id, "morizon", expected_total, saved_count)`.
  - **Kryteria Akceptacji**: Wpis w tabeli `run_audit` zawiera poprawne wartości `expected_total`, `saved_bronze` oraz `completeness_pct`.
  - **Weryfikacja**: Weryfikacja zawartości tabeli `run_audit` po wykonaniu zrzutu.

---

### Faza 3: Integracja w Głównym Potoku ELT (`main.py`)

- [ ] **3.1. Podpięcie `MorizonProvider` w `main.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/main.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/main.py)
  - **Opis**: Zaimportowanie `MorizonProvider`, zainicjalizowanie i wywołanie metody `fetch_listings(run_id=run_id)` obok istniejących providerów `CommercialProvider` i `AdresowoProvider`. Wyświetlenie podsumowania audytu kompletności w konsoli.
  - **Kryteria Akceptacji**: Uruchomienie `python main.py` pobiera dane z serwisu Morizon, zapisuje do Bronze i uwzględnia w konsolidacji Gold oraz w raporcie końcowym.
  - **Weryfikacja**: `python main.py`

---

### Faza 4: Testy Jednostkowe i Weryfikacja Jakościowa

- [ ] **4.1. Utworzenie Dedykowanego Zestawu Testów `tests/test_morizon_criteria.py`**
  - **Plik**: `wyszukiwarka-nieruchomosci/tests/test_morizon_criteria.py`
  - **Opis**: Przygotowanie kompleksowych testów jednostkowych:
    1. Test generatora URL i mapowania parametrów `ps[...]`.
    2. Test parsowania surowego formatu JSON-LD do tabeli `bronze_listings`.
    3. Test filtracji kryteriów biznesowych w `gold_listings` (cena 1.0M - 1.05M PLN, 3 pokoje, piętra 1-8, winda, wykluczenie parteru).
    4. Test międzyserwisowej deduplikacji (scalanie rekordów Morizon + Otodom + Gratka po `dedup_fingerprint`).
    5. Test rejestracji audytu kompletności w `run_audit`.
  - **Kryteria Akceptacji**: Wszystkie testy jednostkowe kończą się wynikiem OK (100% pass rate).
  - **Weryfikacja**: `python -m unittest tests/test_morizon_criteria.py`

- [ ] **4.2. Wykonanie Pełnego Zestawu Testów Regresyjnych**
  - **Plik**: Cały katalog `wyszukiwarka-nieruchomosci/tests/`
  - **Opis**: Uruchomienie wszystkich istniejących testów systemu w celu potwierdzenia braku regresji dla providerów Otodom i Adresowo.
  - **Kryteria Akceptacji**: Wszystkie testy w projekcie przechodzą pomyślnie.
  - **Weryfikacja**: `python -m unittest discover -s tests`

---
*Plan dekompozycji wdrożeniowej przygotowany zgodnie z wytycznymi OpenSpec oraz regułami inżynierskimi.*
