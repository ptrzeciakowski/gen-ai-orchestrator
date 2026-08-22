# Plan Dekompozycji Zadań Wdrożeniowych (tasks.md)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-parallel-ingestion`  
**Data**: 22 Sierpnia 2026  
**Status**: Plan Wdrożenia (Tasks - Ukończony)  
**Dokumenty Referencyjne**:
- [`proposal.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-parallel-ingestion/proposal.md)
- [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-parallel-ingestion/design.md)
- [`main.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/main.py)
- [`src/db.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
- [`src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)

---

## 📋 Lista Zadań Wdrożeniowych (Decomposition)

### Faza 1: Wzmocnienie Współbieżności Bazy Danych SQLite (`src/db.py`)

- [x] **1.1. Konfiguracja trybu WAL i timeoutów w `src/db.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/db.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
  - **Opis**: Włączenie trybu `PRAGMA journal_mode=WAL;` przy inicjalizacji schematu, dodanie `PRAGMA busy_timeout=60000;` oraz `sqlite3.connect(self.db_path, timeout=60.0)` w `get_connection()`.
  - **Kryteria Akceptacji**: Połączenia SQLite automatycznie czekają do 60s przy ewentualnej rywalizacji o blokadę pliku.
  - **Weryfikacja**: `python3 -c "from src.db import DatabaseManager; db = DatabaseManager(); print(db.test_connection())"`

- [x] **1.2. Zabezpieczenie operacji zapisu muteksem (`threading.Lock`)**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/db.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
  - **Opis**: Zainicjalizowanie `self._write_lock = threading.Lock()` w konstruktorze `DatabaseManager` i objęcie operacji `insert_bronze_listing`, `save_run_audit`, `clear_bronze` blokiem `with self._write_lock:`.
  - **Kryteria Akceptacji**: Brak błędów `sqlite3.OperationalError: database is locked` przy równoczesnym zapisie z wielu wątków.
  - **Weryfikacja**: Test jednostkowy współbieżności.

- [x] **1.3. Wdrożenie metody zapisu wsadowego `insert_bronze_listings_batch`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/db.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
  - **Opis**: Dodanie metody umożliwiającej atomowy zapis listy rekordów JSON do `bronze_listings` za pomocą `executemany`.
  - **Kryteria Akceptacji**: Metoda poprawnie zapisuje listę słowników/krotek w jednej transakcji pod osłoną muteksu.
  - **Weryfikacja**: Test jednostkowy zapisu wsadowego.

- [x] **1.4. Utworzenie testu współbieżności bazy danych `tests/test_db_concurrency.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/tests/test_db_concurrency.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/tests/test_db_concurrency.py)
  - **Opis**: Utworzenie testu symulującego 10 równoległych wątków wykonujących łącznie 500 zapisów do bazy SQLite i weryfikacja spójności danych.
  - **Kryteria Akceptacji**: Wszystkie 500 rekordów zostaje poprawnie zapisanych bez żadnego wyjątku `database is locked`.
  - **Weryfikacja**: `python3 -m unittest tests/test_db_concurrency.py`

---

### Faza 2: Implementacja Modułu Orkiestratora Równoległego (`src/parallel_orchestrator.py`)

- [x] **2.1. Utworzenie klasy `ParallelIngestionOrchestrator`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/parallel_orchestrator.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/parallel_orchestrator.py)
  - **Opis**: Implementacja klasy zarządzającej pulą wątków `ThreadPoolExecutor(max_workers=6)` dla wszystkich 7 providerów (Commercial, Direct, Adresowo, Gratka, Morizon, Nieruchomosci-online, OLX).
  - **Kryteria Akceptacji**: Wszystkie providery są uruchamiane równolegle z zachowaniem pomiaru czasu i izolacji wyjątków.
  - **Weryfikacja**: Import i podstawowa walidacja struktury klasy.

- [x] **2.2. Izolacja błędów sieciowych i obsługa raportu audytowego**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/parallel_orchestrator.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/parallel_orchestrator.py)
  - **Opis**: Każdy wątek providera przechwytuje ewentualny błąd i loguje go do raportu wykonania (`portal_results`), dzięki czemu awaria jednego serwisu nie wpływa na pozostałe.
  - **Kryteria Akceptacji**: Zwracany słownik zawiera pełne zestawienie zapisanych ofert, czasy wykonania per portal oraz zebrane audyty kompletności.
  - **Weryfikacja**: Test integracyjny z mockowanymi awariami providerów.

- [x] **2.3. Utworzenie testu jednostkowego orkiestratora `tests/test_parallel_orchestrator.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/tests/test_parallel_orchestrator.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/tests/test_parallel_orchestrator.py)
  - **Opis**: Test weryfikujący równoczesne wykonanie zadań w puli wątków, izolację wyjątków, przekazywanie `run_id` oraz poprawność agregacji wyników.
  - **Kryteria Akceptacji**: Testy przechodzą w 100% z kodem 0.
  - **Weryfikacja**: `python3 -m unittest tests/test_parallel_orchestrator.py`

---

### Faza 3: Integracja z Potokiem Głównym i REST API

- [x] **3.1. Aktualizacja `main.py` do obsługi potoku równoległego**
  - **Plik**: [`wyszukiwarka-nieruchomosci/main.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/main.py)
  - **Opis**: Zastąpienie sekwencyjnego wywoływania providerów klasą `ParallelIngestionOrchestrator`. Wyświetlanie czytelnych statusów w konsoli (czas trwania, liczba zapisanych ofert per portal, audyt kompletności).
  - **Kryteria Akceptacji**: Flagi `--refresh`, `--cache` oraz `--info` działają zgodnie ze specyfikacją.
  - **Weryfikacja**: `python3 main.py --info` oraz `python3 main.py --cache`

- [x] **3.2. Integracja endpointu `POST /api/pipeline/refresh` w `src/api.py`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
  - **Opis**: Połączenie wątku tła w API z `ParallelIngestionOrchestrator` z aktualizowaniem postępu `progress_pct` i kroków `current_step` dla frontendu React.
  - **Kryteria Akceptacji**: Endpoint zwraca status 202, rozpoczyna proces w tle i aktualizuje stan widoczny w `/api/pipeline/status`.
  - **Weryfikacja**: `python3 -m unittest tests/test_api.py`

---

### Faza 4: Weryfikacja Regresji i Testy Końcowe

- [x] **4.1. Pełna weryfikacja pakietu testów jednostkowych**
  - **Kryteria Akceptacji**: Wszystkie testy (w tym 56 istniejących + nowe testy współbieżności i orkiestratora) kończą się sukcesem (`OK`).
  - **Weryfikacja**: `python3 -m unittest discover tests`

- [x] **4.2. Test walidacyjny potoku na istniejących danych (Cache Mode)**
  - **Kryteria Akceptacji**: Błyskawiczne przeliczenie widoku Gold i wygenerowanie raportu na istniejących danych lokalnych.
  - **Weryfikacja**: `python3 main.py --cache`
