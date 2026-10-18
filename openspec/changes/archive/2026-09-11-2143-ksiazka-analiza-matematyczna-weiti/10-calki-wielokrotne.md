# Część X: Całki Wielokrotne i Ich Zastosowania Inżynierskie

Rachunek całkowy funkcji wielu zmiennych stanowi fundamentalne narzędzie modelowania procesów ciągłych w przestrzeni jedno-, dwu- i trójwymiarowej. W elektrotechnice i teorii pola elektromagnetycznego pozwala na wyznaczanie całkowitego ładunku zgromadzonego w obszarze o zadanej gęstości, pojemności układów przewodników o złożonej geometrii, energii pola elektrostatycznego i magnetycznego, a także na analizę szumów losowych w odbiornikach telekomunikacyjnych (całka prawdopodobieństwa Gaussa).

---

## Rozdział 21: Całka podwójna i jej zastosowania

### 21.1. Definicja całki podwójnej Riemanna

Niech $P = [a, b] \times [c, d] \subset \mathbb{R}^2$ będzie prostokątem domkniętym na płaszczyźnie, a funkcja $f: P \to \mathbb{R}$ niech będzie ograniczona.

#### Definicja 21.1 (Podział prostokąta i sumy całkowe)
1. **Podziałem** prostokąta $P$ nazywamy parę podziałów przedziałów:
   $$\Pi_x: a = x_0 < x_1 < \dots < x_n = b, \quad \Pi_y: c = y_0 < y_1 < \dots < y_m = d$$
   dzielących $P$ na $n \times m$ prostokątów cząstkowych $P_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j]$ o polach $\Delta S_{ij} = \Delta x_i \cdot \Delta y_j = (x_i - x_{i-1})(y_j - y_{j-1})$.
2. **Średnicą podziału** $\delta(\Pi)$ nazywamy największą z przekątnych prostokątów $P_{ij}$:
   $$\delta(\Pi) = \max_{i, j} \sqrt{(\Delta x_i)^2 + (\Delta y_j)^2}$$
3. W każdym prostokącie $P_{ij}$ wybieramy punkt pośredni $\xi_{ij} = (\xi_i, \eta_j) \in P_{ij}$. **Sumą całkową Riemanna** nazywamy:
   $$S(f, \Pi, \xi) = \sum_{i=1}^n \sum_{j=1}^m f(\xi_i, \eta_j) \Delta S_{ij}$$

#### Definicja 21.2 (Całka podwójna Riemanna)
Jeżeli dla każdego normalnego ciągu podziałów $\Pi_k$ (takiego, że $\lim_{k\to\infty} \delta(\Pi_k) = 0$) i dowolnego wyboru punktów pośrednich suma całkowa dąży do skończonej granicy $I$, to granicę tę nazywamy **całką podwójną Riemanna** funkcji $f$ po prostokącie $P$ i oznaczamy:
$$\iint_P f(x, y)\,dx\,dy = \lim_{\delta(\Pi) \to 0} \sum_{i=1}^n \sum_{j=1}^m f(\xi_i, \eta_j) \Delta S_{ij}$$

> **Twierdzenie 21.1 (Całkowalność funkcji ciągłych):**  
> Każda funkcja ciągła na prostokącie domkniętym $P$ jest na nim całkowalna w sensie Riemanna.

---

### 21.2. Własności całki podwójnej

Niech funkcje $f, g: D \to \mathbb{R}$ będą całkowalne na ograniczonym obszarze mierzalnym $D \subset \mathbb{R}^2$.
1. **Liniowość:** Dla dowolnych $\alpha, \beta \in \mathbb{R}$:
   $$\iint_D \big( \alpha f(x, y) + \beta g(x, y) \big)\,dx\,dy = \alpha \iint_D f(x, y)\,dx\,dy + \beta \iint_D g(x, y)\,dx\,dy$$
2. **Addytywność względem obszaru:** Jeżeli obszar $D$ jest sumą dwóch obszarów niemających wspólnych punktów wewnętrznych ($D = D_1 \cup D_2$, $\operatorname{Int}(D_1) \cap \operatorname{Int}(D_2) = \emptyset$):
   $$\iint_D f(x, y)\,dx\,dy = \iint_{D_1} f(x, y)\,dx\,dy + \iint_{D_2} f(x, y)\,dx\,dy$$
3. **Monotoniczność:** Jeżeli $f(x, y) \le g(x, y)$ dla każdego $(x, y) \in D$, to:
   $$\iint_D f(x, y)\,dx\,dy \le \iint_D g(x, y)\,dx\,dy$$
4. **Nierówność modułowa:**
   $$\left| \iint_D f(x, y)\,dx\,dy \right| \le \iint_D |f(x, y)|\,dx\,dy$$
5. **Twierdzenie o wartości średniej:** Jeżeli funkcja $f$ jest ciągła na obszarze domkniętym, ograniczonym i spójnym $D$ o polu $|D|$, to istnieje punkt $(\xi, \eta) \in D$ taki, że:
   $$\iint_D f(x, y)\,dx\,dy = f(\xi, \eta) \cdot |D|$$
   Wielkość $\mu = \frac{1}{|D|} \iint_D f(x, y)\,dx\,dy$ jest **wartością średnią dwuwymiarową** funkcji na obszarze $D$.

---

### 21.3. Twierdzenie Fubiniego i obliczanie całek podwójnych

Podstawowym narzędziem sprowadzającym całkę podwójną do zwykłych całek pojedynczych jest **twierdzenie Fubiniego o zamianie na całki iterowane**.

#### Definicja 21.3 (Obszary normalne na płaszczyźnie)
1. Obszar $D \subset \mathbb{R}^2$ nazywamy **normalnym względem osi $OX$**, jeżeli można go opisać nierównościami:
   $$D = \{ (x, y) \in \mathbb{R}^2 : a \le x \le b, \quad g_1(x) \le y \le g_2(x) \}$$
   gdzie funkcje $g_1, g_2: [a, b] \to \mathbb{R}$ są ciągłe oraz $g_1(x) \le g_2(x)$.
2. Obszar $D \subset \mathbb{R}^2$ nazywamy **normalnym względem osi $OY$**, jeżeli:
   $$D = \{ (x, y) \in \mathbb{R}^2 : c \le y \le d, \quad h_1(y) \le x \le h_2(y) \}$$
   gdzie funkcje $h_1, h_2: [c, d] \to \mathbb{R}$ są ciągłe oraz $h_1(y) \le h_2(y)$.

> **Twierdzenie 21.2 (Fubiniego dla obszarów normalnych):**  
> 1. Jeżeli $f$ jest funkcją ciągłą na obszarze normalnym względem osi $OX$, to:
>    $$\iint_D f(x, y)\,dx\,dy = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy \right) dx$$
> 2. Jeżeli $f$ jest ciągła na obszarze normalnym względem osi $OY$, to:
>    $$\iint_D f(x, y)\,dx\,dy = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx \right) dy$$

W przypadku prostokąta $P = [a, b] \times [c, d]$ kolejność całkowania jest dowolna:
$$\iint_P f(x, y)\,dx\,dy = \int_a^b \left( \int_c^d f(x, y)\,dy \right) dx = \int_c^d \left( \int_a^b f(x, y)\,dx \right) dy$$
Ponadto, gdy funkcja ma postać rozdzieloną $f(x, y) = \varphi(x) \cdot \psi(y)$:
$$\iint_P \varphi(x)\psi(y)\,dx\,dy = \left( \int_a^b \varphi(x)\,dx \right) \cdot \left( \int_c^d \psi(y)\,dy \right)$$

---

### 21.4. Zamiana zmiennych w całce podwójnej

Rozważmy przekształcenie dyfeomorficzne $\Phi: \Delta \to D$ płaszczyzny $(u, v)$ na płaszczyznę $(x, y)$:
$$x = x(u, v), \quad y = y(u, v)$$
gdzie funkcje $x(u, v), y(u, v)$ są klasy $C^1$ na obszarze $\Delta \subset \mathbb{R}^2$.

#### Definicja 21.4 (Jakobian przekształcenia)
**Jakobianem (wyznacznikiem Jacobiego)** przekształcenia $\Phi$ nazywamy wyznacznik macierzy pochodnych cząstkowych:
$$J = \frac{\partial(x, y)}{\partial(u, v)} = \det \begin{bmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{bmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}$$
Geometrycznie moduł jakobianu $|J|$ określa lokalny współczynnik skalowania elementarnego pola powierzchni: $dx\,dy = |J|\,du\,dv$.

> **Twierdzenie 21.3 (O zamianie zmiennych w całce podwójnej):**  
> Jeżeli przekształcenie $\Phi$ jest różnowartościowe wewnątrz obszaru $\Delta$ oraz jakobian $J \neq 0$, to dla dowolnej funkcji ciągłej $f$ na $D$:
> $$\iint_D f(x, y)\,dx\,dy = \iint_\Delta f\big(x(u, v), y(u, v)\big) \cdot |J|\,du\,dv$$

#### Współrzędne biegunowe:
Związki transformacyjne:
$$x = r \cos \varphi, \quad y = r \sin \varphi \quad (r \ge 0, \; \varphi \in [0, 2\pi) \text{ lub } [-\pi, \pi])$$
Obliczenie jakobianu:
$$J = \det \begin{bmatrix} \cos \varphi & -r \sin \varphi \\ \sin \varphi & r \cos \varphi \end{bmatrix} = r \cos^2 \varphi - (-r \sin^2 \varphi) = r(\cos^2 \varphi + \sin^2 \varphi) = r$$
Ponieważ $r \ge 0$, mamy $|J| = r$.  
Element pola we współrzędnych biegunowych:
$$dx\,dy = r\,dr\,d\varphi$$
Wzór na zamianę zmiennych:
$$\iint_D f(x, y)\,dx\,dy = \iint_\Delta f(r\cos\varphi, r\sin\varphi) \cdot r\,dr\,d\varphi$$

---

### 21.5. Zastosowania geometryczne i fizyczne całek podwójnych

1. **Pole obszaru płaskiego $D$:**
   $$|D| = \iint_D 1\,dx\,dy$$
2. **Objętość bryły $V$:**  
   Bryła ograniczona od góry powierzchnią $z = f(x, y) \ge 0$ i od dołu płaszczyzną $z = 0$ nad obszarem $D$:
   $$|V| = \iint_D f(x, y)\,dx\,dy$$
   Gdy bryła zawarta jest między dwoma powierzchniami $z_1(x, y) \le z \le z_2(x, y)$:
   $$|V| = \iint_D \big( z_2(x, y) - z_1(x, y) \big)\,dx\,dy$$
3. **Pole płata powierzchniowego:**  
   Pole powierzchni płata $z = f(x, y)$ nad obszarem $D$, gdzie $f \in C^1$:
   $$|S| = \iint_D \sqrt{1 + \left( \frac{\partial f}{\partial x} \right)^2 + \left( \frac{\partial f}{\partial y} \right)^2}\,dx\,dy$$
4. **Masa i ładunek powierzchniowy:**  
   Dla płytki o gęstości powierzchniowej masy lub ładunku $\sigma(x, y)$:
   $$M = \iint_D \sigma(x, y)\,dx\,dy, \quad Q = \iint_D \sigma(x, y)\,dx\,dy$$
5. **Środek ciężkości (środek masy):**
   $$x_C = \frac{1}{M} \iint_D x \cdot \sigma(x, y)\,dx\,dy, \quad y_C = \frac{1}{M} \iint_D y \cdot \sigma(x, y)\,dx\,dy$$
6. **Momenty bezwładności:**
   - Względem osi $OX$: $I_x = \iint_D y^2 \sigma(x, y)\,dx\,dy$,
   - Względem osi $OY$: $I_y = \iint_D x^2 \sigma(x, y)\,dx\,dy$,
   - Biegunowy moment bezwładności względem początku układu:
     $$I_0 = \iint_D (x^2 + y^2)\sigma(x, y)\,dx\,dy = I_x + I_y$$

---

## Rozdział 22: Całka potrójna i całki niewłaściwe wielokrotne

### 22.1. Całka potrójna Riemanna i twierdzenie Fubiniego

Rozważmy ograniczoną bryłę przestrzenną $V \subset \mathbb{R}^3$ oraz funkcję ciągłą $f: V \to \mathbb{R}$.

#### Definicja 22.1 (Całka potrójna)
Dzieląc obszar $V$ siatką prostopadłościanów o objętościach $\Delta V_{ijk} = \Delta x_i \Delta y_j \Delta z_k$:
$$\iiint_V f(x, y, z)\,dx\,dy\,dz = \lim_{\delta(\Pi)\to 0} \sum_{i, j, k} f(\xi_i, \eta_j, \zeta_k) \Delta V_{ijk}$$

#### Twierdzenie Fubiniego dla obszaru normalnego w przestrzeni:
Jeżeli bryła $V$ ma postać:
$$V = \{ (x, y, z) \in \mathbb{R}^3 : (x, y) \in D, \quad z_1(x, y) \le z \le z_2(x, y) \}$$
gdzie $D$ jest rzutem bryły na płaszczyznę $OXY$, to:
$$\iiint_V f(x, y, z)\,dx\,dy\,dz = \iint_D \left( \int_{z_1(x, y)}^{z_2(x, y)} f(x, y, z)\,dz \right) dx\,dy$$

---

### 22.2. Układy współrzędnych krzywoliniowych w $\mathbb{R}^3$

#### 1. Współrzędne walcowe (cylindryczne):
Transformacja:
$$x = r \cos \varphi, \quad y = r \sin \varphi, \quad z = z$$
gdzie $r \ge 0$, $\varphi \in [0, 2\pi)$, $z \in \mathbb{R}$.
Jakobian przekształcenia:
$$J = \det \begin{bmatrix}
\cos \varphi & -r \sin \varphi & 0 \\
\sin \varphi & r \cos \varphi & 0 \\
0 & 0 & 1
\end{bmatrix} = 1 \cdot (r \cos^2 \varphi + r \sin^2 \varphi) = r$$
Stąd element objętości:
$$dV = dx\,dy\,dz = r\,dr\,d\varphi\,dz$$
Współrzędne walcowe stosujemy zawsze w układach posiadających **symetrię osiową** (przewodniki walcowe, falowody kołowe, cewki cylindryczne).

#### 2. Współrzędne sferyczne (kuliste):
Transformacja:
$$x = r \sin \theta \cos \varphi, \quad y = r \sin \theta \sin \varphi, \quad z = r \cos \theta$$
gdzie:
- $r \ge 0$ – promień wodzący (odległość od początku układu),
- $\theta \in [0, \pi]$ – kąt zenitalny (odchylenie od dodatniej półosi $OZ$),
- $\varphi \in [0, 2\pi)$ – kąt azymutalny na płaszczyźnie $OXY$.

Obliczenie jakobianu:
$$J = \det \begin{bmatrix}
\sin \theta \cos \varphi & r \cos \theta \cos \varphi & -r \sin \theta \sin \varphi \\
\sin \theta \sin \varphi & r \cos \theta \sin \varphi & r \sin \theta \cos \varphi \\
\cos \theta & -r \sin \theta & 0
\end{bmatrix} = r^2 \sin \theta$$
Ponieważ $\theta \in [0, \pi]$, $\sin \theta \ge 0$, więc $|J| = r^2 \sin \theta$.  
Element objętości:
$$dV = dx\,dy\,dz = r^2 \sin \theta\,dr\,d\theta\,d\varphi$$
Współrzędne sferyczne są podstawowym aparatem w zagadnieniach o **symetrii środkowej/kulistej** (potencjał elektrostatyczny ładunku punktowego, promieniowanie anten izotropowych).

---

### 22.3. Zastosowania fizyczne całek potrójnych w teorii pola

1. **Całkowity ładunek elektrostatyczny:**  
   Jeżeli w przestrzeni $V$ występuje ciągły rozkład ładunku o gęstości objętościowej $\rho(x, y, z)$ [$\text{C}/\text{m}^3$]:
   $$Q = \iiint_V \rho(x, y, z)\,dx\,dy\,dz$$
2. **Potencjał elektrostatyczny:**  
   Potencjał wywołany przez ładunek rozproszony w bryle $V$ w punkcie obserwacji $P(x_0, y_0, z_0)$ poza obszarem ładunku:
   $$V(P) = \frac{1}{4\pi \varepsilon_0} \iiint_V \frac{\rho(x, y, z)}{\sqrt{(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2}}\,dx\,dy\,dz$$
3. **Energia własna pola elektrostatycznego:**  
   Gęstość energii pola elektrycznego o natężeniu $\vec{E}$ w dielektryku o przenikalności $\varepsilon$:
   $$w_e = \frac{1}{2} \varepsilon \|\vec{E}\|^2 \implies W_e = \iiint_{\mathbb{R}^3} w_e\,dV = \frac{1}{2} \varepsilon \iiint_{\mathbb{R}^3} \|\vec{E}(x, y, z)\|^2\,dx\,dy\,dz$$

---

### 22.4. Całka Poissona-Gaussa i szumy losowe w telekomunikacji

Jednym z najbardziej fundamentalnych rezultatów analizy matematycznej wykorzystującym całkę podwójną jest wyznaczenie wartości całki Poissona-Gaussa:
$$I = \int_{-\infty}^\infty e^{-x^2}\,dx$$
Funkcja podcałkowa $e^{-x^2}$ nie posiada funkcji pierwotnej wyrażalnej przez funkcje elementarne (twierdzenie Liouville'a), jednak jej całka oznaczona po całej prostej może zostać obliczona ściśle.

> **Twierdzenie 22.1 (Całka Gaussa):**  
> $$\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}$$

**Dowód:**  
Rozważmy kwadrat całki $I$:
$$I^2 = \left( \int_{-\infty}^\infty e^{-x^2}\,dx \right) \cdot \left( \int_{-\infty}^\infty e^{-y^2}\,dy \right)$$
Korzystając z twierdzenia Fubiniego, iloczyn całek pojedynczych możemy zapisać jako całkę podwójną po całej płaszczyźnie $\mathbb{R}^2$:
$$I^2 = \iint_{\mathbb{R}^2} e^{-x^2} e^{-y^2}\,dx\,dy = \iint_{\mathbb{R}^2} e^{-(x^2 + y^2)}\,dx\,dy$$
Wprowadzamy współrzędne biegunowe: $x = r \cos \varphi$, $y = r \sin \varphi$, gdzie $r \in [0, \infty)$ oraz $\varphi \in [0, 2\pi)$. Jakobian wynosi $J = r$. Obszar całkowania przekształca się w $\Delta = [0, \infty) \times [0, 2\pi)$:
$$I^2 = \int_0^{2\pi} \left( \int_0^\infty e^{-r^2} \cdot r\,dr \right) d\varphi = \left( \int_0^{2\pi} d\varphi \right) \cdot \left( \int_0^\infty r e^{-r^2}\,dr \right)$$
Całka kątowa wynosi $2\pi$. W całce promieniowej stosujemy podstawienie $t = r^2$, skąd $dt = 2r\,dr \implies r\,dr = \frac{1}{2} dt$:
$$\int_0^\infty r e^{-r^2}\,dr = \frac{1}{2} \int_0^\infty e^{-t}\,dt = \frac{1}{2} \left[ -e^{-t} \right]_0^\infty = \frac{1}{2} (0 - (-1)) = \frac{1}{2}$$
Mnożąc oba rezultaty:
$$I^2 = 2\pi \cdot \frac{1}{2} = \pi \implies I = \sqrt{\pi} \quad \blacksquare$$

#### Zastosowanie w teorii sygnałów i telekomunikacji:
W odbiornikach radiowych i systemach teleinformatycznych fundamentalnym ograniczeniem jest **termiczny szum gaussowski (szum Johnsona-Nyquista)**. Rozkład prawdopodobieństwa napięcia szumu $U$ opisuje gęstość prawdopodobieństwa Gaussa:
$$f_U(u) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(u - m)^2}{2\sigma^2}}$$
Z twierdzenia Gaussa wynika natychmiast warunek normalizacji prawdopodobieństwa:
$$\int_{-\infty}^\infty f_U(u)\,du = \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^\infty e^{-\frac{(u - m)^2}{2\sigma^2}}\,du = 1$$
co po podstawieniu $x = \frac{u-m}{\sigma \sqrt{2}}$ redukuje się do $\frac{1}{\sqrt{\pi}} \int_{-\infty}^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{\sqrt{\pi}} = 1$.

---

### 22.5. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 22.1 (Zmiana kolejności całkowania w całce iterowanej)
Zmienić kolejność całkowania w całce:
$$I = \int_0^1 dx \int_{x^2}^{\sqrt{x}} f(x, y)\,dy$$

**Rozwiązanie:**  
1. **Analiza obszaru $D$:**  
   Obszar jest zadany nierównościami:
   $$0 \le x \le 1, \quad x^2 \le y \le \sqrt{x}$$
   Dolna krawędź to parabola $y = x^2$, górna to gałąź paraboli $y = \sqrt{x}$ (czyli $x = y^2$).
   Punkty przecięcia krzywych: $x^2 = \sqrt{x} \implies x^4 = x \implies x(x^3 - 1) = 0 \implies x = 0$ oraz $x = 1$.
   Zakres zmiennej $y$: od $y_{\min} = 0$ do $y_{\max} = 1$.

2. **Opis obszaru jako normalnego względem osi $OY$:**  
   Dla ustalonego $y \in [0, 1]$:
   - lewa granica: $y = \sqrt{x} \implies x = y^2$,
   - prawa granica: $y = x^2 \implies x = \sqrt{y}$.
   Zatem:
   $$0 \le y \le 1, \quad y^2 \le x \le \sqrt{y}$$

3. **Zapis całki po zamianie kolejności:**
   $$I = \int_0^1 dy \int_{y^2}^{\sqrt{y}} f(x, y)\,dx$$

---

#### Przykład 22.2 (Całka podwójna we współrzędnych biegunowych)
Obliczyć całkę podwójną:
$$\iint_D (x^2 + y^2)\,dx\,dy$$
gdzie $D$ jest obszarem w I ćwiartce ograniczonym okręgami $x^2 + y^2 = 1$, $x^2 + y^2 = 4$ oraz prostymi $y = 0$ i $y = x$.

**Rozwiązanie:**  
1. **Przejście na współrzędne biegunowe:**  
   $x = r \cos \varphi$, $y = r \sin \varphi$, $x^2 + y^2 = r^2$, jakobian $J = r$.
2. **Wyznaczenie granic całkowania:**  
   - Okręgi mają promienie $R_1 = 1$ oraz $R_2 = 2 \implies 1 \le r \le 2$.
   - Prosta $y = 0$ to oś $OX$ ($\varphi = 0$).
   - Prosta $y = x$ ma kąt nachylenia $\operatorname{tg} \varphi = 1 \implies \varphi = \frac{\pi}{4}$.
   Obszar transformowany: $\Delta = [1, 2] \times [0, \pi/4]$.

3. **Obliczenie całki:**
   $$\iint_D (x^2 + y^2)\,dx\,dy = \int_0^{\pi/4} d\varphi \int_1^2 r^2 \cdot r\,dr = \left( \int_0^{\pi/4} d\varphi \right) \cdot \left( \int_1^2 r^3\,dr \right)$$
   $$\int_0^{\pi/4} d\varphi = \frac{\pi}{4}$$
   $$\int_1^2 r^3\,dr = \left[ \frac{r^4}{4} \right]_1^2 = \frac{2^4 - 1^4}{4} = \frac{16 - 1}{4} = \frac{15}{4}$$
   Wynik:
   $$\iint_D (x^2 + y^2)\,dx\,dy = \frac{\pi}{4} \cdot \frac{15}{4} = \frac{15\pi}{16}$$

---

#### Przykład 22.3 (Objętość bryły we współrzędnych walcowych)
Obliczyć objętość bryły ograniczonej od dołu paraboloidą $z = x^2 + y^2$, a od góry płaszczyzną $z = 4$.

**Rozwiązanie:**  
1. **Przecięcie powierzchni:**  
   $x^2 + y^2 = 4$ – okrąg o promieniu $R = 2$ na wysokości $z = 4$.
   Rzut bryły na płaszczyznę $OXY$ to koło $D = \{ (x, y) \in \mathbb{R}^2 : x^2 + y^2 \le 4 \}$.
   W każdym punkcie koła $D$ wysokość bryły wynosi: $z_1 = x^2 + y^2 \le z \le z_2 = 4$.

2. **Współrzędne walcowe:**  
   $x = r \cos \varphi$, $y = r \sin \varphi$, $z = z$, $dV = r\,dr\,d\varphi\,dz$.
   Granice: $\varphi \in [0, 2\pi]$, $r \in [0, 2]$, $z \in [r^2, 4]$.

3. **Całkowanie:**
   $$|V| = \int_0^{2\pi} d\varphi \int_0^2 r\,dr \int_{r^2}^4 dz = 2\pi \int_0^2 r (4 - r^2)\,dr = 2\pi \int_0^2 (4r - r^3)\,dr$$
   $$= 2\pi \left[ 2r^2 - \frac{r^4}{4} \right]_0^2 = 2\pi \left( 2(4) - \frac{16}{4} \right) = 2\pi (8 - 4) = 8\pi$$

---

#### Przykład 22.4 (Ładunek elektrostatyczny we współrzędnych sferycznych)
W kuli o promieniu $R$ gęstość objętościowa ładunku elektrycznego zależy od odległości od środka:
$$\rho(r) = \rho_0 \left( 1 - \frac{r^2}{R^2} \right) \quad (\rho_0 > 0)$$
Wyznaczyć całkowity ładunek $Q$ zgromadzony w kuli.

**Rozwiązanie:**  
Stosujemy współrzędne sferyczne ($r, \theta, \varphi$):
$$Q = \iiint_K \rho(r)\,dV = \int_0^{2\pi} d\varphi \int_0^\pi \sin \theta\,d\theta \int_0^R \rho_0 \left( 1 - \frac{r^2}{R^2} \right) r^2\,dr$$
1. Całka po kącie azymutalnym: $\int_0^{2\pi} d\varphi = 2\pi$.
2. Całka po kącie zenitalnym: $\int_0^\pi \sin \theta\,d\theta = [-\cos \theta]_0^\pi = -(-1) - (-1) = 2$.  
   Iloczyn kątowy to pełny kąt bryłowy kuli: $\Omega = 2\pi \cdot 2 = 4\pi$ steradianów.
3. Całka radialna:
   $$\int_0^R \left( r^2 - \frac{r^4}{R^2} \right) dr = \left[ \frac{r^3}{3} - \frac{r^5}{5R^2} \right]_0^R = \frac{R^3}{3} - \frac{R^3}{5} = R^3 \left( \frac{5 - 3}{15} \right) = \frac{2}{15} R^3$$
Ładunek całkowity:
$$Q = 4\pi \rho_0 \cdot \frac{2}{15} R^3 = \frac{8\pi}{15} \rho_0 R^3$$

---

### 22.6. Zadania do samodzielnego rozwiązania

1. **Zadanie 22.1:** Obliczyć całkę podwójną $\iint_D x y\,dx\,dy$, gdzie $D$ jest trójkątem o wierzchołkach $A(0, 0)$, $B(2, 0)$, $C(0, 2)$.  
   *Odpowiedź:* $\int_0^2 dx \int_0^{2-x} xy\,dy = \frac{2}{3}$.

2. **Zadanie 22.2:** Obliczyć pole obszaru ograniczonego kardioidą o równaniu we współrzędnych biegunowych $r = a(1 + \cos \varphi)$, gdzie $a > 0$.  
   *Odpowiedź:* $S = \frac{1}{2} \int_0^{2\pi} r^2\,d\varphi = \frac{1}{2} a^2 \int_0^{2\pi} (1 + 2\cos\varphi + \cos^2\varphi)\,d\varphi = \frac{3}{2}\pi a^2$.

3. **Zadanie 22.3:** Wyznaczyć masę stożka ściętego o promieniu dolnej podstawy $R_1$, górnej $R_2$ i wysokości $H$, jeżeli gęstość masy jest proporcjonalna do odległości od podstawy: $\rho(z) = k z$.  
   *Odpowiedź:* Całka we współrzędnych walcowych: $M = \frac{\pi k H^2}{12}(R_1^2 + 2 R_1 R_2 + 3 R_2^2)$.

4. **Zadanie 22.4:** Obliczyć moment bezwładności jednorodnej kuli o promieniu $R$ i stałej gęstości $\rho_0$ względem jej osi symetrii $OZ$.  
   *Odpowiedź:* $I_z = \iiint_K (x^2 + y^2)\rho_0\,dV$. We współrzędnych sferycznych $x^2 + y^2 = r^2 \sin^2 \theta$. $I_z = \frac{2}{5} M R^2$, gdzie $M = \frac{4}{3}\pi R^3 \rho_0$.

5. **Zadanie 22.5:** Wykazać, że dla $\alpha > 0$:  
   $$\int_{-\infty}^\infty e^{-\alpha x^2}\,dx = \sqrt{\frac{\pi}{\alpha}}$$
   oraz obliczyć całkę momentową $\int_{-\infty}^\infty x^2 e^{-\alpha x^2}\,dx$ przez różniczkowanie po parametrze $\alpha$.  
   *Odpowiedź:* Różniczkując tożsamość $\int_{-\infty}^\infty e^{-\alpha x^2}dx = \pi^{1/2} \alpha^{-1/2}$ po $\alpha$: $-\int_{-\infty}^\infty x^2 e^{-\alpha x^2} dx = -\frac{1}{2}\pi^{1/2}\alpha^{-3/2} \implies \frac{1}{2\alpha}\sqrt{\frac{\pi}{\alpha}}$.
