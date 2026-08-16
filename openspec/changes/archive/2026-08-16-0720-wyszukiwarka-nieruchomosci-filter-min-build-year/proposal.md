# OpenSpec Proposal: Filtr Minimalnego Roku Budowy Budynku (Min Build Year Filter)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-filter-min-build-year`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/config.py`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/deduplicator.py`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

W pliku `kryteria.md` zdefiniowane jest pole konfiguracyjne:
`- **Minimalny rok budowy**: Dowolny` (lub konkretna wartość liczbowa, np. `1990`, `2005`, `2015`).

Dla kupujących nieruchomości wiek budynku i technologia budowy (wielka płyta z lat 70/80 vs nowe budownictwo po 2000 r.) jest jednym z kluczowych kryteriów decyzyjnych.
Chociaż warstwa **Silver** w `silver_listings` ekstrahuje już pole `build_year` z surowych danych wszystkich 6 serwisów (`Otodom`, `Adresowo`, `Gratka`, `Morizon`, `Nieruchomosci-online`, `OLX`), moduł `Deduplicator` (`src/deduplicator.py`) oraz konfigurator `CriteriaConfig` (`src/config.py`) wymagają formalnej integracji tego filtra w warstwie **Gold**.

---

## 2. Architektura i Przepływ Filtrowania (Target Architecture)

```
[kryteria.md: min_build_year=2000]
           │
           ▼
[CriteriaConfig: self.min_build_year = 2000]
           │
           ▼
[Deduplicator / SQL Gold Layer] ──► WHERE build_year >= 2000 (lub obsługa ofert bez podanego roku)
           │
           ▼
[ReportGenerator] ──► Prezentacja roku budowy w tabeli i sekcji analizy
```

### 🧭 Założenia Biznesowe i Techniczne:
1. **Parsowanie w `CriteriaConfig` (`src/config.py`)**:
   - Odczyt linii `- **Minimalny rok budowy**: <wartość>`:
     - Wartość `Dowolny` / brak -> `min_build_year = None` (brak ograniczenia).
     - Wartość liczbowa (np. `1990`) -> `min_build_year = 1990`.
2. **Egzekwowanie w SQL w warstwie Gold (`src/deduplicator.py`)**:
   - Gdy `config.min_build_year` jest ustawiony:
     - Klauzula filtrująca: `AND (build_year >= ? OR build_year IS NULL)` (z opcją ścisłą lub oznaczaniem braku roku w opisie).
     - Domyślnie: ścisłe odrzucanie budynków starszych niż zadany rok (`build_year >= config.min_build_year`).
3. **Ekstrakcja w warstwie Silver (`src/db.py`)**:
   - Upewnienie się, że `silver_listings` wyciąga `build_year` z ujednoliconych kluczy `raw_payload.build_year` ze wszystkich 6 providerów.
4. **Prezentacja w Raporcie (`src/report_generator.py`)**:
   - Dodanie kolumny **Rok budowy** w tabeli głównej raportu Markdown.
   - Wskazywanie wieku budynku w kartach rekomendacji AI.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Rozszerzenie `CriteriaConfig` (`src/config.py`)**: Parsowanie i walidacja parametru `min_build_year` z `kryteria.md`.
- [ ] **Filtracja SQL w `Deduplicator` (`src/deduplicator.py`)**: Aplikowanie warunku `build_year >= min_build_year` w zapytaniu do widoku `gold_listings`.
- [ ] **Aktualizacja `ReportGenerator` (`src/report_generator.py`)**: Wyświetlanie roku budowy w tabelach ofert.
- [ ] **Testy Jednostkowe (`tests/test_min_build_year_filter.py`)**:
  - Test parsowania roku z `kryteria.md` (zarówno `Dowolny` jak i `1995`).
  - Test odrzucania ofert ze starych budynków (np. 1978 przy progu 1990).
  - Test przepuszczania ofert z budynków spełniających próg (np. 2011).
  - Test obsługi przypadków brzegowych (brak zadeklarowanego roku).

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🎯 **Precyzja selekcji**: Możliwość automatycznego odcięcia bloków z wielkiej płyty lub kamienic przedwojennych na życzenie użytkownika.
* ⚡ **Zero dodatkowego scrapowania**: Filtr działa w 100% na warstwie Gold w pamięci lokalnej SQLite w ułamku sekundy.
