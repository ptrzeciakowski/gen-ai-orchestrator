import os, subprocess

base = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-12-matematyka-dla-nadii"

# ==========================================
# MODUŁ 04: PROCENTY
# ==========================================
m04 = os.path.join(base, "04-procenty")
cs_md_04 = """# KARTA SUPERMOCY: PROCENTY (Klasa 7 & 8)
## Sprytne Metody Nadii – Klocki Procentowe, Obniżki i Punkty Procentowe

---

### 🚀 1. KLUB PROCENTOWYCH UŁAMKÓW (Szybkie Przeliczniki)

| Procent | Ułamek | Co to oznacza w praktyce? | Przykład w pamięci |
| :---: | :---: | :--- | :--- |
| **$50\\%$** | $\\mathbf{\\frac{1}{2}}$ | **Połowa** (podziel przez 2) | $50\\%$ z $80\\text{ zł} = \\mathbf{40\\text{ zł}}$ |
| **$25\\%$** | $\\mathbf{\\frac{1}{4}}$ | **Ćwiartka** (podziel na 4) | $25\\%$ z $60\\text{ zł} = \\mathbf{15\\text{ zł}}$ |
| **$75\\%$** | $\\mathbf{\\frac{3}{4}}$ | **Trzy ćwiartki** ($50\\% + 25\\%$) | $75\\%$ z $40\\text{ zł} = 20 + 10 = \\mathbf{30\\text{ zł}}$ |
| **$10\\%$** | $\\mathbf{\\frac{1}{10}}$ | **Utnij zero** (przesuń przecinek o 1 w lewo) | $10\\%$ z $230\\text{ zł} = \\mathbf{23\\text{ zł}}$ |
| **$5\\%$** | $\\mathbf{\\frac{1}{20}}$ | **Połowa z $10\\%$** | $10\\% = 20 \\implies 5\\% = \\mathbf{10}$ |
| **$1\\%$** | $\\mathbf{\\frac{1}{100}}$ | **Przesuń przecinek o 2 w lewo** | $1\\%$ z $450\\text{ zł} = \\mathbf{4{,}50\\text{ zł}}$ |
| **$20\\%$** | $\\mathbf{\\frac{1}{5}}$ | **Dwa razy $10\\%$** (lub podziel przez 5) | $20\\%$ z $70\\text{ zł} = 2 \\times 7 = \\mathbf{14\\text{ zł}}$ |

---

### 🧩 2. METODA KLOCKÓW PROCENTOWYCH (Liczenie w 5 sekund)

Nie mnóż przez ułamki pod kreską! Zbuduj procent z klocków **$10\\%$, $5\\%$, $1\\%$**:
- **Ile to $15\\%$ z $80$?**
  - Klocek $10\\% = 8$
  - Klocek $5\\% = 4$ (połowa z 8)
  - Razem: $8 + 4 = \\mathbf{12}$!
- **Ile to $35\\%$ z $200$?**
  - Klocek $10\\% = 20 \\rightarrow 3 \\times 20 = 60$
  - Klocek $5\\% = 10$
  - Razem: $60 + 10 = \\mathbf{70}$!

---

### 🛍️ 3. OBNIŻKI I PODWYŻKI (Mnożnik jednokrokowy)

- **Obniżka o $20\\%$:** Zostaje $80\\%$ ceny $\\rightarrow$ nowa cena = $\\mathbf{0{,}8 \\cdot stara\\_cena}$.
- **Podwyżka o $15\\%$:** Nowa cena to $115\\%$ $\\rightarrow$ nowa cena = $\\mathbf{1{,}15 \\cdot stara\\_cena}$.
- 🚨 **PUŁAPKA CKE:** "Cena spadła o $10\\%$, a potem wzrosła o $10\\%$. Czy wróciła do normy?"
  - **NIE!** Start: $100\\text{ zł} \\xrightarrow{-10\\%} 90\\text{ zł} \\xrightarrow{+10\\%} 90 + 9 = \\mathbf{99\\text{ zł}}$! (Straciliśmy 1 zł!).

---

### ⚖️ 4. PUNKTY PROCENTOWE (pp) VS PROCENTY

- Poparcie partii wzrosło z $20\\%$ do $25\\%$:
  - Wzrosło o **$5$ punktów procentowych (pp)** (zwykłe odejmowanie: $25 - 20 = 5$).
  - Wzrosło o **$25\\%$** (bo $\\frac{5}{20} = \\frac{1}{4} = 25\\%$).
"""

cs_html_04 = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Procenty</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.32; }
  .header { text-align: center; border-bottom: 3px solid #f59e0b; padding-bottom: 4px; margin-bottom: 8px; }
  .header h1 { margin: 0; font-size: 17pt; color: #d97706; text-transform: uppercase; }
  .header .sub { font-size: 10pt; font-weight: 600; color: #475569; }
  .card { border-radius: 8px; padding: 7px 10px; border: 1.5px solid #cbd5e1; background: #fff; margin-bottom: 7px; }
  .card-amber { border-color: #f59e0b; background: #fffbeb; }
  .card-emerald { border-color: #10b981; background: #ecfdf5; }
  .card-rose { border-color: #f43f5e; background: #fff1f2; }
  .card-blue { border-color: #3b82f6; background: #eff6ff; }
  .card-title { font-size: 11pt; font-weight: bold; margin-bottom: 4px; display: flex; align-items: center; gap: 5px; }
  .card-amber .card-title { color: #b45309; }
  .card-emerald .card-title { color: #047857; }
  .card-rose .card-title { color: #be123c; }
  .card-blue .card-title { color: #1d4ed8; }
  table.pct-table { width: 100%; border-collapse: collapse; font-size: 9pt; background: #fff; border-radius: 6px; overflow: hidden; }
  table.pct-table th, table.pct-table td { padding: 3px 6px; border: 1px solid #fde68a; text-align: center; }
  table.pct-table th { background: #fef3c7; color: #92400e; font-weight: bold; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .footer-tip { text-align: center; font-size: 8.8pt; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 4px; font-weight: 500; }
</style>
</head>
<body>
<div class="header">
  <h1>🏷️ KARTA SUPERMOCY: PROCENTY (KLASA 7 & 8)</h1>
  <div class="sub">Ściągawka Nadii na biurko – Klocki procentowe, obniżki w sklepie i punkty procentowe!</div>
</div>

<div class="card card-amber">
  <div class="card-title">🚀 1. KLUB PROCENTOWYCH UŁAMKÓW (SZYBKIE PRZELICZNIKI)</div>
  <table class="pct-table">
    <thead>
      <tr><th>Procent</th><th>Ułamek</th><th>Co to oznacza w praktyce?</th><th>Przykład w pamięci</th></tr>
    </thead>
    <tbody>
      <tr><td><b>50%</b></td><td><b>1/2</b></td><td><b>Połowa</b> (podziel przez 2)</td><td>50% z 80 zł = <b>40 zł</b></td></tr>
      <tr><td><b>25%</b></td><td><b>1/4</b></td><td><b>Ćwiartka</b> (podziel na 4)</td><td>25% z 60 zł = <b>15 zł</b></td></tr>
      <tr><td><b>75%</b></td><td><b>3/4</b></td><td><b>Trzy ćwiartki</b> (50% + 25%)</td><td>75% z 40 zł = 20 + 10 = <b>30 zł</b></td></tr>
      <tr><td><b>10%</b></td><td><b>1/10</b></td><td><b>Utnij zero</b> (przesuń przecinek o 1 w lewo)</td><td>10% z 230 zł = <b>23 zł</b></td></tr>
      <tr><td><b>5%</b></td><td><b>1/20</b></td><td><b>Połowa z 10%</b></td><td>10% = 20 &rarr; 5% = <b>10</b></td></tr>
      <tr><td><b>1%</b></td><td><b>1/100</b></td><td><b>Przesuń przecinek o 2 w lewo</b></td><td>1% z 450 zł = <b>4,50 zł</b></td></tr>
      <tr><td><b>20%</b></td><td><b>1/5</b></td><td><b>Dwa razy 10%</b> (lub podziel przez 5)</td><td>20% z 70 zł = 2 &times; 7 = <b>14 zł</b></td></tr>
    </tbody>
  </table>
</div>

<div class="grid-2">
  <div class="card card-emerald">
    <div class="card-title">🧩 2. METODA KLOCKÓW PROCENTOWYCH</div>
    <div style="font-size: 8.8pt;">Zbuduj procent z klocków <b>10%, 5%, 1%</b>:</div>
    <div style="font-size: 8.8pt; background: #fff; padding: 4px 6px; border-radius: 4px; margin-top: 3px; border: 1px solid #a7f3d0;">
      <b>Ile to 15% ze 80 zł?</b><br>
      &bull; 10% = 8 zł<br>
      &bull; 5% = 4 zł (połowa z 8)<br>
      &bull; <b>Razem:</b> 8 + 4 = <b>12 zł</b>!<br><br>
      <b>Ile to 35% z 200 zł?</b><br>
      &bull; 3 &times; 10% = 3 &times; 20 = 60 zł<br>
      &bull; 5% = 10 zł &rarr; <b>Razem: 70 zł</b>!
    </div>
  </div>

  <div class="card card-rose">
    <div class="card-title">🛍️ 3. OBNIŻKI I PODWYŻKI W SKLEPIE</div>
    <div style="font-size: 8.8pt;">Mnożnik jednokrokowy:</div>
    <div style="font-size: 8.8pt; background: #fff; padding: 4px 6px; border-radius: 4px; margin-top: 3px; border: 1px solid #fecdd3;">
      &bull; Obniżka o 20% &rarr; płacisz 80%: <b>0,8 &times; cena</b><br>
      &bull; Podwyżka o 15% &rarr; płacisz 115%: <b>1,15 &times; cena</b><br><br>
      🚨 <b>PUŁAPKA CKE:</b> Spadek o 10% i wzrost o 10%:<br>
      100 zł &rarr; &minus;10% = 90 zł &rarr; +10% (z 90 zł!) = 90 + 9 = <b>99 zł</b>! (Nie wraca do 100 zł!).
    </div>
  </div>
</div>

<div class="card card-blue">
  <div class="card-title">⚖️ 4. PUNKTY PROCENTOWE (pp) VS PROCENTY</div>
  <div style="font-size: 8.8pt;">
    Gdy poparcie wzrosło z <b>20%</b> do <b>25%</b>:<br>
    &bull; Wzrosło o <b>5 punktów procentowych (pp)</b> (zwykłe odejmowanie: 25 &minus; 20 = 5 pp).<br>
    &bull; Wzrosło o <b>25%</b> wartości początkowej (bo 5 / 20 = 1/4 = 25%).
  </div>
</div>

<div class="footer-tip">
  💡 Pamiętaj Nadiu: Procent to po prostu ułamek ze stówką w mianowniku. 10% to Twój najlepszy przyjaciel! 🏆
</div>
</body>
</html>
"""

quiz_md_04 = """# QUIZY SUKCESU: PROCENTY (Klasa 7 & 8)
## 4 Karty Mikro-Treningu (Po 5 minut każda)

---

## 🌟 KARTA 1: BŁYSKAWICZNE KLOCKI PROCENTOWE
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Klocki 10% i 1% – 2 pkt)
Oblicz w pamięci (utnij zero lub przesuń przecinek):
- a) $10\\%$ z $160\\text{ zł} = \\dots\\dots\\dots$ \t b) $10\\%$ z $45\\text{ zł} = \\dots\\dots\\dots$
- c) $1\\%$ z $300\\text{ zł} = \\dots\\dots\\dots$ \t d) $1\\%$ z $85\\text{ zł} = \\dots\\dots\\dots$

### Zadanie 2 (Składanie Klocków – 2 pkt)
Użyj metody $10\\% + 5\\%$:
- a) $15\\%$ z $40 = \\dots\\dots\\dots$ ($10\\% = 4$, a $5\\% = \\dots\\dots$)
- b) $20\\%$ z $80 = \\dots\\dots\\dots$ ($2 \\times 10\\% = \\dots\\dots$)

### Zadanie 3 (Mistrzyni Okazji – 2 pkt)
Ile wynosi $50\\%$ z połowy liczby $200$?
- Odpowiedź: $\\dots\\dots\\dots$

---

## 🌟 KARTA 2: UŁAMKI I PROCENTY W KOSZYKU
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Połącz w Pary – 2 pkt)
Połącz procent z ułamkiem:
- $25\\%$ \t $\\longrightarrow$ \t $\\frac{1}{5}$
- $20\\%$ \t $\\longrightarrow$ \t $\\frac{1}{4}$
- $75\\%$ \t $\\longrightarrow$ \t $\\frac{3}{4}$

### Zadanie 2 (Jaki to Procent? – 2 pkt)
W klasie jest 25 uczniów, w tym 5 ma zielone oczy. Jaki to procent klasy?
- Obliczenie: $\\frac{5}{25} = \\frac{[\\quad]}{100} = \\dots\\dots\\%$

### Zadanie 3 (Czekolada – 2 pkt)
Z tabliczki czekolady mającej 20 kostek zjedzono 6 kostek. Jaki procent czekolady pozostał?
- Obliczenie: $\\dots\\dots\\dots$

---

## 🌟 KARTA 3: OBNIŻKI I PROMOCJE W SKLEPIE
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Czarne Piątki – 2 pkt)
Bluza kosztowała $120\\text{ zł}$. Jej cenę obniżono o $25\\%$.
- a) O ile złotych obniżono cenę? $\\dots\\dots\\dots\\text{ zł}$
- b) Ile kosztuje bluza po obniżce? $\\dots\\dots\\dots\\text{ zł}$

### Zadanie 2 (Szybka Podwyżka – 2 pkt)
Bilet kosztował $40\\text{ zł}$. Podrożał o $10\\%$.
- Nowa cena biletu wynosi: $\\dots\\dots\\dots\\text{ zł}$

### Zadanie 3 (Zadanie Egzaminacyjne CKE – 2 pkt)
Spodnie kosztowały $200\\text{ zł}$. Najpierw obniżono ich cenę o $10\\%$, a potem nową cenę podniesiono o $10\\%$. Ile kosztują teraz?
- **A.** $200\\text{ zł}$ \t **B.** $198\\text{ zł}$ \t **C.** $190\\text{ zł}$ \t **D.** $202\\text{ zł}$

---

## 🌟 KARTA 4: PUNKTY PROCENTOWE I SZACOWANIE
**Czas:** 5 minut | **Punkty:** ...... / 6 pkt

### Zadanie 1 (Punkty Procentowe – 2 pkt)
Poparcie dla drużyny wzrosło z $15\\%$ do $22\\%$.
- Wzrost wyniósł $\\dots\\dots\\dots$ punktów procentowych (pp).

### Zadanie 2 (Prawda czy Fałsz – 2 pkt)
Oceń zdanie:
- a) $30\\%$ z liczby $50$ to tyle samo co $50\\%$ z liczby $30$.  **[ P / F ]**
- b) $100\\%$ z liczby $7$ to $700$.  **[ P / F ]**

### Zadanie 3 (Finał – 2 pkt)
W pewnej szkole $40\\%$ uczniów trenuje siatkówkę, a $30\\%$ koszykówkę. O ile punktów procentowych więcej uczniów trenuje siatkówkę?
- Odpowiedź: $\\dots\\dots\\dots$ pp.

---

## 🗝️ KLUCZ ODPOWIEDZI (Dla Pawła)
- **Karta 1:** 1. a) 16, b) 4,5, c) 3, d) 0,85. 2. a) 6 ($4+2$), b) 16. 3. 50 (połowa to 100, a $50\\%$ ze 100 to 50).
- **Karta 2:** 1. $25\\% \\rightarrow 1/4$, $20\\% \\rightarrow 1/5$, $75\\% \\rightarrow 3/4$. 2. $\\frac{5}{25} = \\frac{20}{100} = 20\\%$. 3. Zostało 14 kostek $\\rightarrow \\frac{14}{20} = \\frac{70}{100} = 70\\%$.
- **Karta 3:** 1. a) $30\\text{ zł}$ (ćwiartka ze 120), b) $90\\text{ zł}$. 2. $44\\text{ zł}$ ($40+4$). 3. Odp. B ($198\\text{ zł}$, bo $200 \\rightarrow 180 \\rightarrow 180 + 18 = 198$).
- **Karta 4:** 1. $7\\text{ pp}$ ($22-15$). 2. a) P (obie wynoszą 15!), b) F (wynosi 7). 3. $10\\text{ pp}$.
"""

quiz_html_04 = f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Procenty</title>
<style>
  @page {{ size: A4 portrait; margin: 10mm 12mm; }}
  * {{ box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.5pt; line-height: 1.35; }}
  .page-break {{ page-break-after: always; }}
  .header-main {{ text-align: center; border-bottom: 2.5px solid #f59e0b; padding-bottom: 5px; margin-bottom: 12px; }}
  .header-main h1 {{ margin: 0; font-size: 16pt; color: #d97706; }}
  .header-main p {{ margin: 2px 0 0 0; font-size: 9.5pt; color: #64748b; }}
  .quiz-card {{ border: 2px solid #cbd5e1; border-radius: 10px; padding: 12px 14px; margin-bottom: 14px; background: #fff; }}
  .quiz-1 {{ border-color: #f59e0b; background: #f8fafc; }}
  .quiz-2 {{ border-color: #10b981; background: #f8fafc; }}
  .quiz-3 {{ border-color: #3b82f6; background: #f8fafc; }}
  .quiz-4 {{ border-color: #8b5cf6; background: #f8fafc; }}
  .quiz-header {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px dashed #cbd5e1; padding-bottom: 6px; margin-bottom: 8px; }}
  .quiz-title {{ font-size: 12pt; font-weight: bold; }}
  .quiz-1 .quiz-title {{ color: #b45309; }}
  .quiz-2 .quiz-title {{ color: #047857; }}
  .quiz-3 .quiz-title {{ color: #1d4ed8; }}
  .quiz-4 .quiz-title {{ color: #6d28d9; }}
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
  <h1>🏷️ QUIZY SUKCESU: PROCENTY (KLASA 7 & 8)</h1>
  <p>5-minutowe wyzwania pewności siebie • 1 karta naraz • Po każdej karcie 3 minuty przerwy!</p>
</div>

<div class="quiz-card quiz-1">
  <div class="quiz-header">
    <div class="quiz-title">🎯 KARTA 1: BŁYSKAWICZNE KLOCKI PROCENTOWE</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Klocki 10% i 1% – 2 pkt)</div>
    <div class="task-body">
      Oblicz w pamięci (utnij zero lub przesuń przecinek):
      <div style="margin: 4px 0; display: flex; gap: 30px;">
        <span>a) 10% ze 160 zł = <span class="blank-line"></span> zł</span>
        <span>b) 10% z 45 zł = <span class="blank-line"></span> zł</span>
      </div>
      <div style="margin: 4px 0; display: flex; gap: 30px;">
        <span>c) 1% z 300 zł = <span class="blank-line"></span> zł</span>
        <span>d) 1% z 85 zł = <span class="blank-line"></span> zł</span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Składanie Klocków – 2 pkt)</div>
    <div class="task-body">
      Użyj metody 10% + 5%:<br>
      a) 15% z 40 = <span class="blank-line"></span> (10% = 4, a 5% to połowa z 4 = 2)<br>
      b) 20% z 80 = <span class="blank-line"></span> (dwa klocki po 10% = 2 &times; 8)
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Mistrzyni Okazji – 2 pkt)</div>
    <div class="task-body">
      Ile wynosi 50% z połowy liczby 200?<br>
      Odpowiedź: <span class="blank-line" style="min-width: 80px;"></span> (połowa z 200 to 100, a połowa ze 100 to...)
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Czarodziejka Promocji!</b></span>
    <span>[ ] 3–4 pkt: <b>Bystry Kalkulator!</b></span>
    <span>[ ] 1–2 pkt: <b>Świetny start!</b></span>
  </div>
</div>

<div class="quiz-card quiz-2">
  <div class="quiz-header">
    <div class="quiz-title">🍕 KARTA 2: UŁAMKI I PROCENTY W KOSZYKU</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Połącz w Pary – 2 pkt)</div>
    <div class="task-body">
      Połącz procent z odpowiadającym ułamkiem:<br>
      <div style="display: flex; justify-content: space-around; font-weight: bold; margin: 4px 0;">
        <span>25% &rarr; 1/4</span>
        <span>20% &rarr; 1/5</span>
        <span>75% &rarr; 3/4</span>
      </div>
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Jaki to Procent? – 2 pkt)</div>
    <div class="task-body">
      W klasie jest 25 uczniów, w tym 5 ma zielone oczy. Jaki to procent klasy?<br>
      Obliczenie: 5 / 25 = [ &nbsp; ] / 100 = <span class="blank-line"></span>%
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Czekolada – 2 pkt)</div>
    <div class="task-body">
      Z tabliczki mającej 20 kostek zjedzono 6 kostek. Jaki procent czekolady <b>pozostał</b>?<br>
      Zostało 14 kostek &rarr; 14 / 20 = <span class="blank-line"></span>%
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Ekspertka Ułamków!</b></span>
    <span>[ ] 3–4 pkt: <b>Pewna Ręka!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🏷️ QUIZY SUKCESU: PROCENTY (CZĘŚĆ 2)</h1>
  <p>Skupienie na 5 minut • Tylko 3 zadania na karcie • Spryt zamiast liczenia!</p>
</div>

<div class="quiz-card quiz-3">
  <div class="quiz-header">
    <div class="quiz-title">🛍️ KARTA 3: OBNIŻKI I PROMOCJE W SKLEPIE</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Czarne Piątki – 2 pkt)</div>
    <div class="task-body">
      Bluza kosztowała 120 zł. Obniżono jej cenę o 25% (ćwiartkę):<br>
      a) O ile złotych obniżono cenę? <span class="blank-line"></span> zł (120 &divide; 4 = ...)<br>
      b) Nowa cena bluzy wynosi: <span class="blank-line"></span> zł
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Szybka Podwyżka – 2 pkt)</div>
    <div class="task-body">
      Bilet kosztował 40 zł. Podrożał o 10% (o 4 zł).<br>
      Nowa cena biletu to: <span class="blank-line"></span> zł
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Zadanie Egzaminacyjne CKE – 2 pkt)</div>
    <div class="task-body">
      Spodnie kosztowały 200 zł. Najpierw staniały o 10%, a potem nową cenę podniesiono o 10%. Ile kosztują teraz?<br>
      <b>A. 200 zł</b> &nbsp; <b>B. 198 zł</b> &nbsp; <b>C. 190 zł</b> &nbsp; <b>D. 202 zł</b>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Pogromczyni Cen w Sklepie!</b></span>
    <span>[ ] 3–4 pkt: <b>Świetny Wynik!</b></span>
    <span>[ ] 1–2 pkt: <b>Dobra próba!</b></span>
  </div>
</div>

<div class="quiz-card quiz-4">
  <div class="quiz-header">
    <div class="quiz-title">⚖️ KARTA 4: PUNKTY PROCENTOWE I SZACOWANIE</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Punkty Procentowe – 2 pkt)</div>
    <div class="task-body">
      Poparcie dla drużyny wzrosło z 15% do 22%.<br>
      Wzrost wyniósł <span class="blank-line"></span> punktów procentowych (pp).
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Prawda czy Fałsz – 2 pkt)</div>
    <div class="task-body">
      Oceń zdanie (wpisz P lub F):<br>
      a) 30% z 50 to dokładnie tyle samo co 50% z 30 &nbsp; [ &nbsp; ]<br>
      b) 100% z liczby 7 to 700 &nbsp; [ &nbsp; ]
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Finał Egzaminacyjny – 2 pkt)</div>
    <div class="task-body">
      W szkole 40% uczniów gra w siatkówkę, a 30% w koszykówkę.<br>
      O ile punktów procentowych więcej osób gra w siatkówkę? Odpowiedź: <span class="blank-line"></span> pp.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Statystyki!</b></span>
    <span>[ ] 3–4 pkt: <b>Pewny Krok!</b></span>
    <span>[ ] 1–2 pkt: <b>Do przodu!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🗝️ KLUCZ ODPOWIEDZI I WSKAZÓWKI COACHINGOWE (PROCENTY)</h1>
  <p>Ściągawka dla Pawła: jak chwalić i utrwalać sprytne nawyki</p>
</div>

<div class="key-section">
  <div class="key-title">Karta 1: Błyskawiczne Klocki Procentowe</div>
  <b>1.</b> a) 16 zł, b) 4,50 zł, c) 3 zł, d) 0,85 zł.<br>
  <b>2.</b> a) 6 (4 + 2), b) 16 (2 &times; 8).<br>
  <b>3.</b> 50 (połowa z 200 to 100, 50% ze 100 to 50).
  <div class="tip-box"><b>💡 Jak chwalić:</b> Zwróć uwagę na lekkość klocków 10% i 5%: <i>"Zero dzielenia pod kreską, złożyłaś to jak klocki Lego!"</i></div>
</div>

<div class="key-section">
  <div class="key-title">Karta 2: Ułamki i Procenty w Koszyku</div>
  <b>1.</b> 25% = 1/4, 20% = 1/5, 75% = 3/4.<br>
  <b>2.</b> 20% (bo 5/25 = 20/100).<br>
  <b>3.</b> 70% (zostało 14 z 20, 14/20 = 70/100).
  <div class="tip-box"><b>💡 Uwaga coachingowa:</b> Zwróć uwagę na słowo <i>"pozostało"</i> w zadaniu 3 – to częsta pułapka na czytanie ze zrozumieniem!</div>
</div>

<div class="key-section">
  <div class="key-title">Karta 3: Obniżki i Promocje w Sklepie</div>
  <b>1.</b> a) 30 zł, b) 90 zł.<br>
  <b>2.</b> 44 zł.<br>
  <b>3.</b> Odpowiedź <b>B</b> (198 zł).
  <div class="tip-box"><b>💡 Sukces przy podwójnej obniżce (198 zł):</b> Zapytaj Nadię, dlaczego nie wróciło do 200 zł. Gdy powie, że 10% liczyliśmy z 180 zł, pogratuluj logicznego myślenia!</div>
</div>

<div class="key-section">
  <div class="key-title">Karta 4: Punkty Procentowe i Szacowanie</div>
  <b>1.</b> 7 pp.<br>
  <b>2.</b> a) P (30% z 50 = 15 oraz 50% z 30 = 15!), b) F (100% z 7 to po prostu 7).<br>
  <b>3.</b> 10 pp.
  <div class="tip-box"><b>💡 Magiczna symetria procentów:</b> Pokaż Nadii ciekawostkę: <i>"X% z Y to zawsze to samo co Y% z X"</i>. Np. 16% z 50 to 50% z 16 = 8! Wszyscy dorośli są tym zachwyceni!</div>
</div>
</body>
</html>
"""

with open(f"{m04}/karta-supermocy-cheat-sheet.md", "w") as f: f.write(cs_md_04.strip() + "\n")
with open(f"{m04}/karta-supermocy-cheat-sheet.html", "w") as f: f.write(cs_html_04.strip())
with open(f"{m04}/quizy-sukcesu-5-minut.md", "w") as f: f.write(quiz_md_04.strip() + "\n")
with open(f"{m04}/quizy-sukcesu-5-minut.html", "w") as f: f.write(quiz_html_04.strip())
print("Moduł 04 gotowy!")

