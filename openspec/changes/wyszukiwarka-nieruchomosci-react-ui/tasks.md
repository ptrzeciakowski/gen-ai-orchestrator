# Plan Wdrożeniowy: Nowoczesny Interfejs Webowy React dla Wyszukiwarki Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-react-ui`  
**Status**: W trakcie realizacji (In Progress)  

---

## 📋 Lista Zadań (Tasks)

### Faza 1: Backend API REST w Pythonie (`src/api.py`)
- [ ] **Zadanie 1.1**: Utworzenie modułu `src/api.py` opartego o FastAPI / Uvicorn z middleware CORS.
- [ ] **Zadanie 1.2**: Implementacja endpointów stanu i kryteriów: `GET /api/status`, `GET /api/criteria`, `POST /api/criteria`.
- [ ] **Zadanie 1.3**: Implementacja endpointu ofert `GET /api/listings` z dynamiczną filtracją SQL, kalkulacją metryk RCN i sortowaniem.
- [ ] **Zadanie 1.4**: Implementacja endpointu telemetrii `GET /api/layers/summary` oraz historii `GET /api/runs`.
- [ ] **Zadanie 1.5**: Implementacja endpointów odświeżania w tle: `POST /api/pipeline/refresh`, `GET /api/pipeline/status`.
- [ ] **Zadanie 1.6**: Utworzenie testów jednostkowych API w `tests/test_api.py` i weryfikacja poprawności.

### Faza 2: Inicjalizacja i Architektura Frontendu React (`ui/`)
- [ ] **Zadanie 2.1**: Zainicjalizowanie projektu React + Vite w katalogu `ui/` z ikonami Lucide i dedykowanym design systemem CSS.
- [ ] **Zadanie 2.2**: Utworzenie warstwy klienta HTTP API (`ui/src/services/api.js`).

### Faza 3: Komponenty Interfejsu Użytkownika
- [ ] **Zadanie 3.1**: Implementacja komponentu `HeaderBar` (świeżość danych, selektor `run_id`, przycisk odświeżania ze statusem).
- [ ] **Zadanie 3.2**: Implementacja komponentu `PipelineLayerSummary` (karty metryk medaliowych Bronze, Silver, Gold).
- [ ] **Zadanie 3.3**: Implementacja komponentu `FilterSidebar` (interaktywne suwaki, przełączniki, multi-select dzielnic, zapis kryteriów).
- [ ] **Zadanie 3.4**: Implementacja komponentów `ListingsGrid` i `ListingsTable` z badżami RCN, multi-linkami do portali i sortowaniem.

### Faza 4: Integracja, Skrypt Uruchomieniowy i Weryfikacja
- [ ] **Zadanie 4.1**: Utworzenie skryptu uruchomieniowego `run_ui.sh` uruchamiającego backend FastAPI i frontend Vite.
- [ ] **Zadanie 4.2**: Weryfikacja budowania produkcyjnego `npm run build` w `ui/`.
- [ ] **Zadanie 4.3**: Uruchomienie pełnego pakietu testów aplikacji i weryfikacja braku regresji.
