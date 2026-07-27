# OpenSpec Proposal: Orchestrator Skill Single Source of Truth

**Zmiana**: `orchestrator-skill-single-source-of-true`  
**Data**: 27 Lipca 2026  
**Status**: Propozycja (Proposal)  

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Dotychczas instrukcje, wytyczne i konwencje dla komend z rodziny OpenSpec (`opsx-explore`, `opsx-design`, `opsx-tasks`, `opsx-implement`, `opsx-archive`) były rozproszone w 3 miejscach:
1. Plikach konfiguracyjnych `.ai/tools/opsx-*.json`,
2. Plikach `SKILL.md` w repozytorium (zawierających jedynie krótkie odwołania do plików `.json`),
3. Skrypcie `openspec-agy-init.sh` (posiadającym zahardkodowane szablony tekstowe w pliku Bash).

Powodowało to duplikację kodu, trudność w utrzymaniu spójności wytycznych oraz złamanie zasady DRY (Don't Repeat Yourself).

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

Ustanawiamy pliki **`SKILL.md`** w katalogu `.ai/skills/` (zlinkowanym z `.agents/skills/`) jako **Jedyne Źródło Prawdy (Single Source of Truth)** dla wszystkich skilli i komend OpenSpec.

1. **Kanoniczne Instrukcje w `SKILL.md`**:
   - Każdy plik `SKILL.md` zawiera samowystarczalne, pełne wytyczne dotyczące danej fazy cyklu życia OpenSpec.
   - W `opsx-explore` zdefiniowano obowiązek zapisu materiałów eksploracyjnych w podfolderze `explore/` pod nazwą w konwencji `NNN-nazwa-zmiany-MM.<ext>`.
2. **Kopiowanie bez Duplikacji Tekstu w Bashu**:
   - Skrypt `openspec-agy-init.sh` został zrefaktoryzowany tak, aby kopiował skille bezpośrednio z `.ai/skills/*` do globalnego katalogu wtyczek Google Antigravity (`~/.gemini/config/plugins/openspec/skills/`).
3. **Uporządkowanie Archiwum**:
   - Zmiana nazw starych katalogów w `openspec/changes/archive/` na czytelny format oraz aktualizacja zbiorczego rejestru `changes-summary.md`.

---

## 3. Zakres Zmiany (Scope of Work)

- Modyfikacja 5 plików skilli: `.ai/skills/opsx-*/SKILL.md`.
- Refaktoryzacja skryptu instalacyjnego `openspec-agy-init.sh`.
- Uproszczenie odpowiednich plików narzędziowych `.ai/tools/opsx-*.json`.
- Przeniesienie i aktualizacja nazw katalogów w `openspec/changes/archive/`.
- Utworzenie dokumentów OpenSpec (`explore/001-...-01.md`, `proposal.md`, `design.md`, `tasks.md`).
