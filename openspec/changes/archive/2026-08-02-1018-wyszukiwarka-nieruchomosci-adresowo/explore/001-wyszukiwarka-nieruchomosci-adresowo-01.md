# Dokument Eksploracyjny OpenSpec: Integracja Serwisu Adresowo.pl oraz Retencja Danych Historycznych (ELT)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-adresowo`  
**Data**: 2 Sierpnia 2026  
**Wersja Dokumentu**: `001-wyszukiwarka-nieruchomosci-adresowo-01.md`  
**Status**: W Trakcie Eksploracji (In Exploration)  
**Dokumenty Referencyjne**:
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Cel Zmiany i Wymagania Biznesowe

Zmiana ma na celu rozszerzenie silnika wyszukiwarki nieruchomości o drugi kluczowy serwis ogłoszeniowy – **Adresowo.pl**, z zachowaniem pełnego rygoru architektury ELT oraz trwałej retencji historycznej.

### Główne Założenia:
1. **Integracja z Adresowo.pl**: Pobieranie surowych obiektów z serwisu Adresowo.pl do warstwy Bronze.
2. **Obsługa Wszystkich Kryteriów z `kryteria.md`**: Wyjaśnienie sposobu filtracji każdego parametru lub jawne wykazanie ograniczeń w przypadku braku wsparcia.
3. **Trwała Retencja Historyczna w Bronze**: Zaprzestanie automatycznego czyszczenia bazy (`clear_bronze()`) przy każdym uruchomieniu. Przechowywanie wszystkich historycznych zrzutów z unikalnym `run_id`.
4. **Deduplikacja Międzyserwisowa w Warstwie Gold**: Konsolidacja tych samych ofert występujących jednocześnie na Otodom i Adresowo.pl na podstawie unikalnego klucza geolokalizacyjno-metrażowego.
5. **Izolacja Raportu & Wykrywanie Nowości (Novelty Detection)**:
   - Raport generowany z uruchomienia prezentuje wyłącznie oferty z aktualnego `run_id`.
   - Dane historyczne z poprzednich uruchomień zostaną wykorzystane do oznaczania ofert jako **NOWA** (brak w poprzednich uruchomieniach) vs **ZNAJOMA/ZMIANA CENY**.
6. **Iteracyjny Plan Testów**: Udokumentowany zestaw testów jednostkowych i integracyjnych dla każdego kryterium z `kryteria.md`.

---

## 2. Analiza Serwisu Adresowo.pl i Mapowanie Kryteriów

Na podstawie wstępnej inspekcji struktury strony Adresowo.pl ustalono, że serwis udostępnia ustrukturyzowane znaczniki `JSON-LD` (`schema.org/Place`, `schema.org/Offer`) oraz dedykowane znaczniki HTML `<span class="...">` zawierające kluczowe metadane oferty.

### 📋 Szczegółowe Mapowanie Kryteriów z `kryteria.md`:

| Kryterium z `kryteria.md` | Obsługa w Adresowo.pl | Sposób Ekstrakcji / Filtracji | Status & Uwagi |
| --- | --- | --- | --- |
| **Miasto** (np. Warszawa) | ✅ Tak | Zapewnione w URL (`/mieszkania/warszawa/`) oraz w `JSON-LD` | **Obsługiwane** |
| **Dzielnice** (np. Ursynów) | ✅ Tak | Zapewnione w URL (`/mieszkania/warszawa/ursynow/`) oraz w `JSON-LD` | **Obsługiwane** |
| **Max odległość od metra (m)** | ⚠️ SQL / SQLite | Obliczanie dystansu `haversine_m` z koordynatów `geo.latitude` / `geo.longitude` dostępnych w `JSON-LD` | **Obsługiwane w SQL** |
| **Typ nieruchomości** (Mieszkanie) | ✅ Tak | W URL (`/mieszkania/`) | **Obsługiwane** |
| **Typ ogłoszeniodawcy** | ✅ Tak | Detekcja znacznika HTML `bez pośredników` -> `Bezpośrednio`, w przeciwnym razie `Agencja` | **Obsługiwane** |
| **Rynek** (Pierwotny / Wtórny) | ⚠️ Brak w URL | **[Hipoteza/Domysł]**: Brak bezpośredniego parametru rynku w URL Adresowo. Wykrywanie w SQL na podstawie roku budowy (`< 2025` -> Wtórny) lub analizy tekstu opisu. | **Wyjaśnione Explicite (Obsługa w SQL)** |
| **Cena minimalna (PLN)** | ✅ Tak | Zwracana w `JSON-LD` (`Offer.price`). Filtrowana w SQL. | **Obsługiwane w SQL** |
| **Cena maksymalna (PLN)** | ✅ Tak | Zwracana w `JSON-LD` (`Offer.price`). Filtrowana w SQL. | **Obsługiwane w SQL** |
| **Max cena za m²** | ✅ Tak | Wyliczana dynamicznie w widoku Silver (`price_pln / area_m2`). | **Obsługiwane w SQL** |
| **Powierzchnia min / max (m²)** | ✅ Tak | Parsowanie z tytułu/opisu `JSON-LD` oraz znaczników HTML (`42 m²`). | **Obsługiwane** |
| **Liczba pokoi min / max** | ✅ Tak | Parsowanie ze znaczników HTML (`1 pokój`, `3 pokoje`). | **Obsługiwane** |
| **Piętro min / max** | ✅ Tak | Parsowanie ze znaczników HTML (`2 piętro`). | **Obsługiwane** |
| **Wyklucz parter** | ✅ Tak | Reguła SQL `floor > 0`. | **Obsługiwane** |
| **Wyklucz ostatnie piętro** | ✅ Tak | Porównanie `floor = total_floors` z HTML (`2 piętro z 10`). | **Obsługiwane** |
| **Minimalny rok budowy** | ✅ Tak | Parsowanie ze znaczników HTML (`1988`, `rok budowy`). | **Obsługiwane** |
| **Winda** | ✅ Tak | Wykrywanie spójnika/znacznika `winda` w parametrach HTML lub opisie. | **Obsługiwane** |
| **Balkon / Taras / Ogródek** | ✅ Tak | Regex w znacznikach HTML i opisie (`balkon`, `taras`, `ogród`). | **Obsługiwane** |
| **Miejsce garażowe / parkingowe** | ✅ Tak | Regex w znacznikach HTML i opisie (`garaż`, `miejsce postojowe`). | **Obsługiwane** |
| **Stan wykończenia** | ⚠️ Analiza tekstu | **Brak dedykowanego filtra w wyszukiwarce Adresowo**. Wykrywanie po słowach kluczowych w opisie (`do remontu`, `do zamieszkania`). | **Wyjaśnione Explicite (Regex w Opisie)** |
| **Stan prawny** | ⚠️ Analiza tekstu | **Brak dedykowanego filtra w wyszukiwarce Adresowo**. Wykrywanie po słowach kluczowych w opisie (`pełna własność`, `księga wieczysta`). | **Wyjaśnione Explicite (Regex w Opisie)** |

---

## 3. Architektura Danych: Retencja Historyczna i Wykrywanie Nowości

Aby spełnić wymóg przechowywania wszystkich uruchomień i umożliwienia późniejszej analizy nowych ofert, rezygnujemy z usuwania danych przed nowym pobraniem.

### 🥉 Warstwa Bronze (`bronze_listings`):
- Tabela `bronze_listings` przechowuje **wszystkie historyczne rekordu** z unikalnym kluczem `UNIQUE(run_id, source_portal, external_id)`.
- Zdejmujemy wywołanie `clear_bronze()` w `main.py`.

### 🥈 Warstwa Silver (`silver_listings`):
- Widok `silver_listings` uwzględnia kolumnę `run_id` oraz `scraped_at`.
- Parsuje zarówno natywny format JSON Otodom, jak i format surowy wyciągnięty z Adresowo.pl (z parsowaniem `JSON-LD` i znaczników HTML).

### 🥇 Warstwa Gold (`gold_listings`) & Deduplikacja:
- Widok `gold_listings` dokonuje deduplikacji międzyserwisowej po kluczu `dedup_fingerprint`.
- Oferty z tej samej geolokalizacji, o tym samym metrażu i liczbie pokoi pojawiające się w Otodom i Adresowo.pl są łączone w jeden rekord w Gold (`source_portals_list = 'otodom:68259469, adresowo:r6l7m7'`).

### 🆕 Algorytm Wykrywania Nowości (Novelty Detection):
Dla dowolnego ogłoszenia w aktualnym uruchomieniu `run_id_current`:
```sql
SELECT 
    g.*,
    CASE 
        WHEN NOT EXISTS (
            SELECT 1 FROM bronze_listings b_prev 
            WHERE b_prev.external_id = g.external_id 
              AND b_prev.source_portal = g.source_portal 
              AND b_prev.run_id != g.run_id
        ) THEN 1 ELSE 0 
    END AS is_new_listing
FROM gold_listings g
WHERE g.run_id = :current_run_id;
```

---

## 4. Porównanie Opcji Architektonicznych (Trade-offs)

| Wariant | Zalety | Wady / Trade-offy | Rekomendacja |
| :--- | :--- | :--- | :--- |
| **Opcja A: Pobieranie Adresowo via HTML & JSON-LD** | Wysoka stabilność, dostępność pełnych metadanych (geolokalizacja, cena, rok budowy). | Wymaga parsu HTML przy braku wytypowanego API JSON. | **Rekomendowana** |
| **Opcja B: Scraping wyłącznie wyników listy** | Bardzo szybki scraping (1 zapytanie na stronę). | Brak pełnych informacji o roku budowy, wykończeniu i stanie prawnym. | Niepełna obsługa kryteriów. |

---

## 5. Nazywanie Niepewności i Ograniczeń (Brutally Honest Assessment)

1. **Limity Zapytań i Nagłówki HTTP Adresowo.pl**:
   - **Fakt**: Adresowo.pl wymaga standardowych nagłówków przeglądarkowych (`User-Agent`, `Accept`).
   - **Niepewność**: Wolumen zapytań przy sprawdzaniu kart szczegółowych dla wielu stron może natrafić na limity prędkości (rate-limiting).
   - **[Hipoteza/Domysł]**: Stosowanie małego opóźnienia (`time.sleep(0.5)`) oraz cachowanie surowych odpowiedzi w tabeli Bronze zminimalizuje ryzyko blokad IP.

2. **Grupowanie Rynku Pierwotnego / Wtórnego**:
   - **Ograniczenie**: Adresowo.pl nie udostępnia sztywnego filtra `market=pierwotny` w adresie URL.
   - **Rozwiązanie**: Klasyfikacja w SQL widoku Silver na podstawie roku budowy oraz treści opisu.

---

## 6. Następne Kroki w OpenSpec

- [x] Utworzenie dokumentu eksploracji `explore/001-wyszukiwarka-nieruchomosci-adresowo-01.md`.
- [ ] Przygotowanie propozycji zmian `proposal.md`.
- [ ] Opracowanie specyfikacji technicznej `design.md`.
- [ ] Stworzenie planu zadań `tasks.md` wraz z dedykowanym pakietem testów kryteriów.
