# Plan Dekompozycji Zadań Wdrożeniowych (tasks.md)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-ui-live-refresh`  
**Data**: 22 Sierpnia 2026  
**Status**: Plan Wdrożenia (Tasks - Ukończony)  
**Dokumenty Referencyjne**:
- [`proposal.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-ui-live-refresh/proposal.md)
- [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-ui-live-refresh/design.md)
- [`src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
- [`ui/src/App.jsx`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/ui/src/App.jsx)
- [`ui/src/components/HeaderBar.jsx`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/ui/src/components/HeaderBar.jsx)

---

## 📋 Lista Zadań Wdrożeniowych (Decomposition)

### Faza 1: Rozbudowa Telemetrii w Backend API (`src/api.py`)

- [x] **1.1. Rozszerzenie słownika `pipeline_state` o `portal_stats`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
  - **Opis**: Dodanie inicjalizacji i aktualizowania słownika `portal_stats` w `handle_post_pipeline_refresh()`.
  - **Kryteria Akceptacji**: Endpoint `/api/pipeline/status` zwraca szczegółowy rozkład per portal (`saved`, `status`, `elapsed_s`).
  - **Weryfikacja**: `python3 -m unittest tests/test_api.py`

---

### Faza 2: Implementacja Komponentów Frontendowych React

- [x] **2.1. Utworzenie komponentu `LiveIngestionModal.jsx`**
  - **Plik**: [`wyszukiwarka-nieruchomosci/ui/src/components/LiveIngestionModal.jsx`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/ui/src/components/LiveIngestionModal.jsx)
  - **Opis**: Modal z timerem na żywo, animowanym paskiem postępu, siatką 6 portali ze statusami oraz ekranem podsumowania sukcesu.
  - **Kryteria Akceptacji**: Płynna animacja, obsługa minimalizacji/zamknięcia i automatycznego odświeżenia.

- [x] **2.2. Aktualizacja `HeaderBar.jsx` oraz `App.jsx`**
  - **Pliki**: [`ui/src/components/HeaderBar.jsx`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/ui/src/components/HeaderBar.jsx), [`ui/src/App.jsx`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/ui/src/App.jsx)
  - **Opis**: Wyeksponowany przycisk "Pobierz najnowsze oferty", podpięcie stanu modalu i interwału odpytywania (1s).
  - **Kryteria Akceptacji**: Kliknięcie przycisku otwiera modal i uruchamia proces pobierania.

- [x] **2.3. Style CSS dla modalu i animacji**
  - **Plik**: [`wyszukiwarka-nieruchomosci/ui/src/index.css`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/ui/src/index.css)
  - **Opis**: Dodanie stylów dla modalu (`modal-overlay`, `modal-content`, `progress-track`, `portal-pill`).

---

### Faza 3: Weryfikacja i Kompilacja Produkcyjna

- [x] **3.1. Kompilacja frontendu i testy jednostkowe**
  - **Kryteria Akceptacji**: `npm run build` w `ui/` przechodzi w 100% bez błędów oraz testy Python API zwracają `OK`.
  - **Weryfikacja**: `npm run build` w `ui/` i `python3 -m unittest discover tests`.
