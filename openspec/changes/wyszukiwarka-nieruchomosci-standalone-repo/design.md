# OpenSpec Design: Wydzielenie Wyszukiwarki Nieruchomości do Osobnego Repozytorium (Standalone Repository Architecture)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-standalone-repo`  
**Data**: 16 Sierpnia 2026  
**Status**: Projekt Techniczny (Design)  
**Dokumenty Wejściowe**: 
- [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-standalone-repo/proposal.md)
- [git-agent SKILL.md](file:///Users/pawel/git/gen-ai-orchestrator/.agents/skills/git-agent/SKILL.md)
- [opsx-validate-repo.sh](file:///Users/pawel/git/gen-ai-orchestrator/.ai/tools/opsx-validate-repo.sh)
- [.ai/guidelines/brutally-honest-rules.md](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Cel i Zakres Architektury (Context & Goals)

Celem zmiany jest fizyczna separacja aplikacji biznesowej `wyszukiwarka-nieruchomosci` z monolitycznego drzewa `gen-ai-orchestrator` do dedykowanego repozytorium `/Users/pawel/git/wyszukiwarka-nieruchomosci`, przy jednoczesnym zachowaniu możliwości orkiestracji zmian przez `gen-ai-orchestrator` za pośrednictwem symlinków w `.repositories/` i `.ai/repositories/`.

### Główne cele:
1. **Niezależne repozytorium Git**: Utworzenie czystego repozytorium Git w `/Users/pawel/git/wyszukiwarka-nieruchomosci` z dedykowaną historią commitów, `.gitignore`, `requirements.txt` oraz `README.md`.
2. **Pełna funkcjonalność aplikacji**: Przeniesienie wszystkich modułów (`src/`, `tests/`, `historia/`, `data/`, `kryteria.md`, `main.py`) bez utraty bazy danych SQLite `listings.db` i historii zrzutów.
3. **Rejestracja w orkiestratorze**: Zarejestrowanie nowej lokalizacji w `.repositories/wyszukiwarka-nieruchomosci` i `.ai/repositories/wyszukiwarka-nieruchomosci`.
4. **Czystość orkiestratora**: Usunięcie fizycznego podkatalogu z `gen-ai-orchestrator` po pomyślnej weryfikacji.

---

## 2. Architektura i Przepływ Migracji (System Architecture & Flow)

```
KROK 1: Kopiowanie & Inicjalizacja         KROK 2: Walidacja & Testy        KROK 3: Rejestracja & Cleanup
┌───────────────────────────────┐         ┌─────────────────────────┐      ┌─────────────────────────┐
│ gen-ai-orchestrator/          │         │ Nowe Repo:              │      │ gen-ai-orchestrator/    │
│ wyszukiwarka-nieruchomosci/   │         │ /Users/pawel/git/       │      │ .repositories/          │
│ ├─ src/                       │         │ wyszukiwarka-.../       │      │ └─ wyszukiwarka-... ──┐ │
│ ├─ tests/                     │ ──────► │ ├─ 42 testy jednostkowe │      │                       │ │
│ ├─ data/                      │         │ ├─ test CLI (--cache)   │      │                       ▼ │
│ └─ ...                        │         │ └─ initial git commit   │      │ /Users/pawel/git/...    │
└───────────────────────────────┘         └─────────────────────────┘      └─────────────────────────┘
```

### 🧭 Szczegółowe Reguły i Kontrakty:

1. **Struktura Plików Nowego Repozytorium (`/Users/pawel/git/wyszukiwarka-nieruchomosci`)**:
   ```
   wyszukiwarka-nieruchomosci/
   ├── .git/
   ├── .gitignore
   ├── README.md
   ├── requirements.txt
   ├── kryteria.md
   ├── main.py
   ├── src/
   │   ├── config.py
   │   ├── db.py
   │   ├── deduplicator.py
   │   ├── rcn_client.py
   │   ├── report_generator.py
   │   └── providers/
   │       ├── adresowo.py
   │       ├── commercial.py
   │       ├── direct.py
   │       ├── gratka.py
   │       ├── morizon.py
   │       ├── nieruchomosci_online.py
   │       └── olx.py
   ├── tests/
   │   ├── test_adresowo_criteria.py
   │   ├── test_completeness.py
   │   ├── test_elt_pipeline.py
   │   ├── test_gratka_criteria.py
   │   ├── test_morizon_criteria.py
   │   ├── test_multi_portal_regression.py
   │   ├── test_nieruchomosci_online_criteria.py
   │   └── test_olx_criteria.py
   ├── data/
   │   └── listings.db
   └── historia/
       └── *.md
   ```

2. **Zawartość `.gitignore`**:
   - `__pycache__/`
   - `*.pyc`
   - `.DS_Store`
   - `data/test_debug*.db` (bazy testowe tymczasowe)
   - `.env` / `venv/`
   - Baza produkcyjna `data/listings.db` oraz pliki raportów `historia/` powinny pozostać w repozytorium jako stan referencyjny.

3. **Zależności w `requirements.txt`**:
   - `requests>=2.31.0`
   - `urllib3>=2.0.0`
   - `fastapi` / `uvicorn` (pod kątem nadchodzącego UI)

4. **Rejestracja w `gen-ai-orchestrator`**:
   - Utworzenie dowiązań symbolicznych:
     - `ln -s /Users/pawel/git/wyszukiwarka-nieruchomosci .repositories/wyszukiwarka-nieruchomosci`
     - `ln -s /Users/pawel/git/wyszukiwarka-nieruchomosci .ai/repositories/wyszukiwarka-nieruchomosci`
   - Walidacja bezpieczeństwa skryptem `./.ai/tools/opsx-validate-repo.sh .repositories/wyszukiwarka-nieruchomosci`.

---

## 3. Wybory Architektoniczne i Trade-offy (Architectural Trade-offs)

1. **Kopiowanie vs `git subtree split` / `git filter-repo`**:
   - **Kopiowanie czystego kodu z initial commit**:
     - *Zalety*: Czyste, przejrzyste nowe repozytorium bez śmieci z orkiestratora i historii innych projektów.
     - *Wady*: Utrata mikroskopijnej historii commitów z branchy orkiestratora (które i tak były w 95% commitem archiwizującym).
     - *Wybór*: **Kopiowanie stanu i czysty initial commit** – rekomendowany, standardowy proces dla wyodrębniania subprojektów w tym środowisku.
2. **Zachowanie bazy SQLite `listings.db` w nowym repo**:
   - Baza `listings.db` (ok. 7 MB) zawiera aktualny zrzut z warstwy Bronze z 6 serwisów. Jej zachowanie pozwala na natychmiastowe uruchomienie CLI i testów w trybie `--cache` bez konieczności ponownego scrapowania sieci.

---

## 4. Obsługa Sytuacji Awaryjnych i Krawędziowych (Edge Cases & Safety)

1. **Walidacja Pętli Symlinków**: Skrypt `opsx-validate-repo.sh` weryfikuje, czy symlink nie wskazuje rekurencyjnie na podkatalog orkiestratora.
2. **Weryfikacja Kompletności Testów**: Usunięcie katalogu `wyszukiwarka-nieruchomosci/` z `gen-ai-orchestrator` nastąpi **wyłącznie po** 100% zaliczeniu testów jednostkowych (`42/42 passed`) w nowej lokalizacji.
