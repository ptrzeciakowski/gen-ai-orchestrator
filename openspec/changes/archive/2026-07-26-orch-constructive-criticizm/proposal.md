# Proposal: Constructive Criticism (12 Rules), README Directory Map & Standard Estimation Metrics

**ID**: `orch-constructive-criticizm`  
**Date**: 2026-07-26  

## Summary
Niniejsza propozycja wprowadza 3 kluczowe usprawnienia w systemie `gen-ai-orchestrator`:

1. **Bezwzględna Uczciwość (12 Rules)**: Implementacja Zasad *How to Make Claude Brutally Honest (12 Rules)* w procesach eksploracji (`opsx-explore`), proposali, projektów architektonicznych (`opsx-design`) i recenzji kodu/designu.
2. **Dokumentacja Struktury Repozytorium w `README.md`**: Wzbogacenie głównego pliku `README.md` o przejrzyste drzewo struktury katalogów wraz ze szczegółowym opisem ról każdego z elementów systemu.
3. **Jednolity Szablon Estymacji (`summary.md`), Wsteczna Migracja & Rejestr `archive/changes-summary.md`**:
   - Standaryzacja sekcji estymacji w `summary.md` w ujęciu tabelarycznym z dołączeniem metryk sesji (Wall-clock, Input Tokens, Output Tokens, estymowane roboczogodziny i roboczodni).
   - Wsteczna aktualizacja plików `summary.md` dla zarchiwizowanych zmian (`2026-07-26-explore-orchestrator-setup` oraz `2026-07-26-orchestrator-setup-repos`).
   - Utworzenie i automatyczna aktualizacja (po archiwizacji tej oraz kolejnych zmian) zbiorczego pliku `openspec/changes/archive/changes-summary.md` gromadzącego metryki na poziomie każdej zarchiwizowanej zmiany.

---

## Motivation

- **Zapobieganie Halucynacjom i Potwierdzaniu Błędów**: Agenci bez jednoznacznych wytycznych mają tendencję do nadmiernej pewności siebie i ukrywania niepewności. 12 Zasad eliminuje te zjawiska.
- **Czytelność Architektury**: Nowi agenci i użytkownicy potrzebują natychmiastowej wiedzy o przeznaczeniu poszczególnych podkatalogów (`.ai/`, `.agents/`, `openspec/`, `specs/`).
- **Przejrzystość Wydajności i Historii Zmian**: Potrzebujemy spójnego, tabelarycznego sposobu mierzenia nakładu pracy (roboczogodziny h oraz roboczodni MD), zużycia tokenów i czasu trwania sesji (wall-clock) zarówno w podsumowaniach pojedynczych zmian (`summary.md`), jak i w centralnym rejestrze zbiorczym (`openspec/changes/archive/changes-summary.md`).

---

## Proposed Changes

### 1. Wdrożenie 12 Rules Brutalnej Szczerości
- Utworzenie `.ai/guidelines/brutally-honest-rules.md`.
- Wzbogacenie `openspec/config.yaml` o reguły dla `proposal` i `design`.
- Aktualizacja `.ai/tools/opsx-explore.json` oraz `.ai/tools/opsx-design.json`.

### 2. Rozbudowa `README.md`
- Dodanie kompletnego drzewa folderów z czytelnym opisem podkatalogów i kluczowych plików.

### 3. Szablon Estymacji, Wsteczna Migracja & Zbiorczy Rejestr `changes-summary.md`
- Ujednolicenie generatora `summary.md` w `.ai/tools/opsx-estimate.json` / `opsx-archive.json`.
- Przekształcenie sekcji `## ⏱️ Effort Estimation & Metrics` w `summary.md` w spójny format tabelaryczny z uwzględnieniem metryk sesyjnych:
  - Sub-agenci estymujący (czas w h oraz man-days MD),
  - Metryki sesji (Wall-clock, Input Tokens, Output Tokens).
- **Wsteczna aktualizacja**: Przebudowa plików `summary.md` w katalogach zarchiwizowanych zmian (`2026-07-26-explore-orchestrator-setup` oraz `2026-07-26-orchestrator-setup-repos`) do nowego standardu z wyliczonymi metrykami sesyjnymi.
- **Utworzenie zbiorczego pliku**: Utworzenie `openspec/changes/archive/changes-summary.md` zbierającego metryki dotychczasowych zmian:
  - Nazwa zmiany
  - Krótki opis zmiany
  - Podsumowanie sesji (wall clock, tokeny we/wy, estymowany czas h i MD)
- **Automatyczna aktualizacja po archiwizacji**: Zapewnienie, że podczas archiwizacji (procedury `opsx-archive`) plik `openspec/changes/archive/changes-summary.md` będzie automatycznie aktualizowany o nowy wpis.

---

## Non-Goals
- Zmiana samego CLI `openspec`.
- Tworzenie sztucznych przeliczników finansowych.
