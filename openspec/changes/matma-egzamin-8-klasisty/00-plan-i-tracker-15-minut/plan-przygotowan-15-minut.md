# Plan i tracker: jedna karta dziennie

**Wersja 2.** Poprzednia wersja (tracker 140 sesji z Kartami Supermocy HTML i quizami 4-kartowymi) jest w `wersja-1/`.

---

## Zasada

**Jedna karta dziennie.** Każda karta to jeden cel z kartkówki lub działu. Karta = 1 strona A4, arkusz = 1 strona A4 (5 minut), klucz dla rodzica/trenera.

## Rytuał 15 minut

| Minuty | Co robimy |
| :---: | :--- |
| **1–3** | **Karta dnia.** Czytamy regułę i oglądamy ilustrację. Druga droga do wyniku: sprawdzamy, czy się zgadza. |
| **4–10** | **Arkusz (5 minut, 6 pkt).** Nadia rozwiązuje sama. Bez zaglądania do karty. |
| **11–15** | **Klucz i poprawa.** Sprawdzamy wynik, zaznaczamy rangę, czytamy pułapkę. Zamykamy zeszyt w 15. minucie. |

## Bezpiecznik

1. **Zakaz kumulacji.** Po przerwie wracamy do jednej karty. Nie robimy dwóch kart za jednym razem.
2. **Chwalimy proces.** Zaznaczamy punkty cząstkowe, np. *„Samo zamienienie minut na godziny to już pewny punkt.”*
3. **Nie zgadujemy.** Najpierw skracaj ułamek, najpierw rozpisz okres, najpierw dopisz zera.

---

## Tracker: kolejność kart

Każdy dzień to jedna karta. Zaznacz `[x]` po zakończeniu bloku 15 minut.

### Blok A: ułamki (`01-liczby-i-ulamki`) — gotowe

| Dzień | Karta | Cel | Status |
| :--- | :--- | :--- | :---: |
| Dzień 1 | `01-liczby-i-ulamki/karty/1-odwrotnosc` | Odwrotność czy liczba przeciwna | `[ ]` |
| Dzień 2 | `01-liczby-i-ulamki/karty/2-skonczone-nieskonczone` | Rozwinięcia skończone czy nieskończone | `[ ]` |
| Dzień 3 | `01-liczby-i-ulamki/karty/3-porownywanie` | Porównywanie ułamków | `[ ]` |
| Dzień 4 | `01-liczby-i-ulamki/karty/4-zaokraglanie` | Zaokrąglanie (mur i policjant) | `[ ]` |
| Dzień 5 | `12-zadania-tekstowe-predkosc-droga-czas/karty/1-minuty-na-godziny` | Minuty na godziny w ułamku dziesiętnym | `[ ]` |

### Blok B: pozostałe działy — do wygenerowania

Każdy dział trzeba rozbić na cele (karty). Nie generujemy całego działu naraz.

| Dział | Folder | Status |
| :--- | :--- | :--- |
| 01 | `01-liczby-i-ulamki` | część: 4 karty z 5+ celów (liczby podzielne, rzymskie, całkowite — do zrobienia) |
| 02 | `02-potegi` | do zrobienia |
| 03 | `03-pierwiastki` | do zrobienia |
| 04 | `04-procenty` | do zrobienia |
| 05 | `05-wyrazenia-algebraiczne` | do zrobienia |
| 06 | `06-rownania` | do zrobienia |
| 07 | `07-trojkaty-katy-pitagoras` | do zrobienia |
| 08 | `08-czworokaty-i-pola` | do zrobienia |
| 09 | `09-uklad-wspolrzednych` | do zrobienia |
| 10 | `10-geometria-przestrzenna` | do zrobienia |
| 11 | `11-rachunek-prawdopodobienstwa-i-statystyka` | do zrobienia |
| 12 | `12-zadania-tekstowe-predkosc-droga-czas` | część: 1 karta (minuty na godziny) |
| 13 | `13-okrag-i-kolo-liczba-pi` | do zrobienia |
| 14 | `14-dowodzenie-i-zadania-otwarte-cke` | do zrobienia |
| 15 | `15-mikro-arkusze-egzaminacyjne-cke` | do zrobienia |

---

## Struktura folderu działu

```
NN-nazwa-dzialu/
├── preambula.tex      # wspólny szablon (A4, ramki, nagłówek karty)
├── build.sh           # kompiluje karty i quizy, sprawdza 1 stronę A4
├── karty/             # jedna karta = jeden cel
└── quizy/             # arkusz i klucz na każdą kartę
```

Kompilacja: `brew install tectonic`, potem `./build.sh` w folderze działu.
