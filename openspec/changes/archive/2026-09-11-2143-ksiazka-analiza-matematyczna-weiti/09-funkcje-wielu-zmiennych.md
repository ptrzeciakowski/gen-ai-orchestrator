# Część IX: Rachunek Różniczkowy Funkcji Wielu Zmiennych

W elektrotechnice, teorii sygnałów, przetwarzaniu informacji oraz uczeniu maszynowym wielkości fizyczne rzadko zależą od jednego parametru. Potencjał pola elektrostatycznego w przestrzeni zależy od trzech współrzędnych przestrzennych $V(x, y, z)$; funkcja strat sieci neuronowej (loss function) zależy od milionów wag $L(w_1, w_2, \dots, w_n)$; impedancja zastępcza obwodu zależy od wartości wielu rezystorów, cewek i kondensatorów oraz częstotliwości pracy. Rachunek różniczkowy funkcji wielu zmiennych stanowi uniwersalny aparat matematyczny pozwalający na badanie wielowymiarowych relacji, ich lokalną linearyzację oraz optymalizację wieloparametrową.

---

## Rozdział 19: Topologia przestrzeni $\mathbb{R}^n$, granice i ciągłość

### 19.1. Przestrzeń euklidesowa $\mathbb{R}^n$ i jej struktura geometryczna

#### Definicja 19.1 (Przestrzeń $\mathbb{R}^n$)
Przestrzenią euklidesową $\mathbb{R}^n$ ($n \in \mathbb{N}$) nazywamy zbiór uporządkowanych ciągów $n$ liczb rzeczywistych:
$$\mathbb{R}^n = \{ \mathbf{x} = (x_1, x_2, \dots, x_n) : x_i \in \mathbb{R} \text{ dla } i=1,\dots,n \}$$
W zbiorze tym definiujemy strukturę przestrzeni liniowej nad ciałem $\mathbb{R}$ z działaniami dodawania wektorów oraz mnożenia przez skalar:
$$\mathbf{x} + \mathbf{y} = (x_1 + y_1, x_2 + y_2, \dots, x_n + y_n)$$
$$\alpha \mathbf{x} = (\alpha x_1, \alpha x_2, \dots, \alpha x_n), \quad \alpha \in \mathbb{R}$$

#### Definicja 19.2 (Iloczyn skalarny, norma i metryka euklidesowa)
1. **Standardowy iloczyn skalarny** wektorów $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$:
   $$\langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x} \cdot \mathbf{y} = \sum_{i=1}^n x_i y_i$$
2. **Norma euklidesowa** (długość wektora):
   $$\|\mathbf{x}\| = \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle} = \sqrt{\sum_{i=1}^n x_i^2}$$
3. **Metryka euklidesowa** (odległość między punktami $\mathbf{x}$ i $\mathbf{y}$):
   $$d(\mathbf{x}, \mathbf{y}) = \|\mathbf{x} - \mathbf{y}\| = \sqrt{\sum_{i=1}^n (x_i - y_i)^2}$$

> **Twierdzenie 19.1 (Nierówność Cauchy'ego-Schwarza i nierówność trójkąta):**
> Dla dowolnych wektorów $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$:
> 1. $|\langle \mathbf{x}, \mathbf{y} \rangle| \le \|\mathbf{x}\| \cdot \|\mathbf{y}\|$ (Nierówność Cauchy'ego-Schwarza).
> 2. $\|\mathbf{x} + \mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|$ (Nierówność trójkąta Minkowskiego).

**Dowód (Nierówność Cauchy'ego-Schwarza):**  
Dla dowolnego $t \in \mathbb{R}$ rozważmy formę kwadratową nieujemną:
$$P(t) = \|\mathbf{x} + t\mathbf{y}\|^2 = \langle \mathbf{x} + t\mathbf{y}, \mathbf{x} + t\mathbf{y} \rangle = \|\mathbf{x}\|^2 + 2t \langle \mathbf{x}, \mathbf{y} \rangle + t^2 \|\mathbf{y}\|^2 \ge 0$$
Trójmian kwadratowy $A t^2 + B t + C$ o współczynnikach $A = \|\mathbf{y}\|^2$, $B = 2\langle \mathbf{x}, \mathbf{y} \rangle$, $C = \|\mathbf{x}\|^2$ przyjmuje wartości nieujemne dla wszystkich $t \in \mathbb{R}$, stąd jego wyróżnik $\Delta$ musi spełniać $\Delta \le 0$:
$$\Delta = B^2 - 4AC = 4 \langle \mathbf{x}, \mathbf{y} \rangle^2 - 4 \|\mathbf{y}\|^2 \|\mathbf{x}\|^2 \le 0 \implies |\langle \mathbf{x}, \mathbf{y} \rangle| \le \|\mathbf{x}\| \cdot \|\mathbf{y}\| \quad \blacksquare$$

---

### 19.2. Pojęcia topologiczne w $\mathbb{R}^n$

#### Definicja 19.3 (Kula, otoczenie, zbiory otwarte i domknięte)
Niech $\mathbf{x}_0 \in \mathbb{R}^n$ oraz $r > 0$.
1. **Kulą otwartą** o środku $\mathbf{x}_0$ i promieniu $r$ nazywamy zbiór:
   $$K(\mathbf{x}_0, r) = B(\mathbf{x}_0, r) = \{ \mathbf{x} \in \mathbb{R}^n : \|\mathbf{x} - \mathbf{x}_0\| < r \}$$
2. **Kulą domkniętą** nazywamy:
   $$\overline{K}(\mathbf{x}_0, r) = \{ \mathbf{x} \in \mathbb{R}^n : \|\mathbf{x} - \mathbf{x}_0\| \le r \}$$
3. **Otoczeniem punktu** $\mathbf{x}_0$ nazywamy dowolny zbiór $U \subset \mathbb{R}^n$ zawierający pewną kulę otwartą $K(\mathbf{x}_0, r)$.
4. Punkt $\mathbf{x}_0 \in A$ nazywamy **punktem wewnętrznym** zbioru $A$, jeżeli istnieje $r > 0$ takie, że $K(\mathbf{x}_0, r) \subset A$. Zbiór wszystkich punktów wewnętrznych oznaczamy $\operatorname{Int}(A)$.
5. Zbiór $A \subset \mathbb{R}^n$ jest **otwarty**, jeżeli każdy jego punkt jest punktem wewnętrznym ($A = \operatorname{Int}(A)$).
6. Zbiór $A \subset \mathbb{R}^n$ jest **domknięty**, jeżeli jego dopełnienie $\mathbb{R}^n \setminus A$ jest zbiorem otwartym.
7. Punkt $\mathbf{x}_0 \in \mathbb{R}^n$ nazywamy **punktem skupienia** zbioru $A$, jeżeli w każdym otoczeniu punktu $\mathbf{x}_0$ znajduje się co najmniej jeden punkt zbioru $A$ różny od $\mathbf{x}_0$.
8. **Brzegiem zbioru** $A$, oznaczanym $\partial A$ lub $\operatorname{Fr}(A)$, nazywamy zbiór punktów $\mathbf{x} \in \mathbb{R}^n$, których każde otoczenie zawiera co najmniej jeden punkt należący do $A$ i co najmniej jeden punkt nienależący do $A$.

#### Definicja 19.4 (Zwartość i spójność)
1. Zbiór $K \subset \mathbb{R}^n$ jest **zwarty**, jeżeli z każdego jego pokrycia zbiorami otwartymi można wybrać podpokrycie skończone.
   > **Twierdzenie 19.2 (Heinego-Borela w $\mathbb{R}^n$):**  
   > Podzbiór $K \subset \mathbb{R}^n$ jest zwarty wtedy i tylko wtedy, gdy jest **domknięty i ograniczony** (tzn. zawarty w pewnej kuli $K(\mathbf{0}, R)$).
2. Zbiór $D \subset \mathbb{R}^n$ nazywamy **łukowo spójnym**, jeżeli dowolne dwa punkty $\mathbf{a}, \mathbf{b} \in D$ można połączyć krzywą ciągłą $\gamma: [0, 1] \to D$ taką, że $\gamma(0) = \mathbf{a}$ i $\gamma(1) = \mathbf{b}$.
3. Otwarty i spójny podzbiór $\mathbb{R}^n$ nazywamy **obszarem**.

---

### 19.3. Ciągi w $\mathbb{R}^n$

#### Definicja 19.5 (Zbieżność ciągu punktów)
Ciąg punktów $(\mathbf{x}^{(k)})_{k=1}^\infty \subset \mathbb{R}^n$, gdzie $\mathbf{x}^{(k)} = (x_1^{(k)}, x_2^{(k)}, \dots, x_n^{(k)})$, jest **zbieżny** do punktu $\mathbf{x}_0 = (x_{1,0}, \dots, x_{n,0})$, co zapisujemy $\lim_{k\to\infty} \mathbf{x}^{(k)} = \mathbf{x}_0$, jeżeli:
$$\forall \varepsilon > 0 \quad \exists N \in \mathbb{N} \quad \forall k > N : \quad \|\mathbf{x}^{(k)} - \mathbf{x}_0\| < \varepsilon$$

> **Twierdzenie 19.3 (Zbieżność po współrzędnych):**  
> Ciąg $(\mathbf{x}^{(k)})$ w $\mathbb{R}^n$ jest zbieżny do $\mathbf{x}_0$ wtedy i tylko wtedy, gdy jest zbieżny po każdej współrzędnej z osobna w $\mathbb{R}$:
> $$\lim_{k\to\infty} \mathbf{x}^{(k)} = \mathbf{x}_0 \iff \forall i \in \{1,\dots,n\}: \lim_{k\to\infty} x_i^{(k)} = x_{i,0}$$

---

### 19.4. Granica funkcji wielu zmiennych

Rozważmy funkcję skalarną $f: D \to \mathbb{R}$, gdzie $D \subset \mathbb{R}^n$, oraz niech $\mathbf{x}_0$ będzie punktem skupienia zbioru $D$.

#### Definicja 19.6 (Granica w sensie Heinego i Cauchy'ego)
1. **Definicja Heinego (ciągowa):**  
   Liczba $g \in \mathbb{R}$ jest granicą funkcji $f$ w punkcie $\mathbf{x}_0$, co zapisujemy $\lim_{\mathbf{x} \to \mathbf{x}_0} f(\mathbf{x}) = g$, jeżeli dla każdego ciągu $(\mathbf{x}^{(k)}) \subset D \setminus \{\mathbf{x}_0\}$ zbieżnego do $\mathbf{x}_0$ zachodzi:
   $$\lim_{k\to\infty} f(\mathbf{x}^{(k)}) = g$$
2. **Definicja Cauchy'ego ($\varepsilon-\delta$):**  
   $$\forall \varepsilon > 0 \quad \exists \delta > 0 \quad \forall \mathbf{x} \in D : \quad 0 < \|\mathbf{x} - \mathbf{x}_0\| < \delta \implies |f(\mathbf{x}) - g| < \varepsilon$$

Obie definicje są równoważne.

> **Uwaga krytyczna (Granica podwójna a granice iterowane):**  
> Dla funkcji dwóch zmiennych $f(x, y)$ pojęcie **granicy podwójnej** $\lim_{(x,y)\to(x_0,y_0)} f(x,y)$ oznacza zbieżność po **wszystkich możliwych ścieżkach** zbliżania się do punktu $(x_0, y_0)$ w płaszczyźnie.  
> **Granice iterowane**:
> $$g_1 = \lim_{x \to x_0} \left[ \lim_{y \to y_0} f(x, y) \right], \quad g_2 = \lim_{y \to y_0} \left[ \lim_{x \to x_0} f(x, y) \right]$$
> mogą istnieć i być równe, a granica podwójna może w ogóle nie istnieć!  
> **Przykład pułapki egzaminacyjnej:**  
> Niech $f(x, y) = \frac{x y}{x^2 + y^2}$ dla $(x,y) \neq (0,0)$.
> - Granice iterowane: $\lim_{x\to 0} (\lim_{y\to 0} \frac{xy}{x^2+y^2}) = \lim_{x\to 0} 0 = 0$ oraz $\lim_{y\to 0} (\lim_{x\to 0} \frac{xy}{x^2+y^2}) = 0$.
> - Zbliżanie się wzdłuż prostej $y = kx$:
>   $$\lim_{x \to 0} f(x, kx) = \lim_{x \to 0} \frac{x \cdot kx}{x^2 + k^2 x^2} = \frac{k}{1 + k^2}$$
>   Granica zależy od współczynnika kierunkowego $k$ (dla $k=1$ wynosi $1/2$, dla $k=-1$ wynosi $-1/2$). Zatem granica podwójna $\lim_{(x,y)\to(0,0)} f(x,y)$ **nie istnieje**!

---

### 19.5. Ciągłość funkcji wielu zmiennych

#### Definicja 19.7 (Ciągłość)
Funkcja $f: D \to \mathbb{R}$ jest **ciągła w punkcie** $\mathbf{x}_0 \in D$, jeżeli:
$$\lim_{\mathbf{x} \to \mathbf{x}_0} f(\mathbf{x}) = f(\mathbf{x}_0)$$
Funkcja jest ciągła na zbiorze $D$, jeżeli jest ciągła w każdym punkcie tego zbioru.

> **Twierdzenie 19.4 (Weierstrassa o osiąganiu kresów):**  
> Jeżeli zbiór $K \subset \mathbb{R}^n$ jest zwarty (domknięty i ograniczony), a funkcja $f: K \to \mathbb{R}$ jest ciągła, to:
> 1. Funkcja $f$ jest ograniczona na $K$.
> 2. Funkcja $f$ osiąga swoje kresy na $K$, tzn. istnieją punkty $\mathbf{x}_{\min}, \mathbf{x}_{\max} \in K$ takie, że:
>    $$f(\mathbf{x}_{\min}) = \inf_{\mathbf{x} \in K} f(\mathbf{x}), \quad f(\mathbf{x}_{\max}) = \sup_{\mathbf{x} \in K} f(\mathbf{x})$$

> **Twierdzenie 19.5 (Własność Darboux dla obszarów spójnych):**  
> Jeżeli funkcja $f: D \to \mathbb{R}$ jest ciągła na obszarze spójnym $D \subset \mathbb{R}^n$, oraz dla dwóch punktów $\mathbf{a}, \mathbf{b} \in D$ zachodzi $f(\mathbf{a}) < c < f(\mathbf{b})$, to istnieje punkt $\mathbf{c} \in D$ taki, że $f(\mathbf{c}) = c$.

---

## Rozdział 20: Różniczkowalność, gradient, wzór Taylora i ekstrema

### 20.1. Pochodne cząstkowe I rzędu

Niech funkcja $f: D \to \mathbb{R}$ ($D \subset \mathbb{R}^n$) będzie określona w otoczeniu punktu $\mathbf{x}_0 = (x_{1,0}, \dots, x_{n,0})$.

#### Definicja 20.1 (Pochodna cząstkowa)
Pochodną cząstkową funkcji $f$ względem zmiennej $x_i$ w punkcie $\mathbf{x}_0$ nazywamy granicę:
$$\frac{\partial f}{\partial x_i}(\mathbf{x}_0) = \lim_{h \to 0} \frac{f(x_{1,0}, \dots, x_{i,0} + h, \dots, x_{n,0}) - f(x_{1,0}, \dots, x_{i,0}, \dots, x_{n,0})}{h}$$
Stosowane oznaczenia: $\frac{\partial f}{\partial x_i}(\mathbf{x}_0)$, $f'_{x_i}(\mathbf{x}_0)$, $D_i f(\mathbf{x}_0)$.

Pochodna cząstkowa jest zwykłą pochodną funkcji jednej zmiennej $x_i$, przy założeniu, że wszystkie pozostałe zmienne $x_j$ ($j \neq i$) są traktowane jako stałe parametry.

#### Interpretacja geometryczna dla $z = f(x, y)$:
- Przekrój powierzchni $z = f(x, y)$ płaszczyzną $y = y_0$ daje krzywą $z = f(x, y_0)$. Pochodna $\frac{\partial f}{\partial x}(x_0, y_0)$ jest tangensem kąta nachylenia stycznej do tej krzywej w punkcie $(x_0, y_0, f(x_0, y_0))$.
- Analogicznie $\frac{\partial f}{\partial y}(x_0, y_0)$ to tangens nachylenia stycznej do krzywej powstałej z przekroju płaszczyzną $x = x_0$.

> **Uwaga krytyczna:**  
> Istnienie wszystkich pochodnych cząstkowych w punkcie **nie gwarantuje nawet ciągłości** funkcji w tym punkcie!  
> Funkcja:
> $$f(x, y) = \begin{cases} \frac{xy}{x^2 + y^2} & \text{dla } (x, y) \neq (0, 0) \\ 0 & \text{dla } (x, y) = (0, 0) \end{cases}$$
> ma pochodne cząstkowe w $(0, 0)$: $\frac{\partial f}{\partial x}(0, 0) = \lim_{h\to 0} \frac{0 - 0}{h} = 0$, $\frac{\partial f}{\partial y}(0, 0) = 0$, ale jak wykazano w Rozdziale 19, nie jest ciągła w $(0, 0)$.

Właściwym pojęciem uogólniającym różniczkowalność z jednej zmiennej jest **różniczkowalność w sensie Frécheta (różniczka zupełna)**.

---

### 20.2. Różniczkowalność i różniczka zupełna

#### Definicja 20.2 (Różniczkowalność w punkcie)
Funkcja $f: D \to \mathbb{R}$ jest **różniczkowalna** w punkcie wewnętrznym $\mathbf{x}_0 \in D$, jeżeli istnieje funkcjonał liniowy $L: \mathbb{R}^n \to \mathbb{R}$ (reprezentowany przez wektor $\mathbf{A} = (A_1, \dots, A_n)$) taki, że:
$$\lim_{\mathbf{h} \to \mathbf{0}} \frac{f(\mathbf{x}_0 + \mathbf{h}) - f(\mathbf{x}_0) - L(\mathbf{h})}{\|\mathbf{h}\|} = 0$$
gdzie $L(\mathbf{h}) = \sum_{i=1}^n A_i h_i$.

> **Twierdzenie 20.1 (Warunek konieczny różniczkowalności):**  
> Jeżeli funkcja $f$ jest różniczkowalna w punkcie $\mathbf{x}_0$, to:
> 1. Jest ciągła w punkcie $\mathbf{x}_0$.
> 2. Posiada wszystkie pochodne cząstkowe w punkcie $\mathbf{x}_0$, przy czym:
>    $$A_i = \frac{\partial f}{\partial x_i}(\mathbf{x}_0), \quad i = 1, \dots, n$$

#### Definicja 20.3 (Różniczka zupełna)
Jeżeli funkcja $f$ jest różniczkowalna w $\mathbf{x}_0$, to formę liniową:
$$df(\mathbf{x}_0, \mathbf{h}) = \sum_{i=1}^n \frac{\partial f}{\partial x_i}(\mathbf{x}_0) h_i = \frac{\partial f}{\partial x_1}(\mathbf{x}_0) dx_1 + \dots + \frac{\partial f}{\partial x_n}(\mathbf{x}_0) dx_n$$
nazywamy **różniczką zupełną** funkcji $f$ w punkcie $\mathbf{x}_0$.

> **Twierdzenie 20.2 (Warunek wystarczający różniczkowalności):**  
> Jeżeli pochodne cząstkowe $\frac{\partial f}{\partial x_i}$ istnieją w otoczeniu punktu $\mathbf{x}_0$ i są **ciągłe** w punkcie $\mathbf{x}_0$, to funkcja $f$ jest różniczkowalna w punkcie $\mathbf{x}_0$.

#### Geometryczne zastosowanie: Płaszczyzna styczna do powierzchni
Jeżeli funkcja $z = f(x, y)$ jest różniczkowalna w punkcie $(x_0, y_0)$, to wykres funkcji posiada w punkcie $P_0(x_0, y_0, f(x_0, y_0))$ **płaszczyznę styczną** o równaniu:
$$z - f(x_0, y_0) = \frac{\partial f}{\partial x}(x_0, y_0)(x - x_0) + \frac{\partial f}{\partial y}(x_0, y_0)(y - y_0)$$
Wektor normalny do płaszczyzny stycznej:
$$\vec{n} = \left[ \frac{\partial f}{\partial x}(x_0, y_0), \; \frac{\partial f}{\partial y}(x_0, y_0), \; -1 \right]$$
Równanie prostej **normalnej**:
$$\frac{x - x_0}{\frac{\partial f}{\partial x}(x_0, y_0)} = \frac{y - y_0}{\frac{\partial f}{\partial y}(x_0, y_0)} = \frac{z - f(x_0, y_0)}{-1}$$

---

### 20.3. Gradient i pochodna kierunkowa

#### Definicja 20.4 (Gradient)
**Gradientem** funkcji różniczkowalnej $f$ w punkcie $\mathbf{x}_0$ nazywamy wektor złożony z pochodnych cząstkowych:
$$\nabla f(\mathbf{x}_0) = \operatorname{grad} f(\mathbf{x}_0) = \left[ \frac{\partial f}{\partial x_1}(\mathbf{x}_0), \frac{\partial f}{\partial x_2}(\mathbf{x}_0), \dots, \frac{\partial f}{\partial x_n}(\mathbf{x}_0) \right]^T$$

#### Definicja 20.5 (Pochodna kierunkowa)
Niech $\vec{v} \in \mathbb{R}^n$ będzie wektorem jednostkowym ($\|\vec{v}\| = 1$). **Pochodną kierunkową** funkcji $f$ w punkcie $\mathbf{x}_0$ w kierunku wektora $\vec{v}$ nazywamy granicę:
$$\frac{\partial f}{\partial \vec{v}}(\mathbf{x}_0) = \lim_{t \to 0^+} \frac{f(\mathbf{x}_0 + t\vec{v}) - f(\mathbf{x}_0)}{t}$$

> **Twierdzenie 20.3 (Obliczanie pochodnej kierunkowej za pomocą gradientu):**  
> Jeżeli funkcja $f$ jest różniczkowalna w punkcie $\mathbf{x}_0$, to dla dowolnego wektora jednostkowego $\vec{v}$:
> $$\frac{\partial f}{\partial \vec{v}}(\mathbf{x}_0) = \langle \nabla f(\mathbf{x}_0), \vec{v} \rangle = \nabla f(\mathbf{x}_0) \cdot \vec{v}$$

#### Kluczowe własności gradientu i interpretacja fizyczno-inżynierska:
1. **Kierunek najszybszego wzrostu:**  
   Z nierówności Cauchy'ego-Schwarza:
   $$\frac{\partial f}{\partial \vec{v}}(\mathbf{x}_0) = \|\nabla f(\mathbf{x}_0)\| \|\vec{v}\| \cos \theta = \|\nabla f(\mathbf{x}_0)\| \cos \theta \le \|\nabla f(\mathbf{x}_0)\|$$
   Wartość maksymalna jest osiągana dla $\cos \theta = 1$, czyli gdy wektor $\vec{v}$ ma kierunek i zwrot zgodny z gradientem $\nabla f(\mathbf{x}_0)$.  
   - Wektor gradientu wskazuje **kierunek najszybszego wzrostu wartości funkcji**, a jego długość $\|\nabla f(\mathbf{x}_0)\|$ jest maksymalną szybkością tego wzrostu.
   - Wektor $-\nabla f(\mathbf{x}_0)$ (antygradient) wskazuje **kierunek najszybszego spadku** (fundament metody *Gradient Descent* w uczeniu maszynowym: $\mathbf{w}_{k+1} = \mathbf{w}_k - \eta \nabla L(\mathbf{w}_k)$).
2. **Prostopadłość do poziomic (powierzchni ekwipotencjalnych):**  
   Gradient funkcji $f$ w każdym punkcie jest prostopadły do poziomicy (linii stałej wartości $f(x, y) = c$) przechodzącej przez ten punkt.
3. **Elektrostatyka:**  
   Potencjał elektrostatyczny $V(x, y, z)$ określa wektor natężenia pola elektrycznego $\vec{E}$:
   $$\vec{E} = -\nabla V = -\left[ \frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}, \frac{\partial V}{\partial z} \right]$$
   Linie sił pola elektrycznego są zawsze ortogonalne do powierzchni ekwipotencjalnych $V = \text{const}$.

---

### 20.4. Pochodne cząstkowe wyższych rzędów i twierdzenie Schwarza

Pochodne cząstkowe rzędu drugiego definiujemy indukcyjnie:
$$\frac{\partial^2 f}{\partial x_j \partial x_i} = \frac{\partial}{\partial x_j} \left( \frac{\partial f}{\partial x_i} \right)$$
Dla $i \neq j$ pochodne te nazywamy **pochodnymi cząstkowymi mieszanymi**.

> **Twierdzenie 20.4 (Schwarza o równości pochodnych mieszanych):**  
> Jeżeli pochodne cząstkowe $\frac{\partial f}{\partial x_i}$, $\frac{\partial f}{\partial x_j}$, $\frac{\partial^2 f}{\partial x_i \partial x_j}$ oraz $\frac{\partial^2 f}{\partial x_j \partial x_i}$ istnieją w otoczeniu punktu $\mathbf{x}_0$ i pochodne mieszane są **ciągłe** w punkcie $\mathbf{x}_0$, to są w tym punkcie równe:
> $$\frac{\partial^2 f}{\partial x_i \partial x_j}(\mathbf{x}_0) = \frac{\partial^2 f}{\partial x_j \partial x_i}(\mathbf{x}_0)$$

**Dowód (dla funkcji dwóch zmiennych $f(x, y)$):**  
Rozważmy wyrażenie podwójnego przyrostu dla małych $h, k > 0$:
$$W(h, k) = f(x_0 + h, y_0 + k) - f(x_0 + h, y_0) - f(x_0, y_0 + k) + f(x_0, y_0)$$
Zdefiniujmy funkcję pomocniczą $\varphi(x) = f(x, y_0 + k) - f(x, y_0)$. Wówczas:
$$W(h, k) = \varphi(x_0 + h) - \varphi(x_0)$$
Z twierdzenia Lagrange'a o wartości średniej dla $\varphi$ na przedziale $[x_0, x_0 + h]$ istnieje $\theta_1 \in (0, 1)$ takie, że:
$$W(h, k) = h \varphi'(x_0 + \theta_1 h) = h \left[ \frac{\partial f}{\partial x}(x_0 + \theta_1 h, y_0 + k) - \frac{\partial f}{\partial x}(x_0 + \theta_1 h, y_0) \right]$$
Stosując ponownie twierdzenie Lagrange'a do funkcji $y \mapsto \frac{\partial f}{\partial x}(x_0 + \theta_1 h, y)$ na przedziale $[y_0, y_0 + k]$, otrzymujemy dla pewnego $\theta_2 \in (0, 1)$:
$$W(h, k) = h k \frac{\partial^2 f}{\partial y \partial x}(x_0 + \theta_1 h, y_0 + \theta_2 k)$$
Definiując symetrycznie $\psi(y) = f(x_0 + h, y) - f(x_0, y)$ i powtarzając procedurę, otrzymujemy istnienie $\theta_3, \theta_4 \in (0, 1)$ takich, że:
$$W(h, k) = h k \frac{\partial^2 f}{\partial x \partial y}(x_0 + \theta_3 h, y_0 + \theta_4 k)$$
Dzieląc przez $hk \neq 0$ i przechodząc do granicy przy $(h, k) \to (0, 0)$, z ciągłości obu pochodnych mieszanych w punkcie $(x_0, y_0)$ dostajemy:
$$\frac{\partial^2 f}{\partial y \partial x}(x_0, y_0) = \frac{\partial^2 f}{\partial x \partial y}(x_0, y_0) \quad \blacksquare$$

---

### 20.5. Wzór Taylora i macierz Hessego

#### Definicja 20.6 (Macierz Hessego)
Niech $f: D \to \mathbb{R}$ będzie funkcją dwukrotnie różniczkowalną w sposób ciągły ($C^2$). **Macierzą Hessego (hesjanem)** funkcji $f$ w punkcie $\mathbf{x}_0$ nazywamy symetryczną macierz drugich pochodnych cząstkowych:
$$H_f(\mathbf{x}_0) = \nabla^2 f(\mathbf{x}_0) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x_1^2} & \frac{\partial^2 f}{\partial x_1 \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f}{\partial x_2 \partial x_1} & \frac{\partial^2 f}{\partial x_2^2} & \dots & \frac{\partial^2 f}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f}{\partial x_n \partial x_1} & \frac{\partial^2 f}{\partial x_n \partial x_2} & \dots & \frac{\partial^2 f}{\partial x_n^2}
\end{bmatrix}_{(\mathbf{x}_0)}$$

> **Twierdzenie 20.5 (Wzór Taylora rzędu drugiego):**  
> Jeżeli funkcja $f$ jest klasy $C^2$ w otoczeniu punktu $\mathbf{x}_0$, to dla małego wektora przyrostu $\mathbf{h} = (h_1, \dots, h_n)$:
> $$f(\mathbf{x}_0 + \mathbf{h}) = f(\mathbf{x}_0) + \nabla f(\mathbf{x}_0)^T \mathbf{h} + \frac{1}{2} \mathbf{h}^T H_f(\mathbf{x}_0) \mathbf{h} + o(\|\mathbf{h}\|^2)$$
> Wyrażenie $Q(\mathbf{h}) = \mathbf{h}^T H_f(\mathbf{x}_0) \mathbf{h} = \sum_{i=1}^n \sum_{j=1}^n \frac{\partial^2 f}{\partial x_i \partial x_j}(\mathbf{x}_0) h_i h_j$ jest **formą kwadratową różniczki drugiego rzędu** $d^2 f(\mathbf{x}_0, \mathbf{h})$.

---

### 20.6. Ekstrema lokalne bezwarunkowe

#### Definicja 20.7 (Ekstremum lokalne)
Funkcja $f: D \to \mathbb{R}$ ma w punkcie $\mathbf{x}_0 \in D$:
1. **Minimum lokalne właściwe**, jeżeli istnieje otoczenie $U(\mathbf{x}_0)$ takie, że $\forall \mathbf{x} \in U(\mathbf{x}_0) \setminus \{\mathbf{x}_0\}: f(\mathbf{x}) > f(\mathbf{x}_0)$.
2. **Maksimum lokalne właściwe**, jeżeli istnieje otoczenie $U(\mathbf{x}_0)$ takie, że $\forall \mathbf{x} \in U(\mathbf{x}_0) \setminus \{\mathbf{x}_0\}: f(\mathbf{x}) < f(\mathbf{x}_0)$.

> **Twierdzenie 20.6 (Warunek konieczny istnienia ekstremum - Lemat Fermata):**  
> Jeżeli funkcja $f$ posiada w punkcie wewnętrznym $\mathbf{x}_0$ ekstremum lokalne i jest w nim różniczkowalna, to jej gradient zeruje się w tym punkcie:
> $$\nabla f(\mathbf{x}_0) = \mathbf{0} \iff \frac{\partial f}{\partial x_1}(\mathbf{x}_0) = 0, \; \frac{\partial f}{\partial x_2}(\mathbf{x}_0) = 0, \; \dots, \; \frac{\partial f}{\partial x_n}(\mathbf{x}_0) = 0$$
> Punkty spełniające $\nabla f(\mathbf{x}_0) = \mathbf{0}$ nazywamy **punktami stacjonarnymi (krytycznymi)**.

> **Twierdzenie 20.7 (Warunek dostateczny istnienia ekstremum):**  
> Niech $\mathbf{x}_0$ będzie punktem stacjonarnym funkcji $f \in C^2$.
> 1. Jeżeli forma kwadratowa hesjanu $Q(\mathbf{h}) = \mathbf{h}^T H_f(\mathbf{x}_0) \mathbf{h}$ jest **dodatnio określona** ($Q(\mathbf{h}) > 0$ dla $\mathbf{h} \neq \mathbf{0}$), to funkcja $f$ ma w $\mathbf{x}_0$ **minimum lokalne właściwe**.
> 2. Jeżeli forma jest **ujemnie określona** ($Q(\mathbf{h}) < 0$ dla $\mathbf{h} \neq \mathbf{0}$), to funkcja ma w $\mathbf{x}_0$ **maksimum lokalne właściwe**.
> 3. Jeżeli forma jest **nieokreślona** (przyjmuje wartości zarówno dodatnie, jak i ujemne), to funkcja **nie ma ekstremum** w $\mathbf{x}_0$ (punkt $\mathbf{x}_0$ jest **punktem siodłowym**).
> 4. W przypadku formy półokreślonej kryterium nie rozstrzyga o istnieniu ekstremum.

#### Kryterium Sylvestera dla funkcji dwóch zmiennych $f(x, y)$:
Niech $(x_0, y_0)$ będzie punktem stacjonarnym. Oznaczmy:
$$A = \frac{\partial^2 f}{\partial x^2}(x_0, y_0), \quad B = \frac{\partial^2 f}{\partial x \partial y}(x_0, y_0), \quad C = \frac{\partial^2 f}{\partial y^2}(x_0, y_0)$$
Wyznacznik macierzy Hessego:
$$\Delta = \det H_f(x_0, y_0) = \det \begin{bmatrix} A & B \\ B & C \end{bmatrix} = A C - B^2$$
- **Przypadek 1:** Jeżeli $\Delta > 0$:
  - gdy $A > 0$ (lub $C > 0$), to w punkcie $(x_0, y_0)$ występuje **minimum lokalne właściwe**,
  - gdy $A < 0$ (lub $C < 0$), to w punkcie $(x_0, y_0)$ występuje **maksimum lokalne właściwe**.
- **Przypadek 2:** Jeżeli $\Delta < 0$, to w punkcie $(x_0, y_0)$ **nie ma ekstremum** (punkt siodłowy).
- **Przypadek 3:** Jeżeli $\Delta = 0$, to kryterium nie rozstrzyga (konieczne jest badanie zachowania funkcji wyższych rzędów lub z definicji).

---

### 20.7. Ekstrema warunkowe i metoda mnożników Lagrange'a

W optymalizacji inżynierskiej szukamy często ekstremum funkcji celu $f(\mathbf{x})$ przy ograniczeniach równościowych (np. maksymalizacja przepustowości kanału transmisyjnego przy ustalonej mocy nadajnika, dopasowanie impedancji odbiornika do źródła).

Rozważmy problem wyznaczenia ekstremum funkcji $f(x_1, \dots, x_n)$ przy $m$ warunkach wiążących ($m < n$):
$$g_j(x_1, \dots, x_n) = 0, \quad j = 1, \dots, m$$

#### Definicja 20.8 (Funkcja Lagrange'a)
Tworzymy funkcję Lagrange'a:
$$\Phi(x_1, \dots, x_n, \lambda_1, \dots, \lambda_m) = f(\mathbf{x}) + \sum_{j=1}^m \lambda_j g_j(\mathbf{x})$$
gdzie parametry $\lambda_1, \dots, \lambda_m \in \mathbb{R}$ nazywamy **mnożnikami Lagrange'a**.

> **Twierdzenie 20.8 (Warunek konieczny istnienia ekstremum warunkowego):**  
> Jeżeli w punkcie $\mathbf{x}_0$ spełniającym więzy $g_j(\mathbf{x}_0) = 0$ funkcja $f$ ma ekstremum warunkowe, a gradienty więzów $\nabla g_1(\mathbf{x}_0), \dots, \nabla g_m(\mathbf{x}_0)$ są liniowo niezależne (tzw. warunek regularności więzów), to istnieją liczby $\lambda_1, \dots, \lambda_m$ takie, że:
> $$\nabla_{\mathbf{x}, \boldsymbol{\lambda}} \Phi = \mathbf{0} \iff \begin{cases}
> \frac{\partial \Phi}{\partial x_i} = \frac{\partial f}{\partial x_i} + \sum_{j=1}^m \lambda_j \frac{\partial g_j}{\partial x_i} = 0, & i = 1, \dots, n \\
> \frac{\partial \Phi}{\partial \lambda_j} = g_j(\mathbf{x}) = 0, & j = 1, \dots, m
> \end{cases}$$

#### Interpretacja geometryczna:
Dla $f(x, y)$ i jednego więzu $g(x, y) = 0$, warunek konieczny oznacza, że w punkcie ekstremum warunkowego wektor gradientu funkcji celu $\nabla f$ jest równoległy do wektora gradientu więzu $\nabla g$:
$$\nabla f(x_0, y_0) = -\lambda \nabla g(x_0, y_0)$$
Oznacza to, że linia poziomicowa funkcji $f$ jest styczna do krzywej więzów $g(x, y) = 0$.

---

### 20.8. Funkcje uwikłane

Równanie $F(x, y) = 0$ definiuje relację między zmiennymi $x$ i $y$. Jeżeli dla każdego $x$ z pewnego przedziału istnieje dokładnie jedno $y = y(x)$ spełniające to równanie, mówimy o **funkcji uwikłanej**.

> **Twierdzenie 20.9 (O istnieniu i różniczkowalności funkcji uwikłanej):**  
> Niech funkcja $F(x, y)$ będzie klasy $C^1$ w otoczeniu punktu $(x_0, y_0)$ oraz:
> 1. $F(x_0, y_0) = 0$,
> 2. $\frac{\partial F}{\partial y}(x_0, y_0) \neq 0$.  
> 
> Wówczas:
> 1. Istnieje otoczenie $U = (x_0 - \delta, x_0 + \delta)$ oraz $V = (y_0 - \varepsilon, y_0 + \varepsilon)$ takie, że dla każdego $x \in U$ istnieje dokładnie jedno $y = y(x) \in V$ spełniające $F(x, y(x)) = 0$.
> 2. Funkcja $y(x)$ jest klasy $C^1$ na $U$, a jej pochodna wyraża się wzorem:
>    $$y'(x) = -\frac{\frac{\partial F}{\partial x}(x, y(x))}{\frac{\partial F}{\partial y}(x, y(x))}$$

Pochodną drugiego rzędu $y''(x)$ obliczamy różniczkując tożsamość $F'_x(x, y(x)) + F'_y(x, y(x)) y'(x) = 0$ po zmiennej $x$:
$$y''(x) = -\frac{F''_{xx} + 2 F''_{xy} y' + F''_{yy} (y')^2}{F'_y}$$
W punkcie stacjonarnym funkcji uwikłanej, gdzie $y'(x_0) = 0$ (czyli $F'_x(x_0, y_0) = 0$), wzór ten upraszcza się do:
$$y''(x_0) = -\frac{F''_{xx}(x_0, y_0)}{F'_y(x_0, y_0)}$$
co pozwala natychmiast rozstrzygnąć o istnieniu ekstremum lokalnego funkcji uwikłanej ($y''(x_0) > 0 \implies \min$, $y''(x_0) < 0 \implies \max$).

---

### 20.9. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 20.1 (Badanie różniczkowalności funkcji w punkcie)
Zbadać ciągłość i różniczkowalność funkcji $f: \mathbb{R}^2 \to \mathbb{R}$ w punkcie $(0, 0)$:
$$f(x, y) = \begin{cases} \frac{x^3 - y^3}{x^2 + y^2} & \text{dla } (x, y) \neq (0, 0) \\ 0 & \text{dla } (x, y) = (0, 0) \end{cases}$$

**Rozwiązanie:**  
1. **Ciągłość w $(0, 0)$:**  
   Przechodzimy do współrzędnych biegunowych: $x = r \cos \varphi$, $y = r \sin \varphi$, gdzie $r \to 0^+$:
   $$|f(x, y) - f(0, 0)| = \left| \frac{r^3(\cos^3 \varphi - \sin^3 \varphi)}{r^2} \right| = r |\cos^3 \varphi - \sin^3 \varphi| \le 2r$$
   Ponieważ $\lim_{r \to 0^+} 2r = 0$, na mocy twierdzenia o trzech funkcjach $\lim_{(x,y)\to(0,0)} f(x, y) = 0 = f(0, 0)$. Zatem funkcja $f$ jest **ciągła** w punkcie $(0, 0)$.

2. **Pochodne cząstkowe w $(0, 0)$:**  
   $$\frac{\partial f}{\partial x}(0, 0) = \lim_{h \to 0} \frac{f(h, 0) - f(0, 0)}{h} = \lim_{h \to 0} \frac{\frac{h^3}{h^2} - 0}{h} = \lim_{h \to 0} \frac{h}{h} = 1$$
   $$\frac{\partial f}{\partial y}(0, 0) = \lim_{k \to 0} \frac{f(0, k) - f(0, 0)}{k} = \lim_{k \to 0} \frac{\frac{-k^3}{k^2} - 0}{k} = \lim_{k \to 0} \frac{-k}{k} = -1$$
   Obie pochodne cząstkowe istnieją i wynoszą: $\nabla f(0, 0) = [1, -1]^T$.

3. **Badanie różniczkowalności z definicji:**  
   Zgodnie z Definicją 20.2 badamy granicę wyrażenia dla $\mathbf{h} = (h_1, h_2) \to (0, 0)$:
   $$\lim_{(h_1, h_2) \to (0, 0)} \frac{f(h_1, h_2) - f(0, 0) - \left( \frac{\partial f}{\partial x}(0, 0) h_1 + \frac{\partial f}{\partial y}(0, 0) h_2 \right)}{\sqrt{h_1^2 + h_2^2}}$$
   Licznik:
   $$\frac{h_1^3 - h_2^3}{h_1^2 + h_2^2} - (h_1 - h_2) = \frac{h_1^3 - h_2^3 - (h_1 - h_2)(h_1^2 + h_2^2)}{h_1^2 + h_2^2} = \frac{-h_1 h_2^2 + h_1^2 h_2}{h_1^2 + h_2^2}$$
   Dzieląc przez $\|\mathbf{h}\| = \sqrt{h_1^2 + h_2^2}$:
   $$g(h_1, h_2) = \frac{h_1^2 h_2 - h_1 h_2^2}{(h_1^2 + h_2^2)^{3/2}}$$
   Niech $(h_1, h_2)$ dąży do $(0, 0)$ po prostej $h_2 = h_1$ ($h_1 > 0$):
   $$g(h_1, h_1) = \frac{h_1^3 - h_1^3}{(2h_1^2)^{3/2}} = 0$$
   Niech $(h_1, h_2)$ dąży po prostej $h_2 = 2 h_1$ ($h_1 > 0$):
   $$g(h_1, 2h_1) = \frac{h_1^2(2h_1) - h_1(4h_1^2)}{(h_1^2 + 4h_1^2)^{3/2}} = \frac{2h_1^3 - 4h_1^3}{(5h_1^2)^{3/2}} = \frac{-2 h_1^3}{5\sqrt{5} h_1^3} = -\frac{2}{5\sqrt{5}} \neq 0$$
   Granica zależy od kierunku i nie jest równa zeru. Zatem funkcja $f$ **nie jest różniczkowalna** w punkcie $(0, 0)$, pomimo że jest w nim ciągła i posiada obie pochodne cząstkowe! $\blacksquare$

---

#### Przykład 20.2 (Pochodna kierunkowa i wektor gradientu)
Dana jest funkcja potencjału $V(x, y, z) = x^2 y - y z^2 + 2 x z$.
1. Wyznaczyć gradient $\nabla V$ w punkcie $P_0(1, 2, -1)$.
2. Obliczyć pochodną kierunkową w punkcie $P_0$ w kierunku wektora $\vec{a} = [2, -1, 2]^T$.
3. Wyznaczyć kierunek i zwrot maksymalnego wzrostu potencjału oraz obliczyć maksymalną wartość tego wzrostu.

**Rozwiązanie:**  
1. Obliczamy pochodne cząstkowe:
   $$\frac{\partial V}{\partial x} = 2xy + 2z, \quad \frac{\partial V}{\partial y} = x^2 - z^2, \quad \frac{\partial V}{\partial z} = -2yz + 2x$$
   W punkcie $P_0(1, 2, -1)$:
   $$\frac{\partial V}{\partial x}(P_0) = 2(1)(2) + 2(-1) = 4 - 2 = 2$$
   $$\frac{\partial V}{\partial y}(P_0) = 1^2 - (-1)^2 = 1 - 1 = 0$$
   $$\frac{\partial V}{\partial z}(P_0) = -2(2)(-1) + 2(1) = 4 + 2 = 6$$
   Zatem gradient wynosi: $\nabla V(P_0) = [2, 0, 6]^T$.

2. Normalizujemy wektor $\vec{a}$ do wektora jednostkowego:
   $$\|\vec{a}\| = \sqrt{2^2 + (-1)^2 + 2^2} = \sqrt{4 + 1 + 4} = \sqrt{9} = 3 \implies \vec{v} = \frac{\vec{a}}{\|\vec{a}\|} = \left[ \frac{2}{3}, -\frac{1}{3}, \frac{2}{3} \right]^T$$
   Pochodna kierunkowa:
   $$\frac{\partial V}{\partial \vec{v}}(P_0) = \nabla V(P_0) \cdot \vec{v} = 2 \left(\frac{2}{3}\right) + 0 \left(-\frac{1}{3}\right) + 6 \left(\frac{2}{3}\right) = \frac{4}{3} + \frac{12}{3} = \frac{16}{3}$$

3. Kierunek maksymalnego wzrostu wyznacza znormalizowany wektor gradientu:
   $$\vec{u}_{\max} = \frac{\nabla V(P_0)}{\|\nabla V(P_0)\|} = \frac{[2, 0, 6]^T}{\sqrt{2^2 + 0^2 + 6^2}} = \frac{[2, 0, 6]^T}{\sqrt{40}} = \left[ \frac{1}{\sqrt{10}}, 0, \frac{3}{\sqrt{10}} \right]^T$$
   Maksymalna szybkość wzrostu wynosi:
   $$\|\nabla V(P_0)\| = \sqrt{40} = 2\sqrt{10}$$

---

#### Przykład 20.3 (Wyznaczanie ekstremów lokalnych bezwarunkowych)
Wyznaczyć wszystkie ekstrema lokalne funkcji $f(x, y) = x^3 + y^3 - 3xy$.

**Rozwiązanie:**  
1. **Warunek konieczny (punkty stacjonarne):**  
   $$\begin{cases} \frac{\partial f}{\partial x} = 3x^2 - 3y = 0 \implies y = x^2 \\ \frac{\partial f}{\partial y} = 3y^2 - 3x = 0 \implies x = y^2 \end{cases}$$
   Wstawiając $y = x^2$ do drugiego równania:
   $$x = (x^2)^2 = x^4 \implies x(x^3 - 1) = 0 \implies x(x - 1)(x^2 + x + 1) = 0$$
   Jedyne pierwiastki rzeczywiste to $x_1 = 0$ oraz $x_2 = 1$.
   - Dla $x_1 = 0 \implies y_1 = 0^2 = 0 \implies P_1(0, 0)$.
   - Dla $x_2 = 1 \implies y_2 = 1^2 = 1 \implies P_2(1, 1)$.

2. **Warunek dostateczny (Macierz Hessego):**  
   Pochodne drugiego rzędu:
   $$\frac{\partial^2 f}{\partial x^2} = 6x, \quad \frac{\partial^2 f}{\partial x \partial y} = -3, \quad \frac{\partial^2 f}{\partial y^2} = 6y$$
   Hesjan:
   $$H_f(x, y) = \begin{bmatrix} 6x & -3 \\ -3 & 6y \end{bmatrix}, \quad \Delta(x, y) = \det H_f(x, y) = 36xy - 9$$

3. **Klasyfikacja punktów:**  
   - **W punkcie $P_1(0, 0)$:**
     $$\Delta(0, 0) = 36(0)(0) - 9 = -9 < 0$$
     Wyznacznik jest ujemny, zatem forma kwadratowa jest nieokreślona. W punkcie $P_1(0, 0)$ funkcja **nie ma ekstremum** (jest to punkt siodłowy).
   - **W punkcie $P_2(1, 1)$:**
     $$\Delta(1, 1) = 36(1)(1) - 9 = 27 > 0$$
     Ponieważ $\Delta > 0$ oraz $A = \frac{\partial^2 f}{\partial x^2}(1, 1) = 6 > 0$, forma jest dodatnio określona.
     Zatem w punkcie $P_2(1, 1)$ funkcja posiada **minimum lokalne właściwe**.
     Wartość minimum wynosi:
     $$f_{\min} = f(1, 1) = 1^3 + 1^3 - 3(1)(1) = 2 - 3 = -1$$

---

#### Przykład 20.4 (Ekstremum warunkowe - maksymalizacja mocy doprowadzonej do obciążenia)
W obwodzie elektrycznym moc wydzielana na impedancji obciążenia o zmiennej konduktancji $g$ i susceptancji $b$ zasilanej ze źródła nieliniowego modelowana jest funkcją:
$$P(x, y) = 4 x y$$
gdzie zmienne $x, y > 0$ podlegają ograniczeniu wynikającemu z dopuszczalnego spadku napięcia na linii zasilającej:
$$g(x, y) = \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1 = 0 \quad (a, b > 0)$$
Wyznaczyć wartości parametrów $(x, y)$ maksymalizujące wydzielaną moc.

**Rozwiązanie:**  
Stosujemy metodę mnożników Lagrange'a. Funkcja Lagrange'a:
$$\Phi(x, y, \lambda) = 4xy + \lambda \left( \frac{x^2}{a^2} + \frac{y^2}{b^2} - 1 \right)$$
Układ równań warunku koniecznego:
$$\begin{cases}
\frac{\partial \Phi}{\partial x} = 4y + \frac{2\lambda x}{a^2} = 0 \implies \lambda x = -2a^2 y \\
\frac{\partial \Phi}{\partial y} = 4x + \frac{2\lambda y}{b^2} = 0 \implies \lambda y = -2b^2 x \\
\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1
\end{cases}$$
Ponieważ szukamy rozwiązań w pierwszym kwadrancie ($x > 0, y > 0$), mnożąc pierwsze równanie przez $x$, a drugie przez $y$:
$$\lambda x^2 = -2a^2 xy, \quad \lambda y^2 = -2b^2 xy$$
Dzieląc stronami:
$$\frac{x^2}{y^2} = \frac{a^2}{b^2} \implies \frac{x^2}{a^2} = \frac{y^2}{b^2}$$
Wstawiając tę zależność do równania elipsy więzów:
$$\frac{x^2}{a^2} + \frac{x^2}{a^2} = 1 \implies \frac{2x^2}{a^2} = 1 \implies x = \frac{a}{\sqrt{2}}$$
Podobnie:
$$\frac{2y^2}{b^2} = 1 \implies y = \frac{b}{\sqrt{2}}$$
Wartość maksymalnej mocy:
$$P_{\max} = 4 \left(\frac{a}{\sqrt{2}}\right)\left(\frac{b}{\sqrt{2}}\right) = 2ab$$
Z interpretacji geometrycznej zbiór więzów w I ćwiartce jest łukiem zwartym, a funkcja $P(x,y)$ na brzegach (dla $x=0$ lub $y=0$) przyjmuje wartość zero, zatem punkt $\left(\frac{a}{\sqrt{2}}, \frac{b}{\sqrt{2}}\right)$ realizuje **maksimum globalne warunkowe**.

---

### 20.10. Zadania do samodzielnego rozwiązania

1. **Zadanie 20.1:** Wyznaczyć granice podwójne funkcji lub wykazać, że nie istnieją:  
   a) $\lim_{(x,y)\to(0,0)} \frac{x^2 - y^2}{x^2 + y^2}$,  
   b) $\lim_{(x,y)\to(0,0)} \frac{x^2 y^2}{x^2 + y^2}$,  
   c) $\lim_{(x,y)\to(0,0)} (1 + x^2 + y^2)^{\frac{1}{x^2+y^2}}$.  
   *Odpowiedzi:* a) Nie istnieje (wzdłuż osi $OX$ wynosi 1, wzdłuż $OY$ wynosi $-1$); b) 0 (oszacowanie przez $r^2 \cos^2\varphi \sin^2\varphi \le r^2$); c) $e$.

2. **Zadanie 20.2:** Wyznaczyć równanie płaszczyzny stycznej i prostej normalnej do powierzchni paraboloidy eliptycznej $z = 2x^2 + 3y^2$ w punkcie $P_0(1, -1, 5)$.  
   *Odpowiedź:* Płaszczyzna styczna: $4x - 6y - z - 5 = 0$; prosta normalna: $\frac{x-1}{4} = \frac{y+1}{-6} = \frac{z-5}{-1}$.

3. **Zadanie 20.3:** Wyznaczyć ekstrema lokalne funkcji trzech zmiennych:  
   $$f(x, y, z) = x^2 + y^2 + z^2 + 2x - 4y + 6z + 10$$  
   *Odpowiedź:* Minimum lokalne w punkcie $(-1, 2, -3)$, $f_{\min} = -4$.

4. **Zadanie 20.4:** Wyznaczyć ekstrema lokalne funkcji uwikłanej $y(x)$ zadanej równaniem $x^2 + 2xy + y^2 - 4x + 2y - 5 = 0$.  
   *Odpowiedź:* $y'(x) = -\frac{2x+2y-4}{2x+2y+2}$. Punkt krytyczny $x + y = 2$. Po podstawieniu do równania: $4 - 4x + 2(2-x) - 5 = 0 \implies -6x + 3 = 0 \implies x = 1/2, y = 3/2$. W punkcie tym $y''(1/2) = -1/3 < 0 \implies$ maksimum lokalne $y_{\max} = 3/2$.

5. **Zadanie 20.5:** Znaleźć najmniejszą i największą odległość punktu $A(0, 0)$ od punktów elipsy $5x^2 + 6xy + 5y^2 = 8$.  
   *Odpowiedź:* Metoda mnożników Lagrange'a dla odległości do kwadratu $d^2 = x^2 + y^2$. $d_{\min} = 1$ w punktach $\pm(1/\sqrt{2}, 1/\sqrt{2})$, $d_{\max} = 2$ w punktach $\pm(\sqrt{2}, -\sqrt{2})$.
