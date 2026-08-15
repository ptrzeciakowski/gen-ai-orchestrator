# Projekt Techniczny: Integracja Serwisu OLX.pl (Warstwa ELT)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-olx`  
**Status**: Projekt Zaakceptowany (Final Architecture & Peer Review Consensus)  
**Autor**: Software Architect (Architekt OLX Provider)  
**Data**: 15 Sierpnia 2026  
**Dokumenty Źródłowe i Wytyczne**:
- [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-olx/proposal.md)
- [design_initial.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-olx/design_initial.md)
- [design-peer-review.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-olx/design-peer-review.md)
- [kryteria.md](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md)
- [brutally-honest-rules.md](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)
- [db.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py) | [deduplicator.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/deduplicator.py) | [config.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/config.py) | [main.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/main.py)

---

## 1. Cel i Zakres Architektury (Context & Goals)

### 1.1. Kontekst Biznesowy i Architektoniczny
Głównym celem zmiany jest włączenie portalu **OLX.pl** jako kluczowego źródła danych w systemie `wyszukiwarka-nieruchomosci` (obok portali Otodom i Adresowo). OLX gromadzi największy wolumen bezpośrednich ogłoszeń właścicieli mieszkań ("bez pośredników") oraz ofert mniejszych, lokalnych biur nieruchomości, co stwarza największy potencjał identyfikacji okazji cenowych poniżej benchmarku rynkowego RCN (Rejestr Cen Nieruchomości m.st. Warszawy).

Projekt jest realizowany zgodnie ze standardem **ELT (Extract-Load-Transform)**:
1. **Extract & Load (Warstwa Bronze)**: Pobranie surowego, szerokiego strumienia ogłoszeń z OLX bez stratnej filtracji i zapisanie do tabeli `bronze_listings` (w formacie JSON).
2. **Transform (Warstwa Silver)**: Zunifikowanie atrybutów nieruchomości (cena, metraż, pokoje, piętro, winda, geolokalizacja) w widoku SQL `silver_listings` za pomocą wbudowanych funkcji SQLite JSON1 (`json_extract`).
3. **Filter & Deduplicate (Warstwa Gold)**: Wyliczenie unikalnego odcisku palca oferty (`dedup_fingerprint`), eliminacja duplikatów międzyserwisowych, wykrycie nowości (`is_new_listing`) oraz nałożenie reguł biznesowych z `kryteria.md`.
4. **Enrich & Report**: Zestawienie z danymi transakcyjnymi RCN i wygenerowanie raportu markdown w katalogu `historia/`.

### 1.2. Szczera Ocena Możliwości i Ograniczeń (Brutally Honest Scope Analysis)
*Na podstawie analizy mechanizmów filtrowania OLX.pl oraz dotychczasowej architektury systemu:*

| Parametr z `kryteria.md` | Poziom Filtrowania | Uzasadnienie Techniczne i Granice Pewności |
| :--- | :---: | :--- |
| **Miasto & Dzielnica** | 🟢 **Natywne URL Query** | OLX natywnie obsługuje strukturę ścieżki i parametr dzielnicy (`/warszawa/q-{district}/` lub `search[filter_enum_district]`). |
| **Cena min / max** | 🟢 **Natywne URL Query** | Obsługiwane przez parametry zapytania GET: `search[filter_float_price:from]` oraz `search[filter_float_price:to]`. |
| **Liczba pokoi** | 🟢 **Natywne URL Query** | Obsługiwane przez tablicowy parametr `search[filter_enum_rooms][0]=three` (lub odpowiednik numeryczny). |
| **Powierzchnia min / max** | 🟡 **Query + Warstwa Gold** | OLX wspiera `search[filter_float_m:from]`, jednak w ogłoszeniach prywatnych metraż bywa mylony z powierzchnią działki/użytkowej. Wymagana re-walidacja w warstwie Gold. |
| **Rynek (Pierwotny / Wtórny)** | 🟡 **Warstwa Gold** | Parametr rynku w OLX bywa niekompletny lub ignorowany przez użytkowników prywatnych dodających ogłoszenia w uproszczonym formularzu. |
| **Piętro / Wyklucz parter** | 🔴 **Wyłącznie Warstwa Gold** | OLX nie udostępnia w URL niezawodnego filtra wykluczającego wyłącznie parter bez jednoczesnego obcięcia ofert z brakującym atrybutem. Filtrowanie następuje w SQL. |
| **Winda** | 🔴 **Wyłącznie Warstwa Gold** | Brak bezpośredniego selektora w formularzu wyszukiwania URL. Wymaga ekstrakcji cech z payloadu oraz analizy regex w tekście opisu (`winda`, `windą`). |
| **Odległość od metra** | 🔴 **Poza zakresem providera** | Obliczane ortodromicznie (`haversine_m`) w module bazy danych i deduplikatora na podstawie współrzędnych geograficznych. |

---

## 2. Architektura Systemu i Przepływ Danych (System Architecture & Flow)

Poniższy diagram ilustruje przepływ danych i powiązania komponentów po wdrożeniu modułu `OLXProvider`:

```mermaid
flowchart TD
    subgraph InputConfig ["Konfiguracja Wejściowa"]
        CRIT["kryteria.md"] --> CFG["CriteriaConfig (src/config.py)"]
    end

    subgraph ExtractionLayer ["Warstwa Ekstrakcji (Extract & Bronze Load)"]
        CFG --> COMM["CommercialProvider (Otodom)"]
        CFG --> ADR["AdresowoProvider (Adresowo.pl)"]
        CFG --> OLX["OLXProvider (src/providers/olx.py)"]
        
        OLX -->|HTTP GET z nagłówkami Browser| OLX_NET["OLX.pl Serwery"]
        OLX_NET -->|HTML + window.__PRERENDERED_STATE__| OLX
        
        COMM -->|insert_bronze_listing| BRONZE[("bronze_listings (SQLite Table)")]
        ADR -->|insert_bronze_listing| BRONZE
        OLX -->|insert_bronze_listing (zoptymalizowany O(1))| BRONZE
        
        COMM -.->|save_run_audit| AUDIT[("run_audit (SQLite Table)")]
        ADR -.->|save_run_audit| AUDIT
        OLX -.->|save_run_audit| AUDIT
    end

    subgraph TransformationLayer ["Warstwa Transformacji i Deduplikacji"]
        BRONZE -->|Szybki json_extract O(1)| SILVER["silver_listings (SQLite View)"]
        SILVER -->|dedup_fingerprint & is_new_listing| GOLD["gold_listings (SQLite View)"]
        GOLD --> DEDUP["Deduplicator (src/deduplicator.py)"]
        CFG -.->|Filtry biznesowe SQL| DEDUP
    end

    subgraph OutputLayer ["Warstwa Raportowania i Wzbogacania"]
        DEDUP --> RPT["ReportGenerator (src/report_generator.py)"]
        RCN["RCNClient (src/rcn_client.py)"] --> RPT
        RPT --> MD_OUT["historia/raport_YYYY-MM-DD_HH-MM-SS.md"]
    end
```

---

## 3. Architektura Modułu `OLXProvider` (`src/providers/olx.py`)

### 3.1. Konstrukcja Zapytań URL i Mapowanie Parametrów
OLX.pl stosuje hierarchiczną strukturę ścieżek URL dla kategorii oraz parametry tablicowe w query string:
* **Format Bazowy URL**: `https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/{city_slug}/`
* **Slug Miasta**: `warszawa`
* **Slug Dzielnicy**: Obsługiwany poprzez podścieżkę `/warszawa/q-{district_slug}/` lub filtr dzielnicy.
* **Filtry Cenowe**:
  - `search[filter_float_price:from]={int(min_price)}`
  - `search[filter_float_price:to]={int(max_price)}`
* **Liczba Pokoi**:
  - `search[filter_enum_rooms][0]=three` (lub odpowiednik dla wskazanej liczby pokoi).
* **Paginacja**:
  - `page={page_number}` (gdzie pierwsza strona to brak parametru lub `page=1`).

### 3.2. Ekstrakcja Danych ze Stanu SSR i Łańcuch Parserów (Multi-pattern Parser)
W celu zagwarantowania odporności na modyfikacje szablonu strony przez OLX, moduł stosuje wielowariantowy łańcuch ekstrakcji stanu SSR:

1. **Wzorzec Główny**: `<script id="__PRERENDERED_STATE__"[^>]*>(.*?)</script>`
2. **Wzorzec Alternatywny 1**: `window\.__PRERENDERED_STATE__\s*=\s*"?(\{.*?\})"?;`
3. **Wzorzec Alternatywny 2 (JSON-LD)**: `<script type="application/ld\+json"[^>]*>(.*?)</script>`
4. **Fallback HTML (Link Harvester)**: Wyrażenie regex `href="(/d/oferta/[^"]+)"` tworzące zredukowany obiekt awaryjny.

### 3.3. Nagłówki HTTP (Browser Emulation & WAF)
```python
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Sec-Ch-Ua': '"Chromium";v="124", "Not(A:Brand";v="24", "Google Chrome";v="124"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1'
}
```

---

## 4. Kontrakty Danych i Baza Danych (`db.py`)

### 4.1. Zoptymalizowany Schemat `raw_payload` (Optymalizacja $O(1)$)
Zgodnie z konsensusem po peer review, `OLXProvider` spłaszcza kluczowe atrybuty do korzenia słownika przed zapisem do `bronze_listings`. Zapewnia to bezpośredni odczyt pól przez SQLite bez obciążających podzapytań `json_each`.

```json
{
  "id": "918273645",
  "title": "Mieszkanie 3 pokoje Ursynów Imielin blisko metra",
  "url": "https://www.olx.pl/d/oferta/mieszkanie-3-pokoje-ursynow-imielin-CID3-ID12345.html",
  "price_pln": 1020000.0,
  "area_m2": 58.5,
  "rooms": 3,
  "floor": 2,
  "total_floors": 10,
  "has_elevator": 1,
  "build_year": 1985,
  "seller_type": "Bezpośrednio",
  "description_text": "Sprzedam bezpośrednio 3-pokojowe mieszkanie na Ursynowie. Budynek posiada nową windę...",
  "location": {
    "city": "Warszawa",
    "district": "Ursynów",
    "coordinates": {
      "latitude": 52.1485,
      "longitude": 21.0452
    }
  },
  "raw_olx_data": {
    "params": [
      {"key": "price", "value": {"value": 1020000}},
      {"key": "m", "value": {"value": 58.5}},
      {"key": "rooms", "value": {"key": "three"}},
      {"key": "floor_select", "value": {"key": "floor_2"}},
      {"key": "elevator", "value": {"key": "yes"}}
    ],
    "user": {
      "is_business": false
    }
  }
}
```

### 4.2. Logika Mapowania w Widoku `silver_listings`
Dzięki pre-normalizacji w Pythonie, widok `silver_listings` korzysta z uniwersalnych i ultra-szybkich selektorów:
* `price_pln`: `CAST(COALESCE(json_extract(b.raw_payload, '$.price_pln'), json_extract(b.raw_payload, '$.price.value')) AS REAL)`
* `area_m2`: `CAST(COALESCE(json_extract(b.raw_payload, '$.area_m2'), json_extract(b.raw_payload, '$.area.value')) AS REAL)`
* `rooms`: `CAST(COALESCE(json_extract(b.raw_payload, '$.rooms'), json_extract(b.raw_payload, '$.roomsNumber')) AS INTEGER)`
* `floor`: `CAST(COALESCE(json_extract(b.raw_payload, '$.floor'), json_extract(b.raw_payload, '$.floorNumber')) AS INTEGER)`
* `has_elevator`: `COALESCE(CAST(json_extract(b.raw_payload, '$.has_elevator') AS INTEGER), CASE WHEN json_extract(b.raw_payload, '$.description_text') LIKE '%winda%' THEN 1 ELSE 0 END)`
* `lat` / `lon`: `CAST(json_extract(b.raw_payload, '$.location.coordinates.latitude') AS REAL)` / `longitude`
* `seller_type`: `COALESCE(json_extract(b.raw_payload, '$.seller_type'), 'Agencja')`

---

## 5. Audyt Kompletności Uruchomień (`run_audit`)

1. `OLXProvider` wyciąga zdeklarowaną liczbę ogłoszeń ze struktury stanu SSR (`props.pageProps.data.adSearch.totalElements` lub `totalCount`) albo z nagłówka HTML regex `r'(\d+[\s\d]*)\s*(?:ogłosze|ofert)'`.
2. Zapisuje metrykę do tabeli `run_audit`:
   ```python
   self.db_manager.save_run_audit(
       run_id=run_id,
       source_portal="olx",
       expected_total=expected_total_olx,
       saved_bronze=saved_count
   )
   ```
3. W konsoli `main.py` wyświetlane jest podsumowanie:
   `📊 Audyt Kompletności Olx: 50/54 (92.6% kompletności w Bronze)`

---

## 6. Wybory Architektoniczne i Trade-offy

1. **Opcja 1 (Wiodąca): Direct HTTP Client + SSR State Parser + Pre-normalization $O(1)$**:
   - Maksymalna wydajność (~1-2s na uruchomienie).
   - Pełne dane strukturalne (w tym precyzyjny GPS, winda, kondygnacja).
   - Zerowy narzut na czas zapytań SQL w `silver_listings`.
2. **Opcja 2: API Mobilne OLX**: Odrzucone ze względu na ryzyko rotacji kluczy OAuth i blokady IP.
3. **Opcja 3: Headless Browser (Playwright)**: Odrzucone z uwagi na potężny narzut RAM/CPU i powolne działanie.

---

## 7. Obsługa Błędów, Antybotów i Przypadków Brzegowych

* **HTTP 403 / 429**: Zastosowanie Exponential Backoff (1.5s, 3.0s). W razie trwałej blokady następuje bezpieczne zakończenie pobierania (graceful degradation) i zachowanie dotychczasowych rekordów w Bronze bez wywalania `main.py`.
* **Mapowanie Pięter**: Mapowanie specyficznych kluczy OLX (`floor_0` -> 0, `floor_1` -> 1, ..., `floor_higher` -> 12, `parter` -> 0).
* **Brakujące Koordynaty**: Przełączenie na zapasowy algorytm deduplikacji po atrybutach fizycznych lokalu w `gold_listings`.

---

## 8. Konsensus Architektoniczny po Peer Review

W wyniku dyskusji i recenzji inżynierskiej:
1. **Wyeliminowano zagrożenie wąskiego gardła w `db.py`**: Zamiast 5 podzapytań `json_each` per wiersz w widoku `silver_listings`, zastosowano normalizację $O(1)$ w Pythonie wewnątrz `OLXProvider`.
2. **Zapewniono multi-pattern parsing stanu SSR**: Zabezpieczenie przed zmianami w szablonie strony OLX (obsługa `__PRERENDERED_STATE__`, JSON-LD i regex link harvester).
3. **Zapewniono bezstratną retencję danych**: Pełny obiekt z OLX trafia do `bronze_listings`, umożliwiając re-parsowanie historycznych zrzutów bez utraty danych.

---
*Dokument zatwierdzony i gotowy do realizacji zgodnie z planem w `tasks.md`.*
