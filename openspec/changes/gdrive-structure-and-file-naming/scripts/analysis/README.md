# Skrypty analizy Dysku (jednorazowe, wrzesień 2026)

Odtwarzają dane użyte w `../../analysis/` (dokumenty 00–05, 09). Czytają **lokalną bazę metadanych DriveFS** (SQLite, tylko do odczytu) — nie używają Google Drive API ani OAuth.

| Skrypt | Wynik |
|---|---|
| `scan_drive.py` | `analysis/data/drive_analysis_data.json` |
| `export_brief.py` | `analysis/data/drive_dataset_complete.json`, `analysis/drive_context_for_agents.md` |

```bash
python3 scan_drive.py
python3 export_brief.py
```

Baza jest wykrywana automatycznie (`~/Library/Application Support/Google/DriveFS/*/metadata_sqlite_db`); przy kilku kontach lub innym położeniu ustaw `GDRIVE_DRIVEFS_DB`. Pliki w `analysis/data/` zawierają metadane prywatne i są ignorowane przez Git.

Dane są migawką z 2026-09-19 — ponowne uruchomienie nadpisze je aktualnym stanem Dysku.
