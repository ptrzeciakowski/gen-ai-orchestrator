# Central Archive Changes Summary

Plik zawiera zbiorczy rejestr wszystkich zarchiwizowanych zmian w standardzie OpenSpec dla repozytorium `gen-ai-orchestrator`. Każda zmiana nosi unikalny znacznik daty i godziny archiwizacji w formacie `YYYY-MM-DD-HHMM-<change-name>`.

> **Założenia kalkulacji metryk**:
> - **Stawki tokenowe LLM**: Input $3.00 / 1M tokenów ($0.000003/token), Output $15.00 / 1M tokenów ($0.000015/token).
> - **Oszczędność Czasowa (h)** = `Estymowany Czas Pracy (h) - Czas Trwania Wall-clock (h)`. Pozwala zmierzyć rzeczywisty zysk czasowy osiągnięty dzięki orkiestracji AI w porównaniu do tradycyjnego wytwarzania oprogramowania.

---

## 📈 Zbiorcze Zestawienie Zarchiwizowanych Zmian

| Nazwa Zmiany (`change-name`) | Krótki Opis Zmiany | Tokeny WE (Input) | Tokeny WY (Output) | Estymowany Koszt LLM ($) | Czas Trwania (Wall-clock) | Estymowany Czas (h) | Estymowane Man-Days (MD) | Oszczędność Czasowa (h) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **`2026-07-26-1914-orchestrator-initial-setup`** | Inicjalizacja struktury repozytorium orkiestratora Gen AI (`.ai/`, `.agents/`, OpenSpec `specs/` i `changes/`) oraz wytycznych uprawnień w `README.md`. | 118,845 | 77,500 | $1.52 | 01:43:25 (1.72h) | 20.5 h | 2.56 MD | **+18.78 h** |
| **`2026-07-26-2012-orchestrator-setup-repos`** | Integracja struktury `.repositories/`, stworzenie `git-agent` z wymuszeniem polityki Feature Branch oraz skryptów walidacyjnych z automatyzacją PR. | 39,597 | 46,000 | $0.81 | 00:20:47 (0.35h) | 6.0 h | 0.75 MD | **+5.65 h** |
| **`2026-07-26-2052-orchestrator-constructive-criticizm`** | Wdrożenie 12 Zasad Brutalnej Szczerości, opis struktury w `README.md`, dwutabelowy szablon `summary.md` oraz zbiorczy rejestr `changes-summary.md`. | 51,746 | 46,000 | $0.85 | 00:30:11 (0.50h) | 10.0 h | 1.25 MD | **+9.50 h** |
| **`2026-07-26-2300-wyszukiwarka-nieruchomosci`** | Etap 1 Wyszukiwarki Nieruchomości: Skupienie na Otodom.pl, bezwzględna walidacja cen max, brak wynajmu, brak linków kategorialnych, integracja RCN z 7 kwantylami ($P10\text{--}P99$) i próbką aktów notarialnych. | 65,400 | 52,100 | $0.80 | 00:42:00 (0.70h) | 10.5 h | 1.31 MD | **+9.80 h** |
| **`2026-07-27-2116-orchestrator-skill-single-source-of-true`** | Ustanowienie `SKILL.md` jako Single Source of Truth dla skilli OpenSpec (`opsx-explore`, `opsx-design`, `opsx-tasks`, `opsx-implement`, `opsx-archive`), konwencja `explore/NNN-nazwa-zmiany-MM.<ext>`, refaktoryzacja `openspec-agy-init.sh`. | 45,000 | 38,000 | $0.71 | 00:15:00 (0.25h) | 8.0 h | 1.00 MD | **+7.75 h** |
| **`2026-08-02-0851-wyszukiwarka-nieruchomosci-data-arch`** | Architektura ELT Bronze/Silver/Gold w SQLite dla Wyszukiwarki Nieruchomości: pobieranie z `__NEXT_DATA__` Otodom, wyliczanie metryk RCN, automatyczne czyszczenie bazy i `run_id`, ścisłe filtrowanie SQL w deduplikatorze oraz bezbłędne renderowanie tabel. | 68,000 | 42,000 | $0.83 | 00:45:00 (0.75h) | 12.0 h | 1.50 MD | **+11.25 h** |
| **`2026-08-02-1018-wyszukiwarka-nieruchomosci-adresowo`** | Integracja serwisu Adresowo.pl z klasą `AdresowoProvider`, obsługa dedykowanych adresów URL (`-Q/`, `_l2`), trwała retencja historyczna w `bronze_listings`, deduplikacja międzyserwisowa oraz wdrożenie flagi nowości (`is_new_listing`). | 75,000 | 48,000 | $0.95 | 00:50:00 (0.83h) | 14.0 h | 1.75 MD | **+13.17 h** |
| **`2026-08-15-1711-wyszukiwarka-nieruchomosci-brozne-completeness`** | Weryfikacja kompletności pobierania w warstwie Bronze: dynamiczna paginacja na bazie `totalCount` (Otodom) i liczby deklarowanych ofert (Adresowo), audyt w tabeli `run_audit`, raportowanie wskaźnika w CLI i nagłówkach Markdown. | 62,000 | 39,000 | $0.77 | 00:35:00 (0.58h) | 10.0 h | 1.25 MD | **+9.42 h** |
| **`2026-08-15-2158-wyszukiwarka-nieruchomosci-gratka`** | Integracja serwisu Gratka.pl: 2-fazowy scraper (lista + detal), ekstrakcja JSON-LD i tabeli cech, politeness delay, audyt kompletności oraz 8 testów jednostkowych zgodności z `kryteria.md`. | 65,000 | 42,000 | $0.82 | 00:35:00 (0.58h) | 12.0 h | 1.50 MD | **+11.42 h** |
| **`2026-08-15-2158-wyszukiwarka-nieruchomosci-morizon`** | Integracja serwisu Morizon.pl: 2-fazowy scraper, obsługa Schema.org `Apartment`/`Place`, wyznaczanie współrzędnych i pięter, audyt kompletności oraz 8 testów jednostkowych. | 68,000 | 44,000 | $0.86 | 00:35:00 (0.58h) | 12.0 h | 1.50 MD | **+11.42 h** |
| **`2026-08-15-2158-wyszukiwarka-nieruchomosci-nieruchomosci-online`** | Integracja serwisu Nieruchomosci-online.pl: obsługa sub-domen miejskich, parsowanie JSON-LD i parametrów technicznych, bezpieczna obsługa formatów tablicowych ofert oraz 9 testów jednostkowych. | 72,000 | 48,000 | $0.94 | 00:40:00 (0.67h) | 14.0 h | 1.75 MD | **+13.33 h** |
| **`2026-08-15-2158-wyszukiwarka-nieruchomosci-olx`** | Integracja serwisu OLX.pl: 1-fazowy parser stanu SSR `__PRERENDERED_STATE__`, pre-normalizacja O(1) do korzenia `raw_payload`, detekcja ofert prywatnych oraz 7 testów jednostkowych. | 64,000 | 40,000 | $0.79 | 00:30:00 (0.50h) | 12.0 h | 1.50 MD | **+11.50 h** |
| **`2026-08-16-0715-wyszukiwarka-nieruchomosci-standalone-repo`** | Wydzielenie silnika wyszukiwarki nieruchomości do dedykowanego repozytorium Git (`ptrzeciakowski/wyszukiwarka-nieruchomosci`), podpięcie przez symlinki `.repositories/`, publikacja na GitHubie oraz walidacja bezpieczeństwa. | 45,000 | 32,000 | $0.62 | 00:20:00 (0.33h) | 6.0 h | 0.75 MD | **+5.67 h** |
| **`2026-08-16-0720-wyszukiwarka-nieruchomosci-filter-min-build-year`** | Wdrożenie filtra minimalnego roku budowy (`min_build_year`): ekstrakcja w `silver_listings`, propagacja `MAX(build_year)` w `gold_listings`, filtracja SQL w `Deduplicator`, rozszerzenie tabeli w `ReportGenerator` oraz 4 testy jednostkowe. | 48,000 | 35,000 | $0.67 | 00:15:00 (0.25h) | 8.0 h | 1.00 MD | **+7.75 h** |
| **`2026-08-16-0730-wyszukiwarka-nieruchomosci-enhanced-deduplication`** | Wdrożenie 3-poziomowej kaskadowej deduplikacji (Ulica -> GPS -> Dzielnica), walidacja bounding box GPS Polski, normalizacja `street_slug` w SQLite, konsolidacja cech w Gold (`MAX(floor)`, `MAX(build_year)`) i 4 testy jednostkowe. | 52,000 | 38,000 | $0.73 | 00:20:00 (0.33h) | 12.0 h | 1.50 MD | **+11.67 h** |
| **`2026-08-16-0750-wyszukiwarka-nieruchomosci-react-ui`** | Nowoczesny interfejs webowy React 19 + Vite z wielowątkowym backendem REST API (Python), dynamiczną filtracją SQL, badżami opłacalności RCN, telemetrią warstw Bronze/Silver/Gold, odświeżaniem bazy w tle i 6 testami API. | 78,000 | 54,000 | $1.04 | 00:25:00 (0.42h) | 24.0 h | 3.00 MD | **+23.58 h** |
| **SUMA / RAZEM** | **Wszystkie zarchiwizowane zmiany (16 zmian)** | **1,017,588** | **721,600** | **$13.71** | **09:21:23 (9.34h)** | **191.0 h** | **23.88 MD** | **+181.66 h** |

---

## 📊 Podsumowanie Agregacji Projektu

- **Łączne Zużycie Tokenów**: 1,017,588 WE / 721,600 WY
- **Łączny Szacowany Koszt API LLM**: **$13.71**
- **Łączny Czas Trwania Sesji AI (Wall-clock)**: **09:21:23** (9.34 h)
- **Łączny Estymowany Czas Pracy Deweloperskiej**: **191.0 roboczogodzin (23.88 MD)**
- **Zysk / Oszczędność Czasu Deweloperskiego**: **+181.66 roboczogodzin (~22.71 MD zaoszczędzone)**
