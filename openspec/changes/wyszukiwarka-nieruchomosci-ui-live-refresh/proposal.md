# OpenSpec Proposal: Interaktywne Odświeżanie Ofert z Portali w Web UI (Live Ingestion Trigger & Progress Modal)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-ui-live-refresh`  
**Data**: 22 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`main.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/main.py)
- [`src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
- [`src/parallel_orchestrator.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/parallel_orchestrator.py)
- [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Użytkownik korzystający z interfejsu przeglądarkowego (React Web UI) nie ma obecnie bezpośredniej, widocznej kontroli nad wyzwalaniem procesu pobierania świeżych ofert z sieci z poziomu interfejsu z czytelnym podglądem postępu.

Chociaż serwer REST API posiada endpoint `POST /api/pipeline/refresh`, w interfejsie użytkownika brakuje:
1. Wyraźnego przycisku w nagłówku aplikacji do uruchomienia pobierania na żądanie.
2. Dedykowanego modalu / paska postępu na żywo informującego, które serwisy aktualnie pracują, ile ofert pobrano oraz jaki jest ogólny postęp potoku (0–100%).
3. Automatycznego odświeżenia widoku ofert i powiadomienia (Toast Notification) po pomyślnym zakończeniu operacji.

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

Wdrożenie komponentu wyzwalania i monitorowania potoku w Web UI:
1. **Przycisk "Pobierz najnowsze oferty" w `HeaderBar`**:
   - Dostępny na głównym pasku nawigacyjnym, z dynamiczną ikoną stanu (gotowy / w trakcie pobierania).
   - Zabezpieczenie przed podwójnym kliknięciem (blokada przycisku i obsługa błędu 409 Conflict z API).
2. **Interaktywny Modal Postępu na Żywo (`LiveIngestionModal`)**:
   - Polling endpointu `/api/pipeline/status` co 1000 ms.
   - Pasek postępu ogólnego (0–100%) oraz wskaźniki per portal (Otodom, Adresowo, Gratka, Morizon, Nieruchomosci-online, OLX).
   - Informacje o błędach w razie problemów z siecią.
3. **Powiadomienie Toast & Auto-Reload**:
   - Po osiągnięciu 100% modal wyświetla podsumowanie i automatycznie przeładowuje siatkę ofert bez konieczności odświeżania całej strony w przeglądarce (`F5`).

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Frontend React (`ui/src/components/LiveIngestionModal.jsx`)**: Komponent modalu ze statusem na żywo, animowanym paskiem postępu i listą statusów portali.
- [ ] **Integracja w `ui/src/components/HeaderBar.jsx`**: Dodanie przycisku wyzwalania pobierania oraz podpięcie modalu.
- [ ] **Obsługa API w `ui/src/api/client.js`**: Funkcje `triggerRefresh()` oraz `getPipelineStatus()`.
- [ ] **Weryfikacja Backend API (`src/api.py`)**: Upewnienie się, że `pipeline_state` precyzyjnie raportuje stan wątków orkiestratora.
- [ ] **Testy Regresji i UI Build**: `npm run build` oraz testy jednostkowe.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* ⚡ **Pełna autonomia użytkownika w Web UI**: Pobieranie świeżych danych jednym kliknięciem bez sięgania do terminala CLI.
* 👁️ **Przejrzystość procesu**: Użytkownik dokładnie widzi, który portal skończył pracę, a który jeszcze pobiera dane.
* 🛡️ **Płynne UX**: Brak zamrażania interfejsu, praca w tle i natychmiastowe odświeżenie danych.
