# OpenSpec Proposal: Równoległe Pobieranie Ogłoszeń ze Wszystkich Serwisów (Parallel Ingestion Pipeline)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-parallel-ingestion`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/main.py`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Obecna architektura potoku ELT w `main.py` wykonuje pobieranie ofert w sposób **sekwencyjny (synchroniczny)**:
1. `Otodom` (~2 sekundy)
2. `Adresowo` (~2 minuty)
3. `Gratka` (~12 minut)
4. `Morizon` (~6 minut)
5. `Nieruchomosci-online` (~5 minut)
6. `OLX` (~10 sekund)

**Sumaryczny czas pełnego pobierania z 6 portali wynosi obecnie ~25 minut.**
Ponieważ każdy portal reprezentuje niezależną domenę internetową z osobnymi limitami sieciowymi, pobieranie sekwencyjne jest wąskim gardłem.

Wdrożenie **wielowątkowego / asynchronicznego pobierania równoległego (`ThreadPoolExecutor` / `concurrent.futures`)** pozwoli na równoczesne odpytywanie wszystkich 6 serwisów. Całkowity czas wykonania świeżego zrzutu skróci się z **~25 minut do czasu trwania najwolniejszego pojedynczego serwisu (~8–10 minut)**, dając ponad **2.5x–3x przyspieszenie całego procesu**.

---

## 2. Architektura Równoległego Zasilania Bazy (Target Architecture)

```
                       ┌───► OtodomProvider (Worker 1) ──────────┐
                       ├───► AdresowoProvider (Worker 2) ────────┤
                       ├───► GratkaProvider (Worker 3) ──────────┼───► [Thread-Safe SQLite Writer]
[main.py: Parallel] ───┼───► MorizonProvider (Worker 4) ─────────┤         (bronze_listings)
                       ├───► NieruchomosciOnlineProvider (W5) ───┤
                       └───► OLXProvider (Worker 6) ─────────────┘
                                                                           │
                                                                           ▼
                                                             [Gold Deduplication & Report]
```

### 🧭 Kluczowe Założenia Techniczne:
1. **Pula Wątków (`ThreadPoolExecutor`)**:
   - Dedykowany worker dla każdego z 6 providerów (`max_workers=6`).
   - Każdy provider zachowuje własne opóźnienia *politeness delay* (0.15–0.3s) oraz nagłówki przeglądarki, unikając agresywnego uderzania w pojedynczą domenę.
2. **Bezpieczeństwo Zapisu do SQLite (Thread-Safety & WAL Mode)**:
   - Baza danych SQLite w trybie `PRAGMA journal_mode=WAL;` z obsługą `threading.Lock()` lub transakcji per worker dla tabeli `bronze_listings` i `run_audit`.
3. **Izolacja Awarii i Graceful Degradation**:
   - Timeout lub błąd sieciowy w jednym portalu (np. przejściowy błąd Gratki) nie blokuje i nie spowalnia pobierania z pozostałych serwisów.
4. **Live Progress Tracking**:
   - Wyświetlanie postępów pobierania na żywo z poszczególnych wątków.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Moduł `ParallelIngestionManager` (`src/parallel_orchestrator.py` lub rozszerzenie `main.py`)**: Implementacja orkiestratora zarządzającego pulą wątków dla 6 providerów.
- [ ] **Zabezpieczenie Wielowątkowości w `DatabaseManager` (`src/db.py`)**: Weryfikacja blokad SQLite / puli połączeń przy równoczesnych zapisach do `bronze_listings` i `run_audit`.
- [ ] **Aktualizacja `main.py`**: Integracja równoległego uruchamiania z zachowaniem trybu buforowania (Cache) oraz flagi `--refresh`.
- [ ] **Testy Regresji Wielowątkowej (`tests/test_parallel_ingestion.py`)**: Test symulujący równoczesne pobieranie mocków z 6 serwisów i walidację integralności bazy danych.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* ⚡ **Skrócenie czasu pełnego scrapowania**: z ~25 minut do ~8 minut (redukcja o ponad 65%).
* 🛡️ **Brak blokowania potoku**: Szybkie serwisy (Otodom, OLX, Adresowo) natychmiast zasilają bazę bez czekania na wolniejsze portale.
* 📈 **Pełna spójność danych**: Wyniki wszystkich serwisów są konsolidowane w jednym `run_id` i natychmiast przekazywane do warstwy Gold.
