# OpenSpec Proposal: Agentowe Zarządzanie Wiedzą w Obsidianie (Personal OS)

**Kod Zmiany**: `obsidian-agentic-pkm`  
**Data**: 18 Października 2026 (Eksploracja: 10 Października 2026)  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`explore/001-obsidian-agentic-pkm-01.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/obsidian-agentic-pkm/explore/001-obsidian-agentic-pkm-01.md)
- Skarbiec docelowy: [`/Users/pawel/Documents/Pawel-personal`](file:///Users/pawel/Documents/Pawel-personal)
- Wtyczka agentowa: [`gemini-scribe`](file:///Users/pawel/Documents/Pawel-personal/.obsidian/plugins/gemini-scribe)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Obecny skarbiec Obsidian (`/Users/pawel/Documents/Pawel-personal`, ok. 75 notatek obejmujących dziennik, eksporty z Notability, notatki ze spotkań dot. Allegro, Roche, Dzieci, Zdrowia) posiada już zainstalowaną wtyczkę `gemini-scribe` (v4.11.0) oraz skonfigurowany klucz `GOOGLE_API_KEY`, jednak:
1. Notatki są luźnymi plikami tekstowymi pozbawionymi ustandaryzowanego **Frontmatter (YAML Properties)**, co utrudnia agentom AI deterministyczne filtrowanie, kategoryzację i budowanie grafu powiązań.
2. Brakuje dedykowanego bufora wejściowego (`00_Inbox/`) oddzielającego surowe zrzuty myśli i transkrypcje od przetworzonej wiedzy atomowej (`10_Wiedza/`) i projektowej (`20_Projekty/`).
3. W katalogu `gemini-scribe/Prompts/` nie wdrożono jeszcze gotowych promptów agentowych automatyzujących czyszczenie notatek (`AutoRefiner`), ekstrakcję zadań ze spotkań (`Meeting-To-ActionItems`) oraz syntezę między-notatkową (`Synthesizer`).

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Płaska, hybrydowa architektura katalogów w skarbcu**:
   - `00_Inbox/` – szybki zrzut surowych notatek, głosówek i eksportów do przetworzenia przez AI,
   - `10_Wiedza/` – ustrukturyzowane notatki atomowe (Zettelkasten),
   - `20_Projekty/` – aktywne projekty i obszary (np. *Allegro*, *Roche*, *Dom*),
   - `30_Dziennik/` – notatki chronologiczne (dotychczasowy `dziennik/`),
   - `90_System/Szablony/` – szablony notatek z predefiniowanym nagłówkiem YAML.
2. **Standard Frontmatter (YAML Properties)**:
   - Ujednolicone pola: `typ` (`inbox`, `pojęcie`, `projekt`, `spotkanie`, `dziennik`), `obszar`, `tagi`, `stworzono`, `ostatnia_modyfikacja`, `status`.
3. **Zestaw Promptów Agentowych (`gemini-scribe/Prompts/`)**:
   - `AutoRefiner.md` – transformacja surowego wpisu z Inboxu w notatkę z YAML Properties i linkami `[[Pojęć]]`,
   - `Meeting-To-ActionItems.md` – ekstrakcja decyzji i zadań z notatek ze spotkań,
   - `Synthesizer.md` – synteza tematyczna na bazie wskazanego obszaru/tagów.
4. **Narzędzie CLI do bezpiecznej migracji wsadowej (Dry-Run + Backup)**:
   - Skrypt Python analizujący istniejące ~75 notatek, proponujący uzupełnienie brakującego Frontmatter YAML bez modyfikacji treści merytorycznej notatek (z pełnym podglądem `dry-run` przed zapisem).

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Struktura katalogów i szablony**: Utworzenie katalogów `00_Inbox/`, `10_Wiedza/`, `20_Projekty/`, `30_Dziennik/`, `90_System/Szablony/` oraz szablonów bazowych w skarbcu.
- [ ] **Prompty `gemini-scribe`**: Wdrożenie `AutoRefiner.md`, `Meeting-To-ActionItems.md` i `Synthesizer.md`.
- [ ] **Pilotaż na wybranych notatkach**: Przetestowanie przepływu `00_Inbox -> AutoRefiner -> 10_Wiedza / 20_Projekty` na 2–3 reprezentatywnych notatkach.
- [ ] **Wsadowe uzupełnienie YAML Frontmatter**: Skrypt audytująco-migrujący dla dotychczasowych notatek z trybem `--dry-run`.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🧠 **Spójny kontekst dla agentów AI**: 100% notatek wyposażonych w metadane YAML umożliwiające precyzyjne zapytania RAG i Dataview.
* ⚡ **Redukcja ręcznego formatowania**: Automatyczne przekształcanie surowych notatek ze spotkań i zrzutów myśli w ustrukturyzowaną wiedzę i listy zadań.
