# Proposal: Constructive Criticism (12 Rules), README Directory Map & Standard Estimation Metrics

**ID**: `orch-constructive-criticizm`  
**Date**: 2026-07-26  

## Summary
Niniejsza propozycja wprowadza 3 kluczowe usprawnienia w systemie `gen-ai-orchestrator`:

1. **Bezwzględna Uczciwość (12 Rules)**: Implementacja Zasad *How to Make Claude Brutally Honest (12 Rules)* w procesach eksploracji (`opsx-explore`), proposali, projektów architektonicznych (`opsx-design`) i recenzji kodu/designu.
2. **Dokumentacja Struktury Repozytorium w `README.md`**: Wzbogacenie głównego pliku `README.md` o przejrzyste drzewo struktury katalogów wraz ze szczegółowym opisem ról każdego z elementów systemu.
3. **Jednolity Szablon Estymacji (`summary.md`), Wsteczna Migracja & Rejestr `archive/changes-summary.md`**:
   - Standaryzacja sekcji estymacji w `summary.md` w ujęciu tabelarycznym z dołączeniem metryk sesji (Wall-clock, Input Tokens, Output Tokens, uśredniony koszt estymatorów).
   - Wsteczna aktualizacja plików `summary.md` dla zarchiwizowanych zmian (`2026-07-26-explore-orchestrator-setup` oraz `2026-07-26-orchestrator-setup-repos`).
   - Utworzenie i automatyczna aktualizacja (po archiwizacji tej oraz kolejnych zmian) zbiorczego pliku `openspec/changes/archive/changes-summary.md` gromadzącego metryki na poziomie każdej zarchiwizowanej zmiany.

---

## Motivation

- **Zapobieganie Halucynacjom i Potwierdzaniu Błędów**: Agenci bez jednoznacznych wytycznych mają tendencję do nadmiernej pewności siebie i ukrywania niepewności. 12 Zasad eliminuje te zjawiska.
- **Czytelność Architektury**: Nowi agenci i użytkownicy potrzebują natychmiastowej wiedzy o przeznaczeniu poszczególnych podkatalogów (`.ai/`, `.agents/`, `openspec/`, `specs/`).
- **Przejrzystość Kosztów, Wydajności i Historii Zmian**: Potrzebujemy spójnego, tabelarycznego sposobu mierzenia nakładu pracy, uśrednionego kosztu estymowanego przez sub-agentów oraz zużycia tokenów i czasu trwania sesji (wall-clock) zarówno w podsumowaniach pojedynczych zmian (`summary.md`), jak i w centralnym rejestrze zbiorczym (`openspec/changes/archive/changes-summary.md`).

---

## Proposed Changes

### 1. Wdrożenie 12 Rules Brutalnej Szczerości
- Utworzenie `.ai/guidelines/brutally-honest-rules.md`.
- Wzbogacenie `openspec/config.yaml` o reguły dla `exploration`, `proposal` i `design`.
- Aktualizacja `.ai/tools/opsx-explore.json` oraz `.ai/tools/opsx-design.json`.

### 2. Rozbudowa `README.md`
- Dodanie kompletnego drzewa folderów z czytelnym opisem podkatalogów i kluczowych plików:
  - `.ai/` (główna struktura instrukcji, narzędzi, skilli i zasobów agnostycznych)
  - `.agents/` (symlinki zgodne ze specyfikacją AGY)
  - `openspec/` (`specs/` dla specyfikacji głównych oraz `changes/` dla prac bieżących i `archive/` dla historii)
  - `specs/` (lokalne wymagania/specyfikacje)
  - Skrypty i narzędzia pomocnicze (`openspec-agy-init.sh`, itp.).

### 3. Szablon Estymacji, Wsteczna Migracja & Zbiorczy Rejestr `changes-summary.md`
- Ujednolicenie generatora `summary.md` w `.ai/tools/opsx-estimate.json` / `opsx-archive.json`.
- Przekształcenie sekcji `## ⏱️ Effort Estimation & Metrics` w `summary.md` w spójny format tabelaryczny z uwzględnieniem metryk sesyjnych:
  - Sub-agenci estymujący (czas h, man-days, uśredniony koszt),
  - Metryki sesji (Wall-clock, Input Tokens, Output Tokens, Uśredniony Koszt).
- **Wsteczna aktualizacja**: Przebudowa plików `summary.md` w katalogach zarchiwizowanych zmian (`2026-07-26-explore-orchestrator-setup` oraz `2026-07-26-orchestrator-setup-repos`) do nowego standardu z wyliczonymi metrykami sesyjnymi.
- **Utworzenie zbiorczego pliku**: Utworzenie `openspec/changes/archive/changes-summary.md` zbierającego metryki dotychczasowych zmian:
  - Nazwa zmiany
  - Krótki opis zmiany
  - Podsumowanie sesji (wall clock, tokeny we/wy, szacowany koszt uśredniony od estymatorów)
- **Automatyczna aktualizacja po archiwizacji**: Zapewnienie, że podczas archiwizacji (procedury `opsx-archive`) plik `openspec/changes/archive/changes-summary.md` będzie automatycznie aktualizowany o nowy wpis.

---

## Non-Goals
- Zmiana samego CLI `openspec`.
- Modyfikacja logiki wykonania w `opsx-implement` poza obowiązkiem informowania o brakującym kontekście.
