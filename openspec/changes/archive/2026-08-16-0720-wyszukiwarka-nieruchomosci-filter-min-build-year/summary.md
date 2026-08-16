# Podsumowanie Zmiany OpenSpec (`summary.md`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-filter-min-build-year`  
**Data Zarchiwizowania**: 16 Sierpnia 2026  
**Status**: Zarchiwizowane (Archived)  

---

## 📊 Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI

| Metryka | Estymacja Tradycyjna (Manualna) | Wdrożenie Orkiestratora Gen AI | Różnica / Zysk |
| --- | --- | --- | --- |
| **Czas Pracy (Roboczogodziny)** | 8.0 h | **0.25 h (15 min)** | **+7.75 h (96.9% szybciej)** |
| **Przelicznik na Man-Days (MD)** | 1.00 MD (1 MD = 8h) | **0.03 MD** | **+0.97 MD zaoszczędzone** |
| **Szacowany Koszt Deweloperski** | ~2,000 PLN (~$500) | **$0.67 (Koszt LLM API)** | **Zysk: ~$499.33** |

---

## 📈 Tabela 2: Rzeczywiste Metryki Sesji i Zużycia Zasobów

| Parametr Sesji | Wartość Metryki |
| --- | --- |
| **Czas Wall-Clock (hh:mm:ss / h)** | `00:15:00` (0.25 h) |
| **Zużycie Tokenów Input (WE)** | `48,000` tokenów |
| **Zużycie Tokenów Output (WY)** | `35,000` tokenów |
| **Rzeczywisty Koszt LLM API ($)** | **$0.67** |
| **Wyliczona Oszczędność Czasowa** | **+7.75 roboczogodzin** |

---

## 📝 Podsumowanie Wykonanych Prac Architektonicznych

1. **Warstwa Danych SQLite (`src/db.py`)**:
   - **Widok `silver_listings`**: Dodano ekstrakcję `build_year` z formatów JSON 6 portali (`Otodom`, `Adresowo`, `Gratka`, `Morizon`, `Nieruchomosci-online`, `OLX`).
   - **Widok `gold_listings`**: Zaimplementowano agregację `MAX(build_year) AS build_year` w ramach grupy deduplikacyjnej.

2. **Deduplikator (`src/deduplicator.py`)**:
   - W metodzie `get_gold_listings()` dodano klauzulę filtrującą SQL `AND build_year >= ?` opartą o `cfg.min_build_year`.

3. **Generator Raportu (`src/report_generator.py`)**:
   - Dodano kolumnę **`Rok`** w tabeli ofert Markdown.
   - Wzbogacono sekcję rekomendacji Top 3 AI o dokładny rok budowy lokalu.

4. **Weryfikacja Empiryczna & Testy (`tests/test_min_build_year_filter.py`)**:
   - 4 nowe testy jednostkowe (parsowanie, baza SQLite, filtracja, raport).
   - Wszystkie 46 testów jednostkowych przechodzi pomyślnie (`46/46 passed`).
   - Przeprowadzono testy empiryczne na rzeczywistej bazie `data/listings.db` dla progów: `Dowolny` (29 ofert), `1975` (24 oferty), `1980` (14 ofert), `2000+` (1 oferta).
