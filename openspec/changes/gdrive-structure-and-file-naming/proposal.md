# Propozycja zmiany: migracja struktury Google Drive i konwencja nazw plików

**Kod:** `gdrive-structure-and-file-naming`  
**Data:** 2026-10-12  
**Status:** propozycja; nie oznacza zatwierdzenia planów operacji ani wykonania zmian na Google Drive.

## Why

Dokument 06 wymaga nazw folderów bez spacji, ale podaje wzorce nazw plików ze spacjami. Mapa 07 łączy przenoszenie zasobów z proponowanymi zmianami nazw i datami częściowo wynikającymi z kontekstu. Review 09 wskazuje korekty mapowania, a zaimportowany skrypt migracyjny jest wersją roboczą z opisanymi ograniczeniami.

Potrzebne są dwa niezależnie planowane i weryfikowane etapy: najpierw migracja katalogów bez zmian nazw plików, następnie audyt i standaryzacja nazw.

## What Changes

- Etap A: dopracować migrację katalogów i przenoszenie plików według 07 oraz korekt 09, zachowując nazwy plików.
- Etap B: po weryfikacji A zinwentaryzować nazwy w podfolderach i wygenerować raport stara nazwa → nowa nazwa. Zmieniać wyłącznie zatwierdzone pozycje.
- Przyjąć proponowany format `YYYY-MM-DD-Temat-Opis.ext`, z wariantami miesiąca, roku lub bez daty; pojedyncze myślniki, transliteracja polskich znaków i rzeczywiste rozszerzenia. Nie dopisywać sztucznych rozszerzeń dokumentom Google.
- Blokować niejednoznaczne daty, opisy, kolizje i zmieniony stan źródła. Zachować ID oraz dziennik przed/po do weryfikacji i warunkowego cofania.
- Backup przygotować ręcznie przez Takeout, z potwierdzeniem zakresu i ograniczeń eksportu. Nie dodawać skryptu backupowego.
- Szczegółowy standard, przykłady, wyjątki i plan: [10 — konwencja nazw plików](../../../sandbox/2026-09-19-gdrive-analysis/10-konwencja-nazewnictwa-plikow.md).

## Capabilities

### New Capabilities

- `gdrive-structural-migration`: planowanie, zatwierdzanie, wykonanie, weryfikacja i warunkowe cofanie zmian struktury.
- `gdrive-file-name-normalization`: audyt nazw, deterministyczne propozycje, wyjątki, kontrola kolizji i osobno zatwierdzana zmiana nazw.

### Modified Capabilities

Nie wskazano istniejącej kanonicznej specyfikacji tych funkcji. Powyższe możliwości wymagają specyfikacji w późniejszym etapie; ten commit dodaje propozycję i dokumentację, nie implementację.

## Impact

Zakres przyszłych zmian obejmuje skrypty w `sandbox/2026-09-19-gdrive-analysis/scripts/`, raporty prywatnych metadanych poza Git i późniejsze uzupełnienie zasad z 06–07. Zachować historyczne dokumenty i korekty 09, dopisując uściślenia zamiast usuwać wcześniejszy kontekst.

Punkty odniesienia:
- [06 — architektura](../../../sandbox/2026-09-19-gdrive-analysis/06-optymalna-struktura-i-procesy-zarzadzania.md)
- [07 — mapa](../../../sandbox/2026-09-19-gdrive-analysis/07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md)
- [09 — review](../../../sandbox/2026-09-19-gdrive-analysis/09-review-katalogow-i-mapowania-gdrive.md)
- [Stan skryptu](../../../sandbox/2026-09-19-gdrive-analysis/scripts/gdrive_migration/README.md)

## Non-Goals

Usuwanie plików, opróżnianie kosza, deduplikacja, migracja zdjęć, szyfrowanie, automatyczna zmiana uprawnień, transfer Takeout, tworzenie backupów skryptem i jednoczesne zmienianie struktury oraz nazw plików. Bieżące zlecenie obejmuje zapis propozycji; nie wdraża operacji Drive.

## Risks and Unverified Assumptions

- 52 pliki i 28 folderów opisują mapę 07, nie zweryfikowany bieżący stan konta. Brakuje pełnego aktualnego audytu nazw w podfolderach.
- Daty biletu i planów podróży oraz rozwinięcie `23` do `2023` wymagają potwierdzenia. Nie wolno przyjmować dat utworzenia/modyfikacji jako daty dokumentu bez dowodu.
- Transliteracja może powodować kolizje i osłabić rozpoznawalność nazw własnych. Zasoby aplikacyjne wymagają wyjątków.
- Takeout nie jest zakładanym mechanizmem odtworzenia 1:1; wybór folderów i kompletność kopii trzeba potwierdzić na koncie.
- Obecny skrypt wymaga poprawienia rozpoznawania roota, zakresu My Drive i weryfikacji. Nie zapewnia rollback ani pełnego mapowania.
- Cofanie może być zablokowane przez późniejsze zmiany lub kolizje. Nie obiecujemy bezwarunkowej odwracalności.

## Acceptance Criteria

1. Etap A zachowuje nazwy plików i ma własny plan oraz weryfikację operacji.
2. Etap B rozpoczyna się po weryfikacji A; obejmuje kompletny raport zakresu i zatwierdzone pozycje.
3. Niepewne daty, opisy, kolizje i zmieniony stan blokują operację; brak fikcyjnych dat i sztucznych rozszerzeń.
4. Każda wykonana operacja ma ID, zapis stanu przed/po, wynik oraz warunki cofania.
5. Testy obejmują rzeczywiste ID roota, kolizje po transliteracji, dokumenty Google, ponowne uruchomienie, błędy częściowe i cofanie.
