# Analiza Matematyczna dla Informatyków i Elektroników
## Podręcznik akademicki (WEiTI PW)

\newpage

# Część I: Fundamenty Analizy Matematycznej

W analizie matematycznej dla inżynierów elektroników i informatyków pojęcia abstrakcyjne nie są jedynie konstrukcją teoretyczną – stanowią fundament aparatu pojęciowego teorii sygnałów, przetwarzania informacji, elektrotechniki teoretycznej oraz algorytmiki. W niniejszej części wprowadzamy rygorystyczny aparat liczb rzeczywistych $\mathbb{R}$ oraz liczb zespolonych $\mathbb{C}$.

---

## Rozdział 1: Ciało liczb rzeczywistych $\mathbb{R}$

### 1.1. Aksjomatyczna budowa zbioru liczb rzeczywistych

Zbiór liczb rzeczywistych $\mathbb{R}$ definiujemy aksjomatycznie jako ciało uporządkowane, zupełne (ciągłe). Oznacza to spełnienie trzech grup aksjomatów.

#### Grupa I: Aksjomaty ciała $(\mathbb{R}, +, \cdot)$
Dla dowolnych $x, y, z \in \mathbb{R}$ określone są dwa działania wewnętrzne: dodawanie $(+)$ oraz mnożenie $(\cdot)$, spełniające warunki:
1. **Łączność:**
   $$(x + y) + z = x + (y + z), \quad (x \cdot y) \cdot z = x \cdot (y \cdot z)$$
2. **Przemienność:**
   $$x + y = y + x, \quad x \cdot y = y \cdot x$$
3. **Istnienie elementów neutralnych:**
   Istnieją elementy $0 \in \mathbb{R}$ oraz $1 \in \mathbb{R}$ ($1 \neq 0$) takie, że:
   $$x + 0 = x, \quad x \cdot 1 = x$$
4. **Istnienie elementów odwrotnych:**
   Dla każdego $x \in \mathbb{R}$ istnieje element przeciwny $-x \in \mathbb{R}$ taki, że $x + (-x) = 0$.
   Dla każdego $x \in \mathbb{R} \setminus \{0\}$ istnieje element odwrotny $x^{-1} = \frac{1}{x} \in \mathbb{R}$ taki, że $x \cdot x^{-1} = 1$.
5. **Rozdzielność mnożenia względem dodawania:**
   $$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$

#### Grupa II: Aksjomaty porządku $(\mathbb{R}, \le)$
W zbiorze $\mathbb{R}$ określona jest relacja częściowego porządku $\le$, która jest porządkiem liniowym i jest zgodna z działaniami algebraicznymi:
1. **Spójność (porządek liniowy):**
   $$\forall_{x, y \in \mathbb{R}} \quad (x \le y) \lor (y \le x)$$
2. **Zgodność z dodawaniem:**
   $$\forall_{x, y, z \in \mathbb{R}} \quad (x \le y) \implies (x + z \le y + z)$$
3. **Zgodność z mnożeniem przez liczby nieujemne:**
   $$\forall_{x, y \in \mathbb{R}} \quad (0 \le x \land 0 \le y) \implies 0 \le x \cdot y$$

#### Grupa III: Aksjomat ciągłości (Zupełność Dedekinda)
Aksjomat ten odróżnia zbiór liczb rzeczywistych $\mathbb{R}$ od zbioru liczb wymiernych $\mathbb{Q}$ (w którym istnieją „luki”, np. $\sqrt{2} \notin \mathbb{Q}$).

> **Aksjomat Ciągłości Dedekinda:**
> Jeżeli niepuste zbiory $A, B \subset \mathbb{R}$ spełniają warunek:
> $$\forall_{a \in A} \forall_{b \in B} \quad a \le b$$
> to istnieje taka liczba rzeczywista $c \in \mathbb{R}$, że dla każdego $a \in A$ i każdego $b \in B$ zachodzi:
> $$a \le c \le b$$

Liczba $c$ oddziela zbiór $A$ od zbioru $B$.

---

### 1.2. Ograniczoność zbiorów i kresy (Supremum i Infimum)

W analizie matematycznej pojęcia kresów zastępują pojęcia elementu największego i najmniejszego, które w zbiorach nieskończonych na ogół nie istnieją.

#### Definicja 1.1 (Ograniczenie zbioru)
Niech $A \subset \mathbb{R}$ będzie zbiorem niepustym.
1. Zbiór $A$ nazywamy **ograniczonym z góry**, jeżeli:
   $$\exists_{M \in \mathbb{R}} \forall_{x \in A} \quad x \le M$$
   Każdą liczbę $M$ o tej własności nazywamy *ograniczeniem górnym* (majorantą) zbioru $A$.
2. Zbiór $A$ nazywamy **ograniczonym z dołu**, jeżeli:
   $$\exists_{m \in \mathbb{R}} \forall_{x \in A} \quad x \ge m$$
   Każdą liczbę $m$ o tej własności nazywamy *ograniczeniem dolnym* (minorantą) zbioru $A$.
3. Zbiór $A$ nazywamy **ograniczonym**, jeżeli jest ograniczony jednocześnie z góry i z dołu, co jest równoważne warunkowi:
   $$\exists_{K > 0} \forall_{x \in A} \quad |x| \le K$$

#### Definicja 1.2 (Kres górny i dolny)
1. Liczbę $S \in \mathbb{R}$ nazywamy **kresem górnym** (*supremum*) niepustego zbioru $A \subset \mathbb{R}$ i oznaczamy $S = \sup A$, jeżeli:
   - $S$ jest ograniczeniem górnym zbioru $A$:
     $$\forall_{x \in A} \quad x \le S$$
   - $S$ jest najmniejszym z ograniczeń górnych:
     $$\forall_{\varepsilon > 0} \exists_{x_0 \in A} \quad x_0 > S - \varepsilon$$
2. Liczbę $s \in \mathbb{R}$ nazywamy **kresem dolnym** (*infimum*) niepustego zbioru $A \subset \mathbb{R}$ i oznaczamy $s = \inf A$, jeżeli:
   - $s$ jest ograniczeniem dolnym zbioru $A$:
     $$\forall_{x \in A} \quad x \ge s$$
   - $s$ jest największym z ograniczeń dolnych:
     $$\forall_{\varepsilon > 0} \exists_{x_0 \in A} \quad x_0 < s + \varepsilon$$

> **Twierdzenie 1.1 (O istnieniu kresów):**
> Każdy niepusty zbiór liczb rzeczywistych ograniczony z góry ma kres górny ($S = \sup A \in \mathbb{R}$).  
> Każdy niepusty zbiór liczb rzeczywistych ograniczony z dołu ma kres dolny ($s = \inf A \in \mathbb{R}$).

**Dowód:**
Niech $A \subset \mathbb{R}$ będzie niepusty i ograniczony z góry. Zdefiniujmy zbiór $B$ jako zbiór wszystkich ograniczeń górnych zbioru $A$:
$$B = \{b \in \mathbb{R} : \forall_{a \in A} \ a \le b\}$$
Zbiór $B$ jest niepusty z założenia o ograniczoności $A$ z góry. Ponadto z samej definicji $B$, dla każdego $a \in A$ i każdego $b \in B$ zachodzi $a \le b$.
Z Aksjomatu Ciągłości Dedekinda wynika, że istnieje $c \in \mathbb{R}$ takie, że:
$$\forall_{a \in A} \forall_{b \in B} \quad a \le c \le b$$
Ponieważ $a \le c$ dla każdego $a \in A$, liczba $c$ jest ograniczeniem górnym zbioru $A$, zatem $c \in B$. Jednocześnie $c \le b$ dla każdego $b \in B$, więc $c$ jest najmniejszym elementem w zbiorze $B$ (najmniejszym ograniczeniem górnym). Stąd $c = \sup A$. $\blacksquare$

#### Własność Archimedesa i gęstość $\mathbb{Q}$ w $\mathbb{R}$

> **Twierdzenie 1.2 (Zasada Archimedesa):**
> Dla dowolnych liczb dodatnich $x, y \in \mathbb{R}$ istnieje liczba naturalna $n \in \mathbb{N}$ taka, że:
> $$n \cdot x > y$$

**Dowód (nie wprost):**
Przypuśćmy przeciwnie, że $\forall_{n \in \mathbb{N}} \ n x \le y$. Oznacza to, że zbiór $A = \{n x : n \in \mathbb{N}\}$ jest ograniczony z góry przez $y$. Na mocy Twierdzenia 1.1 zbiór $A$ posiada kres górny $S = \sup A$.
Z warunku $\varepsilon$-owego kresu górnego (dla $\varepsilon = x > 0$) istnieje element $n_0 x \in A$ taki, że:
$$n_0 x > S - x \implies (n_0 + 1)x > S$$
Lecz liczba $(n_0 + 1)x$ również należy do $A$ (jako iloczyn liczby naturalnej i $x$). Otrzymaliśmy element zbioru $A$ większy od jego kresu górnego $S$, co stanowi sprzeczność. Zatem zasada Archimedesa jest prawdziwa. $\blacksquare$

---

### 1.3. Elementy topologii prostej $\mathbb{R}$

W analizie matematycznej aparat pojęciowy opiera się na strukturze metrycznej prostej rzeczywistej.

#### Definicja 1.3 (Odległość i wartość bezwzględna)
Wartość bezwzględną (moduł) liczby $x \in \mathbb{R}$ definiujemy jako:
$$|x| = \begin{cases} x & \text{dla } x \ge 0 \\ -x & \text{dla } x < 0 \end{cases}$$
Odległość (metrykę euklidesową) punktów $x, y \in \mathbb{R}$ definiujemy jako $d(x, y) = |x - y|$.

Kluczowe własności:
1. $|x| \ge 0$, przy czym $|x| = 0 \iff x = 0$,
2. $|x \cdot y| = |x| \cdot |y|$,
3. **Nierówność trójkąta:**
   $$|x + y| \le |x| + |y|$$
4. **Nierówność trójkąta w dół:**
   $$\big| |x| - |y| \big| \le |x - y|$$

#### Definicja 1.4 (Otoczenie i sąsiedztwo punktu)
1. **Otoczeniem** punktu $x_0 \in \mathbb{R}$ o promieniu $r > 0$ nazywamy przedział otwarty:
   $$U(x_0, r) = (x_0 - r, x_0 + r) = \{x \in \mathbb{R} : |x - x_0| < r\}$$
2. **Sąsiedztwem** punktu $x_0$ o promieniu $r > 0$ nazywamy otoczenie pozbawione samego punktu $x_0$:
   $$S(x_0, r) = U(x_0, r) \setminus \{x_0\} = (x_0 - r, x_0) \cup (x_0, x_0 + r)$$

#### Definicja 1.5 (Klasyfikacja punktów i zbiory otwarte/domknięte)
Niech $E \subset \mathbb{R}$:
1. Punkt $x_0 \in E$ nazywamy **punktem wewnętrznym** zbioru $E$, jeżeli istnieje otoczenie $U(x_0, r) \subset E$. Zbiór wszystkich punktów wewnętrznych oznaczamy $\operatorname{Int} E$ lub $E^\circ$.
2. Zbiór $E$ nazywamy **zbiorem otwartym**, jeżeli każdy jego punkt jest punktem wewnętrznym ($E = \operatorname{Int} E$).
3. Punkt $p \in \mathbb{R}$ nazywamy **punktem skupienia** zbioru $E$, jeżeli w każdym jego sąsiedztwie znajduje się co najmniej jeden punkt ze zbioru $E$:
   $$\forall_{r > 0} \quad S(p, r) \cap E \neq \emptyset$$
4. Zbiór $E$ nazywamy **zbiorem domkniętym**, jeżeli zawiera wszystkie swoje punkty skupienia (co jest równoważne warunkowi, że dopełnienie $\mathbb{R} \setminus E$ jest zbiorem otwartym).
5. Zbiór $E \subset \mathbb{R}$ nazywamy **zbiorem zwartym**, jeżeli z każdego jego pokrycia przedziałami otwartymi można wybrać podpokrycie skończone.

> **Twierdzenie 1.3 (Heinego-Borela w $\mathbb{R}$):**
> Podzbiór $E \subset \mathbb{R}$ jest zwarty wtedy i tylko wtedy, gdy jest domknięty i ograniczony.

---

## Rozdział 2: Ciało liczb zespolonych $\mathbb{C}$

W inżynierii elektronicznej i informatycznej liczby zespolone są podstawowym narzędziem opisu sygnałów okresowych, stanów ustalonych w obwodach prądu zmiennego oraz transformat całkowych (Fouriera, Laplace'a, Z).

### 2.1. Konstrukcja formalna i postać algebraiczna

Ciało liczb zespolonych $\mathbb{C}$ definiujemy jako zbiór par uporządkowanych $(x, y) \in \mathbb{R}^2$ ze specjalnie zdefiniowanymi działaniami:

#### Definicja 2.1 (Działania w $\mathbb{C}$)
Dla $z_1 = (x_1, y_1)$ oraz $z_2 = (x_2, y_2)$:
1. **Dodawanie:**
   $$z_1 + z_2 = (x_1 + x_2, y_1 + y_2)$$
2. **Mnożenie:**
   $$z_1 \cdot z_2 = (x_1 x_2 - y_1 y_2, x_1 y_2 + x_2 y_1)$$

Elementem neutralnym dodawania jest $(0, 0)$, a mnożenia $(1, 0)$.  
Identyfikując liczbę rzeczywistą $x \in \mathbb{R}$ z parą $(x, 0)$, definiujemy **jednostkę urojoną**:
$$i = (0, 1)$$
Zauważmy, że:
$$i^2 = (0, 1) \cdot (0, 1) = (0 \cdot 0 - 1 \cdot 1, 0 \cdot 1 + 1 \cdot 0) = (-1, 0) = -1$$

Każdą liczbę zespoloną $z = (x, y)$ można zatem zapisać jednoznacznie w **postaci algebraicznej**:
$$z = x + i y, \quad x, y \in \mathbb{R}$$
gdzie:
- $x = \operatorname{Re}(z)$ – część rzeczywista (*Real*),
- $y = \operatorname{Im}(z)$ – część urojona (*Imaginary*).

*(Uwaga inżynierska: W elektrotechnice i elektronice jednostkę urojoną oznacza się literą $j$, aby uniknąć pomyłek z natężeniem prądu chwilowego $i(t)$. W dalszych rozważaniach stosujemy oznaczenie $i$ lub $j$ w zależności od kontekstu).*

#### Sprzężenie i moduł liczby zespolonej
1. **Liczbą sprzężoną** do $z = x + iy$ nazywamy liczbę:
   $$\bar{z} = x - iy$$
   Własności sprzężenia:
   $$\overline{z_1 \pm z_2} = \bar{z}_1 \pm \bar{z}_2, \quad \overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2, \quad z \cdot \bar{z} = x^2 + y^2 \ge 0$$
   $$\operatorname{Re}(z) = \frac{z + \bar{z}}{2}, \quad \operatorname{Im}(z) = \frac{z - \bar{z}}{2i}$$

2. **Modułem** liczby zespolonej $z = x + iy$ nazywamy liczbę rzeczywistą nieujemną:
   $$|z| = \sqrt{x^2 + y^2} = \sqrt{z \cdot \bar{z}}$$

> **Twierdzenie 2.1 (Nierówność trójkąta w $\mathbb{C}$):**
> Dla dowolnych $z_1, z_2 \in \mathbb{C}$ zachodzi:
> $$|z_1 + z_2| \le |z_1| + |z_2|$$

**Dowód:**
Rozpatrzmy kwadrat modułu lewej strony:
$$|z_1 + z_2|^2 = (z_1 + z_2)\overline{(z_1 + z_2)} = (z_1 + z_2)(\bar{z}_1 + \bar{z}_2) = z_1 \bar{z}_1 + z_1 \bar{z}_2 + z_2 \bar{z}_1 + z_2 \bar{z}_2$$
Zauważmy, że $z_1 \bar{z}_1 = |z_1|^2$, $z_2 \bar{z}_2 = |z_2|^2$ oraz:
$$z_1 \bar{z}_2 + z_2 \bar{z}_1 = z_1 \bar{z}_2 + \overline{z_1 \bar{z}_2} = 2 \operatorname{Re}(z_1 \bar{z}_2)$$
Dla dowolnej liczby zespolonej $\operatorname{Re}(w) \le |w|$, więc:
$$2 \operatorname{Re}(z_1 \bar{z}_2) \le 2 |z_1 \bar{z}_2| = 2 |z_1| |\bar{z}_2| = 2 |z_1| |z_2|$$
Zatem:
$$|z_1 + z_2|^2 \le |z_1|^2 + 2|z_1||z_2| + |z_2|^2 = (|z_1| + |z_2|)^2$$
Pierwiastkując obustronnie (obie strony są nieujemne), otrzymujemy tezę: $|z_1 + z_2| \le |z_1| + |z_2|$. $\blacksquare$

---

### 2.2. Postać trygonometryczna i wykładnicza

Na płaszczyźnie zespolonej Gaussa liczba $z = x + iy \neq 0$ jest jednoznacznie wyznaczona przez współrzędne biegunowe $(r, \varphi)$:
$$x = r \cos \varphi, \quad y = r \sin \varphi$$
gdzie $r = |z| = \sqrt{x^2 + y^2} > 0$, a kąt $\varphi \in \mathbb{R}$ nazywamy **argumentem** liczby $z$ ($\arg z$).

Kąt $\varphi_0 \in (-\pi, \pi]$ spełniający ten układ nazywamy **argumentem głównym** ($\operatorname{Arg} z$).

#### Definicja 2.2 (Postać trygonometryczna)
$$z = |z| (\cos \varphi + i \sin \varphi)$$

#### Wzór Eulera i postać wykładnicza
Wykorzystując szeregi potęgowe (wprowadzone ściśle w Części VIII), definiujemy funkcję wykładniczą zmiennej urojonej:
$$e^{i\varphi} = \cos \varphi + i \sin \varphi$$
Daje to **postać wykładniczą liczby zespolonej**:
$$z = |z| e^{i\varphi}$$

Z tożsamości tej wynikają fundamentalne wzory Eulera wyrażające funkcje trygonometryczne przez funkcje wykładnicze:
$$\cos \varphi = \frac{e^{i\varphi} + e^{-i\varphi}}{2}, \quad \sin \varphi = \frac{e^{i\varphi} - e^{-i\varphi}}{2i}$$

#### Mnożenie, dzielenie i wzór de Moivre'a
Dla $z_1 = r_1 e^{i\varphi_1}$ i $z_2 = r_2 e^{i\varphi_2}$:
1. **Mnożenie:**
   $$z_1 \cdot z_2 = r_1 r_2 e^{i(\varphi_1 + \varphi_2)} = r_1 r_2 \big( \cos(\varphi_1 + \varphi_2) + i \sin(\varphi_1 + \varphi_2) \big)$$
2. **Dzielenie:**
   $$\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\varphi_1 - \varphi_2)} = \frac{r_1}{r_2} \big( \cos(\varphi_1 - \varphi_2) + i \sin(\varphi_1 - \varphi_2) \big) \quad (z_2 \neq 0)$$

> **Twierdzenie 2.2 (Wzór de Moivre'a):**
> Dla dowolnej liczby całkowitej $n \in \mathbb{Z}$ oraz $\varphi \in \mathbb{R}$:
> $$(\cos \varphi + i \sin \varphi)^n = \cos(n\varphi) + i \sin(n\varphi)$$
> W postaci wykładniczej:
> $$(e^{i\varphi})^n = e^{in\varphi}$$

---

### 2.3. Pierwiastkowanie w ciele liczb zespolonych

W przeciwieństwie do ciała $\mathbb{R}$, w ciele $\mathbb{C}$ każda liczba różna od zera posiada dokładnie $n$ różnych pierwiastków algebraicznych stopnia $n$.

#### Definicja 2.3 (Pierwiastek $n$-tego stopnia)
Liczbę $w \in \mathbb{C}$ nazywamy pierwiastkiem $n$-tego stopnia ($n \in \mathbb{N}, n \ge 2$) z liczby $z \in \mathbb{C}$, jeżeli $w^n = z$. Zbiór wszystkich takich pierwiastków oznaczamy $\sqrt[n]{z}$.

> **Twierdzenie 2.3 (Wzór na pierwiastki zespolone):**
> Jeżeli $z = r e^{i\varphi} \neq 0$, to istnieje dokładnie $n$ różnych pierwiastków $n$-tego stopnia z liczby $z$, danych wzorem:
> $$w_k = \sqrt[n]{r} \left( \cos \frac{\varphi + 2k\pi}{n} + i \sin \frac{\varphi + 2k\pi}{n} \right) = \sqrt[n]{r} \exp\left( i \frac{\varphi + 2k\pi}{n} \right)$$
> dla $k = 0, 1, 2, \dots, n-1$.

#### Interpretacja geometryczna
Wszystkie pierwiastki $w_0, w_1, \dots, w_{n-1}$:
1. Mają identyczny moduł równy $\sqrt[n]{r}$, co oznacza, że leżą na okręgu o środku w początku układu współrzędnych i promieniu $R = \sqrt[n]{r}$.
2. Dzielą ten okrąg na $n$ równych łuków o mierze kątowej $\Delta \varphi = \frac{2\pi}{n}$.
3. Stanowią **wierzchołki $n$-kąta foremnego** wpisanego w ten okrąg.

---

### 2.4. Zastosowania inżynierskie: Metoda symboliczna w teorii obwodów (WEiTI PW)

W elektrotechnice teoretycznej i analizie obwodów liniowych (przedmioty *Teoria Obwodów 1 i 2* na WEiTI) operacje różniczkowania i całkowania równań różniczkowych sprowadza się do prostych działań algebraicznych w ciele liczb zespolonych.

#### Reprezentacja fazorowa sygnału harmonicznego
Niech napięcie sinusoidalne będzie dane funkcją czasu:
$$u(t) = U_m \cos(\omega t + \psi)$$
gdzie $U_m$ to amplituda, $\omega$ – pulsacja, $\psi$ – faza początkowa.
Z tożsamości Eulera:
$$u(t) = \operatorname{Re}\Big( U_m e^{j(\omega t + \psi)} \Big) = \operatorname{Re}\Big( \underline{U}_m e^{j\omega t} \Big)$$
gdzie liczbę zespoloną:
$$\underline{U}_m = U_m e^{j\psi} = U_m (\cos \psi + j \sin \psi)$$
nazywamy **amplitudą zespoloną** (fazorem amplitudy). Wartość skuteczna zespolona to $\underline{U} = \frac{\underline{U}_m}{\sqrt{2}}$.

#### Różniczkowanie w dziedzinie fazorowej
Jeżeli $u(t) \longleftrightarrow \underline{U}$, to pochodna sygnału:
$$\frac{d u(t)}{dt} = \frac{d}{dt}\operatorname{Re}\left( \underline{U} e^{j\omega t} \right) = \operatorname{Re}\left( j\omega \underline{U} e^{j\omega t} \right) \longleftrightarrow j\omega \underline{U}$$
Różniczkowanie odpowiada pomnożeniu fazora przez operator $j\omega$.  
Analogicznie całkowanie odpowiada dzieleniu przez $j\omega$:
$$\int u(t) \, dt \longleftrightarrow \frac{1}{j\omega} \underline{U}$$

#### Impedancja zespolona $\underline{Z}$
Równanie konstytutywne dla elementów RLC w dziedzinie fazorów ma postać prawa Ohma:
$$\underline{U} = \underline{Z} \cdot \underline{I}$$
gdzie $\underline{Z} = R + jX$:
- $R = \operatorname{Re}(\underline{Z})$ – rezystancja (opór czynny),
- $X = \operatorname{Im}(\underline{Z})$ – reaktancja (opór bierny).

Dla podstawowych elementów:
1. **Rezystor $R$:** $u(t) = R i(t) \implies \underline{Z}_R = R$.
2. **Cewka $L$:** $u(t) = L \frac{di(t)}{dt} \implies \underline{U} = j\omega L \underline{I} \implies \underline{Z}_L = j\omega L$.
3. **Kondensator $C$:** $i(t) = C \frac{du(t)}{dt} \implies \underline{I} = j\omega C \underline{U} \implies \underline{Z}_C = \frac{1}{j\omega C} = -j \frac{1}{\omega C}$.

---

### 2.5. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 1.1: Ścisłe wyznaczanie kresów zbioru
Wyznacz $\sup A$ oraz $\inf A$ dla zbioru:
$$A = \left\{ \frac{2n - 1}{n + 2} : n \in \mathbb{N} \right\}, \quad \mathbb{N} = \{1, 2, 3, \dots\}$$
oraz udowodnij wynik na podstawie definicji $\varepsilon$-owej.

**Rozwiązanie:**
Przekształćmy wyraz ogólny:
$$x_n = \frac{2n - 1}{n + 2} = \frac{2(n + 2) - 5}{n + 2} = 2 - \frac{5}{n + 2}$$
Dla $n \ge 1$ ciąg $x_n$ jest rosnący:
$$x_1 = \frac{2(1) - 1}{1 + 2} = \frac{1}{3}$$
$$x_2 = \frac{3}{4}, \quad x_3 = \frac{5}{5} = 1, \quad \dots, \quad \lim_{n \to \infty} x_n = 2$$
Podejrzewamy, że $\inf A = \frac{1}{3}$ oraz $\sup A = 2$.

1. **Dowód dla $\inf A = \frac{1}{3}$:**
   - Ograniczenie dolne: Dla każdego $n \ge 1$:
     $$2 - \frac{5}{n+2} \ge 2 - \frac{5}{1+2} = 2 - \frac{5}{3} = \frac{1}{3}$$
   - Element najmniejszy: Ponieważ $x_1 = \frac{1}{3} \in A$, kres dolny jest osiągany jako element najmniejszy: $\inf A = \min A = \frac{1}{3}$.

2. **Dowód dla $\sup A = 2$:**
   - Ograniczenie górne: Dla każdego $n \ge 1$:
     $$2 - \frac{5}{n+2} < 2 \implies \forall_{x \in A} \ x \le 2$$
   - Warunek $\varepsilon$-owy: Niech dany będzie dowolny $\varepsilon > 0$. Szukamy takiego $n \in \mathbb{N}$, aby zachodziło:
     $$x_n > 2 - \varepsilon \iff 2 - \frac{5}{n+2} > 2 - \varepsilon \iff \frac{5}{n+2} < \varepsilon \iff n + 2 > \frac{5}{\varepsilon} \iff n > \frac{5}{\varepsilon} - 2$$
     Na mocy Zasady Archimedesa zawsze istnieje taka liczba naturalna $n_0 \in \mathbb{N}$, że $n_0 > \max\left(1, \left\lfloor \frac{5}{\varepsilon} - 2 \right\rfloor\right)$.
     Dla tego elementu $x_{n_0} \in A$ zachodzi $x_{n_0} > 2 - \varepsilon$.
   Zatem z definicji $\sup A = 2$ (kres górny nie jest osiągany w zbiorze: $\max A$ nie istnieje).

---

#### Przykład 1.2: Równanie algebraiczne w ciele liczb zespolonych
Rozwiąż w ciele $\mathbb{C}$ równanie:
$$z^2 + 2\bar{z} = 0$$

**Rozwiązanie:**
Niech $z = x + iy$, gdzie $x, y \in \mathbb{R}$. Wtedy $\bar{z} = x - iy$ oraz:
$$z^2 = (x + iy)^2 = x^2 - y^2 + 2ixy$$
Wstawiając do równania:
$$(x^2 - y^2 + 2x) + i(2xy - 2y) = 0$$
Liczba zespolona jest równa zero wtedy i tylko wtedy, gdy jej część rzeczywista i urojona są równe zero:
$$\begin{cases}
x^2 - y^2 + 2x = 0 \\
2y(x - 1) = 0
\end{cases}$$
Z drugiego równania otrzymujemy dwa przypadki: $y = 0$ lub $x = 1$.

- **Przypadek 1: $y = 0$**
  Wstawiamy do pierwszego równania:
  $$x^2 + 2x = 0 \iff x(x + 2) = 0 \implies x_1 = 0, \quad x_2 = -2$$
  Daje to dwa rozwiązania:
  $$z_1 = 0, \quad z_2 = -2$$

- **Przypadek 2: $x = 1$**
  Wstawiamy do pierwszego równania:
  $$1^2 - y^2 + 2(1) = 0 \iff 3 - y^2 = 0 \iff y^2 = 3 \implies y_3 = \sqrt{3}, \quad y_4 = -\sqrt{3}$$
  Daje to kolejne dwa rozwiązania:
  $$z_3 = 1 + i\sqrt{3}, \quad z_4 = 1 - i\sqrt{3}$$

**Odpowiedź:** Równanie posiada 4 rozwiązania:
$$z \in \{0, -2, 1 + i\sqrt{3}, 1 - i\sqrt{3}\}$$

---

#### Przykład 1.3: Pierwiastkowanie liczby zespolonej
Wyznacz wszystkie pierwiastki stopnia 4 z liczby $z = -8 + i 8\sqrt{3}$.

**Rozwiązanie:**
1. Wyznaczamy moduł liczby $z$:
   $$|z| = \sqrt{(-8)^2 + (8\sqrt{3})^2} = \sqrt{64 + 64 \cdot 3} = \sqrt{64 \cdot 4} = \sqrt{256} = 16$$
2. Wyznaczamy argument główny $\varphi$:
   $$\cos \varphi = \frac{x}{|z|} = \frac{-8}{16} = -\frac{1}{2}, \quad \sin \varphi = \frac{y}{|z|} = \frac{8\sqrt{3}}{16} = \frac{\sqrt{3}}{2}$$
   Punkt leży w II ćwiartce płaszczyzny zespolonej:
   $$\varphi = \pi - \frac{\pi}{3} = \frac{2\pi}{3}$$
   Zatem postać wykładnicza: $z = 16 \exp\left( i \frac{2\pi}{3} \right)$.
3. Stosujemy wzór na pierwiastki ($n = 4$):
   $$|w_k| = \sqrt[4]{16} = 2$$
   $$\varphi_k = \frac{\frac{2\pi}{3} + 2k\pi}{4} = \frac{\pi}{6} + k \frac{\pi}{2}, \quad k \in \{0, 1, 2, 3\}$$

Obliczamy poszczególne pierwiastki:
- Dla $k = 0$:
  $$w_0 = 2 \left( \cos \frac{\pi}{6} + i \sin \frac{\pi}{6} \right) = 2 \left( \frac{\sqrt{3}}{2} + i \frac{1}{2} \right) = \sqrt{3} + i$$
- Dla $k = 1$:
  $$w_1 = 2 \left( \cos \frac{2\pi}{3} + i \sin \frac{2\pi}{3} \right) = 2 \left( -\frac{1}{2} + i \frac{\sqrt{3}}{2} \right) = -1 + i\sqrt{3}$$
- Dla $k = 2$:
  $$w_2 = 2 \left( \cos \frac{7\pi}{6} + i \sin \frac{7\pi}{6} \right) = 2 \left( -\frac{\sqrt{3}}{2} - i \frac{1}{2} \right) = -\sqrt{3} - i = -w_0$$
- Dla $k = 3$:
  $$w_3 = 2 \left( \cos \frac{5\pi}{3} + i \sin \frac{5\pi}{3} \right) = 2 \left( \frac{1}{2} - i \frac{\sqrt{3}}{2} \right) = 1 - i\sqrt{3} = -w_1$$

Wszystkie cztery pierwiastki tworzą na płaszczyźnie zespolonej wierzchołki kwadratu wpisanego w okrąg o promieniu $R = 2$.

---

### 2.6. Zadania do samodzielnego rozwiązania

1. **Zadanie 1.1:** Wyznacz kres górny i dolny zbioru $B = \left\{ \frac{3k}{k+1} : k \in \mathbb{N} \right\}$. Czy zbiór posiada element największy lub najmniejszy?
2. **Zadanie 1.2:** Wykaż za pomocą definicji $\varepsilon$-owej, że $\inf \left\{ \frac{1}{n^2} : n \in \mathbb{N} \right\} = 0$.
3. **Zadanie 1.3:** Przedstaw w postaci algebraicznej liczbę $z = \frac{(1 + i\sqrt{3})^{10}}{(1 - i)^{8}}$.
4. **Zadanie 1.4:** Rozwiąż w ciele liczb zespolonych równanie: $z^4 + 16 = 0$. Zaznacz rozwiązania na płaszczyźnie Gaussa.
5. **Zadanie 1.5 (Teoria obwodów):** Obwód szeregowy RLC zasilany jest napięciem o pulsacji $\omega = 1000\text{ rad/s}$. Wartości elementów wynoszą: $R = 10\,\Omega$, $L = 20\text{ mH}$, $C = 50\,\mu\text{F}$. Wyznacz impedancję zespoloną $\underline{Z}$, jej moduł oraz kąt przesunięcia fazowego $\varphi$.

---

### Odpowiedzi i wskazówki do zadań

- **1.1:** $\inf B = \min B = \frac{3}{2}$ (dla $k = 1$), $\sup B = 3$, brak elementu największego ($\max B$ nie istnieje).
- **1.2:** Dla dowolnego $\varepsilon > 0$ wystarczy dobrać $n > \frac{1}{\sqrt{\varepsilon}}$ na mocy zasady Archimedesa.
- **1.3:** $1 + i\sqrt{3} = 2 e^{i\pi/3} \implies (1 + i\sqrt{3})^{10} = 2^{10} e^{i10\pi/3} = 1024 e^{i4\pi/3} = 1024\left(-\frac{1}{2} - i\frac{\sqrt{3}}{2}\right) = -512 - i 512\sqrt{3}$. Mianownik: $1 - i = \sqrt{2} e^{-i\pi/4} \implies (1 - i)^8 = (\sqrt{2})^8 e^{-i2\pi} = 16$. Zatem $z = \frac{-512 - i 512\sqrt{3}}{16} = -32 - 32i\sqrt{3}$.
- **1.4:** $z = \sqrt[4]{-16}$. Rozwiązania tworzą wierzchołki kwadratu o promieniu $R = 2$: $z_k = 2 \exp\left( i \frac{\pi + 2k\pi}{4} \right)$, skąd: $z_0 = \sqrt{2} + i\sqrt{2}$, $z_1 = -\sqrt{2} + i\sqrt{2}$, $z_2 = -\sqrt{2} - i\sqrt{2}$, $z_3 = \sqrt{2} - i\sqrt{2}$.
- **1.5:** $\underline{Z}_L = j\omega L = j \cdot 1000 \cdot 0{,}02 = j20\,\Omega$. $\underline{Z}_C = \frac{1}{j\omega C} = \frac{-j}{1000 \cdot 50 \cdot 10^{-6}} = -j20\,\Omega$. Zatem impedancja całkowita: $\underline{Z} = R + j(\omega L - \frac{1}{\omega C}) = 10 + j(20 - 20) = 10\,\Omega$. Moduł $|\underline{Z}| = 10\,\Omega$, faza $\varphi = 0^\circ$ (stan rezonansu napięć).


\newpage

# Część II: Ciągi Liczbowe

Teoria ciągów liczbowych stanowi punkt wyjścia dla całego aparatu analizy matematycznej – pojęcie granicy ciągu jest fundamentem, na którym buduje się definicje szeregów liczbowych, granic funkcji, ciągłości, pochodnych oraz całek. W inżynierii informatycznej i elektronicznej ciągi odpowiadają **sygnałom dyskretnym w czasie** $x[n]$ oraz procesom iteracyjnym w algorytmach numerycznych.

---

## Rozdział 3: Granica ciągu liczbowego

### 3.1. Podstawowe pojęcia i sposoby zadawania ciągów

#### Definicja 3.1 (Ciąg liczbowy)
Ciągiem liczb rzeczywistych nazywamy odwzorowanie zbioru liczb naturalnych $\mathbb{N} = \{1, 2, 3, \dots\}$ w zbiór liczb rzeczywistych $\mathbb{R}$:
$$a: \mathbb{N} \to \mathbb{R}, \quad a(n) = a_n$$
Wartość $a_n$ nazywamy $n$-tym wyrazem ciągu, a sam ciąg oznaczamy symbolem $(a_n)_{n=1}^\infty$ lub krócej $(a_n)$.

Ciąg może być zadany:
1. **Wzorem jawnym (analitycznym):** np. $a_n = \frac{2n - 1}{3n + 4}$,
2. **Równaniem rekurencyjnym (różnicowym):** np. $a_1 = 1, \ a_{n+1} = \frac{1}{2}\left(a_n + \frac{2}{a_n}\right)$ (algorytm Herona obliczania $\sqrt{2}$),
3. **Opisem słownym/właściwościowym.**

#### Definicja 3.2 (Ograniczoność ciągu)
1. Ciąg $(a_n)$ jest **ograniczony z góry**, jeżeli:
   $$\exists_{M \in \mathbb{R}} \forall_{n \in \mathbb{N}} \quad a_n \le M$$
2. Ciąg $(a_n)$ jest **ograniczony z dołu**, jeżeli:
   $$\exists_{m \in \mathbb{R}} \forall_{n \in \mathbb{N}} \quad a_n \ge m$$
3. Ciąg $(a_n)$ jest **ograniczony**, jeżeli jest ograniczony z góry i z dołu:
   $$\exists_{K > 0} \forall_{n \in \mathbb{N}} \quad |a_n| \le K$$

#### Definicja 3.3 (Monotoniczność ciągu)
Ciąg $(a_n)$ nazywamy:
- **rosnącym** ($\forall_{n} \ a_{n+1} > a_n$),
- **niemalejącym** ($\forall_{n} \ a_{n+1} \ge a_n$),
- **malejącym** ($\forall_{n} \ a_{n+1} < a_n$),
- **nierosnącym** ($\forall_{n} \ a_{n+1} \le a_n$).

---

### 3.2. Definicja granicy właściwej (Definicja Cauchy'ego $\varepsilon-N$)

#### Definicja 3.4 (Granica właściwa ciągu)
Liczbę $g \in \mathbb{R}$ nazywamy **granicą właściwą** ciągu $(a_n)$, co zapisujemy:
$$\lim_{n \to \infty} a_n = g \quad \text{lub} \quad a_n \xrightarrow[n \to \infty]{} g$$
jeżeli dla każdej liczby $\varepsilon > 0$ istnieje taki wskaźnik $N \in \mathbb{N}$ (zależny na ogół od $\varepsilon$, $N = N(\varepsilon)$), że dla wszystkich wyrazów o wskaźnikach $n > N$ odległość $a_n$ od $g$ jest mniejsza od $\varepsilon$:

$$\forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{n \in \mathbb{N}} \quad (n > N \implies |a_n - g| < \varepsilon)$$

#### Interpretacja geometryczna i topologiczna
Warunek $|a_n - g| < \varepsilon$ jest równoważny temu, że $a_n \in U(g, \varepsilon) = (g - \varepsilon, g + \varepsilon)$.  
Oznacza to, że:
> W dowolnie małym otoczeniu punktu $g$ znajdują się **prawie wszystkie** (czyli wszystkie poza co najwyżej skończoną liczbą) wyrazy ciągu $(a_n)$. Poza otoczeniem $U(g, \varepsilon)$ może leżeć co najwyżej $N$ początkowych wyrazów ciągu.

Ciąg, który posiada granicę właściwą $g \in \mathbb{R}$, nazywamy **ciągiem zbieżnym**. Ciąg, który nie jest zbieżny, nazywamy **ciągiem rozbieżnym**.

---

### 3.3. Fundamentalne twierdzenia o zbieżności ciągów

> **Twierdzenie 3.1 (Jedyność granicy):**
> Jeżeli ciąg $(a_n)$ posiada granicę, to jest ona wyznaczona jednoznacznie.

**Dowód (nie wprost):**
Załóżmy przeciwnie, że ciąg $(a_n)$ posiada dwie różne granice $g_1, g_2 \in \mathbb{R}$, gdzie $g_1 \neq g_2$. Wówczas odległość między nimi wynosi $d = |g_1 - g_2| > 0$.  
Wybierzmy $\varepsilon = \frac{d}{2} = \frac{|g_1 - g_2|}{2} > 0$.
- Z faktu, że $\lim a_n = g_1$, istnieje $N_1$ takie, że $\forall_{n > N_1} \ |a_n - g_1| < \varepsilon$.
- Z faktu, że $\lim a_n = g_2$, istnieje $N_2$ takie, że $\forall_{n > N_2} \ |a_n - g_2| < \varepsilon$.

Niech $N_0 = \max(N_1, N_2)$. Dla dowolnego $n > N_0$, stosując nierówność trójkąta:
$$|g_1 - g_2| = |(g_1 - a_n) + (a_n - g_2)| \le |g_1 - a_n| + |a_n - g_2| < \varepsilon + \varepsilon = 2\varepsilon$$
Wstawiając $\varepsilon = \frac{|g_1 - g_2|}{2}$, otrzymujemy:
$$|g_1 - g_2| < |g_1 - g_2|$$
Otrzymana sprzeczność dowodzi, że ciąg nie może posiadać dwóch różnych granic. $\blacksquare$

> **Twierdzenie 3.2 (Ograniczoność ciągu zbieżnego):**
> Każdy ciąg zbieżny jest ograniczony.

**Dowód:**
Niech $\lim_{n \to \infty} a_n = g$. Z definicji granicy przyjmijmy $\varepsilon = 1$. Istnieje $N \in \mathbb{N}$ takie, że:
$$\forall_{n > N} \quad |a_n - g| < 1 \implies g - 1 < a_n < g + 1$$
Zdefiniujmy liczby:
$$m = \min(a_1, a_2, \dots, a_N, g - 1), \quad M = \max(a_1, a_2, \dots, a_N, g + 1)$$
Wówczas dla każdego $n \in \mathbb{N}$ zachodzi nierówność $m \le a_n \le M$, co oznacza, że ciąg $(a_n)$ jest ograniczony. $\blacksquare$

*(Uwaga: Twierdzenie odwrotne nie jest prawdziwe – ciąg ograniczony $a_n = (-1)^n$ nie jest zbieżny).*

---

### 3.4. Granice niewłaściwe

#### Definicja 3.5 (Granice niewłaściwe)
1. Ciąg $(a_n)$ ma granicę niewłaściwą $+\infty$, co zapisujemy $\lim_{n \to \infty} a_n = +\infty$, jeżeli:
   $$\forall_{M \in \mathbb{R}} \exists_{N \in \mathbb{N}} \forall_{n > N} \quad a_n > M$$
2. Ciąg $(a_n)$ ma granicę niewłaściwą $-\infty$, co zapisujemy $\lim_{n \to \infty} a_n = -\infty$, jeżeli:
   $$\forall_{M \in \mathbb{R}} \exists_{N \in \mathbb{N}} \forall_{n > N} \quad a_n < M$$

#### Symbole nieoznaczone
Podczas obliczania granic spotyka się tzw. symbole nieoznaczone, których wartość zależy od tempa zbieżności poszczególnych składników:
$$\left[ \frac{\infty}{\infty} \right], \quad \left[ \frac{0}{0} \right], \quad [\infty - \infty], \quad [0 \cdot \infty], \quad [1^\infty], \quad [0^0], \quad [\infty^0]$$
Wyrażenia tego typu wymagają przekształceń algebraicznych, zastosowania twierdzenia o trzech ciągach lub twierdzeń z liczbą $e$.

---

## Rozdział 4: Twierdzenia o granicach ciągów

### 4.1. Arytmetyka granic

> **Twierdzenie 4.1 (Twierdzenie o działaniach arytmetycznych na granicach):**
> Jeżeli ciągi $(a_n)$ i $(b_n)$ są zbieżne oraz $\lim_{n \to \infty} a_n = a$, $\lim_{n \to \infty} b_n = b$, to:
> 1. $\lim_{n \to \infty} (a_n \pm b_n) = a \pm b$
> 2. $\lim_{n \to \infty} (c \cdot a_n) = c \cdot a \quad (c \in \mathbb{R})$
> 3. $\lim_{n \to \infty} (a_n \cdot b_n) = a \cdot b$
> 4. $\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{a}{b} \quad (\text{o ile } b \neq 0 \text{ oraz } \forall_n \ b_n \neq 0)$

**Dowód dla iloczynu:**
Zauważmy tożsamość:
$$|a_n b_n - ab| = |a_n b_n - a_n b + a_n b - ab| \le |a_n||b_n - b| + |b||a_n - a|$$
Ponieważ ciąg $(a_n)$ jest zbieżny, jest ograniczony (Tw. 3.2), więc $\exists_{K > 0} \forall_n \ |a_n| \le K$. Niech $M = \max(K, |b|) > 0$.
Dla dowolnego $\varepsilon > 0$:
- $\exists_{N_1} \forall_{n > N_1} \ |a_n - a| < \frac{\varepsilon}{2M}$
- $\exists_{N_2} \forall_{n > N_2} \ |b_n - b| < \frac{\varepsilon}{2M}$
Dla $n > N = \max(N_1, N_2)$:
$$|a_n b_n - ab| \le K \cdot \frac{\varepsilon}{2M} + |b| \cdot \frac{\varepsilon}{2M} \le M \frac{\varepsilon}{2M} + M \frac{\varepsilon}{2M} = \varepsilon$$
co dowodzi, że $\lim (a_n b_n) = ab$. $\blacksquare$

---

### 4.2. Twierdzenie o trzech ciągach

> **Twierdzenie 4.2 (O trzech ciągach):**
> Jeżeli ciągi $(a_n), (b_n), (c_n)$ spełniają nierówność:
> $$\exists_{N_0 \in \mathbb{N}} \forall_{n > N_0} \quad a_n \le b_n \le c_n$$
> oraz:
> $$\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = g$$
> to ciąg $(b_n)$ jest zbieżny i $\lim_{n \to \infty} b_n = g$.

**Dowód:**
Niech dany będzie dowolny $\varepsilon > 0$.
Z definicji granicy dla $(a_n)$ i $(c_n)$ od pewnego miejsca $N_1$:
$$g - \varepsilon < a_n < g + \varepsilon \quad \text{oraz} \quad g - \varepsilon < c_n < g + \varepsilon$$
Dla $n > \max(N_0, N_1)$ wykorzystujemy nierówność z założenia:
$$g - \varepsilon < a_n \le b_n \le c_n < g + \varepsilon \implies g - \varepsilon < b_n < g + \varepsilon \iff |b_n - g| < \varepsilon$$
Zatem $\lim_{n \to \infty} b_n = g$. $\blacksquare$

---

### 4.3. Ciągi monotoniczne i ograniczone. Liczba $e$

> **Twierdzenie 4.3 (Weierstrassa o ciągu monotonicznym i ograniczonym):**
> 1. Każdy ciąg niemalejący i ograniczony z góry jest zbieżny, przy czym:
>    $$\lim_{n \to \infty} a_n = \sup \{a_n : n \in \mathbb{N}\}$$
> 2. Każdy ciąg nierosnący i ograniczony z dołu jest zbieżny, przy czym:
>    $$\lim_{n \to \infty} a_n = \inf \{a_n : n \in \mathbb{N}\}$$

**Dowód (dla ciągu niemalejącego):**
Niech $A = \{a_n : n \in \mathbb{N}\}$. Zbiór $A$ jest niepusty i z założenia ograniczony z góry. Na mocy Aksjomatu Ciągłości (Tw. 1.1) istnieje kres górny $S = \sup A \in \mathbb{R}$.
Pokażemy, że $\lim_{n \to \infty} a_n = S$.
Niech dany będzie dowolny $\varepsilon > 0$. Z definicji supremum:
1. $\forall_{n \in \mathbb{N}} \ a_n \le S < S + \varepsilon$,
2. $\exists_{N \in \mathbb{N}} \ a_N > S - \varepsilon$.

Ponieważ ciąg $(a_n)$ jest niemalejący, dla każdego $n > N$ mamy $a_n \ge a_N > S - \varepsilon$.
Łącząc obie nierówności:
$$\forall_{n > N} \quad S - \varepsilon < a_n \le S < S + \varepsilon \implies |a_n - S| < \varepsilon$$
Zatem $\lim a_n = S = \sup A$. $\blacksquare$

---

#### Konstrukcja liczby $e$ (Stała Eulera-Napiera)
Rozpatrzmy ciąg:
$$a_n = \left( 1 + \frac{1}{n} \right)^n$$

> **Lemat 4.1:** Ciąg $a_n = \left(1 + \frac{1}{n}\right)^n$ jest rosnący i ograniczony z góry przez $3$.

**Dowód:**
Korzystając ze wzoru dwumianowego Newtona:
$$a_n = \sum_{k=0}^n \binom{n}{k} \left(\frac{1}{n}\right)^k = 1 + n \cdot \frac{1}{n} + \frac{n(n-1)}{2!} \frac{1}{n^2} + \dots + \frac{n(n-1)\dots(n-k+1)}{k!} \frac{1}{n^k} + \dots$$
$$a_n = 1 + 1 + \frac{1}{2!} \left(1 - \frac{1}{n}\right) + \frac{1}{3!} \left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) + \dots + \frac{1}{n!} \left(1 - \frac{1}{n}\right)\dots\left(1 - \frac{n-1}{n}\right)$$
Dla $a_{n+1}$ każdy czynnik $\left(1 - \frac{j}{n+1}\right) > \left(1 - \frac{j}{n}\right)$, a ponadto pojawia się dodatkowy dodatni składnik, skąd $a_{n+1} > a_n$ (ciąg rosnący).
Oszacowanie z góry: ponieważ $\left(1 - \frac{j}{n}\right) < 1$ oraz dla $k \ge 2$: $k! \ge 2^{k-1}$:
$$a_n < 1 + 1 + \frac{1}{2!} + \frac{1}{3!} + \dots + \frac{1}{n!} < 1 + \sum_{k=0}^{n-1} \left(\frac{1}{2}\right)^k < 1 + \frac{1}{1 - 1/2} = 3$$
Na mocy Twierdzenia Weierstrassa 4.3 ciąg $(a_n)$ posiada granicę właściwą:
$$e \stackrel{\text{def}}{=} \lim_{n \to \infty} \left( 1 + \frac{1}{n} \right)^n \approx 2{,}718281828459\dots$$

---

### 4.4. Twierdzenie Bolzano-Weierstrassa i warunek Cauchy'ego

#### Definicja 3.6 (Podciąg)
Niech dany będzie ciąg $(a_n)$. Jeżeli $(k_n)_{n=1}^\infty$ jest rosnącym ciągiem liczb naturalnych ($1 \le k_1 < k_2 < \dots$), to ciąg $(a_{k_n})_{n=1}^\infty$ nazywamy **podciągiem** ciągu $(a_n)$.

> **Twierdzenie 4.4 (Bolzano-Weierstrassa):**
> Z każdego ciągu ograniczonego można wybrać podciąg zbieżny.

**Zarys dowodu:**
Ciąg ograniczony zawiera się w pewnym przedziale domkniętym $[a, b]$. Dzielimy przedział na dwie połowy. Przynajmniej w jednej z nich leży nieskończenie wiele wyrazów ciągu. Wybieramy tę połowę $[a_1, b_1]$ i pierwszy wyraz $a_{k_1}$. Powtarzając tę procedurę nieskończenie wiele razy, otrzymujemy ciąg przedziałów zstępujących o długości zmierzającej do zera. Z zasady Cantora przekrój tych przedziałów zawiera dokładnie jeden punkt $g$, do którego zbiega wybrany podciąg $(a_{k_n})$. $\blacksquare$

> **Twierdzenie 4.5 (Warunek zbieżności Cauchy'ego):**
> Ciąg $(a_n)$ jest zbieżny w $\mathbb{R}$ wtedy i tylko wtedy, gdy spełnia warunek Cauchy'ego:
> $$\forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{m, n > N} \quad |a_n - a_m| < \varepsilon$$

---

### 4.5. Zastosowania inżynierskie: Liniowe równania różnicowe w filtrach cyfrowych (DSP)

W cyfrowym przetwarzaniu sygnałów (Digital Signal Processing - DSP na WEiTI) sygnał dyskretny reprezentowany jest ciągiem próbek $x[n]$.

Liniowy filtr cyfrowy o nieskończonej odpowiedzi impulsowej (IIR) pierwszego rzędu opisany jest równaniem różnicowym:
$$y[n] = a \cdot y[n-1] + x[n]$$
Dla skoku jednostkowego $x[n] = 1$ dla $n \ge 0$ oraz warunku początkowego $y[-1] = 0$:
$$y[0] = 1$$
$$y[1] = a + 1$$
$$y[2] = a(a + 1) + 1 = a^2 + a + 1$$
Ogólnie, $n$-ty wyraz ciągu wyjściowego wynosi:
$$y[n] = \sum_{k=0}^n a^k = \frac{1 - a^{n+1}}{1 - a} \quad (a \neq 1)$$

**Warunek stabilności asymptotycznej filtru:**
Odpowiedź filtru w stanie ustalonym jest zbieżna ($\lim_{n \to \infty} y[n] = \frac{1}{1-a}$) wtedy i tylko wtedy, gdy:
$$|a| < 1$$
Dla $|a| \ge 1$ ciąg wyjściowy jest rozbieżny (filtr niestabilny). Oznacza to, że biegun transmitancji dyskretnej musi leżeć **wewnątrz koła jednostkowego** na płaszczyźnie zespolonej $Z$.

---

### 4.6. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 2.1: Granica z twierdzenia o trzech ciągach
Oblicz granicę:
$$\lim_{n \to \infty} \sqrt[n]{3^n + 5^n + 7^n}$$

**Rozwiązanie:**
Najszybciej rosnącym składnikiem pod pierwiastkiem jest $7^n$. Konstruujemy oszacowania:
1. Z dołu: pomijamy mniejsze składniki dodatnie:
   $$7 = \sqrt[n]{7^n} \le \sqrt[n]{3^n + 5^n + 7^n}$$
2. Z góry: zastępujemy każdy składnik największym ($7^n$):
   $$\sqrt[n]{3^n + 5^n + 7^n} \le \sqrt[n]{7^n + 7^n + 7^n} = \sqrt[n]{3 \cdot 7^n} = 7 \cdot \sqrt[n]{3}$$

Mamy zatem:
$$7 \le \sqrt[n]{3^n + 5^n + 7^n} \le 7 \sqrt[n]{3}$$
Ponieważ $\lim_{n \to \infty} 7 = 7$ oraz $\lim_{n \to \infty} 7\sqrt[n]{3} = 7 \cdot 1 = 7$, na mocy twierdzenia o trzech ciągach:
$$\lim_{n \to \infty} \sqrt[n]{3^n + 5^n + 7^n} = 7$$

---

#### Przykład 2.2: Granice z liczbą $e$ i symbolem nieoznaczonym $[1^\infty]$
Oblicz granicę ciągu:
$$\lim_{n \to \infty} \left( \frac{2n^2 + 3}{2n^2 - 1} \right)^{3n^2}$$

**Rozwiązanie:**
Sprawdzamy bazę potęgi:
$$\lim_{n \to \infty} \frac{2n^2 + 3}{2n^2 - 1} = \lim_{n \to \infty} \frac{2 + 3/n^2}{2 - 1/n^2} = 1$$
Wykładnik zmierza do $+\infty$. Mamy symbol nieoznaczony $[1^\infty]$.  
Stosujemy tożsamość sprowadzającą do definicji liczby $e$:
$$\frac{2n^2 + 3}{2n^2 - 1} = 1 + \frac{(2n^2 + 3) - (2n^2 - 1)}{2n^2 - 1} = 1 + \frac{4}{2n^2 - 1}$$
Przekształcamy potęgę:
$$\left( 1 + \frac{4}{2n^2 - 1} \right)^{3n^2} = \left[ \left( 1 + \frac{1}{\frac{2n^2 - 1}{4}} \right)^{\frac{2n^2 - 1}{4}} \right]^{\frac{4}{2n^2 - 1} \cdot 3n^2}$$
Czynnik w nawiasie kwadratowym zmierza do $e$, ponieważ $\frac{2n^2 - 1}{4} \to \infty$.  
Obliczamy granicę wykładnika zewnętrznego:
$$\lim_{n \to \infty} \frac{12n^2}{2n^2 - 1} = \lim_{n \to \infty} \frac{12}{2 - 1/n^2} = 6$$
Stąd ostatecznie:
$$\lim_{n \to \infty} \left( \frac{2n^2 + 3}{2n^2 - 1} \right)^{3n^2} = e^6$$

---

#### Przykład 2.3: Zbieżność ciągu rekurencyjnego
Zbadaj zbieżność i oblicz granicę ciągu zadanego rekurencyjnie:
$$a_1 = \sqrt{2}, \quad a_{n+1} = \sqrt{2 + a_n}$$

**Rozwiązanie:**
1. **Ograniczoność z góry przez 2 (dowód indukcyjny):**
   - Dla $n = 1$: $a_1 = \sqrt{2} < 2$ (prawda).
   - Założenie indukcyjne: Załóżmy, że $a_k < 2$.
   - Teza: $a_{k+1} < 2$.
     Mamy: $a_{k+1} = \sqrt{2 + a_k} < \sqrt{2 + 2} = \sqrt{4} = 2$.
   Zasada indukcji dowodzi, że $\forall_{n \in \mathbb{N}} \ a_n < 2$.

2. **Monotoniczność (ciąg rosnący):**
   Badamy różnicę lub iloraz:
   $$a_{n+1} > a_n \iff \sqrt{2 + a_n} > a_n \iff 2 + a_n > a_n^2 \iff a_n^2 - a_n - 2 < 0$$
   Rozkładamy trójmian: $(a_n - 2)(a_n + 1) < 0$. Ponieważ $a_n > 0$ oraz $a_n < 2$, nierówność ta jest spełniona dla wszystkich $n$. Zatem ciąg jest ściśle rosnący.

3. **Obliczenie granicy:**
   Ciąg jest rosnący i ograniczony z góry, więc na mocy Twierdzenia Weierstrassa (Tw. 4.3) posiada granicę właściwą $g = \lim_{n \to \infty} a_n$.
   Przechodząc do granicy w równaniu rekurencyjnym:
   $$g = \sqrt{2 + g} \implies g^2 = 2 + g \implies g^2 - g - 2 = 0$$
   Pierwiastkami są $g = 2$ oraz $g = -1$. Ponieważ $a_n > 0$, granica musi być nieujemna ($g \ge \sqrt{2}$), stąd $g = 2$.

---

### 4.7. Zadania do samodzielnego rozwiązania

1. **Zadanie 2.1:** Wykaż bezpośrednio z definicji Cauchy'ego ($\varepsilon-N$), że $\lim_{n \to \infty} \frac{3n + 2}{n + 1} = 3$.
2. **Zadanie 2.2:** Oblicz granicę: $\lim_{n \to \infty} \left( \frac{1}{n^2 + 1} + \frac{2}{n^2 + 2} + \dots + \frac{n}{n^2 + n} \right)$.
3. **Zadanie 2.3:** Oblicz granicę: $\lim_{n \to \infty} \left( \sqrt{n^2 + 4n + 1} - \sqrt{n^2 - 2n} \right)$.
4. **Zadanie 2.4:** Oblicz granicę: $\lim_{n \to \infty} \left( \frac{n - 3}{n + 2} \right)^{2n+1}$.
5. **Zadanie 2.5 (DSP):** Ciąg próbek wyjściowych układu dyskretnego spełnia równanie $y[n] = 0{,}8 y[n-1] + 2$ dla $n \ge 1$ z warunkiem początkowym $y[0] = 0$. Wyznacz wzór ogólny $y[n]$ oraz oblicz wartość w stanie ustalonym $\lim_{n \to \infty} y[n]$.

---

### Odpowiedzi i wskazówki do zadań

- **2.1:** $\left|\frac{3n+2}{n+1} - 3\right| = \left|\frac{3n+2 - 3n - 3}{n+1}\right| = \frac{1}{n+1} < \varepsilon \iff n > \frac{1}{\varepsilon} - 1$. Wystarczy przyjąć $N = \max\left(1, \left\lfloor \frac{1}{\varepsilon} - 1 \right\rfloor\right)$.
- **2.2:** Stosujemy twierdzenie o trzech ciągach. Suma w liczniku wynosi $\sum_{k=1}^n k = \frac{n(n+1)}{2}$. Szacowanie z dołu: mianownik największy ($n^2 + n$), stąd $\frac{n(n+1)}{2(n^2+n)} = \frac{1}{2}$. Szacowanie z góry: mianownik najmniejszy ($n^2 + 1$), stąd $\frac{n(n+1)}{2(n^2+1)} \to \frac{1}{2}$. Wynik: $\frac{1}{2}$.
- **2.3:** Mnożymy przez sprzężenie sumy: $\frac{(n^2 + 4n + 1) - (n^2 - 2n)}{\sqrt{n^2 + 4n + 1} + \sqrt{n^2 - 2n}} = \frac{6n + 1}{n\sqrt{1 + 4/n + 1/n^2} + n\sqrt{1 - 2/n}} \xrightarrow[n \to \infty]{} \frac{6}{1 + 1} = 3$.
- **2.4:** $\frac{n-3}{n+2} = 1 - \frac{5}{n+2}$. Granica wynosi $e^{\lim (2n+1) \cdot (-5/(n+2))} = e^{-10}$.
- **2.5:** $y[1] = 2$, $y[2] = 2(0{,}8) + 2$, $y[n] = 2 \sum_{k=0}^{n-1} 0{,}8^k = 2 \cdot \frac{1 - 0{,}8^n}{1 - 0{,}8} = 10(1 - 0{,}8^n)$. Ponieważ $0{,}8 < 1$, $\lim_{n \to \infty} 0{,}8^n = 0$, więc wartość w stanie ustalonym wynosi $10$.


\newpage

# Część III: Szeregi Liczbowe

Szeregi liczbowe reprezentują ideę sumowania nieskończonej liczby składników. W analizie inżynierskiej, elektrotechnice i telekomunikacji szeregi stanowią podstawę aproksymacji sygnałów, obliczeń numerycznych, reprezentacji transmitancji oraz teorii stanów nieustalonych.

---

## Rozdział 5: Szeregi o wyrazach nieujemnych

### 5.1. Pojęcie szeregu liczbowego i zbieżności

#### Definicja 5.1 (Szereg liczbowy i suma częściowa)
Niech $(a_n)_{n=1}^\infty$ będzie ciągiem liczb rzeczywistych. Wyrażenie postaci:
$$\sum_{n=1}^\infty a_n = a_1 + a_2 + a_3 + \dots + a_n + \dots$$
nazywamy **szeregiem liczbowym**, a liczby $a_n$ jego **wyrazami**.

Ciąg $(S_n)_{n=1}^\infty$ zdefiniowany jako:
$$S_n = \sum_{k=1}^n a_k = a_1 + a_2 + \dots + a_n$$
nazywamy **ciągiem sum częściowych** szeregu.

#### Definicja 5.2 (Zbieżność i suma szeregu)
1. Jeżeli ciąg sum częściowych $(S_n)$ posiada granicę właściwą $S = \lim_{n \to \infty} S_n \in \mathbb{R}$, to mówimy, że szereg $\sum_{n=1}^\infty a_n$ jest **zbieżny**, a liczbę $S$ nazywamy **sumą szeregu**, co zapisujemy:
   $$\sum_{n=1}^\infty a_n = S$$
2. Jeżeli ciąg sum częściowych $(S_n)$ nie posiada granicy właściwej (zmierza do $\pm\infty$ lub granica nie istnieje), to szereg nazywamy **rozbieżnym**.

#### Definicja 5.3 (Reszta szeregu)
Dla szeregu zbieżnego o sumie $S$, wyrażenie:
$$R_n = S - S_n = \sum_{k=n+1}^\infty a_k$$
nazywamy $n$-tą **resztą szeregu**. Oczywiście $\lim_{n \to \infty} R_n = 0$.

---

### 5.2. Warunek konieczny zbieżności

> **Twierdzenie 5.1 (Warunek konieczny zbieżności szeregu):**
> Jeżeli szereg liczbowy $\sum_{n=1}^\infty a_n$ jest zbieżny, to jego wyraz ogólny zmierza do zera:
> $$\lim_{n \to \infty} a_n = 0$$

**Dowód:**
Zauważmy, że dla $n \ge 2$:
$$a_n = S_n - S_{n-1}$$
Ponieważ szereg jest zbieżny, $\lim_{n \to \infty} S_n = S$ oraz $\lim_{n \to \infty} S_{n-1} = S$. Z twierdzenia o granicy różnicy ciągów:
$$\lim_{n \to \infty} a_n = \lim_{n \to \infty} (S_n - S_{n-1}) = S - S = 0 \quad \blacksquare$$

> **Krytyczna uwaga (Kanon Decewicza/Żakowskiego):**
> Warunek $\lim_{n \to \infty} a_n = 0$ jest jedynie warunkiem **koniecznym**, a **nie dostatecznym**! Spełnienie tego warunku nie przesądza o zbieżności szeregu.  
> Klasycznym kontrprzykładem jest **szereg harmoniczny**:
> $$\sum_{n=1}^\infty \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots$$
> Mimo że $\lim_{n \to \infty} \frac{1}{n} = 0$, szereg ten jest rozbieżny do $+\infty$.

---

### 5.3. Szereg geometryczny

Rozpatrzmy szereg geometryczny o ilorazie $q \in \mathbb{R}$:
$$\sum_{n=0}^\infty q^n = 1 + q + q^2 + q^3 + \dots$$

Dla $q \neq 1$ suma pierwszych $n$ wyrazów wynosi:
$$S_n = \sum_{k=0}^{n-1} q^k = \frac{1 - q^n}{1 - q}$$

Badając granicę $\lim_{n \to \infty} S_n$:
1. Dla $|q| < 1$: $\lim_{n \to \infty} q^n = 0$, stąd szereg jest zbieżny i jego suma wynosi:
   $$\sum_{n=0}^\infty q^n = \frac{1}{1 - q}$$
2. Dla $|q| \ge 1$: wyraz ogólny $q^n$ nie dąży do zera, więc na mocy warunku koniecznego szereg jest rozbieżny.

---

### 5.4. Kryteria zbieżności szeregów o wyrazach nieujemnych ($a_n \ge 0$)

Dla szeregów o wyrazach nieujemnych ciąg sum częściowych jest niemalejący ($S_{n+1} = S_n + a_{n+1} \ge S_n$).  
Zatem szereg o wyrazach nieujemnych jest zbieżny wtedy i tylko wtedy, gdy ciąg jego sum częściowych jest ograniczony z góry.

#### Twierdzenie 5.2 (Kryterium porównawcze w postaci zwykłej)
Niech $0 \le a_n \le b_n$ dla wszystkich $n > n_0$:
1. Jeżeli szereg większy (majoranta) $\sum_{n=1}^\infty b_n$ jest **zbieżny**, to szereg mniejszy $\sum_{n=1}^\infty a_n$ jest również **zbieżny**.
2. Jeżeli szereg mniejszy (minoranta) $\sum_{n=1}^\infty a_n$ jest **rozbieżny**, to szereg większy $\sum_{n=1}^\infty b_n$ jest również **rozbieżny**.

#### Twierdzenie 5.3 (Kryterium porównawcze w postaci ilorazowej / granicznej)
Jeżeli $a_n > 0$ oraz $b_n > 0$ od pewnego miejsca i istnieje granica właściwa:
$$k = \lim_{n \to \infty} \frac{a_n}{b_n} \in (0, +\infty)$$
to oba szeregi $\sum a_n$ i $\sum b_n$ są **jednocześnie zbieżne** albo **jednocześnie rozbieżne**.

---

### 5.5. Kryteria d'Alemberta i Cauchy'ego

> **Twierdzenie 5.4 (Kryterium d'Alemberta - ilorazowe):**
> Niech $a_n > 0$. Załóżmy, że istnieje granica:
> $$D = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$$
> 1. Jeżeli $D < 1$, to szereg $\sum_{n=1}^\infty a_n$ jest **zbieżny**.
> 2. Jeżeli $D > 1$, to $\lim a_n \neq 0$ i szereg $\sum_{n=1}^\infty a_n$ jest **rozbieżny**.
> 3. Jeżeli $D = 1$, to kryterium nie rozstrzyga o zbieżności (należy zastosować inne kryterium).

**Dowód dla przypadku $D < 1$:**
Wybierzmy liczbę $q$ taką, że $D < q < 1$. Niech $\varepsilon = q - D > 0$.
Z definicji granicy ciągu ilorazów istnieje $N$ takie, że dla $n \ge N$:
$$\frac{a_{n+1}}{a_n} < D + \varepsilon = q$$
Wówczas:
$$a_{N+1} < q a_N$$
$$a_{N+2} < q a_{N+1} < q^2 a_N$$
Ogólnie dla $k \ge 1$:
$$a_{N+k} < a_N q^k$$
Szereg $\sum_{k=1}^\infty a_N q^k = a_N \sum_{k=1}^\infty q^k$ jest zbieżnym szeregiem geometrycznym (gdyż $q < 1$). Na mocy kryterium porównawczego (Tw. 5.2) szereg $\sum a_n$ jest zbieżny. $\blacksquare$

> **Twierdzenie 5.5 (Kryterium Cauchy'ego - pierwiastkowe):**
> Niech $a_n \ge 0$. Załóżmy, że istnieje granica:
> $$C = \lim_{n \to \infty} \sqrt[n]{a_n}$$
> 1. Jeżeli $C < 1$, to szereg $\sum_{n=1}^\infty a_n$ jest **zbieżny**.
> 2. Jeżeli $C > 1$, to szereg $\sum_{n=1}^\infty a_n$ jest **rozbieżny**.
> 3. Jeżeli $C = 1$, kryterium nie rozstrzyga o zbieżności.

---

### 5.6. Szereg harmoniczny rzędu $\alpha$ i kryterium całkowe

Szeregiem wzorcowym w kryteriach porównawczych jest **szereg harmoniczny rzędu $\alpha$**:
$$\sum_{n=1}^\infty \frac{1}{n^\alpha} = 1 + \frac{1}{2^\alpha} + \frac{1}{3^\alpha} + \dots$$

> **Twierdzenie 5.6:**
> Szereg $\sum_{n=1}^\infty \frac{1}{n^\alpha}$ jest:
> - **zbieżny** dla $\alpha > 1$,
> - **rozbieżny** dla $\alpha \le 1$.

> **Twierdzenie 5.7 (Kryterium całkowe Maclaurina-Cauchy'ego):**
> Jeżeli funkcja $f: [1, +\infty) \to [0, +\infty)$ jest nierosnąca i ciągła, oraz $a_n = f(n)$ dla każdego $n \in \mathbb{N}$, to szereg $\sum_{n=1}^\infty a_n$ oraz całka niewłaściwa:
> $$\int_1^\infty f(x) \, dx$$
> są **jednocześnie zbieżne** albo **jednocześnie rozbieżne**.

---

## Rozdział 6: Szeregi o wyrazach dowolnych

### 6.1. Zbieżność bezwzględna i warunkowa

Gdy wyrazy szeregu przyjmują dowolne znaki rzeczywiste (lub wartości zespolone $\mathbb{C}$), wprowadzamy fundamentalny podział na zbieżność bezwzględną i warunkową.

#### Definicja 6.1 (Zbieżność bezwzględna i warunkowa)
1. Szereg $\sum_{n=1}^\infty a_n$ nazywamy **bezwzględnie zbieżnym**, jeżeli zbieżny jest szereg utworzony z wartości bezwzględnych jego wyrazów:
   $$\sum_{n=1}^\infty |a_n| < \infty$$
2. Szereg nazywamy **warunkowo zbieżnym**, jeżeli jest on zbieżny, lecz nie jest zbieżny bezwzględnie (tzn. $\sum a_n$ jest zbieżny, ale $\sum |a_n| = +\infty$).

> **Twierdzenie 6.1:**
> Każdy szereg bezwzględnie zbieżny jest zbieżny w zwykłym sensie.

**Dowód:**
Zauważmy, że dla każdego $n$:
$$0 \le a_n + |a_n| \le 2|a_n|$$
Ponieważ szereg $\sum |a_n|$ jest zbieżny, szereg $\sum 2|a_n|$ jest zbieżny. Na mocy kryterium porównawczego szereg $\sum (a_n + |a_n|)$ jest zbieżny. Ponieważ $a_n = (a_n + |a_n|) - |a_n|$, jako różnica dwóch szeregów zbieżnych, szereg $\sum a_n$ jest zbieżny. $\blacksquare$

---

### 6.2. Szeregi naprzemienne i kryterium Leibniza

Szeregiem naprzemiennym nazywamy szereg postaci:
$$\sum_{n=1}^\infty (-1)^{n+1} b_n = b_1 - b_2 + b_3 - b_4 + \dots, \quad b_n > 0$$

> **Twierdzenie 6.2 (Kryterium Leibniza):**
> Jeżeli ciąg $(b_n)$ spełnia dwa warunki:
> 1. jest nierosnący: $\forall_{n \in \mathbb{N}} \ b_{n+1} \le b_n$,
> 2. zmierza do zera: $\lim_{n \to \infty} b_n = 0$,
> to szereg naprzemienny $\sum_{n=1}^\infty (-1)^{n+1} b_n$ jest **zbieżny**.
> Ponadto suma szeregu spełnia oszacowanie $0 \le S \le b_1$, a błąd odcięcia (reszta) spełnia:
> $$|R_n| = |S - S_n| \le b_{n+1}$$

#### Przykład klasyczny:
Szereg anharmoniczny:
$$\sum_{n=1}^\infty \frac{(-1)^{n+1}}{n} = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots$$
Ciąg $b_n = \frac{1}{n}$ jest malejący i dąży do 0. Na mocy kryterium Leibniza szereg jest zbieżny (jego suma wynosi $\ln 2$).  
Jednak szereg modułów to szereg harmoniczny $\sum \frac{1}{n} = \infty$.  
Zatem szereg anharmoniczny jest **zbieżny warunkowo**.

---

### 6.3. Zjawisko Riemanna o przestawianiu wyrazów

Własności zbieżności bezwzględnej i warunkowej diametralnie różnią się przy zmianie kolejności sumowania:

> **Twierdzenie 6.3 (O przemienności szeregów bezwzględnie zbieżnych):**
> W szeregu bezwzględnie zbieżnym można dowolnie zmieniać kolejność wyrazów (permutować wskaźniki), a suma szeregu pozostanie niezmieniona.

> **Twierdzenie 6.4 (Riemanna o szeregach warunkowo zbieżnych):**
> Jeżeli szereg $\sum a_n$ jest zbieżny warunkowo, to dla **dowolnej** liczby rzeczywistej $M \in \mathbb{R}$ (lub $\pm\infty$) istnieje taka permutacja wyrazów $\sigma: \mathbb{N} \to \mathbb{N}$, że:
> $$\sum_{n=1}^\infty a_{\sigma(n)} = M$$

Ten zaskakujący wynik dowodzi, że w obliczeniach numerycznych i algorytmice sumowanie szeregów warunkowo zbieżnych wymaga szczególnej ostrożności – zmiana kolejności sumowania zmiennoprzecinkowego w procesorze może prowadzić do zupełnie innych wyników.

---

### 6.4. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 3.1: Badanie zbieżności kryterium d'Alemberta
Zbadaj zbieżność szeregu:
$$\sum_{n=1}^\infty \frac{(2n)!}{(n!)^2 \cdot 5^n}$$

**Rozwiązanie:**
Stosujemy kryterium d'Alemberta ($a_n > 0$):
$$\frac{a_{n+1}}{a_n} = \frac{\frac{(2n+2)!}{((n+1)!)^2 \cdot 5^{n+1}}}{\frac{(2n)!}{(n!)^2 \cdot 5^n}} = \frac{(2n+2)!}{(2n)!} \cdot \frac{(n!)^2}{((n+1)!)^2} \cdot \frac{5^n}{5^{n+1}}$$
Rozpisujemy silnie:
$$\frac{(2n+2)!}{(2n)!} = (2n+1)(2n+2)$$
$$\frac{n!}{(n+1)!} = \frac{1}{n+1} \implies \frac{(n!)^2}{((n+1)!)^2} = \frac{1}{(n+1)^2}$$
Otrzymujemy:
$$\frac{a_{n+1}}{a_n} = \frac{(2n+1)(2n+2)}{(n+1)^2 \cdot 5} = \frac{2(2n+1)(n+1)}{5(n+1)^2} = \frac{2(2n+1)}{5(n+1)} = \frac{4n + 2}{5n + 5}$$
Obliczamy granicę:
$$D = \lim_{n \to \infty} \frac{4 + 2/n}{5 + 5/n} = \frac{4}{5}$$
Ponieważ $D = \frac{4}{5} < 1$, na mocy kryterium d'Alemberta szereg jest **zbieżny**.

---

#### Przykład 3.2: Badanie zbieżności kryterium Cauchy'ego
Zbadaj zbieżność szeregu:
$$\sum_{n=1}^\infty \left( \frac{3n - 1}{2n + 5} \right)^{n^2}$$

**Rozwiązanie:**
Stosujemy kryterium Cauchy'ego:
$$\sqrt[n]{a_n} = \sqrt[n]{\left( \frac{3n - 1}{2n + 5} \right)^{n^2}} = \left( \frac{3n - 1}{2n + 5} \right)^n$$
Badamy granicę przy $n \to \infty$. Zauważmy, że:
$$\lim_{n \to \infty} \frac{3n - 1}{2n + 5} = \frac{3}{2} > 1$$
Zatem:
$$C = \lim_{n \to \infty} \left( \frac{3n - 1}{2n + 5} \right)^n = \left(\frac{3}{2}\right)^\infty = +\infty$$
Ponieważ $C = +\infty > 1$, na mocy kryterium Cauchy'ego szereg jest **rozbieżny** (jego wyraz ogólny dąży do nieskończoności, więc nie spełnia nawet warunku koniecznego).

---

#### Przykład 3.3: Zbieżność bezwzględna i warunkowa
Zbadaj zbieżność bezwzględną i warunkową szeregu:
$$\sum_{n=1}^\infty \frac{(-1)^n}{\sqrt{n^2 + 2n} + n}$$

**Rozwiązanie:**
1. **Badanie zbieżności bezwzględnej:**
   Badamy szereg modułów:
   $$\sum_{n=1}^\infty \left| \frac{(-1)^n}{\sqrt{n^2 + 2n} + n} \right| = \sum_{n=1}^\infty \frac{1}{\sqrt{n^2 + 2n} + n}$$
   Dla dużych $n$ mianownik zachowuje się jak $n + n = 2n$.  
   Stosujemy ilorazowe kryterium porównawcze z rozbieżnym szeregiem harmonicznym $b_n = \frac{1}{n}$:
   $$\lim_{n \to \infty} \frac{a_n}{b_n} = \lim_{n \to \infty} \frac{\frac{1}{\sqrt{n^2+2n} + n}}{\frac{1}{n}} = \lim_{n \to \infty} \frac{n}{n(\sqrt{1 + 2/n} + 1)} = \frac{1}{1 + 1} = \frac{1}{2} \in (0, \infty)$$
   Ponieważ szereg harmoniczny $\sum \frac{1}{n}$ jest rozbieżny, szereg modułów jest **rozbieżny**. Szereg nie jest zatem bezwzględnie zbieżny.

2. **Badanie zbieżności warunkowej (Kryterium Leibniza):**
   Mamy szereg naprzemienny $(-1)^n b_n$, gdzie $b_n = \frac{1}{\sqrt{n^2 + 2n} + n}$.
   - Ciąg $b_n$ jest dodatni i oczywiście malejący (mianownik rośnie wraz z $n$).
   - $\lim_{n \to \infty} b_n = \lim_{n \to \infty} \frac{1}{\sqrt{n^2 + 2n} + n} = 0$.
   Założenia kryterium Leibniza są spełnione. Zatem szereg jest zbieżny.

**Wniosek:** Szereg jest **zbieżny warunkowo**.

---

### 6.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 3.1:** Zbadaj zbieżność szeregu: $\sum_{n=1}^\infty \frac{n^3 + 2}{2^n}$.
2. **Zadanie 3.2:** Zbadaj zbieżność szeregu: $\sum_{n=1}^\infty \frac{1}{n \ln^2(n+1)}$ za pomocą kryterium całkowego.
3. **Zadanie 3.3:** Zbadaj zbieżność szeregu: $\sum_{n=1}^\infty \left( \frac{n}{n+1} \right)^{n^2}$.
4. **Zadanie 3.4:** Określ, czy szereg $\sum_{n=1}^\infty \frac{(-1)^{n+1}}{\sqrt[3]{n}}$ jest zbieżny bezwzględnie, warunkowo, czy rozbieżny.
5. **Zadanie 3.5 (Inżynieria/Aproksymacja):** Oszacuj błąd odcięcia sumy $S \approx \sum_{n=1}^{10} \frac{(-1)^{n+1}}{n^4}$ za pomocą reszty Leibniza. Ile wyrazów należy zsumować, aby błąd bezwzględny był mniejszy niż $10^{-6}$?

---

### Odpowiedzi i wskazówki do zadań

- **3.1:** Zbieżny na mocy kryterium d'Alemberta ($D = \lim \frac{(n+1)^3}{n^3} \cdot \frac{1}{2} = \frac{1}{2} < 1$).
- **3.2:** Zbieżny. Całka $\int_2^\infty \frac{dx}{x \ln^2 x} = \left[ -\frac{1}{\ln x} \right]_2^\infty = \frac{1}{\ln 2} < \infty$.
- **3.3:** Zbieżny na mocy kryterium Cauchy'ego: $\lim \sqrt[n]{a_n} = \lim \left(\frac{n}{n+1}\right)^n = \lim \left(1 + \frac{1}{n}\right)^{-n} = e^{-1} = \frac{1}{e} < 1$.
- **3.4:** Zbieżny warunkowo. Na mocy kryterium Leibniza jest zbieżny, ale szereg modułów $\sum \frac{1}{n^{1/3}}$ to szereg harmoniczny o $\alpha = \frac{1}{3} \le 1$ (rozbieżny).
- **3.5:** Na mocy kryterium Leibniza $|R_{10}| \le b_{11} = \frac{1}{11^4} = \frac{1}{14641} \approx 6{,}83 \cdot 10^{-5}$. Aby $|R_n| < 10^{-6}$, żądamy $\frac{1}{(n+1)^4} < 10^{-6} \iff (n+1)^4 > 10^6 \iff n+1 > 10^{6/4} = 10\sqrt{10} \approx 31{,}62$, czyli wystarczy zsumować $n \ge 31$ wyrazów.


\newpage

# Część IV: Granica i Ciągłość Funkcji Jednej Zmiennej

Pojęcie granicy funkcji oraz jej ciągłości stanowi pomost łączący dyskretny świat ciągów liczbowych ze światem wielkości ciągłych. W elektronice i teorii sygnałów ciągłość opisuje zjawiska fizyczne, w których napięcia na pojemnościach i prądy w indukcyjnościach nie mogą zmieniać się w sposób skokowy (prawa komutacji), podczas gdy punkty nieciągłości modelują idealne przełączenia kluczy półprzewodnikowych i sygnały cyfrowe.

---

## Rozdział 7: Granica funkcji

### 7.1. Definicje granicy funkcji w punkcie

Niech $X \subset \mathbb{R}$ oraz $f: X \to \mathbb{R}$. Zakładamy, że punkt $x_0 \in \mathbb{R}$ jest **punktem skupienia** dziedziny $X$ (tzn. w każdym sąsiedztwie $x_0$ leży przynajmniej jeden punkt ze zbioru $X$).

Granicę funkcji w punkcie można zdefiniować na dwa równoważne sposoby: w ujęciu ciągowym (Heinego) oraz otoczeniowym (Cauchy'ego).

#### Definicja 7.1 (Definicja Heinego - ujęcie ciągowe)
Liczbę $g \in \mathbb{R}$ nazywamy **granicą funkcji $f$ w punkcie $x_0$ według Heinego**, co zapisujemy:
$$\lim_{x \to x_0} f(x) = g$$
jeżeli dla każdego ciągu argumentów $(x_n)_{n=1}^\infty \subset X \setminus \{x_0\}$ zbieżnego do $x_0$, odpowiadający mu ciąg wartości funkcji $(f(x_n))_{n=1}^\infty$ jest zbieżny do $g$:

$$\forall_{(x_n) \subset X \setminus \{x_0\}} \quad \left( \lim_{n \to \infty} x_n = x_0 \implies \lim_{n \to \infty} f(x_n) = g \right)$$

#### Definicja 7.2 (Definicja Cauchy'ego - ujęcie kwantyfikatorowe $\varepsilon-\delta$)
Liczbę $g \in \mathbb{R}$ nazywamy **granicą funkcji $f$ w punkcie $x_0$ według Cauchy'ego**, jeżeli:

$$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad \big( 0 < |x - x_0| < \delta \implies |f(x) - g| < \varepsilon \big)$$

#### Interpretacja:
Promień $\delta > 0$ określa rozmiar sąsiedztwa punktu $x_0$. Jeżeli argument $x$ znajdzie się w sąsiedztwie $S(x_0, \delta)$, to wartość funkcji $f(x)$ leży w zadanym otoczeniu $U(g, \varepsilon)$ o promieniu $\varepsilon$.

> **Twierdzenie 7.1 (Równoważność definicji Heinego i Cauchy'ego):**
> Definicja Heinego i definicja Cauchy'ego granicy funkcji w punkcie są równoważne:
> $$\lim_{x \to x_0}^{\text{Heine}} f(x) = g \iff \lim_{x \to x_0}^{\text{Cauchy}} f(x) = g$$

**Dowód:**
1. **$(\implies)$ (Dowód nie wprost):**  
   Załóżmy, że zachodzi warunek Heinego, lecz nie zachodzi warunek Cauchy'ego.  
   Negacja warunku Cauchy'ego ma postać:
   $$\exists_{\varepsilon_0 > 0} \forall_{\delta > 0} \exists_{x \in X} \quad \big( 0 < |x - x_0| < \delta \land |f(x) - g| \ge \varepsilon_0 \big)$$
   Dla każdego $n \in \mathbb{N}$ dobierzmy $\delta_n = \frac{1}{n}$. Istnieje wówczas element $x_n \in X \setminus \{x_0\}$ taki, że:
   $$|x_n - x_0| < \frac{1}{n} \quad \text{oraz} \quad |f(x_n) - g| \ge \varepsilon_0$$
   Ciąg $(x_n)$ zmierza do $x_0$ (gdyż $|x_n - x_0| < 1/n \to 0$). Jednak odpowiadający mu ciąg wartości $f(x_n)$ nie dąży do $g$, ponieważ dla każdego $n$ odległość $|f(x_n) - g| \ge \varepsilon_0 > 0$. Przeczy to definicji Heinego. Zatem z warunku Heinego wynika warunek Cauchy'ego.

2. **$(\impliedby)$:**  
   Załóżmy warunek Cauchy'ego i weźmy dowolny ciąg $(x_n) \subset X \setminus \{x_0\}$ zbieżny do $x_0$.  
   Dla ustalonego $\varepsilon > 0$ dobieramy $\delta > 0$ z warunku Cauchy'ego. Ponieważ $\lim x_n = x_0$, istnieje $N$ takie, że $\forall_{n > N} \ 0 < |x_n - x_0| < \delta$.  
   Z warunku Cauchy'ego wynika wtedy, że $\forall_{n > N} \ |f(x_n) - g| < \varepsilon$, co dowodzi, że $\lim_{n \to \infty} f(x_n) = g$. $\blacksquare$

---

### 7.2. Granice jednostronne i kryterium istnienia granicy

#### Definicja 7.3 (Granice jednostronne)
1. **Granica lewostronna** (ozn. $\lim_{x \to x_0^-} f(x)$ lub $f(x_0^-)$):
   $$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (x_0 - \delta < x < x_0 \implies |f(x) - g_L| < \varepsilon)$$
2. **Granica prawostronna** (ozn. $\lim_{x \to x_0^+} f(x)$ lub $f(x_0^+)$):
   $$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (x_0 < x < x_0 + \delta \implies |f(x) - g_P| < \varepsilon)$$

> **Twierdzenie 7.2 (Warunek konieczny i dostateczny istnienia granicy obustronnej):**
> Granica właściwa $\lim_{x \to x_0} f(x)$ istnieje wtedy i tylko wtedy, gdy istnieją obie granice jednostronne i są sobie równe:
> $$\lim_{x \to x_0} f(x) = g \iff \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) = g$$

---

### 7.3. Podstawowe granice wyrażeń nieoznaczonych

W analizie matematycznej szczególne znaczenie mają granice bazowe, służące do wyprowadzania pochodnych funkcji elementarnych:

> **Twierdzenie 7.3:**
> 1. $\lim_{x \to 0} \frac{\sin x}{x} = 1$
> 2. $\lim_{x \to 0} \frac{e^x - 1}{x} = 1$
> 3. $\lim_{x \to 0} \frac{\ln(1 + x)}{x} = 1$
> 4. $\lim_{x \to 0} \frac{(1 + x)^\alpha - 1}{x} = \alpha \quad (\alpha \in \mathbb{R})$

**Dowód dla $\lim_{x \to 0} \frac{\sin x}{x} = 1$:**
Rozważmy koło jednostkowe ($R = 1$) dla kąta $x \in \left(0, \frac{\pi}{2}\right)$.  
Porównując pola figur geometrycznych:
- Pole trójkąta wewnętrznego: $P_1 = \frac{1}{2} \cdot 1 \cdot \sin x = \frac{1}{2} \sin x$,
- Pole wycinka koła o kącie łukowym $x$: $P_2 = \frac{1}{2} \cdot 1^2 \cdot x = \frac{1}{2} x$,
- Pole trójkąta zewnętrznego: $P_3 = \frac{1}{2} \cdot 1 \cdot \operatorname{tg} x = \frac{1}{2} \frac{\sin x}{\cos x}$.

Ponieważ $P_1 < P_2 < P_3$, otrzymujemy:
$$\sin x < x < \frac{\sin x}{\cos x}$$
Dzieląc przez $\sin x > 0$:
$$1 < \frac{x}{\sin x} < \frac{1}{\cos x} \implies \cos x < \frac{\sin x}{x} < 1$$
Ponieważ funkcja $\cos x$ jest parzysta, nierówność ta zachodzi również dla $x \in \left(-\frac{\pi}{2}, 0\right)$.  
Mamy $\lim_{x \to 0} \cos x = 1$ oraz $\lim_{x \to 0} 1 = 1$. Z twierdzenia o trzech funkcjach wynika teza:
$$\lim_{x \to 0} \frac{\sin x}{x} = 1 \quad \blacksquare$$

---

## Rozdział 8: Ciągłość funkcji

### 8.1. Definicja ciągłości i klasyfikacja punktów nieciągłości

#### Definicja 8.1 (Ciągłość funkcji w punkcie)
Niech $f: X \to \mathbb{R}$ oraz $x_0 \in X$ będzie punktem skupienia zbioru $X$.  
Mówimy, że funkcja $f$ jest **ciągła w punkcie $x_0$**, jeżeli:
$$\lim_{x \to x_0} f(x) = f(x_0)$$
Równoważnie w języku $\varepsilon-\delta$:
$$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x \in X} \quad (|x - x_0| < \delta \implies |f(x) - f(x_0)| < \varepsilon)$$

Funkcję nazywamy ciągłą na zbiorze $A \subset X$, jeżeli jest ciągła w każdym punkcie zbioru $A$.

#### Klasyfikacja punktów nieciągłości
Jeżeli funkcja $f$ jest określona w otoczeniu punktu $x_0$ (lub w jego sąsiedztwie), lecz nie jest w nim ciągła, punkt $x_0$ nazywamy **punktem nieciągłości**:
1. **Nieciągłość I rodzaju (zwykła):** Istnieją skończone granice jednostronne $f(x_0^-)$ oraz $f(x_0^+)$.
   - **Nieciągłość usuwalna:** $f(x_0^-) = f(x_0^+) \neq f(x_0)$ (lub $f(x_0)$ nie jest określona). Wystarczy przedefiniować wartość funkcji w punkcie $x_0$, aby stała się ciągła.
   - **Nieciągłość skokowa (skok funkcji):** $f(x_0^-) \neq f(x_0^+)$. Wielkość $s = f(x_0^+) - f(x_0^-)$ nazywamy skokiem funkcji (np. funkcja skoku jednostkowego Heaviside'a $H(t)$).
2. **Nieciągłość II rodzaju:** Przynajmniej jedna z granic jednostronnych jest nieskończona ($\pm\infty$) lub w ogóle nie istnieje (np. $f(x) = \sin(1/x)$ w $x_0 = 0$).

---

### 8.2. Własności funkcji ciągłych na przedziale domkniętym $[a, b]$

Funkcje ciągłe na przedziale domkniętym i ograniczonym (zbiorze zwartym) posiadają wyjątkowe własności, które są kluczowe w algorytmach numerycznych i teorii optymalizacji.

> **Twierdzenie 8.1 (Weierstrassa o osiąganiu kresów):**
> Jeżeli funkcja $f: [a, b] \to \mathbb{R}$ jest ciągła na przedziale domkniętym $[a, b]$, to:
> 1. jest ograniczona: $\exists_{m, M \in \mathbb{R}} \forall_{x \in [a, b]} \ m \le f(x) \le M$,
> 2. osiąga swoje kresy: istnieją punkty $x_{\min}, x_{\max} \in [a, b]$ takie, że:
>    $$f(x_{\min}) = \inf_{x \in [a, b]} f(x) = \min_{x \in [a, b]} f(x)$$
>    $$f(x_{\max}) = \sup_{x \in [a, b]} f(x) = \max_{x \in [a, b]} f(x)$$

> **Twierdzenie 8.2 (Bolzano-Cauchy'ego o wartościach pośrednich / Własność Darboux):**
> Jeżeli funkcja $f: [a, b] \to \mathbb{R}$ jest ciągła oraz $f(a) \neq f(b)$, to dla dowolnej liczby $w$ leżącej pomiędzy $f(a)$ i $f(b)$ istnieje co najmniej jeden punkt $c \in (a, b)$ taki, że:
> $$f(c) = w$$

#### Wniosek (Lokalizacja pierwiastków równań / Metoda Bisekcji):
Jeżeli funkcja ciągła spełnia na końcach przedziału warunek różnych znaków:
$$f(a) \cdot f(b) < 0$$
to wewnątrz przedziału $(a, b)$ istnieje co najmniej jedno rozwiązanie równania $f(x) = 0$.  
Jest to podstawa informatycznego algorytmu podziału binarnego (bisekcji), w którym dzieląc przedział na połowy, lokalizuje się zera funkcji z dokładnością $\mathcal{O}(2^{-n})$.

---

### 8.3. Ciągłość jednostajna i twierdzenie Cantora

W klasycznej definicji ciągłości promień $\delta = \delta(\varepsilon, x_0)$ zależy nie tylko od zadanego $\varepsilon$, lecz również od wybranego punktu $x_0$.

#### Definicja 8.2 (Ciągłość jednostajna)
Funkcję $f: X \to \mathbb{R}$ nazywamy **jednostajnie ciągłą** na zbiorze $X$, jeżeli promień $\delta$ można dobrać wspólnie dla wszystkich punktów dziedziny:
$$\forall_{\varepsilon > 0} \exists_{\delta > 0} \forall_{x_1, x_2 \in X} \quad (|x_1 - x_2| < \delta \implies |f(x_1) - f(x_2)| < \varepsilon)$$

> **Twierdzenie 8.3 (Cantora o ciągłości jednostajnej):**
> Każda funkcja ciągła na przedziale domkniętym $[a, b]$ jest na nim jednostajnie ciągła.

---

### 8.4. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 4.1: Obliczanie granicy z funkcją trygonometryczną
Oblicz granicę:
$$\lim_{x \to 0} \frac{1 - \cos(4x)}{x \sin(3x)}$$

**Rozwiązanie:**
Mamy symbol nieoznaczony $\left[\frac{0}{0}\right]$.  
Stosujemy tożsamość trygonometryczną: $1 - \cos(2\alpha) = 2\sin^2\alpha$, stąd dla $\alpha = 2x$:
$$1 - \cos(4x) = 2\sin^2(2x)$$
Przekształcamy wyrażenie tak, aby wyodrębnić bazowe granice typu $\frac{\sin u}{u}$:
$$\frac{2\sin^2(2x)}{x \sin(3x)} = 2 \cdot \frac{\sin^2(2x)}{(2x)^2} \cdot (2x)^2 \cdot \frac{1}{x \sin(3x)} = 2 \cdot \left(\frac{\sin(2x)}{2x}\right)^2 \cdot 4x^2 \cdot \frac{3x}{\sin(3x)} \cdot \frac{1}{3x^2}$$
Upraszczamy $x^2$:
$$= 2 \cdot \left(\frac{\sin(2x)}{2x}\right)^2 \cdot \frac{3x}{\sin(3x)} \cdot \frac{4}{3}$$
Przechodząc do granicy przy $x \to 0$:
$$\lim_{x \to 0} \frac{\sin(2x)}{2x} = 1, \quad \lim_{x \to 0} \frac{3x}{\sin(3x)} = 1$$
Ostatecznie:
$$\lim_{x \to 0} \frac{1 - \cos(4x)}{x \sin(3x)} = 2 \cdot 1^2 \cdot 1 \cdot \frac{4}{3} = \frac{8}{3}$$

---

#### Przykład 4.2: Dobór parametrów ciągłości funkcji (zadanie egzaminacyjne WEiTI)
Dla jakich wartości parametrów $a, b \in \mathbb{R}$ funkcja:
$$f(x) = \begin{cases}
\frac{\ln(1 + 3x)}{x} & \text{dla } x < 0 \\
a x + b & \text{dla } 0 \le x \le 2 \\
\frac{x^2 - 4}{x - 2} & \text{dla } x > 2
\end{cases}$$
jest ciągła na całym zbiorze $\mathbb{R}$?

**Rozwiązanie:**
Funkcja wewnątrz poszczególnych przedziałów jest ciągła jako ilorazy i sumy funkcji elementarnych.  
Warunkiem ciągłości na $\mathbb{R}$ jest ciągłość w punktach łączenia: $x_0 = 0$ oraz $x_1 = 2$.

1. **Ciągłość w punkcie $x_0 = 0$:**
   - Wartość funkcji: $f(0) = a \cdot 0 + b = b$.
   - Granica prawostronna: $\lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} (ax + b) = b$.
   - Granica lewostronna:
     $$\lim_{x \to 0^-} \frac{\ln(1 + 3x)}{x} = \lim_{x \to 0^-} 3 \cdot \frac{\ln(1 + 3x)}{3x} = 3 \cdot 1 = 3$$
   Warunek ciągłości $f(0^-) = f(0^+) = f(0)$ daje:
   $$b = 3$$

2. **Ciągłość w punkcie $x_1 = 2$:**
   - Wartość funkcji: $f(2) = a \cdot 2 + b = 2a + 3$.
   - Granica lewostronna: $\lim_{x \to 2^-} f(x) = 2a + 3$.
   - Granica prawostronna:
     $$\lim_{x \to 2^+} \frac{x^2 - 4}{x - 2} = \lim_{x \to 2^+} \frac{(x-2)(x+2)}{x-2} = \lim_{x \to 2^+} (x + 2) = 4$$
   Warunek ciągłości $f(2^-) = f(2^+)$ daje:
   $$2a + 3 = 4 \implies 2a = 1 \implies a = \frac{1}{2}$$

**Odpowiedź:** Funkcja jest ciągła na $\mathbb{R}$ dla $a = \frac{1}{2}$ oraz $b = 3$.

---

### 8.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 4.1:** Oblicz granicę: $\lim_{x \to 0} \frac{\operatorname{tg}(5x)}{\arcsin(2x)}$.
2. **Zadanie 4.2:** Oblicz granicę: $\lim_{x \to 0} (1 + 2x)^{1/\sin x}$.
3. **Zadanie 4.3:** Określ rodzaj punktu nieciągłości funkcji $f(x) = \frac{x}{|x|} e^{-1/x^2}$ w punkcie $x_0 = 0$.
4. **Zadanie 4.4:** Wykaż za pomocą twierdzenia Darboux, że równanie $x^5 - 3x - 1 = 0$ ma co najmniej jeden pierwiastek w przedziale $(1, 2)$.
5. **Zadanie 4.5:** Zbadaj jednostajną ciągłość funkcji $f(x) = \sqrt{x}$ na przedziale $[0, +\infty)$.

---

### Odpowiedzi i wskazówki do zadań

- **4.1:** $\lim_{x \to 0} \frac{\operatorname{tg}(5x)/5x \cdot 5x}{\arcsin(2x)/2x \cdot 2x} = \frac{5}{2}$.
- **4.2:** $(1+2x)^{1/\sin x} = \exp\left( \frac{\ln(1+2x)}{\sin x} \right) = \exp\left( \frac{2x}{\sin x} \cdot \frac{\ln(1+2x)}{2x} \right) \xrightarrow[x \to 0]{} e^2$.
- **4.3:** Granica lewostronna: $\lim_{x \to 0^-} (-1) \cdot e^{-\infty} = 0$. Granica prawostronna: $\lim_{x \to 0^+} (+1) \cdot e^{-\infty} = 0$. Ponieważ obie granice jednostronne są równe 0, ale $f(0)$ nie jest zdefiniowana, jest to **nieciągłość I rodzaju usuwalna** (kładąc $f(0) = 0$ uzyskujemy funkcję ciągłą).
- **4.4:** Funkcja $W(x) = x^5 - 3x - 1$ jest ciągła. $W(1) = 1 - 3 - 1 = -3 < 0$, $W(2) = 32 - 6 - 1 = 25 > 0$. Na mocy Twierdzenia Bolzano-Cauchy'ego istnieje $c \in (1, 2)$ takie, że $W(c) = 0$.
- **4.5:** Jest jednostajnie ciągła. Na $[0, 1]$ z twierdzenia Cantora; dla $x, y \ge 1$: $|\sqrt{x} - \sqrt{y}| = \frac{|x-y|}{\sqrt{x}+\sqrt{y}} \le \frac{1}{2}|x-y|$ (spełnia warunek Lipschitza).


\newpage

# Część V: Rachunek Różniczkowy Funkcji Jednej Zmiennej

Rachunek różniczkowy jest jednym z najpotężniejszych narzędzi matematyki stosowanej. Pozwala badać tempo zmian wielkości fizycznych, aproksymować zjawiska nieliniowe za pomocą prostych modeli liniowych oraz optymalizować parametry układów. W inżynierii informatycznej i elektronicznej pochodna leży u podstaw uczenia maszynowego (algorytmy spadku gradientowego), przetwarzania sygnałów oraz analizy obwodów nieliniowych.

---

## Rozdział 9: Pochodna i różniczka funkcji

### 9.1. Definicja pochodnej i interpretacja fizyczno-geometryczna

Niech funkcja $f: X \to \mathbb{R}$ będzie określona w otoczeniu punktu $x_0 \in X$.

#### Definicja 9.1 (Iloraz różnicowy i pochodna w punkcie)
1. **Ilorazem różnicowym** funkcji $f$ odpowiadającym przyrostowi argumentu $\Delta x \neq 0$ nazywamy wyrażenie:
   $$\frac{\Delta f}{\Delta x} = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$
2. Jeżeli istnieje granica właściwa ilorazu różnicowego przy $\Delta x \to 0$, to granicę tę nazywamy **pochodną właściwą funkcji $f$ w punkcie $x_0$** i oznaczamy $f'(x_0)$ lub $\frac{df}{dx}(x_0)$:
   $$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

Funkcję posiadającą skończoną pochodną w punkcie $x_0$ nazywamy **różniczkowalną w punkcie $x_0$**.

#### Interpretacje pochodnej:
1. **Interpretacja geometryczna:**  
   Pochodna $f'(x_0)$ jest tangensem kąta nachylenia prostej stycznej do wykresu funkcji $y = f(x)$ w punkcie $P_0(x_0, f(x_0))$ względem dodatniej półosi $OX$:
   $$m = \operatorname{tg} \alpha = f'(x_0)$$
   Równanie prostej **stycznej**:
   $$y - f(x_0) = f'(x_0)(x - x_0)$$
   Równanie prostej **normalnej** (prostopadłej do stycznej, o ile $f'(x_0) \neq 0$):
   $$y - f(x_0) = -\frac{1}{f'(x_0)}(x - x_0)$$

2. **Interpretacja fizyczna (Elektrotechnika i Teoria Sygnałów):**  
   - Jeżeli $q(t)$ oznacza ładunek elektryczny przepływający przez poprzeczny przekrój przewodnika w czasie $t$, to natężenie prądu elektrycznego jest pochodną ładunku:
     $$i(t) = \frac{dq(t)}{dt}$$
   - Napięcie na cewce indukcyjnej o indukcyjności $L$ jest proporcjonalne do szybkości zmian natężenia prądu:
     $$u_L(t) = L \frac{di(t)}{dt}$$
   - Prąd płynący przez kondensator o pojemności $C$ jest proporcjonalny do pochodnej napięcia:
     $$i_C(t) = C \frac{du_C(t)}{dt}$$

---

### 9.2. Ciągłość a różniczkowalność

> **Twierdzenie 9.1 (O ciągłości funkcji różniczkowalnej):**
> Jeżeli funkcja $f$ jest różniczkowalna w punkcie $x_0$, to jest w tym punkcie ciągła.

**Dowód:**
Dla $x \neq x_0$ możemy zapisać tożsamość:
$$f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0} \cdot (x - x_0)$$
Przechodząc do granicy przy $x \to x_0$:
$$\lim_{x \to x_0} \big( f(x) - f(x_0) \big) = \lim_{x \to x_0} \left[ \frac{f(x) - f(x_0)}{x - x_0} \right] \cdot \lim_{x \to x_0} (x - x_0) = f'(x_0) \cdot 0 = 0$$
Stąd $\lim_{x \to x_0} f(x) = f(x_0)$, co oznacza ciągłość funkcji w punkcie $x_0$. $\blacksquare$

> **Uwaga krytyczna:** Twierdzenie odwrotne nie jest prawdziwe!  
> Funkcja $f(x) = |x|$ jest ciągła w punkcie $x_0 = 0$, lecz nie jest w nim różniczkowalna, gdyż jej pochodne jednostronne są różne:
> $$f'_-(0) = \lim_{x \to 0^-} \frac{|x| - 0}{x} = -1 \neq f'_+(0) = \lim_{x \to 0^+} \frac{|x| - 0}{x} = +1$$

---

### 9.3. Podstawowe reguły różniczkowania

> **Twierdzenie 9.2:**
> Jeżeli funkcje $f$ i $g$ są różniczkowalne w punkcie $x$, to:
> 1. **Liniowość:** $(\alpha f + \beta g)'(x) = \alpha f'(x) + \beta g'(x) \quad (\alpha, \beta \in \mathbb{R})$
> 2. **Iloczyn:** $(f \cdot g)'(x) = f'(x)g(x) + f(x)g'(x)$
> 3. **Iloraz:** $\left( \frac{f}{g} \right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2} \quad (g(x) \neq 0)$
> 4. **Złożenie (reguła łańcuchowa):** $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$
> 5. **Funkcja odwrotna:** $(f^{-1})'(y_0) = \frac{1}{f'(x_0)}$, gdzie $y_0 = f(x_0)$ oraz $f'(x_0) \neq 0$

#### Wzór Leibniza na $n$-tą pochodną iloczynu
Dla funkcji wielokrotnie różniczkowalnych:
$$(f \cdot g)^{(n)}(x) = \sum_{k=0}^n \binom{n}{k} f^{(k)}(x) g^{(n-k)}(x)$$

---

### 9.4. Różniczka funkcji i jej zastosowania inżynierskie

#### Definicja 9.2 (Różniczka funkcji)
Jeżeli funkcja $f$ jest różniczkowalna w punkcie $x_0$, to wyrażenie:
$$df(x_0, \Delta x) = f'(x_0) \cdot \Delta x$$
liniowe względem przyrostu $\Delta x = dx$, nazywamy **różniczką funkcji $f$ w punkcie $x_0$** i zapisujemy $df = f'(x) dx$.

Przyrost rzeczywisty funkcji wynosi:
$$\Delta f = f(x_0 + \Delta x) - f(x_0) = f'(x_0)\Delta x + \alpha(\Delta x)\cdot \Delta x$$
gdzie $\lim_{\Delta x \to 0} \alpha(\Delta x) = 0$. Różniczka $df$ jest więc **częścią główną przyrostu funkcji**, co pozwala na linearyzację:
$$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0) \Delta x$$

#### Zastosowanie: Linearyzacja w punkcie pracy (Elektronika)
Nieliniowy element półprzewodnikowy (np. złącze p-n diody) opisuje równanie Shockleya:
$$I_D = I_S \left( e^{\frac{U_D}{n V_T}} - 1 \right)$$
W punkcie pracy stałoprądowej $Q(U_{D0}, I_{D0})$, dla małych przyrostów sygnału zmiennego $u_d(t)$, linearyzujemy charakterystykę za pomocą różniczki:
$$i_d(t) \approx \left. \frac{dI_D}{dU_D} \right|_{Q} \cdot u_d(t) = g_d \cdot u_d(t)$$
Wielkość $g_d = \frac{1}{r_d} = \frac{I_{D0} + I_S}{n V_T}$ jest **konduktancją dynamiczną** diody. W ten sposób złożony nieliniowy obwód sprowadza się do prostego obwodu liniowego dla małych sygnałów.

---

## Rozdział 10: Twierdzenia o wartości średniej i wzór Taylora

### 10.1. Twierdzenia Rolle'a, Lagrange'a i Cauchy'ego

> **Lemat Fermata (Warunek konieczny istnienia ekstremum lokalnego):**
> Jeżeli funkcja $f$ osiąga w punkcie wewnętrznym $x_0$ ekstremum lokalne i jest w tym punkcie różniczkowalna, to:
> $$f'(x_0) = 0$$

> **Twierdzenie 10.1 (Rolle'a):**
> Jeżeli funkcja $f$ spełnia warunki:
> 1. jest ciągła w przedziale domkniętym $[a, b]$,
> 2. jest różniczkowalna w przedziale otwartym $(a, b)$,
> 3. $f(a) = f(b)$,
> to istnieje co najmniej jeden punkt $c \in (a, b)$ taki, że:
> $$f'(c) = 0$$

> **Twierdzenie 10.2 (Lagrange'a o wartości średniej):**
> Jeżeli funkcja $f$ jest ciągła w $[a, b]$ i różniczkowalna w $(a, b)$, to istnieje punkt $c \in (a, b)$ taki, że:
> $$\frac{f(b) - f(a)}{b - a} = f'(c) \iff f(b) - f(a) = f'(c)(b - a)$$

#### Fundamentalne wnioski z twierdzenia Lagrange'a:
1. Jeżeli $f'(x) = 0$ dla każdego $x \in (a, b)$, to funkcja $f$ jest stała na $(a, b)$.
2. Jeżeli $f'(x) > 0$ dla każdego $x \in (a, b)$, to funkcja $f$ jest ściśle rosnąca na tym przedziale.
3. Jeżeli $f'(x) < 0$ dla każdego $x \in (a, b)$, to funkcja $f$ jest ściśle malejąca na tym przedziale.

---

### 10.2. Reguła de l'Hospitala

Do wyznaczania granic wyrażeń nieoznaczonych postaci $\left[\frac{0}{0}\right]$ oraz $\left[\frac{\infty}{\infty}\right]$ służy twierdzenie Johanna Bernoulliego, powszechnie zwane regułą de l'Hospitala:

> **Twierdzenie 10.3 (Reguła de l'Hospitala):**
> Niech funkcje $f$ i $g$ będą różniczkowalne w sąsiedztwie punktu $x_0$ (właściwego lub niewłaściwego $\pm\infty$), przy czym $g'(x) \neq 0$.  
> Jeżeli:
> $$\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0 \quad \text{lub} \quad \lim_{x \to x_0} |g(x)| = +\infty$$
> oraz istnieje granica ilorazu pochodnych (właściwa lub niewłaściwa):
> $$\lim_{x \to x_0} \frac{f'(x)}{g'(x)} = K$$
> to istnieje również granica wyjściowa i zachodzi równość:
> $$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{f'(x)}{g'(x)} = K$$

---

### 10.3. Wzór Taylora i Maclaurina

Wzór Taylora stanowi uogólnienie twierdzenia o wartości średniej i pozwala przybliżać dowolną funkcję gładką za pomocą wielomianu.

> **Twierdzenie 10.4 (Wzór Taylora z resztą Lagrange'a):**
> Jeżeli funkcja $f$ ma ciągłe pochodne do rzędu $n$ w przedziale domkniętym o końcach $x_0, x$ oraz pochodną rzędu $(n+1)$ wewnątrz tego przedziału, to:
> $$f(x) = f(x_0) + \frac{f'(x_0)}{1!}(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \dots + \frac{f^{(n)}(x_0)}{n!}(x - x_0)^n + R_n(x)$$
> gdzie reszta w postaci Lagrange'a wynosi:
> $$R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!} (x - x_0)^{n+1}, \quad c \in (x_0, x)$$
> lub w postaci Peano (z użyciem symbolu Landaua $o$):
> $$R_n(x) = o\big((x - x_0)^n\big) \quad \text{przy } x \to x_0$$

Dla $x_0 = 0$ wzór Taylora nazywamy **wzorem Maclaurina**:
$$f(x) = \sum_{k=0}^n \frac{f^{(k)}(0)}{k!} x^k + R_n(x)$$

#### Podstawowe rozwinięcia Maclaurina:
1. $$e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^n}{n!} + o(x^n)$$
2. $$\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots + (-1)^k \frac{x^{2k+1}}{(2k+1)!} + o(x^{2k+2})$$
3. $$\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots + (-1)^k \frac{x^{2k}}{(2k)!} + o(x^{2k+1})$$
4. $$\ln(1 + x) = x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots + (-1)^{n-1}\frac{x^n}{n} + o(x^n)$$
5. $$(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!} x^2 + \dots + \binom{\alpha}{n} x^n + o(x^n)$$

---

## Rozdział 11: Badanie przebiegu zmienności funkcji

### 11.1. Ekstrema lokalne i kryteria ich istnienia

#### Warunki dostateczne istnienia ekstremum:
1. **Kryterium I pochodnej:** Jeżeli $f'(x_0) = 0$ oraz pochodna $f'(x)$ zmienia znak przy przejściu przez punkt $x_0$:
   - z $+$ na $-$ $\implies$ w punkcie $x_0$ funkcja osiąga **maksimum lokalne**,
   - z $-$ na $+$ $\implies$ w punkcie $x_0$ funkcja osiąga **minimum lokalne**.
2. **Kryterium II pochodnej:** Niech $f'(x_0) = 0$ oraz istnieje $f''(x_0)$:
   - jeżeli $f''(x_0) < 0$, to w $x_0$ jest **maksimum lokalne właściwe**,
   - jeżeli $f''(x_0) > 0$, to w $x_0$ jest **minimum lokalne właściwe**,
   - jeżeli $f''(x_0) = 0$, kryterium nie rozstrzyga (należy badać wyższe pochodne).

---

### 11.2. Wypukłość, wklęsłość i punkty przegięcia

1. **Wypukłość (wypukłość ku dołowi):** Wykres funkcji leży ponad dowolną swoją styczną.  
   Warunek dostateczny: $f''(x) > 0$ na przedziale.
2. **Wklęsłość (wypukłość ku górze):** Wykres leży pod dowolną swoją styczną.  
   Warunek dostateczny: $f''(x) < 0$ na przedziale.
3. **Punkt przegięcia:** Punkt $(x_0, f(x_0))$, w którym funkcja zmienia charakter z wypukłej na wklęsłą (lub odwrotnie).  
   Warunek konieczny: $f''(x_0) = 0$ (lub $f''(x_0)$ nie istnieje). Warunek dostateczny: zmiana znaku $f''(x)$ w otoczeniu $x_0$.

---

### 11.3. Asymptoty wykresu funkcji

1. **Asymptota pionowa:** Prosta $x = x_0$ jest asymptotą pionową (lewostronną, prawostronną lub obustronną), jeżeli:
   $$\lim_{x \to x_0^{\pm}} f(x) = \pm\infty$$
2. **Asymptota ukośna:** Prosta $y = ax + b$ jest asymptotą ukośną przy $x \to +\infty$ (odpowiednio $-\infty$), jeżeli $\lim_{x \to \pm\infty} [f(x) - (ax + b)] = 0$.  
   Współczynniki wyznacza się ze wzorów:
   $$a = \lim_{x \to \pm\infty} \frac{f(x)}{x}$$
   $$b = \lim_{x \to \pm\infty} \big( f(x) - ax \big)$$
   *(Gdy $a = 0$, asymptota jest asymptotą poziomą: $y = b$).*

---

### 11.4. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 5.1: Reguła de l'Hospitala dla symbolu $[0 \cdot \infty]$ i $[1^\infty]$
Oblicz granicę:
$$\lim_{x \to 0^+} x^{\sin x}$$

**Rozwiązanie:**
Mamy symbol nieoznaczony $\left[0^0\right]$. Stosujemy tożsamość wykładniczą:
$$x^{\sin x} = \exp\big( \sin x \cdot \ln x \big)$$
Badamy granicę wykładnika przy $x \to 0^+$, która jest symbolem $[0 \cdot (-\infty)]$:
$$\lim_{x \to 0^+} (\sin x \cdot \ln x) = \lim_{x \to 0^+} \frac{\ln x}{\frac{1}{\sin x}} = \left[ \frac{-\infty}{+\infty} \right]$$
Stosujemy regułę de l'Hospitala:
$$\lim_{x \to 0^+} \frac{(\ln x)'}{\left( \frac{1}{\sin x} \right)'} = \lim_{x \to 0^+} \frac{\frac{1}{x}}{-\frac{\cos x}{\sin^2 x}} = -\lim_{x \to 0^+} \frac{\sin^2 x}{x \cos x} = -\lim_{x \to 0^+} \left( \frac{\sin x}{x} \cdot \frac{\sin x}{\cos x} \right) = -(1 \cdot 0) = 0$$
Z ciągłości funkcji wykładniczej:
$$\lim_{x \to 0^+} x^{\sin x} = e^0 = 1$$

---

#### Przykład 5.2: Pełne badanie przebiegu zmienności funkcji
Przeprowadź badanie zmienności funkcji:
$$f(x) = \frac{x^2}{x - 1}$$

**Rozwiązanie:**
1. **Dziedzina i punkty osobliwe:** $D_f = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, +\infty)$.
2. **Miejsca zerowe:** $f(x) = 0 \iff x^2 = 0 \implies x = 0$. Punkt przecięcia z osiami: $(0, 0)$.
3. **Asymptoty:**
   - Asymptota pionowa w $x = 1$:
     $$\lim_{x \to 1^-} \frac{x^2}{x-1} = \left[\frac{1}{0^-}\right] = -\infty, \quad \lim_{x \to 1^+} \frac{x^2}{x-1} = \left[\frac{1}{0^+}\right] = +\infty$$
     Prosta $x = 1$ jest obustronną asymptotą pionową.
   - Asymptoty ukośne $y = ax + b$:
     $$a = \lim_{x \to \pm\infty} \frac{f(x)}{x} = \lim_{x \to \pm\infty} \frac{x}{x - 1} = 1$$
     $$b = \lim_{x \to \pm\infty} \big( f(x) - ax \big) = \lim_{x \to \pm\infty} \left( \frac{x^2}{x - 1} - x \right) = \lim_{x \to \pm\infty} \frac{x^2 - x^2 + x}{x - 1} = \lim_{x \to \pm\infty} \frac{x}{x - 1} = 1$$
     Prosta $y = x + 1$ jest asymptotą ukośną obustronną (przy $x \to +\infty$ oraz $x \to -\infty$).
4. **Pierwsza pochodna i ekstrema:**
   $$f'(x) = \frac{2x(x - 1) - x^2 \cdot 1}{(x - 1)^2} = \frac{2x^2 - 2x - x^2}{(x - 1)^2} = \frac{x^2 - 2x}{(x - 1)^2} = \frac{x(x - 2)}{(x - 1)^2}$$
   Mianownik jest ściśle dodatni dla $x \neq 1$. O znaku $f'$ decyduje licznik $x(x - 2)$:
   - $f'(x) = 0 \iff x = 0 \lor x = 2$ (punkty stacjonarne),
   - $f'(x) > 0$ dla $x \in (-\infty, 0) \cup (2, +\infty)$ (funkcja rosnąca),
   - $f'(x) < 0$ dla $x \in (0, 1) \cup (1, 2)$ (funkcja malejąca).
   W punkcie $x = 0$ pochodna zmienia znak z $+$ na $-$: **maksimum lokalne** $f(0) = 0$.  
   W punkcie $x = 2$ pochodna zmienia znak z $-$ na $+$: **minimum lokalne** $f(2) = \frac{4}{1} = 4$.
5. **Druga pochodna i wypukłość:**
   $$f''(x) = \frac{(2x - 2)(x - 1)^2 - (x^2 - 2x) \cdot 2(x - 1)}{(x - 1)^4} = \frac{2(x - 1)[(x - 1)^2 - (x^2 - 2x)]}{(x - 1)^4} = \frac{2(x^2 - 2x + 1 - x^2 + 2x)}{(x - 1)^3} = \frac{2}{(x - 1)^3}$$
   - dla $x > 1$: $f''(x) > 0 \implies$ funkcja jest **wypukła** ku dołowi,
   - dla $x < 1$: $f''(x) < 0 \implies$ funkcja jest **wklęsła** ku górze.  
   Brak punktów przegięcia (w punkcie $x = 1$ funkcja nie jest określona).

---

### 11.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 5.1:** Oblicz pochodną funkcji $f(x) = \ln\left( \frac{1 + \sin x}{1 - \sin x} \right)$ i doprowadź wynik do najprostszej postaci.
2. **Zadanie 5.2:** Wyznacz równanie prostej stycznej do krzywej $y = \operatorname{arctg}(2x)$ w punkcie o odciętej $x_0 = \frac{1}{2}$.
3. **Zadanie 5.3:** Oblicz granicę: $\lim_{x \to 0} \frac{e^x - 1 - x - \frac{x^2}{2}}{x^3}$ za pomocą wzoru Maclaurina.
4. **Zadanie 5.4 (Teoria obwodów - dopasowanie mocy):** Źródło napięcia stałego o sile elektromotorycznej $E$ i oporze wewnętrznym $R_w$ zasila odbiornik o rezystancji $R$. Wykaż, że moc wydzielana na odbiorniku $P(R) = I^2 R = \left( \frac{E}{R + R_w} \right)^2 R$ osiąga maksimum, gdy $R = R_w$ (warunek dopasowania energetycznego), oraz oblicz tę moc maksymalną.
5. **Zadanie 5.5:** Wyznacz wszystkie asymptoty wykresu funkcji $f(x) = x \cdot e^{1/x}$.

---

### Odpowiedzi i wskazówki do zadań

- **5.1:** $f(x) = \ln(1+\sin x) - \ln(1-\sin x) \implies f'(x) = \frac{\cos x}{1+\sin x} - \frac{-\cos x}{1-\sin x} = \cos x \left( \frac{1-\sin x + 1+\sin x}{1-\sin^2 x} \right) = \cos x \cdot \frac{2}{\cos^2 x} = \frac{2}{\cos x}$.
- **5.2:** $y_0 = f(1/2) = \operatorname{arctg}(1) = \frac{\pi}{4}$. Pochodna: $f'(x) = \frac{2}{1+4x^2} \implies f'(1/2) = \frac{2}{1+1} = 1$. Równanie stycznej: $y - \frac{\pi}{4} = 1\left(x - \frac{1}{2}\right) \implies y = x - \frac{1}{2} + \frac{\pi}{4}$.
- **5.3:** Rozwinięcie Maclaurina: $e^x = 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + o(x^3) \implies e^x - 1 - x - \frac{x^2}{2} = \frac{x^3}{6} + o(x^3)$. Dzieląc przez $x^3$, granica wynosi $\frac{1}{6}$.
- **5.4:** Obliczamy pochodną po $R$: $P'(R) = E^2 \cdot \frac{1 \cdot (R+R_w)^2 - R \cdot 2(R+R_w)}{(R+R_w)^4} = E^2 \frac{R_w - R}{(R+R_w)^3}$. Pochodna zeruje się dla $R = R_w$ i zmienia znak z $+$ na $-$. Zatem maksimum występuje dla $R = R_w$, a moc maksymalna wynosi $P_{\max} = \frac{E^2}{4R_w}$.
- **5.5:** Dziedzina $D = \mathbb{R} \setminus \{0\}$. Asymptota pionowa w $x = 0$: $\lim_{x \to 0^+} x e^{1/x} = \lim_{t \to \infty} \frac{e^t}{t} = +\infty$ (asymptota pionowa prawostronna); $\lim_{x \to 0^-} x e^{1/x} = 0 \cdot 0 = 0$. Asymptota ukośna $y = ax + b$: $a = \lim_{x \to \pm\infty} e^{1/x} = 1$; $b = \lim_{x \to \pm\infty} x(e^{1/x} - 1) = \lim_{t \to 0} \frac{e^t - 1}{t} = 1$. Prosta $y = x + 1$ jest asymptotą ukośną obustronną.


\newpage

# Część VI: Całka Nieoznaczona

Rachunek całkowy stanowi naturalne odwrócenie operacji różniczkowania. O ile wyznaczanie pochodnej funkcji elementarnej jest procedurą algorytmiczną, o tyle całkowanie wymaga znajomości szerokiego wachlarza technik analitycznych i przekształceń algebraicznych. W inżynierii funkcja pierwotna pojawia się wszędzie tam, gdzie z prawa opisującego dynamikę zmian (równania różniczkowego) odtwarzamy stan układu, napięcie, ładunek lub energię.

---

## Rozdział 12: Funkcja pierwotna i podstawowe metody całkowania

### 12.1. Pojęcie funkcji pierwotnej i całki nieoznaczonej

#### Definicja 12.1 (Funkcja pierwotna)
Niech funkcja $f: (a, b) \to \mathbb{R}$ będzie określona w przedziale otwartym $(a, b)$.  
Funkcję $F: (a, b) \to \mathbb{R}$ nazywamy **funkcją pierwotną** funkcji $f$ w przedziale $(a, b)$, jeżeli dla każdego $x \in (a, b)$ funkcja $F$ jest różniczkowalna oraz:
$$F'(x) = f(x)$$

> **Twierdzenie 12.1 (O jednoznaczności funkcji pierwotnej):**
> Jeżeli $F(x)$ jest funkcją pierwotną funkcji $f(x)$ w przedziale $(a, b)$, to każda inna funkcja pierwotna $\Phi(x)$ funkcji $f(x)$ w tym przedziale ma postać:
> $$\Phi(x) = F(x) + C, \quad C \in \mathbb{R}$$

**Dowód:**
Zauważmy, że $(\Phi(x) - F(x))' = \Phi'(x) - F'(x) = f(x) - f(x) = 0$ dla każdego $x \in (a, b)$.  
Z wniosku z twierdzenia Lagrange'a o wartości średniej (Tw. 10.2), funkcja o tożsamościowo zerowej pochodnej w przedziale jest funkcją stałą:
$$\Phi(x) - F(x) = C \implies \Phi(x) = F(x) + C \quad \blacksquare$$

#### Definicja 12.2 (Całka nieoznaczona)
Zbiór wszystkich funkcji pierwotnych funkcji $f(x)$ w przedziale $(a, b)$ nazywamy **całką nieoznaczoną** i zapisujemy symbolem:
$$\int f(x) \, dx = F(x) + C, \quad C \in \mathbb{R}$$

#### Podstawowe własności całki nieoznaczonej:
1. **Liniowość:**
   $$\int \big( \alpha f(x) + \beta g(x) \big) \, dx = \alpha \int f(x) \, dx + \beta \int g(x) \, dx \quad (\alpha, \beta \in \mathbb{R})$$
2. **Różniczkowanie całki:**
   $$\frac{d}{dx} \left( \int f(x) \, dx \right) = f(x)$$
3. **Całkowanie różniczki:**
   $$\int dF(x) = \int F'(x) \, dx = F(x) + C$$

---

### 12.2. Tablica podstawowych całek elementarnych

| Funkcja $f(x)$ | Całka $\int f(x)\,dx$ | Założenia |
| :--- | :--- | :--- |
| $x^n$ | $\frac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\frac{1}{x}$ | $\ln|x| + C$ | $x \neq 0$ |
| $e^x$ | $e^x + C$ | |
| $a^x$ | $\frac{a^x}{\ln a} + C$ | $a > 0, a \neq 1$ |
| $\sin x$ | $-\cos x + C$ | |
| $\cos x$ | $\sin x + C$ | |
| $\frac{1}{\cos^2 x}$ | $\operatorname{tg} x + C$ | $x \neq \frac{\pi}{2} + k\pi$ |
| $\frac{1}{\sin^2 x}$ | $-\operatorname{ctg} x + C$ | $x \neq k\pi$ |
| $\frac{1}{1 + x^2}$ | $\operatorname{arctg} x + C$ | |
| $\frac{1}{\sqrt{1 - x^2}}$ | $\arcsin x + C$ | $x \in (-1, 1)$ |
| $\frac{1}{\sqrt{x^2 + q}}$ | $\ln\left| x + \sqrt{x^2 + q} \right| + C$ | $x^2 + q > 0$ |
| $\frac{1}{a^2 - x^2}$ | $\frac{1}{2a} \ln\left| \frac{a + x}{a - x} \right| + C$ | $|x| \neq a$ |

---

### 12.3. Metoda całkowania przez części

> **Twierdzenie 12.2 (O całkowaniu przez części):**
> Jeżeli funkcje $u$ i $v$ mają ciągłe pochodne w przedziale $(a, b)$, to:
> $$\int u(x) v'(x) \, dx = u(x) v(x) - \int u'(x) v(x) \, dx$$
> lub w zapisie różniczkowym ($du = u'dx, dv = v'dx$):
> $$\int u \, dv = u v - \int v \, du$$

#### Całki cykliczne (rekurencyjne)
Często po dwukrotnym całkowaniu przez części poszukiwana całka pojawia się ponownie po prawej stronie równania z przeciwnym znakiem, co pozwala wyznaczyć ją algebraicznie.

---

### 12.4. Metoda całkowania przez podstawienie (zamiana zmiennych)

> **Twierdzenie 12.3 (O całkowaniu przez podstawienie):**
> Jeżeli funkcja $x = \varphi(t)$ jest różniczkowalna i ma ciągłą pochodną $\varphi'(t) \neq 0$ w przedziale $T$, a funkcja $f$ ma funkcję pierwotną $F$ w przedziale $\varphi(T)$, to:
> $$\int f\big(\varphi(t)\big) \varphi'(t) \, dt = F\big(\varphi(t)\big) + C$$
> W praktyce: kładąc $x = \varphi(t)$, różniczkujemy formalnie $dx = \varphi'(t) dt$:
> $$\int f(x) \, dx = \left. \int f\big(\varphi(t)\big) \varphi'(t) \, dt \right|_{t = \varphi^{-1}(x)}$$

#### Ważny przypadek szczególny (Licznik pochodną mianownika):
$$\int \frac{f'(x)}{f(x)} \, dx = \ln|f(x)| + C$$

---

## Rozdział 13: Techniki całkowania wybranych klas funkcji

### 13.1. Całkowanie funkcji wymiernych

Funkcją wymierną nazywamy iloraz dwóch wielomianów:
$$W(x) = \frac{P(x)}{Q(x)}$$

#### Algorytm całkowania funkcji wymiernej:
1. **Dzielenie wielomianów:** Jeżeli $\deg P \ge \deg Q$ (ułamek niewłaściwy), dzielimy licznik przez mianownik z resztą:
   $$\frac{P(x)}{Q(x)} = W_0(x) + \frac{R(x)}{Q(x)}, \quad \deg R < \deg Q$$
   Wielomian $W_0(x)$ całkuje się bezpośrednio.
2. **Rozkład mianownika na czynniki nierozkładalne w $\mathbb{R}$:**
   Zgodnie z Zasadniczym Twierdzeniem Algebry mianownik rozkłada się na czynniki liniowe oraz kwadratowe o ujemnym wyróżniku ($\Delta < 0$):
   $$Q(x) = a_n (x - x_1)^{k_1} \dots (x - x_r)^{k_r} (x^2 + p_1 x + q_1)^{m_1} \dots (x^2 + p_s x + q_s)^{m_s}$$
3. **Rozkład na ułamki proste:**
   Każdemu czynnikowi wielokrotnemu odpowiada suma ułamków prostych:
   - dla $(x - a)^k$:
     $$\frac{A_1}{x - a} + \frac{A_2}{(x - a)^2} + \dots + \frac{A_k}{(x - a)^k}$$
   - dla $(x^2 + px + q)^m$ ($\Delta = p^2 - 4q < 0$):
     $$\frac{B_1 x + C_1}{x^2 + px + q} + \frac{B_2 x + C_2}{(x^2 + px + q)^2} + \dots + \frac{B_m x + C_m}{(x^2 + px + q)^m}$$
4. **Całkowanie ułamków prostych:**
   - I rodzaju: $\int \frac{A}{(x-a)^k} dx = \begin{cases} A \ln|x-a| + C & (k=1) \\ \frac{A}{(1-k)(x-a)^{k-1}} + C & (k>1) \end{cases}$
   - II rodzaju: sprowadzamy mianownik do postaci kanonicznej $(x-p_0)^2 + q_0^2$ i rozdzielamy na część logarytmiczną oraz arkus tangens:
     $$\int \frac{Bx + C}{x^2 + px + q} \, dx = \frac{B}{2} \ln(x^2 + px + q) + \frac{C - \frac{Bp}{2}}{\sqrt{q - \frac{p^2}{4}}} \operatorname{arctg}\left( \frac{x + \frac{p}{2}}{\sqrt{q - \frac{p^2}{4}}} \right) + K$$

---

### 13.2. Całkowanie wyrażeń trygonometrycznych $\int R(\sin x, \cos x) \, dx$

#### Podstawienie uniwersalne:
Podstawienie $t = \operatorname{tg}\frac{x}{2}$ (dla $x \in (-\pi, \pi)$) sprowadza dowolną całkę trygonometryczną do całki z funkcji wymiernej:
$$x = 2 \operatorname{arctg} t \implies dx = \frac{2}{1 + t^2} \, dt$$
Wzory redukcyjne:
$$\sin x = \frac{2 \sin\frac{x}{2} \cos\frac{x}{2}}{\cos^2\frac{x}{2} + \sin^2\frac{x}{2}} = \frac{2t}{1 + t^2}$$
$$\cos x = \frac{\cos^2\frac{x}{2} - \sin^2\frac{x}{2}}{\cos^2\frac{x}{2} + \sin^2\frac{x}{2}} = \frac{1 - t^2}{1 + t^2}$$

#### Podstawienia specjalne (szybsze):
- Jeżeli $R(-\sin x, \cos x) = -R(\sin x, \cos x)$ (funkcja nieparzysta ze względu na $\sin x$) $\implies$ podstawienie $t = \cos x$, $dt = -\sin x dx$.
- Jeżeli $R(\sin x, -\cos x) = -R(\sin x, \cos x)$ (funkcja nieparzysta ze względu na $\cos x$) $\implies$ podstawienie $t = \sin x$, $dt = \cos x dx$.
- Jeżeli $R(-\sin x, -\cos x) = R(\sin x, \cos x)$ (parzysta ze względu na oba) $\implies$ podstawienie $t = \operatorname{tg} x$:
  $$\cos^2 x = \frac{1}{1 + t^2}, \quad \sin^2 x = \frac{t^2}{1 + t^2}, \quad dx = \frac{dt}{1 + t^2}$$

---

### 13.3. Całkowanie wyrażeń niewymiernych i podstawienia Eulera

Dla całek postaci $\int R(x, \sqrt{ax^2 + bx + c}) \, dx$ stosuje się klasyczne **trzy podstawienia Eulera**:

1. **I podstawienie Eulera (gdy $a > 0$):**
   $$\sqrt{ax^2 + bx + c} = t - \sqrt{a}x$$
   Podnosząc obustronnie do kwadratu: $ax^2 + bx + c = t^2 - 2\sqrt{a}xt + ax^2$, skąd $x$ wyraża się jako funkcja wymierna zmiennej $t$:
   $$x = \frac{t^2 - c}{2\sqrt{a}t + b}$$
2. **II podstawienie Eulera (gdy $c > 0$):**
   $$\sqrt{ax^2 + bx + c} = xt + \sqrt{c}$$
   Podnosząc do kwadratu: $ax^2 + bx + c = x^2 t^2 + 2\sqrt{c}xt + c$, dzieląc przez $x \neq 0$:
   $$x = \frac{2\sqrt{c}t - b}{a - t^2}$$
3. **III podstawienie Eulera (gdy $\Delta = b^2 - 4ac > 0$):**
   Niech $x_1, x_2$ będą różnymi pierwiastkami trójmianu: $ax^2 + bx + c = a(x - x_1)(x - x_2)$. Kładziemy:
   $$\sqrt{ax^2 + bx + c} = t(x - x_1)$$
   skąd $a(x - x_1)(x - x_2) = t^2(x - x_1)^2 \implies a(x - x_2) = t^2(x - x_1)$, co natychmiast daje $x$ jako ułamek wymierny $t$.

---

### 13.4. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 6.1: Całkowanie przez części (całka cykliczna)
Oblicz całkę:
$$I = \int e^{2x} \cos(3x) \, dx$$

**Rozwiązanie:**
Całkujemy przez części. Przyjmijmy:
- $u = \cos(3x) \implies du = -3\sin(3x) dx$
- $dv = e^{2x} dx \implies v = \frac{1}{2} e^{2x}$

Mamy:
$$I = \frac{1}{2} e^{2x} \cos(3x) - \int \frac{1}{2} e^{2x} (-3\sin(3x)) \, dx = \frac{1}{2} e^{2x} \cos(3x) + \frac{3}{2} \int e^{2x} \sin(3x) \, dx$$
Całkujemy otrzymaną całkę ponownie przez części:
- $u_1 = \sin(3x) \implies du_1 = 3\cos(3x) dx$
- $dv_1 = e^{2x} dx \implies v_1 = \frac{1}{2} e^{2x}$

Wstawiamy:
$$\int e^{2x} \sin(3x) \, dx = \frac{1}{2} e^{2x} \sin(3x) - \frac{3}{2} \int e^{2x} \cos(3x) \, dx = \frac{1}{2} e^{2x} \sin(3x) - \frac{3}{2} I$$
Łącząc wyniki:
$$I = \frac{1}{2} e^{2x} \cos(3x) + \frac{3}{2} \left[ \frac{1}{2} e^{2x} \sin(3x) - \frac{3}{2} I \right] = \frac{1}{2} e^{2x} \cos(3x) + \frac{3}{4} e^{2x} \sin(3x) - \frac{9}{4} I$$
Przenosimy $I$ na lewą stronę:
$$I + \frac{9}{4} I = \frac{13}{4} I = e^{2x} \left( \frac{1}{2}\cos(3x) + \frac{3}{4}\sin(3x) \right) + C'$$
Mnożąc przez $\frac{4}{13}$:
$$I = \frac{e^{2x}}{13} \big( 2\cos(3x) + 3\sin(3x) \big) + C$$

---

#### Przykład 6.2: Rozkład na ułamki proste
Oblicz całkę:
$$\int \frac{2x^2 - x + 4}{x^3 + 4x} \, dx$$

**Rozwiązanie:**
Rozkładamy mianownik na czynniki nierozkładalne:
$$x^3 + 4x = x(x^2 + 4)$$
Stopień licznika (2) jest mniejszy od stopnia mianownika (3).  
Postać rozkładu na ułamki proste:
$$\frac{2x^2 - x + 4}{x(x^2 + 4)} = \frac{A}{x} + \frac{Bx + C}{x^2 + 4}$$
Mnożymy obustronnie przez $x(x^2 + 4)$:
$$2x^2 - x + 4 = A(x^2 + 4) + (Bx + C)x = (A + B)x^2 + Cx + 4A$$
Porównujemy współczynniki przy odpowiednich potęgach $x$:
$$\begin{cases}
A + B = 2 \\
C = -1 \\
4A = 4 \implies A = 1
\end{cases} \implies B = 2 - A = 1, \quad C = -1$$
Zatem całka przyjmuje postać:
$$\int \left( \frac{1}{x} + \frac{x - 1}{x^2 + 4} \right) \, dx = \int \frac{1}{x} \, dx + \frac{1}{2} \int \frac{2x}{x^2 + 4} \, dx - \int \frac{1}{x^2 + 4} \, dx$$
Obliczamy poszczególne składniki:
1. $\int \frac{1}{x} dx = \ln|x|$,
2. $\frac{1}{2} \int \frac{2x}{x^2+4} dx = \frac{1}{2} \ln(x^2 + 4)$,
3. $\int \frac{1}{x^2 + 4} dx = \frac{1}{2} \operatorname{arctg}\left(\frac{x}{2}\right)$.

Ostatecznie:
$$\int \frac{2x^2 - x + 4}{x^3 + 4x} \, dx = \ln|x| + \frac{1}{2}\ln(x^2 + 4) - \frac{1}{2}\operatorname{arctg}\left(\frac{x}{2}\right) + C = \ln\left( |x| \sqrt{x^2+4} \right) - \frac{1}{2}\operatorname{arctg}\left(\frac{x}{2}\right) + C$$

---

### 13.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 6.1:** Oblicz całkę: $\int x^2 \ln x \, dx$.
2. **Zadanie 6.2:** Oblicz całkę: $\int \frac{x}{\sqrt{1 - x^4}} \, dx$.
3. **Zadanie 6.3:** Oblicz całkę: $\int \frac{dx}{1 + 3\cos^2 x}$.
4. **Zadanie 6.4:** Oblicz całkę funkcji wymiernej: $\int \frac{dx}{x^3 - 1}$.
5. **Zadanie 6.5:** Oblicz całkę: $\int \sqrt{x^2 + 4} \, dx$ za pomocą I podstawienia Eulera lub podstawienia hiperbolicznego.

---

### Odpowiedzi i wskazówki do zadań

- **6.1:** Całkowanie przez części ($u = \ln x, dv = x^2 dx$): $\frac{x^3}{3}\ln x - \int \frac{x^2}{3} dx = \frac{x^3}{3}\ln x - \frac{x^3}{9} + C$.
- **6.2:** Podstawienie $t = x^2 \implies dt = 2x dx$: $\frac{1}{2}\int \frac{dt}{\sqrt{1 - t^2}} = \frac{1}{2}\arcsin(x^2) + C$.
- **6.3:** Podstawienie $t = \operatorname{tg} x \implies dx = \frac{dt}{1+t^2}, \cos^2 x = \frac{1}{1+t^2}$: $\int \frac{\frac{dt}{1+t^2}}{1 + \frac{3}{1+t^2}} = \int \frac{dt}{t^2 + 4} = \frac{1}{2}\operatorname{arctg}\left(\frac{\operatorname{tg} x}{2}\right) + C$.
- **6.4:** Rozkład na ułamki: $\frac{1}{x^3-1} = \frac{1}{3(x-1)} - \frac{x+2}{3(x^2+x+1)}$. Wynik: $\frac{1}{3}\ln|x-1| - \frac{1}{6}\ln(x^2+x+1) - \frac{\sqrt{3}}{3}\operatorname{arctg}\left(\frac{2x+1}{\sqrt{3}}\right) + C$.
- **6.5:** $\frac{x}{2}\sqrt{x^2+4} + 2\ln\left( x + \sqrt{x^2+4} \right) + C$.


\newpage

# Część VII: Całka Oznaczona i Całki Niewłaściwe

Całka oznaczona stanowi fundament ilościowego modelowania w naukach technicznych. O ile całka nieoznaczona jest operacją algebraiczną wyznaczania funkcji pierwotnej, o tyle całka oznaczona jest wielkością liczbową (granicą sum całkowych), reprezentującą pole powierzchni, objętość, całkowity ładunek elektryczny, energię pola czy wartość skuteczną przebiegów czasowych.

---

## Rozdział 14: Całka oznaczona Riemanna

### 14.1. Konstrukcja całki Riemanna

Rozważmy funkcję ograniczoną $f: [a, b] \to \mathbb{R}$ na przedziale domkniętym $[a, b]$ ($a < b$).

#### Definicja 14.1 (Podział przedziału i punkty pośrednie)
1. **Podziałem** $P$ przedziału $[a, b]$ nazywamy skończony ciąg punktów:
   $$P = \{x_0, x_1, x_2, \dots, x_n\}, \quad a = x_0 < x_1 < x_2 < \dots < x_n = b$$
   Punkty te dzielą $[a, b]$ na $n$ podprzedziałów $\Delta x_i = x_i - x_{i-1}$ dla $i = 1, 2, \dots, n$.
2. **Średnicą podziału** $P$ nazywamy długość najdłuższego podprzedziału:
   $$\delta(P) = \max_{1 \le i \le n} \Delta x_i$$
3. W każdym podprzedziale $[x_{i-1}, x_i]$ wybieramy **punkt pośredni** $\xi_i \in [x_{i-1}, x_i]$.
4. **Sumą całkową Riemanna** odpowiadającą podziałowi $P$ i punktom pośrednim $\xi = (\xi_1, \dots, \xi_n)$ nazywamy liczbę:
   $$\sigma(P, \xi) = \sum_{i=1}^n f(\xi_i) \Delta x_i$$

#### Definicja 14.2 (Całka oznaczona Riemanna)
Liczbę $I \in \mathbb{R}$ nazywamy **całką oznaczoną Riemanna** funkcji $f$ na przedziale $[a, b]$ i oznaczamy symbolem:
$$\int_a^b f(x) \, dx$$
jeżeli dla każdego ciągu podziałów $(P_k)$ o średnicy zmierzającej do zera ($\lim_{k \to \infty} \delta(P_k) = 0$) i dla dowolnego wyboru punktów pośrednich $\xi^{(k)}$, odpowiadający ciąg sum całkowych dąży do $I$:

$$\int_a^b f(x) \, dx = \lim_{\delta(P) \to 0} \sum_{i=1}^n f(\xi_i) \Delta x_i$$

Jeżeli granica ta istnieje i jest skończona, funkcję $f$ nazywamy **całkowalną w sensie Riemanna** na $[a, b]$ (co zapisujemy $f \in \mathcal{R}[a, b]$).

---

### 14.2. Warunki całkowalności funkcji

> **Twierdzenie 14.1 (Klasy funkcji całkowalnych w sensie Riemanna):**
> 1. Każda funkcja ciągła na przedziale domkniętym $[a, b]$ jest całkowalna w sensie Riemanna ($C[a, b] \subset \mathcal{R}[a, b]$).
> 2. Każda funkcja monotoniczna na $[a, b]$ jest całkowalna w sensie Riemanna.
> 3. Każda funkcja ograniczona na $[a, b]$, posiadająca co najwyżej przeliczalną liczbę punktów nieciągłości, jest całkowalna w sensie Riemanna.

---

### 14.3. Własności całki oznaczonej

> **Twierdzenie 14.2:**
> Niech $f, g \in \mathcal{R}[a, b]$ oraz $\alpha, \beta \in \mathbb{R}$:
> 1. **Liniowość:** $\int_a^b (\alpha f(x) + \beta g(x)) \, dx = \alpha \int_a^b f(x) \, dx + \beta \int_a^b g(x) \, dx$
> 2. **Addytywność względem przedziału:** Dla dowolnego $c \in [a, b]$:
>    $$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx$$
> 3. **Monotoniczność:** Jeżeli $f(x) \le g(x)$ dla każdego $x \in [a, b]$, to:
>    $$\int_a^b f(x) \, dx \le \int_a^b g(x) \, dx$$
> 4. **Nierówność modułowa:**
>    $$\left| \int_a^b f(x) \, dx \right| \le \int_a^b |f(x)| \, dx$$
> 5. **Twierdzenie o wartości średniej rachunku całkowego:**  
>    Jeżeli funkcja $f$ jest ciągła na $[a, b]$, to istnieje punkt $c \in [a, b]$ taki, że:
>    $$\int_a^b f(x) \, dx = f(c)(b - a) \iff f(c) = \frac{1}{b - a} \int_a^b f(x) \, dx$$
>    Wartość $\mu = \frac{1}{b-a} \int_a^b f(x) \, dx$ nazywamy **wartością średnią funkcji** na przedziale $[a, b]$.

---

### 14.4. Podstawowe Twierdzenie Rachunku Całkowego (Wzór Newtona-Leibniza)

Twierdzenie Newtona-Leibniza stanowi fundamentalny most łączący pojęcie pochodnej z całką oznaczoną.

> **Twierdzenie 14.3 (Funkcja górnej granicy całkowania):**
> Niech $f \in C[a, b]$. Funkcja $\Phi: [a, b] \to \mathbb{R}$ zdefiniowana wzorem:
> $$\Phi(x) = \int_a^x f(t) \, dt$$
> jest różniczkowalna w każdym punkcie $x \in [a, b]$ oraz:
> $$\Phi'(x) = \frac{d}{dx} \left( \int_a^x f(t) \, dt \right) = f(x)$$
> Oznacza to, że funkcja $\Phi(x)$ jest funkcją pierwotną funkcji $f(x)$.

> **Twierdzenie 14.4 (Wzór Newtona-Leibniza):**
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$, a $F$ jest jej dowolną funkcją pierwotną ($F'(x) = f(x)$), to:
> $$\int_a^b f(x) \, dx = F(b) - F(a) = \Big[ F(x) \Big]_a^b$$

**Dowód:**
Wiemy, że $\Phi(x) = \int_a^x f(t) dt$ jest funkcją pierwotną $f(x)$. Ponieważ każda inna funkcja pierwotna $F(x)$ różni się od $\Phi(x)$ o stałą $C$, mamy $F(x) = \Phi(x) + C$.  
Dla $x = a$:
$$F(a) = \Phi(a) + C = \int_a^a f(t) \, dt + C = 0 + C = C$$
Dla $x = b$:
$$F(b) = \Phi(b) + C = \int_a^b f(t) \, dt + F(a)$$
Odejmując $F(a)$ obustronnie:
$$\int_a^b f(x) \, dx = F(b) - F(a) \quad \blacksquare$$

#### Metody obliczania całek oznaczonych:
1. **Całkowanie przez części:**
   $$\int_a^b u(x) v'(x) \, dx = \Big[ u(x) v(x) \Big]_a^b - \int_a^b u'(x) v(x) \, dx$$
2. **Całkowanie przez podstawienie (zamiana granic całkowania):**
   $$\int_a^b f\big(\varphi(t)\big) \varphi'(t) \, dt = \int_{\varphi(a)}^{\varphi(b)} f(x) \, dx$$
   *(Przy zamianie zmiennych w całce oznaczonej przelicza się granice całkowania, co eliminuje konieczność powrotu do zmiennej wyjściowej).*

---

## Rozdział 15: Zastosowania geometryczne i inżynierskie

### 15.1. Zastosowania geometryczne

1. **Pole obszaru płaskiego:**  
   Obszar ograniczony krzywymi $y = f(x)$, $y = g(x)$ ($f(x) \ge g(x)$) oraz prostymi $x = a, x = b$:
   $$P = \int_a^b \big( f(x) - g(x) \big) \, dx$$
   We współrzędnych biegunowych $r = r(\varphi)$ dla $\alpha \le \varphi \le \beta$:
   $$P = \frac{1}{2} \int_\alpha^\beta r^2(\varphi) \, d\varphi$$

2. **Długość łuku krzywej:**
   - Postać jawna $y = f(x)$ ($x \in [a, b]$):
     $$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$
   - Postać parametryczna $x = x(t), y = y(t)$ ($t \in [t_1, t_2]$):
     $$L = \int_{t_1}^{t_2} \sqrt{[\dot{x}(t)]^2 + [\dot{y}(t)]^2} \, dt$$

3. **Objętość bryły obrotowej:**  
   Obrót wykresu funkcji $y = f(x)$ wokół osi $OX$ dla $x \in [a, b]$:
   $$V = \pi \int_a^b [f(x)]^2 \, dx$$

4. **Pole powierzchni bocznej bryły obrotowej:**
   $$S = 2\pi \int_a^b |f(x)| \sqrt{1 + [f'(x)]^2} \, dx$$

---

### 15.2. Zastosowania w elektrotechnice i teorii sygnałów (WEiTI PW)

#### 1. Wartość skuteczna (RMS - Root Mean Square) sygnału okresowego
Dla sygnału okresowego $u(t)$ o okresie $T$ wartość skuteczną definiuje się z bilansu cieplnego (prąd stały wywołujący ten sam efekt cieplny na rezystorze $R$):
$$U_{\text{sk}} = U_{\text{RMS}} = \sqrt{\frac{1}{T} \int_0^T u^2(t) \, dt}$$

Dla czystej sinusoidy $u(t) = U_m \cos(\omega t + \psi)$:
$$U_{\text{RMS}}^2 = \frac{1}{T} \int_0^T U_m^2 \cos^2(\omega t) \, dt = \frac{U_m^2}{T} \int_0^T \frac{1 + \cos(2\omega t)}{2} \, dt = \frac{U_m^2}{2T} [t]_0^T = \frac{U_m^2}{2}$$
Stąd fundamentalna zależność inżynierska:
$$U_{\text{RMS}} = \frac{U_m}{\sqrt{2}} \approx 0{,}707 U_m$$

#### 2. Moc czynna przebiegu okresowego
Moc chwilowa wynosi $p(t) = u(t) \cdot i(t)$. Moc czynna $P$ to wartość średnia mocy chwilowej za okres:
$$P = \frac{1}{T} \int_0^T u(t) i(t) \, dt$$

#### 3. Energia zmagazynowana w polu elektrycznym i magnetycznym
- Energia kondensatora naładowanego do napięcia $U_0$:
  $$W_E = \int_0^{Q_0} u \, dq = \int_0^{Q_0} \frac{q}{C} \, dq = \frac{1}{2}\frac{Q_0^2}{C} = \frac{1}{2} C U_0^2$$
- Energia cewki o indukcyjności $L$ przewodzącej prąd $I_0$:
  $$W_M = \int_0^{t_0} u(t) i(t) \, dt = \int_0^{I_0} L \frac{di}{dt} \cdot i \, dt = L \int_0^{I_0} i \, di = \frac{1}{2} L I_0^2$$

---

## Rozdział 16: Całki niewłaściwe

Gdy przedział całkowania jest nieskończony lub funkcja podcałkowa jest nieograniczona, definicję Riemanna rozszerza się poprzez operację przejścia granicznego.

### 16.1. Całki niewłaściwe I rodzaju (przedział nieskończony)

#### Definicja 16.1
1. Jeżeli funkcja $f$ jest całkowalna na każdym przedziale $[a, T]$ dla $T > a$, to:
   $$\int_a^{+\infty} f(x) \, dx = \lim_{T \to +\infty} \int_a^T f(x) \, dx$$
2. Całka na całej prostej $\mathbb{R}$:
   $$\int_{-\infty}^{+\infty} f(x) \, dx = \int_{-\infty}^c f(x) \, dx + \int_c^{+\infty} f(x) \, dx \quad (c \in \mathbb{R})$$
   (zbieżna wtedy i tylko wtedy, gdy obie całki po prawej stronie są zbieżne niezależnie).

#### Wzorcowa całka I rodzaju:
$$\int_1^{+\infty} \frac{dx}{x^\alpha} = \lim_{T \to \infty} \left[ \frac{x^{1-\alpha}}{1-\alpha} \right]_1^T = \begin{cases} \frac{1}{\alpha - 1} & \text{dla } \alpha > 1 \text{ (zbieżna)} \\ +\infty & \text{dla } \alpha \le 1 \text{ (rozbieżna)} \end{cases}$$

---

### 16.2. Całki niewłaściwe II rodzaju (funkcja nieograniczona)

#### Definicja 16.2
Jeżeli funkcja $f$ jest nieograniczona w lewostronnym otoczeniu punktu $b$ ($\lim_{x \to b^-} |f(x)| = +\infty$):
$$\int_a^b f(x) \, dx = \lim_{\varepsilon \to 0^+} \int_a^{b - \varepsilon} f(x) \, dx$$

#### Wzorcowa całka II rodzaju:
$$\int_0^1 \frac{dx}{x^\alpha} = \begin{cases} \frac{1}{1 - \alpha} & \text{dla } \alpha < 1 \text{ (zbieżna)} \\ +\infty & \text{dla } \alpha \ge 1 \text{ (rozbieżna)} \end{cases}$$

*(Zwróć uwagę na odwrócenie kryterium w porównaniu z całką I rodzaju: w zerze całka jest zbieżna dla $\alpha < 1$, a w nieskończoności dla $\alpha > 1$).*

---

### 16.3. Kryteria zbieżności całek niewłaściwych

> **Twierdzenie 16.1 (Kryterium porównawcze dla całek nieujemnych):**
> Niech $0 \le f(x) \le g(x)$ na $[a, +\infty)$:
> 1. $\int_a^{+\infty} g(x) \, dx < \infty \implies \int_a^{+\infty} f(x) \, dx < \infty$ (zbieżność majoranty pociąga zbieżność),
> 2. $\int_a^{+\infty} f(x) \, dx = +\infty \implies \int_a^{+\infty} g(x) \, dx = +\infty$ (rozbieżność minoranty).

---

### 16.4. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 7.1: Całka oznaczona z zamianą granic całkowania
Oblicz całkę oznaczoną:
$$I = \int_0^{\pi/2} \frac{\cos x}{1 + \sin^2 x} \, dx$$

**Rozwiązanie:**
Stosujemy podstawienie:
$$t = \sin x \implies dt = \cos x \, dx$$
Przeliczamy granice całkowania:
- Dla $x = 0$: $t = \sin(0) = 0$,
- Dla $x = \frac{\pi}{2}$: $t = \sin\left(\frac{\pi}{2}\right) = 1$.

Wstawiając do całki:
$$I = \int_0^1 \frac{dt}{1 + t^2} = \Big[ \operatorname{arctg} t \Big]_0^1 = \operatorname{arctg}(1) - \operatorname{arctg}(0) = \frac{\pi}{4} - 0 = \frac{\pi}{4}$$

---

#### Przykład 7.2: Obliczanie pola powierzchni ograniczonego dwiema krzywymi
Oblicz pole obszaru ograniczonego parabolą $y = x^2$ oraz prostą $y = 2x + 3$.

**Rozwiązanie:**
1. Wyznaczamy punkty przecięcia krzywych:
   $$x^2 = 2x + 3 \iff x^2 - 2x - 3 = 0 \iff (x - 3)(x + 1) = 0 \implies x_1 = -1, \quad x_2 = 3$$
2. W przedziale $[-1, 3]$ prosta leży powyżej paraboli ($2x + 3 \ge x^2$). Pole wynosi:
   $$P = \int_{-1}^3 \big( (2x + 3) - x^2 \big) \, dx = \left[ x^2 + 3x - \frac{x^3}{3} \right]_{-1}^3$$
3. Podstawiamy granice:
   - Dla $x = 3$: $3^2 + 3(3) - \frac{27}{3} = 9 + 9 - 9 = 9$,
   - Dla $x = -1$: $(-1)^2 + 3(-1) - \frac{-1}{3} = 1 - 3 + \frac{1}{3} = -\frac{5}{3}$.
   $$P = 9 - \left(-\frac{5}{3}\right) = 9 + \frac{5}{3} = \frac{32}{3}$$

---

#### Przykład 7.3: Badanie zbieżności całki niewłaściwej
Zbadaj zbieżność całki:
$$\int_0^{+\infty} x^2 e^{-x} \, dx$$

**Rozwiązanie:**
Z definicji całki niewłaściwej:
$$I = \lim_{T \to +\infty} \int_0^T x^2 e^{-x} \, dx$$
Całkujemy przez części:
- $u = x^2 \implies du = 2x dx$, $dv = e^{-x} dx \implies v = -e^{-x}$:
  $$\int x^2 e^{-x} \, dx = -x^2 e^{-x} + 2 \int x e^{-x} \, dx$$
- Ponownie przez części dla $\int x e^{-x} dx$ ($u_1 = x, dv_1 = e^{-x} dx \implies v_1 = -e^{-x}$):
  $$\int x e^{-x} \, dx = -x e^{-x} - \int (-e^{-x}) \, dx = -x e^{-x} - e^{-x}$$
Zatem funkcja pierwotna:
$$F(x) = -e^{-x}(x^2 + 2x + 2)$$
Obliczamy granicę w granicach całkowania:
$$\int_0^T x^2 e^{-x} \, dx = \Big[ -e^{-x}(x^2 + 2x + 2) \Big]_0^T = -e^{-T}(T^2 + 2T + 2) - (-e^0(0 + 0 + 2)) = 2 - \frac{T^2 + 2T + 2}{e^T}$$
Z reguły de l'Hospitala $\lim_{T \to \infty} \frac{T^2 + 2T + 2}{e^T} = 0$.  
Stąd całka jest zbieżna i jej wartość wynosi:
$$\int_0^{+\infty} x^2 e^{-x} \, dx = 2$$

---

### 15.3. Zadania do samodzielnego rozwiązania

1. **Zadanie 7.1:** Oblicz całkę oznaczoną: $\int_1^e \frac{\ln^2 x}{x} \, dx$.
2. **Zadanie 7.2:** Oblicz długość łuku asteroidy zadanej równaniem parametrycznym: $x(t) = a \cos^3 t$, $y(t) = a \sin^3 t$ dla $t \in [0, 2\pi]$ ($a > 0$).
3. **Zadanie 7.3:** Oblicz objętość bryły powstałej przez obrót wokół osi $OX$ wykresu funkcji $f(x) = \sin x$ dla $x \in [0, \pi]$.
4. **Zadanie 7.4 (RMS sygnału trójkątnego):** Napięcie okresowe ma kształt symetrycznej fali trójkątnej o amplitudzie $U_m$ opisanej w pierwszym półokresie $[0, T/2]$ wzorem $u(t) = \frac{2U_m}{T/2} t = \frac{4U_m}{T} t$. Oblicz wartość skuteczną $U_{\text{RMS}}$ tego sygnału i porównaj z wartością dla fali sinusoidalnej.
5. **Zadanie 7.5:** Zbadaj zbieżność całki niewłaściwej: $\int_1^{+\infty} \frac{x^2 + 1}{x^4 + 3x + 2} \, dx$.

---

### Odpowiedzi i wskazówki do zadań

- **7.1:** Podstawienie $t = \ln x \implies dt = \frac{dx}{x}$. Granice: $t \in [0, 1]$. $\int_0^1 t^2 dt = \left[\frac{t^3}{3}\right]_0^1 = \frac{1}{3}$.
- **7.2:** Wykorzystujemy symetrię (4 ćwiartki). Dla $t \in [0, \pi/2]$: $\dot{x} = -3a\cos^2 t \sin t$, $\dot{y} = 3a\sin^2 t \cos t$. $\sqrt{\dot{x}^2 + \dot{y}^2} = 3a\sin t \cos t$. Całka: $L = 4 \int_0^{\pi/2} 3a \sin t \cos t dt = 12a \left[ \frac{\sin^2 t}{2} \right]_0^{\pi/2} = 6a$.
- **7.3:** $V = \pi \int_0^\pi \sin^2 x dx = \pi \int_0^\pi \frac{1 - \cos(2x)}{2} dx = \frac{\pi}{2} [x]_0^\pi = \frac{\pi^2}{2}$.
- **7.4:** Ze względu na symetrię: $U_{\text{RMS}}^2 = \frac{2}{T} \int_0^{T/2} \left( \frac{4U_m}{T} t \right)^2 dt = \frac{32 U_m^2}{T^3} \left[ \frac{t^3}{3} \right]_0^{T/2} = \frac{32 U_m^2}{T^3} \frac{T^3}{24} = \frac{U_m^2}{3}$. Stąd $U_{\text{RMS}} = \frac{U_m}{\sqrt{3}} \approx 0{,}577 U_m$. Dla sinusoidy wartość skuteczna jest większa ($0{,}707 U_m$).
- **7.5:** Zbieżna. Dla dużych $x$ funkcja zachowuje się jak $\frac{x^2}{x^4} = \frac{1}{x^2}$. Stosujemy ilorazowe kryterium porównawcze ze zbieżną całką $\int_1^\infty \frac{dx}{x^2}$.


\newpage

# Część VIII: Szeregi Potęgowe i Wprowadzenie do Analizy Fourierowskiej

Ostatnia część tomu pierwszego łączy aparat szeregów liczbowych z funkcjami rzeczywistymi. Szeregi potęgowe stanowią fundament analizy zespolonej i metod numerycznych, umożliwiając reprezentację funkcji nieliniowych za pomocą nieskończonych wielomianów. Z kolei trygonometryczne szeregi Fouriera są **językiem ojczystym elektroniki, telekomunikacji i teorii sygnałów**, pozwalając na dekompozycję dowolnego przebiegu okresowego na składowe harmoniczne (analiza widmowa).

---

## Rozdział 17: Szeregi funkcyjne i potęgowe

### 17.1. Zbieżność punktowa i jednostajna

#### Definicja 17.1 (Ciąg i szereg funkcyjny)
Niech $f_n: X \to \mathbb{R}$ dla każdego $n \in \mathbb{N}$.  
Wyrażenie postaci $\sum_{n=1}^\infty f_n(x)$ nazywamy **szeregiem funkcyjnym**.  
1. **Zbieżność punktowa:** Szereg jest zbieżny punktowo na zbiorze $X$ do funkcji $S(x)$, jeżeli dla każdego ustalonego $x_0 \in X$ szereg liczbowy $\sum_{n=1}^\infty f_n(x_0)$ jest zbieżny do liczby $S(x_0)$:
   $$\forall_{x \in X} \forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{n > N} \quad \left| \sum_{k=1}^n f_k(x) - S(x) \right| < \varepsilon$$
2. **Zbieżność jednostajna:** Szereg jest zbieżny jednostajnie na $X$ ($S_n \rightrightarrows S$), jeżeli wskaźnik $N$ zależy wyłącznie od $\varepsilon$, a nie od punktu $x$:
   $$\forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{n > N} \forall_{x \in X} \quad \left| \sum_{k=1}^n f_k(x) - S(x) \right| < \varepsilon$$

> **Twierdzenie 17.1 (Kryterium Weierstrassa zbieżności jednostajnej):**
> Jeżeli dla każdego $n \in \mathbb{N}$ istnieje stała $M_n \ge 0$ taka, że:
> $$\forall_{x \in X} \quad |f_n(x)| \le M_n$$
> oraz szereg liczbowy $\sum_{n=1}^\infty M_n$ jest zbieżny, to szereg funkcyjny $\sum_{n=1}^\infty f_n(x)$ jest **zbieżny jednostajnie i bezwzględnie** na zbiorze $X$.

#### Konsekwencje zbieżności jednostajnej:
- **Ciągłość sumy:** Jeżeli funkcje $f_n$ są ciągłe i szereg $\sum f_n$ jest zbieżny jednostajnie, to jego suma $S(x)$ jest funkcją ciągłą.
- **Całkowanie wyraz po wyrazie:**
  $$\int_a^b \left( \sum_{n=1}^\infty f_n(x) \right) \, dx = \sum_{n=1}^\infty \int_a^b f_n(x) \, dx$$
- **Różniczkowanie wyraz po wyrazie:** Jeżeli szereg pochodnych $\sum f_n'$ jest jednostajnie zbieżny, to $\left( \sum f_n(x) \right)' = \sum f_n'(x)$.

---

### 17.2. Szeregi potęgowe

Szeregiem potęgowym o środku w punkcie $x_0$ nazywamy szereg funkcyjny postaci:
$$\sum_{n=0}^\infty a_n (x - x_0)^n = a_0 + a_1 (x - x_0) + a_2 (x - x_0)^2 + \dots$$

> **Twierdzenie 17.2 (Cauchy'ego-Hadamarda o promieniu zbieżności):**
> Dla każdego szeregu potęgowego istnieje liczba $R \in [0, +\infty]$ (zwana **promieniem zbieżności**) taka, że szereg jest:
> - **zbieżny bezwzględnie** dla każdego $x$ takiego, że $|x - x_0| < R$,
> - **rozbieżny** dla każdego $x$ takiego, że $|x - x_0| > R$.
> Promień zbieżności wyznacza się ze wzoru:
> $$R = \frac{1}{\limsup_{n \to \infty} \sqrt[n]{|a_n|}} \quad \text{lub} \quad R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right| \quad (\text{o ile granica istnieje})$$

Przedział $(x_0 - R, x_0 + R)$ nazywamy **przedziałem zbieżności**. Na końcach przedziału ($x = x_0 \pm R$) zbieżność należy badać indywidualnie.

---

### 17.3. Szeregi Taylora i Maclaurina

Wewnątrz przedziału zbieżności suma szeregu potęgowego jest funkcją nieskończenie wiele razy różniczkowalną, a jej współczynniki określone są jednoznacznie przez wartości pochodnych w punkcie środkowym:
$$a_n = \frac{f^{(n)}(x_0)}{n!}$$

#### Kanoniczne rozwinięcia Maclaurina ($x_0 = 0$):
1. $$\frac{1}{1 - x} = \sum_{n=0}^\infty x^n = 1 + x + x^2 + \dots \quad (|x| < 1)$$
2. $$e^x = \sum_{n=0}^\infty \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \dots \quad (x \in \mathbb{R}, \ R = \infty)$$
3. $$\sin x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots \quad (x \in \mathbb{R}, \ R = \infty)$$
4. $$\cos x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots \quad (x \in \mathbb{R}, \ R = \infty)$$
5. $$\ln(1 + x) = \sum_{n=1}^\infty (-1)^{n-1} \frac{x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots \quad (x \in (-1, 1])$$
6. $$\operatorname{arctg} x = \sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots \quad (x \in [-1, 1])$$

---

## Rozdział 18: Trygonometryczne szeregi Fouriera

### 18.1. Układ ortogonalny funkcji trygonometrycznych

Rozważmy zbiór funkcji:
$$\{1, \cos x, \sin x, \cos(2x), \sin(2x), \dots, \cos(nx), \sin(nx), \dots\}$$
na przedziale $[-\pi, \pi]$. Zbiór ten tworzy układ ortogonalny ze standardowym iloczynem skalarnym $(f, g) = \int_{-\pi}^\pi f(x) g(x) dx$:

$$\int_{-\pi}^\pi \cos(nx) \cos(mx) \, dx = \begin{cases} 0 & n \neq m \\ \pi & n = m \ge 1 \\ 2\pi & n = m = 0 \end{cases}$$
$$\int_{-\pi}^\pi \sin(nx) \sin(mx) \, dx = \begin{cases} 0 & n \neq m \\ \pi & n = m \ge 1 \end{cases}$$
$$\int_{-\pi}^\pi \sin(nx) \cos(mx) \, dx = 0 \quad \text{dla wszystkich } n, m$$

---

### 18.2. Rzeczywisty szereg Fouriera

Niech funkcja $f: [-\pi, \pi] \to \mathbb{R}$ będzie całkowalna. **Szeregiem Fouriera** funkcji $f$ nazywamy szereg trygonometryczny:
$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty \big( a_n \cos(nx) + b_n \sin(nx) \big)$$
gdzie współczynniki Eulera-Fouriera określone są wzorami:
$$a_0 = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \, dx$$
$$a_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \cos(nx) \, dx \quad (n \ge 1)$$
$$b_n = \frac{1}{\pi} \int_{-\pi}^\pi f(x) \sin(nx) \, dx \quad (n \ge 1)$$

#### Uogólnienie na dowolny przedział $[-L, L]$ (okres $T = 2L$):
$$f(x) \sim \frac{a_0}{2} + \sum_{n=1}^\infty \left( a_n \cos\frac{n\pi x}{L} + b_n \sin\frac{n\pi x}{L} \right)$$
$$a_n = \frac{1}{L} \int_{-L}^L f(x) \cos\frac{n\pi x}{L} \, dx, \quad b_n = \frac{1}{L} \int_{-L}^L f(x) \sin\frac{n\pi x}{L} \, dx$$

#### Uproszczenia ze względu na parzystość:
- Jeżeli $f(x)$ jest **parzysta** ($f(-x) = f(x)$):
  $$b_n = 0 \quad \text{dla wszystkich } n \ge 1, \quad a_n = \frac{2}{L} \int_0^L f(x) \cos\frac{n\pi x}{L} \, dx$$
  (szereg zawiera wyłącznie cosinusy).
- Jeżeli $f(x)$ jest **nieparzysta** ($f(-x) = -f(x)$):
  $$a_n = 0 \quad \text{dla wszystkich } n \ge 0, \quad b_n = \frac{2}{L} \int_0^L f(x) \sin\frac{n\pi x}{L} \, dx$$
  (szereg zawiera wyłącznie sinusy).

---

### 18.3. Warunki Dirichleta zbieżności szeregu Fouriera

> **Twierdzenie 18.1 (Dirichleta):**
> Jeżeli funkcja okresowa $f$ o okresie $T = 2\pi$ spełnia w przedziale $[-\pi, \pi]$ **warunki Dirichleta**:
> 1. jest przedziałami ciągła (posiada co najwyżej skończoną liczbę punktów nieciągłości I rodzaju),
> 2. jest przedziałami monotoniczna (posiada co najwyżej skończoną liczbę ekstremów lokalnych),
> to szereg Fouriera funkcji $f$ jest zbieżny w każdym punkcie $x \in \mathbb{R}$, przy czym jego suma $S(x)$ wynosi:
> - $S(x) = f(x)$ w każdym punkcie ciągłości funkcji,
> - $S(x) = \frac{f(x^+) + f(x^-)}{2}$ w każdym punkcie skoku (średnia arytmetyczna granic jednostronnych).

#### Zjawisko Gibbsa:
W otoczeniu punktów skokowych sumy częściowe szeregu Fouriera wykazują charakterystyczne oscylacje („przeregulowanie”), których amplituda nie zmierza do zera przy $n \to \infty$, lecz wynosi w granicy ok. $8{,}95\%$ wielkości skoku. Jest to zjawisko kluczowe przy projektowaniu filtrów cyfrowych (zjawisko tętnień pasmowych).

---

### 18.4. Zespolona postać szeregu Fouriera i tożsamość Parsevala

Wykorzystując wzory Eulera $\cos(nx) = \frac{e^{inx} + e^{-inx}}{2}$, szereg Fouriera można zapisać w zwartej postaci zespolonej, preferowanej w telekomunikacji i przetwarzaniu sygnałów:

$$f(t) = \sum_{n=-\infty}^{+\infty} c_n e^{j n \omega_0 t}, \quad \omega_0 = \frac{2\pi}{T}$$
gdzie **widmo zespolone sygnału** stanowią współczynniki:
$$c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(t) e^{-j n \omega_0 t} \, dt$$

Związek ze współczynnikami rzeczywistymi:
$$c_0 = \frac{a_0}{2}, \quad c_n = \frac{a_n - j b_n}{2}, \quad c_{-n} = \bar{c}_n$$

> **Twierdzenie 18.2 (Tożsamość Parsevala - Bilans mocy sygnału):**
> Dla sygnału okresowego o okresie $T$:
> $$\frac{1}{T} \int_0^T f^2(t) \, dt = \sum_{n=-\infty}^{+\infty} |c_n|^2 = \frac{a_0^2}{4} + \frac{1}{2}\sum_{n=1}^\infty (a_n^2 + b_n^2)$$
> Całkowita moc średnia sygnału jest równa sumie mocy poszczególnych składowych harmonicznych.

---

### 18.5. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 8.1: Wyznaczanie promienia i przedziału zbieżności
Wyznacz przedział zbieżności szeregu potęgowego:
$$\sum_{n=1}^\infty \frac{(x - 2)^n}{n \cdot 3^n}$$

**Rozwiązanie:**
Środek szeregu to $x_0 = 2$. Współczynniki: $a_n = \frac{1}{n \cdot 3^n}$.  
Obliczamy promień zbieżności ze wzoru d'Alemberta:
$$R = \lim_{n \to \infty} \left| \frac{a_n}{a_{n+1}} \right| = \lim_{n \to \infty} \frac{\frac{1}{n \cdot 3^n}}{\frac{1}{(n+1) \cdot 3^{n+1}}} = \lim_{n \to \infty} \frac{n+1}{n} \cdot \frac{3^{n+1}}{3^n} = 1 \cdot 3 = 3$$
Zatem wnętrzem przedziału zbieżności jest:
$$|x - 2| < 3 \iff -3 < x - 2 < 3 \iff -1 < x < 5$$
Badamy zbieżność na końcach przedziału:
1. **Dla $x = 5$:**  
   $$\sum_{n=1}^\infty \frac{(5 - 2)^n}{n \cdot 3^n} = \sum_{n=1}^\infty \frac{3^n}{n \cdot 3^n} = \sum_{n=1}^\infty \frac{1}{n}$$
   Jest to rozbieżny szereg harmoniczny ($\alpha = 1$). Zatem punkt $x = 5$ nie należy do przedziału zbieżności.
2. **Dla $x = -1$:**  
   $$\sum_{n=1}^\infty \frac{(-1 - 2)^n}{n \cdot 3^n} = \sum_{n=1}^\infty \frac{(-3)^n}{n \cdot 3^n} = \sum_{n=1}^\infty \frac{(-1)^n}{n}$$
   Jest to szereg naprzemienny zbieżny na mocy kryterium Leibniza (szereg anharmoniczny). Punkt $x = -1$ należy do przedziału zbieżności.

**Odpowiedź:** Przedział zbieżności szeregu wynosi:
$$x \in [-1, 5)$$

---

#### Przykład 8.2: Rozwinięcie fali prostokątnej w szereg Fouriera (klasyk WEiTI)
Wyznacz szereg Fouriera dla symetrycznego sygnału prostokątnego (fala zegarowa):
$$f(x) = \begin{cases} -1 & \text{dla } -\pi < x < 0 \\ 1 & \text{dla } 0 < x < \pi \end{cases}, \quad f(x + 2\pi) = f(x)$$

**Rozwiązanie:**
1. **Analiza parzystości:**  
   Funkcja $f(x)$ jest nieparzysta: $f(-x) = -f(x)$.  
   Wszystkie współczynniki cosinusowe znikają:
   $$a_n = 0 \quad \text{dla } n \ge 0$$
2. **Współczynniki sinusowe $b_n$:**
   $$b_n = \frac{2}{\pi} \int_0^\pi f(x) \sin(nx) \, dx = \frac{2}{\pi} \int_0^\pi 1 \cdot \sin(nx) \, dx = \frac{2}{\pi} \left[ -\frac{\cos(nx)}{n} \right]_0^\pi = \frac{2}{n\pi} \big( 1 - \cos(n\pi) \big)$$
   Zauważmy, że $\cos(n\pi) = (-1)^n$:
   - Dla $n$ parzystych ($n = 2k$): $1 - (-1)^{2k} = 1 - 1 = 0 \implies b_{2k} = 0$.
   - Dla $n$ nieparzystych ($n = 2k-1$): $1 - (-1)^{2k-1} = 1 - (-1) = 2 \implies b_{2k-1} = \frac{4}{(2k-1)\pi}$.
3. **Postać szeregu Fouriera:**
   $$f(x) \sim \frac{4}{\pi} \sum_{k=1}^\infty \frac{\sin\big((2k-1)x\big)}{2k - 1} = \frac{4}{\pi} \left( \sin x + \frac{\sin(3x)}{3} + \frac{\sin(5x)}{5} + \dots \right)$$

#### Wniosek inżynierski:
Fala prostokątna składa się wyłącznie z **harmonicznych nieparzystych** (1., 3., 5., itd.), a amplituda kolejnych harmonicznych maleje odwrotnie proporcjonalnie do ich rzędu ($1/n$). Przepuszczenie fali prostokątnej przez filtr pasmowo-zaporowy usuwający wyższe harmoniczne zamienia falę zegarową w sinusoidę o częstotliwości podstawowej.

---

### 18.6. Zadania do samodzielnego rozwiązania

1. **Zadanie 8.1:** Wyznacz przedział zbieżności szeregu potęgowego: $\sum_{n=1}^\infty \frac{2^n}{n^2} x^n$.
2. **Zadanie 8.2:** Oblicz sumę szeregu $\sum_{n=1}^\infty \frac{n}{3^n}$ za pomocą różniczkowania szeregu potęgowego.
3. **Zadanie 8.3:** Rozwiń funkcję $f(x) = |x|$ w przedziale $[-\pi, \pi]$ w szereg Fouriera.
4. **Zadanie 8.4:** Korzystając z rozwinięcia z zadania 8.3, oblicz sumę szeregu liczbowego: $\sum_{k=0}^\infty \frac{1}{(2k+1)^2} = 1 + \frac{1}{9} + \frac{1}{25} + \dots$.
5. **Zadanie 8.5 (Zastosowanie tożsamości Parsevala):** Wykorzystaj tożsamość Parsevala dla fali prostokątnej z Przykładu 8.2 do obliczenia sumy szeregu $\sum_{k=1}^\infty \frac{1}{(2k-1)^2}$.

---

### Odpowiedzi i wskazówki do zadań

- **8.1:** Promień $R = \lim \frac{2^n/n^2}{2^{n+1}/(n+1)^2} = \frac{1}{2}$. Na końcach $x = \pm 1/2$ otrzymujemy szeregi $\sum \frac{(\pm 1)^n}{n^2}$, które są bezwzględnie zbieżne ($\alpha = 2 > 1$). Zatem przedział zbieżności to przedział domknięty: $x \in \left[ -\frac{1}{2}, \frac{1}{2} \right]$.
- **8.2:** Szereg geometryczny: $\sum_{n=0}^\infty x^n = \frac{1}{1-x}$. Różniczkując obustronnie: $\sum_{n=1}^\infty n x^{n-1} = \frac{1}{(1-x)^2}$. Mnożąc przez $x$: $\sum_{n=1}^\infty n x^n = \frac{x}{(1-x)^2}$. Dla $x = \frac{1}{3}$: suma wynosi $\frac{1/3}{(1 - 1/3)^2} = \frac{1/3}{4/9} = \frac{3}{4}$.
- **8.3:** Funkcja jest parzysta ($b_n = 0$). $a_0 = \frac{2}{\pi} \int_0^\pi x dx = \pi$. $a_n = \frac{2}{\pi} \int_0^\pi x \cos(nx) dx = \frac{2}{\pi n^2} ((-1)^n - 1) = \begin{cases} 0 & n = 2k \\ -\frac{4}{\pi(2k-1)^2} & n = 2k-1 \end{cases}$. Rozwinięcie: $|x| = \frac{\pi}{2} - \frac{4}{\pi} \sum_{k=1}^\infty \frac{\cos((2k-1)x)}{(2k-1)^2}$.
- **8.4:** Podstawiając $x = 0$ do rozwinięcia: $0 = \frac{\pi}{2} - \frac{4}{\pi} \sum_{k=1}^\infty \frac{1}{(2k-1)^2} \implies \sum_{k=1}^\infty \frac{1}{(2k-1)^2} = \frac{\pi^2}{8}$.
- **8.5:** Średnia moc fali prostokątnej: $\frac{1}{2\pi} \int_{-\pi}^\pi 1^2 dx = 1$. Z tożsamości Parsevala: $1 = \frac{1}{2} \sum_{k=1}^\infty b_{2k-1}^2 = \frac{1}{2} \sum_{k=1}^\infty \left( \frac{4}{(2k-1)\pi} \right)^2 = \frac{8}{\pi^2} \sum_{k=1}^\infty \frac{1}{(2k-1)^2} \implies \sum_{k=1}^\infty \frac{1}{(2k-1)^2} = \frac{\pi^2}{8}$. Wynik jest w pełni spójny!


\newpage

