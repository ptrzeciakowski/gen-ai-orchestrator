# OpenSpec Design: Nowoczesny Interfejs Webowy React dla Wyszukiwarki Nieruchomości (Real Estate React UI)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-react-ui`  
**Data**: 16 Sierpnia 2026  
**Status**: Projekt Techniczny (Design)  
**Dokumenty Wejściowe**:
- [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-react-ui/proposal.md)
- [kryteria.md](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/kryteria.md)
- [src/db.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
- [src/deduplicator.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/deduplicator.py)
- [src/rcn_client.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/rcn_client.py)
- [src/config.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/config.py)
- [main.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/main.py)

---

## 1. Cel i Architektura Ogólna (Context & Architecture)

Celem zmiany jest dostarczenie responsywnego, nowoczesnego interfejsu graficznego (SPA w React + lekki backend REST FastAPI), umożliwiającego:
1. Przeglądanie ofert z warstwy Gold w układzie siatki kart oraz interaktywnej tabeli.
2. Dynamiczne filtrowanie "w locie" (cena, metraż, pokoje, piętro, rok budowy, winda, bezpośrednio, dzielnica) z opcją zapisu kryteriów do `kryteria.md`.
3. Porównanie rynkowe RCN (baza cen transakcyjnych m.st. Warszawy, wskaźniki okazji 🟢/🟡/🔴).
4. Telemetrię i audyt warstw medaliowych (**Bronze** -> **Silver** -> **Gold**) oraz historię runów.
5. Możliwość wyzwalania odświeżenia bazy (scrapingu 6 portali w tle) bezpośrednio z UI.

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                    ARCHITEKTURA SYSTEMU UI                                  │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

     ┌────────────────────────────────────────────────────────────────────────┐
     │                      React SPA (Vite + React 19)                       │
     │                      Katalog: wyszukiwarka-nieruchomosci/ui/           │
     │                      Port deweloperski: http://localhost:5173          │
     │                                                                        │
     │  ┌──────────────────────────────────────────────────────────────────┐  │
     │  │ HeaderBar: Świeżość Danych, Selektor Runów, Przycisk Odświeżenia │  │
     │  └──────────────────────────────────────────────────────────────────┘  │
     │  ┌──────────────────────────────────────────────────────────────────┐  │
     │  │ PipelineLayerSummary: Kafelki Medaliowe Bronze / Silver / Gold   │  │
     │  └──────────────────────────────────────────────────────────────────┘  │
     │  ┌───────────────────────────────┬──────────────────────────────────┐  │
     │  │ Dynamic Filter Sidebar        │ ListingsView (Cards & Table)     │  │
     │  │ - Suwaki Ceny, Metrażu        │ - Wskaźniki RCN (Delta %, P50)   │  │
     │  │ - Pokoje, Piętro, Winda, Rok  │ - Multi-linki do Portali         │  │
     │  │ - Zapisz do kryteria.md       │ - Sortowanie, Filtrowanie, Badże │  │
     │  └───────────────────────────────┴──────────────────────────────────┘  │
     └───────────────────────────────────▲────────────────────────────────────┘
                                         │ REST API JSON (CORS)
                                         ▼
     ┌────────────────────────────────────────────────────────────────────────┐
     │                     FastAPI Backend (Uvicorn / Python)                 │
     │                     Moduł: src/api.py | Port: http://localhost:8000    │
     │                                                                        │
     │  - GET /api/status                 - GET /api/criteria                 │
     │  - POST /api/criteria (zapis)      - GET /api/listings (filtry + RCN)  │
     │  - GET /api/layers/summary         - GET /api/runs (historia)          │
     │  - POST /api/pipeline/refresh      - GET /api/pipeline/status          │
     └───────────────────────────────────┬────────────────────────────────────┘
                                         │
                                         ▼
     ┌────────────────────────────────────────────────────────────────────────┐
     │                 Istniejący Silnik Python & SQLite                      │
     │  - src/db.py (DatabaseManager, Widoki Silver i Gold)                   │
     │  - src/deduplicator.py (Deduplicator z filtrami i konsolidacją)        │
     │  - src/rcn_client.py (Baza RCN i wyznaczanie benchmarków cenowych)    │
     │  - src/config.py (Parser i serializator kryteria.md)                   │
     │  - main.py (Orkiestracja scrapingu 6 portali w tle)                    │
     └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Specyfikacja Endpointów Backendowych (`src/api.py`)

Backend oparty o `FastAPI` integruje istniejące moduły domeny bez dublowania logiki biznesowej:

1. **`GET /api/status`**:
   - Zwraca: `db_path`, `latest_run_id`, `last_scraped_at`, `total_bronze`, `total_gold`, `is_scraping_active`.
2. **`GET /api/criteria`**:
   - Parsuje `kryteria.md` przez `CriteriaConfig.from_markdown()` i zwraca obiekt JSON.
3. **`POST /api/criteria`**:
   - Przyjmuje zaktualizowane kryteria i zapisuje je do pliku `kryteria.md`.
4. **`GET /api/listings`**:
   - Parametry Query: `run_id` (opcjonalny, domyślnie najnowszy), `min_price`, `max_price`, `min_area`, `max_area`, `min_rooms`, `max_rooms`, `min_floor`, `max_floor`, `exclude_ground_floor`, `exclude_last_floor`, `require_elevator`, `min_build_year`, `seller_type`, `districts`, `sort_by`, `sort_dir`.
   - Zwraca listę zdeduplikowanych ofert z warstwy Gold wzbogaconych o metryki RCN (`rcn_avg_m2`, `rcn_p50_m2`, `rcn_delta_pct`, `deal_category`).
5. **`GET /api/layers/summary`**:
   - Zwraca telemetrię medaliową:
     - `bronze`: łączna liczba, rozbicie per portal (`otodom`, `adresowo`, `gratka`, `morizon`, `nieruchomosci-online`, `olx`), dane audytowe z `run_audit`.
     - `silver`: liczba rekordów, poprawność koordynatów GPS, liczba wyekstrahowanych ulic (`street_slug`).
     - `gold`: liczba unikalnych po deduplikacji, stopień kompresji duplikatów (`duplicates_merged_pct`), liczba nowości (`is_new_listing`).
6. **`GET /api/runs`**:
   - Zwraca listę historycznych uruchomień `run_id` wraz ze stemplami czasowymi i liczbą ofert.
7. **`POST /api/pipeline/refresh`**:
   - Uruchamia proces pobierania w tle (Background Task) z 6 portali.
8. **`GET /api/pipeline/status`**:
   - Zwraca aktualny stan zadania pobierania (np. `idle`, `scraping_otodom`, `scraping_adresowo`, `completed`, `error`).

---

## 3. Architektura i Komponenty Frontendu (`ui/`)

Aplikacja React (Vite) zoptymalizowana pod UX, czytelność i responsywność:

1. **`HeaderBar`**:
   - Identyfikacja wizualna, wskaźnik połączenia z backendem.
   - Wskaźnik świeżości: `Ostatni zrzut: 16.08.2026 07:28:01` z selektorem wyboru historycznego `run_id`.
   - Przycisk akcji: **"Odśwież bazę"** (ze stanem ładowania i powiadomieniem o postępie).
2. **`PipelineLayerSummary`**:
   - 3 eleganckie karty wizualizujące architekturę medaliową:
     - 🥉 **Bronze**: Liczba surowych payloadów + mini-wykres kompletności per portal.
     - 🥈 **Silver**: Liczba rekordów znormalizowanych + wskaźnik poprawności GPS.
     - 🥇 **Gold**: Liczba unikalnych mieszkań po deduplikacji + wskaźnik eliminacji duplikatów.
3. **`FilterSidebar`**:
   - Kontrolki filtracji z natychmiastowym feedbackiem:
     - Przedział cenowy (min/max PLN) oraz metrażowy (min/max m²).
     - Pokoje (przełączniki `1`, `2`, `3`, `4+`).
     - Piętro (zakres + checkboxy *Wyklucz parter*, *Wyklucz ostatnie piętro*).
     - Minimalny rok budowy (np. *Od 1975 r.*).
     - Winda (*Wymagana* / *Dowolnie*), Typ ogłoszenia (*Bezpośrednio* / *Dowolnie*).
     - Wybór dzielnic Warszawy (multi-select z Ursynowem jako domyślnym).
     - Przycisk **"Zapisz jako domyślne kryteria (kryteria.md)"**.
4. **`ListingsGrid` & `ListingsTable`**:
   - Przełącznik widoku (Karty vs Tabela).
   - **Karta oferty**:
     - Zdjęcie / placeholder architektoniczny z badżem `NOWOŚĆ` (jeśli `is_new_listing = 1`).
     - Tytuł, ulica, dzielnica, metraż, pokoje, piętro, rok budowy, winda.
     - Cena łączna oraz cena za m².
     - **Badż RCN**: Wskaźnik opłacalności względem cen transakcyjnych (np. `🟢 -9.7% vs RCN` / `🟡 +9.2%`).
     - **Przyciski Źródeł**: Bezpośrednie linki do każdego portalu ze scalonego ogłoszenia (np. *Otodom*, *Gratka*, *Adresowo*).
   - **Tabela Analityczna**:
     - Sortowalne kolumny: Tytuł, Dzielnica, Powierzchnia, Pokoje, Rok, Piętro, Cena, PLN/m², RCN Średnia, RCN Delta %, Typ, Źródła, Link.
5. **Skrypt uruchomieniowy `run_ui.sh`**:
   - Jeden skrypt bash uruchamiający serwer FastAPI (port 8000) oraz frontend Vite (port 5173) z automatycznym otwarciem w przeglądarce.

---

## 4. Testy i Zapewnienie Jakości (Quality Assurance)

1. **Testy Backendowe (`tests/test_api.py`)**:
   - Testowanie wszystkich endpointów FastAPI przy użyciu `httpx.AsyncClient` / `TestClient`:
     - Poprawność zwracania statusu i kryteriów.
     - Filtracja w `/api/listings` (cena, pokoje, winda, rok budowy).
     - Zwracanie poprawnych metryk w `/api/layers/summary`.
     - Aktualizacja `kryteria.md` przez `POST /api/criteria`.
2. **Weryfikacja Budowania Frontendu**:
   - Weryfikacja kompilacji produkcyjnej `npm run build` w katalogu `ui/`.
   - Sprawdzenie braku błędów konsoli i ostrzeżeń lintera.
