---
name: matematyka-supermoce
description: >-
  Przygotowuje Kartę Supermocy (jednostronicowy cheat-sheet A4 z mnemotechnikami i sprytnymi metodami) oraz 5-minutowe Quizy Sukcesu (karty mikro-treningu budujące pewność siebie) z matematyki na podstawie podanego zakresu materiału (zadania z podręcznika/ćwiczeń lub opis zagadnienia, np. potęgi, pierwiastki, ułamki, algebra, geometria). Generuje pliki Markdown oraz profesjonalne, gotowe do druku pliki PDF A4 za pomocą silnika headless Chrome (bez plików DOCX).
---

# Matematyka Supermoce & Quizy Sukcesu (Klasy 7–8 i Egzamin Ósmoklasisty)

## Overview (Przegląd)

Skill służy do transformacji dowolnego materiału matematycznego ze szkoły podstawowej (klasy 7–8 oraz przygotowanie do egzaminu ósmoklasisty) w ultra-efektywne, przyjazne poznawczo materiały dydaktyczne dla uczniów z niską tolerancją na znużenie, trudnościami w dłuższej koncentracji lub lękiem przed żmudnymi obliczeniami.

Zamiast monotonnego liczenia "pod kreską" i setek powtarzalnych słupków, skill wdraża metodykę **"Sprytu Matematycznego" (Cheat Codes)**, dekompozycję na mikro-kroki oraz gamifikowane, 5-minutowe sprinty sukcesu.

Format wyjściowy to **wyłącznie czysty Markdown oraz profesjonalnie ostylowany, gotowy do druku PDF na A4** (brak formatu DOCX).

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

W wybranym folderze (np. `sandbox/...` lub w katalogu zmiany OpenSpec) skill tworzy komplet plików:

```
katalog-tematu/
├── karta-supermocy-cheat-sheet.md    # Źródło Markdown karty na biurko
├── karta-supermocy-cheat-sheet.html  # Szablon HTML zoptymalizowany pod 1x A4
├── karta-supermocy-cheat-sheet.pdf   # Wygenerowany elegancki PDF (1 strona A4)
├── quizy-sukcesu-5-minut.md          # Źródło Markdown 4 kart + klucz odpowiedzi
├── quizy-sukcesu-5-minut.html        # Szablon HTML (karty 5-minutowe + klucz)
└── quizy-sukcesu-5-minut.pdf         # Wygenerowany PDF (3 strony A4)
```

> ⚠️ **ZAKAZ GENEROWANIA DOCX**: Zgodnie z wytycznymi użytkownika NIE generujemy plików `.docx` ani `.odt`. Wystarczy czysty `.md`, `.html` i gotowy `.pdf`.

---

### 1. Karta Supermocy (A4 Cheat-Sheet na Biurko)
Muszą znaleźć się w niej 4 moduły mieszczące się bezwzględnie na **1 stronie A4**:
- **Moduł 1: Złota Tabela Sprytu / Klub Przyjaciół** (np. dla ułamków: $4 \leftrightarrow 25, 8 \leftrightarrow 125$; dla potęg: $6^n = 2^n \cdot 3^n$, $(a^b)^c = a^{b \cdot c}$, potęgowanie ilorazu).
- **Moduł 2: Domki Pozycyjne / Wizualny Schemat Myślowy** (schemat kieszonek, reguła strażnika $0$).
- **Moduł 3: Zasada Muru i Policjanta / Antypułapki Egzaminacyjne** (pionowa linia odcięcia, policjant w dół/w górę, efekt domina).
- **Moduł 4: Błyskawiczne Porównywanie / Szacowanie w 3 sekundy** (zasada pizzy, groszy, brakującego kawałka).

**Wymagania techniczne CSS dla Karty:**
```css
@page {
  size: A4 portrait;
  margin: 8mm 10mm 8mm 10mm;
}
* {
  box-sizing: border-box;
  -webkit-print-color-adjust: exact;
  print-color-adjust: exact;
}
```

---

### 2. Quizy Sukcesu (5-minutowe Karty Pewności Siebie)
- **Strona 1 PDF**: Karta 1 i Karta 2 (po 3 zadania na karcie).
- **Strona 2 PDF**: Karta 3 i Karta 4 (po 3 zadania na karcie).
- **Strona 3 PDF**: Klucz odpowiedzi + **Wskazówki coachingowe dla rodzica/trenera**:
  - Jak chwalić za proces i spryt (np. *"Zrobiłaś 6 przykładów w 3 minuty i zero słupków pod kreską!"*).
  - Jak reagować z uśmiechem na typowe błędy (np. *"Czy 8 groszy w Biedronce to tyle co 80 groszy?"*).
  - Zasada rygorystyczna: **maksymalnie 1 karta (5 minut) dziennie**.
- **Struktura każdej karty (3 zadania, 6 pkt)**:
  - *Zadanie 1 (Rozgrzewka, 2 pkt)*: Łączenie w pary, test prawda/fałsz lub uzupełnienie luki – sukces gwarantowany.
  - *Zadanie 2 (Zastosuj Supermoc, 2 pkt)*: Wykorzystanie triku z karty supermocy w konkretnym obliczeniu.
  - *Zadanie 3 (Zagadka Mistrza / Efekt Domina, 2 pkt)*: Typowe zadanie pułapka z egzaminu ósmoklasisty.
  - Pasek rang z checkboxami: 🏆 5–6 pkt (Czarodziejka / Mistrzyni), 3–4 pkt, 1–2 pkt.

---

## 🛠️ Generator PDF (`scripts/generate_pdf.py`)

Do skilla dołączony jest autonomiczny skrypt generujący PDF przez silnik Google Chrome headless:

```bash
python3 .ai/skills/matematyka-supermoce/scripts/generate_pdf.py <sciezka_do_pliku.html> [-o <sciezka_do_wyjscia.pdf>]
```

Skrypt automatycznie wykrywa binarkę Google Chrome na macOS (`/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`) lub Linuksie i renderuje pikselowo perfekcyjny plik PDF.

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
