# OpenSpec Proposal: Wydzielenie Wyszukiwarki Nieruchomości do Osobnego Repozytorium (Standalone Repository Extraction)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-standalone-repo`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/README.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.agents/skills/git-agent/SKILL.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/tools/opsx-validate-repo.sh`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Repozytorium `gen-ai-orchestrator` pełni rolę **centralnej warstwy orkiestracji AI**: zarządza skillami OpenSpec (`.ai/skills/`), agentami (`.ai/agents/`), kanonicznymi wytycznymi (`.ai/guidelines/`) oraz integracją z repozytoriami zewnętrznymi (`.repositories/`).

W toku dotychczasowych etapów prac moduł `wyszukiwarka-nieruchomosci/` rozwinął się w **pełnoprawną, autonomiczną aplikację biznesową**, zawierającą:
- Trójwarstwową architekturę danych SQLite (Bronze -> Silver -> Gold),
- 6 zintegrowanych konektorów do portali (`Otodom`, `Adresowo`, `Gratka`, `Morizon`, `Nieruchomosci-online`, `OLX`),
- Moduł analityki transakcyjnej z Rejestrem Cen Nieruchomości m.st. Warszawy (RCN),
- Silnik deduplikacji, generator raportów Markdown i 42 testy jednostkowe.

Trzymanie kodu aplikacji biznesowej bezpośrednio wewnątrz repozytorium orkiestratora narusza zasadę **Separation of Concerns** (rozdzielenia odpowiedzialności). Zgodnie z docelową architekturą, `gen-ai-orchestrator` powinien zarządzać projektami zewnętrznymi za pośrednictwem dedykowanego agenta `git-agent` oraz rejestru `.repositories/`.

---

## 2. Architektura Docelowa (Target Architecture)

```
gen-ai-orchestrator/                         wyszukiwarka-nieruchomosci/ (Nowe Repozytorium Git)
├── .ai/                                    ├── src/
│   ├── agents/                             │   ├── providers/ (otodom, adresowo, gratka, morizon, ...)
│   ├── skills/                             │   ├── db.py, deduplicator.py, config.py, main.py
│   ├── guidelines/                         │   └── rcn_client.py, report_generator.py
│   └── repositories/                       ├── tests/ (42 testy jednostkowe)
│       └── wyszukiwarka-nieruchomosci ────►├── data/ (listings.db, rcn/)
├── .agents/ (symlinks)                     ├── historia/ (raporty)
├── openspec/ (centralne specs i changes)   ├── kryteria.md
└── README.md                               ├── requirements.txt, README.md, .gitignore
```

### 🧭 Kluczowe Założenia Migracji:
1. **Utworzenie Nowego Repozytorium Git**:
   - Inicjalizacja nowego, samodzielnego repozytorium Git (np. `/Users/pawel/git/wyszukiwarka-nieruchomosci` lub zdalne na GitHub).
   - Przeniesienie pełnego kodu źródłowego, bazy danych, testów, historii raportów i konfiguracji `kryteria.md`.
2. **Niezależne Środowisko i Zależności**:
   - Utworzenie pliku `requirements.txt` / konfiguracji `pyproject.toml` dla niezależnej instalacji w środowisku wirtualnym (`venv`).
   - Przygotowanie dedykowanego pliku `README.md` opisującego instalację, konfigurację `kryteria.md` oraz uruchamianie CLI (`--refresh`, `--cache`, `--info`).
3. **Rejestracja w `gen-ai-orchestrator`**:
   - Dodanie wpisu do rejestru powiązanych repozytoriów w `.ai/repositories/wyszukiwarka-nieruchomosci` (oraz `.repositories/`).
   - Walidacja narzędziem `./.ai/tools/opsx-validate-repo.sh`.
4. **Zarządzanie Cyklem Zmian przez `git-agent`**:
   - Wszelkie kolejne zmiany w wyszukiwarce (np. `parallel-ingestion`, `min-build-year`, `enhanced-deduplication`) będą realizowane w wydzielonym repozytorium z wymuszeniem polityki Feature Branch i Pull Requestów.
5. **Czystość Repozytorium Orkiestratora**:
   - Po zweryfikowaniu działania w nowej lokalizacji, usunięcie lokalnego katalogu `wyszukiwarka-nieruchomosci/` z `gen-ai-orchestrator`.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Krok 1: Inicjalizacja Nowego Repozytorium Git**:
  - Utworzenie katalogu docelowego, inicjalizacja Gita (`git init`).
  - Przeniesienie plików: `src/`, `tests/`, `historia/`, `data/`, `kryteria.md`, `main.py`.
- [ ] **Krok 2: Konfiguracja Niezależnego Projektu**:
  - Przygotowanie `.gitignore` (ignorowanie tymczasowych plików bazodanowych/cache jeśli wymagane, z zachowaniem bazy wzorcowej).
  - Utworzenie `requirements.txt` oraz dokumentacji `README.md`.
- [ ] **Krok 3: Weryfikacja Spójności**:
  - Uruchomienie pełnego zestawu testów jednostkowych (`python3 -m unittest discover tests`) w nowym repozytorium.
  - Wykonanie testowego przeliczenia raportu (`python3 main.py --cache`).
- [ ] **Krok 4: Integracja z Orkiestratorem**:
  - Konfiguracja powiązania w `.ai/repositories/`.
  - Weryfikacja narzędziem `opsx-validate-repo.sh`.
- [ ] **Krok 5: Cleanup Orkiestratora**:
  - Usunięcie katalogu `wyszukiwarka-nieruchomosci/` z głównego drzewa orkiestratora i zaktualizowanie `README.md`.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🏛️ **Czysta Architektura Orkiestratora**: Orkiestrator staje się w 100% generycznym środowiskiem agentowym bez zaśmiecania kodem domenowym konkretnych produktów.
* 🚀 **Autonomia Produktu**: Wyszukiwarka nieruchomości otrzymuje własne wersjonowanie, CI/CD, historię commitów i niezależne repozytorium Git.
* 🤖 **Demonstracja Git-Agenta**: Wszystkie przyszłe zmiany w wyszukiwarce będą orkiestrowane przez `git-agent` z zachowaniem branchingu i PR.
