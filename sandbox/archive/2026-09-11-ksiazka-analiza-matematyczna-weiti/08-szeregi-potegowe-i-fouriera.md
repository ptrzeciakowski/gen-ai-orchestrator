# Część VIII: Szeregi Funkcyjne, Potęgowe i Wprowadzenie do Analizy Fourierowskiej

W analizie matematycznej, teorii sygnałów i telekomunikacji reprezentacja skomplikowanych funkcji ciągłych i nieciągłych za pomocą nieskończonych sum funkcji elementarnych (wielomianów lub sinusoid) stanowi najpotężniejsze narzędzie modelowania. Szeregi potęgowe Taylora pozwalają na aproksymację lokalną nieliniowości w układach elektronicznych oraz na numeryczne wyznaczanie wartości funkcji w procesorach DSP. Z kolei szeregi Fouriera przenoszą sygnały z dziedziny czasu do dziedziny częstotliwości (analiza widmowa), co stanowi kręgosłup współczesnej radiokomunikacji, kompresji multimediów (MP3, JPEG) oraz filtracji sygnałów.

---

## Rozdział 17: Szeregi funkcyjne i potęgowe

### 17.1. Zbieżność punktowa i jednostajna ciągów i szeregów funkcyjnych

Niech dany będzie ciąg funkcji $f_n: X \to \mathbb{R}$ ($n \in \mathbb{N}$) określonych na wspólnym zbiorze $X \subset \mathbb{R}$.

#### Definicja 17.1 (Zbieżność punktowa)
Mówimy, że ciąg funkcji $(f_n)$ jest **zbieżny punktowo** na zbiorze $X$ do funkcji granicznej $f: X \to \mathbb{R}$, co zapisujemy $f_n \to f$, jeżeli dla każdego ustalonego punktu $x \in X$:
$$\lim_{n \to \infty} f_n(x) = f(x) \iff \forall x \in X \forall \varepsilon > 0 \exists N \in \mathbb{N} \forall n > N: \quad |f_n(x) - f(x)| < \varepsilon$$
Wskaźnik $N$ zależy zarówno od $\varepsilon$, jak i od wybranego punktu $x$ ($N = N(\varepsilon, x)$).

#### Definicja 17.2 (Zbieżność jednostajna)
Ciąg funkcji $(f_n)$ jest **zbieżny jednostajnie** na zbiorze $X$ do funkcji $f$, co zapisujemy $f_n \rightrightarrows f$, jeżeli:
$$\forall \varepsilon > 0 \exists N \in \mathbb{N} \forall n > N \forall x \in X: \quad |f_n(x) - f(x)| < \varepsilon$$
Wskaźnik $N$ zależy wyłącznie od $\varepsilon$ ($N = N(\varepsilon)$).  
Równoważnie w metryce Czebyszewa (supremowej):
$$f_n \rightrightarrows f \iff \lim_{n \to \infty} \sup_{x \in X} |f_n(x) - f(x)| = 0$$

#### Zbieżność szeregów funkcyjnych:
Szereg funkcyjny $\sum_{n=1}^\infty f_n(x)$ jest zbieżny jednostajnie na $X$, jeżeli ciąg jego sum częściowych $S_k(x) = \sum_{n=1}^k f_n(x)$ jest zbieżny jednostajnie na $X$.

> **Twierdzenie 17.1 (Kryterium Weierstrassa zbieżności jednostajnej / Kryterium majoranty):**  
> Jeżeli dla każdego $n \in \mathbb{N}$ oraz każdego $x \in X$ zachodzi nierówność:
> $$|f_n(x)| \le M_n$$
> gdzie szereg liczbowy $\sum_{n=1}^\infty M_n$ jest zbieżny, to szereg funkcyjny $\sum_{n=1}^\infty f_n(x)$ jest zbieżny bezwzględnie i **jednostajnie** na zbiorze $X$.

---

### 17.2. Własności sumy szeregu jednostajnie zbieżnego

Zbieżność punktowa nie zachowuje ciągłości ani operacji różniczkowania i całkowania. Zbieżność jednostajna gwarantuje pełną przemienność tych operacji.

> **Twierdzenie 17.2 (Ciągłość sumy szeregu):**  
> Jeżeli funkcje $f_n(x)$ są ciągłe na przedziale $[a, b]$ oraz szereg $\sum_{n=1}^\infty f_n(x)$ jest zbieżny jednostajnie na $[a, b]$ do funkcji $S(x)$, to funkcja sumy $S(x)$ jest **ciągła** na $[a, b]$.

> **Twierdzenie 17.3 (Całkowanie wyraz po wyrazie):**  
> Jeżeli funkcje $f_n(x)$ są ciągłe na $[a, b]$ oraz szereg $\sum_{n=1}^\infty f_n(x)$ jest zbieżny jednostajnie do $S(x)$, to:
> $$\int_a^b S(x)\,dx = \int_a^b \left( \sum_{n=1}^\infty f_n(x) \right) dx = \sum_{n=1}^\infty \int_a^b f_n(x)\,dx$$

> **Twierdzenie 17.4 (Różniczkowanie wyraz po wyrazie):**  
> Jeżeli funkcje $f_n(x)$ są klasy $C^1$ na $[a, b]$, szereg $\sum_{n=1}^\infty f_n(x_0)$ jest zbieżny w co najmniej jednym punkcie $x_0 \in [a, b]$, a szereg pochodnych $\sum_{n=1}^\infty f_n'(x)$ jest **zbieżny jednostajnie** na $[a, b]$, to szereg wyjściowy jest zbieżny jednostajnie do funkcji różniczkowalnej $S(x)$ oraz:
> $$S'(x) = \left( \sum_{n=1}^\infty f_n(x) \right)' = \sum_{n=1}^\infty f_n'(x)$$

---

### 17.3. Szeregi potęgowe i twierdzenie Cauchy'ego-Hadamarda

#### Definicja 17.3 (Szereg potęgowy)
Szeregiem potęgowym o środku w punkcie $x_0 \in \mathbb{R}$ nazywamy szereg funkcyjny postaci:
$$\sum_{n=0}^\infty a_n (x - x_0)^n = a_0 + a_1(x - x_0) + a_2(x - x_0)^2 + \dots$$
gdzie $a_n \in \mathbb{R}$ są współczynnikami szeregu.

> **Twierdzenie 17.5 (Cauchy'ego-Hadamarda o promieniu zbieżności):**  
> Dla każdego szeregu potęgowego istnieje liczba $R \in [0, +\infty]$ (zwana **promieniem zbieżności**) taka, że:
> 1. Szereg jest zbieżny bezwzględnie dla każdego $x$ spełniającego $|x - x_0| < R$,
> 2. Szereg jest rozbieżny dla każdego $x$ spełniającego $|x - x_0| > R$,
> 3. Na każdym przedziale domkniętym $[x_0 - r, x_0 + r] \subset (x_0 - R, x_0 + R)$ ($r < R$) szereg jest zbieżny **jednostajnie**.  
> Promień zbieżności wyznacza się ze wzorów:
> $$R = \frac{1}{\limsup_{n\to\infty} \sqrt[n]{|a_n|}} \quad \text{lub gdy istnieje granica:} \quad R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right|$$

Przedział $(x_0 - R, x_0 + R)$ nazywamy **przedziałem zbieżności**. Zbieżność na końcach przedziału (dla $x = x_0 \pm R$) bada się indywidualnie metodami dla szeregów liczbowych.

> **Twierdzenie 17.6 (Różniczkowalność i analityczność szeregu potęgowego):**  
> Suma szeregu potęgowego $S(x) = \sum_{n=0}^\infty a_n (x - x_0)^n$ jest funkcją nieskończenie wiele razy różniczkowalną wewnątrz przedziału zbieżności ($|x - x_0| < R$). Szereg można różniczkować i całkować wyraz po wyrazie dowolną liczbę razy bez zmiany promienia zbieżności $R$, przy czym:
> $$a_n = \frac{S^{(n)}(x_0)}{n!}$$
> Oznacza to, że każdy szereg potęgowy jest szeregiem Taylora swojej sumy!

---

## Rozdział 18: Trygonometryczne szeregi Fouriera

### 18.1. Układ ortogonalny funkcji trygonometrycznych

Rozważmy przestrzeń funkcji całkowalnych z kwadratem $L^2([-\pi, \pi])$ z iloczynem skalarnym:
$$\langle f, g \rangle = \int_{-\pi}^\pi f(x) g(x)\,dx$$
Dwie funkcje są ortogonalne, jeżeli ich iloczyn skalarny wynosi zero.

> **Twierdzenie 18.1 (Ortogonalność układu trygonometrycznego):**  
> Układ funkcji:
> $$\{ 1, \; \cos(x), \; \sin(x), \; \cos(2x), \; \sin(2x), \; \dots, \; \cos(nx), \; \sin(nx), \; \dots \}$$
> jest ortogonalny na przedziale $[-\pi, \pi]$, to znaczy dla dowolnych $n, m \in \mathbb{N}$:
> 1. $\int_{-\pi}^\pi \cos(nx) \sin(mx)\,dx = 0$,
> 2. $\int_{-\pi}^\pi \cos(nx) \cos(mx)\,dx = \begin{cases} 0 & \text{dla } n \neq m \\ \pi & \text{dla } n = m \ge 1 \\ 2\pi & \text{dla } n = m = 0 \end{cases}$
> 3. $\int_{-\pi}^\pi \sin(nx) \sin(mx)\,dx = \begin{cases} 0 & \text{dla } n \neq m \\ \pi & \text{dla } n = m \ge 1 \end{cases}$

---

### 18.2. Współczynniki Fouriera i twierdzenie Dirichleta

#### Definicja 18.4 (Szereg Fouriera)
Trygonometrycznym szeregiem Fouriera funkcji $2\pi$-okresowej $f(x)$ nazywamy szereg:
$$S_f(x) = \frac{a_0}{2} + \sum_{n=1}^\infty \big( a_n \cos(nx) + b_n \sin(nx) \big)$$
gdzie współczynniki Eulera-Fouriera wyznacza się ze wzorów:
$$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi f(x)\,dx$$
$$a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos(nx)\,dx \quad (n \ge 1)$$
$$b_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin(nx)\,dx \quad (n \ge 1)$$

> **Twierdzenie 18.2 (Warunki Dirichleta zbieżności szeregu Fouriera):**  
> Jeżeli funkcja $2\pi$-okresowa $f(x)$ spełnia w przedziale $[-\pi, \pi]$ **warunki Dirichleta**:
> 1. Jest kawałkami ciągła (posiada co najwyżej skończoną liczbę punktów nieciągłości I rodzaju),
> 2. Jest kawałkami monotoniczna (posiada co najwyżej skończoną liczbę ekstremów lokalnych),  
> to szereg Fouriera funkcji $f$ jest zbieżny w każdym punkcie $x \in \mathbb{R}$, przy czym:
> $$S_f(x) = \frac{f(x^+) + f(x^-)}{2}$$
> - W punktach ciągłości funkcji: $S_f(x) = f(x)$.
> - W punktach skoku (nieciągłości): suma szeregu jest równa średniej arytmetycznej granic jednostronnych.

#### Uproszczenia dla funkcji parzystych i nieparzystych:
1. **Funkcja parzysta ($f(-x) = f(x)$):**
   $$b_n = 0 \quad \forall n \ge 1, \quad a_n = \frac{2}{\pi} \int_0^\pi f(x) \cos(nx)\,dx$$
   Szereg Fouriera staje się **szeregiem cosinusowym**.
2. **Funkcja nieparzysta ($f(-x) = -f(x)$):**
   $$a_n = 0 \quad \forall n \ge 0, \quad b_n = \frac{2}{\pi} \int_0^\pi f(x) \sin(nx)\,dx$$
   Szereg Fouriera staje się **szeregiem sinusowym**.

---

### 18.3. Szereg Fouriera o dowolnym okresie i postać zespolona

Dla funkcji okresowej o okresie $T = 2L$ z pulsacją podstawową $\omega_0 = \frac{2\pi}{T} = \frac{\pi}{L}$:
$$f(t) = \frac{a_0}{2} + \sum_{n=1}^\infty \big( a_n \cos(n \omega_0 t) + b_n \sin(n \omega_0 t) \big)$$
gdzie:
$$a_n = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \cos(n \omega_0 t)\,dt, \quad b_n = \frac{2}{T} \int_{-T/2}^{T/2} f(t) \sin(n \omega_0 t)\,dt$$

#### Zespolona postać szeregu Fouriera:
Stosując tożsamości Eulera $\cos \theta = \frac{e^{i\theta} + e^{-i\theta}}{2}, \sin \theta = \frac{e^{i\theta} - e^{-i\theta}}{2i}$:
$$f(t) = \sum_{n=-\infty}^\infty c_n e^{i n \omega_0 t}$$
gdzie zespolone współczynniki widmowe wyznacza się z całki:
$$c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-i n \omega_0 t}\,dt$$
Związki ze współczynnikami rzeczywistymi: $c_0 = \frac{a_0}{2}$, $c_n = \frac{a_n - i b_n}{2}$, $c_{-n} = c_n^* = \frac{a_n + i b_n}{2}$.

---

### 18.4. Tożsamość Parsevala i widmo mocy sygnału

> **Twierdzenie 18.3 (Tożsamość Parsevala):**  
> Dla funkcji okresowej $f(t) \in L^2([-T/2, T/2])$ zachodzi równość:
> $$\frac{1}{T} \int_{-T/2}^{T/2} [f(t)]^2\,dt = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^\infty (a_n^2 + b_n^2) = \sum_{n=-\infty}^\infty |c_n|^2$$

#### Interpretacja w teorii sygnałów:
Lewa strona równości Parsevala przedstawia **średnią moc całkowitą sygnału** okresowego wydzielaną na jednostkowej rezystancji (kwadrat wartości skutecznej $U_{\text{RMS}}^2$).  
Prawa strona to suma mocy składowej stałej $P_0 = |c_0|^2$ oraz mocy poszczególnych harmonicznych $P_n = 2|c_n|^2$.  
Tożsamość dowodzi zasady zachowania energii: **całkowita energia sygnału w dziedzinie czasu jest dokładnie równa sumie energii jego składowych widmowych w dziedzinie częstotliwości**.

---

### 18.5. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 18.1 (Promień i przedział zbieżności szeregu potęgowego)
Wyznaczyć promień i przedział zbieżności szeregu:
$$\sum_{n=1}^\infty \frac{(x + 2)^n}{n \cdot 4^n}$$

**Rozwiązanie:**  
1. Środek szeregu: $x_0 = -2$. Współczynniki: $a_n = \frac{1}{n 4^n}$.
2. Promień zbieżności:
   $$R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right| = \lim_{n \to \infty} \frac{\frac{1}{n 4^n}}{\frac{1}{(n+1) 4^{n+1}}} = \lim_{n \to \infty} \frac{(n+1) 4^{n+1}}{n 4^n} = \lim_{n \to \infty} 4 \left( 1 + \frac{1}{n} \right) = 4$$
   Przedział otwarty zbieżności: $|x + 2| < 4 \iff -4 < x + 2 < 4 \iff x \in (-6, 2)$.
3. Badanie zbieżności na końcach przedziału:
   - Dla $x = 2$: $(x+2)^n = 4^n$. Szereg przyjmuje postać:
     $$\sum_{n=1}^\infty \frac{4^n}{n 4^n} = \sum_{n=1}^\infty \frac{1}{n}$$
     Jest to szereg harmoniczny rzędu 1, a więc **rozbieżny**.
   - Dla $x = -6$: $(x+2)^n = (-4)^n = (-1)^n 4^n$. Szereg przyjmuje postać:
     $$\sum_{n=1}^\infty \frac{(-1)^n 4^n}{n 4^n} = \sum_{n=1}^\infty \frac{(-1)^n}{n}$$
     Jest to szereg naprzemienny zbieżny na mocy kryterium Leibniza.
4. **Odpowiedź:** Promień zbieżności $R = 4$, przedział zbieżności: $[-6, 2)$.

---

#### Przykład 18.2 (Rozwinięcie w szereg Fouriera fali prostokątnej)
Rozwinąć w szereg Fouriera funkcję okresową o okresie $T = 2\pi$ zdefiniowaną na $[-\pi, \pi]$:
$$f(x) = \begin{cases} -1 & \text{dla } -\pi < x < 0 \\ 1 & \text{dla } 0 < x < \pi \end{cases}$$

**Rozwiązanie:**  
1. Funkcja jest **nieparzysta** ($f(-x) = -f(x)$), stąd $a_n = 0$ dla każdego $n \ge 0$.
2. Współczynniki $b_n$:
   $$b_n = \frac{2}{\pi} \int_0^\pi f(x) \sin(nx)\,dx = \frac{2}{\pi} \int_0^\pi 1 \cdot \sin(nx)\,dx = \frac{2}{\pi} \left[ -\frac{\cos(nx)}{n} \right]_0^\pi = \frac{2}{n\pi} (1 - \cos(n\pi))$$
   Ponieważ $\cos(n\pi) = (-1)^n$:
   $$1 - (-1)^n = \begin{cases} 0 & \text{dla } n \text{ parzystych } (n = 2k) \\ 2 & \text{dla } n \text{ nieparzystych } (n = 2k - 1) \end{cases}$$
   Zatem:
   $$b_{2k-1} = \frac{2}{(2k-1)\pi} \cdot 2 = \frac{4}{\pi(2k-1)}, \quad b_{2k} = 0$$
3. Szereg Fouriera:
   $$S_f(x) = \frac{4}{\pi} \sum_{k=1}^\infty \frac{\sin\big((2k-1)x\big)}{2k - 1} = \frac{4}{\pi} \left( \sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \dots \right)$$

---

#### Przykład 18.3 (Rozwiązanie problemu bazylejskiego za pomocą szeregu Fouriera)
Rozwinąć funkcję $f(x) = x^2$ na $[-\pi, \pi]$ w szereg Fouriera i wyznaczyć sumę szeregu $\sum_{n=1}^\infty \frac{1}{n^2}$.

**Rozwiązanie:**  
1. Funkcja $f(x) = x^2$ jest **parzysta**, więc $b_n = 0$ dla każdego $n \ge 1$.
2. Współczynniki $a_n$:
   $$a_0 = \frac{2}{\pi} \int_0^\pi x^2\,dx = \frac{2}{\pi} \left[ \frac{x^3}{3} \right]_0^\pi = \frac{2\pi^2}{3}$$
   Dla $n \ge 1$ całkujemy dwukrotnie przez części:
   $$a_n = \frac{2}{\pi} \int_0^\pi x^2 \cos(nx)\,dx = \frac{2}{\pi} \left( \left[ \frac{x^2 \sin(nx)}{n} \right]_0^\pi - \int_0^\pi \frac{2x \sin(nx)}{n}\,dx \right)$$
   Składnik w granicach znika ($\sin(n\pi) = 0$). Całkując drugi składnik przez części:
   $$a_n = -\frac{4}{n\pi} \int_0^\pi x \sin(nx)\,dx = -\frac{4}{n\pi} \left( \left[ -\frac{x \cos(nx)}{n} \right]_0^\pi + \int_0^\pi \frac{\cos(nx)}{n}\,dx \right)$$
   $$= -\frac{4}{n\pi} \left( -\frac{\pi \cos(n\pi)}{n} + 0 \right) = \frac{4 \cos(n\pi)}{n^2} = \frac{4(-1)^n}{n^2}$$
3. Szereg Fouriera:
   $$x^2 = \frac{a_0}{2} + \sum_{n=1}^\infty a_n \cos(nx) = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n}{n^2} \cos(nx)$$
4. Podstawiając $x = \pi$ (punkt ciągłości):
   $$\pi^2 = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n}{n^2} \cos(n\pi) = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{(-1)^n (-1)^n}{n^2} = \frac{\pi^2}{3} + 4 \sum_{n=1}^\infty \frac{1}{n^2}$$
   Odejmując $\frac{\pi^2}{3}$:
   $$\frac{2\pi^2}{3} = 4 \sum_{n=1}^\infty \frac{1}{n^2} \implies \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$$
   Jest to słynny rezultat Leonharda Eulera z 1734 roku.

---

### 18.6. Zadania do samodzielnego rozwiązania

1. **Zadanie 18.1:** Wyznaczyć promień zbieżności szeregu $\sum_{n=0}^\infty \frac{(n!)^2}{(2n)!} x^n$.  
   *Odpowiedź:* $R = \lim \frac{a_n}{a_{n+1}} = \lim \frac{(2n+2)(2n+1)}{(n+1)^2} = 4$.

2. **Zadanie 18.2:** Rozwinąć w szereg potęgowy wokół $x_0 = 0$ funkcję $f(x) = \ln\left(\frac{1+x}{1-x}\right)$ i obliczyć sumę szeregu $\sum_{n=0}^\infty \frac{1}{(2n+1) 3^{2n+1}}$.  
   *Odpowiedź:* $f(x) = 2 \sum_{n=0}^\infty \frac{x^{2n+1}}{2n+1}$ dla $|x| < 1$. Dla $x = 1/3$: $f(1/3) = \ln(2)$, suma szeregu wynosi $\frac{1}{2}\ln 2$.

3. **Zadanie 18.3:** Rozwinąć w szereg Fouriera na $[-\pi, \pi]$ funkcję $f(x) = |x|$ (fala trójkątna).  
   *Odpowiedź:* Funkcja parzysta. $f(x) = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=1}^\infty \frac{\cos((2k-1)x)}{(2k-1)^2}$.

4. **Zadanie 18.4:** Korzystając z tożsamości Parsevala dla rozwinięcia $f(x) = x^2$ z Przykładu 18.3, obliczyć sumę szeregu $\sum_{n=1}^\infty \frac{1}{n^4}$.  
   *Odpowiedź:* $\frac{\pi^4}{90}$.

5. **Zadanie 18.5:** Wyznaczyć postać zespoloną szeregu Fouriera dla impulsu prostokątnego o amplitudzie $A$, szerokości $\tau$ i okresie $T$.  
   *Odpowiedź:* $c_n = \frac{A \tau}{T} \frac{\sin(n \omega_0 \tau / 2)}{n \omega_0 \tau / 2} = \frac{A \tau}{T} \operatorname{sinc}\left(\frac{n \omega_0 \tau}{2}\right)$.
