# Plan Wdrożeniowy: Nowoczesny Interfejs Webowy React dla Wyszukiwarki Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-react-ui`  
**Status**: Ukończony (Completed)  

---

## 📋 Lista Zadań (Tasks)

### Faza 1: Backend API REST w Pythonie (`src/api.py`)
- [x] **Zadanie 1.1**: Utworzenie modułu `src/api.py` opartego o wielowątkowy `ThreadingHTTPServer` z obsługą CORS i formatu JSON.
- [x] **Zadanie 1.2**: Implementacja endpointów stanu i kryteriów: `GET /api/status`, `GET /api/criteria`, `POST /api/criteria`.
- [x] **Zadanie 1.3**: Implementacja endpointu ofert `GET /api/listings` z dynamiczną filtracją SQL, kalkulacją metryk RCN i sortowaniem.
- [x] **Zadanie 1.4**: Implementacja endpointu telemetrii `GET /api/layers/summary` oraz historii `GET /api/runs`.
- [x] **Zadanie 1.5**: Implementacja endpointów odświeżania w tle: `POST /api/pipeline/refresh`, `GET /api/pipeline/status`.
- [x] **Zadanie 1.6**: Utworzenie testów jednostkowych API w `tests/test_api.py` i weryfikacja poprawności (6/6 testów OK).

### Faza 2: Inicjalizacja i Architektura Frontendu React (`ui/`)
- [x] **Zadanie 2.1**: Zainicjalizowanie projektu React 19 + Vite w katalogu `ui/` z ikonami Lucide i dedykowanym design systemem CSS (`index.css`).
- [x] **Zadanie 2.2**: Utworzenie warstwy klienta HTTP API (`ui/src/services/api.js`).

### Faza 3: Komponenty Interfejsu Użytkownika
- [x] **Zadanie 3.1**: Implementacja komponentu `HeaderBar` (świeżość danych, selektor `run_id`, przycisk odświeżania ze statusem).
- [x] **Zadanie 3.2**: Implementacja komponentu `PipelineLayerSummary` (karty metryk medaliowych Bronze, Silver, Gold).
- [x] **Zadanie 3.3**: Implementacja komponentu `FilterSidebar` (interaktywne suwaki, przełączniki, multi-select dzielnic, zapis kryteriów do `kryteria.md`).
- [x] **Zadanie 3.4**: Implementacja komponentu `ListingsView` (siatka kart + tabela, badże RCN, multi-linki do portali, wyszukiwarka i sortowanie).

### Faza 4: Integracja, Skrypt Uruchomieniowy i Weryfikacja
- [x] **Zadanie 4.1**: Utworzenie skryptu uruchomieniowego `run_ui.sh` uruchamiającego backend API i frontend Vite jednym poleceniem.
- [x] **Zadanie 4.2**: Weryfikacja budowania produkcyjnego `npm run build` w `ui/` (zbudowano w 399ms z 0 błędów).
- [x] **Zadanie 4.3**: Uruchomienie pełnego pakietu testów aplikacji (56/56 testów zaliczonych).
