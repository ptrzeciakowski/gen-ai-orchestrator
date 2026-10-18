#!/usr/bin/env python3
import os
import subprocess

BASE = "/Users/pawel/git/gen-ai-orchestrator/openspec/changes/matma-egzamin-8-klasisty"
PDF_SCRIPT = "/Users/pawel/git/gen-ai-orchestrator/.ai/skills/matematyka-supermoce/scripts/generate_pdf.py"

def write_and_render(folder, base_name, md_text, html_text):
    d = os.path.join(BASE, folder)
    os.makedirs(d, exist_ok=True)
    md_path = os.path.join(d, f"{base_name}.md")
    html_path = os.path.join(d, f"{base_name}.html")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_text)
    subprocess.run(["python3", PDF_SCRIPT, html_path], check=True)

# ==============================================================================
# MODUŁ 10: GEOMETRIA PRZESTRZENNA (GRANIASTOSŁUPY I OSTROSŁUPY)
# ==============================================================================
cs_md_10 = r"""# KARTA SUPERMOCY: GEOMETRIA PRZESTRZENNA – BRYŁY (Klasa 7 & 8)
## Sprytne Metody Nadii – Graniastosłupy, Ostrosłupy, Pitagoras w Bryle i Litry

---

### 📦 1. ZŁOTA TABELA KRAWĘDZI, WIERZCHOŁKÓW I ŚCIAN ($n$-kąt w podstawie)

| Bryła ($n$-kąt w podstawie) | Wierzchołki ($W$) | Krawędzie ($K$) | Wszystkie Ściany ($S$) | Przykład: Czworokątny ($n=4$) |
| :--- | :---: | :---: | :---: | :---: |
| **Graniastosłup** (2 podstawy: dół i góra) | **$2n$** | **$3n$** | **$n + 2$** | $W=8, \; K=12, \; S=6$ |
| **Ostrosłup** (1 podstawa + dziubek na górze) | **$n + 1$** | **$2n$** | **$n + 1$** | $W=5, \; K=8, \; S=5$ |

> 💡 **Szybki dekoder CKE:** „Graniastosłup ma 15 krawędzi” $\implies 3n = 15 \implies n = 5$ (pięciokąt w podstawie!). „Ostrosłup ma 12 krawędzi” $\implies 2n = 12 \implies n = 6$ (sześciokąt w podstawie!).

---

### 🥤 2. OBJĘTOŚĆ I POLE POWIERZCHNI ("Zasada Trzech Kubków")

- **Graniastosłup prosty:**
  $$V = P_p \cdot H \qquad \text{oraz} \qquad P_c = 2 \cdot P_p + P_b$$
- **Ostrosłup (dokładnie 3 razy mniejsza objętość niż graniastosłup o tej samej podstawie i wysokości!):**
  $$V = \frac{1}{3} \cdot P_p \cdot H \qquad \text{oraz} \qquad P_c = P_p + P_b$$
- **Prostopadłościan ($a \times b \times c$) i Sześcian ($a \times a \times a$):**
  $$V_{\text{prost}} = a \cdot b \cdot c, \qquad V_{\text{sześc}} = a^3, \qquad P_{c\text{ sześc}} = 6a^2, \qquad \text{Suma krawędzi sześcianu} = 12a$$

---

### 📐 3. PITAGORAS WEWNĄTRZ BRYŁY ("Wyjmij Płaski Trójkąt Prostokątny!")

W zadaniach z klasy 7–8 (jak w przykładach CKE ze str. 192–193) prawie zawsze szukasz ukrytego trójkąta prostokątnego (szukaj trójek **3-4-5**, **5-12-13**, **6-8-10**!):
1. **Ściana boczna ostrosłupa:** Krawędź boczna ($13\text{ cm}$) i połowa boku podstawy ($10 : 2 = 5\text{ cm}$) tworzą z wysokością ściany bocznej $h_b$ trójkąt prostokątny **5-12-13** $\implies h_b = 12\text{ cm}$!
2. **Wysokość całego ostrosłupa ($H$):** Wysokość ściany bocznej ($h_b = 13\text{ cm}$) i połowa drugiego boku podstawy ($10\text{ cm}$) tworzą z wysokością bryły $H$ trójkąt prostokątny!
3. **Podstawa z kątem $45^\circ$ (trójkąt prostokątny równoramienny):** Jeśli przeciwprostokątna ma $6\sqrt{2}\text{ dm}$, to obie przyprostokątne mają po **$6\text{ dm}$**, a pole podstawy to $P_p = \frac{6 \cdot 6}{2} = 18\text{ dm}^2$!

---

### 💧 4. KOTWICA POJEMNOŚCI I LITRÓW (Antypułapka Jednostek!)

- **$1\text{ litr (l)} = 1\text{ dm}^3 = 1000\text{ cm}^3$** *(karton mleka to sześcian $10\text{ cm} \times 10\text{ cm} \times 10\text{ cm}$!)*
- **$1\text{ mililitr (ml)} = 1\text{ cm}^3$**
- 🚨 **Złota reguła akwarium:** Gdy wymiary akwarium są w $\text{cm}$ (np. $40\text{ cm} \times 20\text{ cm} \times 30\text{ cm}$), **najpierw zamień je na $\text{dm}$** ($4\text{ dm} \times 2\text{ dm} \times 3\text{ dm} = \mathbf{24\text{ dm}^3 = 24\text{ litry}}$) – unikniesz gubienia tysięcy zer!
"""

cs_html_10 = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Geometria Przestrzenna</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 9.8pt; line-height: 1.3; }
  .header { text-align: center; border-bottom: 3px solid #0284c7; padding-bottom: 4px; margin-bottom: 7px; }
  .header h1 { margin: 0; font-size: 16pt; color: #0369a1; text-transform: uppercase; }
  .header .sub { font-size: 9.5pt; font-weight: 600; color: #475569; }
  .card { border-radius: 8px; padding: 6px 10px; border: 1.5px solid #cbd5e1; background: #fff; margin-bottom: 6px; }
  .card-blue { border-color: #0284c7; background: #f0f9ff; }
  .card-teal { border-color: #0d9488; background: #f0fdfa; }
  .card-amber { border-color: #f59e0b; background: #fffbeb; }
  .card-rose { border-color: #f43f5e; background: #fff1f2; }
  .card-title { font-size: 10.6pt; font-weight: bold; margin-bottom: 4px; }
  .card-blue .card-title { color: #0369a1; }
  .card-teal .card-title { color: #0f766e; }
  .card-amber .card-title { color: #b45309; }
  .card-rose .card-title { color: #be123c; }
  table.p-table { width: 100%; border-collapse: collapse; font-size: 8.8pt; background: #fff; }
  table.p-table th, table.p-table td { padding: 3px 6px; border: 1px solid #bae6fd; text-align: center; }
  table.p-table th { background: #e0f2fe; color: #0c4a6e; font-weight: bold; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .box-white { background: #fff; border: 1px solid #cbd5e1; border-radius: 5px; padding: 5px 8px; margin-top: 3px; font-size: 9pt; }
  .footer-tip { text-align: center; font-size: 8.6pt; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 4px; font-weight: 600; }
</style>
</head>
<body>
<div class="header">
  <h1>📦 KARTA SUPERMOCY: GEOMETRIA PRZESTRZENNA (KLASA 7 &amp; 8)</h1>
  <div class="sub">Graniastosłupy, Ostrosłupy, Trójki Pitagorejskie w Bryłach i Kotwica Litrów</div>
</div>

<div class="card card-blue">
  <div class="card-title">🔢 1. ZŁOTA TABELA KRAWĘDZI, WIERZCHOŁKÓW I ŚCIAN (dla n-kąta w podstawie)</div>
  <table class="p-table">
    <thead>
      <tr><th>Bryła (n-kąt w podstawie)</th><th>Wierzchołki (W)</th><th>Krawędzie (K)</th><th>Wszystkie Ściany (S)</th><th>Przykład: Czworokątny (n=4)</th></tr>
    </thead>
    <tbody>
      <tr><td><b>Graniastosłup</b> (dwie podstawy)</td><td><b>2n</b></td><td><b>3n</b></td><td><b>n + 2</b></td><td>W = 8, &nbsp;K = 12, &nbsp;S = 6</td></tr>
      <tr><td><b>Ostrosłup</b> (jedna podstawa + czubek)</td><td><b>n + 1</b></td><td><b>2n</b></td><td><b>n + 1</b></td><td>W = 5, &nbsp;K = 8, &nbsp;S = 5</td></tr>
    </tbody>
  </table>
  <div class="box-white">
    💡 <b>Błyskawiczny dekoder CKE:</b> Graniastosłup ma <b>18 krawędzi</b> &rarr; 3n = 18 &rarr; <b>n = 6</b> (sześciokątny!). Ostrosłup ma <b>10 krawędzi</b> &rarr; 2n = 10 &rarr; <b>n = 5</b> (pięciokątny!).<br>
    💡 <b>Sześcian o krawędzi a:</b> Suma wszystkich 12 krawędzi = <b>12a</b> &nbsp;|&nbsp; Pole całkowite P<sub>c</sub> = <b>6a²</b> &nbsp;|&nbsp; Objętość V = <b>a³</b>.
  </div>
</div>

<div class="grid-2">
  <div class="card card-teal">
    <div class="card-title">🥤 2. OBJĘTOŚĆ I POLE ("ZASADA 3 KUBKÓW")</div>
    <div class="box-white">
      <b>Graniastosłup prosty:</b><br>
      &bull; Objętość: <b>V = P<sub>p</sub> &middot; H</b><br>
      &bull; Pole całkowite: <b>P<sub>c</sub> = 2 &middot; P<sub>p</sub> + P<sub>b</sub></b>
    </div>
    <div class="box-white" style="margin-top:4px;">
      <b>Ostrosłup (3 razy mniejsza objętość!):</b><br>
      &bull; Objętość: <b>V = &frac13; &middot; P<sub>p</sub> &middot; H</b><br>
      &bull; Pole całkowite: <b>P<sub>c</sub> = P<sub>p</sub> + P<sub>b</sub></b><br>
      <i>(Trzy ostrosłupy wody wypełniają dokładnie jeden graniastosłup o tej samej podstawie i wysokości!)</i>
    </div>
  </div>

  <div class="card card-rose">
    <div class="card-title">💧 3. KOTWICA LITRÓW I POJEMNOŚCI (CKE!)</div>
    <div class="box-white">
      &bull; <b>1 litr (l) = 1 dm³ = 1000 cm³</b><br>
      &bull; <b>1 mililitr (ml) = 1 cm³</b> &nbsp;|&nbsp; <b>1 m³ = 1000 l</b>
    </div>
    <div class="box-white" style="margin-top:4px; border-color:#fecdd3; background:#fff1f2;">
      🚨 <b>Sprytny Trik Akwarium:</b><br>
      Masz wymiary w <b>cm</b> (np. 50 cm &times; 20 cm &times; 30 cm) i pytają o <b>litry</b>?<br>
      <b>Zamień cm na dm PRZED mnożeniem!</b><br>
      5 dm &times; 2 dm &times; 3 dm = <b>30 dm³ = 30 litrów!</b> (Zero stresu z tysiącami zer!).
    </div>
  </div>
</div>

<div class="card card-amber">
  <div class="card-title">📐 4. PITAGORAS WEWNĄTRZ BRYŁY ("WYJMIJ PŁASKI TRÓJKĄT PROSTOKĄTNY!")</div>
  <div class="grid-2">
    <div class="box-white">
      <b>Wzorzec CKE #1 (Ostrosłup – str. 193 podstawy):</b><br>
      Krawędź podstawy ma 10 cm (połowa = <b>5 cm</b>), a krawędź boczna ma <b>13 cm</b>.<br>
      👉 Wyjmujesz trójkąt prostokątny ze ściany: przyprostokątna <b>5</b>, przeciwprostokątna <b>13</b> &rarr; z trójki <b>(5, 12, 13)</b> wysokość ściany ma <b>12 cm</b>!
    </div>
    <div class="box-white">
      <b>Wzorzec CKE #2 (Graniastosłup – str. 192 podstawy):</b><br>
      W podstawie trójkąt równoramienny o kątach 45&deg; i najdłuższym boku <b>6&radic;2 dm</b>.<br>
      👉 To połówka kwadratu! Przyprostokątne mają po <b>6 dm</b>, więc pole podstawy P<sub>p</sub> = (6 &middot; 6) / 2 = <b>18 dm²</b>!
    </div>
  </div>
</div>

<div class="footer-tip">
  🏆 Złota zasada czwartkowych zadań otwartych (3–4 pkt): Zawsze oblicz najpierw osobno P<sub>p</sub> (to już 1 pewny punkt w kluczu CKE!), potem H, a na końcu V!
</div>
</body>
</html>
"""

qz_md_10 = r"""# QUIZY SUKCESU: GEOMETRIA PRZESTRZENNA (Klasa 7 & 8)
## 5-minutowe wyzwania pewności siebie • 1 karta dziennie

### KARTA 1: KRAWĘDZIE, SZEŚCIAN I PROSTOPADŁOŚCIAN (Wtorek)
1. **(2 pkt)** Graniastosłup prosty ma **15 krawędzi**. Ile ma wierzchołków ($2n$) i ile ścian ($n+2$)?
2. **(2 pkt)** Suma długości wszystkich krawędzi sześcianu wynosi **$36\text{ cm}$**. Oblicz długość jednej krawędzi $a$ oraz objętość $V = a^3$.
3. **(2 pkt)** Akwarium ma wymiary $40\text{ cm} \times 30\text{ cm} \times 50\text{ cm}$. Ile **litrów** wody się w nim zmieści? *(Wskazówka: zamień na $\text{dm}$!)*.

### KARTA 2: GRANIASTOSŁUPY I TRÓJKĄT $45^\circ$ (Środa)
1. **(2 pkt)** Pole podstawy graniastosłupa wynosi $15\text{ cm}^2$, a wysokość $H = 8\text{ cm}$. Ile wynosi jego objętość $V$?
2. **(2 pkt)** Podstawą graniastosłupa jest trójkąt prostokątny o przyprostokątnych $6\text{ cm}$ i $8\text{ cm}$ (przeciwprostokątna $10\text{ cm}$), a wysokość bryły $H = 5\text{ cm}$. Oblicz pole podstawy $P_p$ i objętość $V$.
3. **(2 pkt – Wzorzec CKE str. 192)** Podstawą graniastosłupa prostego jest trójkąt prostokątny równoramienny o najdłuższym boku $6\sqrt{2}\text{ dm}$ (czyli przyprostokątne mają po $6\text{ dm}$), a wysokość graniastosłupa wynosi $4\text{ dm}$. Oblicz objętość tego graniastosłupa.

### KARTA 3: OSTROSŁUPY I ZASADA 3 KUBKÓW (Piątek + Spirala)
1. **(2 pkt)** Ostrosłup ma **16 krawędzi**. Jaki wielokąt jest w jego podstawie i ile ma wszystkich ścian?
2. **(2 pkt)** Graniastosłup i ostrosłup mają takie same podstawy i równe wysokości. Objętość graniastosłupa wynosi $60\text{ cm}^3$. Ile wynosi objętość ostrosłupa?
3. **(2 pkt – Spirala z Pierwiastków)** Oblicz wartość wyrażenia $\sqrt{25 + 144}$ i skojarz ją z trójką pitagorejską $(5, 12, 13)$!

### KARTA 4: PITAGORAS W OSTROSŁUPIE – ZADANIE OTWARTE CKE (Czwartek / Sobota)
1. **(2 pkt)** Ostrosłup prawidłowy czworokątny ma krawędź podstawy $a = 6\text{ cm}$ i wysokość bryły $H = 8\text{ cm}$. Oblicz jego objętość $V = \frac{1}{3} P_p \cdot H$.
2. **(2 pkt)** W ostrosłupie prawidłowym czworokątnym krawędź podstawy ma $10\text{ cm}$, a krawędź boczna ma $13\text{ cm}$. Korzystając z trójki $(5, 12, 13)$, wyznacz wysokość ściany bocznej $h_b$.
3. **(2 pkt – Wzorzec CKE str. 193)** Prostokąt $ABCD$ o bokach $AD = 10\text{ cm}$ i $AB = 20\text{ cm}$ jest podstawą ostrosłupa, a wysokość $H = 12\text{ cm}$. Oblicz objętość tego ostrosłupa.
"""

qz_html_10 = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Geometria Przestrzenna</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.33; }
  .page-break { page-break-after: always; }
  .header-main { text-align: center; border-bottom: 2.5px solid #0284c7; padding-bottom: 5px; margin-bottom: 10px; }
  .header-main h1 { margin: 0; font-size: 15.5pt; color: #0369a1; }
  .header-main p { margin: 2px 0 0 0; font-size: 9.2pt; color: #64748b; }
  .quiz-card { border: 2px solid #cbd5e1; border-radius: 10px; padding: 11px 14px; margin-bottom: 12px; background: #f8fafc; }
  .quiz-1 { border-color: #0284c7; }
  .quiz-2 { border-color: #0d9488; }
  .quiz-3 { border-color: #8b5cf6; }
  .quiz-4 { border-color: #f43f5e; }
  .quiz-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px dashed #cbd5e1; padding-bottom: 5px; margin-bottom: 7px; }
  .quiz-title { font-size: 11.5pt; font-weight: bold; }
  .quiz-1 .quiz-title { color: #0369a1; }
  .quiz-2 .quiz-title { color: #0f766e; }
  .quiz-3 .quiz-title { color: #6d28d9; }
  .quiz-4 .quiz-title { color: #be123c; }
  .quiz-meta { font-size: 9pt; font-weight: 600; color: #475569; }
  .task { margin-bottom: 7px; }
  .task-title { font-size: 9.6pt; font-weight: bold; color: #334155; margin-bottom: 2px; }
  .task-body { font-size: 9.8pt; padding-left: 8px; }
  .blank-line { display: inline-block; border-bottom: 1.5px solid #94a3b8; min-width: 55px; height: 15px; vertical-align: middle; margin: 0 3px; }
  .rank-box { margin-top: 7px; padding-top: 5px; border-top: 1px dotted #cbd5e1; display: flex; justify-content: space-between; font-size: 8.5pt; color: #475569; }
  .key-section { background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; font-size: 9.5pt; }
  .key-title { font-weight: bold; color: #1e293b; font-size: 10.2pt; margin-bottom: 3px; }
  .tip-box { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 5px 9px; font-size: 8.8pt; color: #92400e; margin-top: 3px; border-radius: 0 4px 4px 0; }
</style>
</head>
<body>

<div class="header-main">
  <h1>📦 QUIZY SUKCESU: GEOMETRIA PRZESTRZENNA (KLASA 7 &amp; 8)</h1>
  <p>5-minutowe wyzwania w blokach 15-minutowych • Karta Supermocy leży na biurku!</p>
</div>

<div class="quiz-card quiz-1">
  <div class="quiz-header">
    <div class="quiz-title">🎯 KARTA 1: KRAWĘDZIE, SZEŚCIAN I LITRY (WTOREK)</div>
    <div class="quiz-meta">Czas: 5–7 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Dekoder Krawędzi – 2 pkt)</div>
    <div class="task-body">
      Graniastosłup prosty ma <b>15 krawędzi</b> (3n = 15 &rarr; n = <span class="blank-line"></span>).<br>
      Liczba jego wierzchołków (2n) wynosi <span class="blank-line"></span>, a liczba wszystkich ścian (n + 2) wynosi <span class="blank-line"></span>.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Sześcian z drutu – 2 pkt)</div>
    <div class="task-body">
      Suma długości wszystkich 12 krawędzi sześcianu jest równa <b>36 cm</b>.<br>
      Długość jednej krawędzi a = 36 : 12 = <span class="blank-line"></span> cm, a objętość V = a³ = <span class="blank-line"></span> cm³.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Trik Akwarium w Litrach – 2 pkt)</div>
    <div class="task-body">
      Prostopadłościenne akwarium ma wymiary <b>40 cm &times; 30 cm &times; 50 cm</b>.<br>
      Zamień na dm: <span class="blank-line"></span> dm &times; <span class="blank-line"></span> dm &times; <span class="blank-line"></span> dm = <span class="blank-line"></span> dm³ = <span class="blank-line"></span> <b>litrów</b>.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Brył!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobry Trop!</b></span>
    <span>[ ] 1–2 pkt: <b>Rozgrzewka!</b></span>
  </div>
</div>

<div class="quiz-card quiz-2">
  <div class="quiz-header">
    <div class="quiz-title">📐 KARTA 2: GRANIASTOSŁUPY I WZORZEC CKE (ŚRODA)</div>
    <div class="quiz-meta">Czas: 5–7 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Szybka Objętość – 2 pkt)</div>
    <div class="task-body">
      Pole podstawy graniastosłupa wynosi P<sub>p</sub> = 15 cm², a wysokość H = 8 cm.<br>
      Objętość V = P<sub>p</sub> &middot; H = <span class="blank-line"></span> cm³.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Trójkąt 6-8-10 w podstawie – 2 pkt)</div>
    <div class="task-body">
      Podstawą graniastosłupa prostego jest trójkąt prostokątny o przyprostokątnych <b>6 cm</b> i <b>8 cm</b> (oraz przeciwprostokątnej 10 cm). Wysokość bryły H = 5 cm.<br>
      Pole podstawy P<sub>p</sub> = (6 &middot; 8)/2 = <span class="blank-line"></span> cm² &nbsp;&rarr;&nbsp; Objętość V = <span class="blank-line"></span> cm³.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Wzorzec CKE str. 192 – Trójkąt 45&deg; – 2 pkt)</div>
    <div class="task-body">
      Podstawą graniastosłupa jest trójkąt prostokątny równoramienny (kąty 45&deg;) o najdłuższym boku <b>6&radic;2 dm</b> (więc przyprostokątne mają po <b>6 dm</b>). Wysokość bryły wynosi <b>4 dm</b>.<br>
      P<sub>p</sub> = (6 &middot; 6)/2 = <span class="blank-line"></span> dm² &nbsp;&rarr;&nbsp; V = P<sub>p</sub> &middot; 4 = <span class="blank-line"></span> dm³.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Architektka Przestrzeni!</b></span>
    <span>[ ] 3–4 pkt: <b>Pewna Ręka!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>📦 QUIZY SUKCESU: GEOMETRIA PRZESTRZENNA (CZĘŚĆ 2)</h1>
  <p>Ostrosłupy, Zasada 3 Kubków i Pitagoras w Bryle (Wzorzec CKE str. 193)</p>
</div>

<div class="quiz-card quiz-3">
  <div class="quiz-header">
    <div class="quiz-title">⚡ KARTA 3: OSTROSŁUPY + SPIRALA PAMIĘCI (PIĄTEK)</div>
    <div class="quiz-meta">Czas: 5–7 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Krawędzie Ostrosłupa – 2 pkt)</div>
    <div class="task-body">
      Ostrosłup ma <b>16 krawędzi</b> (2n = 16 &rarr; n = <span class="blank-line"></span>).<br>
      Liczba jego wierzchołków (n + 1) wynosi <span class="blank-line"></span>, a liczba wszystkich ścian wynosi <span class="blank-line"></span>.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Zasada Trzech Kubków – 2 pkt)</div>
    <div class="task-body">
      Graniastosłup i ostrosłup mają identyczne podstawy i równe wysokości. Objętość graniastosłupa wynosi <b>60 cm³</b>. Objętość ostrosłupa wynosi: <span class="blank-line"></span> cm³.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Spirala Pamięci: Pierwiastki + Pitagoras – 2 pkt)</div>
    <div class="task-body">
      Oblicz pamiętając, że najpierw dodajemy pod pierwiastkiem:<br>
      &radic;(25 + 144) = &radic;<span class="blank-line"></span> = <span class="blank-line"></span> &nbsp;<i>(Złota trójka pitagorejska: 5, 12, 13!)</i>
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Czarodziejka Ostrosłupów!</b></span>
    <span>[ ] 3–4 pkt: <b>Bystre Oko!</b></span>
    <span>[ ] 1–2 pkt: <b>Trening!</b></span>
  </div>
</div>

<div class="quiz-card quiz-4">
  <div class="quiz-header">
    <div class="quiz-title">🏆 KARTA 4: MISJA OTWARTA CKE – PITAGORAS W OSTROSŁUPIE (CZWARTEK/SOBOTA)</div>
    <div class="quiz-meta">Czas: 7 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Objętość Ostrosłupa Czworokątnego – 2 pkt)</div>
    <div class="task-body">
      Ostrosłup prawidłowy czworokątny ma w podstawie kwadrat o boku <b>a = 6 cm</b>, a jego wysokość wynosi <b>H = 8 cm</b>.<br>
      Krok 1: P<sub>p</sub> = 6² = <span class="blank-line"></span> cm² &nbsp;|&nbsp; Krok 2: V = &frac13; &middot; P<sub>p</sub> &middot; 8 = <span class="blank-line"></span> cm³.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Ściana boczna z trójką 5-12-13 – 2 pkt)</div>
    <div class="task-body">
      W ostrosłupie prawidłowym czworokątnym krawędź podstawy ma <b>10 cm</b> (połowa boku = <b>5 cm</b>), a krawędź boczna ma <b>13 cm</b>.<br>
      Z trójki pitagorejskiej (5, 12, 13) wysokość ściany bocznej h<sub>b</sub> wynosi: <span class="blank-line"></span> cm.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Wzorzec CKE str. 193 – Pełne Zadanie Egzaminacyjne – 2 pkt)</div>
    <div class="task-body">
      Prostokąt o bokach <b>10 cm</b> i <b>20 cm</b> jest podstawą ostrosłupa, a wysokość ostrosłupa wynosi <b>H = 12 cm</b>. Oblicz objętość ostrosłupa:<br>
      P<sub>p</sub> = 10 &middot; 20 = <span class="blank-line"></span> cm² &nbsp;&rarr;&nbsp; V = &frac13; &middot; P<sub>p</sub> &middot; 12 = <span class="blank-line"></span> cm³.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Pogromczyni Zadań za 4 Punkty!</b></span>
    <span>[ ] 3–4 pkt: <b>Super Wynik!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🗝️ WSKAZÓWKI W STYLU GWO &amp; KLUCZ ODPOWIEDZI (GEOMETRIA PRZESTRZENNA)</h1>
  <p>Najpierw przeczytaj Wskazówkę Detektywa, a dopiero potem sprawdź rozwiązanie!</p>
</div>

<div class="key-section">
  <div class="key-title">🕵️‍♀️ Wskazówki Detektywa (w stylu GWO – zanim spojrzysz w klucz!)</div>
  &bull; <b>Karta 1 Zad. 3:</b> Zauważ, że 10 cm = 1 dm, więc 40 cm = 4 dm. Pomnóż wymiary w decymetrach!<br>
  &bull; <b>Karta 2 Zad. 2:</b> W trójkącie prostokątnym o bokach 6, 8, 10 kąt prosty leży naprzeciwko najdłuższego boku (10). Pole trójkąta liczymy z dwóch krótszych boków (6 i 8)!<br>
  &bull; <b>Karta 4 Zad. 1 i 3:</b> Aby nie liczyć ułamków w V = &frac13; &middot; P<sub>p</sub> &middot; H, najpierw podziel przez 3 tę liczbę (P<sub>p</sub> lub H), która dzieli się przez 3 bez reszty!
</div>

<div class="key-section">
  <div class="key-title">✅ Klucz Odpowiedzi: Karta 1 i Karta 2</div>
  <b>Karta 1:</b> <b>1.</b> n = 5; W = 10, S = 7. &nbsp; <b>2.</b> a = 3 cm, V = 3³ = 27 cm³. &nbsp; <b>3.</b> 4 dm &times; 3 dm &times; 5 dm = 60 dm³ = <b>60 litrów</b>.<br>
  <b>Karta 2:</b> <b>1.</b> V = 15 &middot; 8 = <b>120 cm³</b>. &nbsp; <b>2.</b> P<sub>p</sub> = 24 cm², V = 24 &middot; 5 = <b>120 cm³</b>. &nbsp; <b>3.</b> P<sub>p</sub> = 18 dm², V = 18 &middot; 4 = <b>72 dm³</b>.
  <div class="tip-box"><b>💡 Coaching dla rodzica:</b> Pochwal za zamianę cm na dm przed mnożeniem: <i>„Zobacz, dzięki zamianie na 4, 3 i 5 dm policzyłaś 60 litrów w pamięci w 3 sekundy zamiast mnożyć 60 000 cm³!”</i></div>
</div>

<div class="key-section">
  <div class="key-title">✅ Klucz Odpowiedzi: Karta 3 i Karta 4</div>
  <b>Karta 3:</b> <b>1.</b> n = 8 (ośmiokąt); W = 9, S = 9. &nbsp; <b>2.</b> V = 60 : 3 = <b>20 cm³</b>. &nbsp; <b>3.</b> &radic;169 = <b>13</b>.<br>
  <b>Karta 4:</b> <b>1.</b> P<sub>p</sub> = 36 cm², V = &frac13; &middot; 36 &middot; 8 = 12 &middot; 8 = <b>96 cm³</b>. &nbsp; <b>2.</b> h<sub>b</sub> = <b>12 cm</b>. &nbsp; <b>3.</b> P<sub>p</sub> = 200 cm², V = &frac13; &middot; 200 &middot; 12 = 200 &middot; 4 = <b>800 cm³</b>.
  <div class="tip-box"><b>💡 Coaching CKE:</b> Pokaż Nadii trik skracania przez 3: w zadaniu 3 zamiast dzielić 200 przez 3, skracamy 12 : 3 = 4 i mnożymy 200 &middot; 4 = 800!</div>
</div>

</body>
</html>
"""

# ==============================================================================
# MODUŁ 11: RACHUNEK PRAWDOPODOBIEŃSTWA I STATYSTYKA
# ==============================================================================
cs_md_11 = r"""# KARTA SUPERMOCY: STATYSTYKA I PRAWDOPODOBIEŃSTWO (Klasa 7 & 8)
## Sprytne Metody Nadii – Trik Sumy przy Średniej, Wykresy, Moneta, Kostka i Kule

---

### 📊 1. ZŁOTY TRIK ŚREDNIEJ ARYTMETYCZNEJ ("Tajemnica Sumy")

Klasyczny wzór: $\text{Średnia} = \frac{\text{Suma wszystkich liczb}}{\text{Liczba elementów } (n)}$.
Ale na egzaminie CKE najczęściej znasz średnią i szukasz **brakującej liczby**! Wtedy używasz **Supermocy Sumy**:
$$\mathbf{\text{SUMA WSZYSTKICH} = \text{ŚREDNIA} \times \text{LICZBA ELEMENTÓW } (n)}$$

> 🎯 **Wzorzec CKE (Dopisanie oceny):** Średnia czterech ocen Nadii wynosi $4{,}0$. Jaką piąta ocenę musi dostać, aby średnia wzrosła do $4{,}2$?
> - Krok 1 (Stara suma 4 ocen): $4 \cdot 4{,}0 = \mathbf{16}$
> - Krok 2 (Nowa suma 5 ocen): $5 \cdot 4{,}2 = \mathbf{21}$
> - Krok 3 (Piąta ocena to różnica!): $21 - 16 = \mathbf{5}$! *(Rozwiązane w 10 sekund bez równań!)*

---

### 🥧 2. DIAGRAMY KOŁOWE I SŁUPKOWE (Szybki Dekoder)

- **Całe koło to $100\%$ oraz $360^\circ$:**
  - Połowa koła $= 50\% = 180^\circ$
  - Ćwiartka koła (kąt prosty) $= 25\% = 90^\circ$
  - $\frac{1}{10}$ koła $= 10\% = 36^\circ$
- 🚨 **Antypułapka CKE na wykresach słupkowych:** Zawsze sprawdź, co jest na osi pionowej (*liczba uczniów*), a co na poziomej (*liczba rodzeństwa / ocena*)!

---

### 🎲 3. RACHUNEK PRAWDOPODOBIEŃSTWA ("Sprzyjające przez Wszystkie")

$$P(A) = \frac{\text{Liczba wyników SPRZYJAJĄCYCH}}{\text{Liczba WSZYSTKICH możliwych wyników}}$$

| Doświadczenie losowe | Wszystkie wyniki ($\Omega$) | Typowe pytania CKE i gotowce |
| :--- | :---: | :--- |
| **1 rzut monetą** | **$2$** (O, R) | Orzeł: $\frac{1}{2}$ |
| **2 rzuty monetą** | **$4$** (OO, OR, RO, RR) | Dwa orły: $\frac{1}{4}$ &nbsp;\textbar&nbsp; Dokładnie 1 orzeł (OR, RO): $\frac{2}{4} = \frac{1}{2}$ |
| **1 rzut kostką sześcienną** | **$6$** (1, 2, 3, 4, 5, 6) | Parzyste (2,4,6): $\frac{3}{6}=\frac{1}{2}$ &nbsp;\textbar&nbsp; Liczba pierwsza (**2, 3, 5** – *1 nie jest pierwsza!*): $\frac{3}{6}=\frac{1}{2}$ |
| **2 rzuty kostką** | **$36$** ($6 \times 6$) | Jednakowe oczka (1-1, 2-2, ..., 6-6): $\frac{6}{36} = \frac{1}{6}$ |
| **Losowanie kuli z worka** | Suma wszystkich kul w worku | 3 białe i 7 czarnych $\implies$ wszystkich jest **$10$**! Szansa na białą: $\frac{3}{10}$. |
"""

cs_html_11 = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Statystyka i Prawdopodobieństwo</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 9.8pt; line-height: 1.3; }
  .header { text-align: center; border-bottom: 3px solid #7c3aed; padding-bottom: 4px; margin-bottom: 7px; }
  .header h1 { margin: 0; font-size: 15.8pt; color: #5b21b6; text-transform: uppercase; }
  .header .sub { font-size: 9.5pt; font-weight: 600; color: #475569; }
  .card { border-radius: 8px; padding: 6px 10px; border: 1.5px solid #cbd5e1; background: #fff; margin-bottom: 6px; }
  .card-purple { border-color: #7c3aed; background: #f5f3ff; }
  .card-teal { border-color: #0d9488; background: #f0fdfa; }
  .card-amber { border-color: #f59e0b; background: #fffbeb; }
  .card-rose { border-color: #f43f5e; background: #fff1f2; }
  .card-title { font-size: 10.6pt; font-weight: bold; margin-bottom: 4px; }
  .card-purple .card-title { color: #5b21b6; }
  .card-teal .card-title { color: #0f766e; }
  .card-amber .card-title { color: #b45309; }
  .card-rose .card-title { color: #be123c; }
  table.p-table { width: 100%; border-collapse: collapse; font-size: 8.8pt; background: #fff; }
  table.p-table th, table.p-table td { padding: 3px 6px; border: 1px solid #ddd6fe; text-align: center; }
  table.p-table th { background: #ede9fe; color: #4c1d95; font-weight: bold; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .box-white { background: #fff; border: 1px solid #cbd5e1; border-radius: 5px; padding: 5px 8px; margin-top: 3px; font-size: 9pt; }
  .footer-tip { text-align: center; font-size: 8.6pt; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 4px; font-weight: 600; }
</style>
</head>
<body>
<div class="header">
  <h1>🎲 KARTA SUPERMOCY: STATYSTYKA I PRAWDOPODOBIEŃSTWO (KL. 7 &amp; 8)</h1>
  <div class="sub">Złoty Trik Sumy przy Średniej, Diagramy, Kostka, Moneta i Kule w Worku</div>
</div>

<div class="card card-purple">
  <div class="card-title">📊 1. ZŁOTY TRIK ŚREDNIEJ ARYTMETYCZNEJ ("TAJEMNICA SUMY")</div>
  <div class="grid-2">
    <div class="box-white">
      <b>Wzór podstawowy:</b><br>
      Średnia = (Suma wszystkich elementów) : (Liczba elementów n)<br><br>
      ⚡ <b>SUPERMOC ODWRÓCENIA (Gdy znasz średnią!):</b><br>
      <b style="color:#5b21b6; font-size:9.8pt;">SUMA = ŚREDNIA &times; LICZBA ELEMENTÓW (n)</b>
    </div>
    <div class="box-white">
      🎯 <b>Zadanie-Pewniak CKE:</b><br>
      Średnia 4 liczb wynosi <b>10</b>. Dopisano piątą liczbę i średnia wzrosła do <b>12</b>. Jaką liczbę dopisano?<br>
      &bull; Stara suma (4 liczb): 4 &times; 10 = <b>40</b><br>
      &bull; Nowa suma (5 liczb): 5 &times; 12 = <b>60</b><br>
      &bull; Dopisana liczba: 60 &minus; 40 = <b>20</b>! <i>(Czas: 10 sekund!)</i>
    </div>
  </div>
</div>

<div class="card card-teal">
  <div class="card-title">🎲 2. RACHUNEK PRAWDOPODOBIEŃSTWA: P(A) = SPRZYJAJĄCE / WSZYSTKIE</div>
  <table class="p-table">
    <thead>
      <tr><th>Doświadczenie</th><th>Wszystkie wyniki</th><th>Najczęstsze pytania CKE (Gotowce!)</th></tr>
    </thead>
    <tbody>
      <tr><td><b>2 rzuty monetą</b></td><td><b>4</b>: (OO, OR, RO, RR)</td><td>Dwa orły (OO): <b>1/4</b> &nbsp;|&nbsp; Dokładnie 1 orzeł (OR, RO): <b>2/4 = 1/2</b> &nbsp;|&nbsp; Co najmniej 1 orzeł: <b>3/4</b></td></tr>
      <tr><td><b>1 rzut kostką (1..6)</b></td><td><b>6</b>: (1, 2, 3, 4, 5, 6)</td><td>Parzyste (2,4,6): <b>3/6 = 1/2</b> &nbsp;|&nbsp; Podzielne przez 3 (3,6): <b>2/6 = 1/3</b> &nbsp;|&nbsp; Liczba pierwsza (<b>2,3,5</b>): <b>3/6 = 1/2</b></td></tr>
      <tr><td><b>2 rzuty kostką</b></td><td><b>36</b> (bo 6 &times; 6)</td><td>Taka sama liczba oczek (1-1, 2-2, 3-3, 4-4, 5-5, 6-6): <b>6/36 = 1/6</b></td></tr>
      <tr><td><b>Losowanie kuli</b></td><td><b>Suma wszystkich kul!</b></td><td>W worku jest 5 białych i 10 czarnych &rarr; wszystkich jest <b>15</b> (nie 10!). Szansa na białą: <b>5/15 = 1/3</b></td></tr>
    </tbody>
  </table>
</div>

<div class="grid-2">
  <div class="card card-amber">
    <div class="card-title">🥧 3. DIAGRAMY KOŁOWE I SŁUPKOWE</div>
    <div class="box-white">
      <b>Całe koło = 100% = 360&deg;</b><br>
      &bull; Połowa koła = <b>50% = 180&deg;</b><br>
      &bull; Ćwiartka koła (kąt prosty) = <b>25% = 90&deg;</b><br>
      &bull; Jedna piąta koła = <b>20% = 72&deg;</b><br>
      &bull; Jedna dziesiąta koła = <b>10% = 36&deg;</b>
    </div>
  </div>

  <div class="card card-rose">
    <div class="card-title">🚨 4. TRZY ANTYPUŁAPKI EGZAMINACYJNE CKE</div>
    <div class="box-white" style="border-color:#fecdd3; background:#fff1f2;">
      1. <b>Jedynka (1) NIE jest liczbą pierwszą!</b> Na kostce liczby pierwsze to tylko: <b>2, 3 oraz 5</b>.<br>
      2. <b>Worek z kulami:</b> W mianowniku zawsze wpisz <b>sumę wszystkich kul</b>, a nie liczbę kul drugiego koloru!<br>
      3. <b>Zero w średniej:</b> Jeśli uczeń dostał oceny 5, 4, 0, to dzielimy przez <b>3</b> oceny (zero też jest elementem!).
    </div>
  </div>
</div>

<div class="footer-tip">
  🏆 Prawdopodobieństwo to zawsze ułamek od 0 (zdarzenie niemożliwe) do 1 (zdarzenie pewne). Nigdy nie może wyjść więcej niż 1!
</div>
</body>
</html>
"""

qz_md_11 = r"""# QUIZY SUKCESU: STATYSTYKA I PRAWDOPODOBIEŃSTWO (Klasa 7 & 8)
## 5-minutowe wyzwania pewności siebie

### KARTA 1: ŚREDNIA ARYTMETYCZNA I TRIK SUMY (Wtorek)
1. **(2 pkt)** Oblicz średnią arytmetyczną czterech liczb: $5, \; 7, \; 8, \; 12$.
2. **(2 pkt)** Średnia wieku 3 sióstr wynosi $11$ lat. Ile wynosi **łączna suma** ich lat?
3. **(2 pkt – Pewniak CKE)** Średnia czterech ocen Janka to $3{,}5$. Jaką piątą ocenę musi dostać, aby jego średnia wzrosła do $4{,}0$?

### KARTA 2: KOSTKA DO GRY I MONETA (Środa)
1. **(2 pkt)** Rzucamy jeden raz zwykłą sześcienną kostką do gry. Jakie jest prawdopodobieństwo wyrzucenia liczby oczek **większej od 4** (czyli 5 lub 6)?
2. **(2 pkt)** Rzucamy jeden raz kostką. Jakie jest prawdopodobieństwo wyrzucenia **liczby pierwszej**? *(Pamiętaj: 1 nie jest pierwsza!)*.
3. **(2 pkt)** Rzucamy dwa razy monetą (wyniki: OO, OR, RO, RR). Jakie jest prawdopodobieństwo, że wypadnie **dokładnie jeden orzeł**?

### KARTA 3: KULE W WORKU I DIAGRAMY + SPIRALA (Piątek)
1. **(2 pkt)** W pudełku jest $6$ kul białych i $9$ kul czerwonych. Losujemy jedną kulę. Ile jest **wszystkich** kul i jakie jest prawdopodobieństwo wylosowania kuli białej?
2. **(2 pkt)** Na diagramie kołowym wydatki na wakacje zajmują ćwiartkę koła (kąt prosty $90^\circ$). Jaki to procent całego budżetu ($1000\text{ zł}$) i ile to złotych?
3. **(2 pkt – Spirala z Równań)** Rozwiąż w pamięci równanie: $3x - 5 = 16$.

### KARTA 4: ZBIORY OBIEKTÓW I DWIE KOSTKI – MISJA CKE (Czwartek / Sobota)
1. **(2 pkt)** Ile jest wszystkich liczb dwucyfrowych utworzonych wyłącznie z cyfr $2, 5, 7$, jeśli cyfry **nie mogą** się powtarzać? *(Wypisz je!)*.
2. **(2 pkt)** Rzucamy dwa razy sześcienną kostką do gry ($36$ możliwych par). Jakie jest prawdopodobieństwo, że suma oczek wyniesie **dokładnie 11** (pary: $(5,6)$ oraz $(6,5)$)?
3. **(2 pkt)** W worku jest $8$ kul zielonych i pewna liczba kul żółtych. Prawdopodobieństwo wylosowania kuli zielonej wynosi $\frac{1}{3}$. Ile jest **wszystkich** kul w worku i ile jest żółtych?
"""

qz_html_11 = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Statystyka i Prawdopodobieństwo</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.33; }
  .page-break { page-break-after: always; }
  .header-main { text-align: center; border-bottom: 2.5px solid #7c3aed; padding-bottom: 5px; margin-bottom: 10px; }
  .header-main h1 { margin: 0; font-size: 15.5pt; color: #5b21b6; }
  .header-main p { margin: 2px 0 0 0; font-size: 9.2pt; color: #64748b; }
  .quiz-card { border: 2px solid #cbd5e1; border-radius: 10px; padding: 11px 14px; margin-bottom: 12px; background: #f8fafc; }
  .quiz-1 { border-color: #7c3aed; }
  .quiz-2 { border-color: #0d9488; }
  .quiz-3 { border-color: #0284c7; }
  .quiz-4 { border-color: #f43f5e; }
  .quiz-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px dashed #cbd5e1; padding-bottom: 5px; margin-bottom: 7px; }
  .quiz-title { font-size: 11.5pt; font-weight: bold; }
  .quiz-1 .quiz-title { color: #5b21b6; }
  .quiz-2 .quiz-title { color: #0f766e; }
  .quiz-3 .quiz-title { color: #0369a1; }
  .quiz-4 .quiz-title { color: #be123c; }
  .quiz-meta { font-size: 9pt; font-weight: 600; color: #475569; }
  .task { margin-bottom: 7px; }
  .task-title { font-size: 9.6pt; font-weight: bold; color: #334155; margin-bottom: 2px; }
  .task-body { font-size: 9.8pt; padding-left: 8px; }
  .blank-line { display: inline-block; border-bottom: 1.5px solid #94a3b8; min-width: 55px; height: 15px; vertical-align: middle; margin: 0 3px; }
  .rank-box { margin-top: 7px; padding-top: 5px; border-top: 1px dotted #cbd5e1; display: flex; justify-content: space-between; font-size: 8.5pt; color: #475569; }
  .key-section { background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; font-size: 9.5pt; }
  .key-title { font-weight: bold; color: #1e293b; font-size: 10.2pt; margin-bottom: 3px; }
  .tip-box { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 5px 9px; font-size: 8.8pt; color: #92400e; margin-top: 3px; border-radius: 0 4px 4px 0; }
</style>
</head>
<body>

<div class="header-main">
  <h1>🎲 QUIZY SUKCESU: STATYSTYKA I PRAWDOPODOBIEŃSTWO (KL. 7 &amp; 8)</h1>
  <p>5-minutowe wyzwania w blokach 15-minutowych • Karta Supermocy leży na biurku!</p>
</div>

<div class="quiz-card quiz-1">
  <div class="quiz-header">
    <div class="quiz-title">📊 KARTA 1: ŚREDNIA ARYTMETYCZNA I TRIK SUMY (WTOREK)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Rozgrzewka – 2 pkt)</div>
    <div class="task-body">
      Oblicz średnią arytmetyczną czterech liczb: <b>5, 7, 8, 12</b>.<br>
      Suma = <span class="blank-line"></span> &nbsp;&rarr;&nbsp; Średnia = Suma : 4 = <span class="blank-line"></span>.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Odwrócenie Średniej – 2 pkt)</div>
    <div class="task-body">
      Średnia wieku 3 sióstr wynosi <b>11 lat</b>. Ile wynosi łączna suma ich lat?<br>
      Suma = 3 &times; 11 = <span class="blank-line"></span> lat.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Pewniak Egzaminacyjny CKE – 2 pkt)</div>
    <div class="task-body">
      Średnia czterech ocen Janka to <b>3,5</b>. Jaką piątą ocenę musi dostać, aby jego średnia wzrosła do <b>4,0</b>?<br>
      Stara suma (4 &times; 3,5) = <span class="blank-line"></span> &nbsp;|&nbsp; Nowa suma (5 &times; 4,0) = <span class="blank-line"></span> &nbsp;&rarr;&nbsp; Piąta ocena: <span class="blank-line"></span>.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Statystyki!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobry Trop!</b></span>
    <span>[ ] 1–2 pkt: <b>Rozgrzewka!</b></span>
  </div>
</div>

<div class="quiz-card quiz-2">
  <div class="quiz-header">
    <div class="quiz-title">🎲 KARTA 2: KOSTKA DO GRY I MONETA (ŚRODA)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Rzut kostką – 2 pkt)</div>
    <div class="task-body">
      Rzucamy raz sześcienną kostką do gry. Jakie jest prawdopodobieństwo wyrzucenia liczby oczek <b>większej od 4</b> (czyli 5 lub 6)?<br>
      P(A) = <span class="blank-line"></span> / 6 = <span class="blank-line"></span> (po skróceniu).
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Pułapka Liczb Pierwszych na Kostce – 2 pkt)</div>
    <div class="task-body">
      Rzucamy raz kostką. Wypisz oczka będące liczbami pierwszymi (pamiętaj o 1!): <span class="blank-line" style="min-width:80px;"></span>.<br>
      Prawdopodobieństwo wyrzucenia liczby pierwszej wynosi: <span class="blank-line"></span> / 6 = <span class="blank-line"></span>.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Dwa rzuty monetą – 2 pkt)</div>
    <div class="task-body">
      Rzucamy dwa razy monetą (wszystkie wyniki: OO, OR, RO, RR). Jakie jest prawdopodobieństwo wyrzucenia <b>dokładnie jednego orła</b>?<br>
      P(A) = <span class="blank-line"></span> / 4 = <span class="blank-line"></span>.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Królowa Prawdopodobieństwa!</b></span>
    <span>[ ] 3–4 pkt: <b>Bystre Oko!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🎲 QUIZY SUKCESU: STATYSTYKA I PRAWDOPODOBIEŃSTWO (CZĘŚĆ 2)</h1>
  <p>Kule w worku, Diagramy, Kombinatoryka i Spirala Pamięci</p>
</div>

<div class="quiz-card quiz-3">
  <div class="quiz-header">
    <div class="quiz-title">⚡ KARTA 3: KULE, DIAGRAMY + SPIRALA PAMIĘCI (PIĄTEK)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Kule w pudełku – 2 pkt)</div>
    <div class="task-body">
      W pudełku jest <b>6 kul białych</b> i <b>9 kul czerwonych</b>. Losujemy jedną kulę.<br>
      Wszystkich kul jest: 6 + 9 = <span class="blank-line"></span> &nbsp;&rarr;&nbsp; P(biała) = 6 / <span class="blank-line"></span> = <span class="blank-line"></span> (po skróceniu przez 3).
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Diagram kołowy – 2 pkt)</div>
    <div class="task-body">
      Na diagramie kołowym wydatki na książki stanowią ćwiartkę koła (kąt prosty 90&deg;) z budżetu <b>400 zł</b>.<br>
      Jaki to procent? <span class="blank-line"></span>% &nbsp;&rarr;&nbsp; Ile to złotych? <span class="blank-line"></span> zł.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Spirala Pamięci: Równania – 2 pkt)</div>
    <div class="task-body">
      Rozwiąż równanie metodą Wagi Szalkowej: <b>3x &minus; 5 = 16</b> &nbsp;&rarr;&nbsp; 3x = <span class="blank-line"></span> &nbsp;&rarr;&nbsp; x = <span class="blank-line"></span>.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Analizy Danych!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobry Wynik!</b></span>
    <span>[ ] 1–2 pkt: <b>Trening!</b></span>
  </div>
</div>

<div class="quiz-card quiz-4">
  <div class="quiz-header">
    <div class="quiz-title">🏆 KARTA 4: KOMBINATORYKA I ZADANIA CKE (CZWARTEK/SOBOTA)</div>
    <div class="quiz-meta">Czas: 5–7 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Zliczanie obiektów – Dział XII pkt 1 CKE – 2 pkt)</div>
    <div class="task-body">
      Wypisz wszystkie liczby dwucyfrowe utworzone z cyfr <b>2, 5, 7</b>, w których cyfry się <b>nie powtarzają</b>:<br>
      25, 27, <span class="blank-line" style="min-width:140px;"></span> &nbsp;&rarr;&nbsp; Razem jest ich: <span class="blank-line"></span>.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Dwa rzuty kostką – 2 pkt)</div>
    <div class="task-body">
      Rzucamy dwa razy kostką (wszystkich par jest 36). Jakie jest prawdopodobieństwo, że suma oczek wyniesie <b>11</b> (sprzyjają tylko pary: (5,6) oraz (6,5))?<br>
      P(A) = <span class="blank-line"></span> / 36 = <span class="blank-line"></span>.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Zagadka Mistrza CKE z Kulami – 2 pkt)</div>
    <div class="task-body">
      W worku jest <b>8 kul zielonych</b> i pewna liczba żółtych. Szansa wylosowania zielonej wynosi <b>1/3</b>.<br>
      Wszystkich kul w worku jest: 8 &times; 3 = <span class="blank-line"></span>, więc kul żółtych jest: <span class="blank-line"></span> &minus; 8 = <span class="blank-line"></span>.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Pogromczyni Arkuszy CKE!</b></span>
    <span>[ ] 3–4 pkt: <b>Super Wynik!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🗝️ WSKAZÓWKI W STYLU GWO &amp; KLUCZ ODPOWIEDZI (STATYSTYKA I SZANSE)</h1>
  <p>Weryfikacja i wskazówki coachingowe dla Rodzica</p>
</div>

<div class="key-section">
  <div class="key-title">🕵️‍♀️ Wskazówki Detektywa (w stylu GWO – zanim spojrzysz w klucz!)</div>
  &bull; <b>Karta 1 Zad. 3:</b> Oblicz najpierw ile punktów w sumie dawały 4 stare oceny Janka (4 &times; 3,5), a ile musi dawać 5 ocen (5 &times; 4,0).<br>
  &bull; <b>Karta 3 Zad. 1:</b> Zanim zapiszesz ułamek, dodaj kule białe i czerwone – to jest Twój mianownik!<br>
  &bull; <b>Karta 4 Zad. 3:</b> Skoro 8 zielonych kul stanowi 1/3 wszystkich kul w worku, to cały worek mieści 3 razy więcej kul niż 8!
</div>

<div class="key-section">
  <div class="key-title">✅ Klucz Odpowiedzi: Karta 1 i Karta 2</div>
  <b>Karta 1:</b> <b>1.</b> Suma = 32, Średnia = 32 : 4 = <b>8</b>. &nbsp; <b>2.</b> Suma = <b>33 lata</b>. &nbsp; <b>3.</b> Stara suma = 14, Nowa suma = 20 &rarr; Piąta ocena = 20 &minus; 14 = <b>6</b>.<br>
  <b>Karta 2:</b> <b>1.</b> 2/6 = <b>1/3</b>. &nbsp; <b>2.</b> Liczby pierwsze: <b>2, 3, 5</b>; P = 3/6 = <b>1/2</b>. &nbsp; <b>3.</b> Sprzyjają OR i RO &rarr; P = 2/4 = <b>1/2</b>.
  <div class="tip-box"><b>💡 Coaching dla rodzica:</b> Zadanie 3 z Karty 1 pojawia się niemal co roku na egzaminie ósmoklasisty. Pochwal Nadię: <i>„Trik ze starą i nową sumą daje wynik w 5 sekund, podczas gdy inni męczą się z ułamkowym równaniem!”</i></div>
</div>

<div class="key-section">
  <div class="key-title">✅ Klucz Odpowiedzi: Karta 3 i Karta 4</div>
  <b>Karta 3:</b> <b>1.</b> Wszystkich = 15; P = 6/15 = <b>2/5</b>. &nbsp; <b>2.</b> <b>25%</b>; 400 : 4 = <b>100 zł</b>. &nbsp; <b>3.</b> 3x = 21 &rarr; <b>x = 7</b>.<br>
  <b>Karta 4:</b> <b>1.</b> 25, 27, <b>52, 57, 72, 75</b> &rarr; Razem: <b>6 liczb</b>. &nbsp; <b>2.</b> 2/36 = <b>1/18</b>. &nbsp; <b>3.</b> Wszystkich = <b>24</b>, żółtych = 24 &minus; 8 = <b>16</b>.
</div>

</body>
</html>
"""

# ==============================================================================
# MODUŁ 12: ZADANIA TEKSTOWE – PRĘDKOŚĆ, DROGA, CZAS, PROPORCJE I SKALA
# ==============================================================================
cs_md_12 = r"""# KARTA SUPERMOCY: PRĘDKOŚĆ, DROGA, CZAS, PROPORCJE I SKALA (Kl. 7 & 8)
## Sprytne Metody Nadii – Złoty Zegar, Trójkąt $s=v\cdot t$, Woreczki Proporcji i Skala

---

### ⏱️ 1. ZŁOTY PRZELICZNIK ZEGARA (Najczęstsza Pułapka CKE!)

Godzina ma **$60\text{ minut}$** (a nie $100$!). Dlatego ułamki godziny przeliczamy przez $60$:

| Ułamek zwykły / dziesiętny | Liczba minut | Jak to zapamiętać w 3 sekundy? |
| :---: | :---: | :--- |
| **$\frac{1}{2}\text{ h} = 0{,}5\text{ h}$** | **$30\text{ min}$** | Pół godziny |
| **$\frac{1}{4}\text{ h} = 0{,}25\text{ h}$** | **$15\text{ min}$** | Kwadrans ($\frac{3}{4}\text{ h} = 45\text{ min}$) |
| **$\frac{1}{3}\text{ h}$** | **$20\text{ min}$** | $60 : 3 = 20\text{ min}$ ($\frac{2}{3}\text{ h} = 40\text{ min}$) |
| **$\frac{1}{5}\text{ h} = 0{,}2\text{ h}$** | **$12\text{ min}$** | $60 : 5 = 12\text{ min}$ (**Uwaga:** $2{,}2\text{ h} = 2\text{ h } 12\text{ min}$, NIE $2\text{ h } 20\text{ min}$!) |
| **$\frac{1}{10}\text{ h} = 0{,}1\text{ h}$** | **$6\text{ min}$** | Każda $0{,}1\text{ h}$ to **$6\text{ minut}$**! ($0{,}3\text{ h} = 18\text{ min}$, $0{,}4\text{ h} = 24\text{ min}$) |

---

### 🚗 2. TRÓJKĄT PRĘDKOŚCI ($s = v \cdot t$) I METODA SKALI CZASOWEJ

- **Wzory z trójkąta:** $\text{Droga } s = v \cdot t \quad | \quad \text{Prędkość } v = \frac{s}{t} \quad | \quad \text{Czas } t = \frac{s}{v}$
- ⚡ **Metoda Skali Czasowej (Bez ułamków!):**
  *Samochód jedzie z prędkością $80\text{ km/h}$. Ile przejedzie w $15\text{ minut}$?*
  - $60\text{ min} \longrightarrow 80\text{ km}$
  - $15\text{ min}$ (4 razy krócej!) $\longrightarrow 80 : 4 = \mathbf{20\text{ km}}$!
- 🔄 **Przelicznik $\text{km/h} \leftrightarrow \text{m/s}$ (Mnożnik $3{,}6$):**
  - **$1\text{ m/s} = 3{,}6\text{ km/h}$** &nbsp;|&nbsp; **$10\text{ m/s} = 36\text{ km/h}$** &nbsp;|&nbsp; **$20\text{ m/s} = 72\text{ km/h}$** &nbsp;|&nbsp; **$25\text{ m/s} = 90\text{ km/h}$**

---

### ⚖️ 3. PODZIAŁ PROPORCJONALNY ("Metoda Woreczków / Części" – Dział VII kl. 7–8)

*Zadanie CKE: Podziel kwotę $140\text{ zł}$ w stosunku $2 : 5$.*
1. **Dodaj części (woreczki):** $2 + 5 = \mathbf{7\text{ równych części}}$.
2. **Oblicz 1 część:** $140\text{ zł} : 7 = \mathbf{20\text{ zł}}$.
3. **Rozdaj części:** Pierwsza osoba: $2 \cdot 20 = \mathbf{40\text{ zł}}$, druga osoba: $5 \cdot 20 = \mathbf{100\text{ zł}}$!

---

### 🗺️ 4. SKALA MAPY ("Skreśl Dwa Zera na Metry, Pięć Zer na Kilometry!")

- Skala **$1 : 20\,000$**:
  - $1\text{ cm}$ na mapie $= 20\,000\text{ cm}$ w terenie $\xrightarrow{\text{skreśl 2 zera}} \mathbf{200\text{ m}} = \mathbf{0{,}2\text{ km}}$!
"""

cs_html_12 = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Karta Supermocy: Prędkość, Droga, Czas, Proporcje i Skala</title>
<style>
  @page { size: A4 portrait; margin: 8mm 10mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 9.8pt; line-height: 1.3; }
  .header { text-align: center; border-bottom: 3px solid #ea580c; padding-bottom: 4px; margin-bottom: 7px; }
  .header h1 { margin: 0; font-size: 15.5pt; color: #c2410c; text-transform: uppercase; }
  .header .sub { font-size: 9.5pt; font-weight: 600; color: #475569; }
  .card { border-radius: 8px; padding: 6px 10px; border: 1.5px solid #cbd5e1; background: #fff; margin-bottom: 6px; }
  .card-orange { border-color: #ea580c; background: #fff7ed; }
  .card-blue { border-color: #0284c7; background: #f0f9ff; }
  .card-teal { border-color: #0d9488; background: #f0fdfa; }
  .card-rose { border-color: #f43f5e; background: #fff1f2; }
  .card-title { font-size: 10.6pt; font-weight: bold; margin-bottom: 4px; }
  .card-orange .card-title { color: #c2410c; }
  .card-blue .card-title { color: #0369a1; }
  .card-teal .card-title { color: #0f766e; }
  .card-rose .card-title { color: #be123c; }
  table.p-table { width: 100%; border-collapse: collapse; font-size: 8.8pt; background: #fff; }
  table.p-table th, table.p-table td { padding: 3px 6px; border: 1px solid #fed7aa; text-align: center; }
  table.p-table th { background: #ffedd5; color: #9a3412; font-weight: bold; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
  .box-white { background: #fff; border: 1px solid #cbd5e1; border-radius: 5px; padding: 5px 8px; margin-top: 3px; font-size: 9pt; }
  .footer-tip { text-align: center; font-size: 8.6pt; color: #64748b; border-top: 1px dashed #cbd5e1; padding-top: 4px; font-weight: 600; }
</style>
</head>
<body>
<div class="header">
  <h1>🚗 KARTA SUPERMOCY: PRĘDKOŚĆ, CZAS, PROPORCJE I SKALA (KL. 7 &amp; 8)</h1>
  <div class="sub">Złoty Przelicznik Zegara, Trójkąt s = v &middot; t, Woreczki Proporcji i Skala Mapy</div>
</div>

<div class="card card-orange">
  <div class="card-title">⏱️ 1. ZŁOTY PRZELICZNIK ZEGARA (GODZINA MA 60 MINUT, NIE 100!)</div>
  <table class="p-table">
    <thead>
      <tr><th>Ułamek godziny</th><th>Minuty</th><th>Złota Kotwica Pamięciowa</th><th>Typowa Pułapka CKE!</th></tr>
    </thead>
    <tbody>
      <tr><td><b>1/2 h = 0,5 h</b></td><td><b>30 min</b></td><td>Pół godziny (60 : 2 = 30)</td><td>1,5 h = 1 h 30 min (NIE 1 h 50 min!)</td></tr>
      <tr><td><b>1/4 h = 0,25 h</b></td><td><b>15 min</b></td><td>Kwadrans &nbsp;|&nbsp; <b>3/4 h = 0,75 h = 45 min</b></td><td>2,25 h = 2 h 15 min</td></tr>
      <tr><td><b>1/3 h</b> &nbsp;|&nbsp; <b>2/3 h</b></td><td><b>20 min</b> | <b>40 min</b></td><td>60 : 3 = 20 min</td><td>20 min = 1/3 h (wzadaniach z v!)</td></tr>
      <tr><td><b>1/10 h = 0,1 h</b></td><td><b>6 min</b></td><td>Każde <b>0,1 h to 6 minut!</b> (0,2 h = 12 min, 0,4 h = 24 min)</td><td><b>2,2 h = 2 h 12 min</b> (NIE 2 h 20 min!)</td></tr>
    </tbody>
  </table>
</div>

<div class="grid-2">
  <div class="card card-blue">
    <div class="card-title">🚀 2. DROGA, PRĘDKOŚĆ, CZAS (s = v &middot; t)</div>
    <div class="box-white">
      &bull; <b>Droga:</b> s = v &middot; t &nbsp;|&nbsp; <b>Prędkość:</b> v = s / t &nbsp;|&nbsp; <b>Czas:</b> t = s / v<br>
      ⚡ <b>Metoda Skali Czasowej (Bez ułamków!):</b><br>
      Auto jedzie <b>90 km/h</b>. Ile przejedzie w <b>20 minut</b>?<br>
      60 min &rarr; 90 km &nbsp;|&nbsp; 20 min (3 razy krócej!) &rarr; 90 : 3 = <b>30 km</b>!
    </div>
    <div class="box-white" style="margin-top:4px;">
      🔄 <b>Złote Pary m/s &harr; km/h (Mnożnik 3,6):</b><br>
      <b>10 m/s = 36 km/h</b> &nbsp;|&nbsp; <b>15 m/s = 54 km/h</b><br>
      <b>20 m/s = 72 km/h</b> &nbsp;|&nbsp; <b>25 m/s = 90 km/h</b>
    </div>
  </div>

  <div class="card card-teal">
    <div class="card-title">⚖️ 3. PODZIAŁ PROPORCJONALNY ("WORECZKI")</div>
    <div class="box-white">
      <b>Wzorzec CKE:</b> Podziel <b>180 zł</b> w stosunku <b>2 : 7</b>.<br>
      &bull; <b>Krok 1 (Dodaj woreczki):</b> 2 + 7 = <b>9 równych części</b>.<br>
      &bull; <b>Krok 2 (Ile w 1 woreczku?):</b> 180 zł : 9 = <b>20 zł</b>.<br>
      &bull; <b>Krok 3 (Rozdaj):</b> 2 &middot; 20 = <b>40 zł</b> oraz 7 &middot; 20 = <b>140 zł</b>!
    </div>
    <div class="box-white" style="margin-top:4px;">
      <b>Trójkąt o kątach w stosunku 2 : 3 : 4:</b><br>
      Suma kątów = 180&deg;. Razem części: 2+3+4 = <b>9</b>.<br>
      1 część = 180&deg; : 9 = <b>20&deg;</b> &rarr; Kąty: <b>40&deg;, 60&deg;, 80&deg;</b>!
    </div>
  </div>
</div>

<div class="card card-rose">
  <div class="card-title">🗺️ 4. SKALA MAPY ("SKREŚL 2 ZERA NA METRY, 5 ZER NA KILOMETRY!")</div>
  <div class="box-white" style="border-color:#fecdd3;">
    <b>Skala 1 : 50 000</b> oznacza: 1 cm na mapie = <b>50 000 cm</b> w terenie.<br>
    &bull; Zamiana cm na <b>metry (m)</b> &rarr; skreślasz <b>2 zera</b>: 500<s>00</s> cm = <b>500 m</b>.<br>
    &bull; Zamiana cm na <b>kilometry (km)</b> &rarr; przesuwasz przecinek o <b>5 miejsc</b> (lub dzielisz metry przez 1000): 500 m = <b>0,5 km</b>!
  </div>
</div>

<div class="footer-tip">
  🏆 Antypułapka CKE: Średnia prędkość na całej trasie to CAŁA DROGA podzielona przez CAŁY CZAS (nigdy nie dodawaj dwóch prędkości i nie dziel przez 2!).
</div>
</body>
</html>
"""

qz_md_12 = r"""# QUIZY SUKCESU: PRĘDKOŚĆ, DROGA, CZAS, PROPORCJE I SKALA (Kl. 7 & 8)
## 5-minutowe wyzwania pewności siebie

### KARTA 1: ZŁOTY ZEGAR I JEDNOSTKI CZASU (Wtorek)
1. **(2 pkt)** Zamień na godziny i minuty (pamiętaj: $0{,}1\text{ h} = 6\text{ min}$!):
   a) $2{,}2\text{ h} = \dots\text{ h } \dots\text{ min}$ &nbsp;&nbsp;|&nbsp;&nbsp; b) $1{,}4\text{ h} = \dots\text{ h } \dots\text{ min}$
2. **(2 pkt)** Pociąg wyjechał o $8{:}40$ i przyjechał o $11{:}15$, przy czym po drodze miał $15\text{ minut}$ postoju. Ile czasu był w samym ruchu?
3. **(2 pkt)** Zamień prędkości: a) $10\text{ m/s} = \dots\text{ km/h}$ &nbsp;&nbsp;|&nbsp;&nbsp; b) $72\text{ km/h} = \dots\text{ m/s}$.

### KARTA 2: PRĘDKOŚĆ, DROGA, CZAS – METODA SKALI (Środa)
1. **(2 pkt)** Rowerzysta jedzie ze stałą prędkością $24\text{ km/h}$. Jaką drogę pokona w ciągu **kwadransa ($15\text{ minut}$)**?
2. **(2 pkt)** Samochód przejechał $30\text{ km}$ w ciągu $20\text{ minut}$ ($\frac{1}{3}\text{ h}$). Z jaką średnią prędkością (w $\text{km/h}$) jechał?
3. **(2 pkt)** Pani Ania jedzie do pracy $15\text{ km}$ z prędkością $60\text{ km/h}$. Ile **minut** zajmuje jej ta droga?

### KARTA 3: PODZIAŁ PROPORCJONALNY ("WORECZKI") + SPIRALA (Piątek)
1. **(2 pkt)** Sznurek o długości $45\text{ m}$ rozcięto w stosunku $2 : 7$. Na ile równych części dzielimy i jaką długość ma krótszy kawałek?
2. **(2 pkt)** Kąty wewnętrzne trójkąta pozostają w stosunku $1 : 2 : 6$. Oblicz miarę największego kąta tego trójkąta.
3. **(2 pkt – Spirala z Procentów)** Cena kurtki wynosiła $200\text{ zł}$. Po obniżce o $15\%$ kurtka kosztuje: $\dots\text{ zł}$.

### KARTA 4: SKALA MAPY I ZADANIA OTWARTE CKE (Czwartek / Sobota)
1. **(2 pkt)** Mapa jest wykonana w skali $1 : 40\,000$. Ile to **metrów**, a ile **kilometrów** w terenie odpowiada $1\text{ cm}$ na tej mapie?
2. **(2 pkt)** Odległość między dwoma schroniskami na mapie w skali $1 : 50\,000$ wynosi $6\text{ cm}$. Ile **kilometrów** wynosi ta odległość w rzeczywistości?
3. **(2 pkt)** Na przygotowanie $12$ babeczek potrzeba $150\text{ g}$ mąki. Ile gramów mąki potrzeba na przygotowanie $20$ takich babeczek?
"""

qz_html_12 = r"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="UTF-8">
<title>Quizy Sukcesu: Prędkość, Czas, Proporcje i Skala</title>
<style>
  @page { size: A4 portrait; margin: 10mm 12mm; }
  * { box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; color: #1e293b; margin: 0; padding: 0; font-size: 10.2pt; line-height: 1.33; }
  .page-break { page-break-after: always; }
  .header-main { text-align: center; border-bottom: 2.5px solid #ea580c; padding-bottom: 5px; margin-bottom: 10px; }
  .header-main h1 { margin: 0; font-size: 15.5pt; color: #c2410c; }
  .header-main p { margin: 2px 0 0 0; font-size: 9.2pt; color: #64748b; }
  .quiz-card { border: 2px solid #cbd5e1; border-radius: 10px; padding: 11px 14px; margin-bottom: 12px; background: #f8fafc; }
  .quiz-1 { border-color: #ea580c; }
  .quiz-2 { border-color: #0284c7; }
  .quiz-3 { border-color: #0d9488; }
  .quiz-4 { border-color: #f43f5e; }
  .quiz-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px dashed #cbd5e1; padding-bottom: 5px; margin-bottom: 7px; }
  .quiz-title { font-size: 11.5pt; font-weight: bold; }
  .quiz-1 .quiz-title { color: #c2410c; }
  .quiz-2 .quiz-title { color: #0369a1; }
  .quiz-3 .quiz-title { color: #0f766e; }
  .quiz-4 .quiz-title { color: #be123c; }
  .quiz-meta { font-size: 9pt; font-weight: 600; color: #475569; }
  .task { margin-bottom: 7px; }
  .task-title { font-size: 9.6pt; font-weight: bold; color: #334155; margin-bottom: 2px; }
  .task-body { font-size: 9.8pt; padding-left: 8px; }
  .blank-line { display: inline-block; border-bottom: 1.5px solid #94a3b8; min-width: 50px; height: 15px; vertical-align: middle; margin: 0 3px; }
  .rank-box { margin-top: 7px; padding-top: 5px; border-top: 1px dotted #cbd5e1; display: flex; justify-content: space-between; font-size: 8.5pt; color: #475569; }
  .key-section { background: #f8fafc; border: 1.5px solid #94a3b8; border-radius: 8px; padding: 8px 12px; margin-bottom: 8px; font-size: 9.5pt; }
  .key-title { font-weight: bold; color: #1e293b; font-size: 10.2pt; margin-bottom: 3px; }
  .tip-box { background: #fef3c7; border-left: 4px solid #f59e0b; padding: 5px 9px; font-size: 8.8pt; color: #92400e; margin-top: 3px; border-radius: 0 4px 4px 0; }
</style>
</head>
<body>

<div class="header-main">
  <h1>🚗 QUIZY SUKCESU: PRĘDKOŚĆ, CZAS, PROPORCJE I SKALA (KL. 7 &amp; 8)</h1>
  <p>5-minutowe wyzwania w blokach 15-minutowych • Karta Supermocy leży na biurku!</p>
</div>

<div class="quiz-card quiz-1">
  <div class="quiz-header">
    <div class="quiz-title">⏱️ KARTA 1: ZŁOTY PRZELICZNIK ZEGARA I PRĘDKOŚCI (WTOREK)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Pogromca Pułapki Zegara – 2 pkt)</div>
    <div class="task-body">
      Pamiętając, że <b>0,1 h = 6 minut</b>, zamień na godziny i minuty:<br>
      a) <b>2,2 h</b> = <span class="blank-line"></span> h <span class="blank-line"></span> min &nbsp;&nbsp;|&nbsp;&nbsp; b) <b>1,4 h</b> = <span class="blank-line"></span> h <span class="blank-line"></span> min
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Skoki na osi czasu – 2 pkt)</div>
    <div class="task-body">
      Pociąg wyjechał o <b>8:40</b> i dotarł do celu o <b>11:15</b>, ale po drodze stał <b>15 minut</b> na stacji.<br>
      Cały czas podróży: <span class="blank-line"></span> h <span class="blank-line"></span> min &nbsp;&rarr;&nbsp; Czas samego ruchu: <span class="blank-line"></span> h <span class="blank-line"></span> min.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Złote pary m/s i km/h – 2 pkt)</div>
    <div class="task-body">
      Zamień jednostki prędkości: &nbsp; a) <b>10 m/s</b> = <span class="blank-line"></span> km/h &nbsp;&nbsp;|&nbsp;&nbsp; b) <b>72 km/h</b> = <span class="blank-line"></span> m/s
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Władczyni Czasu!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobry Trop!</b></span>
    <span>[ ] 1–2 pkt: <b>Rozgrzewka!</b></span>
  </div>
</div>

<div class="quiz-card quiz-2">
  <div class="quiz-header">
    <div class="quiz-title">🚀 KARTA 2: PRĘDKOŚĆ, DROGA, CZAS BEZ UŁAMKÓW (ŚRODA)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Ile w kwadrans? – 2 pkt)</div>
    <div class="task-body">
      Rowerzysta jedzie ze stałą prędkością <b>24 km/h</b> (czyli 24 km w 60 minut).<br>
      Jaką drogę pokona w ciągu <b>15 minut</b> (4 razy krócej)? &nbsp; s = 24 : 4 = <span class="blank-line"></span> km.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Prędkość z 20 minut – 2 pkt)</div>
    <div class="task-body">
      Samochód przejechał <b>30 km w 20 minut</b>. Skoro w 20 minut przejechał 30 km, to w pełną godzinę (60 min = 3 &times; 20 min) przejedzie: <span class="blank-line"></span> km, więc jego prędkość to <span class="blank-line"></span> km/h!
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Czas przejazdu – 2 pkt)</div>
    <div class="task-body">
      Pani Ania ma do pracy <b>15 km</b> i jedzie ze średnią prędkością <b>60 km/h</b>.<br>
      Jaką częścią z 60 km jest 15 km? <span class="blank-line"></span> &nbsp;&rarr;&nbsp; Ile to minut? <span class="blank-line"></span> min.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Nawigacji!</b></span>
    <span>[ ] 3–4 pkt: <b>Bystre Oko!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🚗 QUIZY SUKCESU: PROPORCJE, SKALA I ZADANIA CKE (CZĘŚĆ 2)</h1>
  <p>Podział proporcjonalny („Metoda Woreczków”), Skala Mapy i Spirala Pamięci</p>
</div>

<div class="quiz-card quiz-3">
  <div class="quiz-header">
    <div class="quiz-title">⚖️ KARTA 3: PODZIAŁ PROPORCJONALNY + SPIRALA (PIĄTEK)</div>
    <div class="quiz-meta">Czas: 5 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Metoda Woreczków – Dział VII CKE – 2 pkt)</div>
    <div class="task-body">
      Sznurek o długości <b>45 m</b> rozcięto na dwie części w stosunku <b>2 : 7</b>.<br>
      Razem części: 2 + 7 = <span class="blank-line"></span> &nbsp;|&nbsp; 1 część = 45 : <span class="blank-line"></span> = <span class="blank-line"></span> m &nbsp;|&nbsp; Krótszy kawałek (2 części) = <span class="blank-line"></span> m.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Kąty w trójkącie w stosunku 1 : 2 : 6 – 2 pkt)</div>
    <div class="task-body">
      Kąty trójkąta (suma 180&deg;) są w stosunku <b>1 : 2 : 6</b> (razem 9 części).<br>
      1 część = 180&deg; : 9 = <span class="blank-line"></span>&deg; &nbsp;&rarr;&nbsp; Największy kąt (6 części) ma miarę: <span class="blank-line"></span>&deg;.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Spirala Pamięci: Procenty – 2 pkt)</div>
    <div class="task-body">
      Kurtka kosztowała <b>200 zł</b>. Ile kosztuje po obniżce o <b>15%</b>?<br>
      10% to <span class="blank-line"></span> zł, 5% to <span class="blank-line"></span> zł &rarr; Obniżka = <span class="blank-line"></span> zł &rarr; Nowa cena: <span class="blank-line"></span> zł.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Czarodziejka Proporcji!</b></span>
    <span>[ ] 3–4 pkt: <b>Dobry Wynik!</b></span>
    <span>[ ] 1–2 pkt: <b>Trening!</b></span>
  </div>
</div>

<div class="quiz-card quiz-4">
  <div class="quiz-header">
    <div class="quiz-title">🗺️ KARTA 4: SKALA MAPY I PROPORCJA CKE (CZWARTEK/SOBOTA)</div>
    <div class="quiz-meta">Czas: 5–7 min &nbsp;|&nbsp; Punkty: ___ / 6 pkt</div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 1 (Odcinanie zer w skali – 2 pkt)</div>
    <div class="task-body">
      Mapa jest w skali <b>1 : 40 000</b>. Zatem 1 cm na mapie to 40 000 cm w terenie.<br>
      Skreśl 2 zera na metry: 1 cm = <span class="blank-line"></span> m = <span class="blank-line"></span> km.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 2 (Odległość na mapie – 2 pkt)</div>
    <div class="task-body">
      Na mapie w skali <b>1 : 50 000</b> (gdzie 1 cm = 500 m = 0,5 km) szlak ma długość <b>6 cm</b>.<br>
      Rzeczywista długość szlaku wynosi: 6 &times; 0,5 km = <span class="blank-line"></span> km.
    </div>
  </div>
  <div class="task">
    <div class="task-title">Zadanie 3 (Proporcjonalność w kuchni – 2 pkt)</div>
    <div class="task-body">
      Na <b>12 babeczek</b> potrzeba <b>150 g</b> mąki (czyli na 4 babeczki potrzeba 150 : 3 = <span class="blank-line"></span> g).<br>
      Ile gramów mąki potrzeba na <b>20 babeczek</b> (5 &times; 4 babeczki)? &nbsp; Odpowiedź: <span class="blank-line"></span> g.
    </div>
  </div>
  <div class="rank-box">
    <span>🏆 [ ] 5–6 pkt: <b>Mistrzyni Zadań z Treścią!</b></span>
    <span>[ ] 3–4 pkt: <b>Super Wynik!</b></span>
    <span>[ ] 1–2 pkt: <b>Krok w przód!</b></span>
  </div>
</div>

<div class="page-break"></div>

<div class="header-main">
  <h1>🗝️ WSKAZÓWKI W STYLU GWO &amp; KLUCZ ODPOWIEDZI (PRĘDKOŚĆ, PROPORCJE, SKALA)</h1>
  <p>Weryfikacja i wskazówki coachingowe dla Rodzica</p>
</div>

<div class="key-section">
  <div class="key-title">🕵️‍♀️ Wskazówki Detektywa (w stylu GWO – zanim spojrzysz w klucz!)</div>
  &bull; <b>Karta 1 Zad. 2:</b> Odejmij 15 minut postoju już na samym początku lub na samym końcu – łatwiej policzyć od 8:40 do 11:00!<br>
  &bull; <b>Karta 3 Zad. 1:</b> Stosunek 2 : 7 oznacza, że całość dzielimy na 2 + 7 = 9 równych kawałków.<br>
  &bull; <b>Karta 4 Zad. 3:</b> Zamiast dzielić 150 przez 12, zauważ, że 12 i 20 dzielą się przez 4! Oblicz ile mąki idzie na 4 babeczki.
</div>

<div class="key-section">
  <div class="key-title">✅ Klucz Odpowiedzi: Karta 1 i Karta 2</div>
  <b>Karta 1:</b> <b>1.</b> a) <b>2 h 12 min</b>, b) <b>1 h 24 min</b>. &nbsp; <b>2.</b> Cały czas: 2 h 35 min; w ruchu: <b>2 h 20 min</b>. &nbsp; <b>3.</b> a) <b>36 km/h</b>, b) <b>20 m/s</b>.<br>
  <b>Karta 2:</b> <b>1.</b> <b>6 km</b>. &nbsp; <b>2.</b> 30 &middot; 3 = 90 km &rarr; <b>90 km/h</b>. &nbsp; <b>3.</b> 1/4 z 60 km &rarr; <b>15 minut</b>.
  <div class="tip-box"><b>💡 Coaching dla rodzica (Punkt zapalny ze sprawdzianu 30.09!):</b> Jeśli Nadia poprawnie napisała 2,2 h = 2 h 12 min, przybijcie piątkę! To definitywne pokonanie jej dawnej pułapki ze sprawdzianu!</div>
</div>

<div class="key-section">
  <div class="key-title">✅ Klucz Odpowiedzi: Karta 3 i Karta 4</div>
  <b>Karta 3:</b> <b>1.</b> 9 części; 1 część = 5 m; krótszy = <b>10 m</b>. &nbsp; <b>2.</b> 1 część = 20&deg;; największy = <b>120&deg;</b>. &nbsp; <b>3.</b> 20 zł + 10 zł = 30 zł obniżki &rarr; <b>170 zł</b>.<br>
  <b>Karta 4:</b> <b>1.</b> <b>400 m</b> = <b>0,4 km</b>. &nbsp; <b>2.</b> <b>3 km</b>. &nbsp; <b>3.</b> Na 4 babeczki: 50 g; na 20 babeczek: 5 &middot; 50 g = <b>250 g</b>.
</div>

</body>
</html>
"""

if __name__ == "__main__":
    write_and_render("10-geometria-przestrzenna", "karta-supermocy-cheat-sheet", cs_md_10, cs_html_10)
    write_and_render("10-geometria-przestrzenna", "quizy-sukcesu-5-minut", qz_md_10, qz_html_10)
    write_and_render("11-rachunek-prawdopodobienstwa-i-statystyka", "karta-supermocy-cheat-sheet", cs_md_11, cs_html_11)
    write_and_render("11-rachunek-prawdopodobienstwa-i-statystyka", "quizy-sukcesu-5-minut", qz_md_11, qz_html_11)
    write_and_render("12-zadania-tekstowe-predkosc-droga-czas", "karta-supermocy-cheat-sheet", cs_md_12, cs_html_12)
    write_and_render("12-zadania-tekstowe-predkosc-droga-czas", "quizy-sukcesu-5-minut", qz_md_12, qz_html_12)
    print("Phase 3 modules (10, 11, 12) generated successfully!")
