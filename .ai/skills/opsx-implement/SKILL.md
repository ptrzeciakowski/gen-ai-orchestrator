---
name: opsx-implement
description: Uruchom implementację kolejnego zadania z pliku tasks.md w OpenSpec. Aktywuj ten skill, gdy użytkownik wpisze opsx-implement, /opsx-implement lub poprosi o realizację zadań OpenSpec.
---
# Instrukcja Skilla: /opsx-implement

Twoim zadaniem jest realizacja wdrożeniowa kolejnego nieodznaczonego zadania z pliku **`tasks.md`** aktywnej zmiany (`openspec/changes/<change-name>/tasks.md`).

## ⚡ Zasady Realizacji Wdrożenia

1. **Wybór Zadania**:
   - Otwórz i przeanalizuj plik `tasks.md`.
   - Znajdź pierwszy krok z pustym polem wyboru (`- [ ]`).

2. **Wdrożenie i Kodowanie**:
   - Przeczytaj odpowiednie sekcje w `design.md` oraz ew. materiały w `explore/` odnośnie wybranego zadania.
   - Wdróż wymagane zmiany w kodzie źródłowym repozytorium.
   - Zachowaj istniejące komentarze, docstringi i struktury niezwiązane ze zmianą.

3. **Weryfikacja i Testy (Empirical Verification)**:
   - **BEZWZGLĘDNY NAKAZ**: Przed zgłoszeniem zakończenia zadania musisz uruchomić komendę budującą, testową lub weryfikacyjną.
   - Nie ogłaszaj sukcesu bez empirycznego dowodu sprawnego działania kodu.
   - Przeanalizuj logi i ewentualne błędy.

4. **Aktualizacja Statusu**:
   - Po pomyślnej weryfikacji zaktualizuj plik `tasks.md`, zmieniając status zadania z `- [ ]` na `- [x]`.
   - Przedstaw krótka i zwięzłą informację dla użytkownika o wykonanych pracach i wskaż kolejne zadanie w kolejce.
