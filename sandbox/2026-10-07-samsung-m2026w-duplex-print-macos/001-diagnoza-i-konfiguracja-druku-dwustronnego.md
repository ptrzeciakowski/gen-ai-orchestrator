# 001: Diagnoza problemu i konfiguracja druku dwustronnego Samsung M2026W na macOS

- **Data i godzina sesji:** 2026-10-06 23:09:23 CEST
- **ID sesji:** `f4d4a9a6-75b1-4089-b43c-4184927b7a96`
- **Tytuł:** Diagnoza braku druku obustronnego w Samsung M2026W i uruchomienie kolejki CUPS z manual duplex
- **Lokalizacja:** `sandbox/2026-10-07-samsung-m2026w-duplex-print-macos`

---

# Rozdział 1: Diagnoza, inżynieria odwrotna filtrów CUPS i rozwiązanie błędu uprawnień

## Użytkownik (Wypowiedź 1)

Mam drukarkę samsung m2026W, w której nie jestem w stanie wymusić drukowania obustronnego (ręcznego z przekładaniem kartek). Kiedyś wydaje mi się, że to działało, ale przestało.

Chciałbym mieć rozwiązanie na to, choćby to miałbyć sterownik napisany od zera, choć zapewne takie istnieją.

Zdiagnozuj problem i zaproponuj konkretne rozwiazania.

## Asystent (Odpowiedź 1)

### Diagnoza problemu

#### 1. Dlaczego to kiedyś działało, a potem przestało?
* **Brak sprzętowego dupleksu:** Drukarka Samsung Xpress M2026W jest budżetową drukarką laserową (SPL/GDI). Fizycznie **nie posiada modułu automatycznego odwracania papieru (duplexera)**. Oznacza to, że druk dwustronny w tym modelu **zawsze musiał być realizowany programowo (manual duplex)**.
* **Co się stało na Twoim Macu:**
  Sprawdziliśmy bieżącą konfigurację podsystemu druku CUPS na Twoim komputerze:
  ```
  urządzenie: dnssd://Samsung%20M2020%20Series%20(SEC8425197CA25B)._ipp._tcp.local./...
  PPD: Samsung M2020 Series-AirPrint (utworzony przez ipp2ppd, APAirPrint: True)
  ```
  1. **Drukarka została dodana przez AirPrint (IPP Everywhere):** W nowszych wersjach macOS (macOS 13/14/15+) system przy wykryciu drukarki w sieci Wi-Fi domyślnie konfiguruje ją w trybie *AirPrint*, ignorując zainstalowane sterowniki producenta.
  2. Podczas negocjacji IPP system pyta urządzenie: *„Czy posiadasz sprzętowy duplexer?”*. Drukarka odpowiada: *„Nie (`sides-supported: one-sided`)”*.
  3. W efekcie macOS **całkowicie usuwa i blokuje opcję druku dwustronnego** w oknie drukowania.
  4. Dodatkowo Apple wycofało wsparcie dla starych wtyczek okna drukowania (PDE), przez co autorskie menu Samsunga przestało się pojawiać w nowym interfejsie okna druku macOS.

#### 2. Jak to działało w oryginalnym sterowniku Samsunga?
W systemie (w katalogu `/Library/Printers/Samsung/`) znajdują się oryginalne uniwersalne binaria Samsung/HP (skompilowane zarówno dla x86_64, jak i natywnie dla Apple Silicon ARM64). Mechanizm ten opierał się na dwóch filtrach:
* **`/Library/Printers/Samsung/UPD/Filters/prefilter`** – analizuje dokument PDF, a przy opcji `SECManualDuplexOption` **automatycznie przestawia kolejność stron** (najpierw parzyste w odwróconym porządku: np. 4, 2, a potem nieparzyste: 1, 3).
* **`/Library/Printers/Samsung/UPD/Filters/rastertosec`** – generuje strumień QPDL z komendą PJL `@PJL SET DUPLEX = MANUAL`. Komenda ta powoduje, że po wydrukowaniu pierwszej partii drukarka **zatrzymuje się i miga diodą**, czekając na przełożenie kartek i wciśnięcie fizycznego przycisku na obudowie.

Przetestowaliśmy niskopoziomowo działanie tych filtrów na Twoim systemie – **działają bezbłędnie**.

---

### Rozwiązania

#### Rozwiązanie 1: Dedykowana kolejka ze sterownikiem Samsunga (Wdrożone i gotowe do użycia)

Skonfigurowaliśmy na Twoim Macu drugą kolejkę drukarki o nazwie:
> **`Samsung M2026W (Druk Dwustronny)`**
> Połączoną bezpośrednio po protokole JetDirect (`socket://sec8425197ca25b.local:9100`) z natywnym sterownikiem Samsunga, domyślnym formatem **A4** oraz włączonym na stałe parametrem **`SECManualDuplexOption=LongEdge`**.

**Jak tego używać w codziennej pracy:**
1. W dowolnym programie (Chrome, Safari, Word, Podgląd itp.) naciśnij `Cmd + P`.
2. Z listy drukarek wybierz:
   * **`Samsung M2026W (Druk Dwustronny)`** – gdy chcesz drukować obustronnie.
   * **`Samsung M2020 Series`** (dotychczasowa) – gdy chcesz zwykły druk jednostronny.
3. Kliknij **Drukuj**.
4. Drukarka wydrukuje pierwszą stronę kartek i **zatrzyma się z migającą diodą**.
5. Weź cały plik kartek z górnej tacy odbiorczej i włóż go prosto do dolnego podajnika (dzięki filtrowi `prefilter` **nie musisz ręcznie odwracać kolejności kartek** – sterownik już to uwzględnił!).
6. Naciśnij fizyczny przycisk wznawiania na drukarce (przycisk **WPS / Print Screen / Zasilania**). Drukarka zadrukuje drugą stronę.

---

#### Rozwiązanie 2: Awaryjny manualny duplex w macOS bez dedykowanej kolejki
Gdybyś kiedykolwiek drukował z innego komputera Mac bez powyższej konfiguracji:
1. Otwórz dokument w aplikacji **Podgląd (Preview)** -> `Cmd + P`.
2. W sekcji **Obsługa papieru** (Paper Handling):
   * Krok 1: Wybierz **Tylko nieparzyste** -> Drukuj.
   * Krok 2: Przełóż wydrukowane kartki do podajnika.
   * Krok 3: Wybierz **Tylko parzyste** oraz zaznacz **Odwrócona kolejność stron** -> Drukuj.

---

#### Rozwiązanie 3: Autorski skrypt / Szybka Akcja Findera (Quick Action)
Gdyby w przyszłych wersjach macOS Apple całkowicie usunęło mechanizm filtrów CUPS, możemy przygotować prosty skrypt w Pythonie zintegrowany z menu kontekstowym Findera (pod prawym przyciskiem myszy na pliku PDF):
* Skrypt sam rozdziela PDF na arkusze parzyste i nieparzyste.
* Drukuje pierwszą partię, wyświetla systemowe okienko powiadomienia: *„Przełóż papier i kliknij OK”*.
* Po kliknięciu wysyła drugą partię.

*(Jeśli rozwiązanie z kolejką CUPS w pełni Ci odpowiada, krok ten nie jest obecnie konieczny, ale możemy go wdrożyć w razie potrzeby).*

---

### Podsumowanie
Problem wynikał z automatycznego przypisania drukarki do ograniczonego profilu AirPrint po aktualizacji systemu. Dedykowana kolejka **`Samsung M2026W (Druk Dwustronny)`** jest już aktywna w Twoim systemie i możesz przetestować na niej dowolny wielostronicowy dokument.

## Użytkownik (Wypowiedź 2)

Zerknij do schowka

## Asystent (Odpowiedź 2)

Na zrzucie ekranu widać, że zadanie z Dokumentów Google zatrzymało się z komunikatem **`Błąd: „Data”`** (ang. *stopped with filter error*).

### Co dokładnie się stało (przyczyna):
Sprawdziłem logi systemowe CUPS (`/var/log/cups/error_log`) oraz raport awarii z godziny 23:44:
```text
PID 7858 (/Library/Printers/Samsung/UPD/Filters/prefilter) crashed on signal 11
DoManualDuplex -> fopen("/Library/Caches/com.sec.printer", "w+") -> EACCES (Permission denied)
```
Filtr Samsunga `prefilter` podczas układania stron do druku dwustronnego zapisuje stan do pliku cache `/Library/Caches/com.sec.printer`. Podczas wcześniejszych testów diagnostycznych w terminalu plik ten został utworzony z uprawnieniami tylko dla Twojego użytkownika, przez co systemowy proces druku (`_lp`) nie miał do niego prawa zapisu i sterownik wyłożył się na braku uprawnień.

---

### Co zostało naprawione:
1. **Nadano pełne prawa zapisu i odczytu (`0666`)** do pliku `/Library/Caches/com.sec.printer`.
2. Kolejka **`Samsung M2026W (Druk Dwustronny)`** została zresetowana i jest gotowa do pracy.

### Co zrobić teraz:
Możesz teraz **ponownie puścić wydruk** (albo kliknąć ikonę odświeżenia w oknie kolejki ze zrzutu ekranu):
1. Drukarka powinna normalnie pobrać papier i wydrukować stronę parzystą.
2. Po wydrukowaniu dioda na drukarce zacznie migać (oczekiwanie na manual duplex).
3. Przełóż wydrukowaną kartkę z górnej tacy do dolnego podajnika i wciśnij fizyczny przycisk na obudowie drukarki (WPS / Print Screen), aby dokończyć drugą stronę.

## Użytkownik (Wypowiedź 3)

Zadziałało - dziękuję!

## Asystent (Odpowiedź 3)

Super, bardzo się cieszę, że zadziałało! 🎉

Od teraz masz w systemie na stałe dwie wygodne kolejki:
* **`Samsung M2020 Series`** – gdy potrzebujesz szybkiego druku jednostronnego.
* **`Samsung M2026W (Druk Dwustronny)`** – gdy chcesz drukować obustronnie z automatycznym przeliczaniem kolejności stron i wstrzymaniem na przełożenie kartek.

Gdyby w przyszłości po jakiejś dużej aktualizacji systemu coś się przestawiło, wiesz już dokładnie, że wystarczy trzymać się natywnego sterownika Samsunga zamiast profilu AirPrint. Miłego drukowania!

