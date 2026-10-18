# Zatwierdzenie, weryfikacja i odtworzenie migracji

## Obecny stan

Planowanie v2 jest tylko do odczytu. `apply` jest zablokowane; poniższa procedura to wymagania przed przyszłym wykonaniem, a nie informacja o już wdrożonym automatycznym rollbacku. Testy wykonuje się na danych syntetycznych i atrapach API; testu zapisu na osobnym koncie Google jeszcze nie przeprowadzono.

## Bramka zatwierdzenia

1. Przejrzeć `dry_run_report.md` i każdą operację w `plan.json`. Zatwierdzić konkretne ID i cele, nie tylko liczbę operacji. Pozostawić listę świadomie odłożonych pozycji.
2. Potwierdzić przypisanie karty szkolnej, energii, firm/projektów oraz poddrzew medycznych. Nie archiwizować Kuby, nie scalać gałęzi dzieci i nie usuwać zbiorów Chrome, Gems, backupów, haseł ani Takeout na podstawie samych nazw.
3. Potwierdzić miejsca zapisu Notability, Chrome i skanera paragonów. Przeniesienie nie może zerwać działania aplikacji. Obsidian nie otrzymuje automatycznie aktywnego Sync.
4. Sprawdzić uprawnienia źródeł i celów oraz skutki dziedziczenia. Planowanie nie potwierdza, że pliki są prywatne. Zmiana nazwy lub rozszerzenia nie szyfruje danych.
5. Przed wykonaniem odświeżyć inwentaryzację i porównać z zatwierdzonym planem. Każda zmiana źródła, rodzica, nazwy lub kolizja powinna zatrzymać odpowiednią partię przed pierwszym zapisem.

Nie nadawać szerszego OAuth i nie zdejmować blokady wykonawcy tylko dlatego, że dry-run zakończył się poprawnie.

## Wymagania dla przyszłego wykonawcy

- Osobny testowy zestaw na Drive, jawna zgoda na zapis i testy: istniejący cel, duplikaty, przerwane wykonanie, ponowienie i odtworzenie.
- Obsługa wyłącznie zatwierdzonego schematu v2 i zapis skrótu kryptograficznego zatwierdzonego planu w dzienniku.
- Dziennik zapisywany trwale **przed i po** każdej operacji: ID, poprzednia nazwa i wszyscy rodzice, stan docelowy, czas, odpowiedź/błąd API oraz ID utworzonego folderu.
- Zatrzymanie przy konflikcie lub błędzie, bez kontynuowania zależnych operacji. Odtworzenie stanu po przerwaniu i idempotentne ponowienie.
- Bez automatycznego usuwania, opróżniania kosza, modyfikacji uprawnień lub szyfrowania. Te działania wymagają osobnego zatwierdzenia i procedury.

## Weryfikacja po każdej przyszłej partii

- Odczytać po ID każdy zmieniony element i porównać nazwę oraz rodziców z celem konkretnej operacji.
- Sprawdzić kompletność przeniesionych poddrzew, zachowanie ID, brak kolizji i brak znikających elementów; same agregaty roota nie wystarczą.
- Sprawdzić rzeczywisty dostęp właściciela i współdzielących, a także nowy zapis dokumentu przez każdą aplikację, której punkt wejścia zmieniono.
- Raportować osobno sukces, brak wykonania, rozbieżność i błąd; nie deklarować zakończenia, jeśli jakaś zależna operacja nie przeszła kontroli.

## Procedura odtworzenia (ręczna, warunkowa)

1. Zatrzymać kolejne partie; zachować plan, pełny dziennik i aktualną inwentaryzację.
2. Cofanie prowadzić w odwrotnej kolejności **tylko potwierdzonych zakończonych operacji**. Sprawdzić bieżący stan przed każdym cofnięciem; nie nadpisywać późniejszych zmian użytkownika.
3. Dla zmiany nazwy przywrócić poprzednią nazwę po sprawdzeniu kolizji. Dla przeniesienia przywrócić poprzednich rodziców, usuwając wyłącznie rodzica dodanego przez migrację, po kontroli dostępu i konfliktów.
4. Nowe foldery pozostawić, jeśli zawierają jakiekolwiek elementy lub późniejsze zmiany. Usunięcie pustych folderów jest osobną zatwierdzaną czynnością, nie domyślnym rollbackiem.
5. Ponownie sprawdzić po ID nazwy, rodziców, dostęp i działanie aplikacji. Zmiany dziedziczonych uprawnień mogą wymagać osobnego odtworzenia — samo cofnięcie rodzica nie gwarantuje pełnego przywrócenia dostępu.

Pola `before` w planie są punktem odniesienia dla zmian nazw i przeniesień, ale **nie zastępują dziennika wykonania, audytu uprawnień ani kopii zapasowej treści**.
