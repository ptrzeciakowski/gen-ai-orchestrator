# Część I: Fundamenty Analizy Matematycznej

W analizie matematycznej dla inżynierów elektroników, informatyków i telekomunikatorów pojęcia abstrakcyjne nie są sztuczną konstrukcją logiczną, lecz bezpośrednim fundamentem modelowania sygnałów, transmisji danych, dynamiki obwodów elektrycznych oraz stabilności procesów przetwarzania informacji. Niniejsza część poświęcona jest rygorystycznemu wykładowi ciała liczb rzeczywistych $\mathbb{R}$ oraz ciała liczb zespolonych $\mathbb{C}$ w ujęciu klasycznego kanonu akademickiego doc. Janiny Decewicz i prof. Wojciecha Żakowskiego.

---

## Rozdział 1: Ciało liczb rzeczywistych $\mathbb{R}$

### 1.1. Konstrukcja aksjomatyczna ciała liczb rzeczywistych

Zbiór liczb rzeczywistych $\mathbb{R}$ definiujemy aksjomatycznie jako ciało uporządkowane, spełniające aksjomat ciągłości (zupełności). Oznacza to spełnienie trzech fundamentalnych grup aksjomatów.

#### Grupa I: Aksjomaty ciała $(\mathbb{R}, +, \cdot)$
W zbiorze $\mathbb{R}$ określone są dwa działania dwuargumentowe: dodawanie $(+)$ oraz mnożenie $(\cdot)$, przyporządkowujące każdej parze $(x, y) \in \mathbb{R} \times \mathbb{R}$ jednoznacznie wyznaczone elementy $x + y \in \mathbb{R}$ oraz $x \cdot y \in \mathbb{R}$, spełniające dla dowolnych $x, y, z \in \mathbb{R}$ następujące postulaty:

1. **Łączność dodawania:**
   $$(x + y) + z = x + (y + z)$$
2. **Przemienność dodawania:**
   $$x + y = y + x$$
3. **Istnienie elementu neutralnego dodawania (zera):**
   $$\exists_{0 \in \mathbb{R}} \forall_{x \in \mathbb{R}} \quad x + 0 = x$$
4. **Istnienie elementu przeciwnego:**
   $$\forall_{x \in \mathbb{R}} \exists_{-x \in \mathbb{R}} \quad x + (-x) = 0$$
5. **Łączność mnożenia:**
   $$(x \cdot y) \cdot z = x \cdot (y \cdot z)$$
6. **Przemienność mnożenia:**
   $$x \cdot y = y \cdot x$$
7. **Istnienie elementu neutralnego mnożenia (jedynki):**
   $$\exists_{1 \in \mathbb{R} \setminus \{0\}} \forall_{x \in \mathbb{R}} \quad x \cdot 1 = x$$
8. **Istnienie elementu odwrotnego:**
   $$\forall_{x \in \mathbb{R} \setminus \{0\}} \exists_{x^{-1} \in \mathbb{R}} \quad x \cdot x^{-1} = 1 \quad \left(\text{oznaczanego również jako } \frac{1}{x}\right)$$
9. **Rozdzielność mnożenia względem dodawania:**
   $$x \cdot (y + z) = (x \cdot y) + (x \cdot z)$$

> **Twierdzenie 1.1 (Elementarne własności algebraiczne wynikające z aksjomatów ciała):**
> 1. Elementy neutralne $0$ i $1$ oraz elementy odwrotne $-x$ i $x^{-1}$ są wyznaczone jednoznacznie.
> 2. Dla każdego $x \in \mathbb{R}$ zachodzi $x \cdot 0 = 0$.
> 3. Dla dowolnych $x, y \in \mathbb{R}$ zachodzi $(-x) \cdot y = -(x \cdot y)$ oraz $(-x) \cdot (-y) = x \cdot y$. W szczególności $(-1) \cdot (-1) = 1$.
> 4. Iloczyn $x \cdot y = 0 \iff (x = 0 \lor y = 0)$ (ciało $\mathbb{R}$ nie posiada właściwych dzielników zera).

**Dowód punktu 2 ($x \cdot 0 = 0$):**
Z aksjomatu elementu neutralnego $0 + 0 = 0$. Mnożąc obustronnie przez $x$ i stosując rozdzielność:
$$x \cdot 0 = x \cdot (0 + 0) = (x \cdot 0) + (x \cdot 0)$$
Dodając do obu stron element przeciwny do $x \cdot 0$, otrzymujemy:
$$-(x \cdot 0) + (x \cdot 0) = -(x \cdot 0) + \big( (x \cdot 0) + (x \cdot 0) \big)$$
$$0 = \big( -(x \cdot 0) + (x \cdot 0) \big) + (x \cdot 0) = 0 + (x \cdot 0) = x \cdot 0 \quad \blacksquare$$

---

#### Grupa II: Aksjomaty porządku liniowego $(\mathbb{R}, \le)$
W zbiorze $\mathbb{R}$ określona jest relacja dwuczłonowa $\le$, będąca relacją porządku liniowego zgodną ze strukturą ciała:
1. **Zwrotność:** $\forall_{x \in \mathbb{R}} \ x \le x$,
2. **Słaba antysymetryczność:** $\forall_{x, y \in \mathbb{R}} \ (x \le y \land y \le x) \implies x = y$,
3. **Przechodniość:** $\forall_{x, y, z \in \mathbb{R}} \ (x \le y \land y \le z) \implies x \le z$,
4. **Spójność (porządek liniowy):** $\forall_{x, y \in \mathbb{R}} \ (x \le y \lor y \le x)$,
5. **Zgodność z dodawaniem:** $\forall_{x, y, z \in \mathbb{R}} \ (x \le y) \implies (x + z \le y + z)$,
6. **Zgodność z mnożeniem:** $\forall_{x, y \in \mathbb{R}} \ (0 \le x \land 0 \le y) \implies 0 \le x \cdot y$.

Relację ostrej nierówności definiujemy standardowo: $x < y \iff (x \le y \land x \neq y)$.

---

#### Grupa III: Aksjomat ciągłości (Zupełność Dedekinda)
Ciało liczb wymiernych $\mathbb{Q}$ spełnia wszystkie aksjomaty Grupy I i Grupy II, lecz nie jest ciągłe – zawiera „luki” odpowiadające liczbom niewymiernym. Pełnię prostej rzeczywistej gwarantuje aksjomat Dedekinda.

#### Definicja 1.1 (Przekrój Dedekinda)
Przekrojem zbioru liczb rzeczywistych $\mathbb{R}$ nazywamy parę zbiorów $(A, B)$ taką, że:
1. $A \neq \emptyset$ oraz $B \neq \emptyset$,
2. $A \cup B = \mathbb{R}$,
3. $\forall_{a \in A} \forall_{b \in B} \quad a \le b$.
Zbiór $A$ nazywamy klasą dolną, a $B$ klasą górną przekroju.

> **Aksjomat Ciągłości Dedekinda:**
> Dla każdego przekroju $(A, B)$ zbioru liczb rzeczywistych $\mathbb{R}$ istnieje liczba $c \in \mathbb{R}$ taka, że:
> $$\forall_{a \in A} \forall_{b \in B} \quad a \le c \le b$$
> Oznacza to, że albo w klasie dolnej $A$ istnieje element największy, albo w klasie górnej $B$ istnieje element najmniejszy (nie ma „dziur” na prostej).

---

### 1.2. Kresy zbiorów i zasada zupełności

Pojęcia kresów zastępują pojęcia elementu największego ($\max$) i najmniejszego ($\min$), które w zbiorach nieskończonych na ogół nie istnieją.

#### Definicja 1.2 (Ograniczenie zbioru)
Niech $A \subset \mathbb{R}$ będzie zbiorem niepustym.
1. Zbiór $A$ nazywamy **ograniczonym z góry**, jeżeli:
   $$\exists_{M \in \mathbb{R}} \forall_{x \in A} \quad x \le M$$
   Każdą liczbę $M$ o tej własności nazywamy *majorantą* (ograniczeniem górnym) zbioru $A$.
2. Zbiór $A$ nazywamy **ograniczonym z dołu**, jeżeli:
   $$\exists_{m \in \mathbb{R}} \forall_{x \in A} \quad x \ge m$$
   Każdą liczbę $m$ o tej własności nazywamy *minorantą* (ograniczeniem dolnym) zbioru $A$.
3. Zbiór $A$ jest **ograniczony**, gdy jest ograniczony z góry i z dołu:
   $$\exists_{K > 0} \forall_{x \in A} \quad |x| \le K$$

#### Definicja 1.3 (Kres górny - Supremum i kres dolny - Infimum)
1. Liczbę $S \in \mathbb{R}$ nazywamy **kresem górnym** (*supremum*) niepustego zbioru $A \subset \mathbb{R}$ (ozn. $S = \sup A$), jeżeli:
   - $S$ jest ograniczeniem górnym zbioru $A$:
     $$\forall_{x \in A} \quad x \le S$$
   - $S$ jest najmniejszym ograniczeniem górnym (warunek $\varepsilon$-owy):
     $$\forall_{\varepsilon > 0} \exists_{x_0 \in A} \quad x_0 > S - \varepsilon$$
2. Liczbę $s \in \mathbb{R}$ nazywamy **kresem dolnym** (*infimum*) niepustego zbioru $A \subset \mathbb{R}$ (ozn. $s = \inf A$), jeżeli:
   - $s$ jest ograniczeniem dolnym zbioru $A$:
     $$\forall_{x \in A} \quad x \ge s$$
   - $s$ jest największym ograniczeniem dolnym (warunek $\varepsilon$-owy):
     $$\forall_{\varepsilon > 0} \exists_{x_0 \in A} \quad x_0 < s + \varepsilon$$

> **Twierdzenie 1.2 (Twierdzenie o istnieniu kresów):**
> Każdy niepusty zbiór liczb rzeczywistych ograniczony z góry ma kres górny ($S = \sup A \in \mathbb{R}$).  
> Każdy niepusty zbiór liczb rzeczywistych ograniczony z dołu ma kres dolny ($s = \inf A \in \mathbb{R}$).

**Dowód:**
Niech $A \subset \mathbb{R}$ będzie niepustym zbiorem ograniczonym z góry. Zdefiniujmy zbiór $B$ wszystkich majorant zbioru $A$:
$$B = \{b \in \mathbb{R} : \forall_{a \in A} \ a \le b\}$$
Z założenia o ograniczoności $A$ z góry wynika, że $B \neq \emptyset$. Ponadto z definicji zbioru $B$, dla dowolnego $a \in A$ i dowolnego $b \in B$ zachodzi $a \le b$.  
Zdefiniujmy przekrój Dedekinda: niech $A'$ będzie zbiorem wszystkich liczb, które nie są ograniczeniami górnymi zbioru $A$ ($A' = \mathbb{R} \setminus B$). Wówczas $A'$ i $B$ tworzą przekrój Dedekinda.  
Z Aksjomatu Ciągłości istnieje liczba $c \in \mathbb{R}$ rozdzielająca te zbiory, co oznacza, że:
$$\forall_{a \in A} \ a \le c \quad \text{oraz} \quad \forall_{b \in B} \ c \le b$$
Pierwsza nierówność dowodzi, że $c$ jest ograniczeniem górnym zbioru $A$, zatem $c \in B$. Druga nierówność dowodzi, że $c$ jest mniejsze bądź równe od dowolnego ograniczenia górnego ze zbioru $B$. Stąd $c$ jest najmniejszym ograniczeniem górnym, czyli $c = \sup A$. $\blacksquare$

---

### 1.3. Zasada Archimedesa i gęstość podzbiorów liczb

> **Twierdzenie 1.3 (Zasada Archimedesa):**
> Dla dowolnych liczb rzeczywistych $x > 0$ oraz $y \in \mathbb{R}$ istnieje liczba naturalna $n \in \mathbb{N}$ taka, że:
> $$n \cdot x > y$$

**Dowód (nie wprost):**
Załóżmy, że teza nie zachodzi, tzn. $\forall_{n \in \mathbb{N}} \ n x \le y$.  
Wówczas zbiór $Z = \{nx : n \in \mathbb{N}\}$ jest niepusty i ograniczony z góry przez $y$. Na mocy Twierdzenia 1.2 zbiór $Z$ posiada kres górny $S = \sup Z \in \mathbb{R}$.  
Z warunku $\varepsilon$-owego kresu górnego (przyjmując $\varepsilon = x > 0$) istnieje w zbiorze $Z$ element $n_0 x$ taki, że:
$$n_0 x > S - x \implies (n_0 + 1)x > S$$
Lecz liczba $(n_0 + 1)x$ również należy do zbioru $Z$ (gdyż $n_0 + 1 \in \mathbb{N}$). Otrzymaliśmy element zbioru $Z$ ściśle większy od jego kresu górnego $S$, co stanowi sprzeczność. Sprzeczność ta dowodzi prawdziwości zasady Archimedesa. $\blacksquare$

#### Wnioski z zasady Archimedesa:
1. Zbiór liczb naturalnych $\mathbb{N}$ jest nieograniczony z góry w $\mathbb{R}$ ($\sup \mathbb{N} = +\infty$).
2. Dla dowolnego $\varepsilon > 0$ istnieje $n \in \mathbb{N}$ takie, że $\frac{1}{n} < \varepsilon$.
3. Dla każdej liczby rzeczywistej $x \in \mathbb{R}$ istnieje dokładnie jedna liczba całkowita $k \in \mathbb{Z}$ taka, że:
   $$k \le x < k + 1$$
   Liczbę $k$ nazywamy **częścią całkowitą** (cechą, *floor*) liczby $x$ i oznaczamy $\lfloor x \rfloor$ lub $[x]$.

> **Twierdzenie 1.4 (O gęstości zbioru liczb wymiernych $\mathbb{Q}$ w $\mathbb{R}$):**
> Pomiędzy dowolnymi dwoma różnymi liczbami rzeczywistymi $x < y$ leży co najmniej jedna (a zatem nieskończenie wiele) liczba wymierna $q \in \mathbb{Q}$.

**Dowód:**
Ponieważ $y - x > 0$, z zasady Archimedesa istnieje liczba $n \in \mathbb{N}$ taka, że:
$$n(y - x) > 1 \iff ny - nx > 1$$
Niech $m = \lfloor nx \rfloor + 1 \in \mathbb{Z}$. Wtedy z definicji części całkowitej:
$$m - 1 \le nx < m \implies nx < m \le nx + 1$$
Ponieważ $nx + 1 < ny$, mamy:
$$nx < m < ny \implies x < \frac{m}{n} < y$$
Liczba $q = \frac{m}{n}$ jest poszukiwaną liczbą wymierną leżącą pomiędzy $x$ a $y$. $\blacksquare$

> **Twierdzenie 1.5 (O gęstości liczb niewymiernych $\mathbb{R} \setminus \mathbb{Q}$):**
> Pomiędzy dowolnymi dwoma różnymi liczbami rzeczywistymi leży co najmniej jedna liczba niewymierna.

**Dowód:**
Dla $x < y$ rozpatrzmy liczby $\frac{x}{\sqrt{2}} < \frac{y}{\sqrt{2}}$. Z twierdzenia 1.4 istnieje liczba wymierna $q \in \mathbb{Q} \setminus \{0\}$ taka, że:
$$\frac{x}{\sqrt{2}} < q < \frac{y}{\sqrt{2}} \implies x < q\sqrt{2} < y$$
Liczba $w = q\sqrt{2}$ jest niewymierna (iloczyn niezerowej liczby wymiernej i liczby niewymiernej jest niewymierny). $\blacksquare$

---

### 1.4. Fundamentalne nierówności klasyczne

W analizie matematycznej wyznaczanie granic i szacowanie błędów opiera się na zestawie nierówności klasycznych.

#### Twierdzenie 1.6 (Nierówność Bernoulliego)
Dla dowolnej liczby rzeczywistej $x > -1$ oraz dowolnej liczby naturalnej $n \in \mathbb{N}$:
$$(1 + x)^n \ge 1 + n x$$
przy czym równość zachodzi wtedy i tylko wtedy, gdy $n = 1$ lub $x = 0$.

**Dowód (indukcyjny po $n$):**
1. **Baza indukcji ($n = 1$):** $(1 + x)^1 = 1 + 1 \cdot x$ (równość zachodzi).
2. **Krok indukcyjny:** Załóżmy, że $(1 + x)^k \ge 1 + kx$ dla pewnego $k \ge 1$.  
   Mnożąc obie strony przez $(1 + x) > 0$:
   $$(1 + x)^{k+1} = (1 + x)^k(1 + x) \ge (1 + kx)(1 + x) = 1 + x + kx + kx^2 = 1 + (k + 1)x + kx^2$$
   Ponieważ $k x^2 \ge 0$, mamy:
   $$(1 + x)^{k+1} \ge 1 + (k + 1)x$$
Z zasady indukcji matematycznej nierówność zachodzi dla każdego $n \in \mathbb{N}$. $\blacksquare$

#### Twierdzenie 1.7 (Nierówność Cauchy'ego między średnimi AM-GM)
Dla dowolnych liczb nieujemnych $a_1, a_2, \dots, a_n \ge 0$:
$$\frac{a_1 + a_2 + \dots + a_n}{n} \ge \sqrt[n]{a_1 a_2 \dots a_n}$$
Średnia arytmetyczna (AM) jest zawsze większa bądź równa od średniej geometrycznej (GM). Równość zachodzi wtedy i tylko wtedy, gdy $a_1 = a_2 = \dots = a_n$.

#### Twierdzenie 1.8 (Nierówność Cauchy'ego-Schwarza)
Dla dowolnych ciągów liczb rzeczywistych $(a_1, \dots, a_n)$ oraz $(b_1, \dots, b_n)$:
$$\left( \sum_{k=1}^n a_k b_k \right)^2 \le \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)$$

---

### 1.5. Elementy topologii prostej $\mathbb{R}$

Struktura metryczna prostej $\mathbb{R}$ opiera się na wartości bezwzględnej $|x - y|$.

#### Definicja 1.4 (Pojęcia topologiczne)
Niech $E \subset \mathbb{R}$ oraz $x_0 \in \mathbb{R}$:
1. **Otoczenie punktu:** $U(x_0, r) = (x_0 - r, x_0 + r) = \{x \in \mathbb{R} : |x - x_0| < r\}$ dla $r > 0$.
2. **Sąsiedztwo punktu:** $S(x_0, r) = U(x_0, r) \setminus \{x_0\}$.
3. **Punkt wewnętrzny:** Punkt $x_0 \in E$ jest punktem wewnętrznym zbioru $E$, gdy $\exists_{r > 0} \ U(x_0, r) \subset E$. Wnętrze zbioru oznaczamy $\operatorname{Int}(E)$.
4. **Zbiór otwarty:** Zbiór $E$, którego każdy punkt jest punktem wewnętrznym ($E = \operatorname{Int}(E)$).
5. **Punkt skupienia:** Punkt $p \in \mathbb{R}$ jest punktem skupienia zbioru $E$, gdy w każdym jego sąsiedztwie leży co najmniej jeden punkt ze zbioru $E$:
   $$\forall_{r > 0} \quad S(p, r) \cap E \neq \emptyset$$
   Pochodną zbioru (zbiór wszystkich punktów skupienia) oznaczamy $E'$.
6. **Punkt izolowany:** Punkt $x_0 \in E$, który nie jest punktem skupienia zbioru $E$.
7. **Zbiór domknięty:** Zbiór $E$ zawierający wszystkie swoje punkty skupienia ($E' \subset E$). Równoważnie: dopełnienie $\mathbb{R} \setminus E$ jest zbiorem otwartym.
8. **Zbiór zwarty:** Zbiór $E \subset \mathbb{R}$ taki, że z każdego jego pokrycia rodziną przedziałów otwartych można wybrać podpokrycie skończone.

> **Twierdzenie 1.9 (Twierdzenie Heinego-Borela dla prostej $\mathbb{R}$):**
> Podzbiór $E \subset \mathbb{R}$ jest zwarty wtedy i tylko wtedy, gdy jest domknięty i ograniczony.

> **Twierdzenie 1.10 (Twierdzenie Bolzano-Weierstrassa dla zbiorów):**
> Każdy nieskończony i ograniczony podzbiór liczb rzeczywistych posiada co najmniej jeden punkt skupienia w $\mathbb{R}$.

---

## Rozdział 2: Ciało liczb zespolonych $\mathbb{C}$

W inżynierii elektronicznej, teorii obwodów i telekomunikacji liczby zespolone są podstawowym aparatem analizy stanów ustalonych w obwodach prądu zmiennego, opisując amplitudy i przesunięcia fazowe sygnałów harmonicznych za pomocą fazorów.

### 2.1. Aksjomatyczna konstrukcja liczb zespolonych (Pary Hamiltona)

Ciało liczb zespolonych $\mathbb{C}$ definiujemy rygorystycznie jako zbiór par uporządkowanych liczb rzeczywistych $\mathbb{R}^2 = \{(x, y) : x, y \in \mathbb{R}\}$ z dwoma działaniami wewnętrznymi.

#### Definicja 2.1 (Dodawanie i mnożenie w $\mathbb{C}$)
Dla $z_1 = (x_1, y_1)$ oraz $z_2 = (x_2, y_2)$:
1. **Dodawanie:**
   $$z_1 + z_2 = (x_1 + x_2, \ y_1 + y_2)$$
2. **Mnożenie:**
   $$z_1 \cdot z_2 = (x_1 x_2 - y_1 y_2, \ x_1 y_2 + x_2 y_1)$$

Elementem neutralnym dodawania jest $(0, 0)$, a mnożenia $(1, 0)$.  
Elementem przeciwnym do $(x, y)$ jest $(-x, -y)$, a elementem odwrotnym do $(x, y) \neq (0, 0)$ jest para:
$$(x, y)^{-1} = \left( \frac{x}{x^2 + y^2}, \ -\frac{y}{x^2 + y^2} \right)$$

Zbiór par postaci $(x, 0)$ tworzy podciało izomorficzne z ciałem liczb rzeczywistych $\mathbb{R}$:
$$(x_1, 0) + (x_2, 0) = (x_1 + x_2, 0), \quad (x_1, 0) \cdot (x_2, 0) = (x_1 x_2, 0)$$
Utożsamiamy zatem $(x, 0) \equiv x$.

#### Jednostka urojona i postać algebraiczna
Definiujemy **jednostkę urojoną**:
$$i = (0, 1)$$
Zauważmy fundamentalną własność:
$$i^2 = (0, 1) \cdot (0, 1) = (0 \cdot 0 - 1 \cdot 1, \ 0 \cdot 1 + 1 \cdot 0) = (-1, 0) \equiv -1$$

Każdą liczbę zespoloną $(x, y)$ możemy zapisać jednoznacznie jako:
$$(x, y) = (x, 0) + (0, y) = (x, 0) + (0, 1) \cdot (y, 0) = x + iy$$
Zapis:
$$z = x + iy \quad (x, y \in \mathbb{R})$$
nazywamy **postacią algebraiczną** liczby zespolonej:
- $x = \operatorname{Re}(z)$ – część rzeczywista (*Real*),
- $y = \operatorname{Im}(z)$ – część urojona (*Imaginary*).

*(Uwaga: w literaturze elektrotechnicznej stosuje się symbol $j = \sqrt{-1}$ zamiast $i$, aby uniknąć pomyłki z prądem elektrycznym $i(t)$).*

> **Twierdzenie 2.1 (O niemożliwości uporządkowania ciała $\mathbb{C}$):**
> W ciele liczb zespolonych $\mathbb{C}$ nie istnieje relacja porządku $\le$ zgodna ze strukturą ciała.

**Dowód:**
W dowolnym ciele uporządkowanym kwadrat dowolnego niezerowego elementu jest ściśle dodatni ($a \neq 0 \implies a^2 > 0$).  
Dla jedynki $1^2 = 1 > 0$, co implikuje $-1 < 0$.  
Gdyby $\mathbb{C}$ było ciałem uporządkowanym, to dla jednostki urojonej $i \neq 0$ musiałoby zachodzić $i^2 > 0$. Lecz z definicji $i^2 = -1 < 0$, co prowadzi do sprzeczności. Zatem w $\mathbb{C}$ nie ma porządku liniowego zgodnego z działaniami. $\blacksquare$

---

### 2.2. Sprzężenie, moduł i nierówności na płaszczyźnie zespolonej

#### Definicja 2.2 (Sprzężenie zespolone)
Liczbą sprzężoną do $z = x + iy$ nazywamy liczbę:
$$\bar{z} = x - iy$$

#### Własności sprzężenia zespolonego:
1. $\overline{z_1 \pm z_2} = \bar{z}_1 \pm \bar{z}_2$
2. $\overline{z_1 \cdot z_2} = \bar{z}_1 \cdot \bar{z}_2$
3. $\overline{\left( \frac{z_1}{z_2} \right)} = \frac{\bar{z}_1}{\bar{z}_2} \quad (z_2 \neq 0)$
4. $\overline{\bar{z}} = z$
5. $\operatorname{Re}(z) = \frac{z + \bar{z}}{2}, \quad \operatorname{Im}(z) = \frac{z - \bar{z}}{2i}$
6. $z \cdot \bar{z} = x^2 + y^2 \ge 0$

#### Definicja 2.3 (Moduł liczby zespolonej)
Modułem liczby zespolonej $z = x + iy$ nazywamy odległość euklidesową punktu $(x, y)$ od początku układu współrzędnych:
$$|z| = \sqrt{x^2 + y^2} = \sqrt{z \cdot \bar{z}}$$

> **Twierdzenie 2.2 (Nierówności trójkąta i tożsamość równoległoboku):**
> Dla dowolnych $z_1, z_2 \in \mathbb{C}$:
> 1. $|z_1 + z_2| \le |z_1| + |z_2|$ (nierówność trójkąta),
> 2. $\big| |z_1| - |z_2| \big| \le |z_1 - z_2|$ (nierówność trójkąta w dół),
> 3. $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2|z_1|^2 + 2|z_2|^2$ (**tożsamość równoległoboku**: suma kwadratów długości przekątnych równoległoboku jest równa sumie kwadratów wszystkich jego boków).

**Dowód tożsamości równoległoboku:**
Stosując zależność $|w|^2 = w \cdot \bar{w}$:
$$|z_1 + z_2|^2 = (z_1 + z_2)(\bar{z}_1 + \bar{z}_2) = |z_1|^2 + z_1\bar{z}_2 + \bar{z}_1 z_2 + |z_2|^2$$
$$|z_1 - z_2|^2 = (z_1 - z_2)(\bar{z}_1 - \bar{z}_2) = |z_1|^2 - z_1\bar{z}_2 - \bar{z}_1 z_2 + |z_2|^2$$
Dodając obie równości stronami, człony mieszane $z_1\bar{z}_2 + \bar{z}_1 z_2$ ulegają redukcji:
$$|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2|z_1|^2 + 2|z_2|^2 \quad \blacksquare$$

---

### 2.3. Postać trygonometryczna i wykładnicza

Na płaszczyźnie zespolonej Gaussa każdemu punktowi $z = x + iy \neq 0$ odpowiada promień wodzący $r = |z| > 0$ oraz kąt skierowany $\varphi \in \mathbb{R}$:
$$x = r \cos \varphi, \quad y = r \sin \varphi$$
Kąt $\varphi$ nazywamy **argumentem** liczby $z$ ($\arg z$). Zbiór wszystkich argumentów:
$$\arg z = \{\operatorname{Arg} z + 2k\pi : k \in \mathbb{Z}\}$$
gdzie $\operatorname{Arg} z \in (-\pi, \pi]$ jest jednoznacznie wyznaczonym **argumentem głównym**:
$$\operatorname{Arg}(x + iy) = \begin{cases}
\operatorname{arctg}\left(\frac{y}{x}\right) & \text{dla } x > 0 \\
\operatorname{arctg}\left(\frac{y}{x}\right) + \pi & \text{dla } x < 0, y \ge 0 \\
\operatorname{arctg}\left(\frac{y}{x}\right) - \pi & \text{dla } x < 0, y < 0 \\
\frac{\pi}{2} & \text{dla } x = 0, y > 0 \\
-\frac{\pi}{2} & \text{dla } x = 0, y < 0
\end{cases}$$

#### Postać trygonometryczna:
$$z = |z| (\cos \varphi + i \sin \varphi)$$

#### Wzory Eulera i postać wykładnicza:
Definiując funkcję wykładniczą zmiennej urojonej jako:
$$e^{i\varphi} \stackrel{\text{def}}{=} \cos \varphi + i \sin \varphi$$
otrzymujemy **postać wykładniczą**:
$$z = |z| e^{i\varphi}$$

Z tożsamości tej wynikają fundamentalne wzory Eulera:
$$\cos \varphi = \frac{e^{i\varphi} + e^{-i\varphi}}{2}, \quad \sin \varphi = \frac{e^{i\varphi} - e^{-i\varphi}}{2i}$$

> **Twierdzenie 2.3 (Wzór de Moivre'a):**
> Dla dowolnej liczby całkowitej $n \in \mathbb{Z}$ oraz $\varphi \in \mathbb{R}$:
> $$(\cos \varphi + i \sin \varphi)^n = \cos(n\varphi) + i \sin(n\varphi) \iff (e^{i\varphi})^n = e^{in\varphi}$$

**Dowód (indukcyjny dla $n \in \mathbb{N}$):**
1. Dla $n = 1$ tożsamość jest oczywista.
2. Krok indukcyjny: załóżmy, że wzór zachodzi dla $k$. Wtedy:
   $$(\cos \varphi + i \sin \varphi)^{k+1} = (\cos \varphi + i \sin \varphi)^k \cdot (\cos \varphi + i \sin \varphi) = \big(\cos(k\varphi) + i\sin(k\varphi)\big)(\cos \varphi + i\sin \varphi)$$
   Wymnażając:
   $$= \big(\cos(k\varphi)\cos \varphi - \sin(k\varphi)\sin \varphi\big) + i\big(\sin(k\varphi)\cos \varphi + \cos(k\varphi)\sin \varphi\big)$$
   Korzystając ze wzorów na cosinus i sinus sumy kątów:
   $$= \cos\big((k + 1)\varphi\big) + i \sin\big((k + 1)\varphi\big)$$
Dla liczb ujemnych $n = -m$ ($m \in \mathbb{N}$) dowód wynika z definicji elementu odwrotnego. $\blacksquare$

---

### 2.4. Pierwiastkowanie w ciele liczb zespolonych

#### Definicja 2.4 (Pierwiastek $n$-tego stopnia w $\mathbb{C}$)
Niech $z \in \mathbb{C}$ oraz $n \in \mathbb{N}, n \ge 2$. Każdą liczbę $w \in \mathbb{C}$ spełniającą równanie algebraiczne:
$$w^n = z$$
nazywamy pierwiastkiem $n$-tego stopnia z liczby $z$. Zbiór wszystkich pierwiastków oznaczamy $\sqrt[n]{z}$.

> **Twierdzenie 2.4 (O pierwiastkach z liczby zespolonej):**
> Jeżeli $z = r e^{i\varphi} \neq 0$, to istnieje dokładnie $n$ różnych pierwiastków $n$-tego stopnia z liczby $z$, danych wzorem:
> $$w_k = \sqrt[n]{r} \left( \cos \frac{\varphi + 2k\pi}{n} + i \sin \frac{\varphi + 2k\pi}{n} \right) = \sqrt[n]{r} \exp\left( i \frac{\varphi + 2k\pi}{n} \right)$$
> dla wskaźników $k = 0, 1, 2, \dots, n - 1$.

#### Geometryczne rozmieszczenie pierwiastków:
1. Wszystkie pierwiastki mają identyczny moduł: $|w_k| = \sqrt[n]{r}$, zatem leżą na okręgu o środku w punkcie $(0, 0)$ i promieniu $R = \sqrt[n]{r}$.
2. Kąty sąsiednich pierwiastków różnią się o stałą wartość $\Delta \varphi = \frac{2\pi}{n}$.
3. Punkty $w_0, w_1, \dots, w_{n-1}$ tworzą **wierzchołki $n$-kąta foremnego** wpisanego w ten okrąg.

#### Pierwiastki z jedności $\sqrt[n]{1}$:
Dla $z = 1 = 1 \cdot e^{i \cdot 0}$:
$$\varepsilon_k = \cos\frac{2k\pi}{n} + i\sin\frac{2k\pi}{n} = \left( \cos\frac{2\pi}{n} + i\sin\frac{2\pi}{n} \right)^k = \varepsilon_1^k$$
Zbiór pierwiastków z jedności $G_n = \{\varepsilon_0, \varepsilon_1, \dots, \varepsilon_{n-1}\}$ tworzy z działaniem mnożenia **skończoną grupę cykliczną** rzędu $n$, generowaną przez pierwiastek pierwotny $\varepsilon_1 = \exp(i 2\pi/n)$.

---

### 2.5. Zastosowania inżynierskie: Teoria obwodów i analiza sygnałów (WEiTI PW)

W elektrotechnice teoretycznej i telekomunikacji liczby zespolone są podstawowym narzędziem redukującym rozwiązywanie liniowych równań różniczkowych zwyczajnych do prostych działań algebraicznych w ciele $\mathbb{C}$ (**metoda symboliczna Steinmetza**).

#### Sygnał harmoniczny i transformata fazorowa
Sygnał harmoniczny w dziedzinie czasu:
$$u(t) = U_m \cos(\omega t + \psi)$$
gdzie $U_m$ to amplituda, $\omega = 2\pi f$ – pulsacja, $\psi$ – faza początkowa.  
Wykorzystując wzór Eulera:
$$u(t) = \operatorname{Re}\Big( U_m e^{j(\omega t + \psi)} \Big) = \operatorname{Re}\Big( U_m e^{j\psi} e^{j\omega t} \Big) = \operatorname{Re}\Big( \sqrt{2} \underline{U} e^{j\omega t} \Big)$$
gdzie liczbę zespoloną:
$$\underline{U} = \frac{U_m}{\sqrt{2}} e^{j\psi} = U_{\text{RMS}} (\cos \psi + j \sin \psi)$$
nazywamy **wartością skuteczną zespoloną (fazorem)** napięcia.

#### Różniczkowanie i całkowanie w dziedzinie fazorów:
- Różniczkowanie sygnału w czasie odpowiada pomnożeniu fazora przez operator $j\omega$:
  $$\frac{d u(t)}{dt} \longleftrightarrow j\omega \underline{U}$$
- Całkowanie w czasie odpowiada podzieleniu fazora przez operator $j\omega$:
  $$\int u(t) \, dt \longleftrightarrow \frac{1}{j\omega} \underline{U}$$

#### Impedancja zespolona $\underline{Z}$
Równanie konstytutywne obwodu ma postać algebraicznego prawa Ohma:
$$\underline{U} = \underline{Z} \cdot \underline{I}$$
gdzie $\underline{Z} = R + jX$:
- $R = \operatorname{Re}(\underline{Z})$ – rezystancja (opór czynny),
- $X = \operatorname{Im}(\underline{Z})$ – reaktancja (opór bierny).

Odwrotność impedancji nazywamy admitancją zespoloną $\underline{Y} = \frac{1}{\underline{Z}} = G + jB$:
- $G = \operatorname{Re}(\underline{Y})$ – konduktancja,
- $B = \operatorname{Im}(\underline{Y})$ – susceptancja.

#### Elementy podstawowe:
1. **Rezystor $R$:** $u(t) = R i(t) \implies \underline{Z}_R = R$ (prąd i napięcie są w fazie).
2. **Cewka o indukcyjności $L$:** $u_L(t) = L \frac{di(t)}{dt} \implies \underline{U}_L = j\omega L \underline{I} \implies \underline{Z}_L = j\omega L$ (napięcie wyprzedza prąd w fazie o $90^\circ$).
3. **Kondensator o pojemności $C$:** $i_C(t) = C \frac{du(t)}{dt} \implies \underline{I}_C = j\omega C \underline{U} \implies \underline{Z}_C = \frac{1}{j\omega C} = -j\frac{1}{\omega C}$ (prąd wyprzedza napięcie o $90^\circ$).

#### Moc w obwodach prądu zmiennego
Definiujemy **moc zespoloną**:
$$\underline{S} = \underline{U} \cdot \underline{I}^* = P + jQ$$
gdzie $\underline{I}^*$ oznacza sprzężenie zespolone fazora prądu:
- $P = \operatorname{Re}(\underline{S}) = U I \cos \varphi$ – **moc czynna** (w watach [W]), odpowiadająca pracy użytecznej i wydzielaniu ciepła,
- $Q = \operatorname{Im}(\underline{S}) = U I \sin \varphi$ – **moc bierna** (w warach [var]), opisująca oscylacje energii pola magnetycznego i elektrycznego,
- $S = |\underline{S}| = U I = \sqrt{P^2 + Q^2}$ – **moc pozorna** (w woltoamperach [VA]).
- $\cos \varphi = \frac{P}{S}$ – **współczynnik mocy** (*Power Factor*).

---

### 2.6. Wzorcowe przykłady obliczeniowe z pełnym rozwiązaniem

#### Przykład 1.1: Ścisłe wyznaczanie kresów zbioru na podstawie definicji $\varepsilon$
Wyznacz kres górny $\sup A$ oraz kres dolny $\inf A$ dla zbioru:
$$A = \left\{ \frac{3n - 2}{2n + 1} : n \in \mathbb{N} \right\}, \quad \mathbb{N} = \{1, 2, 3, \dots\}$$
oraz przeprowadź formalny dowód na gruncie definicji 1.3.

**Rozwiązanie:**
Przekształćmy postać wyrazu ogólnego $x_n$:
$$x_n = \frac{3n - 2}{2n + 1} = \frac{\frac{3}{2}(2n + 1) - \frac{3}{2} - 2}{2n + 1} = \frac{3}{2} - \frac{7/2}{2n + 1} = \frac{3}{2} - \frac{7}{2(2n + 1)}$$
Zauważmy, że ciąg mianowników $2(2n + 1)$ rośnie wraz z $n$, co oznacza, że ułamek $\frac{7}{2(2n+1)}$ maleje. Zatem ciąg $(x_n)$ jest ściśle rosnący:
$$x_1 = \frac{3(1) - 2}{2(1) + 1} = \frac{1}{3}$$
$$x_2 = \frac{6 - 2}{4 + 1} = \frac{4}{5}, \quad x_3 = \frac{9 - 2}{6 + 1} = 1, \quad \dots, \quad \lim_{n \to \infty} x_n = \frac{3}{2}$$

1. **Wyznaczenie i dowód dla $\inf A$:**
   Podejrzewamy, że $\inf A = \frac{1}{3}$.
   - *Warunek ograniczenia z dołu:* Ponieważ ciąg jest rosnący, dla każdego $n \ge 1$:
     $$x_n \ge x_1 = \frac{1}{3} \implies \forall_{x \in A} \ x \ge \frac{1}{3}$$
   - *Warunek $\varepsilon$-owy:* Ponieważ element $x_1 = \frac{1}{3} \in A$, dla dowolnego $\varepsilon > 0$ wystarczy wskazać element $x_0 = x_1 = \frac{1}{3}$, dla którego zachodzi $x_0 < \frac{1}{3} + \varepsilon$.  
   Zatem $\inf A = \min A = \frac{1}{3}$.

2. **Wyznaczenie i dowód dla $\sup A$:**
   Podejrzewamy, że $\sup A = \frac{3}{2}$.
   - *Warunek majoranty:* Dla każdego $n \in \mathbb{N}$:
     $$\frac{7}{2(2n + 1)} > 0 \implies x_n = \frac{3}{2} - \frac{7}{2(2n + 1)} < \frac{3}{2} \implies \forall_{x \in A} \ x \le \frac{3}{2}$$
   - *Warunek $\varepsilon$-owy:* Niech dany będzie dowolny $\varepsilon > 0$. Poszukujemy wskaźnika $n \in \mathbb{N}$ takiego, że:
     $$x_n > \frac{3}{2} - \varepsilon \iff \frac{3}{2} - \frac{7}{2(2n + 1)} > \frac{3}{2} - \varepsilon \iff \frac{7}{2(2n + 1)} < \varepsilon$$
     Przekształcając nierówność względem $n$:
     $$2(2n + 1) > \frac{7}{\varepsilon} \iff 4n + 2 > \frac{7}{\varepsilon} \iff 4n > \frac{7}{\varepsilon} - 2 \iff n > \frac{7}{4\varepsilon} - \frac{1}{2}$$
     Na mocy Zasady Archimedesa (Tw. 1.3) zawsze istnieje taka liczba naturalna $n_0 \in \mathbb{N}$, że $n_0 > \max\left(1, \left\lfloor \frac{7}{4\varepsilon} - \frac{1}{2} \right\rfloor\right)$.  
     Dla tego wskaźnika element $x_{n_0} \in A$ spełnia żądany warunek $x_{n_0} > \frac{3}{2} - \varepsilon$.

Zatem $\sup A = \frac{3}{2}$. Zbiór nie posiada elementu największego ($\max A$ nie istnieje), ponieważ $\frac{3}{2} \notin A$.

---

#### Przykład 1.2: Równanie z modułem i sprzężeniem zespolonym
Rozwiąż w ciele $\mathbb{C}$ równanie:
$$|z|^2 + \bar{z} = 2 + 4i$$

**Rozwiązanie:**
Niech $z = x + iy$, gdzie $x, y \in \mathbb{R}$. Wtedy:
$$|z|^2 = x^2 + y^2, \quad \bar{z} = x - iy$$
Podstawiamy do równania:
$$(x^2 + y^2) + (x - iy) = 2 + 4i \iff (x^2 + y^2 + x) - iy = 2 + 4i$$
Przyrównujemy części rzeczywiste i urojone obu stron:
$$\begin{cases}
x^2 + y^2 + x = 2 \\
-y = 4 \implies y = -4
\end{cases}$$
Podstawiamy $y = -4$ do pierwszego równania:
$$x^2 + (-4)^2 + x = 2 \iff x^2 + x + 16 = 2 \iff x^2 + x + 14 = 0$$
Obliczamy wyróżnik trójmianu kwadratowego:
$$\Delta = 1^2 - 4 \cdot 1 \cdot 14 = 1 - 56 = -55 < 0$$
Ponieważ szukamy $x \in \mathbb{R}$, ujemny wyróżnik oznacza brak rzeczywistych rozwiązań dla zmiennej $x$.  
**Odpowiedź:** Równanie nie posiada rozwiązań w ciele liczb zespolonych ($z \in \emptyset$).

---

#### Przykład 1.3: Geometria płaszczyzny zespolonej
Wyznacz i narysuj na płaszczyźnie zespolonej Gaussa zbiór punktów spełniających warunek:
$$\left\{ z \in \mathbb{C} : \left| \frac{z - 2i}{z + 1} \right| \ge 1 \land \operatorname{Arg}(z) \in \left[ 0, \frac{3\pi}{4} \right] \right\}$$

**Rozwiązanie:**
1. **Warunek ilorazu modułów:**
   Dla $z \neq -1$:
   $$\left| \frac{z - 2i}{z + 1} \right| \ge 1 \iff |z - 2i| \ge |z - (-1)|$$
   Wyrażenie $|z - z_0|$ oznacza odległość geometryczną punktu $z$ od punktu $z_0$ na płaszczyźnie zespolonej.  
   Równość $|z - 2i| = |z - (-1)|$ opisuje **symetralną odcinka** łączącego punkty $A(0, 2)$ oraz $B(-1, 0)$.  
   Środek odcinka $AB$:
   $$S = \left( \frac{0 + (-1)}{2}, \frac{2 + 0}{2} \right) = \left( -\frac{1}{2}, 1 \right)$$
   Wektor $\vec{AB} = [-1 - 0, 0 - 2] = [-1, -2]$.  
   Równanie symetralnej (prosta prostopadła do $\vec{AB}$ przechodząca przez $S$):
   $$-1 \cdot \left(x + \frac{1}{2}\right) - 2 \cdot (y - 1) = 0 \iff -x - \frac{1}{2} - 2y + 2 = 0 \iff 2x + 4y - 3 = 0 \iff y = -\frac{1}{2}x + \frac{3}{4}$$
   Nierówność $|z - 2i| \ge |z - (-1)|$ oznacza punkty leżące bliżej punktu $B(-1, 0)$ niż punktu $A(0, 2)$, czyli półpłaszczyznę zawierającą punkt $B(-1, 0)$ wraz z prostą graniczną:
   $$2(-1) + 4(0) - 3 = -5 \le 0 \implies 2x + 4y - 3 \le 0$$
2. **Warunek argumentu głównego:**
   $$\operatorname{Arg}(z) \in \left[ 0, \frac{3\pi}{4} \right]$$
   Opisuje obszar kątowy zawarty między dodatnią półosią rzeczywistą $OX$ ($y = 0, x \ge 0$) a półprostą wychodzącą z początku układu nachyloną pod kątem $135^\circ$ ($y = -x$ dla $x \le 0, y \ge 0$).
3. **Część wspólna:**
   Szukanym zbiorem jest przecięcie domkniętej półpłaszczyzny $2x + 4y \le 3$ z wycinkiem kątowym $\operatorname{Arg}(z) \in [0, 3\pi/4]$, z wyłączeniem punktu osobliwego $z = -1$.

---

#### Przykład 1.4: Pełna analiza obwodu RLC w dziedzinie fazorów
W obwodzie szeregowym RLC dane są wartości elementów:
$$R = 30\,\Omega, \quad L = 160\text{ mH}, \quad C = 100\,\mu\text{F}$$
Obwód zasilany jest napięciem harmonicznym $u(t) = 230\sqrt{2} \cos(100\pi t + 30^\circ)\text{ V}$.
1. Wyznacz pulsację $\omega$, częstotliwość $f$ oraz fazor wartości skutecznej napięcia $\underline{U}$.
2. Oblicz impedancję zespoloną obwodu $\underline{Z}$ oraz jej moduł i kąt fazowy.
3. Wyznacz fazor prądu $\underline{I}$ oraz postać czasową prądu $i(t)$.
4. Oblicz moc czynną $P$, bierną $Q$ oraz moc pozorną $S$.

**Rozwiązanie:**
1. **Parametry sygnału wymuszającego:**
   - Pulsacja: $\omega = 100\pi \approx 314{,}16\text{ rad/s}$,
   - Częstotliwość: $f = \frac{\omega}{2\pi} = 50\text{ Hz}$ (sieć europejska),
   - Amplituda napięcia: $U_m = 230\sqrt{2}\text{ V} \implies U = U_{\text{RMS}} = 230\text{ V}$,
   - Faza początkowa: $\psi_u = 30^\circ = \frac{\pi}{6}\text{ rad}$,
   - Fazor wartości skutecznej:
     $$\underline{U} = 230 e^{j 30^\circ}\text{ V} = 230 \left( \frac{\sqrt{3}}{2} + j \frac{1}{2} \right) = 115\sqrt{3} + j 115\text{ V} \approx 199{,}19 + j 115\text{ V}$$
2. **Impedancja elementów i obwodu:**
   - Reaktancja indukcyjna:
     $$X_L = \omega L = 100\pi \cdot 0{,}16 = 16\pi \approx 50{,}27\,\Omega \implies \underline{Z}_L = j 50{,}27\,\Omega$$
   - Reaktancja pojemnościowa:
     $$X_C = \frac{1}{\omega C} = \frac{1}{100\pi \cdot 100 \cdot 10^{-6}} = \frac{100}{\pi} \approx 31{,}83\,\Omega \implies \underline{Z}_C = -j 31{,}83\,\Omega$$
   - Reaktancja wypadkowa:
     $$X = X_L - X_C = 50{,}27 - 31{,}83 = 18{,}44\,\Omega \quad (\text{charakter indukcyjny, } X > 0)$$
   - Impedancja zespolona całkowita:
     $$\underline{Z} = R + jX = 30 + j 18{,}44\,\Omega$$
   - Moduł impedancji:
     $$|\underline{Z}| = \sqrt{R^2 + X^2} = \sqrt{30^2 + 18{,}44^2} = \sqrt{900 + 340{,}03} = \sqrt{1240{,}03} \approx 35{,}21\,\Omega$$
   - Kąt fazowy impedancji:
     $$\varphi = \operatorname{arctg}\left(\frac{X}{R}\right) = \operatorname{arctg}\left(\frac{18{,}44}{30}\right) \approx \operatorname{arctg}(0{,}6147) \approx 31{,}58^\circ \approx 0{,}551\text{ rad}$$
   Zatem $\underline{Z} = 35{,}21 e^{j 31{,}58^\circ}\,\Omega$.
3. **Fazor prądu i postać czasowa:**
   Z prawa Ohma:
   $$\underline{I} = \frac{\underline{U}}{\underline{Z}} = \frac{230 e^{j 30^\circ}}{35{,}21 e^{j 31{,}58^\circ}} \approx 6{,}532 e^{j(30^\circ - 31{,}58^\circ)} = 6{,}532 e^{-j 1{,}58^\circ}\text{ A}$$
   Wartość skuteczna prądu wynosi $I \approx 6{,}532\text{ A}$, a faza początkowa $\psi_i = -1{,}58^\circ$.  
   Amplituda prądu: $I_m = I \sqrt{2} = 6{,}532 \sqrt{2} \approx 9{,}238\text{ A}$.  
   Postać czasowa prądu:
   $$i(t) = 9{,}238 \cos(100\pi t - 1{,}58^\circ)\text{ A}$$
4. **Bilans mocy:**
   - Kąt przesunięcia fazowego między napięciem a prądem: $\varphi = \psi_u - \psi_i = 30^\circ - (-1{,}58^\circ) = 31{,}58^\circ$.
   - Współczynnik mocy: $\cos \varphi = \cos(31{,}58^\circ) \approx 0{,}8519$.
   - **Moc czynna:**
     $$P = U I \cos \varphi = 230 \cdot 6{,}532 \cdot 0{,}8519 \approx 1280\text{ W} = 1{,}28\text{ kW}$$
     *(Weryfikacja: $P = I^2 R = (6{,}532)^2 \cdot 30 = 42{,}667 \cdot 30 = 1280\text{ W}$ – pełna zgodność).*
   - **Moc bierna:**
     $$Q = U I \sin \varphi = 230 \cdot 6{,}532 \cdot \sin(31{,}58^\circ) = 1502{,}36 \cdot 0{,}5237 \approx 786{,}8\text{ var}$$
     *(Weryfikacja: $Q = I^2 X = 42{,}667 \cdot 18{,}44 = 786{,}8\text{ var}$).*
   - **Moc pozorna:**
     $$S = U I = 230 \cdot 6{,}532 \approx 1502{,}4\text{ VA}$$
     $$S = \sqrt{P^2 + Q^2} = \sqrt{1280^2 + 786{,}8^2} = \sqrt{1638400 + 619054} = \sqrt{2257454} \approx 1502{,}5\text{ VA}$$

---

### 2.7. Zestaw zadań do samodzielnego rozwiązania

1. **Zadanie 1.1:** Udowodnij za pomocą zasady Archimedesa, że dla zbioru $A = \left\{ 1 - \frac{1}{n^2} : n \in \mathbb{N} \right\}$ zachodzi $\sup A = 1$ oraz $\inf A = 0$.
2. **Zadanie 1.2:** Wykaż, że liczba $\log_{10}(3)$ jest liczbą niewymierną.
3. **Zadanie 1.3:** Udowodnij metodą indukcji matematycznej nierówność: $\frac{1}{2n} \le \frac{1 \cdot 3 \cdot 5 \dots (2n-1)}{2 \cdot 4 \cdot 6 \dots 2n} \le \frac{1}{\sqrt{2n+1}}$ dla każdego $n \in \mathbb{N}$.
4. **Zadanie 1.4:** Rozwiąż w ciele $\mathbb{C}$ równanie: $z^3 = \bar{z}$.
5. **Zadanie 1.5:** Wyznacz część rzeczywistą i urojoną liczby $z = (1 - i\sqrt{3})^{15}$.
6. **Zadanie 1.6:** Wyznacz wszystkie zespolone rozwiązania równania dwukwadratowego: $z^4 - 2z^2 + 4 = 0$.
7. **Zadanie 1.7:** Zapisz w postaci algebraicznej wszystkie pierwiastki stopnia 6 z liczby $z = -64$.
8. **Zadanie 1.8 (Mostek Wiena):** W układzie mostka Wiena impedancje gałęzi tworzą szeregowe połączenie $R_1, C_1$ oraz równoległe $R_2, C_2$. Wykaż, że mostek znajduje się w stanie równowagi fazowej przy pulsacji rezonansowej $\omega_0 = \frac{1}{\sqrt{R_1 R_2 C_1 C_2}}$, a dla $R_1 = R_2 = R$ oraz $C_1 = C_2 = C$ pulsacja wynosi $\omega_0 = \frac{1}{RC}$.

---

### Odpowiedzi i wskazówki do zadań

- **1.1:** Dla $n = 1$: $x_1 = 0 \in A \implies \inf A = \min A = 0$. Ponieważ $1/n^2 > 0$, $x_n < 1$. Dla dowolnego $\varepsilon > 0$ warunek $1 - 1/n^2 > 1 - \varepsilon \iff n^2 > 1/\varepsilon \iff n > 1/\sqrt{\varepsilon}$ jest spełniony z zasady Archimedesa. Stąd $\sup A = 1$.
- **1.2:** Dowód nie wprost: załóżmy $\log_{10} 3 = \frac{p}{q}$, gdzie $p, q \in \mathbb{N}$. Wtedy $10^{p/q} = 3 \implies 10^p = 3^q \implies 2^p \cdot 5^p = 3^q$. Lewa strona jest parzysta i podzielna przez 5, prawa jest nieparzysta i niepodzielna przez 5, co przeczy jednoznaczności rozkładu liczb naturalnych na czynniki pierwsze (Zasadnicze Twierdzenie Arytmetyki).
- **1.3:** Standardowa indukcja matematyczna; w kroku indukcyjnym wystarczy dowieść nierówność $\frac{2k+1}{2k+2} \le \frac{\sqrt{2k+1}}{\sqrt{2k+3}} \iff (2k+1)(2k+3) \le (2k+2)^2 \iff 4k^2 + 8k + 3 \le 4k^2 + 8k + 4$, co jest tożsamościowo prawdziwe.
- **1.4:** Moduł obu stron: $|z|^3 = |\bar{z}| = |z| \implies |z|(|z|^2 - 1) = 0$. Stąd $|z| = 0 \implies z = 0$ lub $|z| = 1$. Dla $|z| = 1$ mnożymy obustronnie przez $z$: $z^4 = z \bar{z} = |z|^2 = 1$. Rozwiązaniami są pierwiastki czwartego stopnia z jedności: $z \in \{0, 1, -1, i, -i\}$ (łącznie 5 rozwiązań).
- **1.5:** Moduł $|1 - i\sqrt{3}| = 2$, argument główny $\varphi = -\frac{\pi}{3}$. Zatem $z = (2 e^{-i\pi/3})^{15} = 2^{15} e^{-i 5\pi} = 32768 (\cos(-5\pi) + i\sin(-5\pi)) = 32768(-1 + 0) = -32768$. $\operatorname{Re}(z) = -32768, \operatorname{Im}(z) = 0$.
- **1.6:** Podstawienie $t = z^2$: $t^2 - 2t + 4 = 0 \implies \Delta = 4 - 16 = -12 = (j 2\sqrt{3})^2 \implies t_{1,2} = 1 \pm j\sqrt{3} = 2 e^{\pm j\pi/3}$. Pierwiastkując: $z = \sqrt{t} \implies z_1 = \sqrt{2} e^{j\pi/6} = \sqrt{2}\left(\frac{\sqrt{3}}{2} + j\frac{1}{2}\right) = \frac{\sqrt{6} + j\sqrt{2}}{2}$, $z_2 = -z_1$, $z_3 = \frac{\sqrt{6} - j\sqrt{2}}{2}$, $z_4 = -z_3$.
- **1.7:** $z = -64 = 64 e^{j\pi}$. Moduł pierwiastków: $\sqrt[6]{64} = 2$. Kąty: $\varphi_k = \frac{\pi + 2k\pi}{6} = \frac{\pi}{6} + k \frac{\pi}{3}$ dla $k = 0, \dots, 5$. $w_0 = \sqrt{3} + j, \ w_1 = 2j, \ w_2 = -\sqrt{3} + j, \ w_3 = -\sqrt{3} - j, \ w_4 = -2j, \ w_5 = \sqrt{3} - j$.
- **1.8:** Warunek równowagi mostka napięciowego $\underline{Z}_1 / \underline{Z}_2 = R_3 / R_4 \in \mathbb{R}$. Impedancja gałęzi szeregowej: $\underline{Z}_1 = R_1 + \frac{1}{j\omega C_1} = \frac{1 + j\omega R_1 C_1}{j\omega C_1}$. Admitancja gałęzi równoległej: $\underline{Y}_2 = \frac{1}{R_2} + j\omega C_2 = \frac{1 + j\omega R_2 C_2}{R_2} \implies \underline{Z}_2 = \frac{R_2}{1 + j\omega R_2 C_2}$. Iloraz: $\frac{\underline{Z}_1}{\underline{Z}_2} = \underline{Z}_1 \underline{Y}_2 = \frac{(1 + j\omega R_1 C_1)(1 + j\omega R_2 C_2)}{j\omega R_2 C_1} = \frac{(1 - \omega^2 R_1 R_2 C_1 C_2) + j\omega(R_1 C_1 + R_2 C_2)}{j\omega R_2 C_1} = \frac{R_1 C_1 + R_2 C_2}{R_2 C_1} + \frac{1 - \omega^2 R_1 R_2 C_1 C_2}{j\omega R_2 C_1}$. Aby iloraz był czysto rzeczywisty, część urojona musi znikać: $1 - \omega^2 R_1 R_2 C_1 C_2 = 0 \implies \omega_0 = \frac{1}{\sqrt{R_1 R_2 C_1 C_2}}$.
