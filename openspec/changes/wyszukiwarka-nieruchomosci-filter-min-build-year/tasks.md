# Plan Wdrożeniowy: Filtr Minimalnego Roku Budowy Budynku

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-filter-min-build-year`  
**Status**: Ukończony (Completed)  

---

## 📋 Lista Zadań (Tasks)

### Faza 1: Rozszerzenie Warstwy Danych i Bazy SQLite (`src/db.py`)
- [x] **Zadanie 1.1**: Dodanie ekstrakcji `build_year` w widoku `silver_listings` (`src/db.py`) z obsługą pól JSON-ów dla 6 serwisów.
- [x] **Zadanie 1.2**: Dodanie propagacji `MAX(build_year) AS build_year` w widoku `gold_listings` (`src/db.py`).

### Faza 2: Integracja z Deduplikatorem i Generatorem Raportu
- [x] **Zadanie 2.1**: Dodanie filtrowania `AND build_year >= ?` w metodzie `get_gold_listings()` w `src/deduplicator.py`.
- [x] **Zadanie 2.2**: Rozszerzenie tabeli ofert i sekcji Top 3 w `src/report_generator.py` o kolumnę / informację o roku budowy (`Rok`).

### Faza 3: Testy Jednostkowe i Weryfikacja Regresyjna
- [x] **Zadanie 3.1**: Utworzenie zestawu testów jednostkowych `tests/test_min_build_year_filter.py` weryfikujących:
  - Ekstrakcję `build_year` z bazy danych SQLite dla warstw Silver i Gold.
  - Parsowanie `CriteriaConfig` (`min_build_year` ze stringa liczbowego i `Dowolny`).
  - Filtrowanie w `Deduplicator.get_gold_listings()`.
  - Poprawność renderowania kolumny w raporcie Markdown.
- [x] **Zadanie 3.2**: Uruchomienie pełnego pakietu testów jednostkowych (`python3 -m unittest discover tests`) i weryfikacja braku regresji (46/46 testów OK).
