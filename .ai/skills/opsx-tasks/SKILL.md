---
name: opsx-tasks
description: Rozbij design na listę zadań (tasks.md) w OpenSpec. Aktywuj ten skill, gdy użytkownik wpisze opsx-tasks, /opsx-tasks lub poprosi o plan wdrożeniowy / dekompozycję zadań.
---
# Instrukcja Skilla: /opsx-tasks

Twoim zadaniem jest utworzenie lub zaktualizowanie pliku planu dekompozycji wdrożeniowej **`tasks.md`** w katalogu aktywnej zmiany (`openspec/changes/<change-name>/tasks.md`).

## 📋 Zasady Dekompozycji Wdrożeniowej

1. **Źródła Analizy**:
   - Przeanalizuj ustalenia z plików `design.md`, `proposal.md` oraz analizy w podfolderze `explore/`.
   - Zidentyfikuj konkretne komponenty, klasy, moduły i pliki wymagające utworzenia lub modyfikacji.

2. **Format i Struktura Pliku `tasks.md`**:
   - Używaj standardowych pól wyboru Markdown (`- [ ]` dla zadań do zrobienia, `- [x]` dla wykonanych).
   - Podziel proces na logiczne, chronologiczne fazy (np. *Faza 1: Przygotowanie Bazy Danych*, *Faza 2: Skrypty Ekstrakcji*, *Faza 3: Testy i Weryfikacja*).
   - Każde zadanie powinno być **atomowe, testowalne i precyzyjnie opisane**:
     - Podaj dokładne ścieżki do plików, które będą tworzone lub modyfikowane.
     - Określ jasne kryteria akceptacji (Acceptance Criteria).
     - Wskaż komendę weryfikującą (np. uruchomienie testu jednostkowego lub skryptu).

3. **Akumulacyjne Wzbogacanie**:
   - W przypadku dopisywania nowych zadań po testach lub przeglądzie kodu, dodawaj je do istniejących sekcji bez usuwania ukończonych historycznych kroków (`- [x]`).
