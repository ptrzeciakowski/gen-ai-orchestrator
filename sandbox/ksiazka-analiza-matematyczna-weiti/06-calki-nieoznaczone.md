# Część VI: Całka Nieoznaczona i Techniki Całkowania

Podczas gdy rachunek różniczkowy polega na wyznaczaniu tempa zmian funkcji i opiera się na algorytmicznych, mechanicznych regułach (pochodna iloczynu, ilorazu, złożenia), rachunek całkowy jest operacją odwrotną, wymagającą rozpoznawania struktur algebraicznych i doboru właściwych przekształceń funkcyjnych. W elektrotechnice i teorii sygnałów całkowanie jest operacją akumulacji: ładunku z prądu ($q(t) = \int i(t)\,dt$), strumienia magnetycznego z napięcia indukowanego ($\Phi(t) = \int u(t)\,dt$), a także stanowi rdzeń wyznaczania odpowiedzi impulsowej i transmitancji układów dynamicznych.

---

## Rozdział 12: Pojęcie funkcji pierwotnej i całki nieoznaczonej

### 12.1. Definicja funkcji pierwotnej i całki nieoznaczonej

Niech funkcja $f$ będzie określona na przedziale $I \subset \mathbb{R}$.

#### Definicja 12.1 (Funkcja pierwotna)
Funkcję $F: I \to \mathbb{R}$ nazywamy **funkcją pierwotną** funkcji $f$ na przedziale $I$, jeżeli $F$ jest różniczkowalna w każdym punkcie $x \in I$ oraz:
$$F'(x) = f(x) \quad \forall x \in I$$

> **Twierdzenie 12.1 (O jednoznaczności funkcji pierwotnej z dokładnością do stałej):**  
> Jeżeli $F(x)$ jest funkcją pierwotną funkcji $f(x)$ na przedziale $I$, to:
> 1. Dla dowolnej stałej $C \in \mathbb{R}$ funkcja $G(x) = F(x) + C$ jest również funkcją pierwotną $f(x)$.
> 2. Każda funkcja pierwotna funkcji $f(x)$ na przedziale $I$ ma postać $F(x) + C$.

**Dowód:**  
1. $G'(x) = (F(x) + C)' = F'(x) + 0 = f(x)$.  
2. Niech $F_1, F_2$ będą dwiema funkcjami pierwotnymi $f$ na przedziale $I$. Rozpatrzmy funkcję różnicową $H(x) = F_1(x) - F_2(x)$.  
Wtedy dla każdego $x \in I$:
$$H'(x) = F_1'(x) - F_2'(x) = f(x) - f(x) = 0$$
Z twierdzenia Lagrange'a o wartości średniej, jeżeli pochodna funkcji na przedziale jest tożsamościowo równa zeru, to funkcja ta jest stała: $H(x) \equiv C$. Stąd $F_1(x) = F_2(x) + C$. $\blacksquare$

#### Definicja 12.2 (Całka nieoznaczona)
Zbiór wszystkich funkcji pierwotnych funkcji $f$ na przedziale $I$ nazywamy **całką nieoznaczoną** i zapisujemy:
$$\int f(x)\,dx = F(x) + C \quad (C \in \mathbb{R})$$
Symbol $\int$ nazywamy znakiem całki, $f(x)$ – funkcją podcałkową, $f(x)\,dx$ – wyrażeniem podcałkowym, a $C$ – stałą całkowania.

---

### 12.2. Własności całki nieoznaczonej i tablica całek elementarnych

> **Twierdzenie 12.2 (Liniowość całki nieoznaczonej):**  
> Dla dowolnych stałych $\alpha, \beta \in \mathbb{R}$:
> $$\int \big( \alpha f(x) + \beta g(x) \big)\,dx = \alpha \int f(x)\,dx + \beta \int g(x)\,dx$$

#### Tablica podstawowych całek elementarnych:

| Funkcja podcałkowa $f(x)$ | Całka nieoznaczona $\int f(x)\,dx$ | Dziedzina |
| :--- | :--- | :--- |
| $x^\alpha \quad (\alpha \neq -1)$ | $\frac{x^{\alpha+1}}{\alpha + 1} + C$ | $x > 0$ (lub $x \in \mathbb{R}$ dla $\alpha \in \mathbb{N}$) |
| $\frac{1}{x}$ | $\ln |x| + C$ | $x \neq 0$ |
| $e^x$ | $e^x + C$ | $x \in \mathbb{R}$ |
| $a^x \quad (a > 0, a \neq 1)$ | $\frac{a^x}{\ln a} + C$ | $x \in \mathbb{R}$ |
| $\sin x$ | $-\cos x + C$ | $x \in \mathbb{R}$ |
| $\cos x$ | $\sin x + C$ | $x \in \mathbb{R}$ |
| $\frac{1}{\cos^2 x} = 1 + \operatorname{tg}^2 x$ | $\operatorname{tg} x + C$ | $x \neq \frac{\pi}{2} + k\pi$ |
| $\frac{1}{\sin^2 x} = 1 + \operatorname{ctg}^2 x$ | $-\operatorname{ctg} x + C$ | $x \neq k\pi$ |
| $\frac{1}{1 + x^2}$ | $\operatorname{arctg} x + C$ | $x \in \mathbb{R}$ |
| $\frac{1}{a^2 + x^2} \quad (a \neq 0)$ | $\frac{1}{a} \operatorname{arctg}\left(\frac{x}{a}\right) + C$ | $x \in \mathbb{R}$ |
| $\frac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ | $x \in (-1, 1)$ |
| $\frac{1}{\sqrt{a^2 - x^2}} \quad (a > 0)$ | $\arcsin\left(\frac{x}{a}\right) + C$ | $x \in (-a, a)$ |
| $\frac{1}{\sqrt{x^2 + q}} \quad (q \neq 0)$ | $\ln |x + \sqrt{x^2 + q}| + C$ | $x^2 + q > 0$ |
| $\frac{1}{x^2 - a^2} \quad (a \neq 0)$ | $\frac{1}{2a} \ln \left| \frac{x - a}{x + a} \right| + C$ | $x \neq \pm a$ |
| $\operatorname{sh} x$ | $\operatorname{ch} x + C$ | $x \in \mathbb{R}$ |
| $\operatorname{ch} x$ | $\operatorname{sh} x + C$ | $x \in \mathbb{R}$ |

---

### 12.3. Dwie fundamentalne metody: przez części i przez podstawienie

> **Twierdzenie 12.3 (Całkowanie przez części):**  
> Jeżeli funkcje $u(x)$ i $v(x)$ są różniczkowalne w sposób ciągły na przedziale $I$, to:
> $$\int u(x) v'(x)\,dx = u(x) v(x) - \int u'(x) v(x)\,dx$$
> w zapisie różniczkowym:
> $$\int u\,dv = u v - \int v\,du$$

**Dowód:**  
Z reguły różniczkowania iloczynu: $(u \cdot v)' = u' v + u v'$. Całkując obie strony:
$$\int (u v)'\,dx = \int u' v\,dx + \int u v'\,dx \implies u v = \int u' v\,dx + \int u v'\,dx$$
Przenosząc składnik $\int u' v\,dx$ na drugą stronę, otrzymujemy tezę. $\blacksquare$

#### Heurystyka doboru funkcji (reguła LIATE):
Przy wyborze funkcji $u(x)$ (którą różniczkujemy) priorytet mają funkcje trudniejsze do bezpośredniego scałkowania:
1. **L**ogarytmiczne ($\ln x$),
2. **I**nverse trigonometric (cyklometryczne: $\arcsin x, \operatorname{arctg} x$),
3. **A**lgebraiczne (wielomiany $x^n$),
4. **T**rygonometryczne ($\sin x, \cos x$),
5. **E**xponential (wykładnicze $e^x, a^x$).

> **Twierdzenie 12.4 (Całkowanie przez podstawienie / zamiana zmiennych):**  
> 1. **Postać I (podstawienie bezpośrednie):**  
>    $$\int f\big(\varphi(x)\big) \varphi'(x)\,dx = \left. \int f(t)\,dt \right|_{t = \varphi(x)}$$
> 2. **Postać II (podstawienie odwrotne):**  
>    Jeżeli funkcja $x = \psi(t)$ jest odwracalna oraz $\psi'(t) \neq 0$:
>    $$\int f(x)\,dx = \left. \int f\big(\psi(t)\big) \psi'(t)\,dt \right|_{t = \psi^{-1}(x)}$$

---

## Rozdział 13: Techniki całkowania wybranych klas funkcji

### 13.1. Całkowanie funkcji wymiernych

Funkcją wymierną nazywamy iloraz dwóch wielomianów $R(x) = \frac{P(x)}{Q(x)}$.
- Jeżeli $\deg P \ge \deg Q$ (ułamek niewłaściwy), dzielimy wielomian $P(x)$ przez $Q(x)$ z resztą:
  $$\frac{P(x)}{Q(x)} = W(x) + \frac{R_1(x)}{Q(x)}, \quad \deg R_1 < \deg Q$$
  gdzie $W(x)$ jest wielomianem (całkowalnym natychmiast).
- Zakładamy dalej, że $\deg P < \deg Q$ (ułamek właściwy).

#### Twierdzenie o rozkładzie na ułamki proste:
Każdy wielomian o współczynnikach rzeczywistych $Q(x)$ rozkłada się jednoznacznie na iloczyn czynników liniowych i nierozkładalnych trójmianów kwadratowych ($\Delta < 0$):
$$Q(x) = a_n (x - x_1)^{k_1} \dots (x - x_r)^{k_r} (x^2 + p_1 x + q_1)^{m_1} \dots (x^2 + p_s x + q_s)^{m_s}$$
Każdą funkcję wymierną właściwą $\frac{P(x)}{Q(x)}$ można jednoznacznie rozłożyć na sumę **ułamków prostych I i II rodzaju**:
1. Ułamek prosty I rodzaju:
   $$\frac{A}{(x - x_i)^k} \implies \int \frac{A}{(x - x_i)^k}\,dx = \begin{cases} A \ln |x - x_i| + C & \text{dla } k = 1 \\ -\frac{A}{(k-1)(x - x_i)^{k-1}} + C & \text{dla } k > 1 \end{cases}$$
2. Ułamek prosty II rodzaju:
   $$\frac{B x + C}{(x^2 + p x + q)^m} \quad (p^2 - 4q < 0)$$
   Dla $m = 1$: wydzielamy w liczniku pochodną mianownika $(2x + p)$:
   $$\frac{Bx + C}{x^2 + px + q} = \frac{B}{2} \frac{2x + p}{x^2 + px + q} + \left( C - \frac{Bp}{2} \right) \frac{1}{\left( x + \frac{p}{2} \right)^2 + \left( q - \frac{p^2}{4} \right)}$$
   Pierwszy składnik daje $\frac{B}{2} \ln(x^2 + px + q)$, drugi daje funkcję $\operatorname{arctg}$.

#### Metoda wydzielania części wymiernej Ostrogradskiego:
Dla ułamków o wielokrotnych biegunach zespolonych stosuje się tożsamość Ostrogradskiego:
$$\int \frac{P(x)}{Q(x)}\,dx = \frac{P_1(x)}{Q_1(x)} + \int \frac{P_2(x)}{Q_2(x)}\,dx$$
gdzie $Q_1(x) = \operatorname{NWD}(Q(x), Q'(x))$ oraz $Q_2(x) = Q(x) / Q_1(x)$. Wielomiany $P_1(x)$ i $P_2(x)$ wyznacza się przez różniczkowanie tożsamości.

---

### 13.2. Całkowanie wyrażeń trygonometrycznych

Rozważmy całkę $\int R(\sin x, \cos x)\,dx$, gdzie $R$ jest funkcją wymierną dwóch zmiennych.

#### 1. Podstawienie uniwersalne:
$$t = \operatorname{tg}\frac{x}{2} \quad (x \in (-\pi, \pi))$$
Ze wzorów trygonometrycznych:
$$\sin x = \frac{2t}{1 + t^2}, \quad \cos x = \frac{1 - t^2}{1 + t^2}, \quad dx = \frac{2}{1 + t^2}\,dt$$
Sprowadza ono każdą całkę trygonometryczną do całki z funkcji wymiernej zmiennej $t$.

#### 2. Podstawienia specjalne (szybsze i redukujące stopień):
- Jeżeli $R(-\sin x, \cos x) = -R(\sin x, \cos x)$ (nieparzysta względem $\sin x$), stosujemy:
  $$t = \cos x, \quad dt = -\sin x\,dx$$
- Jeżeli $R(\sin x, -\cos x) = -R(\sin x, \cos x)$ (nieparzysta względem $\cos x$), stosujemy:
  $$t = \sin x, \quad dt = \cos x\,dx$$
- Jeżeli $R(-\sin x, -\cos x) = R(\sin x, \cos x)$ (parzysta względem obu argumentów jednocześnie):
  $$t = \operatorname{tg} x \implies \sin^2 x = \frac{t^2}{1 + t^2}, \quad \cos^2 x = \frac{1}{1 + t^2}, \quad dx = \frac{dt}{1 + t^2}$$

#### 3. Całki iloczynów funkcji trygonometrycznych (Podstawa teorii Fouriera):
Zamiana iloczynu na sumę:
$$\sin(\alpha x) \cos(\beta x) = \frac{1}{2} \big[ \sin((\alpha + \beta)x) + \sin((\alpha - \beta)x) \big]$$
$$\cos(\alpha x) \cos(\beta x) = \frac{1}{2} \big[ \cos((\alpha + \beta)x) + \cos((\alpha - \beta)x) \big]$$
$$\sin(\alpha x) \sin(\beta x) = \frac{1}{2} \big[ \cos((\alpha - \beta)x) - \cos((\alpha + \beta)x) \big]$$

---

### 13.3. Całkowanie wyrażeń niewymiernych i podstawienia Eulera

Całki postaci $\int R(x, \sqrt{ax^2 + bx + c})\,dx$ sprowadza się do całek funkcji wymiernych za pomocą **trzech klasycznych podstawień Leonharda Eulera**:

1. **I podstawienie Eulera (gdy $a > 0$):**
   $$\sqrt{ax^2 + bx + c} = t - \sqrt{a}x \quad \text{lub} \quad t + \sqrt{a}x$$
   Podnosząc do kwadratu: $ax^2 + bx + c = t^2 \pm 2t\sqrt{a}x + ax^2$. Wyrazy $ax^2$ redukują się, co pozwala wyznaczyć $x$ jako funkcję wymierną $t$:
   $$x = \frac{t^2 - c}{b \pm 2t\sqrt{a}}$$

2. **II podstawienie Eulera (gdy $c > 0$):**
   $$\sqrt{ax^2 + bx + c} = x t + \sqrt{c}$$
   Podnosząc do kwadratu: $ax^2 + bx + c = x^2 t^2 + 2x t \sqrt{c} + c$. Redukując $c$ i dzieląc przez $x \neq 0$:
   $$ax + b = x t^2 + 2t\sqrt{c} \implies x = \frac{2t\sqrt{c} - b}{a - t^2}$$

3. **III podstawienie Eulera (gdy trójmian ma pierwiastki rzeczywiste $x_1, x_2$, $\Delta > 0$):**
   $$\sqrt{a(x - x_1)(x - x_2)} = t(x - x_1)$$
   Podnosząc do kwadratu: $a(x - x_1)(x - x_2) = t^2 (x - x_1)^2$. Dzieląc przez $(x - x_1)$:
   $$a(x - x_2) = t^2 (x - x_1) \implies x = \frac{a x_2 - t^2 x_1}{a - t^2}$$

---

### 13.4. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 13.1 (Całkowanie przez części - całka cykliczna)
Obliczyć całkę:
$$I = \int e^{2x} \cos(3x)\,dx$$

**Rozwiązanie:**  
Stosujemy dwukrotnie całkowanie przez części.  
Krok 1: $u = \cos(3x) \implies du = -3\sin(3x)\,dx$, $dv = e^{2x}\,dx \implies v = \frac{1}{2} e^{2x}$:
$$I = \frac{1}{2} e^{2x} \cos(3x) - \int \frac{1}{2} e^{2x} (-3\sin(3x))\,dx = \frac{1}{2} e^{2x} \cos(3x) + \frac{3}{2} \int e^{2x} \sin(3x)\,dx$$
Krok 2: Całkujemy nową całkę przez części:  
$u_1 = \sin(3x) \implies du_1 = 3\cos(3x)\,dx$, $dv_1 = e^{2x}\,dx \implies v_1 = \frac{1}{2} e^{2x}$:
$$\int e^{2x} \sin(3x)\,dx = \frac{1}{2} e^{2x} \sin(3x) - \frac{3}{2} \int e^{2x} \cos(3x)\,dx = \frac{1}{2} e^{2x} \sin(3x) - \frac{3}{2} I$$
Wstawiając do pierwszego równania:
$$I = \frac{1}{2} e^{2x} \cos(3x) + \frac{3}{2} \left[ \frac{1}{2} e^{2x} \sin(3x) - \frac{3}{2} I \right] = \frac{1}{2} e^{2x} \cos(3x) + \frac{3}{4} e^{2x} \sin(3x) - \frac{9}{4} I$$
Przenosimy $\frac{9}{4} I$ na lewą stronę:
$$\left( 1 + \frac{9}{4} \right) I = \frac{13}{4} I = e^{2x} \left( \frac{1}{2} \cos(3x) + \frac{3}{4} \sin(3x) \right) = \frac{e^{2x}}{4} \big( 2\cos(3x) + 3\sin(3x) \big)$$
Mnożąc przez $\frac{4}{13}$:
$$I = \frac{e^{2x}}{13} \big( 2\cos(3x) + 3\sin(3x) \big) + C$$

---

#### Przykład 13.2 (Rozkład na ułamki proste)
Obliczyć całkę:
$$\int \frac{x^2 + 1}{(x - 1)(x + 2)^2}\,dx$$

**Rozwiązanie:**  
Postać rozkładu na ułamki proste:
$$\frac{x^2 + 1}{(x - 1)(x + 2)^2} = \frac{A}{x - 1} + \frac{B}{x + 2} + \frac{C}{(x + 2)^2}$$
Mnożąc obustronnie przez mianownik:
$$x^2 + 1 = A(x + 2)^2 + B(x - 1)(x + 2) + C(x - 1)$$
- Dla $x = 1$: $1^2 + 1 = A(1 + 2)^2 \implies 2 = 9A \implies A = \frac{2}{9}$.
- Dla $x = -2$: $(-2)^2 + 1 = C(-2 - 1) \implies 5 = -3C \implies C = -\frac{5}{3}$.
- Przyrównując współczynniki przy $x^2$: $1 = A + B \implies B = 1 - A = 1 - \frac{2}{9} = \frac{7}{9}$.

Całkujemy poszczególne ułamki:
$$\int \frac{x^2 + 1}{(x - 1)(x + 2)^2}\,dx = \frac{2}{9} \int \frac{dx}{x - 1} + \frac{7}{9} \int \frac{dx}{x + 2} - \frac{5}{3} \int \frac{dx}{(x + 2)^2}$$
$$= \frac{2}{9} \ln |x - 1| + \frac{7}{9} \ln |x + 2| + \frac{5}{3(x + 2)} + C$$

---

#### Przykład 13.3 (Całka trygonometryczna metodą parzystości)
Obliczyć całkę:
$$\int \frac{dx}{\sin^4 x \cos^2 x}$$

**Rozwiązanie:**  
Funkcja jest parzysta względem obu argumentów (zmiana $\sin x \to -\sin x$ i $\cos x \to -\cos x$ nie zmienia znaku).  
Stosujemy podstawienie:
$$t = \operatorname{tg} x \implies \sin^2 x = \frac{t^2}{1 + t^2}, \quad \cos^2 x = \frac{1}{1 + t^2}, \quad dx = \frac{dt}{1 + t^2}$$
Wstawiając do całki:
$$\int \frac{\frac{dt}{1 + t^2}}{\left( \frac{t^2}{1 + t^2} \right)^2 \cdot \frac{1}{1 + t^2}} = \int \frac{\frac{dt}{1 + t^2}}{\frac{t^4}{(1 + t^2)^3}} = \int \frac{(1 + t^2)^2}{t^4}\,dt = \int \frac{1 + 2t^2 + t^4}{t^4}\,dt$$
$$= \int (t^{-4} + 2t^{-2} + 1)\,dt = -\frac{1}{3t^3} - \frac{2}{t} + t + C$$
Wracając do zmiennej $x$:
$$= -\frac{1}{3\operatorname{tg}^3 x} - \frac{2}{\operatorname{tg} x} + \operatorname{tg} x + C = -\frac{1}{3}\operatorname{ctg}^3 x - 2\operatorname{ctg} x + \operatorname{tg} x + C$$

---

#### Przykład 13.4 (Podstawienie Eulera)
Obliczyć całkę:
$$\int \frac{dx}{\sqrt{x^2 + 4x + 5}}$$

**Rozwiązanie:**  
Wyróżnik trójmianu: $\Delta = 16 - 20 = -4 < 0$. Ponieważ współczynnik przy $x^2$ wynosi $a = 1 > 0$, sprowadzamy trójmian do postaci kanonicznej:
$$x^2 + 4x + 5 = (x + 2)^2 + 1$$
Podstawiamy $u = x + 2$, $du = dx$:
$$\int \frac{du}{\sqrt{u^2 + 1}} = \ln |u + \sqrt{u^2 + 1}| + C = \ln \left| x + 2 + \sqrt{x^2 + 4x + 5} \right| + C$$

---

### 13.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 13.1:** Obliczyć całkę: $\int x^2 \ln x\,dx$.  
   *Odpowiedź:* $\frac{1}{3} x^3 \ln x - \frac{1}{9} x^3 + C$.

2. **Zadanie 13.2:** Obliczyć całkę: $\int \operatorname{arctg} x\,dx$.  
   *Odpowiedź:* $x \operatorname{arctg} x - \frac{1}{2} \ln(1 + x^2) + C$.

3. **Zadanie 13.3:** Obliczyć całkę funkcji wymiernej: $\int \frac{dx}{x^3 + 1}$.  
   *Wskazówka:* $x^3 + 1 = (x + 1)(x^2 - x + 1)$.  
   *Odpowiedź:* $\frac{1}{3} \ln |x + 1| - \frac{1}{6} \ln(x^2 - x + 1) + \frac{\sqrt{3}}{3} \operatorname{arctg}\left(\frac{2x - 1}{\sqrt{3}}\right) + C$.

4. **Zadanie 13.4:** Obliczyć całkę: $\int \frac{\sin^3 x}{\cos^4 x}\,dx$.  
   *Odpowiedź:* Podstawienie $t = \cos x$. $\frac{1}{3\cos^3 x} - \frac{1}{\cos x} + C$.

5. **Zadanie 13.5:** Obliczyć całkę: $\int \sqrt{a^2 - x^2}\,dx$ ($a > 0$).  
   *Wskazówka:* Podstawienie $x = a \sin t$.  
   *Odpowiedź:* $\frac{x}{2}\sqrt{a^2 - x^2} + \frac{a^2}{2}\arcsin\left(\frac{x}{a}\right) + C$.
