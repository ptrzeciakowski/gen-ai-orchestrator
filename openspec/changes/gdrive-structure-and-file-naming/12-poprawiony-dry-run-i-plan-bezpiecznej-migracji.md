# Poprawiony dry-run i przygotowanie bezpiecznej migracji

**Data:** 2026-10-13. **Wynik:** ponowne planowanie tylko do odczytu zakończone. **Nie wykonano migracji na Drive.**

Ten dokument aktualizuje [raport 11](11-raport-dry-run-migracji-2026-10-13.md); wcześniejszy raport pozostaje historycznym zapisem błędnego planu.

## Stan zalecanych kroków

| Krok z raportu 11 | Stan |
|---|---|
| 1. Poprawić rozpoznawanie roota | Wykonano w planowaniu i odczycie inwentaryzacyjnym `verify`. Stary wykonawca jest zablokowany, nie został uznany za naprawiony. |
| 2. Ograniczyć skan i obsłużyć konflikty | Wykonano dla planowania: tylko potwierdzeni potomkowie My Drive, bez przechodzenia przez skróty; wykrywanie duplikatów i kolizji źródeł/celów. |
| 3. Uzupełnić mapowanie zgodnie z 07 i 09 | Uwzględniono 52 pliki oraz propozycje dla 28 folderów i 13 podfolderów folderu 25. Warunkowe mapowania poddrzew nie są wykonywane automatycznie i nadal wymagają decyzji. |
| 4. Testy i ponowienie planowania | 12 testów na osobnych danych syntetycznych i atrapach API przeszło. Ponowiono odczyt rzeczywistego Drive. Testu zmian na osobnym koncie Drive nie wykonano. |
| 5. Zatwierdzenie, weryfikacja i odtworzenie | Przygotowano procedurę w `SAFETY.md`. Ręczne zatwierdzenie należy do użytkownika; automatyczny wykonawca, pełna weryfikacja i rollback nie są gotowe. `apply` pozostaje zablokowane. |

## Wynik nowego dry-run

| Metryka | Wynik |
|---|---:|
| Potwierdzone pozycje w drzewie My Drive | 42 383 |
| Foldery bezpośrednio w root | 28 |
| Pozostałe pozycje bezpośrednio w root | 53 |
| Planowane zmiany nazw folderów | 11 |
| Planowane utworzenia brakujących folderów | 22 |
| Planowane przeniesienia plików | 44 |
| Łączna liczba operacji | 77 |
| Pozycje `blocked` / do decyzji | 36 |
| Operacje faktycznie wykonane na Drive | 0 |

36 pozycji do decyzji nie oznacza 36 różnych zbiorów: raport pokazuje zarówno nieprzypisane foldery główne, jak i szczegółowe decyzje dla podfolderów folderu 25. Podfoldery w obrębie pozostałych przemianowywanych obszarów zachowują dotychczasową strukturę; ich pełna standaryzacja nie została automatycznie zaplanowana.

Liczba 42 383 różni się od 54 585 w pierwszym raporcie przede wszystkim dlatego, że nowy skan ograniczono do potwierdzonego drzewa My Drive. Nie oznacza to usunięcia danych. Nie należy porównywać obu liczb jako identycznego zakresu pomiaru. Bieżący odczyt wykazał 53 pliki w root, podczas gdy historyczna mapa 07 opisuje 52; nieznane pozycje są raportowane do przeglądu.

## Co poprawiono

- Rzeczywisty ID roota zamiast porównywania rodziców z aliasem `root`.
- Planowana zmiana nazwy jest uwzględniana w wirtualnym indeksie przed ustalaniem brakujących folderów. Nie powstaje z góry całe równoległe drzewo docelowe.
- Dokładne dopasowania NFC i obsługa natywnych dokumentów Google, których nazwa w API nie musi zawierać `.gdoc`, `.gsheet`, `.gslides` lub `.gprj`. Bez dopasowań rozmytych do skróconych nazw z dokumentacji.
- Niepewne pliki opisane wcześniej jako przeznaczone do kwarantanny otrzymują w planie cel do przeglądu, nie automatyczne usunięcie.
- Zachowano w propozycjach kontekst osób, samochodów, nieruchomości, firm i importów z folderu 25. Nie przypisano wszystkich projektów Snowflake do HSBC ani energii do konkretnego lokalu na podstawie samej nazwy.
- Dokumenty tożsamości oraz karta szkolna nie są automatycznie przenoszone. Uprawnienia, szyfrowanie i osoba dziecka wymagają potwierdzenia.
- Nowy schemat planu v2 zapisuje stan `before` dla zmian nazw i przeniesień. Nie jest zgodny ze starym wykonawcą; CLI i bezpośrednie wywołanie `apply` są zablokowane.

## Artefakty

- [Czytelny, szczegółowy raport dry-run](scripts/gdrive_migration/dry_run_report.md) — generowany automatycznie przez `plan`; operacje, konflikty i pełna lista propozycji z review 09.
- [Plan v2](scripts/gdrive_migration/plan.json) i [bieżąca inwentaryzacja](scripts/gdrive_migration/inventory.json).
- Poprzednie wyniki zabezpieczone lokalnie w `scripts/gdrive_migration/reports/2026-10-13-original/`.
- [Procedura bezpieczeństwa](scripts/gdrive_migration/SAFETY.md) — bramka zatwierdzenia, wymagania dla przyszłego wykonawcy, weryfikacja po partii i warunkowe ręczne odtworzenie.
- [Testy](scripts/gdrive_migration/test_planner.py), [planer](scripts/gdrive_migration/planner.py) oraz [zaktualizowany README](scripts/gdrive_migration/README.md).

Szczegółowe raporty i inwentaryzacje zawierają prywatne metadane, są ignorowane przez Git i pozostają lokalne; linki do nich nie muszą działać w innym klonie repozytorium. Nie kopiowano tokenów ani credentiali do raportów.

## Następna bramka: decyzje przed zapisem

Przejrzeć szczegółowy raport, rozstrzygnąć niepewne mapowania i zatwierdzić konkretne operacje. Dodatkowo potwierdzić uprawnienia, nowe punkty zapisu aplikacji oraz sposób reorganizacji poddrzew. Dopiero potem przygotować i przetestować wykonawcę na osobnym Drive, wraz z dziennikiem, weryfikacją i odtworzeniem.

**Poprawny dry-run nie jest zgodą na zapis i nie oznacza gotowości do wykonania całej migracji.**
