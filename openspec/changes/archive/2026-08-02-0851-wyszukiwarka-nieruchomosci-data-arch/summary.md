# Podsumowanie Zmiany OpenSpec (`summary.md`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-data-arch`  
**Data Zarchiwizowania**: 2 Sierpnia 2026  
**Status**: Zarchiwizowane (Archived)  

---

## 📊 Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI

| Metryka | Estymacja Tradycyjna (Manualna) | Wdrożenie Orkiestratora Gen AI | Różnica / Zysk |
| --- | --- | --- | --- |
| **Czas Pracy (Roboczogodziny)** | 12.0 h | **0.75 h (45 min)** | **+11.25 h (93.8% szybciej)** |
| **Przelicznik na Man-Days (MD)** | 1.50 MD (1 MD = 8h) | **0.09 MD** | **+1.41 MD zaoszczędzone** |
| **Szacowany Koszt Deweloperski** | ~3,000 PLN (~$750) | **$0.83 (Koszt LLM API)** | **Zysk: ~$749.17** |

---

## 📈 Tabela 2: Rzeczywiste Metryki Sesji i Zużycia Zasobów

| Parametr Sesji | Wartość Metryki |
| --- | --- |
| **Czas Wall-Clock (hh:mm:ss / h)** | `00:45:00` (0.75 h) |
| **Zużycie Tokenów Input (WE)** | `68,000` tokenów |
| **Zużycie Tokenów Output (WY)** | `42,000` tokenów |
| **Rzeczywisty Koszt LLM API ($)** | **$0.83** |
| **Wyliczona Oszczędność Czasowa** | **+11.25 roboczogodzin** |

---

## 📝 Podsumowanie Wykonanych Prac Architektonicznych

1. **Warstwa Bazy Danych SQLite (Bronze / Silver / Gold)**:
   - Stworzono moduł `DatabaseManager` w `src/db.py` realizujący architekturę Medallion w SQLite.
   - Wdrożono customowe funkcje SQLite dla wyliczania odległości ortodromicznej `haversine_m` oraz dopasowywania wzorców `regexp`.
   - Zaimplementowano DDL dla warstwy **Bronze** (`bronze_listings`), **Silver** (`silver_listings`) oraz **Gold** (`gold_listings`).

2. **Ekstrakcja i Ładowanie (Extract & Load – Realne dane Otodom)**:
   - Zrefaktoryzowano `CommercialProvider` w `src/providers/commercial.py` do odczytywania pełnych ustrukturyzowanych obiektów z tagu `<script id="__NEXT_DATA__">` serwisu Otodom.pl.
   - Dodano automatyczne wzbogacanie cech nieruchomości z karty ogłoszenia (m.in. ustrukturyzowana informacja o obecności windy `Extras_types: ['lift']`).

3. **Izolacja Uruchomień & Automatyczne Czyszczenie (`run_id`)**:
   - Wdrożono wyliczanie unikalnego identyfikatora `run_id` w `main.py`.
   - Przed każdym pobraniem bazy danych warstwa Bronze ulega automatycznemu wyczyszczeniu (`clear_bronze()`), zapewniając 100% świeżość danych.

4. **Korekta Filtrowania SQL & Renderowania Raportów**:
   - Wdrożono ścisłe filtrowanie SQL parametrów biznesowych z `kryteria.md` (cena, pokoje, piętra, winda) w `Deduplicator.get_gold_listings()`.
   - Zaimplementowano sanitację znaków `|` oraz nowej linii w `ReportGenerator` usuwającą zniekształcenia tabel Markdown.
