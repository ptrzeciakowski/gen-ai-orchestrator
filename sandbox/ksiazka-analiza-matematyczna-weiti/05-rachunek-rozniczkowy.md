# Część V: Rachunek Różniczkowy Funkcji Jednej Zmiennej

Rachunek różniczkowy jest jednym z najdoskonalszych instrumentów analizy matematycznej. Umożliwia precyzyjne badanie lokalnego tempa zmian wielkości fizycznych, aproksymację zjawisk nieliniowych za pomocą modeli liniowych w otoczeniu punktu pracy oraz wyznaczanie optymalnych parametrów pracy układów. W informatyce pochodna stanowi kręgosłup uczenia maszynowego (algorytmy spadku gradientowego i wstecznej propagacji błędów), a w elektrotechnice opisuje relacje konstytutywne elementów reakcyjnych ($L, C$).

---

## Rozdział 9: Pochodna i różniczka funkcji

### 9.1. Definicja pochodnej i interpretacja fizyczno-geometryczna

Niech funkcja $f: X \to \mathbb{R}$ będzie określona w otoczeniu punktu $x_0 \in X$.

#### Definicja 9.1 (Iloraz różnicowy i pochodna)
1. **Ilorazem różnicowym** funkcji $f$ w punkcie $x_0$ odpowiadającym przyrostowi argumentu $\Delta x \neq 0$ nazywamy wyrażenie:
   $$\frac{\Delta f}{\Delta x} = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$
2. Jeżeli istnieje granica właściwa ilorazu różnicowego przy $\Delta x \to 0$, to granicę tę nazywamy **pochodną funkcji $f$ w punkcie $x_0$** i oznaczamy $f'(x_0)$ lub $\frac{df}{dx}(x_0)$:
   $$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

Funkcję posiadającą skończoną pochodną w punkcie $x_0$ nazywamy **różniczkowalną w punkcie $x_0$**.

#### Interpretacje pochodnej:
1. **Interpretacja geometryczna:**  
   Pochodna $f'(x_0)$ określa współczynnik kierunkowy (tangens kąta nachylenia $\alpha$) prostej stycznej do wykresu funkcji $y = f(x)$ w punkcie $P_0(x_0, f(x_0))$:
   $$m = \operatorname{tg} \alpha = f'(x_0)$$
   Równanie prostej **stycznej**:
   $$y - f(x_0) = f'(x_0)(x - x_0)$$
   Równanie prostej **normalnej** (prostopadłej do stycznej w punkcie styczności, gdy $f'(x_0) \neq 0$):
   $$y - f(x_0) = -\frac{1}{f'(x_0)}(x - x_0)$$

2. **Interpretacja fizyczna (Elektrotechnika i Teoria Sygnałów):**  
   - **Prąd elektryczny:** Prąd $i(t)$ jest pochodną ładunku elektrycznego $q(t)$ przepływającego przez przekrój poprzeczny przewodnika:
     $$i(t) = \frac{dq(t)}{dt}$$
   - **Napięcie na indukcyjności (Cewka):** Z prawa indukcji elektromagnetycznej Faradaya napięcie na cewce $L$ jest proporcjonalne do pochodnej natężenia prądu:
     $$u_L(t) = L \frac{di(t)}{dt}$$
   - **Prąd na pojemności (Kondensator):** Prąd ładujący kondensator o pojemności $C$ jest proporcjonalny do pochodnej napięcia:
     $$i_C(t) = C \frac{du_C(t)}{dt}$$

---

### 9.2. Ciągłość a różniczkowalność

> **Twierdzenie 9.1 (O ciągłości funkcji różniczkowalnej):**  
> Jeżeli funkcja $f$ jest różniczkowalna w punkcie $x_0$, to jest w tym punkcie ciągła.

**Dowód:**  
Dla $x \neq x_0$ zapiszmy tożsamość:
$$f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0} \cdot (x - x_0)$$
Przechodząc do granicy przy $x \to x_0$:
$$\lim_{x \to x_0} \big( f(x) - f(x_0) \big) = \lim_{x \to x_0} \left[ \frac{f(x) - f(x_0)}{x - x_0} \right] \cdot \lim_{x \to x_0} (x - x_0) = f'(x_0) \cdot 0 = 0$$
Stąd $\lim_{x \to x_0} f(x) = f(x_0)$, co dowodzi ciągłości w punkcie $x_0$. $\blacksquare$

> **Uwaga krytyczna:**  
> Ciągłość jest warunkiem **koniecznym**, lecz **niewystarczającym** dla różniczkowalności!  
> Funkcja $f(x) = |x|$ jest ciągła w punkcie $x_0 = 0$, lecz pochodne jednostronne są różne:
> $$f'_-(0) = \lim_{x \to 0^-} \frac{|x| - 0}{x} = -1 \neq f'_+(0) = \lim_{x \to 0^+} \frac{|x| - 0}{x} = +1$$
> Istnieją nawet funkcje ciągłe na całym $\mathbb{R}$, które nie posiadają pochodnej w **żadnym punkcie** (funkcja Weierstrassa $W(x) = \sum_{n=0}^\infty a^n \cos(b^n \pi x)$).

---

### 9.3. Podstawowe reguły różniczkowania

> **Twierdzenie 9.2 (Reguły różniczkowania):**  
> Niech funkcje $f$ i $g$ będą różniczkowalne w punkcie $x$:
> 1. **Liniowość:** $(\alpha f + \beta g)'(x) = \alpha f'(x) + \beta g'(x) \quad (\alpha, \beta \in \mathbb{R})$,
> 2. **Pochodna iloczynu:** $(f \cdot g)'(x) = f'(x)g(x) + f(x)g'(x)$,
> 3. **Pochodna ilorazu:** $\left( \frac{f}{g} \right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2} \quad (g(x) \neq 0)$,
> 4. **Reguła łańcuchowa (pochodna złożenia):** $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$,
> 5. **Pochodna funkcji odwrotnej:** Jeżeli $f$ jest ściśle monotoniczna i różniczkowalna w $x_0$ oraz $f'(x_0) \neq 0$, to funkcja odwrotna $f^{-1}$ jest różniczkowalna w punkcie $y_0 = f(x_0)$ i:
>    $$(f^{-1})'(y_0) = \frac{1}{f'(x_0)} = \frac{1}{f'(f^{-1}(y_0))}$$

#### Pochodna logarytmiczna:
Dla funkcji postaci $y = [u(x)]^{v(x)}$ ($u(x) > 0$):
$$\ln y = v(x) \ln u(x) \implies \frac{y'}{y} = v'(x)\ln u(x) + v(x)\frac{u'(x)}{u(x)}$$
$$y' = [u(x)]^{v(x)} \left( v'(x) \ln u(x) + \frac{v(x) u'(x)}{u(x)} \right)$$

#### Wzór Leibniza na $n$-tą pochodną iloczynu:
Dla funkcji $n$-krotnie różniczkowalnych:
$$(f \cdot g)^{(n)}(x) = \sum_{k=0}^n \binom{n}{k} f^{(k)}(x) g^{(n-k)}(x)$$

---

### 9.4. Różniczka funkcji i jej zastosowania inżynierskie

#### Definicja 9.2 (Różniczka funkcji)
Jeżeli funkcja $f$ jest różniczkowalna w punkcie $x_0$, to wyrażenie:
$$df(x_0, \Delta x) = f'(x_0) \Delta x = f'(x_0) dx$$
liniowe względem przyrostu argumentu $dx = \Delta x$, nazywamy **różniczką funkcji $f$ w punkcie $x_0$**.

Rzeczywisty przyrost funkcji wynosi:
$$\Delta f = f(x_0 + \Delta x) - f(x_0) = f'(x_0)\Delta x + \alpha(\Delta x)\cdot \Delta x = df + o(\Delta x)$$
Różniczka stanowi zatem **liniową część główną przyrostu funkcji**, co pozwala na linearyzację w otoczeniu punktu pracy:
$$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x$$

#### Zastosowanie w teorii obwodów: Linearyzacja nieliniowości małosygnałowych
W złączu p-n diody półprzewodnikowej prąd zależy nieliniowo od napięcia według równania Shockleya:
$$I_D = I_S \left( e^{\frac{U_D}{n V_T}} - 1 \right)$$
W stałoprądowym punkcie pracy $Q(U_{D0}, I_{D0})$ małym zmianom napięcia $u_d(t)$ odpowiada przyrost prądu opisany różniczką:
$$i_d(t) \approx \left. \frac{dI_D}{dU_D} \right|_{Q} \cdot u_d(t) = g_d \cdot u_d(t)$$
Wielkość $g_d = \frac{1}{r_d} = \frac{I_{D0} + I_S}{n V_T} \approx \frac{I_{D0}}{n V_T}$ jest **konduktancją dynamiczną** diody. Pozwala to na zastąpienie nieliniowego elementu rezystorem liniowym $r_d$ dla małych sygnałów zmiennych.

---

## Rozdział 10: Twierdzenia o wartości średniej i wzór Taylora

### 10.1. Twierdzenia Rolle'a, Lagrange'a i Cauchy'ego

> **Lemat Fermata (Warunek konieczny istnienia ekstremum funkcji różniczkowalnej):**  
> Jeżeli funkcja $f$ ma w punkcie $x_0 \in (a, b)$ ekstremum lokalne i jest w nim różniczkowalna, to:
> $$f'(x_0) = 0$$

**Dowód:**  
Niech w $x_0$ będzie maksimum lokalne. Wtedy dla małych $h > 0$: $\frac{f(x_0+h)-f(x_0)}{h} \le 0 \implies f'_+(x_0) \le 0$.  
Dla małych $h < 0$: $\frac{f(x_0+h)-f(x_0)}{h} \ge 0 \implies f'_-(x_0) \ge 0$.  
Z różniczkowalności $f'_+(x_0) = f'_-(x_0) = f'(x_0) \implies f'(x_0) = 0$. $\blacksquare$

> **Twierdzenie 10.1 (Rolle'a):**  
> Jeżeli funkcja $f: [a, b] \to \mathbb{R}$ jest ciągła na $[a, b]$, różniczkowalna na $(a, b)$ oraz $f(a) = f(b)$, to istnieje co najmniej jeden punkt $c \in (a, b)$ taki, że:
> $$f'(c) = 0$$

**Dowód:**  
Z II twierdzenia Weierstrassa funkcja $f$ osiąga na $[a, b]$ swój kres dolny $m$ i górny $M$.  
- Jeżeli $m = M$, to $f$ jest funkcją stałą i $f'(x) = 0$ dla każdego $x \in (a, b)$.  
- Jeżeli $m < M$, to ponieważ $f(a) = f(b)$, co najmniej jeden z kresów musi być osiągany w punkcie wewnętrznym $c \in (a, b)$. W punkcie tym $f$ posiada ekstremum lokalne, skąd z Lematu Fermata $f'(c) = 0$. $\blacksquare$

> **Twierdzenie 10.2 (Lagrange'a o wartości średniej):**  
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$ i różniczkowalna na $(a, b)$, to istnieje punkt $c \in (a, b)$ taki, że:
> $$\frac{f(b) - f(a)}{b - a} = f'(c) \iff f(b) - f(a) = f'(c)(b - a)$$

**Dowód:**  
Wprowadzamy funkcję pomocniczą opisującą odchylenie wykresu od cięciwy łączącej punkty $(a, f(a))$ i $(b, f(b))$:
$$\varphi(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a)$$
Funkcja $\varphi$ spełnia założenia twierdzenia Rolle'a: jest ciągła na $[a, b]$, różniczkowalna na $(a, b)$ oraz $\varphi(a) = \varphi(b) = 0$. Zatem istnieje $c \in (a, b)$ takie, że $\varphi'(c) = 0$:
$$\varphi'(c) = f'(c) - \frac{f(b) - f(a)}{b - a} = 0 \implies f'(c) = \frac{f(b) - f(a)}{b - a} \quad \blacksquare$$

> **Twierdzenie 10.3 (Cauchy'ego o wartości średniej):**  
> Jeżeli funkcje $f, g$ są ciągłe na $[a, b]$, różniczkowalne na $(a, b)$ oraz $g'(x) \neq 0$ na $(a, b)$, to istnieje punkt $c \in (a, b)$ taki, że:
> $$\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}$$

---

### 10.2. Reguła de l'Hospitala

> **Twierdzenie 10.4 (Reguła de l'Hospitala):**  
> Niech funkcje $f$ i $g$ będą różniczkowalne w sąsiedztwie $S(x_0)$ oraz $g'(x) \neq 0$. Jeżeli:
> 1. $\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0 \quad (\text{symbol } [0/0])$  
> lub  
> 2. $\lim_{x \to x_0} |g(x)| = +\infty \quad (\text{symbol } [\infty/\infty])$,  
> oraz istnieje granica (właściwa lub niewłaściwa):
> $$\lim_{x \to x_0} \frac{f'(x)}{g'(x)} = K$$
> to istnieje również granica wyjściowa i:
> $$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{f'(x)}{g'(x)} = K$$

**Dowód dla przypadku $[0/0]$ w punkcie $x_0$:**  
Kładziemy $f(x_0) = 0$ oraz $g(x_0) = 0$, rozszerzając obie funkcje w sposób ciągły na punkt $x_0$.  
Dla dowolnego $x \in S(x_0)$ funkcje $f$ i $g$ spełniają założenia twierdzenia Cauchy'ego o wartości średniej na przedziale o końcach $x_0$ i $x$. Istnieje zatem punkt $c$ leżący ściśle między $x_0$ a $x$ taki, że:
$$\frac{f(x)}{g(x)} = \frac{f(x) - f(x_0)}{g(x) - g(x_0)} = \frac{f'(c)}{g'(c)}$$
Gdy $x \to x_0$, to na mocy twierdzenia o trzech funkcjach również $c \to x_0$. Przechodząc do granicy:
$$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{c \to x_0} \frac{f'(c)}{g'(c)} = K \quad \blacksquare$$

---

### 10.3. Wzór Taylora i Maclaurina

> **Twierdzenie 10.5 (Wzór Taylora z resztą w postaci Lagrange'a i Peano):**  
> Jeżeli funkcja $f$ ma ciągłe pochodne do rzędu $n$ w otoczeniu $U(x_0)$ oraz posiada pochodną rzędu $(n+1)$ w tym otoczeniu, to dla każdego $x \in U(x_0)$:
> $$f(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k + R_n(x)$$
> gdzie reszta $R_n(x)$ może być zapisana jako:
> - **Postać Lagrange'a:** $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!} (x - x_0)^{n+1}$ dla pewnego $c \in (x_0, x)$,
> - **Postać Peano:** $R_n(x) = o\big((x - x_0)^n\big)$ przy $x \to x_0$.

Gdy $x_0 = 0$, wzór nazywamy **wzorem Maclaurina**.

#### Standardowe rozwinięcia Maclaurina:
1. $e^x = \sum_{k=0}^n \frac{x^k}{k!} + o(x^n) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^n}{n!} + o(x^n)$
2. $\sin x = \sum_{k=0}^n \frac{(-1)^k x^{2k+1}}{(2k+1)!} + o(x^{2n+2}) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
3. $\cos x = \sum_{k=0}^n \frac{(-1)^k x^{2k}}{(2k)!} + o(x^{2n+1}) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
4. $\ln(1 + x) = \sum_{k=1}^n \frac{(-1)^{k-1} x^k}{k} + o(x^n) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$
5. $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2!} x^2 + \dots + \binom{\alpha}{n} x^n + o(x^n)$
6. $\frac{1}{1 - x} = 1 + x + x^2 + \dots + x^n + o(x^n)$

---

## Rozdział 11: Badanie przebiegu zmienności funkcji

### 11.1. Monotoniczność i ekstrema lokalne

1. **Kryteria monotoniczności:**
   - Jeżeli $f'(x) > 0$ na $(a, b)$, to funkcja jest ściśle rosnąca na $(a, b)$.
   - Jeżeli $f'(x) < 0$ na $(a, b)$, to funkcja jest ściśle malejąca na $(a, b)$.
2. **Kryterium I pochodnej (warunek wystarczający istnienia ekstremum):**  
   Niech $x_0$ będzie punktem krytycznym ($f'(x_0) = 0$ lub $f'(x_0)$ nie istnieje):
   - zmiana znaku z $+$ na $-$ $\implies$ **maksimum lokalne właściwe**,
   - zmiana znaku z $-$ na $+$ $\implies$ **minimum lokalne właściwe**,
   - brak zmiany znaku $\implies$ brak ekstremum.
3. **Kryterium II pochodnej:**  
   Niech $f'(x_0) = 0$.
   - Jeżeli $f''(x_0) < 0$, to w $x_0$ występuje **maksimum lokalne właściwe**.
   - Jeżeli $f''(x_0) > 0$, to w $x_0$ występuje **minimum lokalne właściwe**.
   - Jeżeli $f''(x_0) = 0$, kryterium nie rozstrzyga (należy badać wyższe pochodne lub zmianę znaku I pochodnej).

---

### 11.2. Wypukłość, wklęsłość i punkty przegięcia

1. **Definicja geometryczna:** Funkcja $f$ jest **wypukła** na przedziale, jeżeli wykres funkcji leży pod każdą cięciwą łączącą dwa punkty wykresu (oraz nad każdą styczną). Funkcja jest **wklęsła**, jeżeli leży nad cięciwami (i pod stycznymi).
2. **Kryteria II pochodnej:**
   - $f''(x) > 0$ na $(a, b) \implies$ funkcja jest ściśle wypukła na $(a, b)$,
   - $f''(x) < 0$ na $(a, b) \implies$ funkcja jest ściśle wklęsła na $(a, b)$.
3. **Punkt przegięcia:** Punkt $(x_0, f(x_0))$ wykresu, w którym funkcja zmienia charakter z wypukłej na wklęsłą (lub odwrotnie). Styczna do wykresu w punkcie przegięcia przecina wykres funkcji!
   - *Warunek konieczny:* $f''(x_0) = 0$ (lub $f''$ nie istnieje).
   - *Warunek dostateczny:* zmiana znaku $f''(x)$ przy przejściu przez $x_0$.

---

### 11.3. Asymptoty wykresu funkcji

1. **Asymptota pionowa $x = x_0$:**  
   Występuje, gdy co najmniej jedna z granic jednostronnych jest nieskończona:
   $$\lim_{x \to x_0^-} f(x) = \pm\infty \quad \text{lub} \quad \lim_{x \to x_0^+} f(x) = \pm\infty$$
2. **Asymptota ukośna $y = ax + b$ (w $+\infty$ lub $-\infty$):**
   $$a = \lim_{x \to \pm\infty} \frac{f(x)}{x}, \quad b = \lim_{x \to \pm\infty} \big( f(x) - ax \big)$$
   Jeżeli $a = 0$, prosta $y = b$ jest **asymptotą poziomą**.

---

### 11.4. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 11.1 (Reguła de l'Hospitala dla potęgi $[1^\infty]$)
Obliczyć granicę:
$$\lim_{x \to 0} \left( \frac{\sin x}{x} \right)^{1/x^2}$$

**Rozwiązanie:**  
Przekształcamy tożsamością wykładniczą:
$$\left( \frac{\sin x}{x} \right)^{1/x^2} = \exp\left( \frac{\ln(\sin x / x)}{x^2} \right)$$
Badamy granicę wykładnika $L = \lim_{x \to 0} \frac{\ln(\sin x / x)}{x^2} = \left[\frac{0}{0}\right]$.  
Stosujemy regułę de l'Hospitala:
$$L = \lim_{x \to 0} \frac{\frac{x}{\sin x} \cdot \frac{x\cos x - \sin x}{x^2}}{2x} = \lim_{x \to 0} \frac{x\cos x - \sin x}{2x^2 \sin x} = \lim_{x \to 0} \left( \frac{x\cos x - \sin x}{2x^3} \cdot \frac{x}{\sin x} \right) = \frac{1}{2} \lim_{x \to 0} \frac{x\cos x - \sin x}{x^3}$$
Ponownie stosujemy regułę de l'Hospitala:
$$\lim_{x \to 0} \frac{\cos x - x\sin x - \cos x}{3x^2} = \lim_{x \to 0} \frac{-x\sin x}{3x^2} = -\frac{1}{3} \lim_{x \to 0} \frac{\sin x}{x} = -\frac{1}{3}$$
Stąd $L = \frac{1}{2} \cdot \left(-\frac{1}{3}\right) = -\frac{1}{6}$. Granica wyjściowa:
$$\lim_{x \to 0} \left( \frac{\sin x}{x} \right)^{1/x^2} = e^{-1/6} = \frac{1}{\sqrt[6]{e}}$$

---

#### Przykład 11.2 (Optymalizacja inżynierska: Twierdzenie o dopasowaniu odbiornika)
Układ zasilający o napięciu Thevenina $E$ i rezystancji wewnętrznej $R_w$ zasila obciążenie $R$. Wyznaczyć wartość rezystancji $R$, dla której moc wydzielana w obciążeniu jest maksymalna.

**Rozwiązanie:**  
Prąd w obwodzie wynosi $I = \frac{E}{R + R_w}$.  
Moc wydzielana w odbiorniku wynosi:
$$P(R) = I^2 R = \frac{E^2 R}{(R + R_w)^2}$$
Różniczkujemy funkcję mocy po $R > 0$:
$$P'(R) = E^2 \frac{1 \cdot (R + R_w)^2 - R \cdot 2(R + R_w)}{(R + R_w)^4} = E^2 \frac{(R + R_w)[(R + R_w) - 2R]}{(R + R_w)^4} = E^2 \frac{R_w - R}{(R + R_w)^3}$$
Punkt stacjonarny: $P'(R) = 0 \iff R = R_w$.  
Badamy znak pochodnej:
- dla $R < R_w$: $P'(R) > 0$ (funkcja rosnąca),
- dla $R > R_w$: $P'(R) < 0$ (funkcja malejąca).
W punkcie $R = R_w$ pochodna zmienia znak z $+$ na $-$, zatem występuje w nim **maksimum absolutne**.  
Maksymalna moc dopasowana:
$$P_{\max} = \frac{E^2 R_w}{(2R_w)^2} = \frac{E^2}{4R_w}$$
Sprawność układu przy dopasowaniu mocy wynosi dokładnie $\eta = 50\%$.

---

#### Przykład 11.3 (Rozwinięcie Taylora do obliczania granic)
Obliczyć granicę:
$$\lim_{x \to 0} \frac{x - \sin x}{x^2 (e^x - 1)}$$

**Rozwiązanie:**  
Stosujemy rozwinięcia Maclaurina:
$$\sin x = x - \frac{x^3}{6} + o(x^3) \implies x - \sin x = \frac{x^3}{6} + o(x^3)$$
$$e^x - 1 = x + o(x) \implies x^2 (e^x - 1) = x^3 + o(x^3)$$
Dzieląc licznik i mianownik przez $x^3$:
$$\lim_{x \to 0} \frac{\frac{1}{6} x^3 + o(x^3)}{x^3 + o(x^3)} = \frac{1/6}{1} = \frac{1}{6}$$

---

#### Przykład 11.4 (Pełne badanie przebiegu zmienności funkcji)
Zbadać przebieg zmienności funkcji $f(x) = \frac{x^3}{x^2 - 4}$.

**Rozwiązanie:**  
1. **Dziedzina i parzystość:**  
   $D_f = \mathbb{R} \setminus \{-2, 2\}$.  
   $f(-x) = \frac{(-x)^3}{(-x)^2 - 4} = -\frac{x^3}{x^2 - 4} = -f(x)$ – funkcja jest **nieparzysta** (wykres symetryczny względem początku układu). Wystarczy badać dla $x \ge 0$.
2. **Miejsca zerowe:** $f(x) = 0 \iff x = 0$.
3. **Asymptoty:**
   - Pionowe: $\lim_{x \to 2^-} f(x) = -\infty$, $\lim_{x \to 2^+} f(x) = +\infty \implies$ asymptota obustronna $x = 2$ (oraz z nieparzystości $x = -2$).
   - Ukośne:
     $$a = \lim_{x \to \infty} \frac{f(x)}{x} = \lim_{x \to \infty} \frac{x^2}{x^2 - 4} = 1$$
     $$b = \lim_{x \to \infty} \big( f(x) - x \big) = \lim_{x \to \infty} \left( \frac{x^3 - x(x^2 - 4)}{x^2 - 4} \right) = \lim_{x \to \infty} \frac{4x}{x^2 - 4} = 0$$
     Prosta $y = x$ jest asymptotą ukośną w obu nieskończonościach ($\pm\infty$).
4. **Pochodna I rzędu i ekstrema:**
   $$f'(x) = \frac{3x^2(x^2 - 4) - x^3(2x)}{(x^2 - 4)^2} = \frac{3x^4 - 12x^2 - 2x^4}{(x^2 - 4)^2} = \frac{x^2(x^2 - 12)}{(x^2 - 4)^2}$$
   Punkty stacjonarne: $x = 0$ oraz $x = \pm\sqrt{12} = \pm 2\sqrt{3}$.
   Dla $x > 0$:
   - $x \in (0, 2) \implies f'(x) < 0$ (maleje),
   - $x \in (2, 2\sqrt{3}) \implies f'(x) < 0$ (maleje),
   - $x \in (2\sqrt{3}, \infty) \implies f'(x) > 0$ (rośnie).
   W punkcie $x = 2\sqrt{3}$ funkcja posiada **minimum lokalne właściwe**:
   $$f_{\min} = f(2\sqrt{3}) = \frac{(2\sqrt{3})^3}{12 - 4} = \frac{24\sqrt{3}}{8} = 3\sqrt{3}$$
   Z nieparzystości: w $x = -2\sqrt{3}$ występuje **maksimum lokalne właściwe** $f_{\max} = -3\sqrt{3}$.
5. **Pochodna II rzędu i punkty przegięcia:**
   $$f''(x) = \frac{8x(x^2 + 12)}{(x^2 - 4)^3}$$
   Dla $x = 0$: $f''(0) = 0$, następuje zmiana znaku z $-$ na $+$ $\implies$ punkt $(0, 0)$ jest **punktem przegięcia**.

---

### 11.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 11.1:** Obliczyć pochodną funkcji $f(x) = (\cos x)^{\ln x}$.  
   *Odpowiedź:* $f'(x) = (\cos x)^{\ln x} \left( \frac{\ln(\cos x)}{x} - \ln x \cdot \operatorname{tg} x \right)$.

2. **Zadanie 11.2:** Wyznaczyć rozwinięcie Maclaurina do rzędu 4 dla funkcji $f(x) = \sqrt{1 + 2x^2}$.  
   *Odpowiedź:* $f(x) = 1 + x^2 - \frac{1}{2}x^4 + o(x^4)$.

3. **Zadanie 11.3:** Wyznaczyć równanie stycznej i normalnej do wykresu funkcji $f(x) = x \ln x$ w punkcie $x_0 = 1$.  
   *Odpowiedź:* $f(1) = 0$, $f'(1) = 1$. Styczna: $y = x - 1$; normalna: $y = -(x - 1) = -x + 1$.

4. **Zadanie 11.4:** Obliczyć granicę: $\lim_{x \to 0} \frac{\operatorname{tg} x - \sin x}{x^3}$.  
   *Odpowiedź:* $\frac{1}{2}$.

5. **Zadanie 11.5:** Wykazać za pomocą wzoru Taylora z resztą Lagrange'a, że dla każdego $x > 0$:  
   $$x - \frac{x^2}{2} < \ln(1 + x) < x$$

6. **Zadanie 11.6:** Znaleźć wymiary cylindrycznej puszki o zadanej objętości $V$, której pole powierzchni całkowitej jest minimalne (minimalizacja zużycia blachy).  
   *Odpowiedź:* $H = 2R = 2 \sqrt[3]{V / (2\pi)}$ (wysokość równa średnicy podstawy).
