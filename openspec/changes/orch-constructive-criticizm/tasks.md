# Tasks: Constructive Criticism (12 Rules), README Map & Estimation Metrics

## 1. Guideline & Configuration Setup

- [ ] 1.1 Utworzenie pliku kanonicznych zasad `.ai/guidelines/brutally-honest-rules.md`
- [ ] 1.2 Aktualizacja konfiguracyjna `openspec/config.yaml` o reguły dla `proposal` i `design`
- [ ] 1.3 Aktualizacja `.ai/tools/opsx-explore.json` oraz `.ai/tools/opsx-design.json` o wymóg 12 Zasad

## 2. Documentation Map (README.md)

- [ ] 2.1 Rozbudowa `README.md` o pełną strukturę katalogów repozytorium z opisami
- [ ] 2.2 Wytyczenie w `README.md` powiązań między agnostyczną strukturą `.ai/` a symlinkami `.agents/`

## 3. Standard Estimation & Metrics Setup

- [ ] 3.1 Utworzenie/aktualizacja skryptów i narzędzi estymacji (`.ai/tools/opsx-analyze-session.sh`, `.ai/tools/opsx-estimate.json`) z podziałem na dwutabelowy układ w `summary.md`
- [ ] 3.2 Przeprowadzenie wstecznej migracji plików `summary.md` w zarchiwizowanych katalogach `2026-07-26-explore-orchestrator-setup` i `2026-07-26-orchestrator-setup-repos`
- [ ] 3.3 Utworzenie początkowego pliku zbiorczego `openspec/changes/archive/changes-summary.md` z danymi dotychczasowych zmian
- [ ] 3.4 Aktualizacja procedury archiwizacji `.ai/tools/opsx-archive.json` oraz skryptu `openspec-agy-init.sh` do automatycznej aktualizacji `changes-summary.md`

## 4. Skills & Verification

- [ ] 4.1 Uruchomienie skryptu `openspec-agy-init.sh` w celu odświeżenia skilli w repozytorium i globalnej wtyczce AGY
- [ ] 4.2 Walidacja działania i spójności pliku `openspec/changes/archive/changes-summary.md`
