# Plan Wdrożeniowy (`tasks.md`): Agentowe Zarządzanie Wiedzą w Obsidianie

**Kod Zmiany**: `obsidian-agentic-pkm`  
**Status**: Gotowe do realizacji (zakończono fazę eksploracji i projektu architektonicznego)

---

## Faza 0: Eksploracja i Architektura OpenSpec

- [x] Przeprowadzić audyt istniejącego skarbca `/Users/pawel/Documents/Pawel-personal` (~75 notatek) oraz zainstalowanych wtyczek (`gemini-scribe` v4.11.0).
- [x] Opracować dokument eksploracyjny [`explore/001-obsidian-agentic-pkm-01.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/obsidian-agentic-pkm/explore/001-obsidian-agentic-pkm-01.md).
- [x] Przygotować specyfikację [`proposal.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/obsidian-agentic-pkm/proposal.md) oraz projekt techniczny [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/obsidian-agentic-pkm/design.md).

---

## Faza 1: Konfiguracja Struktury Skarbca i Szablonów (Wariant A)

- [ ] **Utworzenie szkieletu katalogów w skarbcu Obsidian**:
  - **Ścieżki**: `/Users/pawel/Documents/Pawel-personal/00_Inbox`, `/Users/pawel/Documents/Pawel-personal/10_Wiedza`, `/Users/pawel/Documents/Pawel-personal/20_Projekty`, `/Users/pawel/Documents/Pawel-personal/30_Dziennik`, `/Users/pawel/Documents/Pawel-personal/90_System/Szablony`.
  - **Kryteria akceptacji**: Katalogi istnieją w skarbcu bez naruszania dotychczasowych plików i folderów.
  - **Weryfikacja**: `ls -la /Users/pawel/Documents/Pawel-personal`.
- [ ] **Utworzenie szablonów bazowych z Frontmatter YAML**:
  - **Ścieżki**: `/Users/pawel/Documents/Pawel-personal/90_System/Szablony/Szablon-Notatka-Atomowa.md`, `/Users/pawel/Documents/Pawel-personal/90_System/Szablony/Szablon-Spotkanie.md`, `/Users/pawel/Documents/Pawel-personal/90_System/Szablony/Szablon-Projekt.md`.
  - **Kryteria akceptacji**: Poprawna składnia YAML Properties (wikilinki ujęte w cudzysłowy `"[[...]]"`, pola `typ`, `obszar`, `tagi`, `stworzono`, `ostatnia_modyfikacja`, `status`).

---

## Faza 2: Wdrożenie Promptów Agentowych w `gemini-scribe`

- [ ] **Implementacja promptu `AutoRefiner.md`**:
  - **Ścieżka**: `/Users/pawel/Documents/Pawel-personal/gemini-scribe/Prompts/AutoRefiner.md`.
  - **Kryteria akceptacji**: Prompt przyjmuje surową notatkę, dodaje ustrukturyzowany nagłówek YAML, porządkuje nagłówki Markdown i proponuje wikilinki bez usuwania faktów z oryginału.
- [ ] **Implementacja promptu `Meeting-To-ActionItems.md`**:
  - **Ścieżka**: `/Users/pawel/Documents/Pawel-personal/gemini-scribe/Prompts/Meeting-To-ActionItems.md`.
  - **Kryteria akceptacji**: Prompt ekstrahuje z notatek ze spotkań podsumowanie decyzji, listę zadań (`- [ ]`) wraz z właścicielem i terminem oraz nagłówek YAML `typ: spotkanie`.
- [ ] **Implementacja promptu `Synthesizer.md`**:
  - **Ścieżka**: `/Users/pawel/Documents/Pawel-personal/gemini-scribe/Prompts/Synthesizer.md`.
  - **Kryteria akceptacji**: Prompt generuje zwięzłą syntezę wiedzy i otwartych pytań na podstawie zestawu powiązanych notatek.

---

## Faza 3: Pilotaż na Żywych Notatkach (Wariant B)

- [ ] **Przetworzenie pilotażowe 2–3 wybranych notatek (np. notatka z zebrania i wpis z dziennika)**:
  - **Ścieżki**: wybrane pliki w `/Users/pawel/Documents/Pawel-personal/`.
  - **Kryteria akceptacji**: Poprawne wygenerowanie właściwości YAML w Obsidian Properties, działające linki `[[...]]` oraz zachowanie 100% oryginalnych informacji merytorycznych.

---

## Faza 4: Bezpieczne Wsadowe Uzupełnienie Metadanych YAML (Wariant C)

- [ ] **Kopia zapasowa skarbca przed operacją wsadową**:
  - **Kryteria akceptacji**: Utworzenie pełnego archiwum kopii zapasowej `/Users/pawel/Documents/Pawel-personal` przed modyfikacją plików przez skrypt.
- [ ] **Skrypt audytu i migracji Frontmatter YAML z trybem `--dry-run`**:
  - **Ścieżka**: `openspec/changes/obsidian-agentic-pkm/scripts/vault_yaml_enricher.py`.
  - **Kryteria akceptacji**: Skrypt skanuje ~75 notatek, wykrywa brakujący lub niepełny Frontmatter YAML, generuje raport propozycji zmian w trybie `--dry-run` (bez zapisu na dysku) i zapisuje nagłówki dopiero po zatwierdzeniu (`--apply`), nie zmieniając treści poniżej bloku `---`.
  - **Weryfikacja**: `python3 openspec/changes/obsidian-agentic-pkm/scripts/vault_yaml_enricher.py --dry-run`.
