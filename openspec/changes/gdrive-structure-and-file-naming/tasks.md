# Plan prac (`tasks.md`)

Status: w realizacji — tryb półautomatyczny (decyzja z 2026-10-24). Porządkowanie Dysku odbywa się folder po folderze, z przeglądem przez konektor Google Drive i zatwierdzaniem każdej zmiany przez użytkownika; stan zapisuje `tracker.md`. Skryptowy `apply v2` i warunkowe cofanie są wycofane ze ścieżki krytycznej (planer `v2` zostaje jako narzędzie pomocnicze, tylko do odczytu).

## Faza 0 — Eksploracja, analiza architektury i konsolidacja artefaktów

- [x] Przeprowadzić wielowymiarowy audyt Google Drive i wygenerować dokumentację bazową (`00`–`05`) wraz ze zrzutem metadanych (`analysis/data/drive_analysis_data.json`, `analysis/data/drive_dataset_complete.json`, `analysis/drive_context_for_agents.md`) oraz prezentacją (`analysis/latex-slides/`).
- [x] Opracować docelową architekturę katalogów (`analysis/06-optymalna-struktura-i-procesy-zarzadzania.md`), mapę migracji (`analysis/07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md`), analizę uprawnień/emoji (`analysis/08-uprawnienia-automatyzacja-i-dylemat-emoji.md`), korekty mapowania (`analysis/09-review-katalogow-i-mapowania-gdrive.md`) oraz standard nazewnictwa plików (`analysis/10-konwencja-nazewnictwa-plikow.md`).
- [x] Przenieść i skonsolidować wszystkie artefakty oraz skrypty z `sandbox/2026-09-19-gdrive-analysis` bezpośrednio w katalogu zmiany `openspec/changes/gdrive-structure-and-file-naming/`.

## Etap A — Struktura katalogów (bez zmian nazw plików)

- [x] Wykonać wstępny odczyt inwentaryzacyjny (`dry-run v1`) i zdiagnozować ograniczenia rozpoznawania katalogu głównego (`reports/11-raport-dry-run-migracji-2026-10-13.md`).
- [x] Poprawić obsługę rzeczywistego ID roota i ograniczenie skanu do potwierdzonych potomków My Drive (bez podążania za skrótami i bez Shared Drives) w `scripts/gdrive_migration/migrate.py` oraz `scripts/gdrive_migration/planner.py`.
- [x] Uaktualnić inwentaryzację i mapowanie z uwzględnieniem dokumentu `07` (52 pliki) oraz review `09` (28 folderów głównych i 13 podfolderów folderu `25`), zapisując stan `before` w schemacie planu `v2` (`scripts/gdrive_migration/planner.py`) i blokując stare wywołanie `apply`.
- [x] Przygotować procedurę zatwierdzenia, weryfikacji i warunkowego odtworzenia w `scripts/gdrive_migration/SAFETY.md` oraz przetestować logikę planera (12 testów jednostkowych w `scripts/gdrive_migration/test_planner.py`, weryfikacja: `scripts/gdrive_migration/.venv/bin/python -m unittest -v test_planner`).
- [x] Wykonać poprawiony odczyt `dry-run v2` tylko do odczytu (`reports/12-poprawiony-dry-run-i-plan-bezpiecznej-migracji.md`, lokalny `scripts/gdrive_migration/dry_run_report.md` oraz `plan.json` v2: 42 383 pozycje w My Drive, 77 operacji, 36 pozycji `blocked` do decyzji).
- [x] **Zmiana trybu na półautomatyczny** (2026-10-24): zamiast zbiorczego `apply v2` — porządkowanie katalog po katalogu z zatwierdzaniem przez użytkownika (zasady: `design.md` §3–5, D6). Etap B (nazwy plików) wykonywany w tym samym przebiegu co porządkowanie danego folderu.
- [x] Foldery `01`–`05` uporządkowane (struktura, nazwy, uprawnienia `01`) — szczegóły w `tracker.md`.

## Etap C — Porządkowanie folderów w root (pętla per folder, `tracker.md`)

Dla każdego folderu z listy poniżej wykonać ten sam cykl:

1. Odczyt zawartości (konektor Drive), zestawienie względem `analysis/07`/`09` i `design.md` §3–4.
2. Propozycja: struktura podfolderów, przeniesienia, nowe nazwy folderów i plików (reguły `design.md` §4), pozycje do decyzji. Zmiany wykonuje się dopiero po akceptacji użytkownika; skróty tylko za zgodą (D3a).
3. Wykonanie zatwierdzonych zmian, weryfikacja po ID (rodzic, nazwa) i uprawnień tam, gdzie dotyczy.
4. Aktualizacja `tracker.md` (sekcja szczegółów folderu, decyzje, pozostałe pozycje).

- [x] `07 🏢 Praca i Projekty`
- [ ] `08 🌂 Ubezpieczenia` (najpierw decyzja: osobny folder czy rozproszenie wg 09)
- [ ] `10 🏠 Mieszkanie i Nieruchomości`
- [ ] `11 🏡 Lewickie i Pokój` (09: rozdzielić; Pokój do potwierdzenia)
- [ ] `12 🚗 Pojazdy`
- [ ] `20 📚 Wiedza i Rozwój`, `21 🎵 Audio i Multimedia`, `22 🏃 Sport i Aktywność`, `23 🎮 Gry i Hobby`, `24 🧳 Podróże i Wyjazdy`
- [ ] `80 📱 Aplikacje i Synchronizacja` (sprawdzić punkty zapisu Notability, Chrome, skanera paragonów przed zmianami)
- [ ] `90 📦 Archiwum`, `99 🚮 Do Usunięcia`; `95 💽 Google Takeout` poza zakresem (ręcznie)
- [ ] `00 📥 Inbox` oraz 5 plików luzem w root — przypisanie do folderów
- [ ] Pozostałości: opróżnić kosz po potwierdzeniu aktualności `hasla.kdbx`; ponownie sprawdzić `00 ‼️ Ważne dokumenty`; pozycje do decyzji z `04 🏫 Edukacja Dzieci`
- [ ] Przed zamknięciem zmiany: ręczny backup Takeout potwierdzony przez użytkownika (nie jest bramką dla pojedynczych, odwracalnych kroków; obowiązuje przed ewentualnymi operacjami masowymi)

## Zamknięcie

- [ ] **Uzupełnienie kanonicznej dokumentacji zasad**:
  - **Pliki**: `design.md`, `analysis/06-optymalna-struktura-i-procesy-zarzadzania.md`, `analysis/07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md`, `analysis/10-konwencja-nazewnictwa-plikow.md`.
  - **Kryteria akceptacji**: Dopisanie finalnych uściśleń z porządkowania wszystkich folderów z zachowaniem historii dokumentów `06`–`12`; `tracker.md` bez pozycji otwartych lub z jawnie odroczonymi.

## Wycofane z planu (decyzja z 2026-10-24)

Zachowane jako historia, nie do realizacji w tej zmianie (do wznowienia tylko przy potrzebie operacji masowych):

- ~~Bramka decyzyjna na 36 pozycji `blocked` i `plan.json` v2~~ — pozycje rozstrzygane na bieżąco per folder.
- ~~Wykonawca `apply v2`, dziennik `migration_log.json`, `verify`, warunkowe cofanie, test na koncie testowym~~.
- ~~Zbiorczy audyt nazw, generator raportu `stara → nowa`, moduł normalizatora nazw i testy jednostkowe normalizacji~~ — reguły z `design.md` §4 stosowane przy przeglądzie każdego folderu.
