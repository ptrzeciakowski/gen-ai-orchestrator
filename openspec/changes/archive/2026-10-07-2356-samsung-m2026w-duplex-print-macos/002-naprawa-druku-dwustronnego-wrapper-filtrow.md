# 002: Rozwiązanie problemu braku dupleksu w aplikacjach macOS (Job 177) i Uniwersalny Wrapper Filtrów CUPS

- **Data i godzina sesji:** 2026-10-08 17:16:43 CEST
- **ID sesji:** `179c8600-1034-4461-8995-1613e09d85f7`
- **Tytuł:** Inżynieria odwrotna Job 177, wykrycie pomijania manualnego dupleksu w oknie macOS i wdrożenie uniwersalnego wrappera filtrów CUPS
- **Lokalizacja:** `sandbox/archive/2026-10-07-samsung-m2026w-duplex-print-macos`

---

# Rozdział 1: Analiza zgłoszenia i pełna rekonstrukcja zadania Job 177

## Użytkownik (Wypowiedź 1)
> Wróćmy do '/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-10-07-samsung-m2026w-duplex-print-macos': w dalszym ciągu nie drukuje duplxem

---

## Asystent (Diagnoza Niskopoziomowa)

### 1. Rekonstrukcja zadania wydruku z logów systemowych CUPS

Przeanalizowaliśmy logi demona CUPS (`/var/log/cups/error_log` oraz `/var/log/cups/error_log.O`). O godzinie **17:15:40** zarejestrowano zadanie **Job 177** wysłane przez użytkownika z aplikacji **Podgląd (Preview)**:

```text
D [08/Oct/2026:17:15:40 +0200] [Job 177] argv[0]="Samsung_M2026W_Duplex"
D [08/Oct/2026:17:15:40 +0200] [Job 177] argv[1]="177"
D [08/Oct/2026:17:15:40 +0200] [Job 177] argv[2]="pawel"
D [08/Oct/2026:17:15:40 +0200] [Job 177] argv[3]="02-nowy-zestaw-treningowy.pdf"
D [08/Oct/2026:17:15:40 +0200] [Job 177] argv[4]="1"
D [08/Oct/2026:17:15:40 +0200] [Job 177] argv[5]="AP_ColorMatchingMode=AP_ApplicationColorMatching ... com.apple.print.JobInfo.PMApplicationName=Podgląd com.apple.print.PrintSettings.PMDuplexing..n.=2 DestinationPrinterID=Samsung_M2026W_Duplex Duplex=DuplexNoTumble media=A4 sides=two-sided-long-edge PageSize=A4"
```

### 2. Kluczowe odkrycie: Dlaczego drukarka wypluła 5 osobnych kartek?

Porównaliśmy strukturę wywołań filtrów w **Job 159** (z sesji 1, gdzie manual duplex działał) oraz **Job 177** (gdzie nie zadziałał):

1. **W Job 159 (gdzie dupleks działał):**
   W opcjach `argv[5]` znajdował się jawny parametr:
   ```text
   SECManualDuplexOption=LongEdge
   ```
2. **W Job 177 (z aplikacji Podgląd):**
   Systemowe okno druku macOS przesłało wyłącznie standardowe atrybuty CUPS/Apple:
   ```text
   Duplex=DuplexNoTumble
   sides=two-sided-long-edge
   com.apple.print.PrintSettings.PMDuplexing..n.=2
   ```
   **Parametru `SECManualDuplexOption` NIE BYŁO w `argv[5]`!**

---

## Rozdział 2: Inżynieria odwrotna filtrów Samsunga (`prefilter` i `rastertosec`)

Przeprowadziliśmy deasemblację binariów filtrów (`otool -tvV -arch arm64`) z katalogu `/Library/Printers/Samsung/UPD/Filters/`:

### 1. Zachowanie filtru `prefilter`:
```assembly
0000000100003d54    adr x0, "SECManualDuplexOption"
0000000100003d60    bl  _cupsGetOption
...
0000000100003e00    mov x0, x25 ; SECManualDuplexOption
0000000100003e04    bl  _strcasestr("None")
...
0000000100003fb8    cbz w24, ...
0000000100003fc8    ldr x3, [___stdoutp]
0000000100003fd8    bl  _fwrite  ; <- bezpośredni passthrough!
```
- Filtr `prefilter` odpytuje **wyłącznie** `cupsGetOption("SECManualDuplexOption", ...)`.
- Nie sprawdza standardowych atrybutów `Duplex` ani `sides`.
- Gdy `SECManualDuplexOption` nie ma w `argv[5]`, filtr uznaje opcję za `"None"` i wykonuje **bezpośredni passthrough** (kopiuje PDF wejściowy do wyjściowego 1:1 bez zamiany kolejności stron na arkusze parzyste/nieparzyste).

### 2. Zachowanie filtru `rastertosec`:
```assembly
000000010000a778    adr x0, "SECManualDuplexOption"
000000010000a780    bl  _cupsGetOption
...
000000010000a888    adr x0, "@PJL SET DUPLEX = MANUAL\r\n"
000000010000a890    bl  _printf
000000010000a8b8    cbnz w8, 0x10000ab78 ; <- przeskakuje sprawdzanie PMDuplexing!
...
000000010000a9f0    adr x0, "com.apple.print.PrintSettings.PMDuplexing..n."
000000010000aa38    mov x0, x21 ; PMDuplexing == "2"
000000010000aa5c    adr x0, "@PJL SET DUPLEX = ON\r\n" ; <- HARDWARE DUPLEX!
```
- Gdy `SECManualDuplexOption=LongEdge` jest obecne: filtr generuje `@PJL SET DUPLEX = MANUAL` i przeskakuje sprawdzanie `PMDuplexing`.
- Gdy `SECManualDuplexOption` brakuje: filtr przechodzi do sprawdzania `PMDuplexing..n.`. Widząc wartość `2` (dwustronny), generuje komendę sprzętową:
  ```text
  @PJL SET DUPLEX = ON
  ```
- **Ponieważ Samsung M2026W fizycznie nie posiada modułu automatycznego dupleksu**, kontroler drukarki ignoruje komendę `@PJL SET DUPLEX = ON` i drukuje każdą stronę na osobnym arkuszu bez pauzy i bez migania diody!

---

## Rozdział 3: Trwałe Rozwiązanie Architektoniczne — Uniwersalny Wrapper Filtrów CUPS

Aby zapewnić, że manual duplex działa **zawsze i z każdej aplikacji** (Podgląd, Pages, Word, Safari, Chrome, Google Docs, Acrobat, terminal):

1. **Napisano natywny wrapper w C (`samsung-duplex-wrapper.c`):**
   - Skompilowany uniwersalnie dla **ARM64 (Apple Silicon)** oraz **x86_64 (Intel)**.
   - Działa jako filtr CUPS przed `prefilter` oraz `rastertosec`.
   - Analizuje parametry `argv[5]`:
     - Jeśli dokument ma włączony dupleks standardowy (`Duplex=DuplexNoTumble`, `sides=two-sided-long-edge` lub domyślny na tej kolejce) -> dokłada `SECManualDuplexOption=LongEdge`.
     - Jeśli dupleks z krawędzią krótką (`DuplexTumble`, `two-sided-short-edge`) -> dokłada `SECManualDuplexOption=ShortEdge`.
     - Jeśli użytkownik odznaczył dupleks (`Duplex=None`, `sides=one-sided`) -> dokłada `SECManualDuplexOption=None`.
   - Automatycznie dba o uprawnienia pliku `/Library/Caches/com.sec.printer` (`0666`), zapobiegając crashom.
   - Wywołuje oryginalne filtry za pomocą `execv()`, gwarantując natychmiastowe wykonanie i brak narzutu.

2. **Dedykowane punkty wejścia:**
   - `/Library/Printers/Samsung/UPD/Filters/prefilter-duplex`
   - `/Library/Printers/Samsung/UPD/Filters/rastertosec-duplex`

3. **Aktualizacja PPD (`Samsung_M2020_Series_Clean.ppd`):**
   - Kolejka `Samsung_M2026W_Duplex` wskazuje bezpośrednio na powyższe wrappery.
   - Oryginalne pliki sterownika producenta pozostają w 100% nienaruszone.

---

# Rozdział 4: Diagnoza błędu „No pages found!” (Job 178) i dedykowana kompilacja

## Użytkownik (Wypowiedź 2)
> Powiodło się uruchomienie, potem uruchomiłem test ale nic się nie drukuje.
> ID żądania to Samsung_M2026W_Duplex-178 (1 plików)

## Asystent (Diagnoza i Naprawa)

### 1. Analiza błędu w logu CUPS dla Job 178
W `/var/log/cups/error_log` zarejestrowano:
```text
I [Job 178] Started filter /Library/Printers/Samsung/UPD/Filters/prefilter-duplex (PID 4606)
D [Job 178] argv[0]="Samsung_M2026W_Duplex"
...
E [Job 178] No pages found!
E [Job 178] Nie można otworzyć „/private/var/spool/cups/tmp/011ff6ad29648”.
D [Job 178] PID 4607 (/usr/libexec/cups/filter/cgpdftoraster) stopped with status 3.
```

### 2. Przyczyna źródłowa: Specyfikacja argumentów filtrów CUPS
W architekturze podsystemu CUPS, gdy `cupsd` uruchamia proces filtra (`fork` + `execve`):
* `argv[0]` **nie zawiera nazwy pliku wykonywalnego**, lecz **nazwę kolejki drukarki** (`Samsung_M2026W_Duplex`)!
* Ponieważ pierwsza wersja wrappera badała `basename(argv[0])`, nie znalazła słowa `prefilter`, wpadła w gałąź domyślną i uruchomiła `rastertosec` zamiast `prefilter`!
* W efekcie `cgpdftoraster` otrzymał pusty strumień danych wejściowych i zgłosił błąd `No pages found!`.

### 3. Zastosowane rozwiązanie:
1. **Dedykowane makro kompilacji `-DTARGET_FILTER`:**
   Kompilujemy dwa oddzielne, dedykowane pliki wykonywalne:
   * `prefilter-duplex` ze sztywno zakodowaną ścieżką do `/Library/Printers/Samsung/UPD/Filters/prefilter`.
   * `rastertosec-duplex` ze sztywno zakodowaną ścieżką do `/Library/Printers/Samsung/UPD/Filters/rastertosec`.
2. **Dodatkowa detekcja via `_NSGetExecutablePath()`:**
   W kodzie C dodano odczyt faktycznej ścieżki procesu przez natywne API macOS `_NSGetExecutablePath()`, uniezależniając wrapper od wartości `argv[0]`.
3. Anulowano zakleszczone zadanie 178 poleceniem `cancel 178`.

