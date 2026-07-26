# Exploratory Record: Constructive Criticism, README Map & Metric Estimation

**ID**: `001-orch-constructive-criticizm-001`  
**Date**: 2026-07-26  
**Topic**: Trzyfilarowe rozszerzenie orkiestratora: (1) Zasady 12 Rules Brutalnej Szczerości, (2) Opis struktury katalogów w README.md, (3) Jednolity szablon estymacji w summary.md z metrykami sesji, wsteczną migracją archiwalnych zmian oraz zbiorczym rejestrem archive/changes-summary.md.

---

## 1. Zakres Eksploracji

Eksploracja obejmuje trzy spójne usprawnienia orkiestratora Gen AI (`gen-ai-orchestrator`):

1. **Bezwzględna Uczciwość Architektoniczna (12 Rules)**:
   Inkorporacja 12 Zasad z *How to Make Claude Brutally Honest (12 Rules)* do procesu tworzenia eksploracji, wytycznych proposali oraz oceniania i komentowania designu architektonicznego.

2. **Dokumentacja Struktury Repozytorium w `README.md`**:
   Stworzenie szczegółowego mapowania struktury drzewa katalogów (drzewo plików i katalogów z jasnym opisem przeznaczenia każdego podkatalogu `.ai/`, `.agents/`, `openspec/`, `specs/` itp.) oraz weryfikacja czy w `README.md` nie brakuje kluczowych informacji operacyjnych.

3. **Jednolity Szablon Estymacji (`summary.md`), Wsteczna Migracja & Rejestr `archive/changes-summary.md`**:
   - Standaryzacja pliku `summary.md` generowanego przez skille/narzędzia estymacyjne wg szablonu z `archive/2026-07-26-orchestrator-setup-repos/summary.md`.
   - Przekształcenie sekcji `## ⏱️ Effort Estimation & Metrics` w spójny układ **tabelaryczny**.
   - Wprowadzenie do metryk danych sesyjnych: **Wall-clock** (czas trwania), **Ilość tokenów WE/WY (Input/Output Tokens)** oraz **Szacowany Koszt** (uśredniona wartość wyliczona przez sub-agentów estymujących).
   - **Wsteczna aktualizacja**: Przebudowa istniejących plików `summary.md` dla zarchiwizowanych zmian (`2026-07-26-explore-orchestrator-setup` oraz `2026-07-26-orchestrator-setup-repos`) do nowego standardu.
   - **Zbiorczy plik podsumowania**: Utworzenie początkowego `openspec/changes/archive/changes-summary.md` zbierającego metryki wszystkich zarchiwizowanych zmian oraz automatyczne dopisywanie/aktualizowanie go podczas archiwizacji (w procesie `opsx-archive`).

---

## 2. Krytyczna Analiza Obecnego Stanu (Zgodnie z Zasadami Brutalnej Szczerości)

### 🔴 Luki w Bezwzględnej Uczciwości (12 Rules):
- Brak twardego zakazu fabrykowania statystyk i źródeł przy recenzowaniu architektury.
- Skłonność agentów do cichego uzupełniania luk kontekstowych własnymi domysłami zamiast wytykania brakujących wymagań.

### 🔴 Luki w Dokumentacji (`README.md`):
- Brak wizualnej struktury katalogów w `README.md` utrudnia orientację agentom i deweloperom.
- Brak opisów powiązań pomiędzy podkatalogami `.ai/` (źródłowe instrukcje) a `.agents/` (symlinki dla formatu AGY).

### 🔴 Luki w Estymacji, Metrykach Sesyjnych i Archiwizacji:
- Dotychczasowy format estymacji w `summary.md` różnił się w zarchiwizowanych zmianach i brakowało w nim jednoznacznych tabel ze wskaźnikami zużycia tokenów oraz czasu wall-clock.
- Brak zbiorczego rejestru `openspec/changes/archive/changes-summary.md` utrudniał wgląd w zagregowany koszt i czas trwania wszystkich dotychczasowych prac.

---

## 3. Podsumowanie Decyzyjne Eksploracji

Zgadzamy się na pełne objęcie powyższego zakresu i przechodzimy do aktualizacji dokumentu **Proposal** (`proposal.md`).
