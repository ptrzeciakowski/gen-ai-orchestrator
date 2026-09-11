# Część III: Szeregi Liczbowe

Szereg liczbowy jest formalnym uogólnieniem operacji dodawania na nieskończoną liczbę składników. W naukach inżynierskich szeregi stanowią podstawowe narzędzie aproksymacji sygnałów ciągłych, dyskretyzacji i obliczeń zmiennoprzecinkowych, konstrukcji funkcji specjalnych (Bessela, Neumanna), a także badania stabilności i transmitancji układów automatyki i telekomunikacji.

---

## Rozdział 5: Szeregi o wyrazach nieujemnych

### 5.1. Definicja szeregu, zbieżności i reszty

#### Definicja 5.1 (Szereg liczbowy i suma częściowa)
Niech dany będzie ciąg liczb rzeczywistych $(a_n)_{n=1}^\infty$. Formalne wyrażenie postaci:
$$\sum_{n=1}^\infty a_n = a_1 + a_2 + a_3 + \dots + a_n + \dots$$
nazywamy **szeregiem liczbowym**, a liczby $a_n$ jego **wyrazami**.

Ciąg $(S_n)_{n=1}^\infty$, którego $n$-ty wyraz określony jest wzorem:
$$S_n = \sum_{k=1}^n a_k = a_1 + a_2 + \dots + a_n$$
nazywamy **ciągiem sum częściowych** szeregu.

#### Definicja 5.2 (Zbieżność i suma szeregu)
1. Jeżeli ciąg sum częściowych $(S_n)$ posiada granicę właściwą:
   $$S = \lim_{n \to \infty} S_n \in \mathbb{R}$$
   to mówimy, że szereg $\sum_{n=1}^\infty a_n$ jest **zbieżny**, a liczbę $S$ nazywamy **sumą szeregu**, co zapisujemy:
   $$\sum_{n=1}^\infty a_n = S$$
2. Jeżeli ciąg $(S_n)$ nie posiada granicy właściwej (dąży do $+\infty$, $-\infty$ lub granica nie istnieje), to szereg nazywamy **rozbieżnym**.

#### Definicja 5.3 (Reszta szeregu)
Dla szeregu zbieżnego o sumie $S$, wyrażenie:
$$R_n = S - S_n = \sum_{k=n+1}^\infty a_k$$
nazywamy **$n$-tą resztą szeregu** (błędem odcięcia sumowania na $n$-tym wyrazie). Z definicji granicy wynika natychmiast:
$$\lim_{n \to \infty} R_n = \lim_{n \to \infty} (S - S_n) = S - S = 0$$

---

### 5.2. Warunek konieczny zbieżności szeregu

> **Twierdzenie 5.1 (Warunek konieczny zbieżności szeregu):**
> Jeżeli szereg liczbowy $\sum_{n=1}^\infty a_n$ jest zbieżny, to jego wyraz ogólny dąży do zera:
> $$\lim_{n \to \infty} a_n = 0$$

**Dowód:**
Zauważmy, że dla każdego $n \ge 2$ zachodzi tożsamość:
$$a_n = S_n - S_{n-1}$$
Ponieważ szereg jest zbieżny do sumy $S$, ciąg sum częściowych spełnia $\lim_{n \to \infty} S_n = S$.  
Podciąg przesunięty $(S_{n-1})$ również spełnia $\lim_{n \to \infty} S_{n-1} = S$.  
Z twierdzenia o granicy różnicy ciągów (Tw. 4.1):
$$\lim_{n \to \infty} a_n = \lim_{n \to \infty} (S_n - S_{n-1}) = \lim_{n \to \infty} S_n - \lim_{n \to \infty} S_{n-1} = S - S = 0 \quad \blacksquare$$

> **Kluczowa uwaga metodyczna:**
> Warunek $\lim_{n \to \infty} a_n = 0$ jest warunkiem **koniecznym**, lecz **niewystarczającym**! Istnieją szeregi o wyrazach zmierzających do zera, które są rozbieżne.

#### Klasyczny kontrprzykład: Szereg harmoniczny
Rozpatrzmy szereg:
$$\sum_{n=1}^\infty \frac{1}{n} = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots$$
Wyraz ogólny spełnia warunek konieczny: $\lim_{n \to \infty} \frac{1}{n} = 0$.  
Jednak grupując wyrazy w potęgi dwójki (sposób Mikołaja z Oresme, XIV w.):
$$S_{2^k} = 1 + \frac{1}{2} + \left( \frac{1}{3} + \frac{1}{4} \right) + \left( \frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} \right) + \dots + \left( \frac{1}{2^{k-1}+1} + \dots + \frac{1}{2^k} \right)$$
Zauważmy oszacowanie:
$$\frac{1}{3} + \frac{1}{4} > \frac{1}{4} + \frac{1}{4} = \frac{1}{2}$$
$$\frac{1}{5} + \frac{1}{6} + \frac{1}{7} + \frac{1}{8} > 4 \cdot \frac{1}{8} = \frac{1}{2}$$
Ogólnie każda z $k$ grup o długości $2^{j-1}$ spełnia:
$$\sum_{m=2^{j-1}+1}^{2^j} \frac{1}{m} > 2^{j-1} \cdot \frac{1}{2^j} = \frac{1}{2}$$
Zatem suma częściowa:
$$S_{2^k} > 1 + \frac{1}{2} + \underbrace{\frac{1}{2} + \frac{1}{2} + \dots + \frac{1}{2}}_{k-1 \text{ razy}} = 1 + \frac{k}{2} \xrightarrow[k \to \infty]{} +\infty$$
Ciąg sum częściowych jest nieograniczony z góry, co oznacza, że szereg harmoniczny jest **rozbieżny do $+\infty$**.

---

### 5.3. Szereg geometryczny

Rozważmy szereg geometryczny o ilorazie $q \in \mathbb{R}$:
$$\sum_{n=0}^\infty q^n = 1 + q + q^2 + q^3 + \dots$$

Dla $q \neq 1$ suma pierwszych $n$ wyrazów wynosi:
$$S_n = \sum_{k=0}^{n-1} q^k = \frac{1 - q^n}{1 - q}$$

Badając granicę $\lim_{n \to \infty} S_n$:
1. Dla $|q| < 1$: $\lim_{n \to \infty} q^n = 0$, co daje:
   $$\sum_{n=0}^\infty q^n = \frac{1}{1 - q}$$
2. Dla $|q| \ge 1$: wyraz ogólny nie zmierza do zera ($\lim q^n \neq 0$), więc szereg jest rozbieżny.

---

### 5.4. Kryteria porównawcze dla szeregów o wyrazach nieujemnych

Jeżeli $a_n \ge 0$ dla każdego $n$, to ciąg sum częściowych jest niemalejący:
$$S_{n+1} = S_n + a_{n+1} \ge S_n$$
Z Twierdzenia Weierstrassa o monotoniczności (Tw. 4.4) wynika fundamentalny fakt:
> Szereg o wyrazach nieujemnych jest zbieżny wtedy i tylko wtedy, gdy ciąg jego sum częściowych jest ograniczony z góry.

#### Twierdzenie 5.2 (Kryterium porównawcze zwykłe)
Niech $0 \le a_n \le b_n$ dla wszystkich $n > N_0$:
1. Jeżeli szereg większy (majoranta) $\sum_{n=1}^\infty b_n$ jest **zbieżny**, to szereg mniejszy $\sum_{n=1}^\infty a_n$ jest również **zbieżny**.
2. Jeżeli szereg mniejszy (minoranta) $\sum_{n=1}^\infty a_n$ jest **rozbieżny**, to szereg większy $\sum_{n=1}^\infty b_n$ jest również **rozbieżny**.

**Dowód:**
Niech $S_n = \sum_{k=1}^n a_k$ oraz $T_n = \sum_{k=1}^n b_k$. Dla $n > N_0$ zachodzi $S_n \le T_n + C$ dla pewnej stałej $C$.  
Jeżeli $\sum b_n$ jest zbieżny do $T$, to $T_n \le T$, skąd $S_n \le T + C$, czyli ciąg $(S_n)$ jest ograniczony z góry. Będąc niemalejącym, jest zbieżny.  
Jeżeli $\sum a_n$ jest rozbieżny, to $S_n \to +\infty$, stąd $T_n \to +\infty$, czyli $\sum b_n$ jest rozbieżny. $\blacksquare$

#### Twierdzenie 5.3 (Kryterium porównawcze ilorazowe / graniczne)
Niech $a_n > 0$ oraz $b_n > 0$ od pewnego miejsca $N_0$. Załóżmy, że istnieje granica właściwa:
$$k = \lim_{n \to \infty} \frac{a_n}{b_n}$$
1. Jeżeli $k \in (0, +\infty)$, to szeregi $\sum a_n$ oraz $\sum b_n$ są **jednocześnie zbieżne** albo **jednocześnie rozbieżne**.
2. Jeżeli $k = 0$ oraz $\sum b_n$ jest zbieżny, to $\sum a_n$ jest zbieżny.
3. Jeżeli $k = +\infty$ oraz $\sum b_n$ jest rozbieżny, to $\sum a_n$ jest rozbieżny.

**Dowód punktu 1:**
Dla $k > 0$ wybierzmy $\varepsilon = \frac{k}{2} > 0$. Z definicji granicy od pewnego miejsca $N$:
$$\left| \frac{a_n}{b_n} - k \right| < \frac{k}{2} \iff \frac{k}{2} < \frac{a_n}{b_n} < \frac{3k}{2} \iff \frac{k}{2} b_n < a_n < \frac{3k}{2} b_n$$
Stosując zwykłe kryterium porównawcze (Tw. 5.2) do lewej i prawej nierówności, uzyskujemy natychmiast równoważność zbieżności obu szeregów. $\blacksquare$

---

### 5.5. Kryteria d'Alemberta i Cauchy'ego

> **Twierdzenie 5.4 (Kryterium d'Alemberta - ilorazowe):**
> Niech $a_n > 0$. Załóżmy, że istnieje granica:
> $$D = \lim_{n \to \infty} \frac{a_{n+1}}{a_n}$$
> 1. Jeżeli $D < 1$, to szereg $\sum_{n=1}^\infty a_n$ jest **zbieżny**.
> 2. Jeżeli $D > 1$, to $\lim a_n \neq 0$ i szereg $\sum_{n=1}^\infty a_n$ jest **rozbieżny**.
> 3. Jeżeli $D = 1$, to kryterium nie rozstrzyga o zbieżności.

> **Twierdzenie 5.5 (Kryterium Cauchy'ego - pierwiastkowe):**
> Niech $a_n \ge 0$. Załóżmy, że istnieje granica:
> $$C = \lim_{n \to \infty} \sqrt[n]{a_n}$$
> 1. Jeżeli $C < 1$, to szereg $\sum_{n=1}^\infty a_n$ jest **zbieżny**.
> 2. Jeżeli $C > 1$, to szereg $\sum_{n=1}^\infty a_n$ jest **rozbieżny**.
> 3. Jeżeli $C = 1$, to kryterium nie rozstrzyga o zbieżności.

> **Twierdzenie 5.6 (Relacja siły kryteriów Cauchy'ego i d'Alemberta):**
> Dla dowolnego ciągu liczb dodatnich $(a_n)$ zachodzi nierówność:
> $$\liminf_{n \to \infty} \frac{a_{n+1}}{a_n} \le \liminf_{n \to \infty} \sqrt[n]{a_n} \le \limsup_{n \to \infty} \sqrt[n]{a_n} \le \limsup_{n \to \infty} \frac{a_{n+1}}{a_n}$$
> Oznacza to, że kryterium Cauchy'ego jest **ściśle silniejsze** od kryterium d'Alemberta: ilekroć kryterium d'Alemberta rozstrzyga o zbieżności, kryterium Cauchy'ego również rozstrzyga i daje tę samą granicę ($C = D$), lecz istnieją szeregi, dla których kryterium Cauchy'ego rozstrzyga, a iloraz d'Alemberta nie posiada granicy.

---

### 5.6. Kryterium zagęszczające Cauchy'ego i szereg harmoniczny rzędu $\alpha$

> **Twierdzenie 5.7 (Kryterium kondensacyjne Cauchy'ego):**
> Niech ciąg $(a_n)$ będzie nierosnący i nieujemny ($a_1 \ge a_2 \ge a_3 \ge \dots \ge 0$). Wówczas szereg $\sum_{n=1}^\infty a_n$ jest zbieżny wtedy i tylko wtedy, gdy zbieżny jest szereg „zagęszczony”:
> $$\sum_{k=0}^\infty 2^k a_{2^k} = a_1 + 2a_2 + 4a_4 + 8a_8 + 16a_{16} + \dots$$

**Dowód:**
Grupując wyrazy:
$$S_{2^k-1} = a_1 + (a_2 + a_3) + (a_4 + a_5 + a_6 + a_7) + \dots + (a_{2^{k-1}} + \dots + a_{2^k-1})$$
Ponieważ ciąg jest nierosnący:
$$a_2 + a_3 \le 2a_2$$
$$a_4 + a_5 + a_6 + a_7 \le 4a_4$$
Stąd $S_{2^k-1} \le \sum_{j=0}^{k-1} 2^j a_{2^j}$. Zatem zbieżność szeregu zagęszczonego pociąga zbieżność szeregu wyjściowego.  
Z drugiej strony:
$$a_2 + a_3 \ge 2a_4$$
$$a_4 + a_5 + a_6 + a_7 \ge 4a_8$$
skąd $S_{2^k} \ge a_1 + a_2 + 2a_4 + \dots + 2^{k-1} a_{2^k} = \frac{1}{2} \sum_{j=0}^k 2^j a_{2^j}$, co dowodzi przeciwnej implikacji. $\blacksquare$

#### Zastosowanie: Szereg harmoniczny rzędu $\alpha$
Rozpatrzmy wzorcowy szereg:
$$\sum_{n=1}^\infty \frac{1}{n^\alpha}$$
Stosujemy kryterium kondensacyjne ($a_n = 1/n^\alpha$ jest malejący dla $\alpha > 0$):
$$\sum_{k=0}^\infty 2^k a_{2^k} = \sum_{k=0}^\infty 2^k \frac{1}{(2^k)^\alpha} = \sum_{k=0}^\infty 2^k \cdot 2^{-k\alpha} = \sum_{k=0}^\infty \left( 2^{1-\alpha} \right)^k$$
Otrzymaliśmy szereg geometryczny o ilorazie $q = 2^{1-\alpha}$.  
Szereg geometryczny jest zbieżny $\iff |q| < 1$:
$$2^{1-\alpha} < 1 \iff 1 - \alpha < 0 \iff \alpha > 1$$
Dla $\alpha \le 0$ warunek konieczny $\lim a_n = 0$ nie jest spełniony.  
Otrzymujemy fundamentalne twierdzenie:

> **Twierdzenie 5.8:**
> Szereg harmoniczny rzędu $\alpha$ $\sum_{n=1}^\infty \frac{1}{n^\alpha}$ jest:
> - **zbieżny** dla $\alpha > 1$,
> - **rozbieżny** dla $\alpha \le 1$.

---

### 5.7. Kryteria Raabego i całkowe Maclaurina-Cauchy'ego

Gdy kryteria d'Alemberta i Cauchy'ego zawodzą ($D = 1$ lub $C = 1$, co zachodzi dla wszystkich ułamków wymiernych), stosujemy kryteria drugiego rzędu.

> **Twierdzenie 5.9 (Kryterium Raabego):**
> Niech $a_n > 0$. Załóżmy, że istnieje granica:
> $$R = \lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right)$$
> 1. Jeżeli $R > 1$, to szereg $\sum a_n$ jest **zbieżny**.
> 2. Jeżeli $R < 1$, to szereg $\sum a_n$ jest **rozbieżny**.
> 3. Jeżeli $R = 1$, kryterium nie rozstrzyga.

> **Twierdzenie 5.10 (Kryterium całkowe Maclaurina-Cauchy'ego):**
> Jeżeli funkcja $f: [1, +\infty) \to [0, +\infty)$ jest ciągła i nierosnąca, a $a_n = f(n)$ dla każdego $n \in \mathbb{N}$, to szereg $\sum_{n=1}^\infty a_n$ oraz całka niewłaściwa $\int_1^{+\infty} f(x) \, dx$ są **jednocześnie zbieżne** albo **jednocześnie rozbieżne**.  
> Ponadto błąd reszty spełnia oszacowanie:
> $$\int_{n+1}^{+\infty} f(x) \, dx \le R_n = \sum_{k=n+1}^\infty a_k \le \int_n^{+\infty} f(x) \, dx$$

---

## Rozdział 6: Szeregi o wyrazach dowolnych i zespolonych

### 6.1. Zbieżność bezwzględna i warunkowa

Gdy wyrazy szeregu przyjmują dowolne znaki rzeczywiste (lub wartości z ciała $\mathbb{C}$), wprowadzamy podział na zbieżność bezwzględną i warunkową.

#### Definicja 6.1
1. Szereg $\sum_{n=1}^\infty a_n$ nazywamy **bezwzględnie zbieżnym**, jeżeli zbieżny jest szereg utworzony z wartości bezwzględnych jego wyrazów:
   $$\sum_{n=1}^\infty |a_n| < \infty$$
2. Szereg nazywamy **warunkowo zbieżnym**, jeżeli jest zbieżny, lecz nie jest bezwzględnie zbieżny (tzn. $\sum a_n$ jest zbieżny, ale $\sum |a_n| = +\infty$).

> **Twierdzenie 6.1:**
> Każdy szereg bezwzględnie zbieżny jest zbieżny w zwykłym sensie.

**Dowód:**
Skorzystamy z kryterium zbieżności Cauchy'ego (Tw. 3.7).  
Dla dowolnych wskaźników $m > n$, stosując nierówność trójkąta (Tw. 1.8):
$$\left| \sum_{k=n+1}^m a_k \right| \le \sum_{k=n+1}^m |a_k|$$
Ponieważ szereg $\sum |a_n|$ jest zbieżny, z kryterium Cauchy'ego dla zadanego $\varepsilon > 0$ istnieje $N$ takie, że dla $m > n > N$: $\sum_{k=n+1}^m |a_k| < \varepsilon$.  
Wtedy również:
$$\left| S_m - S_n \right| = \left| \sum_{k=n+1}^m a_k \right| < \varepsilon$$
Ciąg sum częściowych $(S_n)$ spełnia warunek Cauchy'ego w $\mathbb{R}$, jest zatem zbieżny. $\blacksquare$

---

### 6.2. Szeregi naprzemienne i kryterium Leibniza

Szeregiem naprzemiennym nazywamy szereg postaci:
$$\sum_{n=1}^\infty (-1)^{n+1} b_n = b_1 - b_2 + b_3 - b_4 + \dots, \quad b_n > 0$$

> **Twierdzenie 6.2 (Kryterium Leibniza dla szeregów naprzemiennych):**
> Jeżeli ciąg dodatni $(b_n)$ spełnia dwa warunki:
> 1. jest nierosnący: $\forall_{n \in \mathbb{N}} \ b_{n+1} \le b_n$,
> 2. zmierza do zera: $\lim_{n \to \infty} b_n = 0$,
> to szereg naprzemienny $\sum_{n=1}^\infty (-1)^{n+1} b_n$ jest **zbieżny**.
> Suma szeregu spełnia $0 \le S \le b_1$, a błąd odcięcia (reszta) spełnia:
> $$|R_n| = |S - S_n| \le b_{n+1}$$

**Dowód:**
Rozpatrzmy podciąg sum częściowych o wskaźnikach parzystych:
$$S_{2n} = (b_1 - b_2) + (b_3 - b_4) + \dots + (b_{2n-1} - b_{2n})$$
Ponieważ $b_k - b_{k+1} \ge 0$, ciąg $(S_{2n})$ jest niemalejący.  
Ponadto:
$$S_{2n} = b_1 - (b_2 - b_3) - (b_4 - b_5) - \dots - (b_{2n-2} - b_{2n-1}) - b_{2n} \le b_1$$
Ciąg $(S_{2n})$ jest niemalejący i ograniczony z góry przez $b_1$, zatem z twierdzenia Weierstrassa posiada granicę właściwą $S = \lim_{n \to \infty} S_{2n} \le b_1$.  
Badamy sumy częściowe o wskaźnikach nieparzystych:
$$S_{2n+1} = S_{2n} + b_{2n+1}$$
Przechodząc do granicy:
$$\lim_{n \to \infty} S_{2n+1} = \lim_{n \to \infty} S_{2n} + \lim_{n \to \infty} b_{2n+1} = S + 0 = S$$
Ponieważ oba podciągi parzysty i nieparzysty zmierzają do tej samej granicy $S$, cały ciąg sum częściowych jest zbieżny: $\lim_{n \to \infty} S_n = S$. $\blacksquare$

---

### 6.3. Kryteria Dirichleta i Abla

Do badania zbieżności szeregów iloczynowych postaci $\sum_{n=1}^\infty a_n b_n$ służy tożsamość Abela (dyskretne całkowanie przez części).

#### Lemat 6.1 (Przekształcenie Abela)
Niech $A_n = \sum_{k=1}^n a_k$ oznacza sumę częściową ciągu $(a_n)$ (przyjmując $A_0 = 0$). Wtedy:
$$\sum_{k=1}^n a_k b_k = A_n b_n - \sum_{k=1}^{n-1} A_k (b_{k+1} - b_k) = A_n b_{n+1} - \sum_{k=1}^n A_k (b_{k+1} - b_k)$$

> **Twierdzenie 6.3 (Kryterium Dirichleta):**
> Jeżeli sumy częściowe $A_n = \sum_{k=1}^n a_k$ są wspólnie ograniczone ($\exists_{M > 0} \forall_n \ |A_n| \le M$), a ciąg $(b_n)$ jest monotoniczny i dąży do zera ($\lim b_n = 0$), to szereg $\sum_{n=1}^\infty a_n b_n$ jest **zbieżny**.

> **Twierdzenie 6.4 (Kryterium Abla):**
> Jeżeli szereg $\sum a_n$ jest zbieżny, a ciąg $(b_n)$ jest monotoniczny i ograniczony, to szereg $\sum_{n=1}^\infty a_n b_n$ jest **zbieżny**.

#### Zastosowanie inżynierskie:
Kryterium Dirichleta pozwala rozstrzygać zbieżność szeregów trygonometrycznych:
$$\sum_{n=1}^\infty \frac{\sin(nx)}{n^\alpha}, \quad \sum_{n=1}^\infty \frac{\cos(nx)}{n^\alpha} \quad (\alpha > 0, \ x \neq 2k\pi)$$
ponieważ sumy częściowe $\sum_{k=1}^n \sin(kx) = \frac{\cos(x/2) - \cos((n+1/2)x)}{2\sin(x/2)}$ są wspólnie ograniczone przez $\frac{1}{|\sin(x/2)|}$.

---

### 6.4. Twierdzenie Riemanna o permutacjach i iloczyn Cauchy'ego

> **Twierdzenie 6.5 (O przemienności szeregów bezwzględnie zbieżnych):**
> Jeżeli szereg $\sum a_n$ jest bezwzględnie zbieżny do sumy $S$, to dowolny szereg powstały przez permutację jego wyrazów $\sum a_{\sigma(n)}$ jest również bezwzględnie zbieżny i jego suma wynosi dokładnie $S$.

> **Twierdzenie 6.6 (Riemanna o szeregach warunkowo zbieżnych):**
> Jeżeli szereg $\sum a_n$ jest zbieżny warunkowo, to dla dowolnej liczby $M \in \mathbb{R} \cup \{-\infty, +\infty\}$ istnieje taka permutacja $\sigma: \mathbb{N} \to \mathbb{N}$, że:
> $$\sum_{n=1}^\infty a_{\sigma(n)} = M$$

#### Iloczyn Cauchy'ego szeregów:
**Iloczynem Cauchy'ego** szeregów $\sum_{n=0}^\infty a_n$ oraz $\sum_{n=0}^\infty b_n$ nazywamy szereg $\sum_{n=0}^\infty c_n$, gdzie:
$$c_n = \sum_{k=0}^n a_k b_{n-k} = a_0 b_n + a_1 b_{n-1} + \dots + a_n b_0$$

> **Twierdzenie 6.7 (Mertensa):**
> Jeżeli szeregi $\sum a_n$ i $\sum b_n$ są zbieżne do sum odpowiednio $A$ i $B$, przy czym co najmniej jeden z nich jest **bezwzględnie zbieżny**, to ich iloczyn Cauchy'ego $\sum c_n$ jest zbieżny i jego suma wynosi:
> $$\sum_{n=0}^\infty c_n = A \cdot B$$

---

### 6.5. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 3.1: Badanie zbieżności za pomocą kryterium Raabego
Zbadaj zbieżność szeregu:
$$\sum_{n=1}^\infty \frac{(2n-1)!!}{(2n)!!} \cdot \frac{1}{2n+1}$$

**Rozwiązanie:**
Zbadajmy najpierw iloraz d'Alemberta:
$$\frac{a_{n+1}}{a_n} = \frac{\frac{(2n+1)!!}{(2n+2)!!} \frac{1}{2n+3}}{\frac{(2n-1)!!}{(2n)!!} \frac{1}{2n+1}} = \frac{2n+1}{2n+2} \cdot \frac{2n+1}{2n+3} = \frac{4n^2 + 4n + 1}{4n^2 + 10n + 6}$$
Granica wynosi:
$$D = \lim_{n \to \infty} \frac{a_{n+1}}{a_n} = 1$$
Kryterium d'Alemberta nie rozstrzyga o zbieżności.  
Stosujemy kryterium Raabego (Tw. 5.9):
$$R = \lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right) = \lim_{n \to \infty} n \left( \frac{4n^2 + 10n + 6}{4n^2 + 4n + 1} - 1 \right) = \lim_{n \to \infty} n \left( \frac{6n + 5}{4n^2 + 4n + 1} \right) = \lim_{n \to \infty} \frac{6n^2 + 5n}{4n^2 + 4n + 1} = \frac{6}{4} = \frac{3}{2}$$
Ponieważ $R = \frac{3}{2} > 1$, na mocy kryterium Raabego szereg jest **zbieżny**.

---

#### Przykład 3.2: Szacowanie sumy i błędu reszty kryterium całkowym
Dla szeregu $\sum_{n=1}^\infty \frac{1}{n^3}$:
1. Udowodnij zbieżność za pomocą kryterium całkowego.
2. Oszacuj błąd przybliżenia sumy szeregu przez sumę pierwszych 10 wyrazów $S_{10}$.

**Rozwiązanie:**
1. Funkcja $f(x) = \frac{1}{x^3}$ jest ciągła, dodatnia i malejąca na $[1, +\infty)$. Całka niewłaściwa:
   $$\int_1^{+\infty} \frac{dx}{x^3} = \lim_{T \to \infty} \left[ -\frac{1}{2x^2} \right]_1^T = 0 - \left(-\frac{1}{2}\right) = \frac{1}{2} < \infty$$
   Całka jest zbieżna, zatem na mocy kryterium całkowego (Tw. 5.10) szereg jest zbieżny.
2. Stosujemy oszacowanie reszty z Twierdzenia 5.10 dla $n = 10$:
   $$\int_{11}^{+\infty} \frac{dx}{x^3} \le R_{10} \le \int_{10}^{+\infty} \frac{dx}{x^3}$$
   Obliczamy całki:
   $$\int_{10}^{+\infty} \frac{dx}{x^3} = \left[ -\frac{1}{2x^2} \right]_{10}^\infty = \frac{1}{2 \cdot 10^2} = \frac{1}{200} = 0{,}005$$
   $$\int_{11}^{+\infty} \frac{dx}{x^3} = \frac{1}{2 \cdot 11^2} = \frac{1}{242} \approx 0{,}00413$$
   Zatem błąd odcięcia spełnia wąskie oszacowanie:
   $$0{,}00413 \le R_{10} \le 0{,}005$$

---

#### Przykład 3.3: Iloczyn Cauchy'ego szeregów wykładniczych
Oblicz iloczyn Cauchy'ego dwóch szeregów $\sum_{n=0}^\infty \frac{x^n}{n!}$ oraz $\sum_{n=0}^\infty \frac{y^n}{n!}$ ($x, y \in \mathbb{R}$).

**Rozwiązanie:**
Oba szeregi są bezwzględnie zbieżne dla każdego $x, y \in \mathbb{R}$ (z kryterium d'Alemberta).  
Z twierdzenia Mertensa (Tw. 6.7) ich iloczyn Cauchy'ego $\sum c_n$ jest zbieżny.  
Wyznaczamy wyraz ogólny $c_n$:
$$c_n = \sum_{k=0}^n a_k b_{n-k} = \sum_{k=0}^n \frac{x^k}{k!} \frac{y^{n-k}}{(n-k)!} = \frac{1}{n!} \sum_{k=0}^n \frac{n!}{k!(n-k)!} x^k y^{n-k} = \frac{1}{n!} \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$$
Ze wzoru dwumianowego Newtona:
$$\sum_{k=0}^n \binom{n}{k} x^k y^{n-k} = (x + y)^n$$
Zatem:
$$c_n = \frac{(x + y)^n}{n!}$$
Suma iloczynu wynosi:
$$\sum_{n=0}^\infty c_n = \sum_{n=0}^\infty \frac{(x + y)^n}{n!}$$
Tożsamość ta dowodzi na gruncie teorii szeregów fundamentalnego prawa potęg funkcji wykładniczej:
$$e^x \cdot e^y = e^{x+y}$$

---

### 6.6. Zestaw zadań do samodzielnego rozwiązania

1. **Zadanie 3.1:** Zbadaj zbieżność szeregu: $\sum_{n=1}^\infty \frac{n!}{n^n}$.
2. **Zadanie 3.2:** Zbadaj zbieżność szeregu: $\sum_{n=2}^\infty \frac{1}{n \ln n \cdot (\ln(\ln n))^2}$.
3. **Zadanie 3.3:** Zbadaj zbieżność bezwzględną i warunkową szeregu: $\sum_{n=1}^\infty (-1)^n \left( \sqrt{n+1} - \sqrt{n} \right)$.
4. **Zadanie 3.4:** Zbadaj zbieżność szeregu: $\sum_{n=1}^\infty \frac{\cos(n\pi/3)}{\sqrt{n}}$ za pomocą kryterium Dirichleta.
5. **Zadanie 3.5:** Za pomocą kryterium Raabego zbadaj zbieżność szeregu: $\sum_{n=1}^\infty \frac{n! \cdot e^n}{n^{n+p}}$ w zależności od parametru rzeczywistego $p$.

---

### Odpowiedzi i wskazówki do zadań

- **3.1:** Stosujemy kryterium d'Alemberta: $\frac{a_{n+1}}{a_n} = \frac{(n+1)!}{(n+1)^{n+1}} \frac{n^n}{n!} = \left(\frac{n}{n+1}\right)^n = \left(1 + \frac{1}{n}\right)^{-n} \xrightarrow[n \to \infty]{} \frac{1}{e}$. Ponieważ $D = \frac{1}{e} \approx 0{,}368 < 1$, szereg jest **zbieżny**.
- **3.2:** Podstawienie w kryterium całkowym: $t = \ln(\ln x) \implies dt = \frac{dx}{x \ln x}$. Całka $\int \frac{dt}{t^2} = -\frac{1}{t}$ jest zbieżna w nieskończoności. Zatem szereg jest **zbieżny**.
- **3.3:** Mnożymy przez sprzężenie: $b_n = \sqrt{n+1} - \sqrt{n} = \frac{1}{\sqrt{n+1} + \sqrt{n}}$. Ciąg $b_n$ maleje do 0, więc z kryterium Leibniza szereg jest **zbieżny**. Szereg modułów $\sum b_n$ jest rozbieżny (porównanie ilorazowe z $1/\sqrt{n}$, $\alpha = 1/2 \le 1$). Zatem szereg jest **zbieżny warunkowo**.
- **3.4:** Sumy częściowe $\sum_{k=1}^n \cos(k\pi/3)$ są okresowe i ograniczone ($M \le 2$). Ciąg $b_n = \frac{1}{\sqrt{n}}$ maleje monotonicznie do 0. Na mocy kryterium Dirichleta szereg jest **zbieżny**.
- **3.5:** Iloraz: $\frac{a_n}{a_{n+1}} = \frac{1}{e} \left(1 + \frac{1}{n}\right)^{n+p}$. Rozwijając w szereg Taylora: $\left(1 + \frac{1}{n}\right)^{n+p} = e \left( 1 + \frac{p - 1/2}{n} + \mathcal{O}(1/n^2) \right)$. Granica Raabego: $R = \lim n \left( \frac{a_n}{a_{n+1}} - 1 \right) = p - \frac{1}{2}$. Szereg jest zbieżny dla $p > \frac{3}{2}$, a rozbieżny dla $p < \frac{3}{2}$.
