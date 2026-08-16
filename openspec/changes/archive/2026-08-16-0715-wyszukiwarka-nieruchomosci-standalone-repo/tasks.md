# Plan Wdrożeniowy: Wydzielenie Wyszukiwarki Nieruchomości do Osobnego Repozytorium

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-standalone-repo`  
**Status**: Ukończony (Completed)  

---

## 📋 Lista Zadań (Tasks)

### Faza 1: Inicjalizacja Nowego Repozytorium Git
- [x] **Zadanie 1.1**: Utworzenie katalogu docelowego `/Users/pawel/git/wyszukiwarka-nieruchomosci` i inicjalizacja Gita (`git init -b main`).
- [x] **Zadanie 1.2**: Skopiowanie struktury plików (`src/`, `tests/`, `data/`, `historia/`, `kryteria.md`, `main.py`).
- [x] **Zadanie 1.3**: Utworzenie plików konfiguracyjnych: `.gitignore`, `requirements.txt` oraz dedykowanego `README.md`.

### Faza 2: Weryfikacja Niezależności i Testy w Nowym Repozytorium
- [x] **Zadanie 2.1**: Uruchomienie pełnego pakietu testów jednostkowych (`python3 -m unittest discover tests`) w nowej lokalizacji i weryfikacja 42 testów (42/42 OK w 0.201s).
- [x] **Zadanie 2.2**: Weryfikacja wykonania CLI w trybie cache (`python3 main.py --cache`) oraz info (`python3 main.py --info`).
- [x] **Zadanie 2.3**: Wykonanie pierwszego commita (`initial commit`) w repozytorium `/Users/pawel/git/wyszukiwarka-nieruchomosci`.

### Faza 3: Integracja z Orkiestratorem i Cleanup
- [x] **Zadanie 3.1**: Utworzenie symlinków w `gen-ai-orchestrator`:
  - `.repositories/wyszukiwarka-nieruchomosci` -> `/Users/pawel/git/wyszukiwarka-nieruchomosci`
  - `.ai/repositories/wyszukiwarka-nieruchomosci` -> `/Users/pawel/git/wyszukiwarka-nieruchomosci`
- [x] **Zadanie 3.2**: Walidacja podpięcia narzędziem `./.ai/tools/opsx-validate-repo.sh .repositories/wyszukiwarka-nieruchomosci`.
- [x] **Zadanie 3.3**: Usunięcie lokalnego katalogu `wyszukiwarka-nieruchomosci/` z repozytorium `gen-ai-orchestrator`.
- [x] **Zadanie 3.4**: Aktualizacja dokumentacji `README.md` w orkiestratorze oraz utworzenie podsumowania zmiany (`summary.md`).
