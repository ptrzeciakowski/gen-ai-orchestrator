# OpenSpec Proposal: Konteneryzacja i Przygotowanie Chmurowe (Docker & Compose Pipeline)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-cloud-containerization`  
**Data**: 22 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`run_ui.sh`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/run_ui.sh)
- [`requirements.txt`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/requirements.txt)
- [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Obecnie aplikacja uruchamiana jest lokalnie na stacji deweloperskiej za pomocą skryptu shellowego `run_ui.sh`, wymagając zainstalowanego środowiska Node.js, Pythona 3.10+ oraz bibliotek systemowych.

Przed wdrożeniem w chmurze (np. GCP Cloud Run, AWS ECS lub dedykowanym VPS) konieczne jest:
1. Skonteneryzowanie aplikacji w ujednolicony, lekki i powtarzalny obraz Docker.
2. Zbudowanie frontendu produkcyjnego Vite do statycznych plików i serwowanie ich przez szybki serwer HTTP / serwer backendowy Pythona.
3. Odpowiednie odseparowanie wolumenu danych (`data/listings.db`) oraz plików konfiguracyjnych (`kryteria.md`), aby stan bazy nie ulegał zniszczeniu przy restartach kontenera.

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Wieloetapowy `Dockerfile` (Multi-stage Build)**:
   - **Etap 1 (Node.js)**: Kompilacja produkcyjna frontendu React Vite (`npm run build`).
   - **Etap 2 (Python Alpine/Slim)**: Lekki obraz bazowy z zainstalowanymi zależnościami z `requirements.txt`, serwerem REST API oraz zintegrowanym serwowaniem skompilowanego frontendu.
2. **Plik `docker-compose.yml`**:
   - Definicja usług z mapowaniem portu (np. `8000:8000`), zmiennymi środowiskowymi oraz trwałym wolumenem `./data:/app/data`.
3. **Healthcheck & Endpoint `/api/health`**:
   - Monitoring stanu kontenera pod kątem gotowości na zapytania w chmurze.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Serwowanie statyków w `src/api.py`**: Dodanie obsługi serwowania plików ze zbudowanego katalogu `ui/dist/` dla ścieżek innych niż `/api/*`.
- [ ] **`Dockerfile`**: Wieloetapowy proces budowania (Node 20 + Python 3.12-slim).
- [ ] **`docker-compose.yml` & `.dockerignore`**: Konfiguracja uruchomienia i optymalizacja rozmiaru obrazu.
- [ ] **Testy Budowania i Uruchomienia Kontenera**: Weryfikacja lokalnego startu `docker compose up`.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 📦 **100% powtarzalność środowiska**: Zero problemów z zależnościami systemowymi.
* 🚀 **Gotowość do wdrożenia w chmurze**: Jeden kontener zawierający Frontend + Backend API + Bazę SQLite.
