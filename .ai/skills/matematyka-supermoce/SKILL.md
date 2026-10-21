---
name: matematyka-supermoce
description: >-
  Przygotowuje Kartę Supermocy (jednostronicowy cheat-sheet A4 z mnemotechnikami i sprytnymi metodami) oraz 5-minutowe Quizy Sukcesu (karty mikro-treningu budujące pewność siebie) z matematyki na podstawie podanego zakresu materiału (zadania z podręcznika/ćwiczeń lub opis zagadnienia, np. potęgi, pierwiastki, ułamki, algebra, geometria). Generuje pliki Markdown oraz profesjonalne, gotowe do druku pliki PDF A4 za pomocą silnika headless Chrome (bez plików DOCX).
---

# Matematyka Supermoce & Quizy Sukcesu (Klasy 7–8 i Egzamin Ósmoklasisty)

## Overview (Przegląd)

Skill służy do transformacji dowolnego materiału matematycznego ze szkoły podstawowej (klasy 7–8 oraz przygotowanie do egzaminu ósmoklasisty) w ultra-efektywne, przyjazne poznawczo materiały dydaktyczne dla uczniów z niską tolerancją na znużenie, trudnościami w dłuższej koncentracji lub lękiem przed żmudnymi obliczeniami.

Zamiast monotonnego liczenia "pod kreską" i setek powtarzalnych słupków, skill wdraża metodykę **"Sprytu Matematycznego" (Cheat Codes)**, dekompozycję na mikro-kroki oraz gamifikowane, 5-minutowe sprinty sukcesu.

Format wyjściowy to **źródło LaTeX oraz gotowy do druku PDF na A4** (brak formatu DOCX). Zapisy matematyczne zawsze w składni LaTeX.

---

## 🎯 Filozofia Neurodydaktyczna

1. **Format "Sprint 15 minut" (Zasada Mikro-przerw)**:
   - 12 minut dynamicznej pracy na 2–3 zadaniach + 3 minuty pełnego resetu fizycznego.
   - W przypadku kartkówek: format **5 minut na jedną kartę dziennie** (budowanie nawyku sukcesu bez oporu poznawczego).
2. **Koncepcja Trzech Ścieżek (Wybór Najprostszej)**:
   - **Ścieżka A (Cheat Code / Spryt matematyczny)**: Rozszerzanie ułamków, prawa potęg, rozbijanie podstawy, dopełnienia do całości. Obliczenie w 5–10 sekund!
   - **Ścieżka B (Klasyczny Algorytm)**: Dzielenie pisemne / schemat ogólny – ostateczność dla trudnych przypadków.
   - **Ścieżka C (Życiowa / Wizualna)**: Pieniądze (zł/gr), pizza, zegar, oś liczbowa, schemat muru.
3. **Odciążenie Pamięci Roboczej**:
   - Każda karta supermocy zawiera "Złotą Tabelę Kotwiczną" (np. *Klub Przyjaciół 100/1000*, *Trójki Pitagorejskie*, *Prawa Potęg*). Uczeń nie musi zgadywać w pamięci.

---

## 📥 Dwa Tryby Wprowadzania Materiału

Skill potrafi przetworzyć materiał wejściowy podany w dowolny sposób:

1. **Tryb Źródłowy (Zadania z podręcznika / zbioru zadań)**:
   - Użytkownik podaje np.: *"Zadania 4, 5, 6 str. 11 z Matematyki 7 z plusem GWO"*.
   - Agent weryfikuje treść zadań (z bazy materiałów lub web), identyfikuje punkty zapalne (pułapki) i rozpisuje je na mikro-kroki.
2. **Tryb Konceptualny ("Słowno-muzyczny")**:
   - Użytkownik podaje np.: *"Potęgowanie dla klas 7"*, *"Działania na pierwiastkach pod egzamin ósmoklasisty"*, *"Równania z ułamkami"*.
   - Agent automatycznie dobiera wzorcowy kanon CKE, typowe zadania egzaminacyjne i konstruuje pełen zestaw materiałów.

---

## 📦 Standard Generowanych Artefaktów

Każdy materiał powstaje jako **źródło LaTeX → PDF A4** (kompilacja przez `tectonic`). Markdown ani HTML nie są już generowane, chyba że użytkownik o nie poprosi.

```
katalog-tematu/
├── preambula.tex                 # wspólny szablon: A4, ramki reguła/pułapka, nagłówek karty
├── karty/
│   ├── 1-<cel>.tex / .pdf        # karta supermocy: JEDEN cel, 1 strona A4
│   └── ...
├── quizy/
│   ├── 1-arkusz.tex / .pdf       # 5-minutowy arkusz dla ucznia, 1 strona A4
│   ├── 1-klucz.tex / .pdf        # klucz + wskazówki dla rodzica/trenera (nie drukować dla ucznia)
│   └── ...
├── build.sh                      # kompiluje wszystko i sprawdza, czy każdy PDF ma 1 stronę
└── README.md                     # kolejność kart, instrukcja wydruku
```

> **Zasada: jeden cel = jedna karta = jeden arkusz = jeden klucz.** Nie łącz celów na jednej karcie. Jeśli cel nie mieści się na stronie, dziel go na mniejsze cele, a nie zmniejszaj czcionki.

> ⚠️ **ZAKAZ GENEROWANIA DOCX**: NIE generujemy plików `.docx` ani `.odt`.

---

### 1. Karta Supermocy (1 cel = 1 strona A4)

Struktura każdej karty, w tej kolejności:
1. **Cel** w jednym zdaniu (nagłówek: `\naglowekKarty{N}{Tytuł}{cel}`).
2. **Reguła** w ramce (`\begin{regula}[REGUŁA]`), z zapisem wzorem.
3. **Druga droga do tego samego wyniku**, np. rozkład mianownika ↔ dzielenie pod kreską, dzielenie przez 60 ↔ klocki czasu, motylek ↔ oś liczbowa, sprawdzenie iloczynem. Karta pokazuje, że obie drogi dają ten sam wynik.
4. **Ilustracja** (TikZ, obowiązkowa): oś liczbowa, schemat dzielenia pod kreską, tarcza zegara, mur i policjant. Ilustracje są kluczowe dla ucznia.
5. **Przykłady rozstrzygnięte** (2–4 w tabeli lub wypunktowaniu).
6. **Pułapki z kartkówki** (`\begin{pulapka}`, 2–4 pozycje).

Zasady techniczne:
- Każdy plik zaczyna się od `\documentclass[11pt,a4paper]{article}` i `\input{../preambula}`.
- Zapisy w LaTeX: `$...$`, `\dfrac`, okres zapisuj w nawiasie, np. `0{,}(3)` (nie `\overline`), `\text{}` dla jednostek.
- **Ułamki piętrowe nie mogą nachodzić na siebie.** Ułamki `\dfrac` w tabelach (`tabular`) i w tekście powiększają wiersz, więc przy domyślnym odstępie licznik jednego wiersza zachodzi na mianownik poprzedniego. Zasady:
  - W każdej tabeli z ułamkami ustaw `\renewcommand{\arraystretch}{1.6}` lub więcej, a przy ułamkach w kilku kolumnach jednocześnie dodaj `\\[6pt]` po wierszu.
  - Ułamki w tabelach i zdaniach zapisuj konsekwentnie: `\dfrac` (powiększone) albo `\frac` (małe), nie mieszaj obu w jednym wierszu.
  - Ułamek w ciągłym tekście, który ma nie rozpychać linii, zapisuj `\frac`, a nie `\dfrac`.
  - Po kompilacji **obejrzyj PDF** (np. `sips -s format png plik.pdf --out plik.png`) i sprawdź, czy żaden ułamek, indeks ani linia ułamkowa nie nachodzi na sąsiedni wiersz lub kolumnę. Jeśli zwiększenie odstępu wypycha treść na drugą stronę, skróć treść, nie zmniejszaj odstępu poniżej `1.6`.
- Kolory i ramki pochodzą z `preambula.tex`. Nie definiuj ich lokalnie.
- Wcześniejsze „moduły" (Klub Przyjaciół, Mur i Policjant, zasada pizzy) to treści przykładów i pułapek, a nie osobne sekcje.

---

### 2. Quizy Sukcesu (arkusz + klucz na każdą kartę)

Dla każdej karty powstają **dwa pliki**: arkusz i klucz.

**Arkusz dla ucznia** (`quizy/N-arkusz.tex`), 1 strona A4:
- Nagłówek: cel, czas (5 minut), pola Imię / Data / Punkty.
- **3 zadania po 2 pkt** (razem 6 pkt), wszystkie **otwarte**:
  - *Zadanie 1 (Rozgrzewka)*: proste obliczenie lub uzupełnienie luki z wynikiem policzonym przez ucznia.
  - *Zadanie 2 (Zastosuj supermoc)*: trik z karty w konkretnym obliczeniu.
  - *Zadanie 3 (Pułapka / zagadka)*: typowe zadanie z kartkówki lub egzaminu ósmoklasisty.
- **Zakaz zadań testowych**: w arkuszach nie ma zadań zamkniętych, czyli wyboru A/B/C/D, Prawda/Fałsz, S/N, łączenia w pary ani zaznaczania odpowiedzi. Zadania testowe wolno dodać **wyłącznie wtedy, gdy operator / nauczyciel wprost o nie poprosi**. Bez takiej prośby zawsze zadania otwarte.
- **Pokaż obliczenia**: w KAŻDYM zadaniu jest polecenie „Pokaż obliczenia." (lub równoważne, np. „Zapisz tok rozumowania."). Sama odpowiedź bez obliczeń nie daje pełnej liczby punktów, co zapisz w nagłówku arkusza.
- **Układ strony**: zadania wypełniają **całą stronę A4**, a nie tylko jej górną część. Pomiędzy zadaniami (i pod ostatnim) zostaw puste miejsce na obliczenia, czyli wolną przestrzeń w ramce lub z delikatną kratką (np. `\vspace{...}`, `\vfill` między zadaniami lub `\framebox`/`tikz` z kratką). Miejsce dobierz do złożoności zadania, aby uczeń zmieścił cały zapis. Po wygenerowaniu sprawdź w PDF, że strona nie jest w połowie pusta i że nie wyszła poza 1 stronę.
- Linie do wpisywania odpowiedzi końcowej: `\rule{3cm}{0.4pt}`.
- Puste miejsce **wewnątrz ułamka** zapisuj jako `\square`, np. `\dfrac{\square}{5}`. Pozioma kreska w mianowniku wygląda jak kreska ułamkowa i zmyla ucznia.
- Pasek rang z checkboxami: 5–6 pkt, 3–4 pkt, 1–2 pkt.

**Klucz** (`quizy/N-klucz.tex`), 1 strona A4:
- Rozwiązania krok po kroku (pełne obliczenia, takie jak uczeń ma pokazać), z zaznaczonymi poprawnymi odpowiedziami.
- Ramka `title=Wskazówka dla Pawła` (lub rodzica/trenera): jak chwalić proces i jak reagować na typowe błędy.
- Nagłówek oznaczony „nie drukować dla ucznia".

**Zasada dnia:** maksymalnie 1 arkusz (5 minut) dziennie.

---

### Kompilacja i kontrola

```bash
brew install tectonic   # raz
./build.sh              # kompiluje karty/ i quizy/, odrzuca PDF-y dłuższe niż 1 strona
```

- `build.sh` przerywa pracę, jeśli którykolwiek PDF ma więcej niż 1 stronę. Wtedy skracaj treść albo dziel cel.
- Czcionka: ustaw w `preambula.tex` przez `fontspec`. Systemowa czcionka (np. Arial z `/System/Library/Fonts`) działa tylko na tym komputerze, więc przed przeniesieniem projektu zmień ją na czcionkę dołączoną do projektu.
- Po kompilacji usuń `*.log` i `*.xdv`.

---

## 🛠️ Generator PDF z HTML (`scripts/generate_pdf.py`) — tylko starszy format

Skrypt renderuje HTML przez Google Chrome headless. **Nie używaj go dla kart i quizów w LaTeX.** Zostaje do ewentualnych starszych materiałów w HTML:

```bash
python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py <sciezka_do_pliku.html> [-o <sciezka_do_wyjscia.pdf>]
```

---

## 🗺️ Mapa Działów pod Egzamin Ósmoklasisty (CKE)

Gdy użytkownik poprosi o przygotowanie materiałów dla pełnego egzaminu ósmoklasisty, generujemy pakiety według poniższego kanonu:

| Nr | Kod Działu | Temat Wiodący | Kluczowa Supermoc |
| :---: | :--- | :--- | :--- |
| **01** | `01-liczby-ulamki` | Ułamki zwykłe i dziesiętne | Klub Przyjaciół 100/1000, kieszonki, mur i policjant |
| **02** | `02-potegi` | Potęgi o podstawach naturalnych | Rozkładanie podstawy ($6^8 = 2^8 \cdot 3^8$), dodawanie wykładników |
| **03** | `03-pierwiastki` | Działania na pierwiastkach | Wyłączanie czynnika przed znak ($\sqrt{75} = 5\sqrt{3}$), szacowanie |
| **04** | `04-procenty` | Obliczenia procentowe i promile | Przelicznik ułamkowy (10% = 1/10, 25% = 1/4), punkty procentowe |
| **05** | `05-wyrazenia-algebraiczne` | Redukcja wyrazów i sumy | Podkreślanie kolorami, mnożenie nawiasów, pułapka minusa przed nawiasem |
| **06** | `06-rownania` | Równania z jedną niewiadomą | Waga szalkowa, mnożenie przez wspólny mianownik ("likwidacja kresek") |
| **07** | `07-trojkaty-katy` | Kąty, trójkąty i Pitagoras | Suma kątów 180°, trójki pitagorejskie (3-4-5, 5-12-13), trójkąt 30-60-90 |
| **08** | `08-czworokaty-pola` | Pola i obwody wielokątów | Dzielenie figur złożonych, wzory rombu i trapezu |
| **09** | `09-uklad-wspolrzednych` | Punkty i symetrie w układzie | Środek odcinka, odległości poziome/pionowe, symetrie względem osi |
| **10** | `10-geometria-przestrzenna` | Graniastosłupy i ostrosłupy | Siatki, pole powierzchni, objętość $V = P_p \cdot H$ oraz $\frac{1}{3}P_p \cdot H$ |
| **11** | `11-statystyka-prawdopodobienstwo` | Średnia i rachunek szans | Drzewko zdarzeń, reguła sprzyjających / wszystkich |
| **12** | `12-droga-predkosc-czas` | Zadania z treścią i proporcje | Trójkąt $s = v \cdot t$, przeliczanie km/h na m/s ($\div 3{,}6$) |
