# Część VII: Całka Oznaczona i Całki Niewłaściwe

Całka oznaczona Riemanna stanowi formalną matematyczną realizację procesu sumowania nieskończonej liczby nieskończenie małych wielkości. Łączy pojęcie pola pod wykresem funkcji z funkcją pierwotną poprzez Podstawowe Twierdzenie Rachunku Całkowego (wzór Newtona-Leibniza). W elektrotechnice całka oznaczona jest podstawą definiowania wartości średniej i skutecznej (RMS) przebiegów okresowych, obliczania energii pobieranej przez odbiorniki nieliniowe, bilansu cieplnego elementów półprzewodnikowych oraz wyznaczania odpowiedzi układów w dziedzinie częstotliwości za pomocą całek niewłaściwych (transformata Fouriera i Laplace'a).

---

## Rozdział 14: Całka oznaczona Riemanna

### 14.1. Konstrukcja Riemanna i Darboux

Niech funkcja $f: [a, b] \to \mathbb{R}$ będzie ograniczona na przedziale domkniętym $[a, b]$ ($a < b$).

#### Definicja 14.1 (Podział przedziału i sumy całkowe)
1. **Podziałem** $\Pi$ przedziału $[a, b]$ nazywamy skończony zbiór punktów:
   $$\Pi: a = x_0 < x_1 < x_2 < \dots < x_n = b$$
   dzielący $[a, b]$ na $n$ podprzedziałów $[x_{i-1}, x_i]$ o długościach $\Delta x_i = x_i - x_{i-1}$.
2. **Średnicą podziału** nazywamy:
   $$\delta(\Pi) = \max_{1 \le i \le n} \Delta x_i$$
3. Wybierając w każdym podprzedziale punkt pośredni $\xi_i \in [x_{i-1}, x_i]$, tworzymy **sumę całkową Riemanna**:
   $$S(f, \Pi, \xi) = \sum_{i=1}^n f(\xi_i) \Delta x_i$$
4. Oznaczmy kresy funkcji na podprzedziale: $m_i = \inf_{x \in [x_{i-1}, x_i]} f(x)$, $M_i = \sup_{x \in [x_{i-1}, x_i]} f(x)$.
   - **Dolną sumą Darboux** nazywamy: $s(f, \Pi) = \sum_{i=1}^n m_i \Delta x_i$,
   - **Górną sumą Darboux** nazywamy: $S(f, \Pi) = \sum_{i=1}^n M_i \Delta x_i$.

Dla dowolnego podziału i wyboru punktów pośrednich: $s(f, \Pi) \le S(f, \Pi, \xi) \le S(f, \Pi)$.

#### Definicja 14.2 (Całka oznaczona Riemanna)
Mówimy, że funkcja $f$ jest **całkowalna w sensie Riemanna** na $[a, b]$ (co zapisujemy $f \in \mathcal{R}([a, b])$), jeżeli istnieje skończona liczba $I \in \mathbb{R}$ taka, że dla każdego normalnego ciągu podziałów ($\lim_{k\to\infty} \delta(\Pi_k) = 0$) i dowolnego doboru punktów pośrednich $\xi$:
$$\lim_{k \to \infty} S(f, \Pi_k, \xi) = I = \int_a^b f(x)\,dx$$

> **Twierdzenie 14.1 (Kryterium całkowalności Darboux):**  
> Funkcja ograniczona $f$ jest całkowalna w sensie Riemanna na $[a, b]$ wtedy i tylko wtedy, gdy:
> $$\lim_{\delta(\Pi) \to 0} \big( S(f, \Pi) - s(f, \Pi) \big) = 0$$

> **Twierdzenie 14.2 (Klasy funkcji całkowalnych):**  
> Następujące klasy funkcji są całkowalne w sensie Riemanna na $[a, b]$:
> 1. Każda funkcja **ciągła** na $[a, b]$.
> 2. Każda funkcja **monotoniczna** na $[a, b]$.
> 3. Każda funkcja ograniczona mająca **co najwyżej przeliczalną liczbę punktów nieciągłości** (w szczególności funkcje kawałkami ciągłe z nieciągłościami skokowymi).

---

### 14.2. Własności całki oznaczonej

Niech $f, g \in \mathcal{R}([a, b])$:
1. **Liniowość:** $\int_a^b \big( \alpha f(x) + \beta g(x) \big)\,dx = \alpha \int_a^b f(x)\,dx + \beta \int_a^b g(x)\,dx$.
2. **Addytywność względem przedziału:** Dla dowolnego $c \in (a, b)$:
   $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$
3. **Monotoniczność:** Jeżeli $f(x) \le g(x)$ na $[a, b]$, to $\int_a^b f(x)\,dx \le \int_a^b g(x)\,dx$.
4. **Nierówność modułowa:** $\left| \int_a^b f(x)\,dx \right| \le \int_a^b |f(x)|\,dx$.
5. **Twierdzenie o wartości średniej:** Jeżeli $f$ jest ciągła na $[a, b]$, to istnieje punkt $c \in [a, b]$ taki, że:
   $$\int_a^b f(x)\,dx = f(c)(b - a) \iff f(c) = \frac{1}{b - a} \int_a^b f(x)\,dx$$
   Liczbę $\mu = \frac{1}{b-a}\int_a^b f(x)\,dx$ nazywamy **wartością średnią funkcji** na przedziale $[a, b]$.

---

### 14.3. Podstawowe Twierdzenie Rachunku Całkowego (Wzór Newtona-Leibniza)

Rozważmy funkcję górnej granicy całkowania dla funkcji ciągłej $f$:
$$\Phi(x) = \int_a^x f(t)\,dt, \quad x \in [a, b]$$

> **Twierdzenie 14.3 (Różniczkowalność całki względem górnej granicy):**  
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$, to funkcja $\Phi(x)$ jest różniczkowalna na $[a, b]$ oraz:
> $$\Phi'(x) = \frac{d}{dx} \left( \int_a^x f(t)\,dt \right) = f(x)$$
> Oznacza to, że każda funkcja ciągła posiada funkcję pierwotną!

**Dowód:**  
Z definicji pochodnej i addytywności całki:
$$\frac{\Phi(x + h) - \Phi(x)}{h} = \frac{1}{h} \left( \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt \right) = \frac{1}{h} \int_x^{x+h} f(t)\,dt$$
Z twierdzenia o wartości średniej dla całek istnieje punkt $c_h$ leżący między $x$ a $x+h$ taki, że:
$$\frac{1}{h} \int_x^{x+h} f(t)\,dt = \frac{1}{h} \cdot f(c_h) \cdot h = f(c_h)$$
Gdy $h \to 0$, to $c_h \to x$. Z ciągłości funkcji $f$: $\lim_{h \to 0} f(c_h) = f(x)$.  
Zatem $\Phi'(x) = f(x)$. $\blacksquare$

> **Twierdzenie 14.4 (Wzór Newtona-Leibniza):**  
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$, a $F$ jest jej dowolną funkcją pierwotną ($F' = f$), to:
> $$\int_a^b f(x)\,dx = F(b) - F(a) = [F(x)]_a^b$$

**Dowód:**  
Ponieważ $\Phi(x) = \int_a^x f(t)\,dt$ jest funkcją pierwotną $f(x)$, to z Twierdzenia 12.1 dowolna inna funkcja pierwotna $F(x)$ różni się od $\Phi(x)$ o stałą $C$:
$$F(x) = \Phi(x) + C = \int_a^x f(t)\,dt + C$$
Wstawiając $x = a$: $F(a) = \int_a^a f(t)\,dt + C = 0 + C = C$.  
Wstawiając $x = b$: $F(b) = \int_a^b f(t)\,dt + F(a) \implies \int_a^b f(t)\,dt = F(b) - F(a)$. $\blacksquare$

#### Całkowanie przez części i przez podstawienie w całce oznaczonej:
1. **Przez części:**
   $$\int_a^b u(x) v'(x)\,dx = [u(x) v(x)]_a^b - \int_a^b u'(x) v(x)\,dx$$
2. **Przez podstawienie (zamiana granic):**
   $$\int_a^b f(\varphi(x)) \varphi'(x)\,dx = \int_{\varphi(a)}^{\varphi(b)} f(t)\,dt$$

---

## Rozdział 15: Zastosowania geometryczne i inżynierskie całki oznaczonej

### 15.1. Obliczanie wielkości geometrycznych

1. **Pole obszaru płaskiego:**  
   - We współrzędnych kartezjańskich: $S = \int_a^b [f_2(x) - f_1(x)]\,dx$.
   - W postaci parametrycznej ($x = x(t), y = y(t), t \in [\alpha, \beta]$):
     $$S = \int_\alpha^\beta y(t) x'(t)\,dt$$
   - We współrzędnych biegunowych ($r = r(\varphi), \varphi \in [\alpha, \beta]$):
     $$S = \frac{1}{2} \int_\alpha^\beta r^2(\varphi)\,d\varphi$$

2. **Długość łuku krzywej:**  
   - Postać jawna $y = f(x)$: $L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$.
   - Postać parametryczna: $L = \int_\alpha^\beta \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt$.
   - Postać biegunowa: $L = \int_\alpha^\beta \sqrt{r^2(\varphi) + [r'(\varphi)]^2}\,d\varphi$.

3. **Objętość bryły obrotowej:**  
   - Obrót wokół osi $OX$: $V_x = \pi \int_a^b [f(x)]^2\,dx$.
   - Obrót wokół osi $OY$ (metoda powłok walcowych): $V_y = 2\pi \int_a^b x f(x)\,dx$.

4. **Pole powierzchni bryły obrotowej:**  
   - Obrót wokół osi $OX$: $P_x = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2}\,dx$.

---

### 15.2. Zastosowania w elektronice i teorii sygnałów

#### 1. Wartość średnia i skuteczna (RMS) sygnałów okresowych:
Dla sygnału okresowego $u(t)$ o okresie $T$:
- **Wartość średnia:**
  $$U_{\text{śr}} = \frac{1}{T} \int_0^T u(t)\,dt$$
- **Wartość skuteczna (RMS – Root Mean Square):**
  $$U_{\text{RMS}} = \sqrt{\frac{1}{T} \int_0^T u^2(t)\,dt}$$
Wartość skuteczna odpowiada wartości stałego napięcia, które na rezystorze $R$ wydzieliłoby w czasie okresu $T$ taką samą ilość ciepła (energię Joula) co analizowany sygnał zmienny:
$$W = \int_0^T \frac{u^2(t)}{R}\,dt = \frac{U_{\text{RMS}}^2}{R} T$$

#### Kanoniczne sygnały w elektronice:
1. **Sygnał sinusoidalny $u(t) = U_m \sin(\omega t)$:**
   $$U_{\text{RMS}} = \sqrt{\frac{1}{T} \int_0^T U_m^2 \sin^2(\omega t)\,dt} = U_m \sqrt{\frac{1}{T} \int_0^T \frac{1 - \cos(2\omega t)}{2}\,dt} = \frac{U_m}{\sqrt{2}} \approx 0{,}707 U_m$$
2. **Sygnał trójkątny symetryczny o amplitudzie $U_m$:**
   $$U_{\text{RMS}} = \frac{U_m}{\sqrt{3}} \approx 0{,}577 U_m$$
3. **Sygnał prostokątny o wypełnieniu 50% i amplitudzie $\pm U_m$:**
   $$U_{\text{RMS}} = U_m$$

---

## Rozdział 16: Całki niewłaściwe

### 16.1. Całki niewłaściwe I i II rodzaju

#### 1. Całki niewłaściwe I rodzaju (przedział nieograniczony):
$$\int_a^\infty f(x)\,dx = \lim_{B \to \infty} \int_a^B f(x)\,dx$$
$$\int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^\infty f(x)\,dx \quad (c \in \mathbb{R})$$
Jeżeli granice są skończone, całkę nazywamy **zbieżną**, w przeciwnym razie – **rozbieżną**.

#### 2. Całki niewłaściwe II rodzaju (funkcja nieograniczona):
Jeżeli $f(x)$ dąży do $\pm\infty$ przy $x \to b^-$:
$$\int_a^b f(x)\,dx = \lim_{\varepsilon \to 0^+} \int_a^{b - \varepsilon} f(x)\,dx$$

> **Twierdzenie 16.1 (Całki wzorcowe):**  
> 1. $\int_1^\infty \frac{dx}{x^\alpha}$ jest **zbieżna dla $\alpha > 1$**, a rozbieżna dla $\alpha \le 1$.
> 2. $\int_0^1 \frac{dx}{x^\alpha}$ jest **zbieżna dla $\alpha < 1$**, a rozbieżna dla $\alpha \ge 1$.

---

### 16.2. Kryteria zbieżności i wartość główna Cauchy'ego

> **Twierdzenie 16.2 (Kryterium porównawcze i ilorazowe):**  
> Niech $0 \le f(x) \le g(x)$ dla $x \ge a$.
> - Jeżeli $\int_a^\infty g(x)\,dx$ jest zbieżna, to $\int_a^\infty f(x)\,dx$ jest zbieżna.
> - Jeżeli $\int_a^\infty f(x)\,dx$ jest rozbieżna, to $\int_a^\infty g(x)\,dx$ jest rozbieżna.
> - Jeżeli $\lim_{x \to \infty} \frac{f(x)}{g(x)} = k \in (0, \infty)$, to obie całki są jednocześnie zbieżne albo rozbieżne.

#### Wartość główna całki w sensie Cauchy'ego (v.p.):
Gdy całka $\int_{-\infty}^\infty f(x)\,dx$ jest rozbieżna w sensie klasycznym z powodu przeciwnych nieskończoności, jej wartość główną definiujemy jako granicę symetryczną:
$$\operatorname{v.p.} \int_{-\infty}^\infty f(x)\,dx = \lim_{R \to \infty} \int_{-R}^R f(x)\,dx$$
*Przykład:* $\int_{-\infty}^\infty x\,dx$ jest rozbieżna, lecz $\operatorname{v.p.}\int_{-\infty}^\infty x\,dx = \lim_{R\to\infty} \left[\frac{x^2}{2}\right]_{-R}^R = 0$.

---

### 16.3. Funkcje specjalne Eulera: Gamma i Beta

1. **Funkcja Gamma Eulera:**
   $$\Gamma(s) = \int_0^\infty t^{s-1} e^{-t}\,dt \quad (s > 0)$$
   Własności:
   - Wzór redukcyjny: $\Gamma(s + 1) = s \Gamma(s)$,
   - Dla liczb naturalnych: $\Gamma(n + 1) = n!$ (uogólnienie silni na liczby rzeczywiste i zespolone),
   - Wartość dla $s = 1/2$: $\Gamma(1/2) = \sqrt{\pi}$ (związana z całką Gaussa).

2. **Funkcja Beta Eulera:**
   $$\mathrm{B}(p, q) = \int_0^1 x^{p-1} (1 - x)^{q-1}\,dx = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p + q)} \quad (p, q > 0)$$

---

### 16.4. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 16.1 (Obliczanie pola pętli linii parametrycznej)
Obliczyć pole obszaru ograniczonego pętlą krzywej zadanej parametrycznie:
$$x(t) = 3t^2, \quad y(t) = 3t - t^3$$

**Rozwiązanie:**  
1. **Wyznaczenie punktu samoprzecięcia (pętli):**  
   Szukamy $t_1 \neq t_2$ takich, że $x(t_1) = x(t_2)$ i $y(t_1) = y(t_2)$.
   $$3t_1^2 = 3t_2^2 \implies t_1 = -t_2$$
   $$y(t_1) = 3t_1 - t_1^3 = y(-t_1) = -3t_1 + t_1^3 \implies 2(3t_1 - t_1^3) = 0 \implies t_1(3 - t_1^2) = 0$$
   Nietrywialne parametry pętli: $t = -\sqrt{3}$ do $t = +\sqrt{3}$.
2. **Wzór na pole w postaci parametrycznej:**  
   Z symetrii wykresu względem osi $OX$ ($x(t)$ jest parzysta, $y(t)$ nieparzysta):
   $$S = \int_{-\sqrt{3}}^{\sqrt{3}} y(t) x'(t)\,dt = 2 \int_0^{\sqrt{3}} (3t - t^3) \cdot 6t\,dt = 12 \int_0^{\sqrt{3}} (3t^2 - t^4)\,dt$$
   $$= 12 \left[ t^3 - \frac{t^5}{5} \right]_0^{\sqrt{3}} = 12 \left( 3\sqrt{3} - \frac{9\sqrt{3}}{5} \right) = 12 \cdot \frac{6\sqrt{3}}{5} = \frac{72\sqrt{3}}{5}$$

---

#### Przykład 16.2 (Długość łuku asteroidy)
Obliczyć długość całej asteroidy:
$$x(t) = a \cos^3 t, \quad y(t) = a \sin^3 t \quad (a > 0, \; t \in [0, 2\pi])$$

**Rozwiązanie:**  
Krzywa składa się z 4 symetrycznych łuków (w każdej ćwiartce dla $t \in [0, \pi/2]$).
Pochodne:
$$x'(t) = -3a \cos^2 t \sin t, \quad y'(t) = 3a \sin^2 t \cos t$$
Element łuku:
$$ds = \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt = \sqrt{9a^2 \cos^4 t \sin^2 t + 9a^2 \sin^4 t \cos^2 t}\,dt$$
$$= 3a \sqrt{\sin^2 t \cos^2 t (\cos^2 t + \sin^2 t)}\,dt = 3a |\sin t \cos t|\,dt$$
Dla $t \in [0, \pi/2]$ mamy $\sin t \cos t \ge 0$, więc:
$$L = 4 \int_0^{\pi/2} 3a \sin t \cos t\,dt = 12a \left[ \frac{\sin^2 t}{2} \right]_0^{\pi/2} = 12a \cdot \frac{1}{2} = 6a$$

---

#### Przykład 16.3 (Całka niewłaściwa I rodzaju)
Zbadać zbieżność i obliczyć całkę:
$$\int_0^\infty \frac{dx}{x^2 + 4x + 8}$$

**Rozwiązanie:**  
Mianownik: $x^2 + 4x + 8 = (x + 2)^2 + 4 = 4 \left[ \left(\frac{x+2}{2}\right)^2 + 1 \right]$.  
Funkcja pierwotna:
$$\int \frac{dx}{(x+2)^2 + 2^2} = \frac{1}{2} \operatorname{arctg}\left(\frac{x + 2}{2}\right) + C$$
Obliczamy granicę:
$$\int_0^\infty \frac{dx}{x^2 + 4x + 8} = \lim_{B \to \infty} \left[ \frac{1}{2} \operatorname{arctg}\left(\frac{x + 2}{2}\right) \right]_0^B = \frac{1}{2} \left( \lim_{B \to \infty} \operatorname{arctg}\left(\frac{B + 2}{2}\right) - \operatorname{arctg}\left(\frac{2}{2}\right) \right)$$
$$= \frac{1}{2} \left( \frac{\pi}{2} - \operatorname{arctg}(1) \right) = \frac{1}{2} \left( \frac{\pi}{2} - \frac{\pi}{4} \right) = \frac{1}{2} \cdot \frac{\pi}{4} = \frac{\pi}{8}$$

---

### 16.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 16.1:** Obliczyć całkę oznaczoną: $\int_0^1 x e^{-x}\,dx$.  
   *Odpowiedź:* $1 - \frac{2}{e}$.

2. **Zadanie 16.2:** Obliczyć objętość bryły powstałej przez obrót wokół osi $OX$ łuku sinusoidy $y = \sin x$ dla $x \in [0, \pi]$.  
   *Odpowiedź:* $V = \pi \int_0^\pi \sin^2 x\,dx = \frac{\pi^2}{2}$.

3. **Zadanie 16.3:** Wyznaczyć wartość skuteczną przebiegu $u(t) = U_m |\sin(\omega t)|$ (napięcie wyprostowane dwupołówkowo).  
   *Odpowiedź:* $U_{\text{RMS}} = \frac{U_m}{\sqrt{2}}$.

4. **Zadanie 16.4:** Zbadać zbieżność całki niewłaściwej: $\int_0^1 \frac{\ln x}{\sqrt{x}}\,dx$.  
   *Odpowiedź:* Całka jest zbieżna. Przez części: $[2\sqrt{x}\ln x]_0^1 - \int_0^1 2\sqrt{x}\frac{1}{x}dx = 0 - [4\sqrt{x}]_0^1 = -4$.

5. **Zadanie 16.5:** Korzystając z własności funkcji Gamma, obliczyć całkę $\int_0^\infty x^6 e^{-2x}\,dx$.  
   *Wskazówka:* Podstawienie $t = 2x$.  
   *Odpowiedź:* $\frac{\Gamma(7)}{2^7} = \frac{6!}{128} = \frac{720}{128} = \frac{45}{8}$.
