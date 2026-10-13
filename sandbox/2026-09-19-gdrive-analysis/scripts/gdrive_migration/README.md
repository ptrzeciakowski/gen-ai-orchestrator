# Migracja Google Drive — etap strukturalny

## Aktualizacja 2026-10-13: bezpieczne planowanie v2

**Poniższa sekcja zastępuje instrukcje wykonania ze starej wersji opisanej dalej.**

- `plan` korzysta domyślnie z OAuth `drive.metadata.readonly`, pobiera rzeczywisty ID roota i ogranicza inwentaryzację do jego potwierdzonych potomków. Nie podąża za skrótami ani nie włącza Shared Drives.
- Nowy moduł `planner.py` rozpoznaje konflikty, uwzględnia planowane zmiany nazw przed tworzeniem celów i nie tworzy z góry całego pustego drzewa.
- Mapa obejmuje 52 pliki z dokumentu 07 (dokładne dopasowanie nazw, również bez pseudo-rozszerzeń dokumentów Google) oraz 28 folderów i 13 podfolderów folderu 25 z review 09. Warunkowe mapowania folderów są propozycjami do przeglądu, nie automatycznymi operacjami.
- Niepewne pliki trafiają w planie do przeglądu zamiast do usunięcia. Dokumenty tożsamości i karta szkolna wymagają decyzji. Firmy, osoby i nieruchomości nie są zgadywane.
- `plan.json` ma **schema_version 2**; nie jest zgodny ze starym wykonawcą. Zarówno CLI `apply`, jak i bezpośrednie wywołanie starego wykonawcy są zablokowane. `--approve APPLY` nie omija blokady.
- `verify` pozostaje odczytem inwentaryzacyjnym, nie weryfikacją wykonania operacji.

Uruchomienie i testy:

```bash
.venv/bin/python -m unittest -v test_planner
.venv/bin/python migrate.py plan
```

Plan zapisuje `inventory.json`, `plan.json` oraz **`dry_run_report.md`** (czytelne podsumowanie operacji, konfliktów i propozycji mapowania). Raporty i OAuth są lokalne, ignorowane przez Git. Poprzednie wyniki zabezpieczono w `reports/2026-10-13-original/`.

Zobacz [procedurę zatwierdzenia, weryfikacji i odtworzenia](SAFETY.md). Wersja v2 jest narzędziem do planowania, **nie gotowym narzędziem do wykonania całej migracji**. Nie wykonuje audytu uprawnień, szyfrowania, scalenia poddrzew, usuwania ani konfiguracji aplikacji. Do tych etapów potrzebne są decyzje użytkownika i osobno przetestowany wykonawca.

## Historyczny opis wersji roboczej (przed aktualizacją)

**Status: wersja robocza z przekazanego archiwum `gdrive_migration.zip`, niegotowa do migracji produkcyjnej.** Kod `migrate.py` i zależności zachowano bez zmian. Sprawdzono integralność archiwum i składnię Pythona; nie przeprowadzono testów na koncie Google Drive.

Skrypt nie usuwa plików, nie opróżnia kosza, nie szyfruje danych i nie pobiera Takeout. Udostępnia polecenia `plan`, `apply` i `verify`; polecenie jest obowiązkowe. Zmiany wrażliwe i niejednoznaczne wymagają ręcznej decyzji.

## Kontekst

Mapa bazowa: [07 — mapa migracji](../../07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md).
Przed dopracowaniem mapowania uwzględnij [09 — review katalogów i mapowania](../../09-review-katalogow-i-mapowania-gdrive.md).
Obecny kod obejmuje 13 mapowań nazw folderów głównych i 18 nazw plików; nie realizuje kompletnej migracji 28 folderów i 52 plików ani wszystkich korekt z review 09.

## Znane ograniczenia przed użyciem apply

- `root_map()` oraz kontrole rodziców w `apply()` porównują `parents` z literalnym `root`. Trzeba pobrać rzeczywisty identyfikator katalogu głównego i używać go do porównań. `root` jest aliasem przy przekazywaniu ID do API, a pole `parents` zawiera identyfikatory folderów ([dokumentacja Google](https://developers.google.com/workspace/drive/api/guides/folder)).
- W konsekwencji plan i raport verify mogą nie wykazać istniejących elementów roota, a apply może utworzyć równoległe foldery docelowe, pomijając planowane zmiany nazw i przeniesienia. Nie traktuj pustego raportu jako potwierdzenia zakończonej migracji.
- Planowanie nie rozwiązuje wszystkich konfliktów istniejących folderów. `blocked` jest raportem; obecność pozycji blocked nie zatrzymuje pozostałych operacji apply.
- `verify` zapisuje inwentaryzację roota, ale nie porównuje wykonania każdej operacji z planem. Nie stanowi pełnej weryfikacji migracji.
- `scan()` nie filtruje wszystkich wyników do drzewa My Drive; deklarowany zakres wymaga dopracowania. Skróty nie są obsługiwane jako foldery.
- Mapowanie złożonych poddrzew i korekty z review 09 pozostają do opracowania. Nie ma mechanizmu rollback.

**Nie uruchamiaj apply na produkcyjnym Dysku przed usunięciem tych ograniczeń i testem na osobnym zestawie danych.**

## Przygotowanie i planowanie

```bash
cd sandbox/2026-09-19-gdrive-analysis/scripts/gdrive_migration
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

W Google Cloud włącz Drive API i pobierz OAuth Desktop Client jako `credentials.json` do tego katalogu.
Skrypt otworzy logowanie OAuth i zapisze `token.json`. Wszystkie pliki robocze zapisuje obok `migrate.py`, niezależnie od bieżącego katalogu.

```bash
.venv/bin/python migrate.py plan
```

Polecenie zapisuje `plan.json` i `inventory.json` bez zmiany struktury Dysku. Przejrzyj operacje oraz `blocked`; wynik podlega ograniczeniom opisanym powyżej.

## Polecenia po dopracowaniu i testach

```bash
# Wykorzystuje istniejący plan.json; zmienia Dysk.
.venv/bin/python migrate.py apply --approve APPLY

# Zapisuje verification.json; obecnie jest to raport inwentaryzacyjny.
.venv/bin/python migrate.py verify
```

Dziennik operacji trafia do `migration_log.json`. Błędy poszczególnych operacji są zapisywane, a skrypt kontynuuje pozostałe operacje.

Operacje nie obejmują masowej zmiany nazw plików. Katalog Takeout pozostaje nietknięty.
Pliki OAuth, raporty, środowisko wirtualne i cache są wykluczone przez lokalny `.gitignore`.
