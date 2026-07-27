# OpenSpec Tasks: Orchestrator Skill Single Source of Truth

**Zmiana**: `orchestrator-skill-single-source-of-true`  
**Data**: 27 Lipca 2026  
**Status**: Wdrożenie Zakończone (Implementation Complete)  

---

## 📋 Lista Zadań Wdrożeniowych

### Faza 1: Ustanowienie `SKILL.md` jako Single Source of Truth dla Skilli OpenSpec
- [x] **Zadanie 1.1**: Zaktualizować `.ai/skills/opsx-explore/SKILL.md` z kanonicznymi regułami (podfolder `explore/`, konwencja `NNN-nazwa-zmiany-MM.<ext>`, Zasady Brutalnej Szczerości).
  - *Weryfikacja*: Odczyt pliku i sprawdzenie obecności wymaganych wytycznych.
- [x] **Zadanie 1.2**: Zaktualizować `.ai/skills/opsx-design/SKILL.md` z zasadami tworzenia `design.md` na bazie materiałów z `explore/` i prezentowania trade-offów.
  - *Weryfikacja*: Odczyt pliku i sprawdzenie sekcji instruktażowych.
- [x] **Zadanie 1.3**: Zaktualizować `.ai/skills/opsx-tasks/SKILL.md` z regułami dekompozycji wdrożeniowej na atomowe zadania z checkboxami w `tasks.md`.
  - *Weryfikacja*: Odczyt pliku i sprawdzenie wytycznych akceptacyjnych.
- [x] **Zadanie 1.4**: Zaktualizować `.ai/skills/opsx-implement/SKILL.md` z nakazem empirycznej weryfikacji kodu przed oznaczaniem statusu `- [x]`.
  - *Weryfikacja*: Sprawdzenie zapisów dotyczących uruchamiania testów/skryptów.
- [x] **Zadanie 1.5**: Zaktualizować `.ai/skills/opsx-archive/SKILL.md` z wymogami dwutabelowej wyceny `summary.md`, datowania `YYYY-MM-DD-HHMM` i aktualizacji `changes-summary.md`.
  - *Weryfikacja*: Sprawdzenie wymogów archiwizacji.

### Faza 2: Refaktoryzacja Skryptu Instalacyjnego i Plików Narzędziowych
- [x] **Zadanie 2.1**: Zrefaktoryzować `openspec-agy-init.sh` tak, aby kopiował `.ai/skills/*` do `~/.gemini/config/plugins/openspec/skills/` bez zahardkodowanych stringów w Bashu.
  - *Weryfikacja*: Uruchomienie `./openspec-agy-init.sh` i zweryfikowanie statusu wyjścia (exit code 0).
- [x] **Zadanie 2.2**: Uprościć `.ai/tools/opsx-*.json` do lekkich wskaźników przekierowujących do `SKILL.md`.
  - *Weryfikacja*: Sprawdzenie czy opisy i argumenty JSON odesłano do `SKILL.md`.

### Faza 3: Uporządkowanie Archiwum Zmian
- [x] **Zadanie 3.1**: Zmienić nazwy wybranych folderów w `openspec/changes/archive/`:
  - `2026-07-26-1914-explore-orchestrator-setup` ➔ `2026-07-26-1914-orchestrator-initial-setup`
  - `2026-07-26-2052-orch-constructive-criticizm` ➔ `2026-07-26-2052-orchestrator-constructive-criticizm`
  - *Weryfikacja*: Wykonanie `ls -la openspec/changes/archive/` i upewnienie się, że pliki istnieją pod nowymi nazwami.
- [x] **Zadanie 3.2**: Zaktualizować tabela zbiorcza w `openspec/changes/archive/changes-summary.md`.
  - *Weryfikacja*: Odczyt pliku i zweryfikowanie wpisów w tabeli.

### Faza 4: Przygotowanie Dokumentacji OpenSpec dla Zmiany
- [x] **Zadanie 4.1**: Utworzyć plik eksploracji w `explore/001-orchestrator-skill-single-source-of-true-01.md`.
  - *Weryfikacja*: Weryfikacja zgodności z konwencją podfolderu `explore/`.
- [x] **Zadanie 4.2**: Utworzyć pliki `proposal.md`, `design.md` oraz `tasks.md`.
  - *Weryfikacja*: Kompletnie przygotowane artefakty w folderze zmiany.
