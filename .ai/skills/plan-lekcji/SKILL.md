---
name: plan-lekcji
description: Tworzenie i aktualizacja interaktywnych planów lekcji w widoku osi czasu (CSS Grid Timeline View) zoptymalizowanych pod pojedynczą stronę wydruku A4. Użyj, gdy użytkownik prosi o utworzenie, wygenerowanie, modyfikację lub wydruk planu lekcji (np. z Google Docs, Librusa, tekstu czy tabeli).
---

# Plan Lekcji (Markdown Source & A4 PDF Print)

Skill służy do generowania oraz aktualizowania planów lekcji. Głównym edytowalnym źródłem prawdy jest czytelna tabela w Markdown (`<nazwa>-plan-lekcji.md`), a docelowym rezultatem wizualnym jest elegancki plik PDF na **pojedynczej stronie A4** (`<nazwa>-plan-lekcji.pdf`). Plik HTML pełni rolę wewnętrznego mechanizmu renderującego dla headless Chrome (nie musi być eksponowany użytkownikowi).

---

## 📐 Kluczowa Architektura Siatki CSS Grid

Plany lekcji bazują na 5-minutowych jednostkach czasu (interwałach), co pozwala na precyzyjne odzwierciedlenie nietypowych dzwonków, przerw i zajęć pozalekcyjnych.

```css
:root {
    /* 1 interwał (5 min) = 6px (gwarantuje zmieszczenie planu do 17:30-18:30 na 1 stronie A4) */
    --grid-scale: 6px; 
}

.calendar {
    display: grid;
    /* Kolumny: 1 dla godzin (65px), 5 dla dni roboczych (repeat(5, 1fr)) */
    grid-template-columns: 65px repeat(5, 1fr);
    /* Rzędy: Nagłówek (38px) + bufor nad 8:00 (14px) + N interwałów 5-minutowych */
    grid-template-rows: 38px 14px repeat(126, var(--grid-scale));
    gap: 1px;
    background-color: #e2e8f0;
    border: 1px solid #cbd5e1;
    border-radius: 8px;
    overflow: hidden;
    max-width: 1050px;
    margin: 0 auto;
    break-inside: avoid;
    page-break-inside: avoid;
}
```

### ⚠️ Krytyczna zasada: Bufor nad godziną 8:00
- **Rząd 1 (38px)**: Nagłówki kolumn (`Godzina`, `Poniedziałek` ... `Piątek`).
- **Rząd 2 (14px)**: **Pusty bufor odstępu**. Zapewnia, że etykieta `8:00` oraz karty pierwszych lekcji nie stykają się ani nie nachodzą na obramowanie nagłówka.
- **Rząd 3**: Początek osi czasu (dokładnie godzina 8:00).

---

## 🧮 Wzory Matematyczne na Pozycjonowanie

Każdy kafelek lekcji pozycjonowany jest za pomocą zmiennych CSS inline:

```html
<div class="lesson [klasa]" style="--col: [D]; --h: [H]; --m: [M]; --d: [DURATION];">
    Nazwa przedmiotu <span class="time">H:MM-H:MM</span>
</div>
```

1. **Rząd początkowy (`grid-row-start`)**:
   $$\text{Rząd} = (H - 8) \times 12 + \frac{M}{5} + 3$$
   *(Uwaga: `+ 3` wynika z rzędu 1 nagłówka i rzędu 2 bufora).*
   ```css
   grid-row-start: calc( ((var(--h) - 8) * 12) + (var(--m) / 5) + 3 );
   ```

2. **Długość kafelka (`grid-row-end`)**:
   $$\text{Span} = \frac{\text{Czas trwania w min}}{5}$$
   - Lekcja standardowa (45 min): `span 9`
   - Zajęcia 60 min: `span 12`
   - Zajęcia 90 min (np. trening, Early Stage): `span 18`
   ```css
   grid-row-end: span calc(var(--d) / 5);
   ```

3. **Kolumny (`--col`)**:
   - `2`: Poniedziałek
   - `3`: Wtorek
   - `4`: Środa
   - `5`: Czwartek
   - `6`: Piątek

4. **Pozycjonowanie linii siatki i etykiet godzinowych**:
   Wzór na rząd etykiety dla pełnej godziny $H$:
   $$\text{Rząd etykiety} = (H - 8) \times 12 + 3$$
   - `8:00` -> rząd `3`
   - `9:00` -> rząd `15`
   - `10:00` -> rząd `27`
   - `11:00` -> rząd `39`
   - `12:00` -> rząd `51`
   - `13:00` -> rząd `63`
   - `14:00` -> rząd `75`
   - `15:00` -> rząd `87`
   - `16:00` -> rząd `99`
   - `17:00` -> rząd `111`
   - `18:00` -> rząd `123`
   - Centrowanie w pionie na linii siatki: `transform: translateY(-50%);`

---

## 🎨 Paleta Barw i Klasy Kafelków

Stosuj spójną, czytelną typografię i kolorystykę Tailwind-inspired:

| Klasa CSS | Kolor tła | Przeznaczenie |
| :--- | :--- | :--- |
| `.general` | `#3b82f6` (Niebieski) | Przedmioty ogólne (Język polski, Matematyka, Historia, Języki obce, Przyroda itd.) |
| `.sport` | `#14b8a6` (Morski / Teal) | WF, szkolenie sportowe, basen, trening tenisowy |
| `.therapy` | `#8b5cf6` (Fioletowy) | Zajęcia terapeutyczne, psychologiczne, rewalidacja, pedagogiczne |
| `.es` | `#f59e0b` (Bursztynowy) | Szkoły językowe (np. Early Stage) i popołudniowe kursy zewnętrzne |
| `.lunch` | `#ea580c` (Ciepły pomarańcz) | Bloki obiadowe (np. Obiad w szkole) |
| `.home` | `#6366f1` (Indygo) | Zajęcia w domu (np. korepetycje domowe) |
| `.muted` / `.cancelled` | `#94a3b8` (Szary) | Zajęcia wyszarzone, odwołane lub opcjonalne |

---

## 🖨️ Standard Druku A4 (Zero Spilling)

Aby zagwarantować bezproblemowy wydruk na **dokładnie 1 stronie A4**:

1. **Definicja strony w CSS**:
   ```css
   @page {
       size: A4 portrait;
       margin: 8mm;
   }
   ```
2. **Wymuszenie druku kolorów tła**:
   ```css
   -webkit-print-color-adjust: exact;
   print-color-adjust: exact;
   ```
   *(Zapobiega drukowaniu pustych białych kafelków bez tła).*
3. **Ukrywanie elementów ekranowych**:
   Dodaj klasę `.no-print` dla przycisków i nawigacji:
   ```css
   @media print {
       body { background-color: #ffffff; padding: 0; }
       .no-print { display: none !important; }
       .calendar { box-shadow: none; max-width: 100%; border-color: #cbd5e1; }
   }
   ```
4. **Przycisk natychmiastowego druku**:
   ```html
   <div class="actions no-print">
       <button onclick="window.print()" class="btn-print">🖨️ Drukuj plan lekcji (A4)</button>
   </div>
   ```

---

## 📝 Edycja planu w Markdown i Skrypt Python (`generate_plan.py`)

Plany lekcji mogą być wygodnie definiowane i edytowane w czytelnym formacie tabeli Markdown, a następnie automatycznie kompilowane do HTML i PDF (1 strona A4) za pomocą skryptu Python `generate_plan.py` (dostępnego w katalogu roboczym oraz w `scripts/generate_plan.py` w folderze skilla).

### 1. Format tabeli Markdown (`<osoba>-plan-lekcji.md`)
```markdown
# Imię - plan lekcji

| Godziny | Poniedziałek | Wtorek | Środa | Czwartek | Piątek |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 08:00 - 08:45 | Plastyka | Matematyka | Język polski | Wychowanie fizyczne | Fizyka |
| 08:55 - 09:40 | Język polski | Język polski | Matematyka | Język angielski | Język polski |
...
| 14:25 - 15:10 | Obiad | Obiad | Obiad | Muzyka | Obiad |
| 16:00 - 17:00 | - | - | Zajęcia terapeutyczne | - | - |
| 18:00 - 19:00 | - | - | - | Język angielski (w domu) | - |
```

- **Godziny w wierszu**: definiowane w pierwszej kolumnie (`Godziny`).
- **Nietypowe godziny w komórce**: można podać czas bezpośrednio w komórce, np. `Trening (14:00 - 15:30)`.
- **Automatyczna klasyfikacja stylów**: skrypt rozpoznaje słowa kluczowe (*WF*, *Trening*, *Terapia*, *Early Stage*, *Obiad*, *w domu*) i dobiera odpowiedni kolor.
- **Ręczny override stylu**: można podać tag np. `Konsultacje [home]`, `Basen [sport]`, `Przekąska [lunch]`.
- **Puste godziny (okienka)**: pusta komórka lub znak `-`.

### 2. Uruchamianie kompilacji
```bash
# Kompilacja pojedynczego planu:
python3 generate_plan.py nadia-plan-lekcji.md

# Kompilacja wszystkich planów w danym katalogu:
python3 generate_plan.py --all
```
Skrypt automatycznie:
1. Parsuje plik Markdown i tworzy dopasowany HTML z osadzonym CSS Grid i buforami 14px.
2. Kompiluje plik HTML do PDF za pomocą headless Google Chrome.
3. Weryfikuje warunek **dokładnie 1 strony A4**.

---

## 🔄 Procedura Obsługi Źródeł Danych

### 1. Pobieranie z Google Docs (Dokumenty Google)
Gdy użytkownik przekaże link do Google Docs:
- Spróbuj odczytać publiczny eksport:
  `https://docs.google.com/document/d/<DOC_ID>/export?format=txt` (lub `format=html` / `format=zip`).
- Jeśli URL zwraca `401 Unauthorized`:
  - Na macOS sprawdź otwarte karty w przeglądarce za pomocą AppleScript:
    ```bash
    osascript -e 'tell application "Google Chrome" to get URL of every tab of every window'
    ```
  - Pobierz eksport przez aktywną sesję Chrome:
    ```bash
    osascript -e 'tell application "Google Chrome" to set newTab to make new tab at end of tabs of window 1 with properties {URL:"https://docs.google.com/document/d/<DOC_ID>/export?format=txt"}'
    ```

### 2. Mapowanie dzwonków szkolnych
- Zwracaj szczególną uwagę na długości przerw (np. standardowo 10 minut, ale przerwy obiadowe mogą mieć 15-20 minut).
- Sprawdź godziny rozpoczęcia kolejnych lekcji (np. 8:00, 8:55, 9:50, 10:45, 11:40, 12:35 lub 12:45).
- Okienka (oznaczone myślnikiem `-` lub wolne godziny) nie tworzą kafelka, pozostawiając czytelne puste tło siatki.

### 3. Pobieranie zrzutu ze schowka macOS
Gdy użytkownik wskazuje na dane lub zrzut w schowku ("ze schowka", "zrzut ekranu", "wklej"):
- Użyj skryptu:
  ```bash
  bash ~/.gemini/config/skills/mac-clipboard-analyzer/scripts/get_clipboard_image.sh /tmp/clipboard_image.png
  ```
- Obejrzyj obraz za pomocą `view_file` i precyzyjnie porównaj go z planem (zwracając uwagę na przedmioty, sale, godziny, okienka oraz odwołane zajęcia).

---

## 🚫 Zakaz analizy historii Git (`git log`)

- **NIGDY nie uruchamiaj ani nie analizuj `git log` ani historii commitów**.
- Modyfikacje i aktualizacje planów lekcji wykonuj wyłącznie w oparciu o bieżący stan pliku HTML, dostarczone przez użytkownika dane (np. ze schowka, dokumentu, tabeli) i wytyczne promptu.

---

## ✅ Weryfikacja Jakościowa (Checklist)

Po wygenerowaniu lub modyfikacji pliku HTML:
1. **Generowanie wizualizacji PDF i weryfikacja pojedynczej strony A4**:
   Zawsze wygeneruj plik PDF obok pliku HTML w tym samym folderze (np. `<nazwa>-plan-lekcji.pdf`) za pomocą headless Chrome i zweryfikuj liczbę stron:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --print-to-pdf="<FOLDER_DOCELOWY>/<nazwa>-plan-lekcji.pdf" "file://<SCIEZKA_HTML>"
   python3 -c "import re; pages = re.findall(rb'/Type\s*/Page[^s]', open('<FOLDER_DOCELOWY>/<nazwa>-plan-lekcji.pdf', 'rb').read()); print('Liczba stron:', len(pages))"
   ```
   Liczba stron **musi wynosić dokładnie 1**.
2. **Brak kolizji etykiety 8:00**:
   Upewnij się, że etykieta `8:00` jest w rzędzie 3, a rząd 2 ma wysokość 14px.
3. **Spójność linków**:
   W odpowiedzi dla użytkownika podawaj bezpośrednie, klikalne linki do edytowalnego pliku Markdown (`.md`) oraz wygenerowanego pliku PDF (`.pdf`) w formacie `file://...`. Pliki HTML traktuj jako wewnętrzny etap kompilacji.
