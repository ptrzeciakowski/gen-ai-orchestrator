# OpenSpec Proposal: Nowoczesny Interfejs Użytkownika React dla Zunifikowanych Ofert Gold i Statystyk Pipeline'u (Real Estate React UI)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-react-ui`  
**Data**: 16 Sierpnia 2026  
**Status**: Propozycja (Proposal) – Gotowa do Refinementu  
**Dokumenty Referencyjne**: 
- [kryteria.md](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md)
- [.ai/guidelines/brutally-honest-rules.md](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)
- [src/db.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py)
- [src/deduplicator.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/deduplicator.py)
- [src/report_generator.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/report_generator.py)
- [src/rcn_client.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/rcn_client.py)
- [main.py](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/main.py)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Obecny przepływ w projekcie `wyszukiwarka-nieruchomosci` generuje statyczne pliki raportów w formacie Markdown w folderze `historia/` (np. `2026-08-15-215519-oferty.md`). Choć raporty te są szczegółowe i zawierają kalkulacje RCN, posiadają istotne ograniczenia użytkowe:

1. **Brak interaktywnej filtracji "w locie"**: Aby przetestować zmianę kryteriów (np. zmiana ceny z 1.0 mln na 1.2 mln zł lub dopuszczenie 2 piętra), użytkownik musi ręcznie edytować plik `kryteria.md` i ponownie uruchamiać skrypt CLI (`python3 main.py --cache`).
2. **Utrudniony przegląd ofert na urządzeniach i w przeglądarce**: Tabele Markdown przy dużej liczbie kolumn (cena, metraż, RCN, linki, portale, piętro, rok) stają się nieczytelne i nie pozwalają na wygodne sortowanie wielokolumnowe, paginację, filtrowanie pełnotekstowe czy podgląd zdjęć.
3. **Niewidoczna telemetria warstw medaliowych (Bronze / Silver / Gold)**: Informacje o tym, ile ofert pobrano z każdego portalu (Otodom, Adresowo, Gratka, Morizon, OLX, NOL), jaki był stopień kompletności (`run_audit`) i ile rekordów odrzucono na etapie deduplikacji/kryteriów, są rozproszone w logach i bazie SQLite.
4. **Brak analityki historycznej runów**: Baza `data/listings.db` przechowuje historię wielu uruchomień (`run_id`), jednak brakuje widoku porównującego trendy cenowe, napływ nowych ofert (`is_new_listing`) oraz stabilność scraperów w czasie.

---

## 2. Cele i Zakres Wymagań (Objectives & Scope)

### 🎯 Główne Wymagania Biznesowe i Funkcjonalne:
1. **Przeglądarka Ofert Warstwy Gold**:
   - Wyświetlanie zdeduplikowanych rekordów z widoku `gold_listings` wzbogaconych o metryki transakcyjne RCN (średnia cena dzielnicy, mediana P50, delta cenowa `%`, wskaźnik okazji `🟢 / 🟡 / 🔴`).
   - Bezpośrednie, klikalne linki do serwisów źródłowych (ze wsparciem dla ofert scalonych z wielu portali, np. `Otodom + Adresowo + Gratka`).
   - Wyróżnienie nowo dodanych ogłoszeń (`is_new_listing`).
   - Karty ofert oraz widok tabelaryczny z sortowaniem (po cenie, cenie za m², metrażu, okazji RCN, dacie).
2. **Dynamiczny Panel Filtrów (Zgodny z `kryteria.md`)**:
   - Interaktywne kontrolki: suwaki cenowe (min/max), cena za m², metraż, liczba pokoi, zakres pięter, przełączniki (wyklucz parter, wyklucz ostatnie piętro, wymagana winda, rynek pierwotny/wtórny, bezpośrednio/agencja, multi-select dzielnic Warszawy).
   - Tryb natychmiastowego filtrowania w UI (client-side/SQL query).
   - Opcja: *"Zapisz obecne filtry jako domyślne do `kryteria.md`"*.
3. **Podsumowanie Warstw Danych (Medallion Architecture Dashboard)**:
   - **Bronze**: Liczba pobranych surowych payloadów per portal, statusy audytu kompletności (`expected_total` vs `saved_bronze`, `%` z tabeli `run_audit`).
   - **Silver**: Liczba znormalizowanych rekordów z poprawnym adresem, geolokalizacją i ceną.
   - **Gold**: Liczba unikalnych nieruchomości po deduplikacji oraz liczba spełniających aktywne filtry.
4. **Wskaźnik Świeżości Danych (Last Refresh Header)**:
   - Czytelny, widoczny w nagłówku znacznik czasu ostatniego odświeżenia danych (np. `Ostatnie odświeżenie: 15.08.2026, godz. 19:53:29 | Run ID: run_20260815_181714`).
   - Status bazy lokalnej (ścieżka do SQLite, rozmiar, status połączenia).
5. **Historyczne Statystyki i Porównanie Runów (Run History)**:
   - Selektor historycznych `run_id` z możliwością przeglądania stanu bazy z dowolnego zrzutu.
   - Wykresy i zestawienia trendów: wolumen ofert w poszczególnych runach, napływ nowych ofert, stabilność portali źródłowych.
6. **Estetyka i UX (Modern React Interface)**:
   - Nowoczesny, responsywny design (brak przestarzałych stylów, przejrzysta typografia, wyważone kolory, animacje przejść, karty ze wskaźnikami statusu).
   - 100% lokalne działanie (baza danych SQLite `data/listings.db` bez wymogu chmury).

---

## 3. Opcje Architektoniczne i Analiza Trade-offów (Architecture Alternatives)

Zgodnie z zasadami *Brutally Honest Guidelines*, przedstawiamy 3 potencjalne warianty implementacji:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│                                ARCHITEKTURA DOCELOWA (OPCJA A)                               │
└─────────────────────────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────┐         REST API (JSON)         ┌─────────────────────────────────┐
    │          React Frontend          │ ◄─────────────────────────────► │       Lokalny Backend API       │
    │   (Vite + React 19 + Lucide)     │   http://localhost:5173         │   (FastAPI / Uvicorn na py3)    │
    │                                  │                                 │      http://localhost:8000      │
    │  - Panel Filtrów (kryteria.md)   │                                 │                                 │
    │  - Siatka Ofert / Tabela Gold    │                                 │  - Endpointy /api/listings      │
    │  - Podsumowanie Warstw B/S/G     │                                 │  - Endpointy /api/runs & audits │
    │  - Analityka Historyczna         │                                 │  - Integracja z DatabaseManager │
    │  - Wskaźnik Świeżości Danych     │                                 │  - Integracja z RCNClient       │
    └──────────────────────────────────┘                                 └────────────────┬────────────────┘
                                                                                          │
                                                                                          ▼
                                                                         ┌─────────────────────────────────┐
                                                                         │       Lokalne Zasoby Danych     │
                                                                         │  - SQLite: data/listings.db     │
                                                                         │  - Config: kryteria.md          │
                                                                         │  - RCN Cache: data/rcn_cache    │
                                                                         └─────────────────────────────────┘
```

### Porównanie Wariantów:

| Kryterium | Opcja A: React (Vite) + Lekki Backend FastAPI (Rekomendowana) | Opcja B: Next.js (Fullstack App Router + SQLite) | Opcja C: Statyczny Dashboard SPA z eksportem JSON z `main.py` |
| :--- | :--- | :--- | :--- |
| **Architektura** | Frontend SPA w React + backend REST w Pythonie korzystający bezpośrednio z istniejących klas `src/db.py`, `src/rcn_client.py`, `src/config.py`. | Monolityczna aplikacja Next.js (Node.js/React) odpytująca SQLite przez `better-sqlite3`. | `main.py` generuje plik `data/dashboard_data.json`, a frontend React wyświetla dane statycznie. |
| **Zalety** | 1. Pełne ponowne wykorzystanie istniejącego kodu Pythona (kalkulator RCN, parsowanie `kryteria.md`, funkcje SQLite `haversine_m`, `regexp`).<br>2. Błyskawiczne filtrowanie SQL po stronie bazy.<br>3. Możliwość wyzwalania odświeżania danych (`--refresh`) jednym kliknięciem z poziomu UI. | 1. Jeden proces uruchomieniowy.<br>2. Nowoczesny ekosystem React Server Components. | 1. Brak działającego serwera backendowego.<br>2. Proste hostowanie. |
| **Wady / Ryzyka** | Wymaga uruchomienia dwóch procesów deweloperskich (lub jednego polecenia `npm run dev` ze skryptem `concurrently`). | Wymaga przepisania logiki kalkulacji RCN i funkcji SQLite (`haversine`, `regexp`) z Pythona na TypeScript/JS. | Brak dynamicznego zapytania SQL – wszystkie filtry i audyty muszą być wyliczone z góry do JSON-a. Niemożliwe wywołanie odświeżenia bazy z UI. |
| **Ocena** | ⭐⭐⭐⭐⭐ **Najlepsza spójność i elastyczność** | ⭐⭐⭐ Zbyt duży narzut na duplikację logiki biznesowej | ⭐⭐ Zbyt sztywne, brak prawdziwej interaktywności |

---

## 4. Szczegółowy Projekt Komponentów i Endpointów API

### 4.1. Endpointy Backendowe (`src/api.py`):
- `GET /api/status`: Zwraca metadane bazy, ścieżkę, informację o najnowszym `run_id`, datę i czas ostatniego zrzutu oraz ogólne podsumowanie.
- `GET /api/criteria`: Zwraca aktualne parametry sparsowane z `kryteria.md`.
- `POST /api/criteria`: Aktualizuje zawartość `kryteria.md` na dysku.
- `GET /api/listings`: Pobiera oferty z warstwy Gold dla zadanego `run_id` z nałożeniem filtrów przekazanych w query params (`min_price`, `max_price`, `min_rooms`, `districts`, `elevator`, etc.) wraz z wyliczonymi w locie polami RCN (`rcn_avg_price_m2`, `rcn_p50_m2`, `rcn_delta_pct`).
- `GET /api/layers/summary`: Zwraca statystyki warstw dla wybranego `run_id`:
  - **Bronze**: Liczba rekordów per portal, dane audytowe (`saved_bronze`, `expected_total`, `completeness_pct`).
  - **Silver**: Liczba rekordów poprawnie znormalizowanych, liczba rekordów z prawidłowymi koordynatami GPS.
  - **Gold**: Łączna liczba unikalnych ofert po deduplikacji, rozkład cenowy, liczba nowości.
- `GET /api/runs`: Zwraca listę wszystkich historycznych `run_id` wraz z datami, liczbą ofert i audytem.
- `POST /api/pipeline/refresh`: [Opcjonalne / Zaawansowane] Wyzwala asynchroniczne lub synchroniczne odświeżenie danych z portali w warstwie Bronze.

### 4.2. Struktura Interfejsu Użytkownika (React Components):
1. **`HeaderBar`**:
   - Tytuł aplikacji i status połączenia z lokalną bazą.
   - **Wskaźnik świeżości**: Badż ze stemplem czasowym ostatniego zrzutu (`Ostatnia aktualizacja: 15.08.2026 19:53`).
   - Przełącznik aktywnego `run_id` (najnowszy domyślnie, z możliwością wyboru archiwalnych).
2. **`PipelineLayerSummary`** (Podsumowanie Warstw Danych):
   - 3 interaktywne kafelki / karty:
     - 🥉 **Bronze**: Liczba surowych ofert, pasek kompletności per portal (Otodom, Adresowo, Gratka, Morizon, OLX, NOL).
     - 🥈 **Silver**: Liczba znormalizowanych rekordów, wskaźnik poprawności geokodowania i cen.
     - 🥇 **Gold**: Liczba zunifikowanych mieszkań, wskaźnik redukcji duplikatów (np. `-28% duplikatów`), liczba nowych ogłoszeń `is_new_listing`.
3. **`FilterSidebar` / `FilterDrawer`** (Dynamiczne Filtry):
   - Intuicyjne suwaki z polami numerycznymi (Cena, Powierzchnia, Cena/m²).
   - Wybór liczby pokoi (przyciski multi-toggle `1`, `2`, `3`, `4+`).
   - Wybór piętra (suwak min-max + checkboxy *Wyklucz parter*, *Wyklucz ostatnie piętro*).
   - Wymagania: *Winda* (Wymagana / Dowolnie), *Typ ogłoszeniodawcy* (Bezpośrednio / Agencja / Dowolny), *Rynek*.
   - Multi-select Dzielnic Warszawy (Ursynów, Mokotów, Śródmieście, Wola, etc.).
   - Przycisk *"Resetuj"* oraz *"Zapisz jako domyślne w kryteria.md"*.
4. **`ListingsView`** (Przeglądarka Ofert):
   - Przełącznik widoku: **Karty (Cards)** vs **Tabela Analityczna (Data Grid)**.
   - Karta oferty:
     - Tytuł, dzielnica, ulica (jeśli dostępna), metraż, pokoje, piętro, winda.
     - Cena łączna oraz cena za m².
     - **Wskaźnik RCN**: Porównanie do cen transakcyjnych m.st. Warszawy (Średnia RCN, Mediana P50, Delta `%` z kolorowym badgem).
     - **Źródła i Linki**: Bezpośrednie linki do każdego serwisu, w którym ogłoszenie występuje (np. ikony/przyciski `Otodom`, `Adresowo`, `Gratka`).
     - Badż `NOWOŚĆ` dla ogłoszeń z `is_new_listing = 1`.
5. **`RunHistoryModal` / `AnalyticsTab`** (Historia i Trendy):
   - Zestawienie historycznych uruchomień w czasie.
   - Wykres liczby ofert w poszczególnych runach.
   - Zestawienie średnich cen ofertowych w kolejnych zrzutach.

---

## 5. Identyfikacja Ryzyk i Ograniczeń (Brutally Honest Assessment)

Zgodnie z wytycznymi bezwzględnej szczerości:

1. **[Fakt Empiryczny] Brak miniaturek zdjęć w niektórych źródłach**:
   - Otodom i Adresowo posiadają w `raw_payload` URL-e do zdjęć, jednak Gratka i OLX mogą wymagać dodatkowego parsowania JSON-LD lub linków pośrednich. UI musi posiadać elegancki fallback (placeholder / ikona architektoniczna), gdy miniaturka nie jest dostępna.
2. **[Hipoteza/Domysł] Czas startu i zależności**:
   - Uruchomienie interfejsu React wymaga środowiska Node.js (Vite) oraz Python (FastAPI/Uvicorn). Warto dostarczyć prosty skrypt startowy (np. `./start_ui.sh` lub komendę `npm run dev`), aby użytkownik nie musiał ręcznie konfigurować portów.
3. **[Fakt Empiryczny] Wydajność lokalnej bazy SQLite**:
   - Baza `listings.db` ma obecnie kilka megabajtów (ponad 650 rekordów w Bronze). Zapytania do widoków `silver_listings` i `gold_listings` wykonują się w ułamku sekundy (<50ms). Przy obecnej skali baza lokalna SQLite jest optymalnym, bezawaryjnym rozwiązaniem.
4. **[Ograniczenie] Ręczne wyzwalanie scrapowania z poziomu UI**:
   - Pobieranie danych ze wszystkich 6 portali w trybie `--refresh` trwa od kilkunastu do kilkudziesięciu sekund (zwłaszcza przy throttlingu HTTP). Jeśli dodamy przycisk "Pobierz nowe oferty" w UI, backend powinien raportować status pobierania w czasie rzeczywistym (np. przez SSE lub proste polling endpointu statusu).

---

## 6. Proponowany Plan Wdrożenia (Phased Roadmap)

### Faza 1: Backend API i Warstwa Danych (`src/api.py`)
- [ ] Utworzenie modułu API (FastAPI) z obsługą CORS dla lokalnego hosta (`localhost:5173`).
- [ ] Implementacja endpointów: `/api/status`, `/api/criteria`, `/api/listings`, `/api/layers/summary`, `/api/runs`.
- [ ] Obsługa kalkulacji RCN w locie dla zwracanych ofert Gold.
- [ ] Testy endpointów API (`tests/test_api.py`).

### Faza 2: Inicjalizacja Aplikacji React (Frontend Setup)
- [ ] Utworzenie projektu frontendowego (Vite + React + Vanilla/Tailwind CSS + Lucide Icons) w podkatalogu `ui/` lub `web/`.
- [ ] Konfiguracja typów TypeScript/JS dla ofert, kryteriów, audytów i podsumowań warstw.
- [ ] Utworzenie klienta API (`ui/src/services/api.js`).

### Faza 3: Komponenty Interfejsu i Dashboard Warstw
- [ ] Implementacja `HeaderBar` z datą ostatniego odświeżenia i selektorem `run_id`.
- [ ] Implementacja `PipelineLayerSummary` (Bronze / Silver / Gold metrics).
- [ ] Implementacja `FilterSidebar` z pełną synchronizacją z `kryteria.md`.
- [ ] Implementacja widoku ofert `ListingsView` (karty ofert, badże RCN, multi-linki źródłowe, badże nowości).

### Faza 4: Moduł Analityki Historycznej i Dopracowanie UX
- [ ] Widok statystyk historycznych poprzednich runów (`RunHistoryView`).
- [ ] Dopracowanie stylów, responsywności, pustych stanów (empty states), loaderów i animacji.
- [ ] Skrypt startowy `run_ui.sh` uruchamiający jednocześnie backend API i frontend React.

---

## 7. Pytania do Refinementu (Refinement Questions)

Przed przystąpieniem do etapu przygotowania dokumentu technicznego (`design.md`) i zadań (`tasks.md`), poniżej zebrano kluczowe pytania do wspólnego omówienia:

1. **Lokalizacja frontendu**: Czy preferujesz folder `ui/` / `frontend/` wewnątrz katalogu `wyszukiwarka-nieruchomosci/` (np. `wyszukiwarka-nieruchomosci/ui/`), czy bezpośrednio w głównym repozytorium?
2. **Framework CSS**: Czy preferujesz nowoczesny Tailwind CSS, czy Vanilla CSS / CSS Modules?
3. **Akcja odświeżania zrzutu**: Czy interfejs powinien mieć przycisk *"Pobierz nowe oferty teraz"* (uruchamiający scraper w tle), czy ma służyć wyłącznie do przeglądania i dynamicznego filtrowania istniejącej bazy?
4. **Zapisywanie filtrów**: Czy zmiana filtrów w UI powinna automatycznie nadpisywać plik `kryteria.md`, czy użytkownik powinien mieć dedykowany przycisk *"Zapisz jako domyślne kryteria"*?
