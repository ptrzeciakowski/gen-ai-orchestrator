# Plan Implementacji i Lista Zadań (Tasks): Integracja Serwisu Gratka.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-gratka`  
**Data**: 15 Sierpnia 2026  
**Status**: Gotowy do Realizacji (Ready for Implementation)  
**Dokumenty Referencyjne**:
- [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-gratka/design.md)
- [`proposal.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-gratka/proposal.md)
- [`kryteria.md`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md)

---

## 📋 Lista Zadań Implementacyjnych

### Faza 1: Przygotowanie Warstwy Danych i Bazy SQLite (`src/db.py`)

- [ ] **Zadanie 1.1: Aktualizacja i Standaryzacja Widoku `silver_listings` w `src/db.py`**
  - **Plik do modyfikacji**: [`src/db.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py)
  - **Opis**: Upewnienie się, że widok `silver_listings` wspiera odczyt znormalizowanych kluczy pierwszego poziomu (`price_pln`, `area_m2`, `rooms`, `floor`, `total_floors`, `has_elevator`, `location.coordinates`) z zachowaniem ścieżek fallbackowych dla Gratki (`features.winda`, `offer_ld.price`).
  - **Kryteria Akceptacji**:
    - Widok `silver_listings` poprawnie parsuje rekordy z `source_portal = 'gratka'`.
    - Istniejące testy bazy danych (`tests/test_elt_pipeline.py`) przechodzą bez błędów.
  - **Weryfikacja**: `python3 -m unittest tests/test_elt_pipeline.py`

---

### Faza 2: Implementacja Modułu `GratkaProvider` (`src/providers/gratka.py`)

- [ ] **Zadanie 2.1: Utworzenie Klasy `GratkaProvider` i Generatora URL**
  - **Plik do utworzenia**: [`src/providers/gratka.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/gratka.py)
  - **Opis**: Implementacja metody `build_search_url(city_slug, district_slug, page)` z obsługą parametrów dwukropkowych Gratki (`cena-calkowita:min/max`, `liczba-pokoi:min/max`, `powierzchnia-w-m2:min/max`, `page=N`).
  - **Kryteria Akceptacji**:
    - Generator poprawnie składa parametry zapytania GET zgodnie ze specyfikacją.
    - Prawidłowa normalizacja znaków diakrytycznych w nazwach dzielnic.

- [ ] **Zadanie 2.2: Implementacja Dwufazowego Pobierania (List + Detail Scraping)**
  - **Plik do modyfikacji**: [`src/providers/gratka.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/gratka.py)
  - **Opis**: Implementacja pętli paginacji listy ofert oraz pobierania podstron szczegółowych każdego ogłoszenia z buforem czasowym 150-250ms i pełnym zestawem nagłówków Chromium macOS.
  - **Kryteria Akceptacji**:
    - Ekstrakcja ustrukturyzowanych obiektów JSON-LD oraz tabeli cech (winda, piętro, rok budowy).
    - Pre-normalizacja kluczy do korzenia `raw_payload` i zapis do tabeli `bronze_listings`.

- [ ] **Zadanie 2.3: Implementacja Ekstrakcji Metryk Audytu (`run_audit`)**
  - **Plik do modyfikacji**: [`src/providers/gratka.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/providers/gratka.py)
  - **Opis**: Pobranie zadeklarowanej liczby ofert z nagłówka strony listingu Gratki (`expected_total_gratka`) i rejestracja w bazie przez `db_manager.save_run_audit(run_id, "gratka", ...)`.
  - **Kryteria Akceptacji**:
    - Prawidłowe zliczenie i zapis metryk kompletności do tabeli `run_audit`.

---

### Faza 3: Integracja w Głównym Pipeline (`main.py`)

- [ ] **Zadanie 3.1: Rejestracja `GratkaProvider` w `main.py`**
  - **Plik do modyfikacji**: [`main.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/main.py)
  - **Opis**: Zaimportowanie `GratkaProvider`, wywołanie pobierania w sekcji Bronze oraz wyświetlenie podsumowania audytu kompletności Gratki w konsoli.
  - **Kryteria Akceptacji**:
    - `GratkaProvider` uruchamia się w potoku obok `CommercialProvider`, `DirectProvider` i `AdresowoProvider`.
    - Błędy sieciowe Gratki są izolowane i nie blokują generowania raportu końcowego.

---

### Faza 4: Zestaw Testów Jednostkowych i Zgodności Kryteriów (`tests/test_gratka_criteria.py`)

- [ ] **Zadanie 4.1: Utworzenie Dedykowanego Pakietu Testów Kryteriów**
  - **Plik do utworzenia**: [`tests/test_gratka_criteria.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/tests/test_gratka_criteria.py)
  - **Opis**: Zaimplementowanie testów jednostkowych weryfikujących zachowanie warstwy ELT dla ofert z Gratki:
    1. `test_gratka_price_filtering` (zakres 1,000,000 - 1,050,000 PLN).
    2. `test_gratka_rooms_and_elevator` (wymóg 3 pokoi i obecność windy).
    3. `test_gratka_ground_floor_exclusion` (wykluczenie parteru: `floor > 0`).
    4. `test_gratka_cross_portal_deduplication` (fuzja ofert Gratka + Otodom w `gold_listings`).
    5. `test_gratka_completeness_audit` (zapis i odczyt metryk z `run_audit`).
  - **Kryteria Akceptacji**:
    - 100% testów przechodzi pomyślnie (`OK`).
  - **Weryfikacja**: `python3 -m unittest tests/test_gratka_criteria.py`

---

### Faza 5: Weryfikacja Całościowa (End-to-End Validation)

- [ ] **Zadanie 5.1: Uruchomienie Pełnego Zestawu Testów Projektu**
  - **Opis**: Uruchomienie wszystkich testów jednostkowych w repozytorium:
    - `python3 -m unittest discover tests/`
  - **Kryteria Akceptacji**: Wszystkie testy (w tym testy istniejących modułów Adresowo i ELT) przechodzą bez błędów.

---
*Plan dekompozycji wdrożeniowej przygotowany zgodnie ze standardem OpenSpec /opsx-tasks.*
