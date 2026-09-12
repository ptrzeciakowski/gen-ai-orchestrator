import os

base = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-12-matematyka-dla-nadii"

# ==============================================================================
# MODUŁ 06: RÓWNANIA Z JEDNĄ NIEWIADOMĄ
# ==============================================================================
m06 = os.path.join(base, "06-rownania")
os.makedirs(m06, exist_ok=True)

cs_md_06 = """# KARTA SUPERMOCY: RÓWNANIA Z JEDNĄ NIEWIADOMĄ (Klasa 7 & 8)
## Sprytne Metody Nadii – Waga Szalkowa, Magiczny Mostek i Strzał w Mianownik

---

### ⚖️ 1. WAGA SZALKOWA I MAGICZNY MOSTEK ($=$)
Równanie to zrównoważona waga. Gdy przenosisz liczbę lub wyraz z $x$ przez znak równości ($=$):
**ZMIENIASZ ZNAK NA PRZECIWNY!**
- $+$ zamienia się w $-$
- $-$ zamienia się w $+$
- $\\cdot$ zamienia się w $\\div$

> 💡 **Złota reguła:** Lisy ($x$) gromadzą się po LEWEJ stronie, a orzeszki (liczby) po PRAWEJ!
> $$5x - 7 = 2x + 8 \\implies 5x - 2x = 8 + 7 \\implies 3x = 15 \\implies x = 5$$

---

### 💣 2. LIKWIDACJA UŁAMKÓW JEDNYM STRZAŁEM
Masz ułamki? **NIE licz na ułamkach!** Pomnóż całe równanie przez wspólny mianownik (NWW)!
$$\\frac{x+3}{2} - \\frac{x-1}{3} = 2 \\quad \\Big| \\cdot 6$$
$$3(x+3) - 2(x-1) = 12$$
$$3x + 9 - 2x + 2 = 12 \\implies x + 11 = 12 \\implies \\mathbf{x = 1}$$
> 🚨 **Uwaga na wampira:** Zawsze pakuj licznik w nawias po skróceniu! Minus przed ułamkiem zmienia znaki w całym liczniku!

---

### 🧛 3. ANTYPUŁAPKA MINUSA PRZY $x$
- Gdy przy $x$ stoi liczba ujemna, dzielisz przez liczbę ujemną:
  $$-4x = 28 \\implies x = 28 \\div (-4) = \\mathbf{-7}$$
- Gdy przy $x$ stoi sam minus, zmień znaki obu stron:
  $$-x = 13 \\implies \\mathbf{x = -13}$$

---

### 🎭 4. CZY ROZWIĄZANIE ZAWSZE ISTNIEJE?
- **Równanie tożsamościowe (Nieskończenie wiele rozwiązań):**
  $2x + 6 = 2(x + 3) \\implies 2x + 6 = 2x + 6 \\implies 0 = 0$ *(Prawda! Pasuje KAŻDA liczba)*
- **Równanie sprzeczne (Brak rozwiązań):**
  $3x + 5 = 3x + 9 \\implies 5 = 9$ *(Bzdura! Żadna liczba nie pasuje)*

---

### 🧩 5. ZADANIA TEKSTOWE: "KTO MA $x$?"
1. Jako $x$ oznacz **najmniejszą** wartość lub tę, do której odnoszą się inne.
2. Zapisz pozostałe wielkości za pomocą $x$.
3. Ułóż równanie z sumy lub relacji w tekście.
*Przykład: Ania ma 3 razy więcej kredek niż Kasia, a razem mają 48. Kasia = $x$, Ania = $3x$.*
$$x + 3x = 48 \\implies 4x = 48 \\implies x = 12 \\text{ (Kasia)}, \\; 3x = 36 \\text{ (Ania)}$$
"""

cs_html_06 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Równania z Jedną Niewiadomą</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #6366f1; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 16pt; color: #312e81; text-transform: uppercase; letter-spacing: 0.5px; }
  .header p { margin: 2px 0 0; font-size: 9.5pt; color: #4338ca; font-weight: 600; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .card { background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 7px 10px; margin-bottom: 6px; }
  .card-title { font-size: 10.8pt; font-weight: bold; color: #1e1b4b; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; }
  .formula-box { background: #ffffff; border-left: 3.5px solid #6366f1; padding: 5px 8px; margin: 4px 0; font-family: "Courier New", monospace; font-size: 10pt; font-weight: bold; color: #0f172a; border-radius: 0 5px 5px 0; }
  .alert-box { background: #fff1f2; border: 1.5px solid #fecdd3; border-left: 3.5px solid #e11d48; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #9f1239; margin-top: 4px; }
  .success-box { background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 3.5px solid #16a34a; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #166534; margin-top: 4px; }
  ul { margin: 3px 0; padding-left: 17px; }
  li { margin-bottom: 2px; }
  .badge { display: inline-block; background: #e0e7ff; color: #3730a3; padding: 1px 5px; border-radius: 4px; font-size: 8.5pt; font-weight: bold; }
  .step { background: #e2e8f0; color: #1e293b; font-weight: bold; border-radius: 50%; width: 17px; height: 17px; display: inline-flex; align-items: center; justify-content: center; font-size: 8pt; margin-right: 4px; }
</style>
</head>
<body>

<div class="header">
  <h1>⚡ KARTA SUPERMOCY: RÓWNANIA (Klasa 7 & 8)</h1>
  <p>Sprytne Metody Nadii: Waga Szalkowa, Magiczny Mostek i Strzał w Mianownik</p>
</div>

<div class="grid-2">
  <!-- LEWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">⚖️ 1. Waga Szalkowa i Magiczny Mostek (=)</div>
      <p style="margin: 2px 0;">Gdy przenosisz wyraz przez znak równości, <b>zmieniasz znak na przeciwny</b>!</p>
      <ul>
        <li><span class="badge">+</span> przechodzi w <span class="badge">−</span> &nbsp;|&nbsp; <span class="badge">−</span> przechodzi w <span class="badge">+</span></li>
        <li><span class="badge">·</span> przechodzi w <span class="badge">÷</span> (dzielenie obustronne)</li>
      </ul>
      <div class="formula-box">
        5x − 7 = 2x + 8<br>
        5x − 2x = 8 + 7 &nbsp;<i>(lisy po lewej, orzeszki po prawej!)</i><br>
        3x = 15 &nbsp;→&nbsp; <b>x = 5</b>
      </div>
      <div class="success-box">
        🎯 <b>Krótki test:</b> Zawsze sprawdź wynik w pamięci: 5·5 − 7 = 18, 2·5 + 8 = 18. Zgadza się!
      </div>
    </div>

    <div class="card">
      <div class="card-title">💣 2. Strzał w Mianownik (NWW)</div>
      <p style="margin: 2px 0;">Nie męcz się z ułamkami! <b>Mnożymy całe równanie przez NWW</b>:</p>
      <div class="formula-box">
        (x + 3)/2 − (x − 1)/3 = 2 &nbsp;&nbsp;| · 6<br>
        3·(x + 3) − 2·(x − 1) = 12<br>
        3x + 9 − 2x + 2 = 12<br>
        x + 11 = 12 &nbsp;→&nbsp; <b>x = 1</b>
      </div>
      <div class="alert-box">
        🚨 <b>PAMIĘTAJ O NAWIASACH!</b> Po skróceniu mianownika wstaw licznik w nawias! Znak minus przed kreską zmienia WSZYSTKIE znaki w liczniku!
      </div>
    </div>
  </div>

  <!-- PRAWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">🧛 3. Antypułapka Minusa przy x</div>
      <p style="margin: 2px 0;">Co zrobić, gdy przed x stoi minus?</p>
      <ul>
        <li><b>Dzielenie przez minus:</b><br>
          −4x = 28 &nbsp;→&nbsp; x = 28 ÷ (−4) &nbsp;→&nbsp; <b>x = −7</b></li>
        <li><b>Samotny minus:</b><br>
          −x = 13 &nbsp;→&nbsp; <b>x = −13</b> &nbsp;<i>(zmień znaki obu stron)</i></li>
        <li><b>Dwa minusy dają plus:</b><br>
          −3x = −18 &nbsp;→&nbsp; x = −18 ÷ (−3) &nbsp;→&nbsp; <b>x = 6</b></li>
      </ul>
      <div class="alert-box">
        ⚠️ <b>Częsty błąd:</b> Nie "przenoś" liczby z minusem dodając ją, gdy jest połączona mnożeniem! W −4x to jest <b>mnożenie przez −4</b>, więc <b>dzielimy przez −4</b>!
      </div>
    </div>

    <div class="card">
      <div class="card-title">🎭 4. Tożsamość czy Sprzeczność?</div>
      <ul>
        <li><b>Tożsamościowe (Nieskończenie wiele rozwiązań):</b><br>
          2(x + 3) = 2x + 6 &nbsp;→&nbsp; 2x + 6 = 2x + 6 &nbsp;→&nbsp; <b>0 = 0</b><br>
          <span class="badge" style="background:#dcfce7; color:#15803d;">PRAWDA! Każda liczba spełnia równanie.</span></li>
        <li><b>Sprzeczne (Brak rozwiązań):</b><br>
          3x + 4 = 3x + 9 &nbsp;→&nbsp; <b>4 = 9</b><br>
          <span class="badge" style="background:#fee2e2; color:#b91c1c;">BZDURA! Żadna liczba nie spełnia równania.</span></li>
      </ul>
    </div>

    <div class="card">
      <div class="card-title">🧩 5. Zadania Tekstowe: Kto ma x?</div>
      <ol style="margin: 2px 0; padding-left: 18px;">
        <li>Oznacz jako <b>x</b> najmniejszą wielkość lub tę, z którą porównujesz.</li>
        <li>Wyraź pozostałe wielkości przez x.</li>
        <li>Ułóż równanie z treści zadania.</li>
      </ol>
      <div class="formula-box" style="font-size: 9.3pt;">
        Ania ma 3 razy więcej kredek niż Kasia. Razem mają 48.<br>
        Kasia: x &nbsp;|&nbsp; Ania: 3x<br>
        x + 3x = 48 &nbsp;→&nbsp; 4x = 48 &nbsp;→&nbsp; <b>Kasia = 12, Ania = 36</b>
      </div>
    </div>
  </div>
</div>

</body>
</html>
"""

q_md_06 = """# QUIZY SUKCESU: RÓWNANIA Z JEDNĄ NIEWIADOMĄ
## 4 Karty Treningowe po 5 Minut (Format Egzaminu Ósmoklasisty)

### KARTA 1: Podstawy i Mostek (=)
1. Rozwiąż: $3x - 7 = 14$
2. Rozwiąż: $6x + 4 = 2x + 24$
3. Rozwiąż: $15 - 2x = 5$

### KARTA 2: Prysznic Nawiasów i Porządki
1. Rozwiąż: $4(x - 2) = 16$
2. Rozwiąż: $5(2x - 1) - 3(x + 2) = 17$
3. Rozwiąż: $7 - (3x - 2) = 18$

### KARTA 3: Strzał w Mianownik (Likwidacja Ułamków)
1. Rozwiąż: $\\frac{x}{4} + 3 = 8$
2. Rozwiąż: $\\frac{x - 1}{2} = \\frac{x + 3}{4}$
3. Rozwiąż: $\\frac{2x - 1}{3} - \\frac{x + 1}{2} = 1$

### KARTA 4: Zadania Tekstowe i Pułapki
1. W klasie jest 28 uczniów. Dziewcząt jest o 4 więcej niż chłopców. Ilu jest chłopców?
2. Rozwiąż i wskaż liczbę rozwiązań: $3(x + 2) = 3x + 6$
3. Rozwiąż pułapkę minusa: $-5x + 12 = 37$
"""

q_html_06 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Równania z Jedną Niewiadomą</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10pt; line-height: 1.35; }
  .header { text-align: center; border-bottom: 2px solid #6366f1; padding-bottom: 4px; margin-bottom: 12px; }
  .header h1 { margin: 0; font-size: 15pt; color: #312e81; }
  .header p { margin: 2px 0 0; font-size: 9pt; color: #4338ca; }
  .quiz-card { background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; }
  .quiz-title { font-size: 11pt; font-weight: bold; color: #1e1b4b; display: flex; justify-content: space-between; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; margin-bottom: 8px; }
  .task { margin-bottom: 8px; font-size: 10pt; }
  .task-num { font-weight: bold; color: #4f46e5; margin-right: 4px; }
  .answer-space { border-bottom: 1px dashed #94a3b8; height: 26px; margin-top: 3px; display: flex; align-items: flex-end; color: #64748b; font-size: 8.5pt; font-style: italic; }
  .page-break { page-break-before: always; }
  .coach-card { background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; }
  .coach-title { font-size: 11pt; font-weight: bold; color: #166534; margin-bottom: 6px; }
  table.answers { width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 9pt; }
  table.answers th, table.answers td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; }
  table.answers th { background: #e2e8f0; color: #1e293b; }
</style>
</head>
<body>

<!-- STRONA 1: KARTA 1 & KARTA 2 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: RÓWNANIA Z JEDNĄ NIEWIADOMĄ</h1>
  <p>Trening Mikrokroków Nadii – 5 minut na kartę | Zegar start!</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 1: Podstawy i Mostek (=)</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Rozwiąż równanie: <b>3x − 7 = 14</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Przerzuć lisy na lewo, orzeszki na prawo: <b>6x + 4 = 2x + 24</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Uważaj na znak: <b>15 − 2x = 5</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 2: Prysznic Nawiasów i Porządki</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Otwórz nawias: <b>4(x − 2) = 16</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Wykonaj prysznic i zredukuj: <b>5(2x − 1) − 3(x + 2) = 17</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Wampir przed nawiasem: <b>7 − (3x − 2) = 18</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 2: KARTA 3 & KARTA 4 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: RÓWNANIA Z JEDNĄ NIEWIADOMĄ</h1>
  <p>Trening Mikrokroków Nadii – Część II</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 3: Strzał w Mianownik (Likwidacja Ułamków)</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Pomnóż obie strony przez 4: <b>x/4 + 3 = 8</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Pomnóż przez wspólny mianownik 4: <b>(x − 1)/2 = (x + 3)/4</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Pomnóż przez NWW(2,3)=6: <b>(2x − 1)/3 − (x + 1)/2 = 1</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 4: Zadania Tekstowe i Pułapki CKE</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> W klasie jest 28 uczniów. Dziewcząt jest o 4 więcej niż chłopców. Zapisz równanie i oblicz, ilu jest chłopców.
    <div class="answer-space">Równanie: _____________________ | Chłopców = ______</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Rozwiąż równanie i określ, ile ma rozwiązań: <b>3(x + 2) = 3x + 6</b>
    <div class="answer-space">Wynik i wniosek: _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Pułapka minusa: <b>−5x + 12 = 37</b>
    <div class="answer-space">x = _________________________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 3: PRZEWODNIK RODZICA I ODPOWIEDZI -->
<div class="coach-card">
  <div class="coach-title">🧠 PRZEWODNIK MENTORA (Dla Rodzica / Nauczyciela)</div>
  <p style="margin: 3px 0 6px;"><b>Jak wspierać Nadię podczas tej sesji:</b></p>
  <ul>
    <li><b>Waga, nie magia:</b> Przypominaj: <i>"Przenosisz przez znak równości? Płacisz myto – zmieniasz znak!"</i></li>
    <li><b>Strzał w mianownik:</b> Jeśli Nadia gubi się w ułamkach, pochwal ją za pierwszy odruch: <i>"Jaki jest wspólny mianownik? Super, mnożymy wszystko!"</i></li>
    <li><b>Doceniaj mikro-sukces:</b> Równania bywają frustrujące, gdy ucieknie znak. Gdy zauważy swój błąd bez podpowiedzi – pochwal jej czujność detektywa!</li>
  </ul>
</div>

<div class="quiz-card">
  <div class="quiz-title"><span>🔑 KLUCZ ODPOWIEDZI Z WYJAŚNIENIEM KROK PO KROKU</span></div>
  <table class="answers">
    <thead>
      <tr>
        <th style="width: 15%;">Karta</th>
        <th style="width: 15%;">Zadanie</th>
        <th style="width: 25%;">Prawidłowa Odpowiedź</th>
        <th>Kluczowy krok / Wyjaśnienie</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><b>KARTA 1</b></td>
        <td>Zadanie 1</td>
        <td><b>x = 7</b></td>
        <td>3x = 14 + 7 = 21 → x = 21 ÷ 3 = 7</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>x = 5</b></td>
        <td>6x − 2x = 24 − 4 → 4x = 20 → x = 5</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>x = 5</b></td>
        <td>−2x = 5 − 15 = −10 → x = −10 ÷ (−2) = 5</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 2</b></td>
        <td>Zadanie 1</td>
        <td><b>x = 6</b></td>
        <td>4x − 8 = 16 → 4x = 24 → x = 6</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>x = 4</b></td>
        <td>10x − 5 − 3x − 6 = 17 → 7x − 11 = 17 → 7x = 28 → x = 4</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>x = −3</b></td>
        <td>7 − 3x + 2 = 18 → 9 − 3x = 18 → −3x = 9 → x = −3</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 3</b></td>
        <td>Zadanie 1</td>
        <td><b>x = 20</b></td>
        <td>x/4 = 5 → x = 5 · 4 = 20 (lub mnożąc całość przez 4: x + 12 = 32)</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>x = 5</b></td>
        <td>Mnożymy przez 4: 2(x − 1) = x + 3 → 2x − 2 = x + 3 → x = 5</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>x = 11</b></td>
        <td>Mnożymy przez 6: 2(2x − 1) − 3(x + 1) = 6 → 4x − 2 − 3x − 3 = 6 → x − 5 = 6 → x = 11</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 4</b></td>
        <td>Zadanie 1</td>
        <td><b>Chłopcy = 12</b> (Dziewczęta = 16)</td>
        <td>x + (x + 4) = 28 → 2x = 24 → x = 12</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>0 = 0 (nieskończenie wiele)</b></td>
        <td>3x + 6 = 3x + 6 → 0 = 0, równanie tożsamościowe, spełnia każda liczba</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>x = −5</b></td>
        <td>−5x = 37 − 12 = 25 → x = 25 ÷ (−5) = −5</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
"""

with open(os.path.join(m06, "karta-supermocy-cheat-sheet.md"), "w") as f: f.write(cs_md_06)
with open(os.path.join(m06, "karta-supermocy-cheat-sheet.html"), "w") as f: f.write(cs_html_06)
with open(os.path.join(m06, "quizy-sukcesu-5-minut.md"), "w") as f: f.write(q_md_06)
with open(os.path.join(m06, "quizy-sukcesu-5-minut.html"), "w") as f: f.write(q_html_06)
print("Moduł 06 zapisany!")

# ==============================================================================
# MODUŁ 07: TRÓJKĄTY, KĄTY I TWIERDZENIE PITAGORASA
# ==============================================================================
m07 = os.path.join(base, "07-trojkaty-katy-pitagoras")
os.makedirs(m07, exist_ok=True)

cs_md_07 = """# KARTA SUPERMOCY: TRÓJKĄTY, KĄTY I TWIERDZENIE PITAGORASA (Klasa 7 & 8)
## Sprytne Metody Nadii – Złote Kąty, Święte Trójki i Magiczne Ekierki

---

### 📐 1. KĄTY – 3 ŻELAZNE ZASADY
1. **Suma kątów w trójkącie:** ZAWSZE $180^\\circ$. W czworokącie: $360^\\circ$.
2. **Kąty przyległe (linia prosta):** dają w sumie $180^\\circ$ (np. $110^\\circ + 70^\\circ$).
3. **Kąty wierzchołkowe (krzyżyk X) oraz naprzemianległe (Zorro Z):** są DOKŁADNIE RÓWNE!

---

### 🔺 2. TWIERDZENIE PITAGORASA BEZ BŁĘDU
$$a^2 + b^2 = c^2$$
> 🚨 **ŚWIĘTA ZASADA:** $c$ to ZAWSZE najdłuższy bok (przeciwprostokątna naprzeciw kąta $90^\\circ$)!
- Szukasz **najdłuższego boku ($c$)**? $\\implies$ **DODAJESZ:** $c = \\sqrt{a^2 + b^2}$
- Szukasz **krótszego boku ($a$ lub $b$)**? $\\implies$ **ODEJMUJESZ:** $a^2 = c^2 - b^2$

---

### ⚡ 3. ŚWIĘTE TRÓJKI PITAGOREJSKIE (Oszczędź 2 minuty liczenia!)
Jeśli widzisz trójkąt prostokątny, sprawdź, czy to nie święta trójka:
- **3 – 4 – 5** (oraz ich podwojenia: **6 – 8 – 10**, potrójenia: **9 – 12 – 15**, **30 – 40 – 50**)
- **5 – 12 – 13**
- **8 – 15 – 17**
*Widzisz przyprostokątne 6 i 8? Przeciwprostokątna to OD RAZU 10! Bez podnoszenia do kwadratu!*

---

### 📐 4. MAGICZNE EKIERKI (Trójkąty $45^\\circ-45^\\circ-90^\\circ$ i $30^\\circ-60^\\circ-90^\\circ$)
- **Trójkąt $45^\\circ-45^\\circ-90^\\circ$ (Połówka kwadratu):**
  Przyprostokątne to $a, a$, a przeciwprostokątna (przekątna kwadratu) to **$a\\sqrt{2}$**.
  *Kwadrat o boku 6 ma przekątną $d = 6\\sqrt{2}$.*
- **Trójkąt $30^\\circ-60^\\circ-90^\\circ$ (Połówka trójkąta równobocznego):**
  - Krótki bok (naprzeciw $30^\\circ$) = $a$
  - Najdłuższy bok (przeciwprostokątna) = **$2a$** (dwa razy dłuższy!)
  - Średni bok (wysokość $h$, naprzeciw $60^\\circ$) = **$a\\sqrt{3}$**
  - Wzory trójkąta równobocznego: $h = \\frac{a\\sqrt{3}}{2}$, $P = \\frac{a^2\\sqrt{3}}{4}$.

---

### 🛑 5. NIERÓWNOŚĆ TRÓJKĄTA (Czy da się go zbudować?)
Suma dwóch KRÓTSZYCH boków musi być **WIĘKSZA** niż najdłuższy bok:
$$a + b > c$$
- Boki 3, 5, 7 $\\implies 3 + 5 = 8 > 7$ ✅ (TAK, zbudujesz trójkąt)
- Boki 2, 4, 7 $\\implies 2 + 4 = 6 < 7$ ❌ (NIE, boki się nie zepną!)
"""

cs_html_07 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Trójkąty, Kąty i Twierdzenie Pitagorasa</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #0284c7; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 15.5pt; color: #0369a1; text-transform: uppercase; letter-spacing: 0.5px; }
  .header p { margin: 2px 0 0; font-size: 9.5pt; color: #0284c7; font-weight: 600; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .card { background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 7px 10px; margin-bottom: 6px; }
  .card-title { font-size: 10.8pt; font-weight: bold; color: #0c4a6e; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; }
  .formula-box { background: #ffffff; border-left: 3.5px solid #0284c7; padding: 5px 8px; margin: 4px 0; font-family: "Courier New", monospace; font-size: 10pt; font-weight: bold; color: #0f172a; border-radius: 0 5px 5px 0; }
  .alert-box { background: #fff1f2; border: 1.5px solid #fecdd3; border-left: 3.5px solid #e11d48; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #9f1239; margin-top: 4px; }
  .success-box { background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 3.5px solid #16a34a; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #166534; margin-top: 4px; }
  ul { margin: 3px 0; padding-left: 17px; }
  li { margin-bottom: 2px; }
  .badge { display: inline-block; background: #e0f2fe; color: #0369a1; padding: 1px 5px; border-radius: 4px; font-size: 8.5pt; font-weight: bold; }
</style>
</head>
<body>

<div class="header">
  <h1>⚡ KARTA SUPERMOCY: TRÓJKĄTY I PITAGORAS (Klasa 7 & 8)</h1>
  <p>Sprytne Metody Nadii: Złote Kąty, Święte Trójki i Magiczne Ekierki</p>
</div>

<div class="grid-2">
  <!-- LEWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">📐 1. Trzy Żelazne Zasady Kątów</div>
      <ul>
        <li><b>W trójkącie:</b> suma kątów = <b>180°</b>. W czworokącie = <b>360°</b>.</li>
        <li><b>Kąty przyległe (linia prosta):</b> dają <b>180°</b> (np. 180° − 65° = 115°).</li>
        <li><b>Kąty wierzchołkowe (krzyżyk) i naprzemianległe (litera Z):</b> są <b>DOKŁADNIE RÓWNE</b>!</li>
      </ul>
      <div class="success-box">
        💡 <b>Trójkąt równoramienny:</b> Kąty przy podstawie są IDENTYCZNE! Jeśli kąt między ramionami ma 40°, to przy podstawie: (180° − 40°) ÷ 2 = 70°.
      </div>
    </div>

    <div class="card">
      <div class="card-title">🔺 2. Twierdzenie Pitagorasa bez Błędu</div>
      <div class="formula-box">
        a² + b² = c² &nbsp;&nbsp;(c = przeciwprostokątna!)
      </div>
      <ul>
        <li>Szukasz <b>długiego boku (c)</b>? → <b>DODAJESZ:</b><br>
          c² = 6² + 8² = 36 + 64 = 100 → <b>c = 10</b></li>
        <li>Szukasz <b>krótkiego boku (a lub b)</b>? → <b>ODEJMUJESZ:</b><br>
          a² = 13² − 12² = 169 − 144 = 25 → <b>a = 5</b></li>
      </ul>
      <div class="alert-box">
        🚨 <b>NAJWIĘKSZA PUŁAPKA CKE:</b> Zawsze upewnij się, gdzie jest kąt prosty! Najdłuższy bok c leży DOKŁADNIE NAPRZECIW kąta prostego!
      </div>
    </div>

    <div class="card">
      <div class="card-title">🛑 3. Nierówność Trójkąta</div>
      <p style="margin: 2px 0;">Suma dwóch <b>krótszych boków</b> musi być <b>WIĘKSZA</b> niż najdłuższy: <b>a + b &gt; c</b></p>
      <ul>
        <li>Boki 3, 5, 7 → 3 + 5 = 8 &gt; 7 <span class="badge" style="background:#dcfce7; color:#166534;">TAK ✅</span></li>
        <li>Boki 2, 4, 7 → 2 + 4 = 6 &lt; 7 <span class="badge" style="background:#fee2e2; color:#991b1b;">NIE ❌</span></li>
      </ul>
    </div>
  </div>

  <!-- PRAWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">⚡ 4. Święte Trójki (Bez Liczenia!)</div>
      <p style="margin: 2px 0;">Zapamiętaj te zestawy – pojawiają się w 80% zadań:</p>
      <ul>
        <li><span class="badge">3 – 4 – 5</span> oraz ich wielokrotności:
          <ul>
            <li><b>6 – 8 – 10</b> (podwojenie)</li>
            <li><b>9 – 12 – 15</b> (potrojenie)</li>
            <li><b>30 – 40 – 50</b></li>
          </ul>
        </li>
        <li><span class="badge">5 – 12 – 13</span> (np. przeciwprostokątna 13, przyprostokątna 12 → drugi bok to od razu 5!)</li>
        <li><span class="badge">8 – 15 – 17</span></li>
      </ul>
      <div class="success-box">
        🚀 <b>Oszczędzasz 2 minuty:</b> Widzisz boki 6 i 8? Od razu piszesz 10!
      </div>
    </div>

    <div class="card">
      <div class="card-title">📐 5. Magiczne Ekierki (Specjalne Trójkąty)</div>
      <p style="margin: 2px 0;"><b>A. Ekierka 45°−45°−90° (Połówka kwadratu):</b></p>
      <div class="formula-box">
        Boki: a, a, a√2 &nbsp;|&nbsp; Przekątna kwadratu d = a√2
      </div>
      <p style="margin: 2px 0; font-size: 9.3pt;">Kwadrat o boku 7 ma przekątną <b>7√2</b>.</p>

      <p style="margin: 4px 0 2px;"><b>B. Ekierka 30°−60°−90° (Połówka trójkąta równobocznego):</b></p>
      <div class="formula-box">
        Krótki bok (naprzeciw 30°) = a<br>
        Przeciwprostokątna = 2a &nbsp;(dwa razy dłuższy!)<br>
        Średni bok (wysokość h, naprzeciw 60°) = a√3
      </div>
      <p style="margin: 2px 0; font-size: 9.3pt;"><b>Trójkąt równoboczny:</b> h = (a√3)/2, &nbsp; Pole P = (a²√3)/4</p>
    </div>
  </div>
</div>

</body>
</html>
"""

q_md_07 = """# QUIZY SUKCESU: TRÓJKĄTY, KĄTY I TWIERDZENIE PITAGORASA
## 4 Karty Treningowe po 5 Minut (Format Egzaminu Ósmoklasisty)

### KARTA 1: Kąty i Sumy w Figurach
1. W trójkącie równoramiennym kąt między ramionami ma $50^\\circ$. Jakie miary mają kąty przy podstawie?
2. Kąt przyległy do kąta $\\alpha$ ma miarę $135^\\circ$. Ile wynosi kąt $\\alpha$?
3. W czworokącie trzy kąty mają miary $70^\\circ, 110^\\circ, 120^\\circ$. Jaka jest miara czwartego kąta?

### KARTA 2: Twierdzenie Pitagorasa i Święte Trójki
1. Przyprostokątne mają długości 6 cm i 8 cm. Oblicz długość przeciwprostokątnej.
2. Przeciwprostokątna ma 13 cm, a jedna z przyprostokątnych 12 cm. Oblicz długość drugiej przyprostokątnej.
3. Czy z odcinków o długościach 5 cm, 7 cm i 13 cm można zbudować trójkąt? Uzasadnij.

### KARTA 3: Ekierki i Trójkąt Równoboczny
1. Kwadrat ma bok o długości 9 cm. Ile wynosi długość jego przekątnej?
2. Oblicz wysokość i pole trójkąta równobocznego o boku $a = 6\\text{ cm}$.
3. W trójkącie prostokątnym o kątach $30^\\circ, 60^\\circ, 90^\\circ$ przeciwprostokątna ma 14 cm. Ile wynosi najkrótszy bok?

### KARTA 4: Miszmasz Egzaminacyjny
1. Drabina o długości 10 m jest oparta o ścianę. Jej dolny koniec znajduje się 6 m od ściany. Na jaką wysokość sięga drabina?
2. W trójkącie prostokątnym przyprostokątna naprzeciw kąta $30^\\circ$ ma długość 5 cm. Oblicz pole tego trójkąta.
3. Kąty w trójkącie mają miary $x, 2x, 3x$. Wyznacz miarę największego kąta.
"""

q_html_07 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Trójkąty, Kąty i Pitagoras</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10pt; line-height: 1.35; }
  .header { text-align: center; border-bottom: 2px solid #0284c7; padding-bottom: 4px; margin-bottom: 12px; }
  .header h1 { margin: 0; font-size: 15pt; color: #0369a1; }
  .header p { margin: 2px 0 0; font-size: 9pt; color: #0284c7; }
  .quiz-card { background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; }
  .quiz-title { font-size: 11pt; font-weight: bold; color: #0c4a6e; display: flex; justify-content: space-between; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; margin-bottom: 8px; }
  .task { margin-bottom: 8px; font-size: 10pt; }
  .task-num { font-weight: bold; color: #0284c7; margin-right: 4px; }
  .answer-space { border-bottom: 1px dashed #94a3b8; height: 26px; margin-top: 3px; display: flex; align-items: flex-end; color: #64748b; font-size: 8.5pt; font-style: italic; }
  .page-break { page-break-before: always; }
  .coach-card { background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; }
  .coach-title { font-size: 11pt; font-weight: bold; color: #166534; margin-bottom: 6px; }
  table.answers { width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 9pt; }
  table.answers th, table.answers td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; }
  table.answers th { background: #e2e8f0; color: #1e293b; }
</style>
</head>
<body>

<!-- STRONA 1: KARTA 1 & KARTA 2 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: TRÓJKĄTY, KĄTY I PITAGORAS</h1>
  <p>Trening Mikrokroków Nadii – 5 minut na kartę | Zegar start!</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 1: Kąty i Sumy w Figurach</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> W trójkącie równoramiennym kąt między ramionami ma 50°. Jakie miary mają kąty przy podstawie?
    <div class="answer-space">Kąty przy podstawie = _________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Kąt przyległy do kąta α ma miarę 135°. Ile wynosi kąt α?
    <div class="answer-space">α = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Trzy kąty czworokąta mają 70°, 110° i 120°. Jaka jest miara czwartego kąta?
    <div class="answer-space">Czwarty kąt = ________________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 2: Twierdzenie Pitagorasa i Święte Trójki</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Przyprostokątne trójkąta mają 6 cm i 8 cm. Oblicz przeciwprostokątną c.
    <div class="answer-space">c = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Przeciwprostokątna ma 13 cm, a przyprostokątna 12 cm. Oblicz drugą przyprostokątną.
    <div class="answer-space">a = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Czy z odcinków 5 cm, 7 cm i 13 cm można zbudować trójkąt? Zapisz warunek.
    <div class="answer-space">Odpowiedź i warunek: __________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 2: KARTA 3 & KARTA 4 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: TRÓJKĄTY, KĄTY I PITAGORAS</h1>
  <p>Trening Mikrokroków Nadii – Część II</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 3: Ekierki i Trójkąt Równoboczny</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Kwadrat ma bok 9 cm. Ile wynosi długość jego przekątnej d?
    <div class="answer-space">d = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Trójkąt równoboczny ma bok a = 6 cm. Oblicz jego wysokość h oraz pole P.
    <div class="answer-space">h = _______________ | P = _______________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> W trójkącie 30°−60°−90° przeciwprostokątna ma 14 cm. Ile wynosi najkrótszy bok?
    <div class="answer-space">Najkrótszy bok = ______________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 4: Miszmasz Egzaminacyjny CKE</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Drabina o długości 10 m oparta jest o ścianę. Jej dół jest 6 m od ściany. Na jaką wysokość sięga drabina?
    <div class="answer-space">Wysokość = ___________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> W trójkącie prostokątnym o kątach 30°, 60°, 90° bok naprzeciw 30° ma 5 cm. Oblicz pole trójkąta.
    <div class="answer-space">Pole = _______________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Kąty w trójkącie mają miary x, 2x, 3x. Wyznacz miarę największego kąta.
    <div class="answer-space">Największy kąt = ______________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 3: PRZEWODNIK RODZICA I ODPOWIEDZI -->
<div class="coach-card">
  <div class="coach-title">🧠 PRZEWODNIK MENTORA (Dla Rodzica / Nauczyciela)</div>
  <p style="margin: 3px 0 6px;"><b>Wskazówki neurodydaktyczne:</b></p>
  <ul>
    <li><b>Zmysł wzroku:</b> Zachęcaj Nadię do zaznaczania kąta prostego łukiem z kropką i wskazywania palcem boku naprzeciwko: <i>"To jest przeciwprostokątna!"</i></li>
    <li><b>Święte Trójki:</b> Jeśli Nadia od razu poda 10 w zadaniu z bokami 6 i 8 bez rozpisywania całego Pitagorasa, nagródź to: <i>"Brawo, poznałaś trójkę pitagorejską jak prawdziwy mistrz!"</i></li>
    <li><b>Ekierki:</b> W trójkącie 30-60-90 przypomnij: <i>"Krótki bok to połowa najdłuższego!"</i>.</li>
  </ul>
</div>

<div class="quiz-card">
  <div class="quiz-title"><span>🔑 KLUCZ ODPOWIEDZI Z WYJAŚNIENIEM KROK PO KROKU</span></div>
  <table class="answers">
    <thead>
      <tr>
        <th style="width: 15%;">Karta</th>
        <th style="width: 15%;">Zadanie</th>
        <th style="width: 25%;">Prawidłowa Odpowiedź</th>
        <th>Kluczowy krok / Wyjaśnienie</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><b>KARTA 1</b></td>
        <td>Zadanie 1</td>
        <td><b>65° i 65°</b></td>
        <td>(180° − 50°) ÷ 2 = 130° ÷ 2 = 65°</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>45°</b></td>
        <td>180° − 135° = 45° (kąty przyległe sumują się do 180°)</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>60°</b></td>
        <td>360° − (70° + 110° + 120°) = 360° − 300° = 60°</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 2</b></td>
        <td>Zadanie 1</td>
        <td><b>10 cm</b></td>
        <td>Święta trójka 6-8-10 (lub 6² + 8² = 36 + 64 = 100, √100 = 10)</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>5 cm</b></td>
        <td>Święta trójka 5-12-13 (lub 13² − 12² = 169 − 144 = 25, √25 = 5)</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>NIE MOŻNA</b></td>
        <td>5 + 7 = 12, a 12 &lt; 13 (suma krótszych boków musi być większa niż najdłuższy!)</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 3</b></td>
        <td>Zadanie 1</td>
        <td><b>9√2 cm</b></td>
        <td>Wzór na przekątną kwadratu: d = a√2 = 9√2</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>h = 3√3 cm, P = 9√3 cm²</b></td>
        <td>h = (6√3)/2 = 3√3; &nbsp; P = (6²√3)/4 = 36√3 / 4 = 9√3</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>7 cm</b></td>
        <td>W trójkącie 30-60-90 bok naprzeciw 30° jest połową przeciwprostokątnej: 14 ÷ 2 = 7</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 4</b></td>
        <td>Zadanie 1</td>
        <td><b>8 m</b></td>
        <td>Święta trójka 6-8-10! (lub h² = 10² − 6² = 100 − 36 = 64 → h = 8)</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>12,5√3 cm² (lub 25√3 / 2)</b></td>
        <td>Przyprostokątne to a = 5 oraz b = 5√3. Pole = (5 · 5√3) / 2 = 12,5√3</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>90°</b></td>
        <td>x + 2x + 3x = 180° → 6x = 180° → x = 30°. Największy kąt to 3x = 90° (trójkąt prostokątny!)</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
"""

with open(os.path.join(m07, "karta-supermocy-cheat-sheet.md"), "w") as f: f.write(cs_md_07)
with open(os.path.join(m07, "karta-supermocy-cheat-sheet.html"), "w") as f: f.write(cs_html_07)
with open(os.path.join(m07, "quizy-sukcesu-5-minut.md"), "w") as f: f.write(q_md_07)
with open(os.path.join(m07, "quizy-sukcesu-5-minut.html"), "w") as f: f.write(q_html_07)
print("Moduł 07 zapisany!")

# ==============================================================================
# MODUŁ 08: CZWOROKĄTY I POLA FIGUR
# ==============================================================================
m08 = os.path.join(base, "08-czworokaty-i-pola")
os.makedirs(m08, exist_ok=True)

cs_md_08 = """# KARTA SUPERMOCY: CZWOROKĄTY I POLA FIGUR (Klasa 7 & 8)
## Sprytne Metody Nadii – Mapa Pól, Sekret Przekątnych Rombu i Tajemnice Koła

---

### 🏰 1. MAPA PÓL FIGUR PŁASKICH
- **Prostokąt:** $P = a \\cdot b$, &nbsp; $Obw = 2a + 2b$
- **Kwadrat:** $P = a^2 = \\frac{d^2}{2}$, &nbsp; $Obw = 4a$
- **Równoległobok:** $P = a \\cdot h_a$ *(Wysokość $h$ MUSI opadać pod kątem prostym na bok $a$!)*
- **Trójkąt:** $P = \\frac{a \\cdot h}{2}$ *(Połówka równoległoboku)*

---

### 💎 2. ROMB – DWA WZORY I SEKRET PRZEKĄTNYCH
1. Ze zwykłej podstawy i wysokości: **$P = a \\cdot h$**
2. Z przekątnych (królewski wzór): **$P = \\frac{e \\cdot f}{2}$**
> 💡 **Sekret rombu:** Przekątne przecinają się w połowie pod kątem **$90^\\circ$**!
> Tworzą 4 trójkąty prostokątne o bokach: $\\frac{e}{2}, \\frac{f}{2}$ oraz $a$.
> **Zawsze działa tu Pitagoras:** $\\left(\\frac{e}{2}\\right)^2 + \\left(\\frac{f}{2}\\right)^2 = a^2$!

---

### 📐 3. TRAPEZ – ŚREDNIA Z PODSTAW
$$P = \\frac{(a + b) \\cdot h}{2}$$
- Wyobraź sobie, że bierzesz średnią z górnej i dolnej podstawy: $\\frac{a+b}{2}$ i mnożysz przez wysokość $h$.
- **W trapezie równoramiennym:** opuszczając dwie wysokości, odcinasz na dole dwa równe kawałki:
  $$x = \\frac{a - b}{2}$$

---

### ⭕ 4. KOŁO I OKRĄG (Liczba $\\pi \\approx 3{,}14$)
- **Obwód okręgu (długość sznurka):** $$L = 2\\pi r = \\pi d$$
- **Pole koła (pizza):** $$P = \\pi r^2$$
> 🚨 **ANTPUŁAPKA CKE:** Jeśli w zadaniu podają średnicę $d = 12\\text{ cm}$, OD RAZU zapisz na marginesie: **$r = 6\\text{ cm}$**! Połowa błędów na egzaminie wynika z podstawienia średnicy zamiast promienia!

---

### ✂️ 5. METODA ROZCINANIA I DOPEŁNIANIA
Gdy masz skomplikowaną figurę wielokątną:
1. **Rozetnij:** podziel ją na znane klocki (prostokąty, trójkąty) i dodaj ich pola.
2. **Dopełnij (Pudełko):** obrysuj figurę prostokątem i odejmij puste trójkąty narożne!
"""

cs_html_08 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Czworokąty i Pola Figur</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #10b981; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 15.5pt; color: #065f46; text-transform: uppercase; letter-spacing: 0.5px; }
  .header p { margin: 2px 0 0; font-size: 9.5pt; color: #059669; font-weight: 600; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .card { background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 7px 10px; margin-bottom: 6px; }
  .card-title { font-size: 10.8pt; font-weight: bold; color: #064e3b; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; }
  .formula-box { background: #ffffff; border-left: 3.5px solid #10b981; padding: 5px 8px; margin: 4px 0; font-family: "Courier New", monospace; font-size: 10pt; font-weight: bold; color: #0f172a; border-radius: 0 5px 5px 0; }
  .alert-box { background: #fff1f2; border: 1.5px solid #fecdd3; border-left: 3.5px solid #e11d48; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #9f1239; margin-top: 4px; }
  .success-box { background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 3.5px solid #16a34a; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #166534; margin-top: 4px; }
  ul { margin: 3px 0; padding-left: 17px; }
  li { margin-bottom: 2px; }
  .badge { display: inline-block; background: #d1fae5; color: #065f46; padding: 1px 5px; border-radius: 4px; font-size: 8.5pt; font-weight: bold; }
</style>
</head>
<body>

<div class="header">
  <h1>⚡ KARTA SUPERMOCY: CZWOROKĄTY I POLA FIGUR (Klasa 7 & 8)</h1>
  <p>Sprytne Metody Nadii: Mapa Pól, Sekret Przekątnych Rombu i Tajemnice Koła</p>
</div>

<div class="grid-2">
  <!-- LEWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">🏰 1. Mapa Pól Figur Płaskich</div>
      <ul>
        <li><b>Kwadrat:</b> P = a² &nbsp;lub&nbsp; P = d²/2</li>
        <li><b>Prostokąt:</b> P = a · b</li>
        <li><b>Równoległobok:</b> P = a · h<sub>a</sub><br>
          <i>(Wysokość musi tworzyć kąt prosty z tym konkretnym bokiem!)</i></li>
        <li><b>Trójkąt:</b> P = (a · h) / 2</li>
      </ul>
      <div class="success-box">
        💡 <b>Dwie wysokości równoległoboku:</b> Pole jest takie samo! a · h<sub>a</sub> = b · h<sub>b</sub>. Jeśli znasz boki i jedną wysokość, drugą wyliczysz w mig!
      </div>
    </div>

    <div class="card">
      <div class="card-title">💎 2. Romb – Dwa Oblicza i Pitagoras</div>
      <div class="formula-box">
        Wzór 1: P = a · h &nbsp;|&nbsp; Wzór 2: P = (e · f) / 2
      </div>
      <p style="margin: 2px 0;"><b>Sekret przekątnych e i f:</b></p>
      <ul>
        <li>Przecinają się pod kątem <b>90°</b> i dzielą dokładnie <b>na pół</b>.</li>
        <li>Dają 4 trójkąty prostokątne o przyprostokątnych e/2, f/2 i boku a.</li>
      </ul>
      <div class="formula-box" style="font-size: 9.3pt;">
        Przykład: Przekątne 6 i 8 cm → połówki to 3 i 4 cm.<br>
        Święta trójka 3-4-5 → <b>bok rombu a = 5 cm!</b>
      </div>
    </div>
  </div>

  <!-- PRAWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">📐 3. Trapez – Średnia z Podstaw</div>
      <div class="formula-box">
        P = [(a + b) · h] / 2
      </div>
      <p style="margin: 2px 0;"><b>Trapez równoramienny (trik z wysokościami):</b></p>
      <p style="margin: 2px 0; font-size: 9.3pt;">Opuszczając dwie wysokości z górnej podstawy b, odcinasz na dole dwa równe kawałki:</p>
      <div class="formula-box" style="font-size: 9.3pt;">
        x = (a − b) / 2 &nbsp;&nbsp;→&nbsp;&nbsp; ramię z Pitagorasa: x² + h² = c²
      </div>
    </div>

    <div class="card">
      <div class="card-title">⭕ 4. Koło i Okrąg (Magia π)</div>
      <div class="formula-box">
        Obwód okręgu (wstążka): L = 2πr = πd<br>
        Pole koła (pizza): P = πr²
      </div>
      <div class="alert-box">
        🚨 <b>ANTYPUŁAPKA ŚREDNICY:</b> Jeśli zadanie podaje średnicę d = 10 cm, NATYCHMIAST napisz <b>r = 5 cm</b>! Do wzoru na pole ZAWSZE wstawiasz promień r, a nie średnicę!
      </div>
      <div class="success-box">
        💡 <b>Wynik z π:</b> Na egzaminie zazwyczaj zostawiasz π w wyniku (np. P = 25π cm²), chyba że każą przyjąć π ≈ 3,14 lub 22/7.
      </div>
    </div>

    <div class="card">
      <div class="card-title">✂️ 5. Rozcinanie i Pudełko</div>
      <p style="margin: 2px 0; font-size: 9.3pt;">Gdy figura ma nietypowy kształt na siatce kwadratowej:</p>
      <ol style="margin: 2px 0; padding-left: 17px; font-size: 9.3pt;">
        <li>Obrysuj ją prostokątem ("pudełkiem").</li>
        <li>Odejmij pola pustych trójkątów narożnych: P = P<sub>pudełka</sub> − P<sub>rogów</sub>.</li>
      </ol>
    </div>
  </div>
</div>

</body>
</html>
"""

q_md_08 = """# QUIZY SUKCESU: CZWOROKĄTY I POLA FIGUR
## 4 Karty Treningowe po 5 Minut (Format Egzaminu Ósmoklasisty)

### KARTA 1: Pola Trójkątów i Równoległoboków
1. Równoległobok ma bok 12 cm i opadającą na niego wysokość 5 cm. Oblicz jego pole.
2. W trójkącie prostokątnym przyprostokątne mają 7 cm i 8 cm. Ile wynosi jego pole?
3. Równoległobok o polu $48\\text{ cm}^2$ ma bok 8 cm. Oblicz wysokość opadającą na ten bok.

### KARTA 2: Romb i Magia Przekątnych
1. Przekątne rombu mają długości 8 cm i 14 cm. Oblicz pole rombu.
2. Przekątne rombu mają długości 12 cm i 16 cm. Oblicz długość boku tego rombu (wykorzystaj Pitagorasa).
3. Romb o boku 10 cm ma wysokość 6 cm. Oblicz pole rombu.

### KARTA 3: Trapez bez Tajemnic
1. Podstawy trapezu mają długości 9 cm i 15 cm, a wysokość wynosi 6 cm. Oblicz pole trapezu.
2. Trapez równoramienny ma podstawy 16 cm i 10 cm. Oblicz długość odcinka $x$ odciętego przez wysokość na dolnej podstawie.
3. Pole trapezu wynosi $40\\text{ cm}^2$, a suma podstaw to 16 cm. Ile wynosi wysokość trapezu?

### KARTA 4: Koło, Okrąg i Figury Złożone
1. Oblicz pole i obwód koła o promieniu $r = 7\\text{ cm}$ (zostaw $\\pi$).
2. Koło ma średnicę $d = 12\\text{ cm}$. Oblicz jego pole.
3. Obwód koła wynosi $18\\pi\\text{ cm}$. Ile wynosi pole tego koła?
"""

q_html_08 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Czworokąty i Pola Figur</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10pt; line-height: 1.35; }
  .header { text-align: center; border-bottom: 2px solid #10b981; padding-bottom: 4px; margin-bottom: 12px; }
  .header h1 { margin: 0; font-size: 15pt; color: #065f46; }
  .header p { margin: 2px 0 0; font-size: 9pt; color: #059669; }
  .quiz-card { background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; }
  .quiz-title { font-size: 11pt; font-weight: bold; color: #064e3b; display: flex; justify-content: space-between; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; margin-bottom: 8px; }
  .task { margin-bottom: 8px; font-size: 10pt; }
  .task-num { font-weight: bold; color: #10b981; margin-right: 4px; }
  .answer-space { border-bottom: 1px dashed #94a3b8; height: 26px; margin-top: 3px; display: flex; align-items: flex-end; color: #64748b; font-size: 8.5pt; font-style: italic; }
  .page-break { page-break-before: always; }
  .coach-card { background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; }
  .coach-title { font-size: 11pt; font-weight: bold; color: #166534; margin-bottom: 6px; }
  table.answers { width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 9pt; }
  table.answers th, table.answers td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; }
  table.answers th { background: #e2e8f0; color: #1e293b; }
</style>
</head>
<body>

<!-- STRONA 1: KARTA 1 & KARTA 2 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: CZWOROKĄTY I POLA FIGUR</h1>
  <p>Trening Mikrokroków Nadii – 5 minut na kartę | Zegar start!</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 1: Pola Trójkątów i Równoległoboków</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Równoległobok ma bok 12 cm i opuszczoną na niego wysokość 5 cm. Oblicz pole.
    <div class="answer-space">P = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Przyprostokątne trójkąta prostokątnego mają 7 cm i 8 cm. Oblicz pole.
    <div class="answer-space">P = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Równoległobok o polu 48 cm² ma bok o długości 8 cm. Oblicz wysokość dla tego boku.
    <div class="answer-space">h = _________________________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 2: Romb i Magia Przekątnych</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Przekątne rombu mają 8 cm i 14 cm. Oblicz pole tego rombu.
    <div class="answer-space">P = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Przekątne rombu mają 12 cm i 16 cm. Oblicz bok a rombu (skorzystaj z połówek przekątnych i Pitagorasa).
    <div class="answer-space">a = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Romb ma bok 10 cm i wysokość 6 cm. Jakie jest jego pole?
    <div class="answer-space">P = _________________________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 2: KARTA 3 & KARTA 4 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: CZWOROKĄTY I POLA FIGUR</h1>
  <p>Trening Mikrokroków Nadii – Część II</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 3: Trapez bez Tajemnic</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Podstawy trapezu to 9 cm i 15 cm, a wysokość ma 6 cm. Oblicz pole.
    <div class="answer-space">P = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Trapez równoramienny ma podstawy 16 cm i 10 cm. Ile wynosi odcinek x odcięty przez wysokość?
    <div class="answer-space">x = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Pole trapezu to 40 cm², a suma podstaw wynosi 16 cm. Oblicz wysokość h.
    <div class="answer-space">h = _________________________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 4: Koło, Okrąg i Figury Złożone</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Koło ma promień r = 7 cm. Zapisz jego obwód L i pole P z liczbą π.
    <div class="answer-space">L = _______________ | P = _______________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Koło ma średnicę d = 12 cm. Uważaj na pułapkę – oblicz jego pole.
    <div class="answer-space">P = _________________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Obwód koła wynosi 18π cm. Ile wynosi pole tego koła?
    <div class="answer-space">r = _________ | P = ___________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 3: PRZEWODNIK RODZICA I ODPOWIEDZI -->
<div class="coach-card">
  <div class="coach-title">🧠 PRZEWODNIK MENTORA (Dla Rodzica / Nauczyciela)</div>
  <p style="margin: 3px 0 6px;"><b>Wskazówki motywacyjne:</b></p>
  <ul>
    <li><b>Romb:</b> Przypomnij Nadii, że romb to "kopnięty kwadrat" – ma równe boki, ale jego przekątne tworzą 4 trójkąty prostokątne. Połówki przekątnych to przyprostokątne!</li>
    <li><b>Pułapka średnicy:</b> Gdy Nadia zobaczy średnicę w zadaniu, zapytaj: <i>"Jaki jest pierwszy odruch detektywa?"</i> Odpowiedź: <i>"Podzielić przez 2 i wpisać promień r!"</i></li>
    <li><b>Brak stresu z π:</b> Liczba π to po prostu litera/symbol w wyniku (jak x). Nie trzeba jej wymnażać przez 3,14, chyba że zadanie wyraźnie tego żąda.</li>
  </ul>
</div>

<div class="quiz-card">
  <div class="quiz-title"><span>🔑 KLUCZ ODPOWIEDZI Z WYJAŚNIENIEM KROK PO KROKU</span></div>
  <table class="answers">
    <thead>
      <tr>
        <th style="width: 15%;">Karta</th>
        <th style="width: 15%;">Zadanie</th>
        <th style="width: 25%;">Prawidłowa Odpowiedź</th>
        <th>Kluczowy krok / Wyjaśnienie</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><b>KARTA 1</b></td>
        <td>Zadanie 1</td>
        <td><b>60 cm²</b></td>
        <td>P = a · h = 12 · 5 = 60 cm²</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>28 cm²</b></td>
        <td>P = (7 · 8) / 2 = 56 / 2 = 28 cm² (w trójkącie prostokątnym przyprostokątne to podstawa i wysokość)</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>6 cm</b></td>
        <td>P = a · h → 48 = 8 · h → h = 48 ÷ 8 = 6 cm</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 2</b></td>
        <td>Zadanie 1</td>
        <td><b>56 cm²</b></td>
        <td>P = (e · f) / 2 = (8 · 14) / 2 = 56 cm²</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>10 cm</b></td>
        <td>Połówki to e/2 = 6, f/2 = 8. Święta trójka 6-8-10 → a = 10 cm!</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>60 cm²</b></td>
        <td>Romb to też równoległobok: P = a · h = 10 · 6 = 60 cm²</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 3</b></td>
        <td>Zadanie 1</td>
        <td><b>72 cm²</b></td>
        <td>P = [(9 + 15) · 6] / 2 = [24 · 6] / 2 = 72 cm²</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>3 cm</b></td>
        <td>x = (a − b) / 2 = (16 − 10) / 2 = 6 / 2 = 3 cm</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>5 cm</b></td>
        <td>P = [(a + b) · h] / 2 → 40 = [16 · h] / 2 → 40 = 8h → h = 5 cm</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 4</b></td>
        <td>Zadanie 1</td>
        <td><b>L = 14π cm, P = 49π cm²</b></td>
        <td>L = 2πr = 14π; &nbsp; P = πr² = π · 7² = 49π</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>36π cm²</b></td>
        <td>Średnica d = 12 → promień r = 6 cm! P = π · 6² = 36π cm² (nie 144π!)</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>P = 81π cm²</b> (r = 9 cm)</td>
        <td>2πr = 18π → 2r = 18 → r = 9 cm. P = π · 9² = 81π cm²</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
"""

with open(os.path.join(m08, "karta-supermocy-cheat-sheet.md"), "w") as f: f.write(cs_md_08)
with open(os.path.join(m08, "karta-supermocy-cheat-sheet.html"), "w") as f: f.write(cs_html_08)
with open(os.path.join(m08, "quizy-sukcesu-5-minut.md"), "w") as f: f.write(q_md_08)
with open(os.path.join(m08, "quizy-sukcesu-5-minut.html"), "w") as f: f.write(q_html_08)
print("Moduł 08 zapisany!")

# ==============================================================================
# MODUŁ 09: UKŁAD WSPÓŁRZĘDNYCH I GEOMETRIA ANALITYCZNA
# ==============================================================================
m09 = os.path.join(base, "09-uklad-wspolrzednych")
os.makedirs(m09, exist_ok=True)

cs_md_09 = """# KARTA SUPERMOCY: UKŁAD WSPÓŁRZĘDNYCH (Klasa 7 & 8)
## Sprytne Metody Nadii – Nawigacja GPS, Średnia Współrzędnych i Pitagoras na Kratkach

---

### 📍 1. NAWIGACJA GPS: PUNKT $(x, y)$
- **$x$ (oś pozioma $OX$):** idziesz po korytarzu w lewo ($-$) lub w prawo ($+$).
- **$y$ (oś pionowa $OY$):** jedziesz windą w dół ($-$) lub w górę ($+$).
> 🚨 **Pułapka zer:**
> - Punkt na osi $OX$ ma postać $(x, 0)$, np. $(5, 0)$.
> - Punkt na osi $OY$ ma postać $(0, y)$, np. $(0, -3)$.

---

### 🎯 2. ŚRODEK ODCINKA = ZWYKŁA ŚREDNIA ARYTMETYCZNA!
Masz punkty $A(x_1, y_1)$ i $B(x_2, y_2)$? Środek $S$ to po prostu średnia z ich współrzędnych:
$$S = \\left( \\frac{x_1 + x_2}{2}, \\; \\frac{y_1 + y_2}{2} \\right)$$
*Przykład: $A(1, 7)$ i $B(5, 3) \\implies S = \\left(\\frac{1+5}{2}, \\frac{7+3}{2}\\right) = \\mathbf{(3, 5)}$*

---

### 📏 3. DŁUGOŚĆ ODCINKA (Pitagoras na Kratkach)
Nie ucz się skomplikowanego wzoru na pamięć!
Dorysuj trójkąt prostokątny na kratkach i policz boki:
- Poziomy bok: $\\Delta x = |x_2 - x_1|$
- Pionowy bok: $\\Delta y = |y_2 - y_1|$
- Długość odcinka: **$d = \\sqrt{(\\Delta x)^2 + (\\Delta y)^2}$**
*Przykład: Od $(2, 1)$ do $(6, 4)$ $\\implies$ w poziomie 4, w pionie 3 $\\implies$ święta trójka 3-4-5 $\\implies$ **długość = 5!***

---

### 🪞 4. LUSTRA I SYMETRIE
- **Odbicie w osi $OX$:** punkt przeskakuje góra-dół $\\implies$ **$y$ zmienia znak**: $(x, \\mathbf{-y})$
  *$(3, 4) \\to (3, -4)$*
- **Odbicie w osi $OY$:** punkt przeskakuje lewo-prawo $\\implies$ **$x$ zmienia znak**: $(\\mathbf{-x}, y)$
  *$(3, 4) \\to (-3, 4)$*
- **Odbicie w początku $(0,0)$:** punkt przeskakuje po skosie $\\implies$ **OBA znaki się zmieniają**: $(\\mathbf{-x}, \\mathbf{-y})$
  *$(3, 4) \\to (-3, -4)$*

---

### 📦 5. METODA PUDEŁKA NA POLE FIGURY NA KRATKACH
Gdy masz obliczyć pole skośnego trójkąta w układzie współrzędnych:
1. Narysuj wokół niego prostokątne "pudełko" o bokach równoległych do osi.
2. Policz pole prostokąta: $P_{\\text{box}} = a \\cdot b$.
3. Odejmij pola narożnych trójkątów prostokątnych!
"""

cs_html_09 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Układ Współrzędnych</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #8b5cf6; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 15.5pt; color: #5b21b6; text-transform: uppercase; letter-spacing: 0.5px; }
  .header p { margin: 2px 0 0; font-size: 9.5pt; color: #7c3aed; font-weight: 600; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .card { background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 8px; padding: 7px 10px; margin-bottom: 6px; }
  .card-title { font-size: 10.8pt; font-weight: bold; color: #4c1d95; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; border-bottom: 1.5px solid #cbd5e1; padding-bottom: 2px; }
  .formula-box { background: #ffffff; border-left: 3.5px solid #8b5cf6; padding: 5px 8px; margin: 4px 0; font-family: "Courier New", monospace; font-size: 10pt; font-weight: bold; color: #0f172a; border-radius: 0 5px 5px 0; }
  .alert-box { background: #fff1f2; border: 1.5px solid #fecdd3; border-left: 3.5px solid #e11d48; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #9f1239; margin-top: 4px; }
  .success-box { background: #f0fdf4; border: 1.5px solid #bbf7d0; border-left: 3.5px solid #16a34a; padding: 5px 8px; border-radius: 4px; font-size: 9.3pt; color: #166534; margin-top: 4px; }
  ul { margin: 3px 0; padding-left: 17px; }
  li { margin-bottom: 2px; }
  .badge { display: inline-block; background: #ede9fe; color: #5b21b6; padding: 1px 5px; border-radius: 4px; font-size: 8.5pt; font-weight: bold; }
</style>
</head>
<body>

<div class="header">
  <h1>⚡ KARTA SUPERMOCY: UKŁAD WSPÓŁRZĘDNYCH (Klasa 7 & 8)</h1>
  <p>Sprytne Metody Nadii: Nawigacja GPS, Średnia Współrzędnych i Pitagoras na Kratkach</p>
</div>

<div class="grid-2">
  <!-- LEWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">📍 1. Nawigacja GPS: Punkt (x, y)</div>
      <ul>
        <li><b>x (oś pozioma OX):</b> idziesz po korytarzu lewo (−) / prawo (+).</li>
        <li><b>y (oś pionowa OY):</b> jedziesz windą dół (−) / góra (+).</li>
      </ul>
      <div class="formula-box">
        A(3, −4) → 3 w prawo, 4 w dół<br>
        B(−2, 5) → 2 w lewo, 5 w górę
      </div>
      <div class="alert-box">
        🚨 <b>Gdzie jest zero?</b><br>
        (4, 0) leży <b>na osi OX</b> &nbsp;|&nbsp; (0, −3) leży <b>na osi OY</b>!
      </div>
    </div>

    <div class="card">
      <div class="card-title">🎯 2. Środek Odcinka = Średnia!</div>
      <p style="margin: 2px 0;">Środek odcinka S to po prostu średnia arytmetyczna współrzędnych:</p>
      <div class="formula-box">
        S = [ (x₁ + x₂)/2 , (y₁ + y₂)/2 ]
      </div>
      <div class="success-box">
        💡 <b>Przykład:</b> A(−3, 8) i B(5, 2)<br>
        x<sub>S</sub> = (−3 + 5) / 2 = 2 / 2 = <b>1</b><br>
        y<sub>S</sub> = (8 + 2) / 2 = 10 / 2 = <b>5</b> &nbsp;→&nbsp; <b>S = (1, 5)</b>
      </div>
    </div>
  </div>

  <!-- PRAWA KOLUMNA -->
  <div>
    <div class="card">
      <div class="card-title">📏 3. Odległość = Pitagoras na Kratkach</div>
      <p style="margin: 2px 0;">Nie musisz wkuwać wzoru! Policz kratki:</p>
      <ul>
        <li>Krok w poziomie: Δx = |x₂ − x₁|</li>
        <li>Krok w pionie: Δy = |y₂ − y₁|</li>
        <li>Odległość d: <b>d² = (Δx)² + (Δy)²</b></li>
      </ul>
      <div class="formula-box">
        Od A(1, 2) do B(4, 6):<br>
        poziomo = 3, pionowo = 4 → trójka 3-4-5 → <b>d = 5</b>
      </div>
    </div>

    <div class="card">
      <div class="card-title">🪞 4. Lustra i Symetrie</div>
      <ul>
        <li><b>Odbicie w osi OX:</b> punkt spada góra/dół → <b>y zmienia znak</b>: (x, <b>−y</b>)<br>
          <i>(3, 7) → (3, −7)</i></li>
        <li><b>Odbicie w osi OY:</b> punkt przeskakuje lewo/prawo → <b>x zmienia znak</b>: (<b>−x</b>, y)<br>
          <i>(3, 7) → (−3, 7)</i></li>
        <li><b>Względem punktu (0,0):</b> <b>OBA zmieniają znak</b>: (<b>−x, −y</b>)<br>
          <i>(3, 7) → (−3, −7)</i></li>
      </ul>
    </div>

    <div class="card">
      <div class="card-title">📦 5. Metoda Pudełka na Pole Figury</div>
      <p style="margin: 2px 0; font-size: 9.3pt;">Skośny trójkąt na kratkach?</p>
      <ol style="margin: 2px 0; padding-left: 17px; font-size: 9.3pt;">
        <li>Obrysuj trójkąt prostokątem ("pudełkiem").</li>
        <li>Oblicz pole prostokąta: P = a · b.</li>
        <li>Odejmij 3 narożne trójkąty: P<sub>trójkąta</sub> = P<sub>box</sub> − (P₁ + P₂ + P₃).</li>
      </ol>
    </div>
  </div>
</div>

</body>
</html>
"""

q_md_09 = """# QUIZY SUKCESU: UKŁAD WSPÓŁRZĘDNYCH
## 4 Karty Treningowe po 5 Minut (Format Egzaminu Ósmoklasisty)

### KARTA 1: Odczytywanie i Położenie Punktów
1. W której ćwiartce układu leży punkt $P(-4, 7)$?
2. Podaj współrzędne punktu leżącego na osi $OY$ w odległości 5 jednostek poniżej osi $OX$.
3. Punkt $A(3, -2)$ przesunięto o 4 jednostki w lewo i 5 jednostek w górę. Jakie ma teraz współrzędne?

### KARTA 2: Środek Odcinka
1. Oblicz współrzędne środka odcinka o końcach $A(-5, 3)$ i $B(7, 9)$.
2. Punkt $S(2, 4)$ jest środkiem odcinka $AB$. Wiadomo, że $A(-2, 1)$. Wyznacz współrzędne punktu $B$.
3. Czy środek odcinka łączącego punkty $(4, -2)$ i $(-4, 2)$ leży w początku układu współrzędnych $(0,0)$?

### KARTA 3: Odległości i Pitagoras na Kratkach
1. Oblicz odległość między punktami $A(2, 3)$ i $B(2, 9)$.
2. Oblicz odległość między punktami $C(1, 2)$ i $D(4, 6)$.
3. Oblicz długość przeciwprostokątnej trójkąta o wierzchołkach $(0,0), (6,0), (0,8)$.

### KARTA 4: Symetrie i Pola Figur
1. Podaj współrzędne punktu symetrycznego do $K(-3, 5)$ względem osi $OX$.
2. Podaj współrzędne punktu symetrycznego do $M(4, -6)$ względem początku układu $(0,0)$.
3. Oblicz pole trójkąta o wierzchołkach $A(1, 1), B(7, 1), C(4, 6)$.
"""

q_html_09 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Układ Współrzędnych</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10pt; line-height: 1.35; }
  .header { text-align: center; border-bottom: 2px solid #8b5cf6; padding-bottom: 4px; margin-bottom: 12px; }
  .header h1 { margin: 0; font-size: 15pt; color: #5b21b6; }
  .header p { margin: 2px 0 0; font-size: 9pt; color: #7c3aed; }
  .quiz-card { background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 8px; padding: 10px 14px; margin-bottom: 14px; }
  .quiz-title { font-size: 11pt; font-weight: bold; color: #4c1d95; display: flex; justify-content: space-between; border-bottom: 1px solid #cbd5e1; padding-bottom: 4px; margin-bottom: 8px; }
  .task { margin-bottom: 8px; font-size: 10pt; }
  .task-num { font-weight: bold; color: #8b5cf6; margin-right: 4px; }
  .answer-space { border-bottom: 1px dashed #94a3b8; height: 26px; margin-top: 3px; display: flex; align-items: flex-end; color: #64748b; font-size: 8.5pt; font-style: italic; }
  .page-break { page-break-before: always; }
  .coach-card { background: #f0fdf4; border: 1.5px solid #86efac; border-radius: 8px; padding: 10px 14px; margin-bottom: 12px; }
  .coach-title { font-size: 11pt; font-weight: bold; color: #166534; margin-bottom: 6px; }
  table.answers { width: 100%; border-collapse: collapse; margin-top: 6px; font-size: 9pt; }
  table.answers th, table.answers td { border: 1px solid #cbd5e1; padding: 5px 8px; text-align: left; }
  table.answers th { background: #e2e8f0; color: #1e293b; }
</style>
</head>
<body>

<!-- STRONA 1: KARTA 1 & KARTA 2 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: UKŁAD WSPÓŁRZĘDNYCH</h1>
  <p>Trening Mikrokroków Nadii – 5 minut na kartę | Zegar start!</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 1: Odczytywanie i Położenie Punktów</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> W której ćwiartce układu leży punkt P(−4, 7)?
    <div class="answer-space">Ćwiartka: _____________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Podaj współrzędne punktu leżącego na osi OY, 5 jednostek poniżej osi OX.
    <div class="answer-space">Punkt = (____ , ____)</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Punkt A(3, −2) przesunięto o 4 w lewo i 5 w górę. Podaj nowe współrzędne.
    <div class="answer-space">A' = (____ , ____)</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 2: Środek Odcinka (Średnia)</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Oblicz współrzędne środka odcinka o końcach A(−5, 3) i B(7, 9).
    <div class="answer-space">S = (____ , ____)</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Punkt S(2, 4) jest środkiem odcinka AB. Wiadomo, że A(−2, 1). Wyznacz punkt B.
    <div class="answer-space">B = (____ , ____)</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Czy środek odcinka łączącego (4, −2) i (−4, 2) to początek układu (0,0)?
    <div class="answer-space">TAK / NIE, bo: _________________________</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 2: KARTA 3 & KARTA 4 -->
<div class="header">
  <h1>🎯 QUIZY SUKCESU: UKŁAD WSPÓŁRZĘDNYCH</h1>
  <p>Trening Mikrokroków Nadii – Część II</p>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 3: Odległości i Pitagoras na Kratkach</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Oblicz odległość między punktami A(2, 3) i B(2, 9).
    <div class="answer-space">|AB| = _______________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Oblicz odległość między C(1, 2) i D(4, 6) (policz kroki w poziomie i pionie).
    <div class="answer-space">|CD| = _______________________________</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Oblicz długość przeciwprostokątnej trójkąta o wierzchołkach (0,0), (6,0) i (0,8).
    <div class="answer-space">Długość = ____________________________</div>
  </div>
</div>

<div class="quiz-card">
  <div class="quiz-title">
    <span>KARTA 4: Symetrie i Pola Figur</span>
    <span style="font-size: 9pt; font-weight: normal; color: #64748b;">Czas: 5 min | Punkty: __/3</span>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 1.</span> Punkt symetryczny do K(−3, 5) względem osi OX ma współrzędne:
    <div class="answer-space">K' = (____ , ____)</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 2.</span> Punkt symetryczny do M(4, −6) względem początku (0,0) ma współrzędne:
    <div class="answer-space">M' = (____ , ____)</div>
  </div>
  <div class="task">
    <span class="task-num">Zadanie 3.</span> Oblicz pole trójkąta o wierzchołkach A(1, 1), B(7, 1) i C(4, 6).
    <div class="answer-space">Podstawa = ___ | Wysokość = ___ | P = ___</div>
  </div>
</div>

<div class="page-break"></div>

<!-- STRONA 3: PRZEWODNIK RODZICA I ODPOWIEDZI -->
<div class="coach-card">
  <div class="coach-title">🧠 PRZEWODNIK MENTORA (Dla Rodzica / Nauczyciela)</div>
  <p style="margin: 3px 0 6px;"><b>Wskazówki motywacyjne:</b></p>
  <ul>
    <li><b>Metafora windy:</b> Jeśli mylą się osie x i y, powiedz: <i>"Najpierw idziesz po korytarzu (x), dopiero potem wsiadasz do windy i jedziesz w górę/w dół (y)!"</i></li>
    <li><b>Środek to średnia:</b> Zamiast wzoru: <i>"Dodaj iksy i podziel przez 2, dodaj igreki i podziel przez 2 – jak średnia ocen!"</i></li>
    <li><b>Odbicie w lustrze:</b> Odbicie w osi OX zmienia znak tylko igreka (bo punkt przeskakuje pod/nad oś).</li>
  </ul>
</div>

<div class="quiz-card">
  <div class="quiz-title"><span>🔑 KLUCZ ODPOWIEDZI Z WYJAŚNIENIEM KROK PO KROKU</span></div>
  <table class="answers">
    <thead>
      <tr>
        <th style="width: 15%;">Karta</th>
        <th style="width: 15%;">Zadanie</th>
        <th style="width: 25%;">Prawidłowa Odpowiedź</th>
        <th>Kluczowy krok / Wyjaśnienie</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="3"><b>KARTA 1</b></td>
        <td>Zadanie 1</td>
        <td><b>II ćwiartka</b></td>
        <td>x &lt; 0 (lewo) i y &gt; 0 (góra) → II ćwiartka</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>(0, −5)</b></td>
        <td>Na osi OY x wynosi 0. W dół o 5 oznacza y = −5.</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>A'(−1, 3)</b></td>
        <td>x = 3 − 4 = −1; &nbsp; y = −2 + 5 = 3</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 2</b></td>
        <td>Zadanie 1</td>
        <td><b>S(1, 6)</b></td>
        <td>x = (−5 + 7)/2 = 2/2 = 1; &nbsp; y = (3 + 9)/2 = 12/2 = 6</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>B(6, 7)</b></td>
        <td>(−2 + x_B)/2 = 2 → −2 + x_B = 4 → x_B = 6; &nbsp; (1 + y_B)/2 = 4 → y_B = 7</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>TAK</b></td>
        <td>x = (4 − 4)/2 = 0; &nbsp; y = (−2 + 2)/2 = 0 → środek to (0,0)</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 3</b></td>
        <td>Zadanie 1</td>
        <td><b>6 jednostek</b></td>
        <td>Punkty leżą w pionie (ten sam x = 2). Odległość to |9 − 3| = 6</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>5 jednostek</b></td>
        <td>Δx = 4 − 1 = 3, Δy = 6 − 2 = 4. Święta trójka 3-4-5 → odległość = 5</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>10 jednostek</b></td>
        <td>Przyprostokątne leżą na osiach: 6 i 8. Święta trójka 6-8-10 → przeciwprostokątna = 10</td>
      </tr>

      <tr>
        <td rowspan="3"><b>KARTA 4</b></td>
        <td>Zadanie 1</td>
        <td><b>K'(−3, −5)</b></td>
        <td>Względem OX zmienia się znak y: 5 zamienia się w −5</td>
      </tr>
      <tr>
        <td>Zadanie 2</td>
        <td><b>M'(−4, 6)</b></td>
        <td>Względem (0,0) OBA znaki zmieniają się na przeciwne: 4 → −4, −6 → 6</td>
      </tr>
      <tr>
        <td>Zadanie 3</td>
        <td><b>P = 15</b></td>
        <td>Podstawa AB leży na linii y=1, długość a = 7 − 1 = 6. Wysokość h = 6 − 1 = 5. Pole = (6 · 5)/2 = 15</td>
      </tr>
    </tbody>
  </table>
</div>

</body>
</html>
"""

with open(os.path.join(m09, "karta-supermocy-cheat-sheet.md"), "w") as f: f.write(cs_md_09)
with open(os.path.join(m09, "karta-supermocy-cheat-sheet.html"), "w") as f: f.write(cs_html_09)
with open(os.path.join(m09, "quizy-sukcesu-5-minut.md"), "w") as f: f.write(q_md_09)
with open(os.path.join(m09, "quizy-sukcesu-5-minut.html"), "w") as f: f.write(q_html_09)
print("Moduł 09 zapisany!")
