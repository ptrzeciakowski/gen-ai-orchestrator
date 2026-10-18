# Część XII: Równania Różniczkowe Zwyczajne (ODE) w Elektronice i Informatyce

Równania różniczkowe zwyczajne stanowią fundament matematycznego modelowania dynamiki układów fizycznych. W elektrotechnice, elektronice i teorii sterowania prawa Kirchhoffa w połączeniu z relacjami konstytutywnymi elementów biernych ($u_R = R i$, $u_L = L \frac{di}{dt}$, $i_C = C \frac{du}{dt}$) prowadzą wprost do równań różniczkowych opisujących stany nieustalone w obwodach. Z kolei metoda transformaty Laplace'a pozwala na zamianę operacji różniczkowania i całkowania w dziedzinie czasu na algebraiczne działania w dziedzinie częstotliwości zespolonej $s$, co leży u podstaw syntezy filtrów analogowych i cyfrowych oraz analizy stabilności układów ze sprzężeniem zwrotnym.

---

## Rozdział 25: Równania różniczkowe rzędu pierwszego

### 25.1. Podstawowe pojęcia i twierdzenie o istnieniu i jedyności rozwiązania

#### Definicja 25.1 (Równanie różniczkowe zwyczajne I rzędu)
1. **Równaniem różniczkowym zwyczajnym I rzędu** nazywamy równanie postaci:
   $$F(x, y, y') = 0 \quad \text{lub w postaci normalnej (rozwikłanej):} \quad y' = f(x, y)$$
   gdzie $x$ jest zmienną niezależną, $y = y(x)$ jest funkcją niewiadomą, a $y' = \frac{dy}{dx}$ jej pochodną.
2. **Rozwiązaniem (całką)** równania w przedziale $(a, b)$ nazywamy każdą funkcję $\varphi: (a, b) \to \mathbb{R}$ różniczkowalną, która po podstawieniu do równania tożsamościowo spełnia to równanie: $\forall x \in (a, b): \varphi'(x) = f(x, \varphi(x))$.
3. **Rozwiązaniem ogólnym (CORZ)** nazywamy rodzinę funkcji $y = \varphi(x, C)$ zależną od parametru (stałej całkowania) $C \in \mathbb{R}$, opisującą wszystkie rozwiązania równania w zadanym obszarze.
4. **Rozwiązaniem szczególnym (CSRZ)** nazywamy konkretne rozwiązanie otrzymane z rozwiązania ogólnego przez ustalenie wartości stałej $C = C_0$.
5. **Zagadnieniem początkowym Cauchy'ego** nazywamy problem wyznaczenia rozwiązania równania $y' = f(x, y)$ spełniającego **warunek początkowy**:
   $$y(x_0) = y_0$$

> **Twierdzenie 25.1 (Picarda-Lindelöfa o istnieniu i jedyności rozwiązania):**  
> Niech funkcja $f(x, y)$ będzie ciągła w prostokącie $D = [x_0 - a, x_0 + a] \times [y_0 - b, y_0 + b]$ oraz spełnia warunek Lipschitza względem zmiennej $y$:
> $$\exists L > 0 \quad \forall (x, y_1), (x, y_2) \in D : \quad |f(x, y_1) - f(x, y_2)| \le L |y_1 - y_2|$$
> (w szczególności warunek ten jest spełniony, gdy pochodna cząstkowa $\frac{\partial f}{\partial y}$ jest ciągła i ograniczona w $D$).  
> Wówczas zagadnienie Cauchy'ego $y' = f(x, y), y(x_0) = y_0$ posiada **dokładnie jedno** rozwiązanie zdefiniowane w pewnym otoczeniu punktu $x_0$.

---

### 25.2. Równania o zmiennych rozdzielonych

#### Definicja 25.2 (Równanie o zmiennych rozdzielonych)
Równaniem o zmiennych rozdzielonych nazywamy równanie postaci:
$$\frac{dy}{dx} = g(x) \cdot h(y)$$
gdzie $g$ jest ciągła na $(a, b)$, a $h$ ciągła na $(c, d)$.

#### Algorytm rozwiązywania:
1. Jeżeli $h(y) \neq 0$, rozdzielamy zmienne:
   $$\frac{1}{h(y)}\,dy = g(x)\,dx$$
2. Całkujemy obie strony tożsamości:
   $$\int \frac{1}{h(y)}\,dy = \int g(x)\,dx + C$$
3. Wyznaczamy funkcję $y(x)$ (postać jawna lub uwikłana).
4. Badamy miejsca zerowe funkcji $h(y) = 0$: jeżeli $h(y_k) = 0$, to funkcja stała $y(x) \equiv y_k$ jest również rozwiązaniem równania (może być to rozwiązanie osobliwe lub szczególne zawarte w CORZ dla pewnego $C$).

---

### 25.3. Równania liniowe rzędu pierwszego

#### Definicja 25.3 (Równanie liniowe I rzędu)
Równaniem różniczkowym liniowym I rzędu nazywamy równanie:
$$y' + p(x) y = q(x)$$
gdzie $p(x)$ i $q(x)$ są funkcjami ciągłymi na przedziale $(a, b)$.  
Gdy $q(x) \equiv 0$, równanie nazywamy **jednorodnym (RLJ)**, w przeciwnym razie – **niejednorodnym (RLN)**.

#### Metoda rozwiązywania RLJ:
$$y' + p(x) y = 0 \implies \frac{dy}{y} = -p(x)\,dx \implies \ln |y| = -\int p(x)\,dx + C_1$$
Rozwiązanie ogólne równania jednorodnego (CORJ):
$$y_0(x) = C e^{-\int p(x)\,dx}, \quad C \in \mathbb{R}$$

#### Metoda uzmienniania stałej Lagrange'a dla RLN:
Poszukujemy rozwiązania równania niejednorodnego w postaci:
$$y(x) = C(x) e^{-\int p(x)\,dx}$$
Różniczkując:
$$y'(x) = C'(x) e^{-\int p(x)\,dx} - C(x) p(x) e^{-\int p(x)\,dx}$$
Wstawiając do równania $y' + p(x) y = q(x)$:
$$C'(x) e^{-\int p(x)\,dx} - C(x) p(x) e^{-\int p(x)\,dx} + p(x) C(x) e^{-\int p(x)\,dx} = q(x)$$
Wyrazy zawierające $C(x)$ redukują się tożsamościowo, dając:
$$C'(x) = q(x) e^{\int p(x)\,dx} \implies C(x) = \int q(x) e^{\int p(x)\,dx}\,dx + C$$
Ostateczne rozwiązanie ogólne równania niejednorodnego (CORN):
$$y(x) = e^{-\int p(x)\,dx} \left( \int q(x) e^{\int p(x)\,dx}\,dx + C \right)$$

---

### 25.4. Równanie Bernoulliego

#### Definicja 25.4 (Równanie Bernoulliego)
Równaniem Bernoulliego nazywamy równanie nieliniowe postaci:
$$y' + p(x) y = q(x) y^\alpha \quad (\alpha \in \mathbb{R}, \; \alpha \neq 0, \; \alpha \neq 1)$$

#### Algorytm sprowadzania do równania liniowego:
1. Dzielimy obie strony równania przez $y^\alpha$:
   $$y^{-\alpha} y' + p(x) y^{1-\alpha} = q(x)$$
2. Wprowadzamy nową funkcję niewiadomą:
   $$z(x) = y^{1-\alpha}$$
   Jej pochodna wynosi:
   $$z' = (1 - \alpha) y^{-\alpha} y' \implies y^{-\alpha} y' = \frac{z'}{1 - \alpha}$$
3. Wstawiając do równania:
   $$\frac{z'}{1 - \alpha} + p(x) z = q(x) \iff z' + (1 - \alpha) p(x) z = (1 - \alpha) q(x)$$
   Otrzymujemy liniowe równanie różniczkowe I rzędu względem zmiennej $z(x)$.

---

### 25.5. Zastosowania inżynierskie: Stany nieustalone w obwodach RC i RL

#### 1. Ładowanie kondensatora w obwodzie RC:
Szeregowy obwód składający się z rezystora $R$, kondensatora $C$ oraz stałego źródła napięcia $E$ zamykany jest w chwili $t = 0$.
Z drugiego prawa Kirchhoffa:
$$u_R(t) + u_C(t) = E$$
Wyrażając prąd przez ładunek: $i(t) = \frac{dq}{dt}$, a napięcie na kondensatorze $u_C = \frac{q}{C}$, otrzymujemy:
$$R \frac{dq}{dt} + \frac{q}{C} = E \iff \frac{dq}{dt} + \frac{1}{RC} q = \frac{E}{R}$$
Jest to równanie liniowe I rzędu ze stałymi współczynnikami. Wielkość $\tau = RC$ nazywamy **stałą czasową obwodu RC** [$\text{s}$].
Rozwiązanie przy warunku początkowym $q(0) = 0$:
$$q(t) = C E \left( 1 - e^{-\frac{t}{\tau}} \right)$$
Napięcie na kondensatorze i prąd ładowania:
$$u_C(t) = \frac{q(t)}{C} = E \left( 1 - e^{-\frac{t}{\tau}} \right)$$
$$i(t) = \frac{dq}{dt} = \frac{E}{R} e^{-\frac{t}{\tau}}$$
Dla $t = \tau$: $u_C(\tau) = E(1 - e^{-1}) \approx 0{,}632 E$ (napięcie osiąga 63,2% wartości ustalonej). Dla $t = 5\tau$: $u_C(5\tau) \approx 0{,}993 E$ (stan ustalony uważa się praktycznie za osiągnięty).

#### 2. Włączanie cewki indukcyjnej w obwodzie RL:
Dla obwodu $RL$ pod napięciem stałym $E$:
$$u_R(t) + u_L(t) = E \iff R i(t) + L \frac{di}{dt} = E \iff \frac{di}{dt} + \frac{R}{L} i = \frac{E}{L}$$
Stała czasowa obwodu wynosi $\tau = \frac{L}{R}$. Rozwiązanie przy zerowym stanie początkowym $i(0) = 0$:
$$i(t) = \frac{E}{R} \left( 1 - e^{-\frac{t}{\tau}} \right)$$
Z uwagi na indukowaną SEM samoindukcji prąd w cewce nie może zmienić się skokowo (pierwsze prawo komutacji: $i_L(0^+) = i_L(0^-)$).

---

## Rozdział 26: Równania liniowe wyższych rzędów i metoda transformaty Laplace'a

### 26.1. Równania liniowe rzędu drugiego o stałych współczynnikach

Rozważmy równanie różniczkowe liniowe II rzędu:
$$y'' + a y' + b y = f(x) \quad (a, b \in \mathbb{R})$$
Struktura rozwiązania ogólnego równania niejednorodnego (CORN):
$$y(x) = y_0(x) + y_s(x)$$
gdzie $y_0(x)$ jest rozwiązaniem ogólnym równania jednorodnego (CORJ), a $y_s(x)$ jest dowolnym rozwiązaniem szczególnym równania niejednorodnego (CSRN).

#### Rozwiązywanie równania jednorodnego $y'' + a y' + b y = 0$:
Podstawiamy próbne rozwiązanie wykładnicze Eulera $y = e^{r x}$:
$$(r^2 + a r + b) e^{r x} = 0$$
Ponieważ $e^{r x} \neq 0$, otrzymujemy **równanie charakterystyczne**:
$$r^2 + a r + b = 0, \quad \Delta = a^2 - 4b$$

1. **Przypadek $\Delta > 0$:** Dwa różne pierwiastki rzeczywiste $r_1 \neq r_2$:
   $$y_0(x) = C_1 e^{r_1 x} + C_2 e^{r_2 x}$$
2. **Przypadek $\Delta = 0$:** Jeden pierwiastek podwójny $r_0 = -\frac{a}{2}$:
   $$y_0(x) = (C_1 + C_2 x) e^{r_0 x}$$
3. **Przypadek $\Delta < 0$:** Dwa pierwiastki zespolone sprzężone $r_{1,2} = \alpha \pm i \beta$, gdzie $\alpha = -\frac{a}{2}$, $\beta = \frac{\sqrt{-\Delta}}{2}$:
   $$y_0(x) = e^{\alpha x} (C_1 \cos \beta x + C_2 \sin \beta x)$$

---

### 26.2. Metoda przewidywań dla wymuszeń specjalnych

Dla równania ze stałymi współczynnikami, gdy funkcja po prawej stronie $f(x)$ jest kombinacją wielomianów, funkcji wykładniczych i trygonometrycznych, rozwiązanie szczególne $y_s(x)$ można znaleźć bez całkowania, przewidując jego postać:

| Prawa strona $f(x)$ | Warunek rezonansu | Przewidywana postać CSRN $y_s(x)$ |
| :--- | :--- | :--- |
| $W_m(x)$ (wielomian st. $m$) | $r = 0$ nie jest pierw. charakt. | $Q_m(x)$ (wielomian st. $m$) |
| $W_m(x)$ | $r = 0$ jest pierwiastkiem $k$-krotnym | $x^k Q_m(x)$ |
| $P(x) e^{\lambda x}$ | $\lambda$ nie jest pierw. charakt. | $Q(x) e^{\lambda x}$ ($\deg Q = \deg P$) |
| $P(x) e^{\lambda x}$ | $\lambda$ jest pierw. $k$-krotnym | $x^k Q(x) e^{\lambda x}$ |
| $e^{\alpha x} (A \cos \beta x + B \sin \beta x)$ | $\alpha \pm i \beta$ nie jest pierw. charakt. | $e^{\alpha x} (C \cos \beta x + D \sin \beta x)$ |
| $e^{\alpha x} (A \cos \beta x + B \sin \beta x)$ | $\alpha \pm i \beta$ jest pierw. charakt. (**Rezonans**) | $x e^{\alpha x} (C \cos \beta x + D \sin \beta x)$ |

Nieznane współczynniki wielomianów wyznaczamy metodą współczynników nieoznaczonych po podstawieniu $y_s$ do wyjściowego równania.

---

### 26.3. Zastosowanie w teorii obwodów: Drgania w obwodzie RLC

Rozważmy szeregowy obwód $RLC$ podłączony do źródła napięcia $e(t)$. Z drugiego prawa Kirchhoffa:
$$u_R(t) + u_L(t) + u_C(t) = e(t) \iff R i(t) + L \frac{di(t)}{dt} + \frac{1}{C} \int_0^t i(\tau)\,d\tau + u_C(0) = e(t)$$
Różniczkując obustronnie po czasie $t$:
$$L \frac{d^2 i}{dt^2} + R \frac{di}{dt} + \frac{1}{C} i = \frac{de}{dt} \iff \frac{d^2 i}{dt^2} + 2\alpha \frac{di}{dt} + \omega_0^2 i = \frac{1}{L} \frac{de}{dt}$$
gdzie:
- $\alpha = \frac{R}{2L}$ – współczynnik tłumienia [$\text{s}^{-1}$],
- $\omega_0 = \frac{1}{\sqrt{LC}}$ – pulsacja rezonansowa drgań swobodnych (wzór Thomsona) [$\text{rad}/\text{s}$].

Równanie charakterystyczne obwodu swobodnego ($e(t) \equiv 0$):
$$r^2 + 2\alpha r + \omega_0^2 = 0 \implies r_{1,2} = -\alpha \pm \sqrt{\alpha^2 - \omega_0^2}$$

#### Trzy stany pracy obwodu RLC:
1. **Silne tłumienie / Ruch aperiodyczny ($\alpha > \omega_0 \iff R > 2\sqrt{L/C}$):**  
   Dwa pierwiastki rzeczywiste ujemne $r_1, r_2 < 0$. Prąd zanika monotonicznie bez oscylacji:
   $$i(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$$
2. **Tłumienie krytyczne ($\alpha = \omega_0 \iff R = 2\sqrt{L/C} = R_{\text{kr}}$):**  
   Pierwiastek podwójny $r = -\alpha$. Rezystancja krytyczna $R_{\text{kr}} = 2\sqrt{L/C}$. Stan ten charakteryzuje **najszybszy możliwy zanik stanu nieustalonego bez oscylacji**:
   $$i(t) = (C_1 + C_2 t) e^{-\alpha t}$$
3. **Drgania tłumione / Stan oscylacyjny ($\alpha < \omega_0 \iff R < 2\sqrt{L/C}$):**  
   Pierwiastki zespolone sprzężone $r_{1,2} = -\alpha \pm i \omega$, gdzie $\omega = \sqrt{\omega_0^2 - \alpha^2}$ jest pulsacją drgań tłumionych:
   $$i(t) = e^{-\alpha t} (C_1 \cos \omega t + C_2 \sin \omega t) = I_0 e^{-\alpha t} \sin(\omega t + \psi)$$
   Współczynnik dobroci obwodu:
   $$Q = \frac{\omega_0}{2\alpha} = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$
   Im większa dobroć $Q$, tym mniejsze tłumienie i wolniejszy zanik drgań rezonansowych.

---

### 26.4. Wprowadzenie do metody transformaty Laplace'a

#### Definicja 26.5 (Transformata Laplace'a jednostronna)
Transformatą Laplace'a funkcji rzeczywistej $f: [0, \infty) \to \mathbb{R}$ (zwanej **oryginałem**) nazywamy funkcję zmiennej zespolonej $s = \sigma + i\omega$ zdefiniowaną całką niewłaściwą:
$$\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty f(t) e^{-st}\,dt$$

> **Twierdzenie 26.2 (Podstawowe własności transformaty Laplace'a):**  
> 1. **Liniowość:** $\mathcal{L}\{\alpha f(t) + \beta g(t)\} = \alpha F(s) + \beta G(s)$.
> 2. **Transformata pochodnej (klucz do równań różniczkowych):**
>    $$\mathcal{L}\{f'(t)\} = s F(s) - f(0^+)$$
>    $$\mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0^+) - f'(0^+)$$
>    $$\mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - \sum_{k=1}^n s^{n-k} f^{(k-1)}(0^+)$$
> 3. **Transformata całki:**
>    $$\mathcal{L}\left\{ \int_0^t f(\tau)\,d\tau \right\} = \frac{F(s)}{s}$$
> 4. **Przesunięcie w dziedzinie częstotliwości (tłumienie):**
>    $$\mathcal{L}\{e^{at} f(t)\} = F(s - a)$$
> 5. **Przesunięcie w dziedzinie czasu (opóźnienie):**
>    $$\mathcal{L}\{f(t - T) \mathbf{1}(t - T)\} = e^{-sT} F(s) \quad (T > 0)$$
> 6. **Twierdzenie o splocie (Borela):**
>    $$\mathcal{L}\{(f * g)(t)\} = \mathcal{L}\left\{ \int_0^t f(\tau) g(t - \tau)\,d\tau \right\} = F(s) \cdot G(s)$$

#### Tabela podstawowych transformat Laplace'a:

| Funkcja oryginalna $f(t)$ ($t \ge 0$) | Transformata $F(s) = \mathcal{L}\{f(t)\}$ |
| :--- | :--- |
| Dystrybucja Diraca $\delta(t)$ | $1$ |
| Skok jednostkowy Heaviside'a $\mathbf{1}(t)$ | $\frac{1}{s}$ |
| $t^n$ ($n \in \mathbb{N}$) | $\frac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\frac{1}{s - a}$ |
| $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ |
| $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ |
| $e^{at} \sin(\omega t)$ | $\frac{\omega}{(s - a)^2 + \omega^2}$ |
| $e^{at} \cos(\omega t)$ | $\frac{s - a}{(s - a)^2 + \omega^2}$ |

#### Transmitancja operatorowa i analiza stabilności układów:
Dla układu liniowego opisanego równaniem różniczkowym o zerowych warunkach początkowych:
$$a_n y^{(n)} + \dots + a_0 y = b_m x^{(m)} + \dots + b_0 x$$
przejście do dziedziny transformaty Laplace'a daje:
$$(a_n s^n + \dots + a_0) Y(s) = (b_m s^m + \dots + b_0) X(s)$$
Stosunek transformaty sygnału wyjściowego do wejściowego nazywamy **transmitancją operatorową**:
$$H(s) = \frac{Y(s)}{X(s)} = \frac{b_m s^m + \dots + b_0}{a_n s^n + \dots + a_0} = \frac{L(s)}{M(s)}$$
- Pierwiastki licznika $L(s) = 0$ nazywamy **zerami transmitancji**.
- Pierwiastki mianownika $M(s) = 0$ nazywamy **biegunami transmitancji**.
- **Kryterium stabilności BIBO:** Układ liniowy jest stabilny wtedy i tylko wtedy, gdy wszystkie bieguny jego transmitancji leżą **ściśle w lewej półpłaszczyźnie zespolonej**:
  $$\forall k: \operatorname{Re}(s_k) < 0$$

---

### 26.5. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 26.1 (Równanie liniowe I rzędu z warunkiem początkowym)
Rozwiązać zagadnienie Cauchy'ego:
$$y' + \frac{2x}{1 + x^2} y = \frac{3x^2}{1 + x^2}, \quad y(0) = 2$$

**Rozwiązanie:**  
1. **Równanie jednorodne:**
   $$y' + \frac{2x}{1 + x^2} y = 0 \implies \frac{dy}{y} = -\frac{2x}{1 + x^2}\,dx \implies \ln |y| = -\ln(1 + x^2) + \ln |C|$$
   $$y_0(x) = \frac{C}{1 + x^2}$$

2. **Uzmiennianie stałej:**
   $$y(x) = \frac{C(x)}{1 + x^2} \implies y' = \frac{C'(x)(1+x^2) - C(x)(2x)}{(1+x^2)^2} = \frac{C'(x)}{1+x^2} - \frac{2x C(x)}{(1+x^2)^2}$$
   Wstawiając do równania wyjściowego:
   $$\frac{C'(x)}{1 + x^2} = \frac{3x^2}{1 + x^2} \implies C'(x) = 3x^2 \implies C(x) = x^3 + C$$
   Rozwiązanie ogólne (CORN):
   $$y(x) = \frac{x^3 + C}{1 + x^2}$$

3. **Uwzględnienie warunku początkowego $y(0) = 2$:**
   $$2 = \frac{0^3 + C}{1 + 0^2} = C \implies C = 2$$
   Ostateczne rozwiązanie zagadnienia Cauchy'ego:
   $$y(x) = \frac{x^3 + 2}{1 + x^2}$$

---

#### Przykład 26.2 (Równanie liniowe II rzędu - metoda przewidywań z rezonansem)
Wyznaczyć rozwiązanie ogólne równania:
$$y'' - 4y' + 4y = 8 e^{2x} + 4x$$

**Rozwiązanie:**  
1. **Rozwiązanie równania jednorodnego (CORJ):**  
   Równanie charakterystyczne:
   $$r^2 - 4r + 4 = 0 \implies (r - 2)^2 = 0 \implies r_1 = r_2 = 2 \quad (\text{pierwiastek podwójny, } k = 2)$$
   Stąd:
   $$y_0(x) = (C_1 + C_2 x) e^{2x}$$

2. **Wyznaczenie CSRN dla członu $f_1(x) = 8 e^{2x}$:**  
   Liczba $\lambda = 2$ jest podwójnym pierwiastkiem równania charakterystycznego ($k = 2$, rezonans rzędu 2).
   Przewidujemy postać:
   $$y_{s1}(x) = A x^2 e^{2x}$$
   Obliczamy pochodne:
   $$y'_{s1} = A (2x e^{2x} + 2x^2 e^{2x}) = 2A(x + x^2) e^{2x}$$
   $$y''_{s1} = 2A(1 + 2x) e^{2x} + 4A(x + x^2) e^{2x} = 2A(1 + 4x + 2x^2) e^{2x}$$
   Wstawiając do lewej strony:
   $$y''_{s1} - 4y'_{s1} + 4y_{s1} = 2A(1 + 4x + 2x^2) e^{2x} - 8A(x + x^2) e^{2x} + 4A x^2 e^{2x}$$
   $$= e^{2x} [2A + 8Ax + 4Ax^2 - 8Ax - 8Ax^2 + 4Ax^2] = 2A e^{2x}$$
   Przyrównując do prawej strony:
   $$2A e^{2x} = 8 e^{2x} \implies 2A = 8 \implies A = 4 \implies y_{s1}(x) = 4x^2 e^{2x}$$

3. **Wyznaczenie CSRN dla członu $f_2(x) = 4x$:**  
   Liczba $\lambda = 0$ nie jest pierwiastkiem równania charakterystycznego.
   Przewidujemy wielomian stopnia 1:
   $$y_{s2}(x) = B x + D \implies y'_{s2} = B, \quad y''_{s2} = 0$$
   Wstawiając do lewej strony:
   $$0 - 4B + 4(Bx + D) = 4Bx + (4D - 4B) = 4x$$
   Przyrównując współczynniki przy odpowiednich potęgach:
   $$\begin{cases} 4B = 4 \implies B = 1 \\ 4D - 4B = 0 \implies D = B = 1 \end{cases} \implies y_{s2}(x) = x + 1$$

4. **Zasada superpozycji (CORN):**
   $$y(x) = y_0(x) + y_{s1}(x) + y_{s2}(x) = (C_1 + C_2 x) e^{2x} + 4x^2 e^{2x} + x + 1$$

---

#### Przykład 26.3 (Rozwiązywanie równania różniczkowego metodą transformaty Laplace'a)
Wyznaczyć odpowiedź obwodu opisanego równaniem:
$$y'' + 4y' + 3y = 6 e^{-t}, \quad y(0) = 1, \quad y'(0) = 0$$

**Rozwiązanie:**  
1. **Transformacja Laplace'a równania:**  
   Stosujemy transformatę do obu stron z uwzględnieniem warunków początkowych:
   $$\mathcal{L}\{y''\} = s^2 Y(s) - s y(0) - y'(0) = s^2 Y(s) - s \cdot 1 - 0 = s^2 Y(s) - s$$
   $$\mathcal{L}\{y'\} = s Y(s) - y(0) = s Y(s) - 1$$
   $$\mathcal{L}\{e^{-t}\} = \frac{1}{s + 1}$$
   Równanie operatorowe:
   $$(s^2 Y(s) - s) + 4(s Y(s) - 1) + 3 Y(s) = \frac{6}{s + 1}$$
   $$(s^2 + 4s + 3) Y(s) - s - 4 = \frac{6}{s + 1}$$

2. **Wyznaczenie $Y(s)$:**
   $$(s^2 + 4s + 3) Y(s) = s + 4 + \frac{6}{s + 1} = \frac{(s + 4)(s + 1) + 6}{s + 1} = \frac{s^2 + 5s + 10}{s + 1}$$
   Ponieważ $s^2 + 4s + 3 = (s + 1)(s + 3)$:
   $$Y(s) = \frac{s^2 + 5s + 10}{(s + 1)^2 (s + 3)}$$

3. **Rozkład na ułamki proste:**
   $$Y(s) = \frac{A}{s + 1} + \frac{B}{(s + 1)^2} + \frac{C}{s + 3}$$
   Mnożąc obustronnie przez mianownik:
   $$s^2 + 5s + 10 = A(s + 1)(s + 3) + B(s + 3) + C(s + 1)^2$$
   - Dla $s = -1$: $(-1)^2 + 5(-1) + 10 = B(-1 + 3) \implies 6 = 2B \implies B = 3$.
   - Dla $s = -3$: $(-3)^2 + 5(-3) + 10 = C(-3 + 1)^2 \implies 4 = 4C \implies C = 1$.
   - Przyrównując współczynniki przy $s^2$: $1 = A + C \implies 1 = A + 1 \implies A = 0$.
   Zatem:
   $$Y(s) = \frac{3}{(s + 1)^2} + \frac{1}{s + 3}$$

4. **Odwrotna transformata Laplace'a ($\mathcal{L}^{-1}$):**  
   Z własności przesunięcia: $\mathcal{L}^{-1}\left\{\frac{1}{(s+1)^2}\right\} = t e^{-t}$ oraz $\mathcal{L}^{-1}\left\{\frac{1}{s+3}\right\} = e^{-3t}$.
   Ostateczne rozwiązanie w dziedzinie czasu:
   $$y(t) = 3t e^{-t} + e^{-3t} \quad (t \ge 0)$$

---

### 26.6. Zadania do samodzielnego rozwiązania

1. **Zadanie 26.1:** Rozwiązać równanie o zmiennych rozdzielonych: $x y' = y(1 + \ln y - \ln x)$.  
   *Wskazówka:* Podstawienie $u = y/x$.  
   *Odpowiedź:* $y = x e^{C x}$.

2. **Zadanie 26.2:** Rozwiązać równanie Bernoulliego: $y' + 2xy = 2x y^3$.  
   *Odpowiedź:* Podstawienie $z = y^{-2}$. $y(x) = \pm \frac{1}{\sqrt{1 + C e^{2x^2}}}$.

3. **Zadanie 26.3:** W obwodzie szeregowym $RL$ o parametrach $R = 10 \; \Omega$, $L = 2 \; \text{H}$ podłączono źródło sinusoidalne $e(t) = 100 \sin(10t) \; \text{V}$. Wyznaczyć prąd ustalony $i(t)$.  
   *Odpowiedź:* Impedancja obwodu $Z = R + j\omega L = 10 + j 20 = 10\sqrt{5} e^{j \operatorname{arctg} 2}$. Prąd w stanie ustalonym: $i(t) = \frac{100}{10\sqrt{5}} \sin(10t - \operatorname{arctg} 2) = 2\sqrt{5} \sin(10t - \operatorname{arctg} 2) \; \text{A}$.

4. **Zadanie 26.4:** Wyznaczyć rozwiązanie ogólne równania różniczkowego rzędu drugiego: $y'' + 9y = \sin(3x)$.  
   *Odpowiedź:* Zjawisko rezonansu. $y_0 = C_1 \cos 3x + C_2 \sin 3x$. Przewidujemy $y_s = x(A \cos 3x + B \sin 3x)$. $y(x) = C_1 \cos 3x + C_2 \sin 3x - \frac{1}{6} x \cos(3x)$.

5. **Zadanie 26.5:** Metodą transformaty Laplace'a wyznaczyć rozwiązanie równania różniczkowego z wymuszeniem skokowym:  
   $$y'' + 2y' + 5y = 5 \cdot \mathbf{1}(t), \quad y(0) = 0, \quad y'(0) = 0$$  
   *Odpowiedź:* $Y(s) = \frac{5}{s(s^2 + 2s + 5)} = \frac{1}{s} - \frac{s + 2}{(s+1)^2 + 4} = \frac{1}{s} - \frac{s+1}{(s+1)^2 + 4} - \frac{1}{2}\frac{2}{(s+1)^2 + 4}$.  
   W dziedzinie czasu: $y(t) = 1 - e^{-t} \left( \cos 2t + \frac{1}{2}\sin 2t \right)$.
