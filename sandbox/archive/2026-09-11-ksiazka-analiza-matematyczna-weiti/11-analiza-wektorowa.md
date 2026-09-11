# Część XI: Całki Krzywoliniowe, Powierzchniowe i Analiza Wektorowa

Analiza wektorowa i teoria całek krzywoliniowych oraz powierzchniowych stanowią język współczesnej elektrodynamiki klasycznej, teorii obwodów z parametrami rozproszonymi, radiokomunikacji, teorii falowodów oraz optyki falowej. To właśnie twierdzenia Greena, Gaussa-Ostrogradskiego i Stokesa umożliwiły Jamesowi Clerkowi Maxwellowi syntezę wszystkich dotychczasowych praw elektryczności i magnetyzmu w cztery zwarte równania pola elektromagnetycznego oraz doprowadziły do teoretycznego odkrycia fal elektromagnetycznych rozchodzących się z prędkością światła.

---

## Rozdział 23: Całki krzywoliniowe i twierdzenie Greena

### 23.1. Krzywe w przestrzeni $\mathbb{R}^3$ i parametryzacja łukowa

#### Definicja 23.1 (Krzywa regularna)
1. **Krzywą zorientowaną** $K \subset \mathbb{R}^3$ nazywamy obraz przedziału $[a, b]$ przy odwzorowaniu ciągłym $\vec{r}: [a, b] \to \mathbb{R}^3$:
   $$\vec{r}(t) = [x(t), y(t), z(t)]^T, \quad t \in [a, b]$$
2. Krzywą nazywamy **gładką (regularną)**, jeżeli funkcja $\vec{r}(t)$ jest klasy $C^1$ na $[a, b]$ oraz wektor pochodnej (wektor prędkości / styczny) nie zeruje się w żadnym punkcie:
   $$\vec{r}'(t) = [x'(t), y'(t), z'(t)]^T \neq \vec{0} \quad \forall t \in [a, b]$$
3. Krzywą nazywamy **prostą (łukiem Jordana)**, jeżeli odwzorowanie $\vec{r}$ jest różnowartościowe na $[a, b)$ oraz $(a, b]$. Jeżeli $\vec{r}(a) = \vec{r}(b)$, to krzywą nazywamy **zamkniętą**.
4. Krzywą nazywamy **kawałkami gładką**, jeżeli składa się ze skończonej liczby łuków gładkich połączonych wierzchołkami.

#### Długość łuku i element łuku $ds$:
Długość krzywej regularnej $K$ wyraża się wzorem:
$$|K| = \int_a^b \|\vec{r}'(t)\|\,dt = \int_a^b \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2}\,dt$$
Różniczka długości łuku (tzw. **element łuku**):
$$ds = \|\vec{r}'(t)\|\,dt = \sqrt{dx^2 + dy^2 + dz^2}$$

---

### 23.2. Całka krzywoliniowa nieskierowana (I rodzaju)

Niech funkcja skalarna $f: K \to \mathbb{R}$ będzie ciągła na krzywej regularnej $K$.

#### Definicja 23.2 (Całka krzywoliniowa nieskierowana)
Dzieląc łuk $K$ punktami $P_0, P_1, \dots, P_n$ na łuki cząstkowe o długościach $\Delta s_i$ i wybierając na każdym punkty pośrednie $\Xi_i \in \Delta s_i$:
$$\int_K f(x, y, z)\,ds = \lim_{\max \Delta s_i \to 0} \sum_{i=1}^n f(\Xi_i) \Delta s_i$$

> **Twierdzenie 23.1 (Obliczanie całki nieskierowanej):**  
> Jeżeli krzywa $K$ dana jest parametryzacją $\vec{r}(t)$ dla $t \in [a, b]$, to:
> $$\int_K f(x, y, z)\,ds = \int_a^b f(x(t), y(t), z(t)) \sqrt{[x'(t)]^2 + [y'(t)]^2 + [z'(t)]^2}\,dt$$

Wartość całki nieskierowanej **nie zależy od wyboru zwrotu (orientacji)** krzywej: $\int_{-K} f\,ds = \int_K f\,ds$.

#### Zastosowania fizyczne:
1. **Długość łuku:** $|K| = \int_K 1\,ds$.
2. **Masa i ładunek linijowy przewodu:** Jeżeli $\lambda(x, y, z)$ określa gęstość liniową masy lub ładunku [$\text{C}/\text{m}$]:
   $$M = \int_K \lambda(x, y, z)\,ds, \quad Q = \int_K \lambda(x, y, z)\,ds$$
3. **Środek ciężkości przewodu:**
   $$x_C = \frac{1}{M} \int_K x \lambda(s)\,ds, \quad y_C = \frac{1}{M} \int_K y \lambda(s)\,ds, \quad z_C = \frac{1}{M} \int_K z \lambda(s)\,ds$$

---

### 23.3. Całka krzywoliniowa skierowana (II rodzaju)

Rozważmy pole wektorowe $\vec{F}: D \to \mathbb{R}^3$, gdzie $\vec{F}(x, y, z) = [P(x, y, z), Q(x, y, z), R(x, y, z)]^T$, określone wzdłuż zorientowanej krzywej regularnej $K$ od punktu początkowego $A = \vec{r}(a)$ do końcowego $B = \vec{r}(b)$.

#### Definicja 23.3 (Całka krzywoliniowa skierowana)
Całką krzywoliniową skierowaną pola wektorowego $\vec{F}$ wzdłuż zorientowanej krzywej $K$ nazywamy granicę sum iloczynów skalarnych wektora siły i wektora przesunięcia:
$$\int_K \vec{F} \cdot d\vec{r} = \int_K P\,dx + Q\,dy + R\,dz = \lim_{\max \|\Delta \vec{r}_i\| \to 0} \sum_{i=1}^n \vec{F}(\Xi_i) \cdot \Delta \vec{r}_i$$

> **Twierdzenie 23.2 (Obliczanie całki skierowanej):**  
> $$\int_K P\,dx + Q\,dy + R\,dz = \int_a^b \left[ P(\vec{r}(t)) x'(t) + Q(\vec{r}(t)) y'(t) + R(\vec{r}(t)) z'(t) \right] dt$$

#### Własności całki skierowanej:
1. **Zmiana orientacji zmienia znak całki na przeciwny:**
   $$\int_{-K} \vec{F} \cdot d\vec{r} = -\int_K \vec{F} \cdot d\vec{r}$$
2. **Sens fizyczny (Praca i Napięcie elektryczne):**  
   - Praca wykonana przez pole sił $\vec{F}$ przy przesunięciu cząstki wzdłuż krzywej $K$:
     $$W = \int_K \vec{F} \cdot d\vec{r}$$
   - Napięcie elektryczne $U_{AB}$ (różnica potencjałów) między punktami $A$ i $B$ w polu elektrostatycznym o natężeniu $\vec{E}$:
     $$U_{AB} = \int_{K: A \to B} \vec{E} \cdot d\vec{r}$$
   - **Cyrkulacja pola:** Całkę wzdłuż krzywej zamkniętej oznaczamy symbolem $\oint_K \vec{F} \cdot d\vec{r}$. W elektrotechnice całka $\oint_K \vec{E} \cdot d\vec{r}$ określa siłę elektromotoryczną (SEM) indukowaną w obwodzie.

---

### 23.4. Niezależność całki od drogi i pola potencjalne

W ogólnym przypadku wartość pracy $\int_K \vec{F} \cdot d\vec{r}$ zależy od trajektorii łączącej punkty $A$ i $B$. Szczególną klasę stanowią **pola potencjalne (konserwatywne)**.

#### Definicja 23.4 (Pole potencjalne)
Pole wektorowe $\vec{F}$ nazywamy **potencjalnym** w obszarze $D$, jeżeli istnieje funkcja skalarna $V: D \to \mathbb{R}$ (zwana **potencjałem** lub funkcją pierwotną pola) taka, że:
$$\vec{F} = \nabla V \iff P = \frac{\partial V}{\partial x}, \quad Q = \frac{\partial V}{\partial y}, \quad R = \frac{\partial V}{\partial z}$$

> **Twierdzenie 23.3 (O równoważności warunków potencjalności pola):**  
> Niech pole wektorowe $\vec{F} = [P, Q, R]^T$ będzie klasy $C^1$ w obszarze jednospójnym $D \subset \mathbb{R}^3$. Wówczas następujące warunki są równoważne:
> 1. Pole $\vec{F}$ jest potencjalne: $\vec{F} = \nabla V$.
> 2. Całka $\int_K \vec{F} \cdot d\vec{r}$ nie zależy od drogi całkowania, a zależy wyłącznie od punktu początkowego $A$ i końcowego $B$:
>    $$\int_{K: A \to B} \vec{F} \cdot d\vec{r} = V(B) - V(A)$$
> 3. Cyrkulacja pola po dowolnej zamkniętej krzywej kawałkami gładkiej $K \subset D$ jest równa zeru:
>    $$\oint_K \vec{F} \cdot d\vec{r} = 0$$
> 4. Pole jest **bezwirowe**: $\operatorname{rot} \vec{F} = \vec{0}$ w całym obszarze $D$, czyli:
>    $$\frac{\partial R}{\partial y} = \frac{\partial Q}{\partial z}, \quad \frac{\partial P}{\partial z} = \frac{\partial R}{\partial x}, \quad \frac{\partial Q}{\partial x} = \frac{\partial P}{\partial y}$$

---

### 23.5. Twierdzenie Greena na płaszczyźnie

Twierdzenie Greena wiąże całkę krzywoliniową skierowaną po brzegu obszaru płaskiego z całką podwójną po tym obszarze.

#### Definicja 23.5 (Orientacja dodatnia brzegu)
Mówimy, że brzeg $\partial D$ obszaru płaskiego $D$ jest **zorientowany dodatnio**, jeżeli przy poruszaniu się wzdłuż brzegu obszar $D$ pozostaje stale **po lewej stronie** (dla pojedynczego obszaru bez dziur odpowiada to obiegowi przeciwnemu do ruchu wskazówek zegara, CCW).

> **Twierdzenie 23.4 (Twierdzenie Greena):**  
> Jeżeli obszar $D \subset \mathbb{R}^2$ jest ograniczony brzegiem kawałkami gładkim $\partial D$ zorientowanym dodatnio, a funkcje $P(x, y)$ i $Q(x, y)$ są klasy $C^1$ na domknięciu $\overline{D}$, to:
> $$\oint_{\partial D} P\,dx + Q\,dy = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx\,dy$$

**Dowód (dla obszaru normalnego względem obu osi):**  
Niech $D = \{ (x, y) : a \le x \le b, \; g_1(x) \le y \le g_2(x) \}$. Obliczmy całkę podwójną z $-\frac{\partial P}{\partial y}$:
$$\iint_D -\frac{\partial P}{\partial y}\,dx\,dy = -\int_a^b dx \int_{g_1(x)}^{g_2(x)} \frac{\partial P}{\partial y}\,dy = -\int_a^b \big[ P(x, g_2(x)) - P(x, g_1(x)) \big]\,dx$$
$$= \int_a^b P(x, g_1(x))\,dx - \int_a^b P(x, g_2(x))\,dx$$
Brzeg $\partial D$ składa się z dolnej krzywej $C_1: y = g_1(x)$ (od $x=a$ do $b$), odcinka pionowego prawego, górnej krzywej $C_2: y = g_2(x)$ (od $x=b$ do $a$) oraz odcinka pionowego lewego. Na odcinkach pionowych $dx = 0$, więc całka z $P\,dx$ znika. Zatem:
$$\oint_{\partial D} P\,dx = \int_a^b P(x, g_1(x))\,dx + \int_b^a P(x, g_2(x))\,dx = \iint_D -\frac{\partial P}{\partial y}\,dx\,dy$$
Postępując analogicznie dla obszaru normalnego względem osi $OY$, otrzymujemy:
$$\oint_{\partial D} Q\,dy = \iint_D \frac{\partial Q}{\partial x}\,dx\,dy$$
Dodając obie równości stronami, otrzymujemy tezę twierdzenia Greena. $\blacksquare$

#### Wzór na pole obszaru za pomocą całki krzywoliniowej:
Kładąc w twierdzeniu Greena kolejno $P = 0, Q = x$ lub $P = -y, Q = 0$ lub symetrycznie $P = -\frac{1}{2}y, Q = \frac{1}{2}x$, otrzymujemy $\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = 1$, skąd:
$$|D| = \iint_D 1\,dx\,dy = \oint_{\partial D} x\,dy = -\oint_{\partial D} y\,dx = \frac{1}{2} \oint_{\partial D} (x\,dy - y\,dx)$$

---

## Rozdział 24: Całki powierzchniowe, twierdzenia Gaussa-Ostrogradskiego i Stokesa oraz elektrodynamika Maxwella

### 24.1. Powierzchnie zorientowane i całka powierzchniowa nieskierowana

Niech gładki płat powierzchniowy $S \subset \mathbb{R}^3$ będzie sparametryzowany równaniem wektorowym:
$$\vec{r}(u, v) = [x(u, v), y(u, v), z(u, v)]^T, \quad (u, v) \in \Delta \subset \mathbb{R}^2$$
Wektor normalny do powierzchni:
$$\vec{N}(u, v) = \frac{\partial \vec{r}}{\partial u} \times \frac{\partial \vec{r}}{\partial v} = \det \begin{bmatrix}
\vec{i} & \vec{j} & \vec{k} \\
\frac{\partial x}{\partial u} & \frac{\partial y}{\partial u} & \frac{\partial z}{\partial u} \\
\frac{\partial x}{\partial v} & \frac{\partial y}{\partial v} & \frac{\partial z}{\partial v}
\end{bmatrix}$$
Element pola powierzchni (różniczka powierzchni):
$$dS = \|\vec{N}(u, v)\|\,du\,dv = \sqrt{EG - F^2}\,du\,dv$$
gdzie $E, F, G$ to współczynniki pierwszej formy kwadratowej Gaussa:
$$E = \left\langle \frac{\partial \vec{r}}{\partial u}, \frac{\partial \vec{r}}{\partial u} \right\rangle, \quad F = \left\langle \frac{\partial \vec{r}}{\partial u}, \frac{\partial \vec{r}}{\partial v} \right\rangle, \quad G = \left\langle \frac{\partial \vec{r}}{\partial v}, \frac{\partial \vec{r}}{\partial v} \right\rangle$$
Dla powierzchni zadanej w postaci jawnej $z = f(x, y)$:
$$dS = \sqrt{1 + \left(\frac{\partial f}{\partial x}\right)^2 + \left(\frac{\partial f}{\partial y}\right)^2}\,dx\,dy$$

#### Definicja 24.1 (Całka powierzchniowa nieskierowana - I rodzaju)
Dla funkcji skalarnej $g: S \to \mathbb{R}$:
$$\iint_S g(x, y, z)\,dS = \iint_\Delta g(\vec{r}(u, v)) \|\vec{N}(u, v)\|\,du\,dv$$
Wartość całki nieskierowanej nie zależy od wyboru strony (orientacji) płata. Służy do obliczania całkowitej masy powłoki lub ładunku powierzchniowego: $Q = \iint_S \sigma(x, y, z)\,dS$.

---

### 24.2. Całka powierzchniowa skierowana (II rodzaju) i pojęcie strumienia

Płat powierzchniowy $S$ nazywamy **orientowalnym (dwustronnym)**, jeżeli można na nim w sposób ciągły określić jednostkowy wektor normalny $\vec{n}_0(P)$. Wybór jednego z dwóch zwrotów wektora $\vec{n}_0$ ustala **orientację powierzchni**.

#### Definicja 24.2 (Strumień pola wektorowego / Całka powierzchniowa skierowana)
Niech pole wektorowe $\vec{F} = [P, Q, R]^T$ będzie określone na zorientowanej powierzchni $S$ o wektorze normalnym $\vec{n}_0 = [\cos \alpha, \cos \beta, \cos \gamma]^T$. **Strumieniem pola $\vec{F}$ przez powierzchnię $S$** nazywamy:
$$\Phi = \iint_S \vec{F} \cdot d\vec{S} = \iint_S (\vec{F} \cdot \vec{n}_0)\,dS = \iint_S P\,dy\,dz + Q\,dz\,dx + R\,dx\,dy$$
Dla parametryzacji $\vec{r}(u, v)$:
$$\iint_S \vec{F} \cdot d\vec{S} = \pm \iint_\Delta \vec{F}(\vec{r}(u, v)) \cdot \left( \frac{\partial \vec{r}}{\partial u} \times \frac{\partial \vec{r}}{\partial v} \right) du\,dv$$
znak $+$ lub $-$ zależy od zgodności zwrotu wektora $\vec{N}$ z przyjętą orientacją płata.

---

### 24.3. Operatory różniczkowe pola: Nabla, Dywergencja, Rotacja i Laplasjan

Wprowadzamy formalny wektorowy operator różniczkowy Hamiltona (**nabla**):
$$\nabla = \left[ \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right]^T = \vec{i}\frac{\partial}{\partial x} + \vec{j}\frac{\partial}{\partial y} + \vec{k}\frac{\partial}{\partial z}$$

1. **Gradient pola skalarnego $f$:**
   $$\nabla f = \operatorname{grad} f = \left[ \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right]^T$$
2. **Dywergencja (rozbieżność) pola wektorowego $\vec{F} = [P, Q, R]^T$:**
   $$\operatorname{div} \vec{F} = \nabla \cdot \vec{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$
   Dywergencja jest polem skalarnym. Mierzy lokalną gęstość źródeł pola w punkcie:
   - $\operatorname{div} \vec{F} > 0$ – źródło (pole "wypływa" z punktu, np. ładunek dodatni),
   - $\operatorname{div} \vec{F} < 0$ – ujście (pole "wpływa" do punktu, np. ładunek ujemny),
   - $\operatorname{div} \vec{F} = 0$ – pole **bezźródłowe** (strumień netto przez dowolną zamkniętą otoczkę wynosi zero).
3. **Rotacja (wirowość) pola wektorowego $\vec{F}$:**
   $$\operatorname{rot} \vec{F} = \operatorname{curl} \vec{F} = \nabla \times \vec{F} = \det \begin{bmatrix}
   \vec{i} & \vec{j} & \vec{k} \\
   \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
   P & Q & R
   \end{bmatrix} = \left[ \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \; \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \; \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right]^T$$
   Rotacja jest polem wektorowym. Mierzy tendencję pola do tworzenia wirów (cyrkulacji) wokół danego punktu.
4. **Laplasjan pola skalarnego $f$:**
   $$\Delta f = \nabla^2 f = \nabla \cdot (\nabla f) = \operatorname{div}(\operatorname{grad} f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

#### Fundamentalne tożsamości różniczkowe:
1. **Pole potencjalne jest bezwirowe:**
   $$\operatorname{rot}(\operatorname{grad} f) = \nabla \times (\nabla f) \equiv \vec{0}$$
2. **Pole wirowe jest bezźródłowe:**
   $$\operatorname{div}(\operatorname{rot} \vec{F}) = \nabla \cdot (\nabla \times \vec{F}) \equiv 0$$
3. **Podwójna rotacja (tożsamość wektorowa falowa):**
   $$\nabla \times (\nabla \times \vec{F}) = \nabla(\nabla \cdot \vec{F}) - \Delta \vec{F} = \operatorname{grad}(\operatorname{div} \vec{F}) - \Delta \vec{F}$$
   gdzie $\Delta \vec{F} = [\Delta P, \Delta Q, \Delta R]^T$.

---

### 24.4. Twierdzenie Gaussa-Ostrogradskiego (o dywergencji)

Twierdzenie Gaussa-Ostrogradskiego wiąże strumień pola wektorowego przez zamkniętą powierzchnię z całką potrójną z dywergencji po bryle objętej tą powierzchnią.

> **Twierdzenie 24.1 (Gaussa-Ostrogradskiego):**  
> Niech $V \subset \mathbb{R}^3$ będzie obszarem ograniczonym, którego brzeg $\partial V = S$ jest zamkniętą powierzchnią kawałkami gładką zorientowaną na zewnątrz (wektory normalne skierowane poza bryłę $V$). Jeżeli pole wektorowe $\vec{F} = [P, Q, R]^T$ jest klasy $C^1$ na domknięciu $\overline{V}$, to:
> $$\iint_{\partial V} \vec{F} \cdot d\vec{S} = \iiint_V (\operatorname{div} \vec{F})\,dV$$
> czyli w zapisie współrzędnościowym:
> $$\iint_S P\,dy\,dz + Q\,dz\,dx + R\,dx\,dy = \iiint_V \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) dx\,dy\,dz$$

#### Fizyczna interpretacja:
Całkowity strumień wektora opuszczający objętość $V$ przez jej powierzchnię graniczną $S$ jest równy sumie wszystkich elementarnych źródeł pola zawartych wewnątrz tej objętości.

---

### 24.5. Twierdzenie Stokesa (o rotacji)

Twierdzenie Stokesa stanowi trójwymiarowe uogólnienie twierdzenia Greena. Wiąże cyrkulację pola wektorowego wzdłuż zamkniętego konturu przestrzennego ze strumieniem rotacji tego pola przez powierzchnię rozpiętą na tym konturze.

> **Twierdzenie 24.2 (Stokesa):**  
> Niech $S \subset \mathbb{R}^3$ będzie zorientowaną powierzchnią gładką, której brzeg $\partial S = K$ jest zamkniętą krzywą kawałkami gładką zorientowaną zgodnie z regułą śruby prawoskrętnej względem wektora normalnego do powierzchni. Jeżeli pole wektorowe $\vec{F}$ jest klasy $C^1$ w otoczeniu powierzchni $S$, to:
> $$\oint_{\partial S} \vec{F} \cdot d\vec{r} = \iint_S (\operatorname{rot} \vec{F}) \cdot d\vec{S}$$
> W zapisie współrzędnościowym:
> $$\oint_K P\,dx + Q\,dy + R\,dz = \iint_S \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right) dy\,dz + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right) dz\,dx + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) dx\,dy$$

---

### 24.6. Zwieńczenie analizy wektorowej: Równania elektrodynamiki Maxwella i równanie falowe

Cała współczesna teoria fal elektromagnetycznych, anten, mikrofal i telekomunikacji opiera się na czterech równaniach Maxwella, będących bezpośrednią aplikacją twierdzeń Gaussa-Ostrogradskiego i Stokesa.

#### Równania Maxwella w postaci różniczkowej i całkowej:

| Zjawisko / Prawo | Postać różniczkowa | Postać całkowa | Zastosowane twierdzenie |
| :--- | :--- | :--- | :--- |
| **Prawo Gaussa dla elektrostatyki** | $\nabla \cdot \vec{D} = \rho$ | $\iint_{\partial V} \vec{D} \cdot d\vec{S} = Q_{\text{wew}} = \iiint_V \rho\,dV$ | Tw. Gaussa-Ostrogradskiego |
| **Prawo Gaussa dla magnetyzmu** | $\nabla \cdot \vec{B} = 0$ | $\iint_{\partial V} \vec{B} \cdot d\vec{S} = 0$ (brak monopoli magnetycznych) | Tw. Gaussa-Ostrogradskiego |
| **Prawo indukcji Faradaya** | $\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$ | $\oint_{\partial S} \vec{E} \cdot d\vec{r} = -\frac{d}{dt} \iint_S \vec{B} \cdot d\vec{S} = -\frac{d\Phi_B}{dt}$ | Twierdzenie Stokesa |
| **Prawo Ampère'a-Maxwella** | $\nabla \times \vec{H} = \vec{J} + \frac{\partial \vec{D}}{\partial t}$ | $\oint_{\partial S} \vec{H} \cdot d\vec{r} = I_{\text{przew}} + \frac{d\Psi_D}{dt}$ | Twierdzenie Stokesa |

gdzie:
- $\vec{E}$ – natężenie pola elektrycznego [$\text{V}/\text{m}$], $\vec{D} = \varepsilon \vec{E}$ – indukcja elektryczna,
- $\vec{H}$ – natężenie pola magnetycznego [$\text{A}/\text{m}$], $\vec{B} = \mu \vec{H}$ – indukcja magnetyczna,
- $\vec{J}$ – gęstość prądu przewodzenia, $\frac{\partial \vec{D}}{\partial t}$ – **prąd przesunięcia Maxwella** (umożliwiający przepływ prądu zmiennego przez dielektryk kondensatora).

#### Wyprowadzenie równania falowego dla fal elektromagnetycznych:
W próżni pozbawionej ładunków swobodnych ($\rho = 0$) i prądów przewodzenia ($\vec{J} = \vec{0}$) równania Maxwella przyjmują postać:
$$\nabla \cdot \vec{E} = 0, \quad \nabla \cdot \vec{B} = 0, \quad \nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}, \quad \nabla \times \vec{B} = \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t}$$
Przykładamy operator rotacji ($\nabla \times$) do prawa Faradaya:
$$\nabla \times (\nabla \times \vec{E}) = \nabla \times \left( -\frac{\partial \vec{B}}{\partial t} \right) = -\frac{\partial}{\partial t}(\nabla \times \vec{B})$$
Stosując tożsamość wektorową $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \Delta \vec{E}$ oraz wiedząc, że $\nabla \cdot \vec{E} = 0$:
$$-\Delta \vec{E} = -\frac{\partial}{\partial t} \left( \mu_0 \varepsilon_0 \frac{\partial \vec{E}}{\partial t} \right) = -\mu_0 \varepsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$
Otrzymujemy **trójwymiarowe równanie falowe D'Alemberta**:
$$\Delta \vec{E} - \frac{1}{c^2} \frac{\partial^2 \vec{E}}{\partial t^2} = \vec{0}$$
gdzie stała propagacji $c$ jest prędkością rozchodzenia się fali w próżni:
$$c = \frac{1}{\sqrt{\varepsilon_0 \mu_0}} \approx 3 \cdot 10^8 \; \left[\frac{\text{m}}{\text{s}}\right]$$
Identyczne równanie falowe spełnia pole magnetyczne $\vec{B}$: $\Delta \vec{B} - \frac{1}{c^2} \frac{\partial^2 \vec{B}}{\partial t^2} = \vec{0}$.  
Wynik ten stanowi jedno z największych osiągnięć w historii nauki – analityczny dowód, że światło jest falą elektromagnetyczną!

---

### 24.7. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 24.1 (Praca w polu sił - całka krzywoliniowa skierowana)
Obliczyć pracę wykonaną przez pole sił $\vec{F}(x, y, z) = [y^2, 2xy, z]^T$ wzdłuż linii śrubowej $K$:
$$x(t) = \cos t, \quad y(t) = \sin t, \quad z(t) = t, \quad t \in [0, 2\pi]$$

**Rozwiązanie:**  
1. **Badanie potencjalności pola:**  
   Sprawdźmy rotację $\operatorname{rot} \vec{F}$:
   $$\operatorname{rot} \vec{F} = \det \begin{bmatrix} \vec{i} & \vec{j} & \vec{k} \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ y^2 & 2xy & z \end{bmatrix} = \vec{i}(0 - 0) - \vec{j}(0 - 0) + \vec{k}(2y - 2y) = \vec{0}$$
   Pole jest bezwirowe w całym $\mathbb{R}^3$, a więc jest potencjalne!

2. **Wyznaczenie potencjału $V(x, y, z)$:**  
   $$\frac{\partial V}{\partial x} = y^2 \implies V(x, y, z) = x y^2 + \varphi(y, z)$$
   $$\frac{\partial V}{\partial y} = 2xy + \frac{\partial \varphi}{\partial y} = 2xy \implies \frac{\partial \varphi}{\partial y} = 0 \implies \varphi(y, z) = \psi(z)$$
   $$\frac{\partial V}{\partial z} = \psi'(z) = z \implies \psi(z) = \frac{1}{2} z^2 + C$$
   Potencjał pola: $V(x, y, z) = x y^2 + \frac{1}{2} z^2$.

3. **Obliczenie pracy:**  
   Punkt początkowy $A = \vec{r}(0) = (\cos 0, \sin 0, 0) = (1, 0, 0)$.  
   Punkt końcowy $B = \vec{r}(2\pi) = (\cos 2\pi, \sin 2\pi, 2\pi) = (1, 0, 2\pi)$.  
   Z niezależności całki od drogi całkowania:
   $$W = \int_K \vec{F} \cdot d\vec{r} = V(B) - V(A) = \left( 1 \cdot 0^2 + \frac{1}{2}(2\pi)^2 \right) - \left( 1 \cdot 0^2 + \frac{1}{2}(0)^2 \right) = \frac{4\pi^2}{2} = 2\pi^2$$

---

#### Przykład 24.2 (Zastosowanie twierdzenia Greena)
Obliczyć całkę krzywoliniową:
$$I = \oint_K (e^x \sin y - 2y)\,dx + (e^x \cos y + 3x)\,dy$$
gdzie $K$ jest okręgiem $x^2 + y^2 = 4$ zorientowanym dodatnio (CCW).

**Rozwiązanie:**  
1. **Oznaczenia i pochodne cząstkowe:**  
   $P(x, y) = e^x \sin y - 2y \implies \frac{\partial P}{\partial y} = e^x \cos y - 2$  
   $Q(x, y) = e^x \cos y + 3x \implies \frac{\partial Q}{\partial x} = e^x \cos y + 3$

2. **Różnica pochodnych:**  
   $$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} = (e^x \cos y + 3) - (e^x \cos y - 2) = 5$$

3. **Zastosowanie twierdzenia Greena:**  
   $$I = \iint_D 5\,dx\,dy = 5 \iint_D 1\,dx\,dy = 5 \cdot |D|$$
   gdzie $D$ jest kołem o promieniu $R = 2$, a jego pole wynosi $|D| = \pi R^2 = 4\pi$.  
   Stąd:
   $$I = 5 \cdot 4\pi = 20\pi$$

---

#### Przykład 24.3 (Strumień pola wektorowego - twierdzenie Gaussa-Ostrogradskiego)
Obliczyć strumień pola wektorowego $\vec{F}(x, y, z) = [x^3, y^3, z^3]^T$ przez zewnętrzną stronę sfery $S: x^2 + y^2 + z^2 = R^2$.

**Rozwiązanie:**  
Powierzchnia $S$ jest brzegiem kuli $V = \{ (x, y, z) : x^2 + y^2 + z^2 \le R^2 \}$.
1. **Obliczenie dywergencji pola:**  
   $$\operatorname{div} \vec{F} = \frac{\partial}{\partial x}(x^3) + \frac{\partial}{\partial y}(y^3) + \frac{\partial}{\partial z}(z^3) = 3x^2 + 3y^2 + 3z^2 = 3(x^2 + y^2 + z^2)$$

2. **Zastosowanie twierdzenia Gaussa-Ostrogradskiego:**  
   $$\Phi = \iint_S \vec{F} \cdot d\vec{S} = \iiint_V 3(x^2 + y^2 + z^2)\,dV$$

3. **Przejście do współrzędnych sferycznych:**  
   $x^2 + y^2 + z^2 = r^2$, $dV = r^2 \sin \theta\,dr\,d\theta\,d\varphi$, gdzie $r \in [0, R], \theta \in [0, \pi], \varphi \in [0, 2\pi]$:
   $$\Phi = 3 \int_0^{2\pi} d\varphi \int_0^\pi \sin \theta\,d\theta \int_0^R r^2 \cdot r^2\,dr$$
   - Kąty: $\int_0^{2\pi} d\varphi \int_0^\pi \sin \theta\,d\theta = 2\pi \cdot 2 = 4\pi$.
   - Promień: $\int_0^R r^4\,dr = \left[ \frac{r^5}{5} \right]_0^R = \frac{R^5}{5}$.  
   Wynik:
   $$\Phi = 3 \cdot 4\pi \cdot \frac{R^5}{5} = \frac{12\pi}{5} R^5$$

---

### 24.8. Zadania do samodzielnego rozwiązania

1. **Zadanie 24.1:** Obliczyć masę łuku asteroidy $x(t) = a \cos^3 t, y(t) = a \sin^3 t$ ($t \in [0, \pi/2]$), jeżeli gęstość liniowa w każdym punkcie jest równa $\lambda(x, y) = y$.  
   *Odpowiedź:* $ds = 3a \sin t \cos t\,dt$. $M = \int_0^{\pi/2} (a \sin^3 t)(3a \sin t \cos t)\,dt = 3a^2 \int_0^{\pi/2} \sin^4 t \cos t\,dt = \frac{3}{5} a^2$.

2. **Zadanie 24.2:** Wyznaczyć pole obszaru ograniczonego pętlą liścia Kartezjusza $x^3 + y^3 - 3axy = 0$ stosując wzór całkowy Greena we współrzędnych biegunowych ($y = tx$).  
   *Odpowiedź:* $|D| = \frac{3}{2} a^2$.

3. **Zadanie 24.3:** Obliczyć cyrkulację pola $\vec{F}(x, y, z) = [y, z, x]^T$ wzdłuż brzegu trójkąta powstałego z przecięcia płaszczyzny $x + y + z = 1$ z płaszczyznami układu współrzędnych (obieg w I oktancie widziany z góry przeciwnie do wskazówek zegara).  
   *Odpowiedź:* Z twierdzenia Stokesa $\operatorname{rot} \vec{F} = [-1, -1, -1]^T$. Wektor normalny $\vec{n} = [1, 1, 1]/\sqrt{3}$. $\oint_K \vec{F} \cdot d\vec{r} = -\frac{3}{2}$.

4. **Zadanie 24.4:** Wykazać tożsamość wektorową $\operatorname{div}(f \vec{A}) = f \operatorname{div} \vec{A} + \vec{A} \cdot \nabla f$.

5. **Zadanie 24.5:** Korzystając z twierdzenia Gaussa-Ostrogradskiego wykazać, że dla dowolnej zamkniętej powierzchni gładkiej $S$ ograniczającej bryłę $V$ zachodzi:
   $$\iint_S \vec{r} \cdot d\vec{S} = 3 |V|$$
   gdzie $\vec{r} = [x, y, z]^T$ jest promieniem wodzącym.  
   *Wskazówka:* $\operatorname{div} \vec{r} = \frac{\partial x}{\partial x} + \frac{\partial y}{\partial y} + \frac{\partial z}{\partial z} = 1 + 1 + 1 = 3$.
