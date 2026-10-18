# Część II: Ciągi Liczbowe

Teoria ciągów liczbowych stanowi bramę do całej współczesnej analizy matematycznej. Pojęcie granicy ciągu jest pierwotnym pojęciem granicznym, na bazie którego definiuje się sumy szeregów nieskończonych, granice funkcji, ciągłość, różniczkowalność oraz całki Riemanna. W inżynierii informatycznej i elektronicznej ciąg liczbowy jest modelem **sygnału dyskretnego w czasie** $x[n]$ (próbkowanie), a granica opisuje stany ustalone w dyskretnych układach dynamicznych, filtrach cyfrowych oraz zbieżność algorytmów numerycznych.

---

## Rozdział 3: Granica ciągu liczbowego i topologia zbieżności

### 3.1. Podstawowe definicje i sposoby zadawania ciągów

#### Definicja 3.1 (Ciąg liczb rzeczywistych)
Ciągiem liczb rzeczywistych nazywamy funkcję odwzorowującą zbiór liczb naturalnych $\mathbb{N} = \{1, 2, 3, \dots\}$ w zbiór liczb rzeczywistych $\mathbb{R}$:
$$a: \mathbb{N} \to \mathbb{R}, \quad a(n) = a_n$$
Wartość $a_n$ nazywamy **$n$-tym wyrazem ciągu**, a sam ciąg oznaczamy symbolem $(a_n)_{n=1}^\infty$ lub krócej $(a_n)$.

Ciągi mogą być zadawane:
1. **Wzorem jawnym (analitycznym):** np. $a_n = \frac{3n^2 - 1}{2n^2 + 5}$,
2. **Równaniem różnicowym (rekurencyjnym):** z podaniem warunków początkowych, np.:
   $$a_1 = a, \quad a_{n+1} = f(a_n)$$
3. **Konstrukcją graniczną lub właściwościową.**

#### Definicja 3.2 (Ograniczoność ciągu)
1. Ciąg $(a_n)$ jest **ograniczony z góry**, jeżeli:
   $$\exists_{M \in \mathbb{R}} \forall_{n \in \mathbb{N}} \quad a_n \le M$$
2. Ciąg $(a_n)$ jest **ograniczony z dołu**, jeżeli:
   $$\exists_{m \in \mathbb{R}} \forall_{n \in \mathbb{N}} \quad a_n \ge m$$
3. Ciąg $(a_n)$ jest **ograniczony**, jeżeli jest ograniczony z góry i z dołu, co jest równoważne warunkowi:
   $$\exists_{K > 0} \forall_{n \in \mathbb{N}} \quad |a_n| \le K$$

#### Definicja 3.3 (Monotoniczność ciągu)
Ciąg $(a_n)$ nazywamy:
- **ściśle rosnącym:** $\forall_{n \in \mathbb{N}} \ a_{n+1} > a_n \iff a_{n+1} - a_n > 0$,
- **niemalejącym (słabo rosnącym):** $\forall_{n \in \mathbb{N}} \ a_{n+1} \ge a_n$,
- **ściśle malejącym:** $\forall_{n \in \mathbb{N}} \ a_{n+1} < a_n \iff a_{n+1} - a_n < 0$,
- **nierosnącym (słabo malejącym):** $\forall_{n \in \mathbb{N}} \ a_{n+1} \le a_n$.

---

### 3.2. Granica właściwa ciągu (Definicja Cauchy'ego $\varepsilon-N$)

#### Definicja 3.4 (Granica właściwa ciągu)
Liczbę $g \in \mathbb{R}$ nazywamy **granicą właściwą** ciągu $(a_n)$, co zapisujemy:
$$\lim_{n \to \infty} a_n = g \quad \text{lub} \quad a_n \xrightarrow[n \to \infty]{} g$$
jeżeli dla każdej liczby rzeczywistej $\varepsilon > 0$ istnieje wskaźnik naturalny $N \in \mathbb{N}$ (zależny od $\varepsilon$, $N = N(\varepsilon)$) taki, że dla każdego wskaźnika $n > N$ odległość wyrazu $a_n$ od liczby $g$ jest mniejsza od $\varepsilon$:

$$\forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{n \in \mathbb{N}} \quad \big( n > N \implies |a_n - g| < \varepsilon \big)$$

#### Interpretacja geometryczna i topologiczna:
Nierówność $|a_n - g| < \varepsilon$ jest równoważna relacji:
$$a_n \in (g - \varepsilon, \ g + \varepsilon) = U(g, \varepsilon)$$
Oznacza to, że:
> W dowolnie małym otoczeniu $U(g, \varepsilon)$ punktu $g$ znajdują się **prawie wszystkie** wyrazy ciągu (tzn. wszystkie poza co najwyżej skończoną liczbą wyrazów o wskaźnikach $n \le N$). Poza otoczeniem $U(g, \varepsilon)$ leżeć może co najwyżej $N$ początkowych elementów.

Ciąg posiadający granicę właściwą $g \in \mathbb{R}$ nazywamy **ciągiem zbieżnym**. Ciąg, który nie posiada granicy właściwej, nazywamy **ciągiem rozbieżnym**.

> **Twierdzenie 3.1 (Jedyność granicy ciągu):**
> Każdy ciąg zbieżny posiada dokładnie jedną granicę.

**Dowód (nie wprost):**
Załóżmy, że ciąg $(a_n)$ posiada dwie różne granice $g_1, g_2 \in \mathbb{R}$, przy czym $g_1 \neq g_2$. Wtedy odległość $d = |g_1 - g_2| > 0$.  
Wybierzmy promień otoczenia $\varepsilon = \frac{d}{2} = \frac{|g_1 - g_2|}{2} > 0$.
- Z faktu, że $\lim a_n = g_1$: $\exists_{N_1 \in \mathbb{N}} \forall_{n > N_1} \ |a_n - g_1| < \varepsilon$,
- Z faktu, że $\lim a_n = g_2$: $\exists_{N_2 \in \mathbb{N}} \forall_{n > N_2} \ |a_n - g_2| < \varepsilon$.

Niech $N = \max(N_1, N_2)$. Dla dowolnego wskaźnika $n > N$, stosując nierówność trójkąta (Tw. 1.8):
$$|g_1 - g_2| = |(g_1 - a_n) + (a_n - g_2)| \le |g_1 - a_n| + |a_n - g_2| < \varepsilon + \varepsilon = 2\varepsilon$$
Wstawiając $\varepsilon = \frac{|g_1 - g_2|}{2}$:
$$|g_1 - g_2| < |g_1 - g_2|$$
Otrzymana sprzeczność dowodzi, że $g_1 = g_2$. Granica ciągu jest wyznaczona jednoznacznie. $\blacksquare$

> **Twierdzenie 3.2 (Ograniczoność ciągu zbieżnego):**
> Każdy ciąg zbieżny jest ograniczony.

**Dowód:**
Niech $\lim_{n \to \infty} a_n = g$. Z definicji granicy dla $\varepsilon = 1$ istnieje wskaźnik $N \in \mathbb{N}$ taki, że dla wszystkich $n > N$:
$$|a_n - g| < 1 \implies g - 1 < a_n < g + 1$$
Zdefiniujmy liczby:
$$m = \min\big(a_1, a_2, \dots, a_N, \ g - 1\big), \quad M = \max\big(a_1, a_2, \dots, a_N, \ g + 1\big)$$
Wtedy dla każdego $n \in \mathbb{N}$ zachodzi nierówność $m \le a_n \le M$, co oznacza, że ciąg $(a_n)$ jest ograniczony. $\blacksquare$

> **Twierdzenie 3.3 (Lemat o zachowaniu znaku granicy):**
> Jeżeli $\lim_{n \to \infty} a_n = g$ oraz $g > 0$ (odpowiednio $g < 0$), to:
> $$\exists_{N \in \mathbb{N}} \forall_{n > N} \quad a_n > 0 \quad (\text{odpowiednio } a_n < 0)$$

**Dowód:**
Dla $g > 0$ wystarczy przyjąć $\varepsilon = \frac{g}{2} > 0$. Wtedy od pewnego miejsca $N$:
$$|a_n - g| < \frac{g}{2} \implies g - \frac{g}{2} < a_n < g + \frac{g}{2} \implies a_n > \frac{g}{2} > 0 \quad \blacksquare$$

---

### 3.3. Granice niewłaściwe i symbole nieoznaczone

#### Definicja 3.5 (Granice niewłaściwe)
1. Mówimy, że ciąg $(a_n)$ ma granicę niewłaściwą $+\infty$ (ozn. $\lim_{n \to \infty} a_n = +\infty$), jeżeli:
   $$\forall_{M \in \mathbb{R}} \exists_{N \in \mathbb{N}} \forall_{n > N} \quad a_n > M$$
2. Mówimy, że ciąg $(a_n)$ ma granicę niewłaściwą $-\infty$ (ozn. $\lim_{n \to \infty} a_n = -\infty$), jeżeli:
   $$\forall_{M \in \mathbb{R}} \exists_{N \in \mathbb{N}} \forall_{n > N} \quad a_n < M$$

#### Klasyfikacja symboli nieoznaczonych:
Przy wyznaczaniu granic sum, iloczynów, ilorazów i potęg pojawia się 7 klasycznych wyrażeń nieoznaczonych:
$$\left[ \frac{\infty}{\infty} \right], \quad \left[ \frac{0}{0} \right], \quad [\infty - \infty], \quad [0 \cdot \infty], \quad [1^\infty], \quad [0^0], \quad [\infty^0]$$
Wyrażenia te nazywamy nieoznaczonymi, ponieważ granica ciągu o takiej postaci zależy od relacji prędkości dążenia poszczególnych składowych do swoich granic i może przyjąć dowolną wartość z $\mathbb{R} \cup \{-\infty, +\infty\}$ lub w ogóle nie istnieć.

---

### 3.4. Podciągi, granice górne i dolne oraz twierdzenie Bolzano-Weierstrassa

#### Definicja 3.6 (Podciąg)
Niech dany będzie ciąg $(a_n)_{n=1}^\infty$. Jeżeli $(k_n)_{n=1}^\infty$ jest ściśle rosnącym ciągiem liczb naturalnych:
$$1 \le k_1 < k_2 < k_3 < \dots < k_n < \dots$$
to ciąg $(a_{k_n})_{n=1}^\infty$ nazywamy **podciągiem** ciągu $(a_n)$.

> **Twierdzenie 3.4:**
> Jeżeli ciąg $(a_n)$ jest zbieżny do granicy $g$ (właściwej lub niewłaściwej), to każdy jego podciąg $(a_{k_n})$ jest również zbieżny do tej samej granicy $g$.

#### Definicja 3.7 (Punkt skupienia ciągu)
Liczbę $p \in \mathbb{R} \cup \{-\infty, +\infty\}$ nazywamy **punktem skupienia** ciągu $(a_n)$, jeżeli istnieje podciąg $(a_{k_n})$ zbieżny do $p$:
$$\lim_{n \to \infty} a_{k_n} = p$$

#### Definicja 3.8 (Granica górna i dolna - Limes Superior i Limes Inferior)
Niech $S$ będzie zbiorem wszystkich punktów skupienia ciągu $(a_n)$ w rozszerzonym zbiorze liczb rzeczywistych $\overline{\mathbb{R}} = \mathbb{R} \cup \{-\infty, +\infty\}$:
1. **Granicą górną** ciągu $(a_n)$ nazywamy kres górny zbioru $S$:
   $$\limsup_{n \to \infty} a_n = \varlimsup_{n \to \infty} a_n = \sup S = \lim_{n \to \infty} \left( \sup_{k \ge n} a_k \right)$$
2. **Granicą dolną** ciągu $(a_n)$ nazywamy kres dolny zbioru $S$:
   $$\liminf_{n \to \infty} a_n = \varliminf_{n \to \infty} a_n = \inf S = \lim_{n \to \infty} \left( \inf_{k \ge n} a_k \right)$$

> **Twierdzenie 3.5 (Kryterium istnienia granicy za pomocą $\limsup$ i $\liminf$):**
> Ciąg $(a_n)$ posiada granicę $g \in \overline{\mathbb{R}}$ wtedy i tylko wtedy, gdy jego granica górna i dolna są sobie równe:
> $$\lim_{n \to \infty} a_n = g \iff \limsup_{n \to \infty} a_n = \liminf_{n \to \infty} a_n = g$$

> **Twierdzenie 3.6 (Bolzano-Weierstrassa dla ciągów):**
> Z każdego ciągu ograniczonego można wybrać podciąg zbieżny.

**Dowód (metodą bisekcji przedziałów):**
Niech ciąg $(a_n)$ będzie ograniczony: $\exists_{A, B \in \mathbb{R}} \forall_n \ A \le a_n \le B$.  
Oznaczmy przedział domknięty $I_1 = [a_1, b_1] = [A, B]$. Zbiór wskaźników $N_1 = \mathbb{N}$ jest nieskończony.  
Dzielimy przedział $I_1$ punktem środkowym $c_1 = \frac{a_1 + b_1}{2}$ na dwie połowy: $[a_1, c_1]$ oraz $[c_1, b_1]$. Przynajmniej jedna z tych połów zawiera nieskończenie wiele wyrazów ciągu.  
Wybieramy tę połowę i oznaczamy jako $I_2 = [a_2, b_2]$, a z jej wyrazów wybieramy pierwszy element podciągu $a_{k_1}$.  
Kontynuując tę procedurę indukcyjnie, konstruujemy ciąg zstępujących przedziałów domkniętych:
$$I_1 \supset I_2 \supset I_3 \supset \dots \supset I_n \supset \dots$$
o długościach:
$$|I_n| = b_n - a_n = \frac{B - A}{2^{n-1}} \xrightarrow[n \to \infty]{} 0$$
oraz rosnący ciąg wskaźników $k_1 < k_2 < \dots < k_n$ taki, że $a_{k_n} \in I_n$.  
Z zasady ciągłości Cantora przekrój wszystkich przedziałów $\bigcap_{n=1}^\infty I_n = \{g\}$ zawiera dokładnie jeden punkt $g \in \mathbb{R}$.  
Ponieważ $a_n \le a_{k_n} \le b_n$ oraz $\lim a_n = \lim b_n = g$, z twierdzenia o trzech ciągach:
$$\lim_{n \to \infty} a_{k_n} = g \quad \blacksquare$$

---

### 3.5. Warunek zbieżności Cauchy'ego i zupełność metryczna $\mathbb{R}$

Definicja granicy Cauchy'ego wymaga uprzedniej znajomości wartości granicy $g$. Kryterium Cauchy'ego pozwala rozstrzygać o zbieżności ciągu wyłącznie na podstawie relacji między jego wyrazami.

#### Definicja 3.9 (Ciąg Cauchy'ego)
Ciąg $(a_n)$ nazywamy **ciągiem Cauchy'ego** (ciągiem fundamentalnym), jeżeli odległość między dowolnymi dwoma wyrazami o dostatecznie dużych wskaźnikach jest dowolnie mała:

$$\forall_{\varepsilon > 0} \exists_{N \in \mathbb{N}} \forall_{m, n \in \mathbb{N}} \quad \big( m, n > N \implies |a_n - a_m| < \varepsilon \big)$$

> **Twierdzenie 3.7 (Kryterium zbieżności Cauchy'ego):**
> Ciąg liczb rzeczywistych $(a_n)$ jest zbieżny do granicy właściwej $g \in \mathbb{R}$ wtedy i tylko wtedy, gdy jest ciągiem Cauchy'ego.

**Dowód:**
1. **$(\implies)$ Konieczność:**  
   Niech $\lim_{n \to \infty} a_n = g$. Z definicji granicy dla zadanego $\varepsilon > 0$ istnieje $N$ takie, że dla $k > N$: $|a_k - g| < \frac{\varepsilon}{2}$.  
   Dla dowolnych $m, n > N$, stosując nierówność trójkąta:
   $$|a_n - a_m| = |(a_n - g) + (g - a_m)| \le |a_n - g| + |a_m - g| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$
   Zatem ciąg spełnia warunek Cauchy'ego.

2. **$(\impliedby)$ Dostateczność:**  
   Niech $(a_n)$ spełnia warunek Cauchy'ego.
   - *Krok 1 (ograniczoność):* Dla $\varepsilon = 1$ istnieje $N_1$ takie, że $\forall_{n > N_1} \ |a_n - a_{N_1+1}| < 1$. Stąd ciąg Cauchy'ego jest ograniczony.
   - *Krok 2 (istnienie podciągu zbieżnego):* Na mocy Twierdzenia Bolzano-Weierstrassa (Tw. 3.6) z ograniczonego ciągu $(a_n)$ można wybrać podciąg zbieżny $(a_{k_n})$ do pewnej granicy $g \in \mathbb{R}$.
   - *Krok 3 (zbieżność całego ciągu do $g$):* Ustalmy dowolny $\varepsilon > 0$.  
     Z warunku Cauchy'ego: $\exists_{N_2} \forall_{n, m > N_2} \ |a_n - a_m| < \frac{\varepsilon}{2}$.  
     Ze zbieżności podciągu: $\exists_{K} \forall_{j > K} \ |a_{k_j} - g| < \frac{\varepsilon}{2}$.  
     Wybierzmy wskaźnik $k_j > \max(N_2, K)$. Wtedy dla dowolnego $n > N_2$:
     $$|a_n - g| \le |a_n - a_{k_j}| + |a_{k_j} - g| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon$$
     Dowodzi to, że cały ciąg $(a_n)$ zmierza do $g$. $\blacksquare$

---

## Rozdział 4: Metody wyznaczania granic ciągów

### 4.1. Arytmetyka granic ciągów

> **Twierdzenie 4.1 (Działania na granicach ciągów):**
> Jeżeli ciągi $(a_n)$ i $(b_n)$ są zbieżne oraz $\lim_{n \to \infty} a_n = a$, $\lim_{n \to \infty} b_n = b$, to:
> 1. $\lim_{n \to \infty} (a_n \pm b_n) = a \pm b$,
> 2. $\lim_{n \to \infty} (c \cdot a_n) = c \cdot a \quad (c \in \mathbb{R})$,
> 3. $\lim_{n \to \infty} (a_n \cdot b_n) = a \cdot b$,
> 4. $\lim_{n \to \infty} \frac{a_n}{b_n} = \frac{a}{b} \quad (\text{o ile } b \neq 0 \text{ oraz } \forall_n \ b_n \neq 0)$,
> 5. $\lim_{n \to \infty} |a_n| = |a|$,
> 6. $\lim_{n \to \infty} a_n^k = a^k \quad (k \in \mathbb{N})$.

**Dowód dla ilorazu (punkt 4):**
Pokażemy najpierw, że $\lim_{n \to \infty} \frac{1}{b_n} = \frac{1}{b}$.  
Ponieważ $b \neq 0$, z lematu o zachowaniu znaku dla $\varepsilon_0 = \frac{|b|}{2} > 0$ istnieje $N_1$ takie, że dla $n > N_1$:
$$|b_n| > \frac{|b|}{2} \iff \frac{1}{|b_n|} < \frac{2}{|b|}$$
Badamy różnicę:
$$\left| \frac{1}{b_n} - \frac{1}{b} \right| = \left| \frac{b - b_n}{b \cdot b_n} \right| = \frac{|b_n - b|}{|b| \cdot |b_n|} < \frac{2}{|b|^2} |b_n - b|$$
Dla zadanego $\varepsilon > 0$ dobieramy $N_2$ z faktu, że $\lim b_n = b$, tak aby $|b_n - b| < \frac{|b|^2 \varepsilon}{2}$.  
Dla $n > \max(N_1, N_2)$:
$$\left| \frac{1}{b_n} - \frac{1}{b} \right| < \frac{2}{|b|^2} \cdot \frac{|b|^2 \varepsilon}{2} = \varepsilon$$
Korzystając z reguły iloczynu: $\lim \frac{a_n}{b_n} = \lim \left( a_n \cdot \frac{1}{b_n} \right) = a \cdot \frac{1}{b} = \frac{a}{b}$. $\blacksquare$

---

### 4.2. Twierdzenie o trzech ciągach i o dwóch ciągach

> **Twierdzenie 4.2 (Twierdzenie o trzech ciągach):**
> Jeżeli dla ciągów $(a_n), (b_n), (c_n)$ spełniony jest warunek:
> $$\exists_{N_0 \in \mathbb{N}} \forall_{n > N_0} \quad a_n \le b_n \le c_n$$
> oraz:
> $$\lim_{n \to \infty} a_n = \lim_{n \to \infty} c_n = g$$
> to ciąg $(b_n)$ jest zbieżny i $\lim_{n \to \infty} b_n = g$.

> **Twierdzenie 4.3 (Twierdzenie o dwóch ciągach dla granic niewłaściwych):**
> 1. Jeżeli $\forall_{n > N_0} \ a_n \le b_n$ oraz $\lim_{n \to \infty} a_n = +\infty$, to $\lim_{n \to \infty} b_n = +\infty$.
> 2. Jeżeli $\forall_{n > N_0} \ b_n \le a_n$ oraz $\lim_{n \to \infty} a_n = -\infty$, to $\lim_{n \to \infty} b_n = -\infty$.

---

### 4.3. Ciągi monotoniczne i liczba $e$

> **Twierdzenie 4.4 (Weierstrassa o zbieżności ciągu monotonicznego i ograniczonego):**
> 1. Ciąg niemalejący i ograniczony z góry jest zbieżny do swojego kresu górnego:
>    $$\lim_{n \to \infty} a_n = \sup \{a_n : n \in \mathbb{N}\}$$
> 2. Ciąg nierosnący i ograniczony z dołu jest zbieżny do swojego kresu dolnego:
>    $$\lim_{n \to \infty} a_n = \inf \{a_n : n \in \mathbb{N}\}$$

#### Precyzyjna konstrukcja liczby $e$:
Rozpatrzmy dwa ciągi:
$$a_n = \left( 1 + \frac{1}{n} \right)^n, \quad b_n = \left( 1 + \frac{1}{n} \right)^{n+1}$$

> **Twierdzenie 4.5:**
> 1. Ciąg $(a_n)$ jest ściśle rosnący.
> 2. Ciąg $(b_n)$ jest ściśle malejący.
> 3. Dla każdego $n \in \mathbb{N}$: $a_n < b_n$.
> 4. Oba ciągi są zbieżne do tej samej granicy właściwej:
>    $$\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = e \approx 2{,}718281828459\dots$$

**Dowód monotoniczności $(a_n)$ za pomocą nierówności Bernoulliego:**
Badamy iloraz $\frac{a_{n+1}}{a_n}$:
$$\frac{a_{n+1}}{a_n} = \frac{\left( 1 + \frac{1}{n+1} \right)^{n+1}}{\left( 1 + \frac{1}{n} \right)^n} = \frac{\left( \frac{n+2}{n+1} \right)^{n+1}}{\left( \frac{n+1}{n} \right)^n} = \frac{n+1}{n} \cdot \left( \frac{(n+2)n}{(n+1)^2} \right)^{n+1} = \frac{n+1}{n} \left( \frac{n^2 + 2n}{n^2 + 2n + 1} \right)^{n+1} = \frac{n+1}{n} \left( 1 - \frac{1}{(n+1)^2} \right)^{n+1}$$
Stosujemy nierówność Bernoulliego (Tw. 1.6) dla $x = -\frac{1}{(n+1)^2} > -1$:
$$\left( 1 - \frac{1}{(n+1)^2} \right)^{n+1} > 1 - (n + 1)\frac{1}{(n+1)^2} = 1 - \frac{1}{n+1} = \frac{n}{n+1}$$
Wstawiając z powrotem:
$$\frac{a_{n+1}}{a_n} > \frac{n+1}{n} \cdot \frac{n}{n+1} = 1 \implies a_{n+1} > a_n$$
Ciąg $(a_n)$ jest zatem ściśle rosnący.  
Ponieważ $a_n < b_n \le b_1 = (1 + 1)^2 = 4$, ciąg $(a_n)$ jest ograniczony z góry. Na mocy Twierdzenia Weierstrassa posiada granicę właściwą $e$. $\blacksquare$

> **Twierdzenie 4.6 (O niewymierności liczby $e$):**
> Liczba $e$ jest liczbą niewymierną ($e \notin \mathbb{Q}$).

---

### 4.4. Twierdzenie Stolza-Cesàro

Twierdzenie Stolza jest dyskretnym odpowiednikiem reguły de l'Hospitala i stanowi potężne narzędzie obliczania granic symboli $\left[\frac{0}{0}\right]$ oraz $\left[\frac{\infty}{\infty}\right]$ dla ciągów.

> **Twierdzenie 4.7 (Twierdzenie Stolza-Cesàro):**
> Niech $(a_n)$ i $(b_n)$ będą ciągami liczb rzeczywistych. Załóżmy, że ciąg $(b_n)$ jest ściśle rosnący od pewnego miejsca oraz $\lim_{n \to \infty} b_n = +\infty$.  
> Jeżeli istnieje granica (właściwa lub niewłaściwa):
> $$\lim_{n \to \infty} \frac{a_{n+1} - a_n}{b_{n+1} - b_n} = g$$
> to istnieje również granica ilorazu wyjściowego i zachodzi równość:
> $$\lim_{n \to \infty} \frac{a_n}{b_n} = g$$

#### Wniosek (Twierdzenie Cauchy'ego o średnich):
1. Jeżeli $\lim_{n \to \infty} x_n = g$, to granica średnich arytmetycznych:
   $$\lim_{n \to \infty} \frac{x_1 + x_2 + \dots + x_n}{n} = g$$
2. Jeżeli $x_n > 0$ oraz $\lim_{n \to \infty} \frac{x_{n+1}}{x_n} = g$, to granica pierwiastków:
   $$\lim_{n \to \infty} \sqrt[n]{x_n} = g$$

---

### 4.5. Zastosowania inżynierskie: Filtry cyfrowe wyższych rzędów i stabilność (DSP)

W cyfrowym przetwarzaniu sygnałów liniowy, niezmienniczy w czasie filtr dyskretny (LTI) rzędu drugiego opisany jest równaniem różnicowym:
$$y[n] - a_1 y[n-1] - a_2 y[n-2] = x[n]$$
Dla odpowiedzi swobodnej ($x[n] = 0$) rozwiązanie ma postać ciągu geometrycznego $y[n] = \lambda^n$.  
Wstawiając do równania jednorodnego:
$$\lambda^n - a_1 \lambda^{n-1} - a_2 \lambda^{n-2} = 0 \iff \lambda^2 - a_1 \lambda - a_2 = 0$$
Równanie to nazywamy **równaniem charakterystycznym filtru**, a jego pierwiastki $\lambda_1, \lambda_2 \in \mathbb{C}$ są biegunami transmitancji w dziedzinie transformaty $Z$.

#### Warunki stabilności asymptotycznej filtru (zbieżność $\lim_{n \to \infty} y[n] = 0$):
1. **Dwa różne pierwiastki rzeczywiste ($\Delta > 0$):** $y[n] = C_1 \lambda_1^n + C_2 \lambda_2^n$. Ciąg zmierza do zera wtedy i tylko wtedy, gdy $|\lambda_1| < 1$ oraz $|\lambda_2| < 1$.
2. **Pierwiastek podwójny ($\Delta = 0$):** $y[n] = (C_1 + C_2 n) \lambda_1^n$. Ponieważ $\lim_{n \to \infty} n \lambda^n = 0 \iff |\lambda| < 1$, warunkiem zbieżności jest $|\lambda_1| < 1$.
3. **Para sprzężona pierwiastków zespolonych ($\Delta < 0$):** $\lambda_{1,2} = r e^{\pm j\Omega}$. Wtedy:
   $$y[n] = r^n \big( A \cos(n\Omega) + B \sin(n\Omega) \big)$$
   Ciąg reprezentuje oscylacje tłumione. Zbieżność do zera zachodzi wtedy i tylko wtedy, gdy promień $r = |\lambda| < 1$.

**Fundamentalna zasada DSP:**  
Układ dyskretny jest stabilny asymptotycznie (odpowiedź impulsowa jest ciągiem zbieżnym do zera) wtedy i tylko wtedy, gdy wszystkie pierwiastki równania charakterystycznego leżą **ściśle wewnątrz koła jednostkowego na płaszczyźnie zespolonej**:
$$\forall_k \quad |\lambda_k| < 1$$

---

### 4.6. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 2.1: Zastosowanie twierdzenia Stolza-Cesàro
Oblicz granicę ciągu:
$$\lim_{n \to \infty} \frac{1^k + 2^k + 3^k + \dots + n^k}{n^{k+1}} \quad (k \in \mathbb{N})$$

**Rozwiązanie:**
Niech $a_n = \sum_{j=1}^n j^k$ oraz $b_n = n^{k+1}$.  
Ciąg $b_n$ jest ściśle rosnący i dąży do $+\infty$. Stosujemy twierdzenie Stolza:
$$\frac{a_{n+1} - a_n}{b_{n+1} - b_n} = \frac{(n+1)^k}{(n+1)^{k+1} - n^{k+1}}$$
Rozwijamy mianownik za pomocą wzoru dwumianowego Newtona:
$$(n+1)^{k+1} - n^{k+1} = \sum_{j=0}^{k+1} \binom{k+1}{j} n^{k+1-j} - n^{k+1} = (k+1)n^k + \binom{k+1}{2}n^{k-1} + \dots + 1$$
Licznik wynosi $(n+1)^k = n^k + k n^{k-1} + \dots + 1$.  
Iloraz przyrostów wynosi:
$$\frac{n^k + k n^{k-1} + \dots}{(k+1)n^k + \binom{k+1}{2}n^{k-1} + \dots} = \frac{1 + \frac{k}{n} + \dots}{(k+1) + \binom{k+1}{2}\frac{1}{n} + \dots}$$
Przechodząc do granicy przy $n \to \infty$:
$$\lim_{n \to \infty} \frac{a_{n+1} - a_n}{b_{n+1} - b_n} = \frac{1}{k+1}$$
Na mocy twierdzenia Stolza-Cesàro:
$$\lim_{n \to \infty} \frac{\sum_{j=1}^n j^k}{n^{k+1}} = \frac{1}{k+1}$$
*(Wynik ten odpowiada całce Riemanna $\int_0^1 x^k dx = \frac{1}{k+1}$)*.

---

#### Przykład 2.2: Granice zagnieżdżonych pierwiastków z twierdzenia o trzech ciągach
Oblicz granicę ciągu:
$$a_n = \sqrt[n]{2^n \cdot n^3 + 3^n \cdot n^2 + 5^n}$$

**Rozwiązanie:**
Dominującym składnikiem pod pierwiastkiem przy dużych $n$ jest potęga o największej podstawie, czyli $5^n$ (ponieważ wykładniczy wzrost $5^n$ przewyższa wielomianowy wzrost $n^3 \cdot 2^n$ czy $n^2 \cdot 3^n$).
Konstruujemy oszacowania:
1. **Oszacowanie z dołu:**
   $$5 = \sqrt[n]{5^n} \le \sqrt[n]{2^n n^3 + 3^n n^2 + 5^n}$$
2. **Oszacowanie z góry:**  
   Dla $n \ge 10$: $2^n n^3 < 5^n$ oraz $3^n n^2 < 5^n$.  
   Zatem:
   $$\sqrt[n]{2^n n^3 + 3^n n^2 + 5^n} \le \sqrt[n]{5^n + 5^n + 5^n} = \sqrt[n]{3 \cdot 5^n} = 5 \sqrt[n]{3}$$
Mamy podwójną nierówność:
$$5 \le a_n \le 5 \sqrt[n]{3}$$
Ponieważ $\lim_{n \to \infty} 5 = 5$ oraz $\lim_{n \to \infty} 5\sqrt[n]{3} = 5 \cdot 1 = 5$, na mocy twierdzenia o trzech ciągach:
$$\lim_{n \to \infty} a_n = 5$$

---

#### Przykład 2.3: Zbieżność algorytmu Herona obliczania $\sqrt{c}$
Rozważmy ciąg zdefiniowany rekurencyjnie wzorem:
$$x_1 = c > 0, \quad x_{n+1} = \frac{1}{2}\left( x_n + \frac{c}{x_n} \right) \quad (n \ge 1)$$
Wykaż, że ciąg jest zbieżny do $\sqrt{c}$ oraz zbadaj prędkość zbieżności.

**Rozwiązanie:**
1. **Ograniczoność z dołu przez $\sqrt{c}$:**  
   Stosując nierówność między średnią arytmetyczną i geometryczną (AM-GM, Tw. 1.7):
   $$x_{n+1} = \frac{x_n + \frac{c}{x_n}}{2} \ge \sqrt{x_n \cdot \frac{c}{x_n}} = \sqrt{c}$$
   Zatem dla każdego $n \ge 1$: $x_{n+1} \ge \sqrt{c}$.
2. **Monotoniczność dla $n \ge 2$:**
   $$x_{n+1} - x_n = \frac{1}{2}x_n + \frac{c}{2x_n} - x_n = \frac{c - x_n^2}{2x_n}$$
   Ponieważ dla $n \ge 2$ mamy $x_n \ge \sqrt{c} \implies x_n^2 \ge c \implies c - x_n^2 \le 0$.  
   Stąd $x_{n+1} - x_n \le 0$, czyli ciąg $(x_n)$ jest nierosnący od drugiego wyrazu.
3. **Istnienie i wartość granicy:**  
   Ciąg jest nierosnący i ograniczony z dołu przez $\sqrt{c}$. Z twierdzenia Weierstrassa (Tw. 4.4) istnieje skończona granica $g = \lim_{n \to \infty} x_n \ge \sqrt{c}$.  
   Przechodząc do granicy w równaniu rekurencyjnym:
   $$g = \frac{1}{2}\left( g + \frac{c}{g} \right) \iff 2g = g + \frac{c}{g} \iff g = \frac{c}{g} \iff g^2 = c \implies g = \sqrt{c}$$
4. **Analiza błędu (zbieżność kwadratowa):**  
   Zdefiniujmy błąd względny $\varepsilon_n = x_n - \sqrt{c}$:
   $$\varepsilon_{n+1} = x_{n+1} - \sqrt{c} = \frac{x_n + \frac{c}{x_n} - 2\sqrt{c}}{2} = \frac{x_n^2 - 2x_n\sqrt{c} + c}{2x_n} = \frac{(x_n - \sqrt{c})^2}{2x_n} = \frac{\varepsilon_n^2}{2x_n}$$
   Oznacza to, że błąd w kolejnym kroku jest proporcjonalny do **kwadratu błędu poprzedniego**, co podwaja liczbę cyfr dokładnych w każdej iteracji (metoda Newtona).

---

### 4.7. Zestaw zadań do samodzielnego rozwiązania

1. **Zadanie 2.1:** Wykaż z definicji Cauchy'ego $\varepsilon-N$, że $\lim_{n \to \infty} \frac{2n^2 - 1}{n^2 + 3} = 2$.
2. **Zadanie 2.2:** Wyznacz granicę górną $\limsup a_n$ oraz dolną $\liminf a_n$ dla ciągu $a_n = (-1)^n \frac{n}{n+1} + \sin\left(\frac{n\pi}{2}\right)$. Czy ciąg posiada granicę?
3. **Zadanie 2.3:** Oblicz granicę ciągu: $\lim_{n \to \infty} \left( \frac{n^2 + 2n - 1}{n^2 - n + 2} \right)^{2n+3}$.
4. **Zadanie 2.4:** Oblicz granicę: $\lim_{n \to \infty} \left( \frac{1}{\sqrt{n^4+1}} + \frac{2}{\sqrt{n^4+2}} + \dots + \frac{n}{\sqrt{n^4+n}} \right)$.
5. **Zadanie 2.5:** Wyznacz granicę: $\lim_{n \to \infty} \frac{1}{n} \sqrt[n]{(n+1)(n+2)\dots(2n)}$ korzystając z twierdzenia o średnich.
6. **Zadanie 2.6 (Filtr cyfrowy IIR):** Odpowiedź impulsowa filtru spełnia równanie rekurencyjne $y[n] - 0{,}9 y[n-1] + 0{,}2 y[n-2] = 0$ z warunkami początkowymi $y[0] = 1, y[1] = 0{,}5$. Wyznacz postać jawną ciągu próbek $y[n]$ oraz zbadaj stabilność układu.

---

### Odpowiedzi i wskazówki do zadań

- **2.1:** $\left| \frac{2n^2 - 1}{n^2 + 3} - 2 \right| = \left| \frac{2n^2 - 1 - 2n^2 - 6}{n^2 + 3} \right| = \frac{7}{n^2 + 3} < \frac{7}{n^2} < \varepsilon \iff n > \sqrt{\frac{7}{\varepsilon}}$. Wystarczy przyjąć $N = \left\lfloor \sqrt{7/\varepsilon} \right\rfloor + 1$.
- **2.2:** Podciągi dla reszt modulo 4:
  - $n = 4k$: $1 \cdot 1 + 0 = 1$,
  - $n = 4k+1$: $(-1) \cdot 1 + 1 = 0$,
  - $n = 4k+2$: $1 \cdot 1 + 0 = 1$,
  - $n = 4k+3$: $(-1) \cdot 1 - 1 = -2$.
  Zbiór punktów skupienia $S = \{-2, 0, 1\}$. Zatem $\limsup a_n = 1$, $\liminf a_n = -2$. Ciąg nie posiada granicy.
- **2.3:** Sprowadzamy do liczby $e$: $\frac{n^2+2n-1}{n^2-n+2} = 1 + \frac{3n-3}{n^2-n+2}$. Granica wykładnika: $\lim_{n \to \infty} (2n+3) \cdot \frac{3n-3}{n^2-n+2} = \lim \frac{6n^2 + \dots}{n^2 + \dots} = 6$. Wynik: $e^6$.
- **2.4:** Suma w liczniku: $\sum_{k=1}^n k = \frac{n(n+1)}{2}$. Szacowanie z dołu: $\frac{n(n+1)}{2\sqrt{n^4+n}} \to \frac{1}{2}$. Szacowanie z góry: $\frac{n(n+1)}{2\sqrt{n^4+1}} \to \frac{1}{2}$. Z twierdzenia o trzech ciągach granica wynosi $\frac{1}{2}$.
- **2.5:** Niech $x_n = \frac{(n+1)(n+2)\dots(2n)}{n^n}$. Obliczamy $\lim \frac{x_{n+1}}{x_n} = \lim \frac{\frac{(n+2)\dots(2n+2)}{(n+1)^{n+1}}}{\frac{(n+1)\dots(2n)}{n^n}} = \lim \frac{(2n+1)(2n+2)}{(n+1)(n+1)} \cdot \left( \frac{n}{n+1} \right)^n = \lim \frac{2(2n+1)}{n+1} \left(1 + \frac{1}{n}\right)^{-n} = 4 e^{-1} = \frac{4}{e}$. Na mocy twierdzenia o średnich: $\lim \sqrt[n]{x_n} = \frac{4}{e}$.
- **2.6:** Równanie charakterystyczne: $\lambda^2 - 0{,}9\lambda + 0{,}2 = 0 \iff (\lambda - 0{,}5)(\lambda - 0{,}4) = 0$. Bieguny: $\lambda_1 = 0{,}5, \lambda_2 = 0{,}4$. Postać ogólna: $y[n] = C_1 (0{,}5)^n + C_2 (0{,}4)^n$. Z warunków początkowych: $C_1 + C_2 = 1$, $0{,}5 C_1 + 0{,}4 C_2 = 0{,}5 \implies C_1 = 1, C_2 = 0$. Zatem $y[n] = (0{,}5)^n$. Ponieważ obydwa bieguny $|\lambda_i| < 1$, filtr jest stabilny asymptotycznie i $\lim_{n \to \infty} y[n] = 0$.
