# Raport dry-run migracji Google Drive

**Data wykonania:** 2026-10-13  
**Tryb:** `plan` — odczyt metadanych bez zmian na Google Drive.  
**Ocena:** inwentaryzacja zakończona; plan niegotowy do wykonania.

## Podsumowanie

Skrypt odczytał **54 585 pozycji** i zapisał lokalny plan zawierający **51 operacji zapewnienia folderów docelowych** (`ensure_folder`). Nie zaplanował zmian nazw ani przeniesień plików. To nie oznacza, że nie są potrzebne: błąd rozpoznawania katalogu głównego uniemożliwił ich poprawne zaplanowanie.

**Nie uruchamiać `apply` na podstawie tego planu.**

| Metryka | Wynik |
|---|---:|
| Pozycje w inwentaryzacji | 54 585 |
| Foldery | 7 733 |
| Pozostałe pozycje, w tym skróty | 46 852 |
| Skróty Google Drive | 16 |
| Operacje `ensure_folder` | 51 |
| Operacje zmiany nazwy | 0 |
| Operacje przeniesienia pliku | 0 |
| Pozycje `blocked` | 1 |
| Zmiany wykonane na Google Drive | 0 |

## Sposób wykonania i źródła

Uruchomiono `scripts/gdrive_migration/migrate.py` z poleceniem `plan`. Na czas uruchomienia ustawiono w pamięci zakres OAuth `https://www.googleapis.com/auth/drive.metadata.readonly`; nie zmieniono kodu skryptu. Nie uruchamiano `apply` ani `verify`.

Źródła raportu:

- [plan.json](scripts/gdrive_migration/plan.json) — operacje, blokady i liczba pozycji;
- [inventory.json](scripts/gdrive_migration/inventory.json) — metadane pozycji odczytanych z API;
- [README skryptu](scripts/gdrive_migration/README.md) — ograniczenia implementacji;
- [migrate.py](scripts/gdrive_migration/migrate.py) — rzeczywista logika skanowania i planowania.

Raport przygotowano lokalnie na podstawie istniejących wyników, bez ponownego odpytywania Google Drive. Pliki JSON są lokalne i ignorowane przez Git, więc linki mogą nie działać w innym klonie repozytorium.

Podczas wykonania zapisano także lokalny `token.json` i utworzono alias `credentials.json` do wskazanego pliku OAuth. Raport nie zawiera tokenów, danych klienta OAuth ani identyfikatorów prywatnych plików.

## Co zawiera plan

| Obszar docelowy | Liczba operacji `ensure_folder` |
|---|---:|
| 00-📥-Inbox | 3 |
| 00-🔒-Poufne-Dokumenty | 2 |
| 01-👨‍👩‍👧‍👦-Rodzina | 5 |
| 02-🏫-Edukacja-Dzieci | 2 |
| 03-🏥-Zdrowie | 5 |
| 04-📄-Dokumenty-Osobiste | 3 |
| 05-💰-Finanse | 5 |
| 07-🏢-Praca-i-Projekty | 4 |
| 10-🏠-Mieszkanie-i-Nieruchomosci | 4 |
| 11-🏡-Lewickie | 2 |
| 12-🚗-Pojazdy | 2 |
| 20-📚-Wiedza-i-Rozwoj | 3 |
| 21-🎵-Audio-i-Multimedia | 1 |
| 22-🏃-Sport-i-Aktywnosc | 1 |
| 23-🎮-Gry-i-Hobby | 1 |
| 24-🏖️-Podroze-i-Wyjazdy | 2 |
| 80-📱-Aplikacje-i-Synchronizacja | 2 |
| 90-🗄️-Archiwum | 3 |
| 99-🗑️-Do-Usuniecia | 1 |
| **Łącznie** | **51** |

`ensure_folder` oznacza zapewnienie całej ścieżki: przy wykonaniu istniejące foldery mogą zostać wykorzystane, a brakujące utworzone. **51 operacji nie oznacza 51 nowych folderów.** Plan dodaje te ścieżki bez wcześniejszego ustalenia, które foldery już istnieją; nie podaje rzeczywistej liczby utworzeń.

Jedyna pozycja `blocked` dotyczy złożonych połączeń podfolderów, wrażliwych identyfikatorów i czyszczenia archiwum. Jest ogólną informacją o zakresie celowo nieautomatyzowanym, a nie kompletną listą konfliktów wykrytych na Dysku.

## Najważniejsze ograniczenie: katalog główny

`root_map()` sprawdza, czy pole `parents` zawiera dosłowny tekst `root`. API używa `root` jako aliasu w zapytaniach, ale w metadanych rodzica zwraca rzeczywisty identyfikator katalogu.

W zapisanej inwentaryzacji **żadna z 54 585 pozycji nie ma `root` w polu `parents`**. Dlatego obecna implementacja nie rozpoznała elementów katalogu głównego, a plan zawiera wyłącznie stałą listę folderów docelowych i ogólne ostrzeżenie.

Konsekwencje:

- brak zmian nazw i przeniesień jest skutkiem wadliwego rozpoznawania roota, nie potwierdzeniem uporządkowania Dysku;
- raport nie rozstrzyga konfliktów nazw ani sposobu scalenia istniejących folderów;
- wykonanie `apply` mogłoby utworzyć równoległe foldery docelowe zamiast przemianować istniejące;
- obecność jednej pozycji `blocked` nie świadczy o braku innych problemów.

## Zakres inwentaryzacji i pozostałe ograniczenia

- Skan obejmuje dostępne nieusunięte pozycje w przestrzeni `drive`; kod nie ogranicza jednoznacznie wyników do drzewa My Drive. Liczba 54 585 nie jest więc potwierdzoną liczbą pozycji wyłącznie na Moim Dysku.
- 149 pozycji nie ma rodzica w zwróconych metadanych; nie należy na tej podstawie automatycznie uznawać ich za pliki w katalogu głównym ani za osierocone.
- Żadna pozycja nie ma niepustego `driveId`; nie rozstrzyga to, czy wszystkie wyniki należą do My Drive.
- Skróty nie są obsługiwane jako foldery. Mapowanie złożonych poddrzew pozostaje niekompletne.
- Kod obejmuje 13 mapowań nazw folderów głównych i 18 nazw plików, a nie całą migrację opisaną w dokumentach 07 i 09.
- `blocked` nie zatrzymuje automatycznie `apply`, `verify` nie sprawdza realizacji każdej operacji, a mechanizmu rollback nie ma.
- Inwentaryzacja nie zawiera rozmiarów plików, więc raport nie ocenia zajętego miejsca ani potencjalnych oszczędności.

## Zalecane kolejne kroki

1. Poprawić rozpoznawanie roota: pobierać jego rzeczywisty identyfikator i stosować go w planowaniu, kontrolach `apply` oraz `verify`.
2. Jednoznacznie ograniczyć i opisać zakres skanowania oraz obsłużyć konflikty i istniejące foldery docelowe.
3. Uzupełnić mapowanie zgodnie z dokumentami [07](07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md) i [09](09-review-katalogow-i-mapowania-gdrive.md).
4. Przetestować logikę na osobnym zestawie danych, a następnie ponownie wykonać planowanie z dostępem tylko do odczytu.
5. Przed jakimkolwiek `apply` ręcznie zatwierdzić poprawiony plan i przygotować weryfikację oraz procedurę odtworzenia zmian.

**Wniosek:** dry-run dostarczył inwentaryzację, ale nie wiarygodny plan migracji. Żadne operacje migracyjne nie zostały wykonane.
