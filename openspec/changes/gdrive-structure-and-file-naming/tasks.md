# Plan prac (`tasks.md`)

Status: w realizacji (Etap A: zakończono fazę analizy `00`–`10`, konsolidację artefaktów w katalogu zmiany oraz bezpieczne planowanie `dry-run v2` w trybie read-only; wykonanie zapisu `apply` pozostaje zablokowane do czasu decyzji użytkownika).

## Faza 0 — Eksploracja, analiza architektury i konsolidacja artefaktów

- [x] Przeprowadzić wielowymiarowy audyt Google Drive i wygenerować dokumentację bazową (`00`–`05`) wraz ze zrzutem metadanych (`drive_analysis_data.json`, `drive_dataset_complete.json`, `drive_context_for_agents.md`) oraz prezentacją (`latex-slides/`).
- [x] Opracować docelową architekturę katalogów (`06-optymalna-struktura-i-procesy-zarzadzania.md`), mapę migracji (`07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md`), analizę uprawnień/emoji (`08-uprawnienia-automatyzacja-i-dylemat-emoji.md`), korekty mapowania (`09-review-katalogow-i-mapowania-gdrive.md`) oraz standard nazewnictwa plików (`10-konwencja-nazewnictwa-plikow.md`).
- [x] Przenieść i skonsolidować wszystkie artefakty oraz skrypty z `sandbox/2026-09-19-gdrive-analysis` bezpośrednio w katalogu zmiany `openspec/changes/gdrive-structure-and-file-naming/`.

## Etap A — Struktura katalogów (bez zmian nazw plików)

- [x] Wykonać wstępny odczyt inwentaryzacyjny (`dry-run v1`) i zdiagnozować ograniczenia rozpoznawania katalogu głównego (`11-raport-dry-run-migracji-2026-10-13.md`).
- [x] Poprawić obsługę rzeczywistego ID roota i ograniczenie skanu do potwierdzonych potomków My Drive (bez podążania za skrótami i bez Shared Drives) w `scripts/gdrive_migration/migrate.py` oraz `scripts/gdrive_migration/planner.py`.
- [x] Uaktualnić inwentaryzację i mapowanie z uwzględnieniem dokumentu `07` (52 pliki) oraz review `09` (28 folderów głównych i 13 podfolderów folderu `25`), zapisując stan `before` w schemacie planu `v2` (`scripts/gdrive_migration/planner.py`) i blokując stare wywołanie `apply`.
- [x] Przygotować procedurę zatwierdzenia, weryfikacji i warunkowego odtworzenia w `scripts/gdrive_migration/SAFETY.md` oraz przetestować logikę planera (12 testów jednostkowych w `scripts/gdrive_migration/test_planner.py`, weryfikacja: `scripts/gdrive_migration/.venv/bin/python -m unittest -v test_planner`).
- [x] Wykonać poprawiony odczyt `dry-run v2` tylko do odczytu (`12-poprawiony-dry-run-i-plan-bezpiecznej-migracji.md`, lokalny `scripts/gdrive_migration/dry_run_report.md` oraz `plan.json` v2: 42 383 pozycje w My Drive, 77 operacji, 36 pozycji `blocked` do decyzji).
- [ ] **Bramka decyzyjna i ręczny backup**:
  - **Pliki**: `scripts/gdrive_migration/dry_run_report.md`, `scripts/gdrive_migration/plan.json`, `scripts/gdrive_migration/SAFETY.md`.
  - **Kryteria akceptacji**: Rozstrzygnięcie 36 pozycji `blocked` / warunkowych z raportu `12` (m.in. przypisanie karty szkolnej, energii, firm/projektów, poddrzew medycznych, dokumentów tożsamości i podfolderów folderu `25`), potwierdzenie punktów zapisu aplikacji (Notability, Chrome, skaner paragonów) oraz potwierdzenie ręcznego backupu Takeout.
- [ ] **Implementacja i testy wykonawcy `apply v2` oraz warunkowego cofania**:
  - **Pliki**: `scripts/gdrive_migration/migrate.py`, `scripts/gdrive_migration/planner.py`, `scripts/gdrive_migration/test_planner.py`.
  - **Kryteria akceptacji**: Obsługa wyłącznie zatwierdzonego schematu `plan.json` v2 ze sprawdzeniem skrótu kryptograficznego planu, trwały zapis dziennika `migration_log.json` przed i po każdej operacji, zatrzymanie partii przy rozbieżności stanu `before` lub kolizji, pełna weryfikacja `verify` po ID każdej operacji oraz testy wznowienia, błędów częściowych i warunkowego cofania na osobnym zestawie testowym Drive.
  - **Weryfikacja**: `scripts/gdrive_migration/.venv/bin/python -m unittest -v` oraz test na koncie testowym przed odblokowaniem produkcyjnego `apply`.
- [ ] **Wykonanie zatwierdzonych operacji Etapu A i weryfikacja końcowa**:
  - **Pliki**: `scripts/gdrive_migration/migrate.py`, `scripts/gdrive_migration/migration_log.json`, `scripts/gdrive_migration/verification.json`.
  - **Kryteria akceptacji**: Wykonanie wyłącznie zatwierdzonych partii operacji przy zachowaniu oryginalnych nazw plików, 100% zgodności ID i rodziców w `verify` oraz działające zapisy z podpiętych aplikacji.
  - **Weryfikacja**: `scripts/gdrive_migration/.venv/bin/python migrate.py verify`.

## Etap B — Standaryzacja nazw plików (po zakończeniu i weryfikacji Etapu A)

- [ ] **Zebranie pełnego wykazu nazw plików w podfolderach**:
  - **Pliki**: `scripts/gdrive_migration/migrate.py`, `10-konwencja-nazewnictwa-plikow.md`.
  - **Kryteria akceptacji**: Rekurencyjny odczyt nazw w podfolderach objętych zakresem po migracji struktury, statystyka wzorców i identyfikacja zasobów aplikacyjnych wymagających wykluczenia.
- [ ] **Doprecyzowanie deterministycznego modułu normalizacji nazw**:
  - **Pliki**: `10-konwencja-nazewnictwa-plikow.md`, nowy moduł normalizatora w `scripts/gdrive_migration/`.
  - **Kryteria akceptacji**: Reguły formatu `YYYY-MM-DD-Temat-Opis.ext` (oraz wariantów `YYYY-MM`, `YYYY`, bez daty), transliteracja polskich znaków, brak sztucznych rozszerzeń dla natywnych dokumentów Google, blokada przy niejednoznacznej dacie lub kolizji nazw w tym samym folderze.
- [ ] **Wygenerowanie raportu propozycji zmian nazw (`stara nazwa → nowa nazwa`)**:
  - **Pliki**: lokalny raport JSON/Markdown w `scripts/gdrive_migration/`.
  - **Kryteria akceptacji**: Każda pozycja zawiera `ID`, `stara nazwa`, `nowa nazwa`, `reguła`, `źródło daty`, `konflikt` oraz pole decyzji (`zatwierdzone` / `odrzucone` / `blocked`).
- [ ] **Testy jednostkowe normalizacji i cofania zmian nazw**:
  - **Pliki**: testy jednostkowe w `scripts/gdrive_migration/`.
  - **Kryteria akceptacji**: Pokrycie testami transliteracji, dat częściowych, natywnych dokumentów Google, rozszerzeń wieloczłonowych, kolizji po transliteracji, idempotencji i warunkowego cofania z dziennika przed/po.
  - **Weryfikacja**: `scripts/gdrive_migration/.venv/bin/python -m unittest -v`.
- [ ] **Zatwierdzenie pozycji raportu, wykonanie zmian nazw i weryfikacja**:
  - **Pliki**: `scripts/gdrive_migration/migrate.py`, dziennik operacji i raport weryfikacji.
  - **Kryteria akceptacji**: Zmiana wyłącznie pozycji jawnie zatwierdzonych przez użytkownika z kontrolą niezmienionego stanu `before`, weryfikacja każdej operacji po ID i zapis wyjątków.
- [ ] **Uzupełnienie kanonicznej dokumentacji zasad**:
  - **Pliki**: `06-optymalna-struktura-i-procesy-zarzadzania.md`, `07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md`, `10-konwencja-nazewnictwa-plikow.md`.
  - **Kryteria akceptacji**: Dopisanie finalnych uściśleń po wdrożeniu Etapu A i B z zachowaniem pełnej historii dokumentów `06`–`12`.
