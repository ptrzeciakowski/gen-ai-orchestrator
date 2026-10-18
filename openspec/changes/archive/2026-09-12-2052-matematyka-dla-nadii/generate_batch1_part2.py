import os

base = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-12-matematyka-dla-nadii"

# ==========================================
# MODUŁ 05: WYRAŻENIA ALGEBRAICZNE
# ==========================================
m05 = os.path.join(base, "05-wyrazenia-algebraiczne")
cs_md_05 = """# KARTA SUPERMOCY: WYRAŻENIA ALGEBRAICZNE (Klasa 7 & 8)
## Sprytne Metody Nadii – Kolorowe Rodziny, Prysznic i Wampir przed Nawiasem

---

### 🎨 1. ZASADA KOLOROWYCH RODZIN (Redukcja Wyrazów Podobnych)

W algebrze dodajesz TYLKO wyrazy z tej samej rodziny:
- $x$ to **lisy**
- $x^2$ to **lisy w kapeluszach** (nie sumują się ze zwykłymi lisami!)
- $y$ to **żyrafy**
- same liczby to **orzeszki**

> 🚨 **ŻELAZNA ZASADA ZNAKU:** Znak ($+$ lub $-$) przed liczbą należy do niej! Bierz go w kółko razem z wyrazem!
> $$3x - 5y + 4x - 2y = (3x + 4x) + (-5y - 2y) = \\mathbf{7x - 7y}$$

---

### 🚿 2. MNOŻENIE PRZEZ NAWIAS ("Prysznic dla Każdego")

Liczba stojąca przed nawiasem polewa KAŻDY składnik w środku:
$$a(b + c) = a \\cdot b + a \\cdot c$$
- $3(2x - 5) = 3 \\cdot 2x - 3 \\cdot 5 = \\mathbf{6x - 15}$
- $-4(3x - 2) = (-4) \\cdot 3x - (-4) \\cdot 2 = \\mathbf{-12x + 8}$ *(dwa minusy dają plus!)*

---

### 🧛 3. WAMPIR PRZED NAWIASEM (Antypułapka Minusa)

Gdy przed nawiasem stoi sam minus $-$, to jest to **wampir**: znika, ale **ODWRACA WSZYSTKIE ZNAKI W ŚRODKU NA PRZECIWNE**:
- $-(3x - 7) = \\mathbf{-3x + 7}$
- $-(2x + 5y - 4) = \\mathbf{-2x - 5y + 4}$
- $5x - (2x - 3) = 5x - 2x + 3 = \\mathbf{3x + 3}$ *(połowa uczniów zapomina zmienić drugi znak!)*

---

### 🤝 4. MNOŻENIE DWÓCH NAWIASÓW ("Każdy wita się z każdym")

$$(a + b)(c + d) = ac + ad + bc + bd$$
$$(x + 3)(x - 5) = x^2 - 5x + 3x - 15 = \\mathbf{x^2 - 2x - 15}$$
"""

cs_html_05 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Wyrażenia Algebraiczne</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #6366f1; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 17pt; color: #4f46e5; text-transform: uppercase; }
  .header .sub { font-size: 10pt; font-weight: 600; color: #475569; }
  .card { border-radius: 8px; padding: 7px 10px; border: 1.5px solid #cbd5e1; background: #fff; margin-bottom: 7px; }
  .card-indigo { border-color: #6366f1; background: #eef2ff; }
  .card-rose { border-color: #f43f5e; background: #fff1f2; }
  .card-amber { border-color: #f59e0b; background: #fffbeb; }
  .card-emerald { border-color: #10b981; background: #ecfdf5; }
  .card-title { font-size: 11pt; font-weight: bold; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; }
  .card-indigo .card-title { color: #4338ca; }
  .card-rose .card-title { color: #be123c; }
  .card-amber .card-title { color: #b45309; }
  .card-emerald .card-title { color: #047857; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .family-badge { display: inline-block; padding: 2px 6px; border-radius: 4px; font-weight: bold; margin: 1px; }
  .footer-tip { text-align: center; font-size: 8.8pt; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 4px; font-weight: 500; }
</style>
</head>
<body>
<div class="header">
  <h1>🦊 KARTA SUPERMOCY: WYRAŻENIA ALGEBRAICZNE (KLASA 7 & 8)</h1>
  <div class="sub">Ściągawka Nadii na biurko – Kolorowe rodziny, prysznic i wampir przed nawiasem!</div>
</div>

<div class="card card-indigo">
  <div class="card-title">🎨 1. ZASADA KOLOROWYCH RODZIN (REDUKCJA WYRAZÓW PODOBNYCH)</div>
  <div style="font-size: 8.8pt;">Dodajesz TYLKO wyrazy z tej samej rodziny. Pamiętaj: <b>znak przed liczbą należy do niej</b>!</div>
  <div style="background: #fff; padding: 5px 8px; border-radius: 6px; margin-top: 4px; border: 1px solid #c7d2fe; font-size: 9.5pt;">
    <span class="family-badge" style="background: #dbeafe; color: #1e40af;">+3x</span>
    <span class="family-badge" style="background: #fce7f3; color: #9d174d;">&minus;5y</span>
    <span class="family-badge" style="background: #dbeafe; color: #1e40af;">+4x</span>
    <span class="family-badge" style="background: #fce7f3; color: #9d174d;">&minus;2y</span>
    = (3x + 4x) + (&minus;5y &minus; 2y) = <b>7x &minus; 7y</b>
  </div>
  <div style="font-size: 8.5pt; color: #475569; margin-top: 2px;">
    &bull; <i>x to lisy, x<sup>2</sup> to lisy w kapeluszach (nie łącz ich!), y to żyrafy, same liczby to orzeszki!</i>
  </div>
</div>

<div class="grid-2">
  <div class="card card-emerald">
    <div class="card-title">🚿 2. PRYSZNIC DLA NAWIASU</div>
    <div style="font-size: 8.8pt;">Liczba z przodu polewa każdego w środku:</div>
    <div style="background: #fff; padding: 4px 6px; border-radius: 4px; margin-top: 3px; border: 1px solid #a7f3d0; font-size: 8.8pt;">
      <b>3(2x &minus; 5)</b> = 3&times;2x &minus; 3&times;5 = <b>6x &minus; 15</b><br>
      <b>&minus;4(3x &minus; 2)</b> = &minus;12x <b>+ 8</b> <i>(minus i minus = plus!)</i>
    </div>
  </div>

  <div class="card card-rose">
    <div class="card-title">🧛 3. WAMPIR PRZED NAWIASEM</div>
    <div style="font-size: 8.8pt;">Minus odwraca WSZYSTKIE znaki w środku:</div>
    <div style="background: #fff; padding: 4px 6px; border-radius: 4px; margin-top: 3px; border: 1px solid #fecdd3; font-size: 8.8pt;">
      &bull; <b>&minus;(3x &minus; 7)</b> = <b>&minus;3x + 7</b><br>
      &bull; <b>5x &minus; (2x &minus; 3)</b> = 5x &minus; 2x <b>+ 3</b> = <b>3x + 3</b><br>
      🚨 <i>Połowa uczniów zapomina zmienić drugi znak!</i>
    </div>
  </div>
</div>

<div class="card card-amber">
  <div class="card-title">🤝 4. MNOŻENIE DWÓCH NAWIASÓW ("KAŻDY Z KAŻDYM")</div>
  <div style="font-size: 8.8pt;">
    (a + b)(c + d) = ac + ad + bc + bd<br>
    <b>(x + 3)(x &minus; 5)</b> = x<sup>2</sup> &minus; 5x + 3x &minus; 15 = <b>x<sup>2</sup> &minus; 2x &minus; 15</b>
  </div>
</div>

<div class="footer-tip">
  💡 Pamiętaj Nadiu: Litera to po prostu puste pudełko na liczbę. Zawsze pilnuj znaku, który stoi przed nią! 🏆
</div>
</body>
</html>
"""

quiz_md_05 = """# QUIZY SUKCESU: WYRAŻENIA ALGEBRAICZNE (Klasa 7 & 8)
## 4 Karty Mikro-Treningu (Po 5 minut każda)

---

## 🌟 KARTA 1: REDUKCJA WYRAZÓW PODOBNYCH (RODZINY)
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Połącz Rodziny – 2 pkt)
Zredukuj wyrazy podobne:
- a) $4x + 3x - 2x = \\dots\\dots\\dots$
- b) $5a - 2b + 3a + 7b = \\dots\\dots\\dots$

### Zadanie 2 (Uważaj na Kapelusze! – 2 pkt)
Uprość wyrażenie: $3x^2 + 5x - 2x^2 + 4x =$
- Rodzina $x^2$: $\\dots\\dots\\dots$
- Rodzina $x$: $\\dots\\dots\\dots$
- Cały wynik: $\\dots\\dots\\dots$

### Zadanie 3 (Szybka Wartość – 2 pkt)
Oblicz wartość wyrażenia $2x - 3$ dla $x = 5$:
- Wynik: $\\dots\\dots\\dots$

---

## 🌟 KARTA 2: PRYSZNIC DLA NAWIASU
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Mnożenie przez Liczbę – 2 pkt)
Wymnóż nawias:
- a) $4(2x + 3) = \\dots\\dots\\dots$
- b) $5(3a - 4) = \\dots\\dots\\dots$

### Zadanie 2 (Minus z Przodu – 2 pkt)
Uważaj na znaki:
- a) $-2(3x - 5) = \\dots\\dots\\dots$
- b) $-3(4 - 2y) = \\dots\\dots\\dots$

### Zadanie 3 (Obwód Prostokąta – 2 pkt)
Prostokąt ma boki o długościach $x$ oraz $2x + 1$. Zapisz obwód w najprostszej postaci:
- $Obwód = 2 \\cdot x + 2(2x + 1) = \\dots\\dots\\dots$

---

## 🌟 KARTA 3: WAMPIR PRZED NAWIASEM
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Odwróć Znaki – 2 pkt)
Opuść nawiasy zmieniając znaki:
- a) $-(4x - 5) = \\dots\\dots\\dots$
- b) $-(2a + 3b - 1) = \\dots\\dots\\dots$

### Zadanie 2 (Pojedynek z Minusem – 2 pkt)
Uprość wyrażenie:
- a) $7x - (3x - 4) = 7x - 3x + [\\quad] = \\dots\\dots\\dots$
- b) $10 - (2x + 3) = \\dots\\dots\\dots$

### Zadanie 3 (Prawda czy Fałsz – 2 pkt)
Oceń zdanie:
- a) $5 - (x - 2) = 3 - x$  **[ P / F ]**
- b) $5 - (x - 2) = 7 - x$  **[ P / F ]**

---

## 🌟 KARTA 4: MNOŻENIE NAWIASÓW I POLA
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Każdy z Każdym – 2 pkt)
Wymnóż nawiasy:
- $(x + 2)(x + 5) = x^2 + 5x + 2x + 10 = \\dots\\dots\\dots$

### Zadanie 2 (Uwaga na Minus – 2 pkt)
Wymnóż nawiasy i zredukuj:
- $(x - 3)(x + 4) = x^2 + 4x - 3x - 12 = \\dots\\dots\\dots$

### Zadanie 3 (Pole Prostokąta – 2 pkt)
Zapisz pole prostokąta o bokach $(a + 3)$ i $(a + 2)$ w postaci sumy algebraicznej:
- $P = \\dots\\dots\\dots$

---

## 🗝️ KLUCZ ODPOWIEDZI (Dla Pawła)
- **Karta 1:** 1. a) $5x$, b) $8a + 5b$. 2. $x^2 + 9x$. 3. $2(5) - 3 = 7$.
- **Karta 2:** 1. a) $8x + 12$, b) $15a - 20$. 2. a) $-6x + 10$, b) $-12 + 6y$. 3. $6x + 2$.
- **Karta 3:** 1. a) $-4x + 5$, b) $-2a - 3b + 1$. 2. a) $4x + 4$, b) $7 - 2x$. 3. a) F, b) P (bo $5 + 2 = 7$!).
- **Karta 4:** 1. $x^2 + 7x + 10$. 2. $x^2 + x - 12$. 3. $a^2 + 5a + 6$.
"""

quiz_html_05 = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Wyrażenia Algebraiczne</title>
<style>
  @page {{ size: A4 portrait; margin: 10mm 12mm; }}
  * {{ box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.5pt; line-height: 1.35; }}
  .page-break {{ page-break-after: always; }}
  .header-main {{ text-align: center; border-bottom: 2.5px solid #6366f1; padding-bottom: 5px; margin-bottom: 12px; }}
  .header-main h1 {{ margin: 0; font-size: 16pt; color: #4338ca; }}
  .header-main p {{ margin: 2px 0 0 0; font-size: 9.5pt; color: #64748b; }}
  .quiz-card {{ border: 2px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; margin-bottom: 14px; background: #fff; }}
  .quiz-1 {{ border-color: #6366f1; background: #f8fafc; }}
  .quiz-2 {{ border-color: #10b981; background: #f8fafc; }}
  .quiz-3 {{ border-color: #f43f5e; background: #f8fafc; }}
  .quiz-4 {{ border-color: #f59e0b; background: #f8fafc; }}
  .quiz-header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px dashed #cbd5e1; padding-bottom: 6px; margin-bottom: 8px; }}
  .quiz-title {{ font-size: 12pt; font-weight: bold; }}
  .quiz-1 .quiz-title {{ color: #4338ca; }}
  .quiz-2 .quiz-title {{ color: #047857; }}
  .quiz-3 .quiz-title {{ color: #be123c; }}
  .quiz-4 .quiz-title {{ color: #b45309; }}
  .quiz-meta {{ font-size: 9pt; font-weight: 600; color: #475569; }}
  .task {{ margin-bottom: 8px; }}
  .task-title {{ font-size: 9.8pt; font-weight: bold; color: #334155; margin-bottom: 3px; }}
  .task-body {{ font-size: 10pt; padding-left: 10px; }}
  .blank-line {{ display: inline-block; border-bottom: 1.5px solid #94a3b8; min-width: 50px; height: 16px; vertical-align: middle; margin: 0 4px; }}
  .rank-box {{ margin-top: 8px; padding-top: 6px; border-top: 1px dotted #cbd5e1; display: flex; justify-content: space-between; font-size: 8.5pt; color: #475569; }}
  .key-section {{ background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 10px 14px; margin-bottom: 10px; }}
  .key-title {{ font-weight: bold; color: #1e293b; font-size: 10.5pt; margin-bottom: 4px; }}
  .tip-box {{ background: #fef3c7; border-left: 4px solid #f59e0b; padding: 6px 10px; font-size: 9pt; color: #92400e; margin-top: 4px; border-radius: 0 4px 4px 0; }}
</style>
</head>
<body>

<div class="header-main">
  <h1>🦊 QUIZY SUKCESU: WYRAŻENIA ALGEBRAICZNE (KLASA 7 & 8)</h1>
  <p>5-minutowe wyzwania pewności siebie • 1 karta naraz • Po każdej karcie 3 minuty przerwy!</p>
</div>

<div class="quiz-card quiz-1">
  <div class="quiz-header">
    <div class="quiz-title">🎯 KARTA 1: REDUKCJA WYRAZÓW PODOBNYCH (RODZINY)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Połącz Rodziny – 2 pkt)</div>
    <div class="task-body">
      Zredukuj wyrazy podobne:
      <div style="margin: 4px 0;">
        a) 4x + 3x &minus; 2x = <span class="blank-line"></span><br>
        b) 5a &minus; 2b + 3a + 7b = <span class="blank-line"></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Uważaj na Kapelusze! – 2 pkt)</div>
    <div class="task-body">
      Uprość: 3x<sup>2</sup> + 5x &minus; 2x<sup>2</sup> + 4x = <span class="blank-line" style="min-width:100px;"></span>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Szybka Wartość – 2 pkt)</div>
    <div class="task-body">
      Oblicz wartość 2x &minus; 3 dla x = 5: &nbsp; 2 &times; 5 &minus; 3 = <span class="blank-line"></span>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Królowa Algebry!</b></span>
    <span>[ ] 3–4 pkt: <b>Sprytne Oko!</b></span>
    <span>[ ] 1–2 pkt: <b>Dobry początek!</b></span>
  </div>
</div>

<div class="quiz-card quiz-2">
  <div class="quiz-header">
    <div class="quiz-title">🚿 KARTA 2: PRYSZNIC DLA NAWIASU</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Mnożenie przez Liczbę – 2 pkt)</div>
    <div class="task-body">
      Wymnóż nawias:
      <div style="margin: 4px 0;">
        a) 4(2x + 3) = <span class="blank-line"></span><br>
        b) 5(3a &minus; 4) = <span class="blank-line"></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Minus z Przodu – 2 pkt)</div>
    <div class="task-body">
      Uważaj na podwójny minus:
      <div style="margin: 4px 0;">
        a) &minus;2(3x &minus; 5) = <span class="blank-line"></span><br>
        b) &minus;3(4 &minus; 2y) = <span class="blank-line"></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Obwód Prostokąta – 2 pkt)</div>
    <div class="task-body">
      Boki to x oraz 2x + 1. Obwód = 2x + 2(2x + 1) = 2x + 4x + 2 = <span class="blank-line"></span>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Czysta Perfekcja!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobra Robota!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🦊 QUIZY SUKCESU: WYRAŻENIA ALGEBRAICZNE (CZĘŚĆ 2)</h1>
  <p>Skupienie na 5 minut • Tylko 3 zadania na karcie • Poskramiamy wampiry!</p>
</div>

<div class="quiz-card quiz-3">
  <div class="quiz-header">
    <div class="quiz-title">🧛 KARTA 3: WAMPIR PRZED NAWIASEM</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Odwróć Znaki – 2 pkt)</div>
    <div class="task-body">
      Opuść nawias:
      <div style="margin: 4px 0;">
        a) &minus;(4x &minus; 5) = <span class="blank-line"></span><br>
        b) &minus;(2a + 3b &minus; 1) = <span class="blank-line"></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Pojedynek z Minusem – 2 pkt)</div>
    <div class="task-body">
      Uprość wyrażenie:
      <div style="margin: 4px 0;">
        a) 7x &minus; (3x &minus; 4) = 7x &minus; 3x + 4 = <span class="blank-line"></span><br>
        b) 10 &minus; (2x + 3) = <span class="blank-line"></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Prawda czy Fałsz – 2 pkt)</div>
    <div class="task-body">
      Oceń zdanie: 5 &minus; (x &minus; 2) jest równe:<br>
      a) 3 &minus; x &nbsp; [ &nbsp; ] &nbsp;&bull;&nbsp; b) 7 &minus; x &nbsp; [ &nbsp; ]
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Pogromczyni Wampirów!</b></span>
    <span>[ ] 3–4 pkt: <b>Bystra Obserwatorka!</b></span>
    <span>[ ] 1–2 pkt: <b>Dobra próba!</b></span>
  </div>
</div>

<div class="quiz-card quiz-4">
  <div class="quiz-header">
    <div class="quiz-title">🤝 KARTA 4: MNOŻENIE NAWIASÓW I POLA</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Każdy z Każdym – 2 pkt)</div>
    <div class="task-body">
      Wymnóż: (x + 2)(x + 5) = x<sup>2</sup> + 5x + 2x + 10 = <span class="blank-line"></span>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Uwaga na Minus – 2 pkt)</div>
    <div class="task-body">
      (x &minus; 3)(x + 4) = x<sup>2</sup> + 4x &minus; 3x &minus; 12 = <span class="blank-line"></span>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Pole Prostokąta – 2 pkt)</div>
    <div class="task-body">
      Boki to a + 3 oraz a + 2. Pole = (a + 3)(a + 2) = <span class="blank-line"></span>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Architektka Algebry!</b></span>
    <span>[ ] 3–4 pkt: <b>Celny Rachunek!</b></span>
    <span>[ ] 1–2 pkt: <b>Do przodu!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🗝️ KLUCZ ODPOWIEDZI I WSKAZÓWKI COACHINGOWE (ALGEBRA)</h1>
  <p>Ściągawka dla Pawła: jak utrwalać nawyk ochrony znaków</p>
</div>

<div class="key-section">
  <div class="key-title">Karta 1: Redukcja Wyrazów Podobnych</div>
  <b>1.</b> a) 5x, b) 8a + 5b.<br>
  <b>2.</b> x<sup>2</sup> + 9x.<br>
  <b>3.</b> 7.
  <div class="tip-box"><b>💡 Jak chwalić:</b> Zwróć uwagę, że nie połączyła x z x<sup>2</sup>: <i>"Brawo, nie dałaś lisom założyć kapeluszy, to dwie różne rodziny!"</i></div>
</div>

<div class="key-section">
  <div class="key-title">Karta 2: Prysznic dla Nawiasu</div>
  <b>1.</b> a) 8x + 12, b) 15a &minus; 20.<br>
  <b>2.</b> a) &minus;6x + 10, b) &minus;12 + 6y.<br>
  <b>3.</b> 6x + 2.
  <div class="tip-box"><b>💡 Uwaga coachingowa:</b> Zawsze pilnuj, by liczba przed nawiasem pomnożyła WSZYSTKIE wyrazy, a nie tylko pierwszy!</div>
</div>

<div class="key-section">
  <div class="key-title">Karta 3: Wampir przed Nawiasem</div>
  <b>1.</b> a) &minus;4x + 5, b) &minus;2a &minus; 3b + 1.<br>
  <b>2.</b> a) 4x + 4, b) 7 &minus; 2x.<br>
  <b>3.</b> a) F, b) P (bo 5 &minus; (&minus;2) = 5 + 2 = 7).
  <div class="tip-box"><b>💡 Metafora wampira:</b> Pamiętaj o wampirze: wchodzi do nawiasu i odwraca znaki do góry nogami!</div>
</div>

<div class="key-section">
  <div class="key-title">Karta 4: Mnożenie Nawiasów i Pola</div>
  <b>1.</b> x<sup>2</sup> + 7x + 10.<br>
  <b>2.</b> x<sup>2</sup> + x &minus; 12.<br>
  <b>3.</b> a<sup>2</sup> + 5a + 6.
  <div class="tip-box"><b>💡 Rytuał:</b> Cztery strzałki mnożenia: góra-góra, góra-dół, dół-góra, dół-dół. Uczeń ma pełną kontrolę nad procesem!</div>
</div>
</body>
</html>
"""

with open(f"{m05}/karta-supermocy-cheat-sheet.md", "w") as f: f.write(cs_md_05.strip() + "\n")
with open(f"{m05}/karta-supermocy-cheat-sheet.html", "w") as f: f.write(cs_html_05.strip())
with open(f"{m05}/quizy-sukcesu-5-minut.md", "w") as f: f.write(quiz_md_05.strip() + "\n")
with open(f"{m05}/quizy-sukcesu-5-minut.html", "w") as f: f.write(quiz_html_05.strip())
print("Moduł 05 gotowy!")

