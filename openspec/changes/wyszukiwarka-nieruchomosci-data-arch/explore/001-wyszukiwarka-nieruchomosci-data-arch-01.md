# Eksploracja Architektury Danych: Wyszukiwarka Nieruchomości ELT (Bronze / Silver / Gold)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-data-arch`  
**Data**: 27 Lipca 2026  
**Status**: W trakcie eksploracji (OpenSpec Explore)  
**Dokumenty Referencyjne**: 
- `openspec/changes/wyszukiwarka-nieruchomosci-data-arch/proposal_architektury_nieruchomosci.pdf`
- `wyszukiwarka-nieruchomosci/kryteria.md`
- `.ai/guidelines/brutally-honest-rules.md`

---

## 1. Cel i Kontekst Zmiany

Zgodnie z nowym podejściem architektonicznym (opisanym w propozycji PDF), odchodzimy od dotychczasowego modelu tłumienia wyników na etapie zapytań HTTP do portali (gdzie nakładano liczne parametry filtrowania bezpośrednio w URL / API portalu). 

**Nowa Koncepcja (ELT - Extract, Load, Transform)**:
1. **Ekstrakcja (Extract)**: Pobieramy szeroki strumień ogłoszeń z danego serwisu wyłącznie w oparciu o szeroki parametr lokalizacyjny (np. **Miasto: Warszawa** z `kryteria.md`).
2. **Ładowanie (Load - Warstwa Bronze)**: Surowe odpowiedzi w formacie JSON (lub surowy HTML z osadzonym `<script id="__NEXT_DATA__">`) są natychmiastowo zapisywane do tabeli `bronze_listings` w relacyjnej bazie **SQLite** bez wstępnego parsowania i walidacji.
3. **Transformacja i Filtracja (Transform - Warstwa Silver)**: Wszystkie filtry bizneowe zdefiniowane w `kryteria.md` (np. cena, metraż, pokoje, piętro, parter, winda, stan prawny, dzielnica) zostają przeniesione do warstwy bazy danych SQLite z wykorzystaniem funkcji JSON1 (`json_extract`, `json_tree`).
4. **Deduplikacja i Analityka (Warstwa Gold)**: Deduplikacja międzyserwisowa po unikalnym hashu nieruchomości (`round(lat,3)_round(lon,3)_area_rooms`) oraz integracja z danymi referencyjnymi transakcji (RCiWN).

---

## 2. Nazywanie Niepewności i Ograniczeń wprost (Brutally Honest Analysis)

Zgodnie z zasadami z pliku `.ai/guidelines/brutally-honest-rules.md`, poniżej bezkompromisowo punktujemy niepewności, ograniczenia techniczne i luki kontekstowe zaproponowanego podejścia:

### ⚠️ A. Paginacja i Limity Pobierania Portali (Portal Limits)
- **Fakt**: Portale takie jak Otodom czy OLX stosują twarde limity paginacji (np. maksymalnie 50 stron po 24/36 ofert, co daje limit ~1200-2000 ofert per zapytanie).
- **Niepewność / Wyzwanie**: Na podstawie dostępnych informacji, w mieście takim jak Warszawa liczba aktywnych ogłoszeń mieszkań na pojedynczym portalu może wynosić od 5 000 do ponad 15 000. 
- **[Hipoteza/Domysł]**: Zapytanie portalu o "całą Warszawę" bez podziału na pod-kategorie (np. rynki: pierwotny/wtórny lub przedziały cenowe) spowoduje ucięcie wyników na 50. stronie i utratę pozostałych ofert! 
- **Rekomendacja architektoniczna**: Pobieranie szerokie w warstwie Bronze może wymagać podziału na tzw. *Extraction Chunks* (np. `Warszawa + Rynek Pierwotny`, `Warszawa + Rynek Wtórny` lub podział według dzielnic na poziomie zapytania HTTP), mimo że pełna filtracja biznesowa odbywa się w SQLite.

### ⚠️ B. Parsowalność i Kompletność Surowego JSON-a (Schema Variability)
- **Fakt**: Dane surowe z portali komercyjnych (Otodom, OLX) i portali ogłoszeń bezpośrednich (Adresowo, Sprzedajemy) mają drastycznie różne struktury JSON.
- **Niepewność**: Część parametrów z `kryteria.md` (np. *Stan prawny: Spółdzielcze własnościowe z KW*, *Winda*, *Wyklucz ostatnie piętro*) często nie występuje wprost jako ustrukturyzowane pole w JSON-ie i bywa ukryta w treści opisu ogłoszenia.
- **[Hipoteza/Domysł]**: Wyciągnięcie relacji "czy piętro jest ostatnie" wymaga znajomości całkowitej liczby pięter w budynku (`total_floors`). Jeśli portal zwraca tylko `floor=4` bez `total_floors`, filtr w SQL nie będzie w stanie rozstrzygnąć tego warunku deterministycznie.
- **Nazwanie Luki**: Brak weryfikacji, które dokładnie polskie słowa kluczowe w tekstach opisów odpowiadają stanom prawnym / wykończeniom.

### ⚠️ C. Odległość od Metra i Geolokalizacja w SQLite
- **Fakt**: Kryterium *Maksymalna odległość od stacji metra (m)* w `kryteria.md` wymaga obliczania dystansu przestrzennego (np. wzór Haversine'a).
- **Ograniczenie**: Standardowa kompilacja SQLite nie posiada wbudowanych funkcji trygonometrycznych (sin/cos/radians/acos) ani modułu SpatiaLite, chyba że zostaną zarejestrowane customowe funkcje w Pythonie (`sqlite3.create_function`) lub wyliczone przy użyciu przybliżeń kartezjańskich.

---

## 3. Szczegółowe Mapowanie Kryteriów z `kryteria.md` na SQLite

Poniżej przedstawiono propozycyjne mapowanie poszczególnych sekcji z `kryteria.md` na konstrukcję widoku SQL (`silver_listings`) na bazie danych w `bronze_listings`:

### Schemat Tabeli Bronze (`bronze_listings`)
```sql
CREATE TABLE IF NOT EXISTS bronze_listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_portal TEXT NOT NULL,          -- np. 'otodom', 'olx', 'adresowo'
    city TEXT NOT NULL,                   -- np. 'Warszawa'
    raw_payload JSON NOT NULL,            -- Pełny surowy JSON ogłoszenia / strony
    scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Mapowanie Warunków Filtracji w Warstwie Silver (`silver_listings`)

| Sekcja w `kryteria.md` | Parametr | Obsługa w SQL (Widok `silver_listings`) | Uwagi i Ograniczenia |
| :--- | :--- | :--- | :--- |
| **📍 Lokalizacja** | Miasto = Warszawa | `city = 'Warszawa'` (w warstwie Bronze) | Pobieranie na poziomie skryptu ekstrakcji. |
| | Dzielnice = [Ursynów] | `json_extract(raw_payload, '$.location.district') IN ('Ursynów')` | Wymaga ujednolicenia nazw dzielnic (np. Ursynów vs Warszawa-Ursynów). |
| | Odległość od metra | Custom SQL function `haversine_m(lat, lon, metro_lat, metro_lon)` lub kalkulacja w Python/Gold | Standardowy SQLite wymaga zarejestrowania funkcji w Pythonie. |
| **🏠 Nieruchomość** | Typ = Mieszkanie | `json_extract(raw_payload, '$.category') = 'mieszkanie'` | Flaga w JSON. |
| | Typ ogłoszeniodawcy | `json_extract(raw_payload, '$.estate') IN ('private', 'agency')` | Zależy od słownika portalu. |
| | Rynek | `json_extract(raw_payload, '$.market') IN ('primary', 'secondary')` | Mapowanie wartości 'Pierwotny' / 'Wtórny'. |
| | Cena (PLN): 800k - 1.2M | `CAST(json_extract(raw_payload, '$.price') AS REAL) BETWEEN 800000 AND 1200000` | Przekształcenie na typ numeryczny. |
| | Max cena za m² | `(price / area) <= max_price_per_m2` | Wyliczane dynamicznie, gdy `max_price_per_m2 IS NOT NULL`. |
| | Liczba pokoi: 3 | `CAST(json_extract(raw_payload, '$.rooms') AS INT) = 3` | Filtrowanie dokładne. |
| | Piętro min/max: 1 - 8 | `CAST(json_extract(raw_payload, '$.floor') AS INT) BETWEEN 1 AND 8` | Parter to piętro 0. |
| | Wyklucz parter: Tak | `CAST(json_extract(raw_payload, '$.floor') AS INT) > 0` | Parter (`floor = 0`) jest odrzucany. |
| | Wyklucz ostatnie piętro | `floor < total_floors` lub sprawdzanie w opisie | **[Hipoteza/Domysł]**: Wymaga pola `total_floors` w JSON payloadzie. |
| **🛠️ Wyposażenie** | Winda = Tak | `json_extract(raw_payload, '$.features.elevator') = 1` lub regex w tekście opisu | Często wymaga parsowania tablicy tagów/wyposażenia. |
| | Balkon / Taras | Sprawdzanie flag wyposażenia w JSON | Elastyczny warunek. |
| | Miejsce garażowe | Sprawdzanie flag wyposażenia w JSON | Niewymagane w kryteriach. |
| | Stan wykończenia | Mapowanie pola `finish_status` w JSON | Słownik portalu (do zamieszkania, do remontu). |
| | Stan prawny | Regex na treści opisu / flaga `legal_status` | Często obecny tylko w opisie tekstowym. |

---

## 4. Architektura Rurociągu ELT i Propozycja Zapytania Widoku SQL

Przykładowa definicja widoku `silver_listings` w SQLite wykorzystująca `JSON1`:

```sql
CREATE VIEW IF NOT EXISTS silver_listings AS
WITH parsed_listings AS (
    SELECT 
        id AS bronze_id,
        source_portal,
        scraped_at,
        json_extract(raw_payload, '$.id') AS external_id,
        json_extract(raw_payload, '$.title') AS title,
        json_extract(raw_payload, '$.location.city') AS city,
        json_extract(raw_payload, '$.location.district') AS district,
        CAST(json_extract(raw_payload, '$.price.value') AS REAL) AS price_pln,
        CAST(json_extract(raw_payload, '$.area.value') AS REAL) AS area_m2,
        CAST(json_extract(raw_payload, '$.rooms') AS INTEGER) AS rooms,
        CAST(json_extract(raw_payload, '$.floor') AS INTEGER) AS floor,
        CAST(json_extract(raw_payload, '$.total_floors') AS INTEGER) AS total_floors,
        json_extract(raw_payload, '$.market') AS market_type,
        json_extract(raw_payload, '$.owner_type') AS seller_type,
        json_extract(raw_payload, '$.features.elevator') AS has_elevator,
        json_extract(raw_payload, '$.location.coordinates.latitude') AS lat,
        json_extract(raw_payload, '$.location.coordinates.longitude') AS lon,
        raw_payload
    FROM bronze_listings
)
SELECT 
    *,
    ROUND(price_pln / area_m2, 2) AS price_per_m2
FROM parsed_listings
WHERE city = 'Warszawa'
  -- Aplikacja Kryteriów Biznesowych z kryteria.md:
  AND (district IN ('Ursynów'))
  AND (price_pln BETWEEN 800000 AND 1200000)
  AND (rooms = 3)
  AND (floor BETWEEN 1 AND 8)
  AND (floor > 0) -- Wyklucz parter
  AND (has_elevator = 1 OR has_elevator IS TRUE);
```

---

## 5. Porównanie Opcji Architektonicznych (Architectural Trade-offs)

| Wymiar | Opcja 1: Czyste SQL Views (Rozszerzenie JSON1) | Opcja 2: Materializowane Tabele Silver (`CREATE TABLE AS`) | Opcja 3: Parsowanie Python -> SQLite z Dedykowanymi Kolumnami |
| :--- | :--- | :--- | :--- |
| **Wydajność zapytań** | Niska przy dużych wolumenach (Dynamiczne parsowanie JSON przy każdym `SELECT`). | Wysoka (Możliwość nakładania indeksów na kolumny `price`, `district`). | Bardzo wysoka (Indeksy SQL od razu na wyciągniętych kolumnach). |
| **Odporność na zmiany schematu** | Bardzo wysoka (JSON jest nienaruszony w Bronze). | Wysoka. | Średnia (Wymaga modyfikacji struktury tabel przy zmianie portalu). |
| **Zgodność z Minimalistycznym ELT** | Maksymalna. | Bardzo wysoka. | Umiarkowana (Przenosi część logiki do Pythona). |
| **Rekomendowany Wybór** | **Opcja 2 (Materializowane Tabele Silver via Python Orkiestrator)** - Zachowuje surowość Bronze, ale zapewnia szybkość filtrowania. |

---

## 6. Kolejne Kroki w Procesie OpenSpec

1. Wygenerowanie pełnego dokumentu propozycji architektonicznej `proposal.md`.
2. Przygotowanie dokumentu projektu technicznego `design.md` z dokładnym schematem klas w Pythonie (`01_extract.py`, `02_transform.py`, `03_report.py`).
3. Dekompozycja zadań w `tasks.md`.
