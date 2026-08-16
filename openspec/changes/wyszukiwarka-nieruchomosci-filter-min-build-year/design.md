# OpenSpec Design: Filtr Minimalnego Roku Budowy Budynku (Min Build Year Filter)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-filter-min-build-year`  
**Data**: 16 Sierpnia 2026  
**Status**: Projekt Techniczny (Design)  
**Dokumenty Wejściowe**:
- [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-filter-min-build-year/proposal.md)
- [kryteria.md](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/kryteria.md)
- [db.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
- [deduplicator.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/deduplicator.py)
- [report_generator.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/report_generator.py)

---

## 1. Cel i Zakres Architektury (Context & Goals)

Celem zmiany jest dodanie i pełna integracja parametru **Minimalny rok budowy** (`min_build_year`) w całym potoku przetwarzania danych (ELT) Wyszukiwarki Nieruchomości: od parsowania konfiguracji w `kryteria.md`, przez ekstrakcję w warstwie **Silver**, agregację i filtrowanie SQL w warstwie **Gold**, aż po prezentację w generowanych raportach Markdown.

### Główne cele:
1. **Unifikacja ekstrakcji w warstwie Silver (`silver_listings`)**: Ekstrakcja pola `build_year` z JSON-ów wszystkich 6 portali (`Otodom`, `Adresowo`, `Gratka`, `Morizon`, `Nieruchomosci-online`, `OLX`).
2. **Propagacja do warstwy Gold (`gold_listings`)**: Uwzględnienie `MAX(build_year) AS build_year` podczas deduplikacji międzyserwisowej, co pozwala uzupełnić brakujący rok budowy w przypadku, gdy jeden z portali posiada tę informację.
3. **Precyzyjne filtrowanie w `Deduplicator`**: Aplikowanie warunku `build_year >= ?` w zapytaniu SQL warstwy Gold.
4. **Prezentacja w Raporcie Markdown**: Dodanie kolumny `Rok` w tabeli głównej oraz atrybutu roku budowy w kartach Top 3 rekomendacji AI.
5. **Kompleksowe testy regresyjne**: Zapewnienie pełnego zestawu testów jednostkowych dla parsowania, warstwy DB, deduplikatora i raportu.

---

## 2. Architektura i Przepływ Danych (System Architecture & Flow)

```
[kryteria.md: Minimalny rok budowy: 2000]
                   │
                   ▼
       [CriteriaConfig.load_from_file()] ──► self.min_build_year = 2000
                   │
                   ▼
┌─────────────────────────────────────────────────────────────┐
│ Warstwa Silver (silver_listings)                            │
│ COALESCE(                                                   │
│   raw_payload.build_year,                                   │
│   raw_payload.technical_details.build_year,                 │
│   raw_payload.target.Build_year,                            │
│   raw_payload.investmentEstimatedDelivery.year,             │
│   characteristics[key='build_year'].value                   │
│ ) AS build_year                                             │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Warstwa Gold (gold_listings)                                │
│ MAX(build_year) AS build_year GROUP BY dedup_fingerprint    │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ Deduplicator.get_gold_listings()                            │
│ WHERE ... AND (build_year >= :min_build_year)               │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ ReportGenerator.generate_report()                           │
│ Tabela Markdown: Kolumna 'Rok' | Top 3: Rok budowy          │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Kontrakty Schematów i Zapytań SQL

### 3.1. Widok `silver_listings`:
Dodanie kolumny `build_year` w CTE `extracted_data`:
```sql
CAST(COALESCE(
    json_extract(b.raw_payload, '$.build_year'),
    json_extract(b.raw_payload, '$.technical_details.build_year'),
    json_extract(b.raw_payload, '$.target.Build_year'),
    json_extract(b.raw_payload, '$.target.Construction_year'),
    json_extract(b.raw_payload, '$.investmentEstimatedDelivery.year'),
    (
        SELECT json_extract(value, '$.value')
        FROM json_each(b.raw_payload, '$.characteristics')
        WHERE json_extract(value, '$.key') = 'build_year'
        LIMIT 1
    )
) AS INTEGER) AS build_year
```

### 3.2. Widok `gold_listings`:
W sekcji CTE `deduplicated`:
```sql
MAX(build_year) AS build_year
```
Gwarantuje to zachowanie najwyższej (najbardziej precyzyjnej) wartości roku w przypadku zduplikowanych ofert z różnych serwisów.

### 3.3. Zapytanie `Deduplicator.get_gold_listings()`:
```python
if cfg.min_build_year is not None:
    query += " AND build_year >= ?"
    params.append(cfg.min_build_year)
```

---

## 4. Wybory Architektoniczne i Trade-offy (Architectural Trade-offs)

1. **Obsługa ofert z nieznanym rokiem budowy (`build_year IS NULL`)**:
   - *Opcja A (Łagodna)*: `AND (build_year >= ? OR build_year IS NULL)` - przepuszcza oferty bez podanego roku, co zapobiega fałszywym odrzuceniom (False Negatives), ale może przepuścić wielką płytę bez uzupełnionego formularza.
   - *Opcja B (Ścisła - Wybrana)*: `AND build_year >= ?` - gdy użytkownik wprost definiuje minimalny rok (np. 2000), oczekuje wyłącznie budynków o potwierdzonym roku budowy.
   - *Wybór*: **Opcja B (Ścisła)** dla zapytania filtrującego.

2. **Deduplikacja roku budowy (`MAX(build_year)`)**:
   - Użycie agregacji `MAX(build_year)` w widoku `gold_listings` rozwiązuje problem asymetrii danych między portalami (np. Morizon ma rok 2005, a OLX ma `NULL` dla tego samego mieszkania).

---

## 5. Obsługa Sytuacji Awaryjnych i Krawędziowych (Edge Cases)

1. **Brak parametru w `kryteria.md` lub wartość `Dowolny`**:
   - `min_build_year` przyjmuje wartość `None` – warunek SQL nie jest dodawany, zwracane są wszystkie oferty.
2. **Nietypowe formaty roku w payloadach**:
   - Wartości tekstowe konwertowane przez `CAST(... AS INTEGER)`, co bezpiecznie zamienia stringi na inty lub `NULL`.
3. **Oferty z rynku pierwotnego (inwestycje w trakcie budowy)**:
   - Rok oddania do użytkowania pobierany m.in. z `investmentEstimatedDelivery.year` (np. 2026/2027).
