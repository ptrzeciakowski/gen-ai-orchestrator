# Wprowadzenie do rachunku całkowego: Całki pojedyncze

Rachunek całkowy jest jednym z fundamentalnych działów analizy matematycznej. Stanowi naturalne dopełnienie i operację odwrotną do różniczkowania, a jednocześnie potężne narzędzie do wyznaczania pól powierzchni, objętości, długości łuków oraz rozwiązywania zagadnień fizycznych i inżynierskich.

---

## 1. Całka nieoznaczona

### 1.1. Definicja funkcji pierwotnej
Niech funkcja $f(x)$ będzie określona w przedziale otwartym $(a, b)$. Funkcję $F(x)$ nazywamy **funkcją pierwotną** funkcji $f(x)$ w tym przedziale, jeżeli dla każdego $x \in (a, b)$ zachodzi:

$$F'(x) = f(x)$$

Jeżeli $F(x)$ jest funkcją pierwotną funkcji $f(x)$, to każda funkcja postaci $F(x) + C$ (gdzie $C \in \mathbb{R}$ jest dowolną stałą) również jest funkcją pierwotną $f(x)$, ponieważ:

$$\frac{d}{dx} \big( F(x) + C \big) = F'(x) + 0 = f(x)$$

### 1.2. Definicja całki nieoznaczonej
Zbiór wszystkich funkcji pierwotnych funkcji $f(x)$ nazywamy **całką nieoznaczoną** i zapisujemy symbolem:

$$\int f(x) \, dx = F(x) + C$$

Gdzie:
- $\int$ – znak całki (pochodzi od stylizowanej litery *S* – łac. *summa*),
- $f(x)$ – funkcja podcałkowa,
- $f(x)\,dx$ – wyrażenie podcałkowe,
- $x$ – zmienna całkowania,
- $C$ – stała całkowania ($C \in \mathbb{R}$).

---

## 2. Podstawowe własności całki nieoznaczonej

1. **Liniowość całki (całka sumy/różnicy oraz wyciąganie stałej):**

   $$\int \big( \alpha f(x) \pm \beta g(x) \big) \, dx = \alpha \int f(x) \, dx \pm \beta \int g(x) \, dx \quad (\alpha, \beta \in \mathbb{R})$$

2. **Pochodna całki nieoznaczonej:**

   $$\frac{d}{dx} \left( \int f(x) \, dx \right) = f(x)$$

3. **Całka z pochodnej funkcji:**

   $$\int F'(x) \, dx = F(x) + C$$

---

## 3. Tablica podstawowych wzorów całkowych

| Funkcja $f(x)$ | Całka $\int f(x) \, dx$ | Założenia |
| :--- | :--- | :--- |
| $0$ | $C$ | $C \in \mathbb{R}$ |
| $a$ | $a x + C$ | $a \in \mathbb{R}$ |
| $x^n$ | $\frac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\frac{1}{x}$ | $\ln\|x\| + C$ | $x \neq 0$ |
| $e^x$ | $e^x + C$ | |
| $a^x$ | $\frac{a^x}{\ln a} + C$ | $a > 0, a \neq 1$ |
| $\sin x$ | $-\cos x + C$ | |
| $\cos x$ | $\sin x + C$ | |
| $\frac{1}{\cos^2 x}$ | $\operatorname{tg} x + C$ | $x \neq \frac{\pi}{2} + k\pi$ |
| $\frac{1}{\sin^2 x}$ | $-\operatorname{ctg} x + C$ | $x \neq k\pi$ |
| $\frac{1}{1 + x^2}$ | $\operatorname{arctg} x + C$ | |
| $\frac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ | $x \in (-1, 1)$ |

---

## 4. Podstawowe metody wyznaczania całek

### 4.1. Całkowanie przez części
Wzór wyprowadza się z reguły różniczkowania iloczynu dwóch funkcji $(u \cdot v)' = u'v + uv'$:

$$\int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx$$

W zapisie różniczkowym ($du = u'\,dx$, $dv = v'\,dx$):

$$\int u \, dv = u v - \int v \, du$$

#### Przykład:
Obliczmy całkę $\int x e^x \, dx$:

Przyjmijmy:
- $u = x \implies du = dx$
- $dv = e^x \, dx \implies v = e^x$

Stosując wzór:

$$\int x e^x \, dx = x e^x - \int e^x \, dx = x e^x - e^x + C = e^x (x - 1) + C$$

---

### 4.2. Całkowanie przez podstawienie (zamiana zmiennych)
Metoda ta wynika z reguły łańcuchowej różniczkowania funkcji złożonej:

$$\int f\big( g(x) \big) \cdot g'(x) \, dx = \int f(u) \, du, \quad \text{gdzie } u = g(x), \ du = g'(x) dx$$

#### Przykład:
Obliczmy całkę $\int 2x \cos(x^2) \, dx$:

Podstawienie:
- $u = x^2$
- $du = 2x \, dx$

Otrzymujemy:

$$\int 2x \cos(x^2) \, dx = \int \cos(u) \, du = \sin(u) + C = \sin(x^2) + C$$

---

## 5. Całka oznaczona (w sensie Riemanna)

### 5.1. Intuicja geometryczna i konstrukcja Riemanna
Całka oznaczona $\int_{a}^{b} f(x) \, dx$ reprezentuje pole pod wykresem nieujemnej funkcji $f(x)$ w przedziale $[a, b]$.

Dzielimy przedział $[a, b]$ na $n$ podprzedziałów punktami $a = x_0 < x_1 < \dots < x_n = b$, gdzie $\Delta x_i = x_i - x_{i-1}$, a w każdym przedziale wybieramy punkt pośredni $\xi_i \in [x_{i-1}, x_i]$.

Suma Riemanna ma postać:

$$S_n = \sum_{i=1}^n f(\xi_i) \Delta x_i$$

Gdy średnica podziału $\lambda = \max_{1 \le i \le n} \Delta x_i \to 0$, granica tej sumy (jeśli istnieje i nie zależy od wyboru punktów) definiuje całkę oznaczoną:

$$\int_{a}^{b} f(x) \, dx = \lim_{\lambda \to 0} \sum_{i=1}^n f(\xi_i) \Delta x_i$$

---

### 5.2. Podstawowe Twierdzenie Rachunku Całkowego (Wzór Newtona-Leibniza)
Jeżeli funkcja $f(x)$ jest ciągła w przedziale $[a, b]$, a $F(x)$ jest jej dowolną funkcją pierwotną ($F'(x) = f(x)$), to:

$$\int_{a}^{b} f(x) \, dx = \Big[ F(x) \Big]_a^b = F(b) - F(a)$$

#### Przykład:
Obliczmy pole pod parabolą $f(x) = x^2$ na przedziale $[0, 2]$:

$$\int_{0}^{2} x^2 \, dx = \left[ \frac{x^3}{3} \right]_0^2 = \frac{2^3}{3} - \frac{0^3}{3} = \frac{8}{3}$$

---

### 5.3. Kluczowe własności całki oznaczonej

1. **Zamiana granic całkowania:**

   $$\int_{a}^{b} f(x) \, dx = -\int_{b}^{a} f(x) \, dx$$

2. **Równe granice całkowania:**

   $$\int_{a}^{a} f(x) \, dx = 0$$

3. **Addytywność względem przedziału całkowania:**

   $$\int_{a}^{b} f(x) \, dx = \int_{a}^{c} f(x) \, dx + \int_{c}^{b} f(x) \, dx \quad (c \in [a, b])$$

4. **Twierdzenie o wartości średniej:**
   Jeżeli $f$ jest ciągła na $[a, b]$, to istnieje punkt $c \in (a, b)$ taki, że:

   $$f(c) = \frac{1}{b - a} \int_{a}^{b} f(x) \, dx$$

---

## 6. Wybrane zastosowania geometryczne całek pojedynczych

### 6.1. Pole obszaru między dwoma wykresami
Jeżeli $f(x) \ge g(x)$ dla każdego $x \in [a, b]$:

$$P = \int_{a}^{b} \big( f(x) - g(x) \big) \, dx$$

### 6.2. Długość łuku krzywej
Dla funkcji $f(x)$ mającej ciągłą pochodną na przedziale $[a, b]$:

$$L = \int_{a}^{b} \sqrt{1 + \big( f'(x) \big)^2} \, dx$$

### 6.3. Objętość bryły obrotowej (obrót wokół osi $OX$)
Bryła powstała przez obrót wykresu funkcji $f(x)$ wokół osi $OX$ w granicach $x \in [a, b]$:

$$V = \pi \int_{a}^{b} \big( f(x) \big)^2 \, dx$$

### 6.4. Pole powierzchni bryły obrotowej (obrót wokół osi $OX$)
Pole powierzchni bocznej powstałej w wyniku obrotu wykresu $f(x)$:

$$S = 2\pi \int_{a}^{b} |f(x)| \sqrt{1 + \big( f'(x) \big)^2} \, dx$$
