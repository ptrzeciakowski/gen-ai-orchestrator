import os, subprocess

base = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-12-matematyka-dla-nadii"
pdf_script = "/Users/pawel/git/gen-ai-orchestrator/.ai/skills/matematyka-supermoce/scripts/generate_pdf.py"

# --- MODUŁ 03: PIERWIASTKI ---
m03 = os.path.join(base, "03-pierwiastki")
cs_md_03 = """# KARTA SUPERMOCY: PIERWIASTKI (Klasa 7 & 8)
## Sprytne Metody Nadii – Wyłączanie Czynnika, Szacowanie i Antypułapki

---

### 🚀 1. KLUB ZNANYCH PIERWIASTKÓW (Złota Tabela do Pamięci)

Gdy widzisz pierwiastek kwadratowy, szukaj jego "ojca" (liczby podniesionej do potęgi 2):

| Pierwiastek | Wynik | Pierwiastek | Wynik | Pierwiastek Sześcienny | Wynik |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $\\sqrt{4}$ | **2** | $\\sqrt{81}$ | **9** | $\\sqrt[3]{1}$ | **1** |
| $\\sqrt{9}$ | **3** | $\\sqrt{100}$ | **10** | $\\sqrt[3]{8}$ | **2** |
| $\\sqrt{16}$ | **4** | $\\sqrt{121}$ | **11** | $\\sqrt[3]{27}$ | **3** |
| $\\sqrt{25}$ | **5** | $\\sqrt{144}$ | **12** | $\\sqrt[3]{64}$ | **4** |
| $\\sqrt{36}$ | **6** | $\\sqrt{169}$ | **13** | $\\sqrt[3]{125}$ | **5** |
| $\\sqrt{49}$ | **7** | $\\sqrt{196}$ | **14** | $\\sqrt[3]{1000}$ | **10** |
| $\\sqrt{64}$ | **8** | $\\sqrt{225}$ | **15** | $\\sqrt[3]{-8}$ | **-2** |

---

### 🧩 2. WYŁĄCZANIE CZYNNIKA ("Szukaj Magicznego Kwadratu: 4, 9, 25, 100")

Zamiast żmudnego rozkładania na drzewko, rozbij liczbę pod pierwiastkiem na iloczyn ze znajomym kwadratem:
- $\\sqrt{12} = \\sqrt{4 \\cdot 3} = \\sqrt{4} \\cdot \\sqrt{3} = \\mathbf{2\\sqrt{3}}$
- $\\sqrt{18} = \\sqrt{9 \\cdot 2} = \\sqrt{9} \\cdot \\sqrt{2} = \\mathbf{3\\sqrt{2}}$
- $\\sqrt{50} = \\sqrt{25 \\cdot 2} = \\sqrt{25} \\cdot \\sqrt{2} = \\mathbf{5\\sqrt{2}}$
- $\\sqrt{75} = \\sqrt{25 \\cdot 3} = \\sqrt{25} \\cdot \\sqrt{3} = \\mathbf{5\\sqrt{3}}$
- $\\sqrt{200} = \\sqrt{100 \\cdot 2} = \\sqrt{100} \\cdot \\sqrt{2} = \\mathbf{10\\sqrt{2}}$

---

### 🎯 3. SZACOWANIE PIERWIASTKA NA OSI (Pomiędzy czym a czym?)

Szukasz pierwiastków "idealnych" stojących tuż przed i tuż po Twojej liczbie:
- **Ile to $\\sqrt{41}$?**
  Stoi między $\\sqrt{36}=6$ a $\\sqrt{49}=7$. Zatem $\\sqrt{41}$ leży między **$6$ a $7$** (ok. $6{,}4$).
- **Ile to $\\sqrt[3]{20}$?**
  Stoi między $\\sqrt[3]{8}=2$ a $\\sqrt[3]{27}=3$. Zatem $\\sqrt[3]{20}$ leży między **$2$ a $3$** (ok. $2{,}7$).

---

### 🚨 4. NAJWIĘKSZA PUŁAPKA CKE: DODAWANIE POD PIERWIASTKIEM!

- ❌ $\\sqrt{9 + 16} \\neq \\sqrt{9} + \\sqrt{16} = 3 + 4 = 7$! *(NIGDY nie rozrywaj dodawania!)*
- ✅ **NAJPIERW DODAJ POD PIERWIASTKIEM:** $\\sqrt{9 + 16} = \\sqrt{25} = \\mathbf{5}$!
- ❌ $\\sqrt{100 - 36} \\neq 10 - 6 = 4$!
- ✅ **NAJPIERW ODEJMIJ:** $\\sqrt{100 - 36} = \\sqrt{64} = \\mathbf{8}$!
- ⭐ Mnożenie i dzielenie MOŻNA łączyć: $\\sqrt{a} \\cdot \\sqrt{b} = \\sqrt{a \\cdot b}$ oraz $\\frac{\\sqrt{a}}{\\sqrt{b}} = \\sqrt{\\frac{a}{b}}$.
"""

cs_html_03 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Pierwiastki</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #0d9488; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 17pt; color: #0f766e; text-transform: uppercase; }
  .header .sub { font-size: 10pt; font-weight: 600; color: #475569; }
  .card { border-radius: 8px; padding: 7px 10px; border: 1.5px solid #cbd5e1; background: #fff; margin-bottom: 7px; }
  .card-teal { border-color: #0d9488; background: #f0fdfa; }
  .card-rose { border-color: #f43f5e; background: #fff1f2; }
  .card-amber { border-color: #f59e0b; background: #fffbeb; }
  .card-blue { border-color: #3b82f6; background: #eff6ff; }
  .card-title { font-size: 11pt; font-weight: bold; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; }
  .card-teal .card-title { color: #0f766e; }
  .card-rose .card-title { color: #be123c; }
  .card-amber .card-title { color: #b45309; }
  .card-blue .card-title { color: #1d4ed8; }
  table.p-table { width: 100%; border-collapse: collapse; font-size: 9pt; background: #fff; border-radius: 6px; overflow: hidden; }
  table.p-table th, table.p-table td { padding: 3px 6px; border: 1px solid #ccfbf1; text-align: center; }
  table.p-table th { background: #99f6e4; color: #115e59; font-weight: bold; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .footer-tip { text-align: center; font-size: 8.8pt; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 4px; font-weight: 500; }
</style>
</head>
<body>
<div class="header">
  <h1>🌿 KARTA SUPERMOCY: PIERWIASTKI (KLASA 7 & 8)</h1>
  <div class="sub">Ściągawka Nadii na biurko – Wyłączanie czynnika, szacowanie i antypułapki CKE!</div>
</div>

<div class="card card-teal">
  <div class="card-title">🚀 1. KLUB ZNANYCH PIERWIASTKÓW (ZŁOTA TABELA)</div>
  <table class="p-table">
    <thead>
      <tr><th>Kwadratowe</th><th>Wynik</th><th>Kwadratowe</th><th>Wynik</th><th>Sześcienne</th><th>Wynik</th></tr>
    </thead>
    <tbody>
      <tr><td>&radic;4</td><td><b>2</b></td><td>&radic;81</td><td><b>9</b></td><td><sup>3</sup>&radic;1</td><td><b>1</b></td></tr>
      <tr><td>&radic;9</td><td><b>3</b></td><td>&radic;100</td><td><b>10</b></td><td><sup>3</sup>&radic;8</td><td><b>2</b></td></tr>
      <tr><td>&radic;16</td><td><b>4</b></td><td>&radic;121</td><td><b>11</b></td><td><sup>3</sup>&radic;27</td><td><b>3</b></td></tr>
      <tr><td>&radic;25</td><td><b>5</b></td><td>&radic;144</td><td><b>12</b></td><td><sup>3</sup>&radic;64</td><td><b>4</b></td></tr>
      <tr><td>&radic;36</td><td><b>6</b></td><td>&radic;169</td><td><b>13</b></td><td><sup>3</sup>&radic;125</td><td><b>5</b></td></tr>
      <tr><td>&radic;49</td><td><b>7</b></td><td>&radic;196</td><td><b>14</b></td><td><sup>3</sup>&radic;1000</td><td><b>10</b></td></tr>
      <tr><td>&radic;64</td><td><b>8</b></td><td>&radic;225</td><td><b>15</b></td><td><sup>3</sup>&radic;(&minus;8)</td><td><b>&minus;2</b></td></tr>
    </tbody>
  </table>
</div>

<div class="grid-2">
  <div class="card card-blue">
    <div class="card-title">🧩 2. WYŁĄCZANIE CZYNNIKA</div>
    <div style="font-size: 8.8pt;">Szukaj magicznego kwadratu: <b>4, 9, 25, 100</b>:</div>
    <div style="font-size: 8.8pt; background: #fff; padding: 4px 6px; border-radius: 4px; margin-top: 3px; border: 1px solid #bfdbfe;">
      &bull; &radic;12 = &radic;(4&times;3) = <b>2&radic;3</b><br>
      &bull; &radic;18 = &radic;(9&times;2) = <b>3&radic;2</b><br>
      &bull; &radic;50 = &radic;(25&times;2) = <b>5&radic;2</b><br>
      &bull; &radic;75 = &radic;(25&times;3) = <b>5&radic;3</b><br>
      &bull; &radic;200 = &radic;(100&times;2) = <b>10&radic;2</b>
    </div>
  </div>

  <div class="card card-amber">
    <div class="card-title">🎯 3. SZACOWANIE NA OSI</div>
    <div style="font-size: 8.8pt;">Szukaj idealnych sąsiadów:</div>
    <div style="font-size: 8.8pt; background: #fff; padding: 4px 6px; border-radius: 4px; margin-top: 3px; border: 1px solid #fde68a;">
      <b>Ile to &radic;41?</b><br>
      Leży między &radic;36 = 6 a &radic;49 = 7.<br>
      Zatem &radic;41 to <b>między 6 a 7</b> (&approx; 6,4).<br><br>
      <b>Ile to <sup>3</sup>&radic;20?</b><br>
      Leży między <sup>3</sup>&radic;8 = 2 a <sup>3</sup>&radic;27 = 3.<br>
      Zatem to <b>między 2 a 3</b> (&approx; 2,7).
    </div>
  </div>
</div>

<div class="card card-rose">
  <div class="card-title">🚨 4. NAJWIĘKSZA PUŁAPKA CKE: DODAWANIE POD PIERWIASTKIEM!</div>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px; font-size: 8.8pt;">
    <div style="background: #fff; padding: 4px 6px; border-radius: 4px; border: 1px solid #fecdd3;">
      ❌ <b>BŁĄD:</b> &radic;(9 + 16) &ne; &radic;9 + &radic;16 = 3 + 4 = 7!<br>
      ✅ <b>POPRAWNIE:</b> &radic;(9 + 16) = &radic;25 = <b>5</b>!
    </div>
    <div style="background: #fff; padding: 4px 6px; border-radius: 4px; border: 1px solid #fecdd3;">
      ❌ <b>BŁĄD:</b> &radic;(100 &minus; 36) &ne; 10 &minus; 6 = 4!<br>
      ✅ <b>POPRAWNIE:</b> &radic;(100 &minus; 36) = &radic;64 = <b>8</b>!
    </div>
  </div>
  <div style="font-size: 8.5pt; color: #9f1239; margin-top: 3px;">
    ⭐ Mnożenie i dzielenie MOŻNA łączyć: &radic;a &times; &radic;b = &radic;(a&times;b) oraz &radic;a / &radic;b = &radic;(a/b).
  </div>
</div>

<div class="footer-tip">
  💡 Pamiętaj Nadiu: Znak pierwiastka to parasol. Zanim go zwiniesz, musisz policzyć to, co pod nim jest! 🏆
</div>
</body>
</html>
"""

quiz_md_03 = """# QUIZY SUKCESU: PIERWIASTKI (Klasa 7 & 8)
## 4 Karty Mikro-Treningu (Po 5 minut każda)

---

## 🌟 KARTA 1: SZYBKIE PIERWIASTKI I SZACOWANIE
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Rozgrzewka – 2 pkt)
Oblicz w pamięci:
- a) $\\sqrt{64} = \\dots\\dots\\dots$ \t b) $\\sqrt{144} = \\dots\\dots\\dots$
- c) $\\sqrt[3]{27} = \\dots\\dots\\dots$ \t d) $\\sqrt[3]{-8} = \\dots\\dots\\dots$

### Zadanie 2 (Szacowanie – 2 pkt)
Wskaż między jakimi dwiema kolejnymi liczbami całkowitymi leży podany pierwiastek:
- a) $\\sqrt{30}$ leży między $\\dots\\dots$ a $\\dots\\dots$ (bo $\\sqrt{25} < \\sqrt{30} < \\sqrt{36}$)
- b) $\\sqrt{50}$ leży między $\\dots\\dots$ a $\\dots\\dots$

### Zadanie 3 (Mistrz Osi – 2 pkt)
Która liczba jest większa: $\\sqrt{17}$ czy $4$?
- Odpowiedź: $\\dots\\dots\\dots$, ponieważ $\\sqrt{17} \\dots\\dots \\sqrt{16}$.

---

## 🌟 KARTA 2: WYŁĄCZANIE CZYNNIKA PRZED PIERWIASTEK
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Magiczna Czwórka – 2 pkt)
Rozbij na $4 \\cdot [\\quad]$ i wyłącz $2$ przed pierwiastek:
- a) $\\sqrt{20} = \\sqrt{4 \\cdot 5} = \\dots\\dots\\dots$
- b) $\\sqrt{28} = \\sqrt{4 \\cdot 7} = \\dots\\dots\\dots$

### Zadanie 2 (Magiczna Dziewiątka i 25 – 2 pkt)
Wyłącz czynnik przed pierwiastek:
- a) $\\sqrt{45} = \\sqrt{9 \\cdot 5} = \\dots\\dots\\dots$
- b) $\\sqrt{75} = \\sqrt{25 \\cdot 3} = \\dots\\dots\\dots$

### Zadanie 3 (Zadanie Egzaminacyjne – 2 pkt)
Zapisz w najprostszej postaci: $2\\sqrt{18} = 2 \\cdot (3\\sqrt{2}) = \\dots\\dots\\dots$

---

## 🌟 KARTA 3: DZIAŁANIA NA PIERWIASTKACH
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Mnożenie i Dzielenie – 2 pkt)
Wrzuć pod jeden pierwiastek i oblicz:
- a) $\\sqrt{2} \\cdot \\sqrt{8} = \\sqrt{2 \\cdot 8} = \\sqrt{\\dots\\dots} = \\dots\\dots$
- b) $\\frac{\\sqrt{75}}{\\sqrt{3}} = \\sqrt{\\frac{75}{3}} = \\sqrt{\\dots\\dots} = \\dots\\dots$

### Zadanie 2 (Dodawanie takich samych pierwiastków – 2 pkt)
Pamiętaj: $\\sqrt{3}$ traktuj jak jabłko!
- a) $3\\sqrt{5} + 4\\sqrt{5} = \\dots\\dots\\dots$
- b) $7\\sqrt{2} - 2\\sqrt{2} = \\dots\\dots\\dots$

### Zadanie 3 (Uprość Wyrażenie – 2 pkt)
Oblicz: $\\sqrt{50} + \\sqrt{18} = 5\\sqrt{2} + 3\\sqrt{2} = \\dots\\dots\\dots$

---

## 🌟 KARTA 4: ANTYPUŁAPKA DODAWANIA POD ZNAKIEM PIERWIASTKA
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Prawda czy Fałsz – 2 pkt)
Oceń prawdziwość zdań:
- a) $\\sqrt{36 + 64} = 6 + 8 = 14$  **[ P / F ]**
- b) $\\sqrt{36 + 64} = \\sqrt{100} = 10$  **[ P / F ]**

### Zadanie 2 (Oblicz Poprawnie – 2 pkt)
Najpierw wykonaj działanie pod pierwiastkiem:
- a) $\\sqrt{100 - 64} = \\sqrt{\\dots\\dots} = \\dots\\dots$
- b) $\\sqrt{1 + \\frac{9}{16}} = \\sqrt{\\frac{25}{16}} = \\dots\\dots$

### Zadanie 3 (Finał Egzaminacyjny CKE – 2 pkt)
Wartość wyrażenia $\\sqrt{25 - 9}$ wynosi:
- **A.** 4 \t **B.** 2 \t **C.** 16 \t **D.** 8

---

## 🗝️ KLUCZ ODPOWIEDZI (Dla Pawła)
- **Karta 1:** 1. a) 8, b) 12, c) 3, d) -2. 2. a) 5 i 6, b) 7 i 8. 3. $\\sqrt{17} > 4$.
- **Karta 2:** 1. a) $2\\sqrt{5}$, b) $2\\sqrt{7}$. 2. a) $3\\sqrt{5}$, b) $5\\sqrt{3}$. 3. $6\\sqrt{2}$.
- **Karta 3:** 1. a) $\\sqrt{16}=4$, b) $\\sqrt{25}=5$. 2. a) $7\\sqrt{5}$, b) $5\\sqrt{2}$. 3. $8\\sqrt{2}$.
- **Karta 4:** 1. a) F, b) P. 2. a) $\\sqrt{36}=6$, b) $\\frac{5}{4} = 1\\frac{1}{4}$. 3. Odp. A (bo $\\sqrt{16}=4$).
*Wskazówka:* Zwróć uwagę na Zadanie 1 z Karty 4 – połowa uczniów w Polsce daje się na to nabrać!
"""

quiz_html_03 = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Pierwiastki</title>
<style>
  @page {{ size: A4 portrait; margin: 10mm 12mm; }}
  * {{ box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.5pt; line-height: 1.35; }}
  .page-break {{ page-break-after: always; }}
  .header-main {{ text-align: center; border-bottom: 2.5px solid #0d9488; padding-bottom: 5px; margin-bottom: 12px; }}
  .header-main h1 {{ margin: 0; font-size: 16pt; color: #0f766e; }}
  .header-main p {{ margin: 2px 0 0 0; font-size: 9.5pt; color: #64748b; }}
  .quiz-card {{ border: 2px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; margin-bottom: 14px; background: #fff; }}
  .quiz-1 {{ border-color: #0d9488; background: #f8fafc; }}
  .quiz-2 {{ border-color: #3b82f6; background: #f8fafc; }}
  .quiz-3 {{ border-color: #8b5cf6; background: #f8fafc; }}
  .quiz-4 {{ border-color: #f43f5e; background: #f8fafc; }}
  .quiz-header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px dashed #cbd5e1; padding-bottom: 6px; margin-bottom: 8px; }}
  .quiz-title {{ font-size: 12pt; font-weight: bold; }}
  .quiz-1 .quiz-title {{ color: #0f766e; }}
  .quiz-2 .quiz-title {{ color: #1d4ed8; }}
  .quiz-3 .quiz-title {{ color: #6d28d9; }}
  .quiz-4 .quiz-title {{ color: #be123c; }}
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
  <h1>🌿 QUIZY SUKCESU: PIERWIASTKI (KLASA 7 & 8)</h1>
  <p>5-minutowe wyzwania pewności siebie • 1 karta naraz • Po każdej karcie 3 minuty przerwy!</p>
</div>

<div class="quiz-card quiz-1">
  <div class="quiz-header">
    <div class="quiz-title">🎯 KARTA 1: SZYBKIE PIERWIASTKI I SZACOWANIE</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Rozgrzewka – 2 pkt)</div>
    <div class="task-body">
      Oblicz w pamięci:
      <div style="margin: 4px 0; display: flex; gap: 30px;">
        <span>a) &radic;64 = <span class="blank-line"></span></span>
        <span>b) &radic;144 = <span class="blank-line"></span></span>
        <span>c) <sup>3</sup>&radic;27 = <span class="blank-line"></span></span>
        <span>d) <sup>3</sup>&radic;(&minus;8) = <span class="blank-line"></span></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Szacowanie – 2 pkt)</div>
    <div class="task-body">
      Wskaż między jakimi dwiema kolejnymi liczbami całkowitymi leży pierwiastek:
      <div style="margin: 4px 0;">
        a) &radic;30 leży między <span class="blank-line"></span> a <span class="blank-line"></span> (bo &radic;25 &lt; &radic;30 &lt; &radic;36)<br>
        b) &radic;50 leży między <span class="blank-line"></span> a <span class="blank-line"></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Mistrz Osi – 2 pkt)</div>
    <div class="task-body">
      Która liczba jest większa: <b>&radic;17</b> czy <b>4</b>?<br>
      Odpowiedź: <span class="blank-line" style="min-width: 80px;"></span>, ponieważ &radic;17 jest większy od &radic;16.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Czarodziejka Pierwiastków!</b></span>
    <span>[ ] 3–4 pkt: <b>Bystre Oko!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok do przodu!</b></span>
  </div>
</div>

<div class="quiz-card quiz-2">
  <div class="quiz-header">
    <div class="quiz-title">🧩 KARTA 2: WYŁĄCZANIE CZYNNIKA PRZED PIERWIASTEK</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Magiczna Czwórka – 2 pkt)</div>
    <div class="task-body">
      Rozbij na 4 &times; [ &nbsp; ] i wyłącz 2 przed pierwiastek:
      <div style="margin: 4px 0; display: flex; gap: 40px;">
        <span>a) &radic;20 = &radic;(4 &times; 5) = <span class="blank-line"></span></span>
        <span>b) &radic;28 = &radic;(4 &times; 7) = <span class="blank-line"></span></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Magiczna Dziewiątka i 25 – 2 pkt)</div>
    <div class="task-body">
      Wyłącz czynnik przed pierwiastek:
      <div style="margin: 4px 0; display: flex; gap: 40px;">
        <span>a) &radic;45 = &radic;(9 &times; 5) = <span class="blank-line"></span></span>
        <span>b) &radic;75 = &radic;(25 &times; 3) = <span class="blank-line"></span></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Zadanie Egzaminacyjne – 2 pkt)</div>
    <div class="task-body">
      Uprość wyrażenie: 2&radic;18 = 2 &times; (3&radic;2) = <span class="blank-line" style="min-width: 80px;"></span>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Rozkładu!</b></span>
    <span>[ ] 3–4 pkt: <b>Sprytny Rachunek!</b></span>
    <span>[ ] 1–2 pkt: <b>Trenujemy dalej!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🌿 QUIZY SUKCESU: PIERWIASTKI (CZĘŚĆ 2)</h1>
  <p>Skupienie na 5 minut • Tylko 3 zadania na karcie • Wybierz najsprytniejszą ścieżkę!</p>
</div>

<div class="quiz-card quiz-3">
  <div class="quiz-header">
    <div class="quiz-title">⚡ KARTA 3: DZIAŁANIA NA PIERWIASTKACH</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Mnożenie i Dzielenie – 2 pkt)</div>
    <div class="task-body">
      Wrzuć pod jeden pierwiastek i oblicz:
      <div style="margin: 4px 0; display: flex; gap: 40px;">
        <span>a) &radic;2 &times; &radic;8 = &radic;(2 &times; 8) = &radic;<span class="blank-line" style="min-width:30px;"></span> = <span class="blank-line"></span></span>
        <span>b) &radic;75 / &radic;3 = &radic;(75/3) = &radic;<span class="blank-line" style="min-width:30px;"></span> = <span class="blank-line"></span></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Dodawanie takich samych pierwiastków – 2 pkt)</div>
    <div class="task-body">
      Dodaj jak jabłka do koszyka:
      <div style="margin: 4px 0; display: flex; gap: 40px;">
        <span>a) 3&radic;5 + 4&radic;5 = <span class="blank-line"></span></span>
        <span>b) 7&radic;2 &minus; 2&radic;2 = <span class="blank-line"></span></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Uprość Wyrażenie – 2 pkt)</div>
    <div class="task-body">
      Oblicz: &radic;50 + &radic;18 = 5&radic;2 + 3&radic;2 = <span class="blank-line" style="min-width: 80px;"></span>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Niepokonana w Działaniach!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobra Precyzja!</b></span>
    <span>[ ] 1–2 pkt: <b>Trening!</b></span>
  </div>
</div>

<div class="quiz-card quiz-4">
  <div class="quiz-header">
    <div class="quiz-title">🚨 KARTA 4: ANTYPUŁAPKA DODAWANIA POD PIERWIASTKIEM</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Prawda czy Fałsz – 2 pkt)</div>
    <div class="task-body">
      Oceń zdanie (wpisz P lub F):
      <div style="margin: 4px 0;">
        a) &radic;(36 + 64) = 6 + 8 = 14 &nbsp; [ &nbsp; ]<br>
        b) &radic;(36 + 64) = &radic;100 = 10 &nbsp; [ &nbsp; ]
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Oblicz Poprawnie – 2 pkt)</div>
    <div class="task-body">
      Najpierw wykonaj działanie pod pierwiastkiem:
      <div style="margin: 4px 0; display: flex; gap: 40px;">
        <span>a) &radic;(100 &minus; 64) = &radic;<span class="blank-line" style="min-width:30px;"></span> = <span class="blank-line"></span></span>
        <span>b) &radic;(1 + 9/16) = &radic;(25/16) = <span class="blank-line"></span></span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Finał Egzaminacyjny CKE – 2 pkt)</div>
    <div class="task-body">
      Wartość wyrażenia <b>&radic;(25 &minus; 9)</b> wynosi:
      <div style="margin: 4px 0; display: flex; gap: 30px; font-weight: bold;">
        <span>A. 4</span> <span>B. 2</span> <span>C. 16</span> <span>D. 8</span>
      </div>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Pogromczyni Pułapek CKE!</b></span>
    <span>[ ] 3–4 pkt: <b>Czyste Konto!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🗝️ KLUCZ ODPOWIEDZI I WSKAZÓWKI COACHINGOWE (PIERWIASTKI)</h1>
  <p>Ściągawka dla Pawła: weryfikacja i budowanie poczucia sprawczości</p>
</div>

<div class="key-section">
  <div class="key-title">Karta 1: Szybkie Pierwiastki i Szacowanie</div>
  <b>1.</b> a) 8, b) 12, c) 3, d) &minus;2.<br>
  <b>2.</b> a) 5 i 6, b) 7 i 8.<br>
  <b>3.</b> &radic;17 &gt; 4 (bo &radic;17 &gt; &radic;16 = 4).
  <div class="tip-box"><b>💡 Jak chwalić:</b> <i>"Świetnie oszacowałaś &radic;30 w głowie bez kalkulatora! To dokładnie to, czego wymaga egzamin."</i></div>
</div>

<div class="key-section">
  <div class="key-title">Karta 2: Wyłączanie Czynnika przed Pierwiastek</div>
  <b>1.</b> a) 2&radic;5, b) 2&radic;7.<br>
  <b>2.</b> a) 3&radic;5, b) 5&radic;3.<br>
  <b>3.</b> 6&radic;2.
  <div class="tip-box"><b>💡 Sprytny trik:</b> Przypomnij: szukamy zawsze klocków 4, 9, 25. Nie trzeba dzielić przez 2 i 3 po sto razy!</div>
</div>

<div class="key-section">
  <div class="key-title">Karta 3: Działania na Pierwiastkach</div>
  <b>1.</b> a) &radic;16 = 4, b) &radic;25 = 5.<br>
  <b>2.</b> a) 7&radic;5, b) 5&radic;2.<br>
  <b>3.</b> 8&radic;2.
  <div class="tip-box"><b>💡 Metafora jabłek:</b> 3 koszyki &radic;5 + 4 koszyki &radic;5 to 7 koszyków &radic;5. Pod pierwiastkiem nic się nie zmienia!</div>
</div>

<div class="key-section">
  <div class="key-title">Karta 4: Antypułapka Dodawania pod Pierwiastkiem</div>
  <b>1.</b> a) F, b) P.<br>
  <b>2.</b> a) &radic;36 = 6, b) 5/4 = 1 1/4.<br>
  <b>3.</b> Odpowiedź <b>A</b> (bo &radic;16 = 4).
  <div class="tip-box"><b>💡 Rytuał:</b> Zapytaj: <i>"Czy rozrywamy parasol, gdy pada deszcz? Nie! Najpierw liczymy pod parasolem!"</i></div>
</div>
</body>
</html>
"""

with open(f"{m03}/karta-supermocy-cheat-sheet.md", "w") as f: f.write(cs_md_03.strip() + "\n")
with open(f"{m03}/karta-supermocy-cheat-sheet.html", "w") as f: f.write(cs_html_03.strip())
with open(f"{m03}/quizy-sukcesu-5-minut.md", "w") as f: f.write(quiz_md_03.strip() + "\n")
with open(f"{m03}/quizy-sukcesu-5-minut.html", "w") as f: f.write(quiz_html_03.strip())
print("Moduł 03 gotowy!")

