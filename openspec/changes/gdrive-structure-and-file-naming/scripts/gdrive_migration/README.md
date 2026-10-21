# Migracja Google Drive — etap strukturalny

**Stan:** narzędzie do **planowania w trybie tylko do odczytu** (plan `schema_version: 2`). Wykonawca `apply` jest celowo zablokowany — `--approve APPLY` go nie odblokowuje. Wymagania dla przyszłego wykonawcy: [SAFETY.md](SAFETY.md). Plan prac: [tasks.md](../../tasks.md).

## Co robi

- `plan` — OAuth `drive.metadata.readonly`; pobiera rzeczywisty ID roota i ogranicza inwentaryzację do jego potwierdzonych potomków (bez skrótów i Shared Drives). Zapisuje `inventory.json`, `plan.json` i czytelny `dry_run_report.md`.
- `verify` — odczyt inwentaryzacyjny roota do `verification.json`. To **nie** weryfikacja wykonania operacji.
- `apply` — odmawia wykonania.

`planner.py` buduje plan z mapy [07](../../analysis/07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md) (pliki) i review [09](../../analysis/09-review-katalogow-i-mapowania-gdrive.md) (foldery), wykrywa kolizje i duplikaty, a niepewne pozycje (dokumenty tożsamości, karta szkolna, firmy, osoby, nieruchomości) oznacza jako `blocked` zamiast zgadywać. Wyniki ostatniego przebiegu: [raport 12](../../reports/12-poprawiony-dry-run-i-plan-bezpiecznej-migracji.md).

Narzędzie nie audytuje uprawnień, nie szyfruje, nie scala poddrzew, nie usuwa i nie zmienia nazw plików.

## Przygotowanie

```bash
cd openspec/changes/gdrive-structure-and-file-naming/scripts/gdrive_migration
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

Dane OAuth leżą **poza repozytorium**, w `~/.config/gdrive-migration/` (zmienna `GDRIVE_MIGRATION_CONFIG` zmienia katalog):

- `credentials.json` — OAuth Desktop Client z Google Cloud (Drive API włączone),
- `token.json` — tworzony przy pierwszym logowaniu.

Pliki robocze (`inventory.json`, `plan.json`, `dry_run_report.md`, `verification.json`) powstają obok `migrate.py` i są ignorowane przez Git.

## Uruchomienie i testy

```bash
.venv/bin/python -m unittest -v test_planner
.venv/bin/python migrate.py plan
.venv/bin/python migrate.py verify
```
