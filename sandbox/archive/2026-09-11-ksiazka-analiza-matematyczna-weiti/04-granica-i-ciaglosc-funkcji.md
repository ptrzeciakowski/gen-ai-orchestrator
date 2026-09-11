# Część IV: Granica i Ciągłość Funkcji Jednej Zmiennej

Pojęcie granicy funkcji oraz jej ciągłości stanowi pomost łączący dyskretny świat ciągów liczbowych ze światem wielkości ciągłych. W elektronice, automatyce i teorii sygnałów ciągłość opisuje naturalne procesy fizyczne, w których napięcia na pojemnościach i prądy w indukcyjnościach nie mogą zmieniać się w sposób nieskończenie szybki (prawa komutacji obwodów elektrycznych), podczas gdy punkty nieciągłości modelują idealne przełączenia kluczy półprzewodnikowych, dyskretyzację poziomów w przetwornikach analogowo-cyfrowych (ADC) oraz sygnały zegarowe w układach cyfrowych.

---

## Rozdział 7: Granica funkcji

### 7.1. Definicje Heinego i Cauchy'ego oraz ich równoważność

Niech funkcja rzeczywista $f: X \to \mathbb{R}$ będzie określona na podzbiorze $X \subset \mathbb{R}$. Niech punkt $x_0 \in \mathbb{R}$ będzie **punktem skupienia** zbioru $X$, co oznacza, że w każdym otoczeniu punktu $x_0$ znajduje się co najmniej jeden punkt zbioru $X$ różny od $x_0$:
$$\forall r > 0: \quad (X \setminus \{x_0\}) \cap (x_0 - r, x_0 + r) \neq \emptyset$$
Punkt $x_0$ sam nie musi należeć do dziedziny $X$ funkcji $f$.

#### Definicja 7.1 (Granica funkcji według Heinego – podejście ciągowe)
Liczbę $g \in \mathbb{R}$ nazywamy **granicą właściwą funkcji $f$ w punkcie $x_0$ według Heinego**, co zapisujemy:
$$\lim_{x \to x_0} f(x) = g$$
jeżeli dla każdego ciągu argumentów $(x_n)_{n=1}^\infty \subset X \setminus \{x_0\}$ zbieżnego do $x_0$, odpowiadający mu ciąg wartości funkcji $(f(x_n))_{n=1}^\infty$ jest zbieżny do $g$:
$$\forall_{(x_n) \subset X \setminus \{x_0\}} \quad \left( \lim_{n \to \infty} x_n = x_0 \implies \lim_{n \to \infty} f(x_n) = g \right)$$

#### Definicja 7.2 (Granica funkcji według Cauchy'ego – podejście otoczeniowe $\varepsilon-\delta$)
Liczbę $g \in \mathbb{R}$ nazywamy **granicą właściwą funkcji $f$ w punkcie $x_0$ według Cauchy'ego**, jeżeli dla każdej liczby $\varepsilon > 0$ istnieje liczba $\delta > 0$ taka, że dla wszystkich argumentów $x \in X$, których odległość od $x_0$ jest dodatnia i mniejsza od $\delta$, odległość wartości $f(x)$ od $g$ jest mniejsza od $\varepsilon$:
$$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad \big( 0 < |x - x_0| < \delta \implies |f(x) - g| < \varepsilon \big)$$

#### Granice w nieskończoności oraz granice niewłaściwe:
1. **Granica w nieskończoności $\lim_{x \to +\infty} f(x) = g$ (Cauchy):**
   $$\forall_{\varepsilon > 0} \exists_{M > 0} \forall_{x \in X} \quad (x > M \implies |f(x) - g| < \varepsilon)$$
2. **Granica w minus nieskończoności $\lim_{x \to -\infty} f(x) = g$ (Cauchy):**
   $$\forall_{\varepsilon > 0} \exists_{M > 0} \forall_{x \in X} \quad (x < -M \implies |f(x) - g| < \varepsilon)$$
3. **Granica niewłaściwa $\lim_{x \to x_0} f(x) = +\infty$:**
   $$\forall_{E > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (0 < |x - x_0| < \delta \implies f(x) > E)$$
4. **Granica niewłaściwa $\lim_{x \to x_0} f(x) = -\infty$:**
   $$\forall_{E > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (0 < |x - x_0| < \delta \implies f(x) < -E)$$

> **Twierdzenie 7.1 (O równoważności definicji Heinego i Cauchy'ego):**  
> Definicja Heinego i definicja Cauchy'ego granicy funkcji w punkcie są logicznie równoważne:
> $$\lim_{x \to x_0}^{\text{Heine}} f(x) = g \iff \lim_{x \to x_0}^{\text{Cauchy}} f(x) = g$$

**Dowód:**  
1. **Implikacja $(\implies)$ (Dowód nie wprost):**  
   Załóżmy, że zachodzi warunek Heinego, lecz nie zachodzi warunek Cauchy'ego.  
   Negacja warunku Cauchy'ego ma postać:
   $$\exists_{\varepsilon_0 > 0} \forall_{\delta > 0} \exists_{x \in X} \quad \big( 0 < |x - x_0| < \delta \land |f(x) - g| \ge \varepsilon_0 \big)$$
   Dla każdej liczby naturalnej $n \in \mathbb{N}$ dobierzmy $\delta_n = \frac{1}{n}$. Z powyższego zaprzeczenia wynika istnienie punktu $x_n \in X \setminus \{x_0\}$ takiego, że:
   $$0 < |x_n - x_0| < \frac{1}{n} \quad \text{oraz} \quad |f(x_n) - g| \ge \varepsilon_0$$
   Zauważmy, że ciąg $(x_n)$ jest zbieżny do $x_0$ (gdyż $|x_n - x_0| < 1/n \to 0$). Jednak odpowiadający mu ciąg wartości $f(x_n)$ nie dąży do $g$, ponieważ każdy jego wyraz jest oddalony od $g$ o co najmniej $\varepsilon_0 > 0$. Przeczy to założeniu o spełnieniu warunku Heinego. Zatem z warunku Heinego wynika warunek Cauchy'ego.

2. **Implikacja $(\impliedby)$:**  
   Załóżmy warunek Cauchy'ego i weźmy dowolny ciąg $(x_n) \subset X \setminus \{x_0\}$ zbieżny do $x_0$.  
   Dla ustalonego $\varepsilon > 0$ dobieramy $\delta > 0$ z warunku Cauchy'ego. Ponieważ $\lim_{n \to \infty} x_n = x_0$, z definicji granicy ciągu istnieje wskaźnik $N \in \mathbb{N}$ taki, że dla wszystkich $n > N$:
   $$0 < |x_n - x_0| < \delta$$
   Z warunku Cauchy'ego wynika wówczas natychmiast, że dla każdego $n > N$:
   $$|f(x_n) - g| < \varepsilon$$
   Dowodzi to, że $\lim_{n \to \infty} f(x_n) = g$. $\blacksquare$

---

### 7.2. Granice jednostronne i kryterium istnienia granicy

W wielu zagadnieniach fizycznych zachowanie funkcji z lewej i prawej strony punktu jest diametralnie różne (np. napięcie na diodzie Zenera przed i po przekroczeniu napięcia przebicia).

#### Definicja 7.3 (Granice jednostronne)
1. **Granica lewostronna** (oznaczana $\lim_{x \to x_0^-} f(x)$ lub $f(x_0^-$)):
   $$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (x_0 - \delta < x < x_0 \implies |f(x) - g_L| < \varepsilon)$$
2. **Granica prawostronna** (oznaczana $\lim_{x \to x_0^+} f(x)$ lub $f(x_0^+)$)):
   $$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (x_0 < x < x_0 + \delta \implies |f(x) - g_P| < \varepsilon)$$

> **Twierdzenie 7.2 (Warunek konieczny i dostateczny istnienia granicy obustronnej):**  
> Granica właściwa $\lim_{x \to x_0} f(x)$ istnieje wtedy i tylko wtedy, gdy istnieją obie skończone granice jednostronne i są sobie równe:
> $$\lim_{x \to x_0} f(x) = g \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = g$$

---

### 7.3. Arytmetyka granic i twierdzenia o szacowaniu

> **Twierdzenie 7.3 (Twierdzenie o działaniach na granicach funkcji):**  
> Jeżeli $\lim_{x \to x_0} f(x) = A$ oraz $\lim_{x \to x_0} g(x) = B$ ($A, B \in \mathbb{R}$), to:
> 1. $\lim_{x \to x_0} \big( f(x) \pm g(x) \big) = A \pm B$,
> 2. $\lim_{x \to x_0} \big( f(x) \cdot g(x) \big) = A \cdot B$,
> 3. $\lim_{x \to x_0} \frac{f(x)}{g(x)} = \frac{A}{B} \quad (\text{o ile } B \neq 0)$,
> 4. Jeżeli $f(x) > 0$ w otoczeniu $x_0$ oraz $A > 0$, to $\lim_{x \to x_0} [f(x)]^{g(x)} = A^B$.

> **Twierdzenie 7.4 (Twierdzenie o trzech funkcjach):**  
> Jeżeli w pewnym sąsiedztwie $S(x_0, \delta)$ spełniony jest warunek:
> $$f(x) \le g(x) \le h(x)$$
> oraz:
> $$\lim_{x \to x_0} f(x) = \lim_{x \to x_0} h(x) = K$$
> to istnieje granica $\lim_{x \to x_0} g(x)$ i zachodzi równość:
> $$\lim_{x \to x_0} g(x) = K$$

> **Twierdzenie 7.5 (Twierdzenie o dwóch funkcjach dla granic niewłaściwych):**  
> 1. Jeżeli $f(x) \le g(x)$ w sąsiedztwie $x_0$ oraz $\lim_{x \to x_0} f(x) = +\infty$, to $\lim_{x \to x_0} g(x) = +\infty$.
> 2. Jeżeli $g(x) \le f(x)$ w sąsiedztwie $x_0$ oraz $\lim_{x \to x_0} f(x) = -\infty$, to $\lim_{x \to x_0} g(x) = -\infty$.

---

### 7.4. Kanoniczne granice wyrażeń nieoznaczonych

Wyprowadzenie granic kanonicznych leży u podstaw wyznaczania pochodnych wszystkich funkcji elementarnych bez stosowania reguły de l'Hospitala (której użycie w tym miejscu stanowiłoby błąd logiczny *circulus in probando*).

> **Twierdzenie 7.6 (Fundamentalna granica trygonometryczna):**  
> $$\lim_{x \to 0} \frac{\sin x}{x} = 1$$

**Dowód geometryczny:**  
Rozpatrzmy koło jednostkowe ($R = 1$) na płaszczyźnie kartezjańskiej. Dla kąta $x \in \left(0, \frac{\pi}{2}\right)$ porównajmy pola trzech figur geometrycznych:
1. Trójkąt $OAB$ o wierzchołkach $(0,0)$, $(1,0)$ i $(\cos x, \sin x)$: pole wynosi $P_1 = \frac{1}{2} \cdot 1 \cdot \sin x = \frac{1}{2} \sin x$.
2. Wycinek koła jednostkowego o kącie środkowym $x$: pole wynosi $P_2 = \frac{1}{2} R^2 x = \frac{1}{2} x$.
3. Trójkąt prostokątny $OAC$ o wierzchołkach $(0,0)$, $(1,0)$ i $(1, \operatorname{tg} x)$: pole wynosi $P_3 = \frac{1}{2} \cdot 1 \cdot \operatorname{tg} x = \frac{1}{2} \operatorname{tg} x$.

Z inkluzji geometrycznej $P_1 < P_2 < P_3$:
$$\frac{1}{2} \sin x < \frac{1}{2} x < \frac{1}{2} \operatorname{tg} x \iff \sin x < x < \frac{\sin x}{\cos x}$$
Dzieląc obustronnie przez $\sin x > 0$:
$$1 < \frac{x}{\sin x} < \frac{1}{\cos x} \iff \cos x < \frac{\sin x}{x} < 1$$
Ponieważ funkcja $\cos x$ oraz $\frac{\sin x}{x}$ są parzyste, nierówność ta zachodzi również dla $x \in \left(-\frac{\pi}{2}, 0\right)$.  
Przechodząc do granicy przy $x \to 0$: ponieważ $\lim_{x \to 0} \cos x = 1$, na mocy twierdzenia o trzech funkcjach otrzymujemy:
$$\lim_{x \to 0} \frac{\sin x}{x} = 1 \quad \blacksquare$$

> **Twierdzenie 7.7 (Kanon granic nieoznaczonych):**  
> 1. $\lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$
> 2. $\lim_{x \to 0} \frac{e^x - 1}{x} = 1, \quad \lim_{x \to 0} \frac{a^x - 1}{x} = \ln a \quad (a > 0)$
> 3. $\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1, \quad \lim_{x \to 0} \frac{\log_a(1 + x)}{x} = \frac{1}{\ln a}$
> 4. $\lim_{x \to 0} \frac{(1 + x)^\alpha - 1}{x} = \alpha \quad (\alpha \in \mathbb{R})$
> 5. $\lim_{x \to 0} \frac{\arcsin x}{x} = 1, \quad \lim_{x \to 0} \frac{\operatorname{arctg} x}{x} = 1$
> 6. $\lim_{x \to 0} \frac{\operatorname{sh} x}{x} = 1, \quad \lim_{x \to 0} \frac{\operatorname{ch} x - 1}{x^2} = \frac{1}{2}$

**Dowód punktu 3 ($\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$):**  
Korzystając z ciągłości funkcji logarytmicznej oraz definicji liczby $e = \lim_{u \to \infty} (1 + 1/u)^u$:
$$\lim_{x \to 0} \frac{\ln(1 + x)}{x} = \lim_{x \to 0} \ln\left( (1 + x)^{1/x} \right) = \ln\left( \lim_{x \to 0} (1 + x)^{1/x} \right) = \ln(e) = 1 \quad \blacksquare$$

---

### 7.5. Skale asymptotyczne, symbole Landaua i złożoność obliczeniowa

W teorii algorytmów, przetwarzaniu sygnałów i analizie numerycznej precyzyjne tempo wzrostu lub zaniku funkcji w otoczeniu punktu lub w nieskończoności opisuje się aparatem **symboli Landaua**.

#### Definicja 7.4 (Symbole asymptotyczne Landaua)
Niech $f, g$ będą określone w sąsiedztwie punktu $x_0$ (lub dla $x \to \infty$).
1. **$f(x) = O(g(x))$ przy $x \to x_0$ ("duże O"):**  
   Istnieją stałe $M > 0$ oraz $\delta > 0$ takie, że dla $0 < |x - x_0| < \delta$:
   $$|f(x)| \le M |g(x)|$$
   (iloraz $\frac{|f(x)|}{|g(x)|}$ jest ograniczony).
2. **$f(x) = o(g(x))$ przy $x \to x_0$ ("małe o"):**  
   $$\lim_{x \to x_0} \frac{f(x)}{g(x)} = 0$$
   (funkcja $f$ zmierza do zera szybciej niż funkcja $g$).
3. **Równoważność asymptotyczna $f(x) \sim g(x)$ przy $x \to x_0$:**  
   $$\lim_{x \to x_0} \frac{f(x)}{g(x)} = 1 \iff f(x) = g(x) + o(g(x))$$

#### Przykłady równoważności asymptotycznych przy $x \to 0$:
$$\sin x \sim x, \quad \operatorname{tg} x \sim x, \quad \arcsin x \sim x, \quad \operatorname{arctg} x \sim x$$
$$e^x - 1 \sim x, \quad \ln(1 + x) \sim x, \quad 1 - \cos x \sim \frac{1}{2} x^2, \quad \sqrt{1 + x} - 1 \sim \frac{1}{2} x$$
Reguła ta pozwala na natychmiastowe upraszczanie czynników iloczynowych w granicach skomplikowanych wyrażeń!

---

## Rozdział 8: Ciągłość funkcji

### 8.1. Definicja ciągłości i taksonomia punktów nieciągłości

#### Definicja 8.1 (Ciągłość funkcji w punkcie)
Niech funkcja $f: X \to \mathbb{R}$ będzie określona w otoczeniu punktu $x_0 \in X$. Funkcja $f$ jest **ciągła w punkcie $x_0$**, jeżeli:
$$\lim_{x \to x_0} f(x) = f(x_0)$$
W języku Cauchy'ego ($\varepsilon-\delta$):
$$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (|x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon)$$
Funkcja jest ciągła na zbiorze $A \subset X$, jeżeli jest ciągła w każdym punkcie tego zbioru.

#### Klasyfikacja punktów nieciągłości:
Punkt $x_0$ nazywamy punktem nieciągłości funkcji $f$, jeżeli funkcja nie jest w nim ciągła (nie istnieje granica, granica jest nieskończona lub granica jest różna od wartości $f(x_0)$).

1. **Nieciągłość usuwalna:**  
   Istnieje granica właściwa $\lim_{x \to x_0} f(x) = g$, lecz funkcja nie jest określona w $x_0$ lub $f(x_0) \neq g$.  
   *Przykład:* $f(x) = \frac{\sin x}{x}$ dla $x \neq 0$. Kładąc $f(0) = 1$, otrzymujemy funkcję ciągłą na całym $\mathbb{R}$.

2. **Nieciągłość I rodzaju (skokowa / nieusuwalna):**  
   Istnieją obie granice jednostronne skończone, lecz są różne:
   $$f(x_0^-) \neq f(x_0^+)$$
   Wielkość $s = f(x_0^+) - f(x_0^-)$ nazywamy **skokiem funkcji** w punkcie $x_0$.  
   *Przykład inżynierski:* Funkcja skoku jednostkowego Heaviside'a:
   $$\mathbf{1}(t) = \begin{cases} 0 & \text{dla } t < 0 \\ 1 & \text{dla } t \ge 0 \end{cases}$$
   W punkcie $t = 0$: $\mathbf{1}(0^-) = 0$, $\mathbf{1}(0^+) = 1$, skok wynosi $s = 1$.

3. **Nieciągłość II rodzaju:**  
   Co najmniej jedna z granic jednostronnych $f(x_0^-)$ lub $f(x_0^+)$ nie istnieje lub jest nieskończona ($\pm\infty$).  
   - *Osobliwość asymptotyczna:* $f(x) = \frac{1}{x}$ w $x_0 = 0$ ($f(0^-) = -\infty, f(0^+) = +\infty$).
   - *Osobliwość oscylacyjna:* $f(x) = \sin\left(\frac{1}{x}\right)$ w $x_0 = 0$ (granice jednostronne w ogóle nie istnieją, funkcja oscyluje nieskończenie gęsto w przedziale $[-1, 1]$).

---

### 8.2. Własności funkcji ciągłych na przedziale zwartym

Przedział domknięty i ograniczony $[a, b]$ jest zbiorem zwartym w $\mathbb{R}$. Funkcje ciągłe na zbiorach zwartych posiadają fundamentalne własności geometryczne.

> **Twierdzenie 8.1 (I Twierdzenie Weierstrassa o ograniczoności):**  
> Każda funkcja ciągła na przedziale domkniętym $[a, b]$ jest ograniczona:
> $$\exists_{m, M \in \mathbb{R}} \forall_{x \in [a, b]} \quad m \le f(x) \le M$$

**Dowód (nie wprost):**  
Załóżmy, że funkcja $f$ nie jest ograniczona z góry. Wtedy dla każdego $n \in \mathbb{N}$ istnieje punkt $x_n \in [a, b]$ taki, że $f(x_n) > n$.  
Ciąg $(x_n) \subset [a, b]$ jest ograniczony. Na mocy Twierdzenia Bolzano-Weierstrassa istnieje podciąg $(x_{k_n})$ zbieżny do pewnego punktu $x_0 \in [a, b]$.  
Z ciągłości funkcji $f$ w punkcie $x_0$ (definicja Heinego):
$$\lim_{n \to \infty} f(x_{k_n}) = f(x_0) \in \mathbb{R}$$
Lecz z konstrukcji $f(x_{k_n}) > k_n \to \infty$, skąd $\lim f(x_{k_n}) = +\infty$.  
Sprzeczność ta dowodzi, że funkcja musi być ograniczona z góry. Analogicznie dowodzi się ograniczenia z dołu. $\blacksquare$

> **Twierdzenie 8.2 (II Twierdzenie Weierstrassa o osiąganiu kresów):**  
> Jeżeli funkcja $f$ jest ciągła na przedziale domkniętym $[a, b]$, to osiąga w nim swój kres górny i kres dolny:
> $$\exists_{x_{\min}, x_{\max} \in [a, b]} \quad f(x_{\min}) = \inf_{x \in [a, b]} f(x) = \min_{x \in [a, b]} f(x), \quad f(x_{\max}) = \sup_{x \in [a, b]} f(x) = \max_{x \in [a, b]} f(x)$$

> **Twierdzenie 8.3 (Bolzano-Cauchy'ego o wartości pośredniej / Własność Darboux):**  
> Jeżeli funkcja $f: [a, b] \to \mathbb{R}$ jest ciągła oraz $f(a) \neq f(b)$, to dla dowolnej liczby $w$ leżącej ściśle pomiędzy $f(a)$ i $f(b)$ istnieje co najmniej jeden punkt $c \in (a, b)$ taki, że:
> $$f(c) = w$$

**Dowód (metodą bisekcji przedziałów):**  
Załóżmy bez straty ogólności, że $f(a) < w < f(b)$. Rozpatrzmy funkcję pomocniczą $g(x) = f(x) - w$.  
Wtedy $g(a) < 0$ oraz $g(b) > 0$. Poszukujemy punktu $c$ takiego, że $g(c) = 0$.  
Konstruujemy ciąg zstępujących przedziałów domkniętych $I_n = [a_n, b_n]$:
1. Kładziemy $I_1 = [a_1, b_1] = [a, b]$.
2. W $n$-tym kroku wyznaczamy środek przedziału $c_n = \frac{a_n + b_n}{2}$:
   - Jeżeli $g(c_n) = 0$, kładziemy $c = c_n$ i dowód jest zakończony.
   - Jeżeli $g(c_n) < 0$, kładziemy $I_{n+1} = [c_n, b_n]$.
   - Jeżeli $g(c_n) > 0$, kładziemy $I_{n+1} = [a_n, c_n]$.

W każdym kroku spełniony jest warunek $g(a_n) < 0$ oraz $g(b_n) > 0$, a długość przedziału wynosi $|I_n| = \frac{b - a}{2^{n-1}} \xrightarrow[n\to\infty]{} 0$.  
Z zasady zstępujących przedziałów Cantora przekrój $\bigcap_{n=1}^\infty I_n$ zawiera dokładnie jeden punkt $c \in [a, b]$, do którego zbieżne są oba ciągi: $\lim a_n = \lim b_n = c$.  
Z ciągłości funkcji $g$:
$$g(c) = \lim_{n \to \infty} g(a_n) \le 0 \quad \text{oraz} \quad g(c) = \lim_{n \to \infty} g(b_n) \ge 0$$
Stąd wynika, że $g(c) = 0 \iff f(c) = w$. $\blacksquare$

#### Zastosowanie inżynierskie: Metoda bisekcji lokalizacji zer nieliniowych
Twierdzenie Bolzano-Cauchy'ego stanowi podstawę algorytmu bisekcji (połowienia przedziału) do numerycznego znajdowania punktów pracy obwodów nieliniowych i pierwiastków równań przestępnych. Każda iteracja zmniejsza niepewność położenia pierwiastka o połowę, dając zbieżność geometryczną z błędem $\varepsilon_n = \frac{b-a}{2^n}$.

---

### 8.3. Ciągłość jednostajna i twierdzenie Cantora

#### Definicja 8.2 (Ciągłość jednostajna)
Funkcję $f: X \to \mathbb{R}$ nazywamy **jednostajnie ciągłą** na zbiorze $X$, jeżeli promień $\delta$ w warunku Cauchy'ego zależy wyłącznie od $\varepsilon$, a nie od położenia punktu w dziedzinie:
$$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x_1, x_2 \in X} \quad \big( |x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \varepsilon \big)$$

> **Twierdzenie 8.4 (Cantora o ciągłości jednostajnej):**  
> Każda funkcja ciągła na przedziale domkniętym $[a, b]$ jest na nim jednostajnie ciągła.

#### Warunek Lipschitza:
Jeżeli funkcja $f: X \to \mathbb{R}$ spełnia warunek:
$$\exists L > 0 \forall x_1, x_2 \in X: \quad |f(x_1) - f(x_2)| \le L |x_1 - x_2|$$
to funkcję nazywamy **lipschitzowską** ze stałą $L$. Każda funkcja spełniająca warunek Lipschitza jest jednostajnie ciągła (wystarczy przyjąć $\delta = \varepsilon / L$). Jeżeli dodatkowo $L < 1$, funkcja jest **odwzorowaniem zwężającym (kontrakcją)**.

> **Twierdzenie 8.5 (Banacha o punkcie stałym dla prostej):**  
> Niech $f: [a, b] \to [a, b]$ będzie kontrakcją ze stałą $L < 1$. Wówczas:
> 1. Istnieje dokładnie jeden punkt stały $x^* \in [a, b]$ taki, że $f(x^*) = x^*$.
> 2. Ciąg kolejnych przybliżeń $x_{n+1} = f(x_n)$ jest zbieżny do $x^*$ dla dowolnego punktu startowego $x_0 \in [a, b]$, przy czym błąd szacuje się nierównością:
>    $$|x_n - x^*| \le \frac{L^n}{1 - L} |x_1 - x_0|$$

---

### 8.4. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 8.1 (Granica z funkcjami cyklometrycznymi)
Obliczyć granicę:
$$\lim_{x \to 0} \frac{\operatorname{arcsin}(3x) - \operatorname{arctg}(2x)}{x \cos(5x)}$$

**Rozwiązanie:**  
Mamy symbol nieoznaczony $\left[\frac{0}{0}\right]$. Rozbijamy wyrażenie:
$$\frac{\operatorname{arcsin}(3x) - \operatorname{arctg}(2x)}{x \cos(5x)} = \frac{1}{\cos(5x)} \left( \frac{\operatorname{arcsin}(3x)}{x} - \frac{\operatorname{arctg}(2x)}{x} \right)$$
Korzystając z granic kanonicznych:
$$\frac{\operatorname{arcsin}(3x)}{x} = 3 \cdot \frac{\operatorname{arcsin}(3x)}{3x} \xrightarrow[x \to 0]{} 3 \cdot 1 = 3$$
$$\frac{\operatorname{arctg}(2x)}{x} = 2 \cdot \frac{\operatorname{arctg}(2x)}{2x} \xrightarrow[x \to 0]{} 2 \cdot 1 = 2$$
Ponadto $\lim_{x \to 0} \cos(5x) = \cos(0) = 1$. Stąd:
$$\lim_{x \to 0} \frac{\operatorname{arcsin}(3x) - \operatorname{arctg}(2x)}{x \cos(5x)} = \frac{1}{1} (3 - 2) = 1$$

---

#### Przykład 8.2 (Granica z różnicą pierwiastków sześciennych)
Obliczyć granicę przy $x \to +\infty$:
$$\lim_{x \to +\infty} x^{3/2} \left( \sqrt{x^3 + 1} - \sqrt{x^3 - 1} \right)$$

**Rozwiązanie:**  
Mamy symbol $[\infty \cdot 0]$. Mnożymy przez sprzężenie sumy pierwiastków:
$$\sqrt{x^3 + 1} - \sqrt{x^3 - 1} = \frac{(x^3 + 1) - (x^3 - 1)}{\sqrt{x^3 + 1} + \sqrt{x^3 - 1}} = \frac{2}{\sqrt{x^3 + 1} + \sqrt{x^3 - 1}}$$
Wstawiając do granicy:
$$\lim_{x \to +\infty} \frac{2 x^{3/2}}{\sqrt{x^3 + 1} + \sqrt{x^3 - 1}} = \lim_{x \to +\infty} \frac{2 x^{3/2}}{x^{3/2} \left( \sqrt{1 + 1/x^3} + \sqrt{1 - 1/x^3} \right)} = \frac{2}{\sqrt{1} + \sqrt{1}} = \frac{2}{2} = 1$$

---

#### Przykład 8.3 (Granica typu potęgowego $[1^\infty]$)
Obliczyć granicę:
$$\lim_{x \to 0} \left( \frac{1 + \operatorname{tg} x}{1 + \sin x} \right)^{1/x^3}$$

**Rozwiązanie:**  
Symbol $[1^\infty]$. Korzystamy z tożsamości $u^v = \exp(v \ln u)$:
$$L = \lim_{x \to 0} \frac{1}{x^3} \ln\left( \frac{1 + \operatorname{tg} x}{1 + \sin x} \right) = \lim_{x \to 0} \frac{1}{x^3} \ln\left( 1 + \frac{\operatorname{tg} x - \sin x}{1 + \sin x} \right)$$
Ponieważ $\frac{\operatorname{tg} x - \sin x}{1 + \sin x} \to 0$, korzystamy z faktu $\ln(1 + u) \sim u$:
$$L = \lim_{x \to 0} \frac{1}{x^3} \cdot \frac{\operatorname{tg} x - \sin x}{1 + \sin x} = \lim_{x \to 0} \frac{\sin x \left( \frac{1}{\cos x} - 1 \right)}{x^3 (1 + \sin x)} = \lim_{x \to 0} \frac{\sin x (1 - \cos x)}{x^3 \cos x (1 + \sin x)}$$
Rozdzielamy na iloczyn granic kanonicznych:
$$L = \lim_{x \to 0} \left( \frac{\sin x}{x} \right) \cdot \left( \frac{1 - \cos x}{x^2} \right) \cdot \frac{1}{\cos x (1 + \sin x)} = 1 \cdot \frac{1}{2} \cdot \frac{1}{1(1 + 0)} = \frac{1}{2}$$
Zatem wyjściowa granica wynosi:
$$\lim_{x \to 0} \left( \frac{1 + \operatorname{tg} x}{1 + \sin x} \right)^{1/x^3} = e^{1/2} = \sqrt{e}$$

---

#### Przykład 8.4 (Dobór parametrów ciągłości dla funkcji sklejanej)
Wyznaczyć parametry $p, q \in \mathbb{R}$, dla których funkcja jest ciągła na całym $\mathbb{R}$:
$$f(x) = \begin{cases}
\frac{e^{3x} - 1}{\sin(2x)} & \text{dla } x < 0 \\
p x + q & \text{dla } 0 \le x \le 1 \\
\frac{\sqrt{x} - 1}{x^2 - 1} & \text{dla } x > 1
\end{cases}$$

**Rozwiązanie:**  
1. **Ciągłość w $x_0 = 0$:**
   - Wartość: $f(0) = q$.
   - Granica prawostronna: $\lim_{x \to 0^+} f(x) = q$.
   - Granica lewostronna:
     $$\lim_{x \to 0^-} \frac{e^{3x} - 1}{\sin(2x)} = \lim_{x \to 0^-} \left( \frac{e^{3x} - 1}{3x} \cdot \frac{2x}{\sin(2x)} \cdot \frac{3}{2} \right) = 1 \cdot 1 \cdot \frac{3}{2} = \frac{3}{2}$$
   Warunek ciągłości $f(0^-) = f(0^+) = f(0)$ daje: $q = \frac{3}{2}$.

2. **Ciągłość w $x_1 = 1$:**
   - Wartość: $f(1) = p(1) + q = p + \frac{3}{2}$.
   - Granica lewostronna: $\lim_{x \to 1^-} f(x) = p + \frac{3}{2}$.
   - Granica prawostronna:
     $$\lim_{x \to 1^+} \frac{\sqrt{x} - 1}{x^2 - 1} = \lim_{x \to 1^+} \frac{\sqrt{x} - 1}{(x - 1)(x + 1)} = \lim_{x \to 1^+} \frac{\sqrt{x} - 1}{(\sqrt{x} - 1)(\sqrt{x} + 1)(x + 1)} = \lim_{x \to 1^+} \frac{1}{(\sqrt{x} + 1)(x + 1)}$$
     Podstawiając $x = 1$: $\frac{1}{(1 + 1)(1 + 1)} = \frac{1}{4}$.  
   Warunek ciągłości $f(1^-) = f(1^+)$ daje:
   $$p + \frac{3}{2} = \frac{1}{4} \implies p = \frac{1}{4} - \frac{6}{4} = -\frac{5}{4}$$
Funkcja jest ciągła na $\mathbb{R}$ dla $p = -\frac{5}{4}$ oraz $q = \frac{3}{2}$.

---

### 8.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 8.1:** Obliczyć granicę: $\lim_{x \to 0} \frac{\cos(3x) - \cos(7x)}{x^2}$.  
   *Odpowiedź:* 20. (Wzór na różnicę cosinusów: $\cos 3x - \cos 7x = 2\sin 5x \sin 2x$).

2. **Zadanie 8.2:** Obliczyć granicę: $\lim_{x \to 0} \frac{\ln(\cos x)}{x^2}$.  
   *Odpowiedź:* $-\frac{1}{2}$. (Przekształcenie: $\ln(1 + (\cos x - 1)) \sim \cos x - 1 \sim -\frac{1}{2}x^2$).

3. **Zadanie 8.3:** Obliczyć granicę jednostronną: $\lim_{x \to 0^+} x^{\sin x}$.  
   *Odpowiedź:* 1. ($\sin x \ln x \sim x \ln x \to 0 \implies e^0 = 1$).

4. **Zadanie 8.4:** Sklasyfikować punkty nieciągłości funkcji $f(x) = \frac{1}{1 + e^{1/x}}$ w punkcie $x_0 = 0$.  
   *Odpowiedź:* $f(0^+) = 0$, $f(0^-) = 1$. Nieciągłość I rodzaju (skokowa), skok $s = -1$.

5. **Zadanie 8.5:** Wykazać, że równanie $x \cdot 2^x = 1$ ma dokładnie jedno rozwiązanie w przedziale $(0, 1)$.  
   *Odpowiedź:* Funkcja $f(x) = x 2^x - 1$ jest ciągła, $f(0) = -1 < 0$, $f(1) = 1 > 0$, z twierdzenia Darboux ma pierwiastek; pochodna $f'(x) = 2^x(1 + x \ln 2) > 0$ oznacza ścisłą monotoniczność, stąd jedyność.

6. **Zadanie 8.6:** Zbadać jednostajną ciągłość funkcji $f(x) = \sin(x^2)$ na prostej $\mathbb{R}$.  
   *Odpowiedź:* Nie jest jednostajnie ciągła. Dla ciągów $x_n = \sqrt{n\pi + \pi/2}$, $y_n = \sqrt{n\pi}$ odległość $|x_n - y_n| \to 0$, lecz $|f(x_n) - f(y_n)| = 1$.
