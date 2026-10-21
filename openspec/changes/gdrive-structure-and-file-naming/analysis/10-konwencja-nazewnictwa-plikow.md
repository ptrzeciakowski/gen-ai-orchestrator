# 10: Proponowana konwencja nazw plików Google Drive

**Data:** 2026-10-12, Europe/Warsaw  
**Status:** propozycja do wdrożenia po migracji katalogów; ten dokument nie uruchamia zmian na Dysku.  
**Powiązana zmiana:** [propozycja OpenSpec](../proposal.md).

## 1. Dwa osobne etapy

Etap A obejmuje migrację katalogów i przypisanie plików do docelowych folderów zgodnie z [mapą 07](07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md) i [korektami 09](09-review-katalogow-i-mapowania-gdrive.md). Zachowuje nazwy plików.

Etap B rozpoczyna się po zweryfikowaniu etapu A. Obejmuje audyt nazw, raport `stara nazwa → nowa nazwa`, zatwierdzenie konkretnych pozycji i dopiero potem zmianę nazw. Każdy etap ma oddzielny plan, dziennik i weryfikację. Rozdzielenie pomaga ustalić przyczynę problemu, ale samo nie zapewnia możliwości cofnięcia zmian.

## 2. Analiza istniejących nazw i granice danych

[Dokument 06](06-optymalna-struktura-i-procesy-zarzadzania.md) wymaga bezspacyjnych nazw folderów, a w tabeli wzorców plików podaje m.in. `YYYY-MM-DD - [Podmiot] - [Przedmiot].ext` i `2026-07-24 - Warta - Polisa Toyota Corolla.pdf`. Propozycja usuwa tę niespójność przez rozszerzenie zasady pojedynczego myślnika na pliki.

Tabela w dokumencie 07 opisuje 52 pliki roota: występują daty `30.05.23`, pełne daty ISO w nazwach budżetu, spacje, podkreślniki, znaki diakrytyczne oraz oznaczenia `V2` i `(1)`. Część dat proponowanych w 07 wynika z kontekstu, a nie nazwy źródłowej.

To analiza zapisanej mapy, nie aktualnego konta. Brakuje pełnego bieżącego wykazu nazw ze wszystkich podfolderów. Nie ustalono dominującego formatu na całym Dysku ani udziałów procentowych poszczególnych wzorców. Sufiksy eksportowe `.gdoc`, `.gsheet` i `.gslides` z tabeli nie są dowodem, że występują w rzeczywistym polu `name`.

## 3. Standard

Podstawowy wzorzec: `YYYY-MM-DD-Temat-Opis.ext`. Dopuszczalne warianty: `YYYY-MM-Temat-Opis.ext`, `YYYY-Temat-Opis.ext` i `Temat-Opis.ext`, gdy data jest nieznana lub nie ma znaczenia. Dla dokumentu natywnego Google wzorzec nie ma sztucznego rozszerzenia.

| Element | Reguła |
| :--- | :--- |
| Separator | Pojedynczy myślnik; bez spacji i podkreślników między słowami. Bez myślnika na początku i końcu. |
| Data | Kolejność rok–miesiąc–dzień. Dokładność zgodna z dowodem; nie dopisujemy fikcyjnego dnia ani miesiąca. |
| Znaczenie daty | Data dokumentu, zdarzenia lub okresu rozliczeniowego wskazana w raporcie; nie zastępujemy jej automatycznie datą utworzenia lub modyfikacji w Drive. |
| Litery | Bez polskich znaków diakrytycznych: ą→a, ć→c, ę→e, ł→l, ń→n, ó→o, ś→s, ź/ż→z; analogicznie wielkie litery. |
| Nazwy własne | Zachować sens, identyfikatory, markę i rozpoznawalność po transliteracji. Inne alfabety i nieobsługiwane znaki kierować do ręcznego review. |
| Wielkość liter | Czytelne człony jak w przykładach; zachować akronimy ALK, ISO i identyfikatory. Nie wymuszać automatycznie zmiany wielkości liter nazw własnych. |
| Wersja | Potwierdzone `V2` normalizować do końcowego `v2`. Nie dopisywać `v1` na podstawie braku sufiksu i nie uznawać starej wersji za zbędną. |
| Rozszerzenie | Zachować rzeczywiste rozszerzenie pliku, również wieloczłonowe. Dokumentom natywnym Google nie dopisywać `.gdoc`, `.gsheet` ani `.gslides`; typ ustalać z MIME. |
| Opis | Nie wymyślać treści z niejasnego tytułu. Nowy opis semantyczny wymaga potwierdzenia. |
| Kolizja | Blokować zmianę przy kolizji w folderze docelowym, również między propozycjami. Sprawdzać Unicode NFC i kolizje po transliteracji; podobieństwo bez uwzględnienia wielkości liter zgłaszać do review. |

## 4. Przykłady z mapy

Poniższe propozycje nie są zatwierdzonym planem operacji. Nazwy dokumentów natywnych pokazano bez sufiksów używanych w tabeli eksportowej.

| Obecna nazwa według mapy | Propozycja | Warunek |
| :--- | :--- | :--- |
| `Apteki ALK 30.05.23.xlsx` | `2023-05-30-Apteki-ALK-Zestawienie.xlsx` | Potwierdzić rozwinięcie dwucyfrowego roku i dopisanie „Zestawienie”. |
| `Bilet - WH64222365.pdf` | `2026-08-Bilet-WH64222365.pdf` | Miesiąc i rok pochodzą z propozycji 07; potwierdzić w dokumencie. Bez potwierdzenia: `Bilet-WH64222365.pdf`. |
| `Analiza zużycia energii i fotowoltaiki` | `Analiza-Zuzycia-Energii-i-Fotowoltaiki` | Nie dopisywać roku 2026 tylko dlatego, że występuje w mapie. Potwierdzić MIME i rzeczywistą nazwę. |
| `Plan wycieczki - Tatry Wysokie (Słowacja) V2` | `2026-08-Tatry-Wysokie-Slowacja-Plan-Wycieczki-v2` | Potwierdzić datę i kolejność członów; bez potwierdzonej daty pominąć prefiks. |

## 5. Reguły transformacji i wyjątki

1. Odczytać rzeczywistą nazwę, ID, MIME i ID rodzica; rozdzielić rozszerzenie tylko dla rzeczywistego pliku binarnego.
2. Znormalizować Unicode, transliterować obsługiwane znaki i zastąpić odstępy oraz podkreślniki pojedynczym myślnikiem w części opisowej.
3. Nie zmieniać automatycznie interpunkcji wewnątrz identyfikatora. Usunięcie nawiasów, dwukropka lub zmiana kolejności słów musi być jawna w raporcie.
4. Rozpoznać datę wyłącznie na podstawie udokumentowanej reguły; niejednoznaczne daty, w tym dwucyfrowe lata, wymagają decyzji.
5. Sprawdzić proponowane nazwy względem wszystkich rodzeństw oraz całego planu. Kolizje blokować, bez automatycznej numeracji, nadpisywania lub deduplikacji.
6. Pozycje już zgodne ze standardem oznaczyć jako bez zmian; ponowne planowanie ma być idempotentne.

Domyślnie wykluczyć kopie aplikacyjne, archiwa Takeout, zasoby synchronizacji, foldery zarządzane przez aplikacje, skróty, pliki spoza My Drive i zasoby bez prawa zmiany nazwy. Dodanie wyjątku do zakresu wymaga jawnego review. Sufiks `(1)` nie dowodzi duplikatu. Oryginalne pakiety, backupy i identyfikatory mogą wymagać zachowania nazwy.

## 6. Raport, wykonanie i cofanie

Raport JSON/CSV powinien zawierać: ID pliku, ID rodzica, MIME, starą nazwę, proponowaną nazwę, regułę transformacji, źródło i dokładność daty, uzasadnienie opisu, konflikt, status `unchanged/proposed/blocked/excluded` oraz decyzję użytkownika. Raporty zawierają prywatne metadane i nie trafiają do Git.

Wykonanie etapu B obejmuje wyłącznie zatwierdzone pozycje z konkretnego planu. Przed każdą operacją sprawdzić ponownie ID, nazwę źródłową, rodzica, uprawnienia i kolizje. Zmiana od czasu planowania blokuje pozycję. Dziennik zapisuje stan przed i po oraz wynik operacji.

Weryfikacja porównuje każdą wykonaną operację z zatwierdzonym planem; liczy sukcesy, pominięcia i błędy. Dla cofania zapisać oryginalne nazwy, a w etapie A także rodziców. Przywracanie jest warunkowe: wymaga niezmienionego stanu i kontroli kolizji. Obecny skrypt nie zapewnia rollback.

## 7. Backup przed migracją

Backup użytkownik przygotowuje ręcznie, bez dodatkowego skryptu. W Google Takeout można odznaczyć inne usługi i pozostawić Dysk. Oficjalna instrukcja opisuje wybór podzbioru danych tam, gdzie produkt udostępnia taką opcję; dostępność wyboru konkretnych folderów należy sprawdzić na koncie podczas eksportu. Nie zakładamy jej jako zweryfikowanej dla tego konta. [Instrukcja Google Takeout](https://support.google.com/accounts/answer/3024190?hl=pl).

Opcja „Dodaj do Dysku” zapisuje archiwum na Google Drive i zużywa miejsce konta. Instrukcja nie gwarantuje wskazania dowolnego folderu docelowego. Po eksporcie użytkownik może uporządkować archiwum ręcznie; kopia na tym samym koncie nie jest niezależnym backupem. [Instrukcja Google Takeout](https://support.google.com/accounts/answer/3024190?hl=pl).

Takeout traktujemy jako eksport danych, bez założenia odtworzenia Dysku jeden do jednego, uprawnień, historii wersji lub właściwości dokumentów natywnych. Google ostrzega, że zmiany wykonane pomiędzy zleceniem a utworzeniem eksportu mogą nie zostać uwzględnione, w tym zmiany uprawnień Drive. Przed migracją zweryfikować możliwość otwarcia próbek i zakres kopii; osobno zachować metadane operacji. [Ograniczenia eksportu](https://support.google.com/accounts/answer/3024190?hl=pl).

## 8. Plan wdrożenia

1. Dopracować etap A: rzeczywiste ID roota, zakres My Drive, konflikty, mapowanie 09, weryfikacja operacji i warunkowe cofanie.
2. Potwierdzić backup oraz zatwierdzić plan katalogów. Przetestować i wykonać etap A, następnie zweryfikować jego wynik.
3. Po etapie A zebrać pełny wykaz nazw w podfolderach objętych zakresem; raportować rzeczywiste liczby wzorców oraz wyjątki.
4. Wygenerować raport etapu B i zatwierdzić konkretne propozycje wraz z datami i opisami.
5. Przetestować normalizację i cofanie na osobnym zestawie danych. Wykonać zatwierdzone zmiany, zweryfikować operacje i odnotować wyjątki.

Warunki akceptacji: brak zmian nazw plików w etapie A; brak dopisanych fikcyjnych dat i rozszerzeń; kolizje i zmieniony stan blokują wykonanie; raport obejmuje wszystkie pozycje zakresu; każda wykonana zmiana ma zapis przed/po i wynik weryfikacji. Wcześniejsze dokumenty 06–09 pozostają historią; wdrożenie propozycji wymaga późniejszego uzupełnienia kanonicznych reguł.
