---
name: opsx-archive
description: Zarchiwizuj obecną zmianę w OpenSpec (uruchamia też auto-estymację). Aktywuj ten skill, gdy użytkownik wpisze opsx-archive, /opsx-archive lub poprosi o zarchiwizowanie/zamknięcie zmiany.
---
# Instrukcja Skilla: /opsx-archive

Twoim zadaniem jest zamknięcie, wycena i zarchiwizowanie ukończonej zmiany w OpenSpec.

## 📦 Zasady Archiwizacji Zmiany

1. **Generowanie Dwutabelowego Podsumowania (`summary.md`)**:
   - W katalogu zmiany (`openspec/changes/<change-name>/summary.md`) utwórz plik podsumowania zawierający dwie tabele:
     - **Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI**:
       - Estymowany czas tradycyjny (h i Roboczodni / Man-Days).
       - Estymowany koszt tradycyjny (PLN / USD).
     - **Tabela 2: Rzeczywiste Metryki Sesji**:
       - Czas trwania sesji wall-clock (hh:mm:ss i h).
       - Tokeny WE (Input) i WY (Output).
       - Szacowany rzeczywisty koszt LLM API ($).
       - **Wyliczona Oszczędność Czasowa (h)** = `Estymowany Czas (h) - Czas Wall-clock (h)`.

2. **Przeniesienie do Archiwum (Archive Naming)**:
   - Utwórz unikalną nazwę folderu w formacie: **`YYYY-MM-DD-HHMM-<change-name>`** (np. `2026-07-27-2115-wyszukiwarka-nieruchomosci-data-arch`).
   - Przenieś całą zawartość zmiany z `openspec/changes/<change-name>` do `openspec/changes/archive/YYYY-MM-DD-HHMM-<change-name>`.

3. **Aktualizacja Rejestru Centralnego**:
   - Dpisz nową pozycję tabeli oraz zaktualizuj podsumowanie agregujące w centralnym pliku `openspec/changes/archive/changes-summary.md`.
