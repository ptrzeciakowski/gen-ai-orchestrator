---
name: opsx-explore
description: Rozpocznij proces eksploracji OpenSpec dla nowego pomysłu. Aktywuj ten skill, gdy użytkownik wpisze opsx-explore, /opsx-explore, eksploracja openspec lub poprosi o analize nowego pomyslu.
---
# Instrukcja Skilla: /opsx-explore

Twoim zadaniem jako Agenta jest przeprowadzanie wstępnej analizy architektonicznej i eksploracyjnej dla nowego pomysłu lub zmiany w standardzie **OpenSpec**.

## Zasady Wykonania Eksploracji

1. **Lokalizacja i Nazewnictwo Artefaktów Eksploracji**:
   - Wszystkie analizy eksploracyjne i towarzyszące im materiały **MUSZĄ** lądować w podfolderze `explore/` wewnątrz katalogu danej zmiany (`openspec/changes/<change-name>/explore/`).
   - Nazwy plików muszą przestrzegać konwencji: **`NNN-nazwa-zmiany-MM.<ext>`**
     - `NNN` – 3-cyfrowy numer eksploracji w ramach zmiany (np. `001`, `002`).
     - `nazwa-zmiany` – unikalna nazwa zmiany (`change-name`).
     - `MM` – 2-cyfrowy numer wersji dokumentu/pliku w ramach danej eksploracji (np. `01`, `02`).
     - `<ext>` – plik główny **musi być w formacie `.md`**, a opcjonalne towarzyszące skrypty mogą posiadać rozszerzenia `.sql`, `.json`, `.py`, `.sh` itp.
   - *Przykład*: `openspec/changes/wyszukiwarka-nieruchomosci-data-arch/explore/001-wyszukiwarka-nieruchomosci-data-arch-01.md`.

2. **Bezwzględne Przestrzeganie Zasad Brutalnej Szczerości**:
   - Przed przystąpieniem do analizy załaduj i bezwzględnie stosuj wytyczne z pliku `.ai/guidelines/brutally-honest-rules.md`.
   - **Nazywaj niepewności wprost**: Jeżeli nie posiadasz pełnych danych lub empirycznych pomiarów, napisz to otwarcie zamiast udawać pewność.
   - **Oznaczaj domysły**: Wszelkie niepewne przypuszczenia i założenia oznaczaj etykietą **`[Hipoteza/Domysł]`**.
   - **Zakaz zmyślania metryk i źródeł**: Nigdy nie twórz fikcyjnych statystyk, raportów ani nieaktywnych adresów URL.
   - **Prezentuj alternatywy architektoniczne**: Wskazuj potencjalne ścieżki i ich trade-offy.

3. **Akumulacyjne Wzbogacanie (Non-Destructive Enrichment)**:
   - Nie usuwaj ani nie skracaj wcześniej wypracowanych wartościowych sekcji. Dopisuj nowe uściślenia i poprawki w sposób audytowalny.
