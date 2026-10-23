# Plan Wdrożeniowy OpenSpec (`tasks.md`): System Przygotowań do Egzaminu Ósmoklasisty („Mikro-Sprinty 15 Minut”)

**Kod Zmiany**: `matma-egzamin-8-klasisty`  
**Data**: 18 Października 2026 (aktualizacja v2: 19 Października 2026)  
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

## Faza 1: Plan i Tracker v2 (`00-plan-i-tracker-15-minut`)

- [x] **1.1: Zasada „jedna karta dziennie” i tracker kart**
  - **Ścieżka**: `openspec/changes/matma-egzamin-8-klasisty/00-plan-i-tracker-15-minut/plan-przygotowan-15-minut.md`
  - **Kryteria akceptacji**: tabela kart w kolejności (dzień → karta), lista działów do wygenerowania, rytuał 15 minut (karta 3 min, arkusz 7 min, klucz 5 min).
- [ ] **1.2: PDF trackera w LaTeX** (1–2 strony A4)
  - **Kryteria akceptacji**: `build.sh` w folderze `00` daje plik PDF z liczbą stron równą 1 lub 2.

---

## Faza 2: Dział `01-liczby-i-ulamki` (v2)

- [x] **2.1: Karty, arkusze i klucze** dla celów: odwrotność, rozwinięcia skończone i nieskończone, porównywanie, zaokrąglanie (mur i policjant). Wariant B zaokrąglania (pieniądze i połowa) ma kartę `4b`, bez arkusza.
  - **Ścieżki**: `01-liczby-i-ulamki/karty/*.tex`, `01-liczby-i-ulamki/quizy/*.tex`
  - **Kryteria akceptacji**: każdy cel ma kartę, arkusz i klucz. Karta `4b` ma jeszcze arkusz do dopisania (zadanie 2.4). Każdy PDF ma 1 stronę.
- [x] **2.2: Kontrola formatu** (`build.sh`, `preambula.tex`, okresy w nawiasie)
  - **Komenda weryfikująca**: `cd 01-liczby-i-ulamki && ./build.sh`
- [ ] **2.4: Arkusz i klucz dla wariantu B zaokrąglania** (`karty/4b-zaokraglanie-polowa.tex`)
  - **Ścieżki**: `01-liczby-i-ulamki/quizy/4b-arkusz.tex`, `01-liczby-i-ulamki/quizy/4b-klucz.tex`
- [ ] **2.3: Cele brakujące w dziale:** liczby podzielne (NWD, NWW), liczby rzymskie, liczby całkowite (dodawanie i odejmowanie), zapis ułamka jako wielokrotności.
  - **Kryteria akceptacji**: każdy nowy cel ma kartę, arkusz i klucz zgodnie z §3.1 `design.md`.

---

## Faza 3: Dział `12-zadania-tekstowe-predkosc-droga-czas` (v2)

- [x] **3.1: Minuty na godziny** (karta, arkusz, klucz)
  - **Ścieżka**: `12-zadania-tekstowe-predkosc-droga-czas/karty/1-minuty-na-godziny.tex`
- [ ] **3.2: Pozostałe cele działu** (proporcjonalność prosta, podział proporcjonalny, $s=v\cdot t$, skala)
  - **Kryteria akceptacji**: każdy cel ma kartę, arkusz i klucz.

---

## Faza 4: Pozostałe działy (v2)

Każdy dział powstaje w osobnym kroku, zgodnie z §3.1 `design.md`. Kolejność: najpierw działy z planu w tygodniach 9–16 (potęgi, pierwiastki, wyrażenia, równania), potem geometria i statystyka.

- [ ] **4.1: `02-potegi`** (cele: prawa potęg, rozbicie podstawy, notacja $a\cdot 10^k$)
- [ ] **4.2: `03-pierwiastki`** (cele: pierwiastki, wyłączanie czynnika, szacowanie)
- [x] **4.3: `04-procenty`** (4 karty: procent z liczby, jaki to procent i całość, obniżki i podwyżki, punkty procentowe; każda z arkuszem i kluczem)
- [ ] **4.4: `05-wyrazenia-algebraiczne`** (cele: redukcja wyrazów, mnożenie nawiasów, pułapka minusa)
- [ ] **4.5: `06-rownania`** (cele: równania 1. stopnia, likwidacja ułamków, zadania tekstowe)
- [ ] **4.6: `07-trojkaty-katy-pitagoras`** (cele: kąty, trójkąty, Pitagoras, trójki pitagorejskie)
- [ ] **4.7: `08-czworokaty-i-pola`** (cele: pola wielokątów, wysokość, jednostki pola)
- [ ] **4.8: `09-uklad-wspolrzednych`** (cele: oś liczbowa, środek odcinka, odległości)
- [ ] **4.9: `10-geometria-przestrzenna`** (cele: graniastosłupy, ostrosłupy, siatki, objętość)
- [ ] **4.10: `11-rachunek-prawdopodobienstwa-i-statystyka`** (cele: średnia, wykresy, prawdopodobieństwo)
- [ ] **4.11: `13-okrag-i-kolo-liczba-pi`** (cele: długość okręgu, pole koła)
- [ ] **4.12: `14-dowodzenie-i-zadania-otwarte-cke`** (cele: dowody, przekształcanie wzorów)
- [ ] **4.13: `15-mikro-arkusze-egzaminacyjne-cke`** (cele: 6 odcinków po 15 minut, klucz punktacji)

---

## Faza 5: Walidacja i Indeks

- [ ] **5.1: Walidacja stron:** `build.sh` we wszystkich działach kończy się sukcesem.
- [ ] **5.2: `README.md` na poziomie zmiany:** kolejność działów, stan każdego działu, instrukcja drukowania.
