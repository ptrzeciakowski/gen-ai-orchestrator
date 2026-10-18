# Plan Wdrożeniowy OpenSpec (`tasks.md`): System Przygotowań do Egzaminu Ósmoklasisty („Mikro-Sprinty 15 Minut”)

**Kod Zmiany**: `matma-egzamin-8-klasisty`  
**Data**: 18 Października 2026  
**Dokumenty Bazy**: [`proposal.md`](./proposal.md), [`design.md`](./design.md), [`explore/001-matma-egzamin-8-klasisty-01.md`](./explore/001-matma-egzamin-8-klasisty-01.md)

---

## Faza 0: Eksploracja, Pobranie Źródeł CKE/GWO i Projekt Architektury (Ukończone)

- [x] **Zadanie 0.1: Pobranie wzorcowego podręcznika GWO i skryptu ekstrakcji**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/explore/download_gwo_book.py`
    - `openspec/changes/matma-egzamin-8-klasisty/explore/Matematyka-z-plusem-6-Podrecznik.pdf`
    - `openspec/changes/matma-egzamin-8-klasisty/explore/Matematyka-z-plusem-6-Podrecznik-textual-pages.json`
  - **Kryteria akceptacji**: Pobrany komplet 284 stron z 1-sekundowym opóźnieniem, złożony bezstratnie w pojedynczy plik PDF wraz z warstwą tekstową JSON.
  - **Komenda weryfikująca**: `ls -lh openspec/changes/matma-egzamin-8-klasisty/explore/`

- [x] **Zadanie 0.2: Pobranie i ekstrakcja Podstawy Programowej CKE 2024 (`D20240996.pdf`, str. 182–196)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/explore/D20240996-podstawa-programowa-2024.pdf`
    - `openspec/changes/matma-egzamin-8-klasisty/explore/001-matma-egzamin-8-klasisty-01.md`
    - `openspec/changes/matma-egzamin-8-klasisty/proposal.md`
    - `openspec/changes/matma-egzamin-8-klasisty/design.md`
  - **Kryteria akceptacji**: Pełne mapowanie działów klas IV–VI oraz VII–VIII na 15-minutowe bloki z wykluczeniem zagadnień nieobowiązujących (Dział XV Symetrie kl. VII–VIII, wzory skróconego mnożenia, usuwanie niewymierności, tw. odwrotne do Pitagorasa, wycinki kołowe).

---

## Faza 1: Master-Plan 28 Tygodni i Drukowalny Tracker 15-Minutówek (`00-plan-i-tracker-15-minut`)

- [ ] **Zadanie 1.1: Utworzenie Mapy Przygody Egzaminacyjnej (Tracker 140 Sesji po 15 minut) oraz Przewodnika Pedagogicznego (`3 + 7 + 5 min`)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/00-plan-i-tracker-15-minut/plan-przygotowan-15-minut.md`
    - `openspec/changes/matma-egzamin-8-klasisty/00-plan-i-tracker-15-minut/plan-przygotowan-15-minut.html`
    - `openspec/changes/matma-egzamin-8-klasisty/00-plan-i-tracker-15-minut/plan-przygotowan-15-minut.pdf`
  - **Kryteria akceptacji**:
    - Dokument zawiera rozkład 28 tygodni (4 Fazy, Moduły `01`–`15`) z polami wyboru dla 5 sesji tygodniowo (`Poniedziałek` – `Piątek` + opcjonalna `Sobota`),
    - Zawiera instrukcję prowadzenia pojedynczego bloku 15-minutowego (`3 min Rozgrzewka Kotwiczna + 7 min Sprint Zadaniowy + 5 min Audyt Detektywa`) oraz zasady *Bezpiecznika Anty-Stresowego*,
    - Wygenerowany plik PDF mieści się dokładnie na **2 stronach A4** (Strona 1: Wizualny Tracker 140 sesji na ścianę/biurko; Strona 2: Harmonogram 28 tygodni i ściągawka metodyczna dla rodzica).
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/00-plan-i-tracker-15-minut/plan-przygotowan-15-minut.html`

---

## Faza 2: Migracja i Konsolidacja Sprawdzonych Pakietów Bazowych (`01`–`09`)

- [ ] **Zadanie 2.1: Skopiowanie i weryfikacja pakietów `01`–`09` z archiwum `2026-09-12-2052-matematyka-dla-nadii`**
  - **Ścieżki katalogów**:
    - `openspec/changes/matma-egzamin-8-klasisty/01-liczby-i-ulamki/`
    - `openspec/changes/matma-egzamin-8-klasisty/02-potegi/`
    - `openspec/changes/matma-egzamin-8-klasisty/03-pierwiastki/`
    - `openspec/changes/matma-egzamin-8-klasisty/04-procenty/`
    - `openspec/changes/matma-egzamin-8-klasisty/05-wyrazenia-algebraiczne/`
    - `openspec/changes/matma-egzamin-8-klasisty/06-rownania/`
    - `openspec/changes/matma-egzamin-8-klasisty/07-trojkaty-katy-pitagoras/`
    - `openspec/changes/matma-egzamin-8-klasisty/08-czworokaty-i-pola/`
    - `openspec/changes/matma-egzamin-8-klasisty/09-uklad-wspolrzednych/`
  - **Kryteria akceptacji**:
    - Każdy z 9 katalogów zawiera komplet 6 plików: `karta-supermocy-cheat-sheet.{md,html,pdf}` (1 strona A4) oraz `quizy-sukcesu-5-minut.{md,html,pdf}` (3 strony A4),
    - Walidacja przez `PDFDocument` potwierdza brak przepełnienia stron.
  - **Komenda weryfikująca**:
    `ls -1 openspec/changes/matma-egzamin-8-klasisty/0{1..9}-*/*.pdf | wc -l` *(oczekiwane: 18 plików PDF)*

---

## Faza 3: Wygenerowanie Brakujących Pakietów Działowych Kl. VII–VIII (`10`, `11`, `12`)

- [ ] **Zadanie 3.1: Pakiet `10-geometria-przestrzenna` (Graniastosłupy i Ostrosłupy z Pitagorasem – Dział XI kl. VII–VIII)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/10-geometria-przestrzenna/karta-supermocy-cheat-sheet.{md,html,pdf}`
    - `openspec/changes/matma-egzamin-8-klasisty/10-geometria-przestrzenna/quizy-sukcesu-5-minut.{md,html,pdf}`
  - **Kryteria akceptacji**:
    - *Karta Supermocy (1 str. A4)*: Złota tabela krawędzi/wierzchołków/ścian ($3n, 2n, n+2$ vs $2n, n+1, n+1$), wzory na pole powierzchni i objętość ($V = P_p \cdot H$ vs $V = \frac{1}{3}P_p \cdot H$), wyciąganie trójkąta prostokątnego z wnętrza bryły (Pitagoras w graniastosłupie i ostrosłupie jak w przykładach ze str. 192–193 `D20240996.pdf`), kotwica jednostek pojemności ($1\text{ l} = 1\text{ dm}^3 = 1000\text{ cm}^3$).
    - *Quizy Sukcesu (3 str. A4)*: 4 karty 5-minutowe (12 zadań, w tym zadania egzaminacyjne z siatkami, trójkątem $45^\circ-45^\circ-90^\circ$ w ścianie bocznej i ostrosłupem z trójką 5-12-13) + wskazówki w stylu GWO + klucz odpowiedzi.
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/10-geometria-przestrzenna/karta-supermocy-cheat-sheet.html`

- [ ] **Zadanie 3.2: Pakiet `11-rachunek-prawdopodobienstwa-i-statystyka` (Średnia, Wykresy, Kombinatoryka i Szanse – Działy XII–XIII kl. VII–VIII)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/11-rachunek-prawdopodobienstwa-i-statystyka/karta-supermocy-cheat-sheet.{md,html,pdf}`
    - `openspec/changes/matma-egzamin-8-klasisty/11-rachunek-prawdopodobienstwa-i-statystyka/quizy-sukcesu-5-minut.{md,html,pdf}`
  - **Kryteria akceptacji**:
    - *Karta Supermocy (1 str. A4)*: Złoty Trik Sumy przy Średniej ($\text{Suma} = \text{Średnia} \times n$ – zadania z dopisaniem/usunięciem elementu), czytanie diagramów kołowych i słupkowych, wzór $P(A) = \frac{\text{sprzyjające}}{\text{wszystkie}}$, tabela $6 \times 6$ dla dwóch rzutów kostką, drzewko monety i losowanie kul.
    - *Quizy Sukcesu (3 str. A4)*: 4 karty 5-minutowe + wskazówki GWO + klucz odpowiedzi.
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/11-rachunek-prawdopodobienstwa-i-statystyka/karta-supermocy-cheat-sheet.html`

- [ ] **Zadanie 3.3: Pakiet `12-zadania-tekstowe-predkosc-droga-czas` (Proporcjonalność Prosta, Podział Proporcjonalny, $s=v\cdot t$, Zegar i Skala – Dział VII kl. VII–VIII + Dział XII kl. IV–VI)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/12-zadania-tekstowe-predkosc-droga-czas/karta-supermocy-cheat-sheet.{md,html,pdf}`
    - `openspec/changes/matma-egzamin-8-klasisty/12-zadania-tekstowe-predkosc-droga-czas/quizy-sukcesu-5-minut.{md,html,pdf}`
  - **Kryteria akceptacji**:
    - *Karta Supermocy (1 str. A4)*: Trójkąt $s / v \cdot t$, przelicznik $\text{km/h} \leftrightarrow \text{m/s}$ ($\div 3{,}6$ i $\times 3{,}6$), Złoty Przelicznik Zegara ($0{,}1\text{ h} = 6\text{ min}$, $\frac{1}{4}\text{ h} = 15\text{ min}$, $\frac{1}{5}\text{ h} = 12\text{ min}$), podział proporcjonalny metodą „Woreczków” ($a:b$), skala mapy i pułapka skali pola powierzchni ($k^2$).
    - *Quizy Sukcesu (3 str. A4)*: 4 karty 5-minutowe + wskazówki GWO + klucz odpowiedzi.
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/12-zadania-tekstowe-predkosc-droga-czas/karta-supermocy-cheat-sheet.html`

---

## Faza 4: Domknięcie Pełnej Podstawy CKE 2024 (`13`, `14`, `15`)

- [ ] **Zadanie 4.1: Pakiet `13-okrag-i-kolo-liczba-pi` (Długość Okręgu i Pole Koła – Dział XIV kl. VII–VIII)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/13-okrag-i-kolo-liczba-pi/karta-supermocy-cheat-sheet.{md,html,pdf}`
    - `openspec/changes/matma-egzamin-8-klasisty/13-okrag-i-kolo-liczba-pi/quizy-sukcesu-5-minut.{md,html,pdf}`
  - **Kryteria akceptacji**:
    - *Karta Supermocy (1 str. A4)*: Odróżnienie okręgu (obręcz, $L = 2\pi r = \pi d$) od koła (tarcza pizzy, $P = \pi r^2$), szybkie cofanie wzoru ($P = 49\pi \implies r = 7 \implies d = 14$), obwody i pola figur złożonych (stadion/bieżnia = prostokąt + dwa półkola = prostokąt + 1 pełne koło!), antypułapka średnicy vs promienia.
    - *Quizy Sukcesu (3 str. A4)*: 4 karty 5-minutowe + wskazówki GWO + klucz odpowiedzi.
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/13-okrag-i-kolo-liczba-pi/karta-supermocy-cheat-sheet.html`

- [ ] **Zadanie 4.2: Pakiet `14-dowodzenie-i-zadania-otwarte-cke` (Dowody Geometryczne i Algebraiczne, Przekształcanie Wzorów i Notacja Wykładnicza – Uzupełnienie CKE 2024)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/14-dowodzenie-i-zadania-otwarte-cke/karta-supermocy-cheat-sheet.{md,html,pdf}`
    - `openspec/changes/matma-egzamin-8-klasisty/14-dowodzenie-i-zadania-otwarte-cke/quizy-sukcesu-5-minut.{md,html,pdf}`
  - **Kryteria akceptacji**:
    - *Karta Supermocy (1 str. A4)*: Szablon 3 Kroków Dowodu Algebraicznego (kolejne liczby naturalne $n, n+1, n+2$, parzyste $2n$, nieparzyste $2n+1$, wyłączanie czynnika przed nawias), Szablon Dowodu Geometrycznego (kąty w trójkącie równoramiennym i cechy przystawania trójkątów – dokładnie pod przykłady ze str. 191 `D20240996.pdf`), przekształcanie wzorów metodą Liczby-Atrapy ($6 = 2 \cdot 3$), notacja wykładnicza $a \cdot 10^k$.
    - *Quizy Sukcesu (3 str. A4)*: 4 karty 5-minutowe + wskazówki GWO + klucz odpowiedzi.
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/14-dowodzenie-i-zadania-otwarte-cke/karta-supermocy-cheat-sheet.html`

- [ ] **Zadanie 4.3: Pakiet `15-mikro-arkusze-egzaminacyjne-cke` (Wzorcowy Arkusz Egzaminu Ósmoklasisty CKE Podzielony na 6 Bloków po 15 Minut)**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/15-mikro-arkusze-egzaminacyjne-cke/mikro-arkusz-egzaminacyjny-6x15min.{md,html,pdf}`
    - `openspec/changes/matma-egzamin-8-klasisty/15-mikro-arkusze-egzaminacyjne-cke/klucz-i-wskazowki-mikro-arkusza.{md,html,pdf}`
  - **Kryteria akceptacji**:
    - Kompletny arkusz 21 zadań (15 zamkniętych + 6 otwartych = 45 pkt wg aktualnej struktury CKE) rozpisany na **6 dziennych odcinków po 15 minut (Dzień 1–6)**,
    - Osobny plik z **Wskazówkami Detektywa (styl GWO)** (1 zdanie podpowiedzi przed spojrzeniem w rozwiązanie) oraz **Kluczem Punktacji Cząstkowej CKE** (za co przyznawany jest każdy pojedynczy punkt w zadaniach otwartych 16–21).
  - **Komenda weryfikująca**:
    `python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py openspec/changes/matma-egzamin-8-klasisty/15-mikro-arkusze-egzaminacyjne-cke/mikro-arkusz-egzaminacyjny-6x15min.html`

---

## Faza 5: Globalna Walidacja PDFKit i Indeks Główny (`README.md`)

- [ ] **Zadanie 5.1: Automatyczna weryfikacja liczby stron A4 wszystkich wygenerowanych plików PDF oraz utworzenie `README.md`**
  - **Ścieżki plików**:
    - `openspec/changes/matma-egzamin-8-klasisty/README.md`
  - **Kryteria akceptacji**:
    - Wszystkie 14 plików `karta-supermocy-cheat-sheet.pdf` w katalogach `01`–`14` mają dokładnie **1 stronę A4** (`pageCount == 1`),
    - Wszystkie 14 plików `quizy-sukcesu-5-minut.pdf` w katalogach `01`–`14` mają dokładnie **3 strony A4** (`pageCount == 3`),
    - Plik `README.md` zawiera klikalną tabelę wszystkich 16 modułów (`00`–`15`) z bezpośrednimi linkami do plików `.md`, `.html` i `.pdf`.
  - **Komenda weryfikująca**:
    Skrypt Swift `PDFDocument` weryfikujący liczbę stron wszystkich plików PDF w `openspec/changes/matma-egzamin-8-klasisty/`.
