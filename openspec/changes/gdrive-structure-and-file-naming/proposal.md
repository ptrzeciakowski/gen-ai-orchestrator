# Propozycja zmiany: migracja struktury Google Drive i konwencja nazw plików

**Kod:** `gdrive-structure-and-file-naming`  
**Data:** 2026-10-12 (aktualizacja konsolidacyjna: 2026-10-18)  
**Status:** w realizacji (Etap A: zakończone bezpieczne planowanie `dry-run v2` tylko do odczytu; wykonanie `apply` na Google Drive pozostaje zablokowane do czasu ręcznego zatwierdzenia pozycji `blocked` i testu wykonawcy).

## Why

Dokument 06 wymaga nazw folderów bez spacji, ale podaje wzorce nazw plików ze spacjami. Mapa 07 łączy przenoszenie zasobów z proponowanymi zmianami nazw i datami częściowo wynikającymi z kontekstu. Review 09 wskazuje korekty mapowania, a zaimportowany skrypt migracyjny w wersji pierwotnej posiadał ograniczenia uniemożliwiające bezpieczne wykonanie (co potwierdził pierwszy raport dry-run 11).

Potrzebne są dwa niezależnie planowane i weryfikowane etapy: najpierw migracja katalogów bez zmian nazw plików (Etap A, dla którego wdrożono już nowy planer `v2` i wykonano poprawiony dry-run 12), a następnie audyt i standaryzacja nazw plików (Etap B). Wszystkie artefakty analityczne (`00`–`12`), dane inwentaryzacyjne, prezentacja Beamer (`analysis/latex-slides/`) oraz skrypty (`scripts/`) zostały skonsolidowane bezpośrednio w katalogu tej zmiany.

## What Changes

- Etap A: dopracować migrację katalogów i przenoszenie plików według 07 oraz korekt 09, zachowując nazwy plików.
  - Wdrożono moduł `planner.py` (schemat planu `v2`), obsługę rzeczywistego ID roota, zawężenie skanu do potwierdzonych potomków My Drive, procedurę bezpieczeństwa `SAFETY.md` oraz 12 testów jednostkowych (`test_planner.py`).
  - Wykonano poprawiony odczyt `dry-run v2` ([12 — poprawiony dry-run](./reports/12-poprawiony-dry-run-i-plan-bezpiecznej-migracji.md)): 42 383 potwierdzone pozycje w My Drive, 77 zaplanowanych operacji (11 zmian nazw folderów, 22 utworzenia brakujących folderów, 44 przeniesienia plików) oraz 36 pozycji `blocked` wymagających decyzji użytkownika przed odblokowaniem zapisu.
- Etap B: po weryfikacji A zinwentaryzować nazwy w podfolderach i wygenerować raport stara nazwa → nowa nazwa. Zmieniać wyłącznie zatwierdzone pozycje.
- Przyjąć proponowany format `YYYY-MM-DD-Temat-Opis.ext`, z wariantami miesiąca, roku lub bez daty; pojedyncze myślniki, transliteracja polskich znaków i rzeczywiste rozszerzenia. Nie dopisywać sztucznych rozszerzeń dokumentom Google.
- Blokować niejednoznaczne daty, opisy, kolizje i zmieniony stan źródła. Zachować ID oraz dziennik przed/po do weryfikacji i warunkowego cofania.
- Backup przygotować ręcznie przez Takeout, z potwierdzeniem zakresu i ograniczeń eksportu. Nie dodawać skryptu backupowego.
- Szczegółowy standard, przykłady, wyjątki i plan: [10 — konwencja nazw plików](./analysis/10-konwencja-nazewnictwa-plikow.md).

## Capabilities

### New Capabilities

- `gdrive-structural-migration`: planowanie (`planner.py`, schemat `v2`), zatwierdzanie (`SAFETY.md`), wykonanie, weryfikacja i warunkowe cofanie zmian struktury.
- `gdrive-file-name-normalization`: audyt nazw, deterministyczne propozycje, wyjątki, kontrola kolizji i osobno zatwierdzana zmiana nazw.

### Modified Capabilities

Nie wskazano istniejącej kanonicznej specyfikacji tych funkcji. Powyższe możliwości wymagają specyfikacji w późniejszym etapie; zmiana konsoliduje pełną dokumentację analityczną (`00`–`12`), skrypty oraz bezpieczny planer `v2` (read-only), przy zablokowanym wykonawcy `apply`.

## Impact

Wszystkie materiały z dawnego `sandbox/2026-09-19-gdrive-analysis` zostały przeniesione do katalogu zmiany `openspec/changes/gdrive-structure-and-file-naming/`. Zakres obejmuje skrypty w `openspec/changes/gdrive-structure-and-file-naming/scripts/`, raporty prywatnych metadanych poza Git i późniejsze uzupełnienie zasad z 06–07. Zachowano historyczne dokumenty (`00`–`09`) i pierwszy raport dry-run (`11`), dopisując uściślenia i wyniki `dry-run v2` (`12`) zamiast usuwać wcześniejszy kontekst.

Punkty odniesienia w katalogu zmiany:
- [00 — synteza i rekomendacje główne](./analysis/00-synteza-i-rekomendacje-glowne.md) (oraz analizy bazowe [01](./analysis/01-architektura-i-struktura.md), [02](./analysis/02-uprawnienia-bezpieczenstwo-archiwizacja.md), [03](./analysis/03-plan-czyszczenia-i-selekcja-plikow.md), [04](./analysis/04-workflow-nawyki-i-automatyzacja.md), [05](./analysis/05-wielowymiarowa-kategoryzacja-i-metryki.md))
- [06 — architektura](./analysis/06-optymalna-struktura-i-procesy-zarzadzania.md)
- [07 — mapa](./analysis/07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md)
- [08 — uprawnienia, automatyzacja i dylemat emoji](./analysis/08-uprawnienia-automatyzacja-i-dylemat-emoji.md)
- [09 — review](./analysis/09-review-katalogow-i-mapowania-gdrive.md)
- [10 — konwencja nazw plików](./analysis/10-konwencja-nazewnictwa-plikow.md)
- [11 — raport dry-run migracji (v1)](./reports/11-raport-dry-run-migracji-2026-10-13.md)
- [12 — poprawiony dry-run i plan bezpiecznej migracji (v2)](./reports/12-poprawiony-dry-run-i-plan-bezpiecznej-migracji.md)
- [Stan skryptu migracji](./scripts/gdrive_migration/README.md) oraz [procedura bezpieczeństwa SAFETY.md](./scripts/gdrive_migration/SAFETY.md)

## Non-Goals

Usuwanie plików, opróżnianie kosza, deduplikacja, migracja zdjęć, szyfrowanie, automatyczna zmiana uprawnień, transfer Takeout, tworzenie backupów skryptem i jednoczesne zmienianie struktury oraz nazw plików. Wykonawca `apply` pozostaje celowo zablokowany do czasu zatwierdzenia planu przez użytkownika.

## Risks and Unverified Assumptions

- W `dry-run v2` potwierdzono 42 383 pozycje w drzewie My Drive, 28 folderów i 53 pliki w root (wobec 52 w historycznej mapie 07 — 1 dodatkowa pozycja oznaczona do przeglądu). Nadal brakuje pełnego audytu nazw wewnątrz wszystkich podfolderów (zadanie Etapu B).
- 36 pozycji `blocked` / do decyzji w `dry-run v2` (m.in. przypisanie karty szkolnej, energii, firm/projektów, poddrzew medycznych, dokumentów tożsamości oraz podfolderów folderu `25`) wymaga ręcznego rozstrzygnięcia przed zapisem.
- Daty biletu i planów podróży oraz rozwinięcie `23` do `2023` wymagają potwierdzenia. Nie wolno przyjmować dat utworzenia/modyfikacji jako daty dokumentu bez dowodu.
- Transliteracja może powodować kolizje i osłabić rozpoznawalność nazw własnych. Zasoby aplikacyjne wymagają wyjątków.
- Takeout nie jest zakładanym mechanizmem odtworzenia 1:1; wybór folderów i kompletność kopii trzeba potwierdzić na koncie.
- Planer `v2` (`planner.py`) poprawnie rozwiązuje rzeczywiste ID roota i ogranicza skan do My Drive w trybie odczytu, natomiast nowy wykonawca `apply` obsługujący schemat `v2`, pełną weryfikację po partii i warunkowy rollback wymaga jeszcze implementacji i testów na osobnym koncie testowym Drive.
- Cofanie może być zablokowane przez późniejsze zmiany lub kolizje. Nie obiecujemy bezwarunkowej odwracalności.

## Acceptance Criteria

1. Etap A zachowuje nazwy plików i ma własny plan (`plan.json` v2) oraz weryfikację operacji.
2. Etap B rozpoczyna się po weryfikacji A; obejmuje kompletny raport zakresu i zatwierdzone pozycje.
3. Niepewne daty, opisy, kolizje i zmieniony stan blokują operację; brak fikcyjnych dat i sztucznych rozszerzeń.
4. Każda wykonana operacja ma ID, zapis stanu przed/po, wynik oraz warunki cofania zgodne z `SAFETY.md`.
5. Testy obejmują rzeczywiste ID roota, kolizje po transliteracji, dokumenty Google, ponowne uruchomienie, błędy częściowe i cofanie.
