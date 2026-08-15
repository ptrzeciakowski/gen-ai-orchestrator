# Peer Review Architektoniczny: Integracja OLX.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-olx`  
**Recenzent**: Architekt Oprogramowania (Autor projektu `wyszukiwarka-nieruchomosci-morizon`)  
**Data Recenzji**: 15 Sierpnia 2026  
**Dokument Recenzowany**: [`design_initial.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-olx/design_initial.md)  
**Standard Oceny**: [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md) & Architektura ELT

---

## 🧐 Recenzja Architektoniczna: Architekt Morizon

### 1. Ogólna Ocena Jakości Projektu
Projekt techniczny integracji serwisu OLX.pl jest bardzo szczegółowy i doskonale diagnozuje specyfikę danych z OLX (szczególnie wysoki udział ofert bezpośrednich od osób prywatnych: `user.is_business == 0`). Wybór ekstrakcji ze stanu React SSR (`__PRERENDERED_STATE__`) pozwala na pobranie bogatego zestawu danych (w tym koordynatów GPS i parametrów technicznych) w pojedynczym zapytaniu HTTP, co jest wysoce efektywne.

W projekcie zidentyfikowano jednak jedno istotne **wąskie gardło wydajnościowe** w proponowanym schemacie widoku SQL `silver_listings`.

---

### 2. Szczegółowa Ocena w Wymiarach Architektonicznych

#### 2.1. Spójność z Architekturą ELT i Zagrożenie Wydajnościowe w `db.py`
* **Zidentyfikowany problem wydajnościowy w widoku `silver_listings`**:
  - W sekcji 4.2 zaproponowano użycie wielu skorelowanych podzapytań z funkcją `json_each()` dla każdego wiersza w widoku `silver_listings`:
    ```sql
    (SELECT json_extract(value, '$.value.value') FROM json_each(b.raw_payload, '$.params') WHERE json_extract(value, '$.key') = 'price' LIMIT 1)
    (SELECT json_extract(value, '$.value.value') FROM json_each(b.raw_payload, '$.params') WHERE json_extract(value, '$.key') = 'm' LIMIT 1)
    (SELECT ... FROM json_each(b.raw_payload, '$.params') WHERE json_extract(value, '$.key') = 'rooms' LIMIT 1)
    (SELECT ... FROM json_each(b.raw_payload, '$.params') WHERE json_extract(value, '$.key') IN ('floor_select', 'floor') LIMIT 1)
    (SELECT ... FROM json_each(b.raw_payload, '$.params') WHERE json_extract(value, '$.key') IN ('elevator', 'has_elevator') LIMIT 1)
    ```
  - *Analiza ryzyka*: Wykonanie 5 niezależnych podzapytań `json_each` per wiersz dla tabeli `bronze_listings` zawierającej tysiące rekordów z wielu uruchomień (`run_id`) drastycznie zwolni czas wykonywania zapytań przez `Deduplicator` i generator raportów!
  - *Rekomendacja inżynierska*:
    Podczas scrapingu w `OLXProvider`, tuż przed wywołaniem `insert_bronze_listing`, provider powinien **przepisać kluczowe parametry do znormalizowanych pól w korzeniu obiektu JSON** (np. `item['price_pln'] = ...`, `item['area_m2'] = ...`, `item['rooms'] = ...`, `item['floor'] = ...`, `item['has_elevator'] = ...`).  
    Dzięki temu `silver_listings` odczyta je przez szybki, bezpośredni `json_extract(b.raw_payload, '$.price_pln')`, a podzapytania `json_each` pozostaną jedynie jako opcjonalny mechanizm awaryjny (fallback).

#### 2.2. Poprawność Mapowania Kryteriów Biznesowych (`kryteria.md`)
* **Mocne strony**:
  - Precyzyjne mapowanie parametrów tablicowych `search[filter_float_price:from]`, `search[filter_float_price:to]` oraz `search[filter_enum_rooms]`.
  - Doskonała obsługa mapowania poziomów w OLX (`floor_0` -> 0, `floor_1` -> 1, ..., `floor_higher` -> 12).
  - Skuteczna klasyfikacja `seller_type` na bazie `user.is_business` (`0` -> "Bezpośrednio", `1` -> "Agencja").

#### 2.3. Odporność na Zmiany Szablonu OLX i Antybot
* **Mocne strony**:
  - Realistyczne nagłówki Chromium na macOS.
  - Zastosowanie Exponential Backoff w przypadku błędów HTTP 429 / 403.
  - Odrzucenie Playwright na rzecz lekkiego klienta HTTP z zachowaniem spójności całego ekosystemu projektu.
* **Uwaga do selektora stanu SSR**:
  - Struktura `__PRERENDERED_STATE__` bywa przez OLX modyfikowana (np. zmiana nazwy węzła z `adSearch` na `listing` lub minifikacja).
  - Rekomenduję rozszerzenie listy wzorców regex o wykrywanie obiektów JSON-LD (`<script type="application/ld+json">`), które OLX również generuje dla wyszukiwarek (Schema.org `Product` / `Offer`).

#### 2.4. Deduplikacja Międzyserwisowa (`gold_listings`)
* **Mocne strony**:
  - Obiekt stanu SSR OLX zawiera dokładne koordynaty GPS (`location.latitude`, `location.longitude`), co pozwala na natychmiastowe i precyzyjne łączenie ofert z OLX z ofertami z Otodom, Adresowo i Morizona.
  - Połączenie ogłoszeń prywatnych z OLX z ogłoszeniami agencji na Otodom/Morizonie pozwoli na wykrycie prowizji pośredników w kolumnach `min_price_pln` vs `max_price_pln`.

---

### 3. Rekomendacje Standaryzacyjne
1. **Pre-normalizacja payloadu w Pythonie**: Wzbogacenie surowego słownika JSON o ustandaryzowane klucze pierwszego poziomu przed zapisem do Bronze, aby odciążyć silnik SQLite z wielokrotnego `json_each`.
2. **Multi-pattern SSR Parser**: Przygotowanie łańcucha fallbacków dla różnych wersji szablonu SSR OLX (`__PRERENDERED_STATE__`, `window.__PRERENDERED_STATE__`, JSON-LD).
3. **Standaryzacja slugów dzielnic**: Walidacja, czy format `/warszawa/q-{district}/` poprawnie zawęża wyniki na OLX dla wszystkich dzielnic z `config.districts`.

---
*Status Recenzji: **Zatwierdzony z zaleceniem krytycznej optymalizacji wydajnościowej podzapytań w widoku Silver.***
