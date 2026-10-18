# Analiza Matematyczna dla Informatyków i Elektroników
## Podręcznik akademicki dla studentów Wydziału Elektroniki i Technik Informacyjnych Politechniki Warszawskiej (WEiTI PW)
### Opracowany według kanonu dydaktycznego prof. W. Żakowskiego i doc. J. Decewicza

---

# TOM I: Funkcje Jednej Zmiennej, Szeregi i Rachunek Całkowy

\newpage

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


\newpage

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


\newpage

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


\newpage

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


\newpage

# Część V: Rachunek Różniczkowy Funkcji Jednej Zmiennej

Rachunek różniczkowy jest jednym z najdoskonalszych instrumentów analizy matematycznej. Umożliwia precyzyjne badanie lokalnego tempa zmian wielkości fizycznych, aproksymację zjawisk nieliniowych za pomocą modeli liniowych w otoczeniu punktu pracy oraz wyznaczanie optymalnych parametrów pracy układów. W informatyce pochodna stanowi kręgosłup uczenia maszynowego (algorytmy spadku gradientowego i wstecznej propagacji błędów), a w elektrotechnice opisuje relacje konstytutywne elementów reakcyjnych ($L, C$).

---

## Rozdział 9: Pochodna i różniczka funkcji

### 9.1. Definicja pochodnej i interpretacja fizyczno-geometryczna

Niech funkcja $f: X \to \mathbb{R}$ będzie określona w otoczeniu punktu $x_0 \in X$.

#### Definicja 9.1 (Iloraz różnicowy i pochodna)
1. **Ilorazem różnicowym** funkcji $f$ w punkcie $x_0$ odpowiadającym przyrostowi argumentu $\Delta x \neq 0$ nazywamy wyrażenie:
   $$\frac{\Delta f}{\Delta x} = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}$$
2. Jeżeli istnieje granica właściwa ilorazu różnicowego przy $\Delta x \to 0$, to granicę tę nazywamy **pochodną funkcji $f$ w punkcie $x_0$** i oznaczamy $f'(x_0)$ lub $\frac{df}{dx}(x_0)$:
   $$f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x} = \lim_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}$$

Funkcję posiadającą skończoną pochodną w punkcie $x_0$ nazywamy **różniczkowalną w punkcie $x_0$**.

#### Interpretacje pochodnej:
1. **Interpretacja geometryczna:**  
   Pochodna $f'(x_0)$ określa współczynnik kierunkowy (tangens kąta nachylenia $\alpha$) prostej stycznej do wykresu funkcji $y = f(x)$ w punkcie $P_0(x_0, f(x_0))$:
   $$m = \operatorname{tg} \alpha = f'(x_0)$$
   Równanie prostej **stycznej**:
   $$y - f(x_0) = f'(x_0)(x - x_0)$$
   Równanie prostej **normalnej** (prostopadłej do stycznej w punkcie styczności, gdy $f'(x_0) \neq 0$):
   $$y - f(x_0) = -\frac{1}{f'(x_0)}(x - x_0)$$

2. **Interpretacja fizyczna (Elektrotechnika i Teoria Sygnałów):**  
   - **Prąd elektryczny:** Prąd $i(t)$ jest pochodną ładunku elektrycznego $q(t)$ przepływającego przez przekrój poprzeczny przewodnika:
     $$i(t) = \frac{dq(t)}{dt}$$
   - **Napięcie na indukcyjności (Cewka):** Z prawa indukcji elektromagnetycznej Faradaya napięcie na cewce $L$ jest proporcjonalne do pochodnej natężenia prądu:
     $$u_L(t) = L \frac{di(t)}{dt}$$
   - **Prąd na pojemności (Kondensator):** Prąd ładujący kondensator o pojemności $C$ jest proporcjonalny do pochodnej napięcia:
     $$i_C(t) = C \frac{du_C(t)}{dt}$$

---

### 9.2. Ciągłość a różniczkowalność

> **Twierdzenie 9.1 (O ciągłości funkcji różniczkowalnej):**  
> Jeżeli funkcja $f$ jest różniczkowalna w punkcie $x_0$, to jest w tym punkcie ciągła.

**Dowód:**  
Dla $x \neq x_0$ zapiszmy tożsamość:
$$f(x) - f(x_0) = \frac{f(x) - f(x_0)}{x - x_0} \cdot (x - x_0)$$
Przechodząc do granicy przy $x \to x_0$:
$$\lim_{x \to x_0} \big( f(x) - f(x_0) \big) = \lim_{x \to x_0} \left[ \frac{f(x) - f(x_0)}{x - x_0} \right] \cdot \lim_{x \to x_0} (x - x_0) = f'(x_0) \cdot 0 = 0$$
Stąd $\lim_{x \to x_0} f(x) = f(x_0)$, co dowodzi ciągłości w punkcie $x_0$. $\blacksquare$

> **Uwaga krytyczna:**  
> Ciągłość jest warunkiem **koniecznym**, lecz **niewystarczającym** dla różniczkowalności!  
> Funkcja $f(x) = |x|$ jest ciągła w punkcie $x_0 = 0$, lecz pochodne jednostronne są różne:
> $$f'_-(0) = \lim_{x \to 0^-} \frac{|x| - 0}{x} = -1 \neq f'_+(0) = \lim_{x \to 0^+} \frac{|x| - 0}{x} = +1$$
> Istnieją nawet funkcje ciągłe na całym $\mathbb{R}$, które nie posiadają pochodnej w **żadnym punkcie** (funkcja Weierstrassa $W(x) = \sum_{n=0}^\infty a^n \cos(b^n \pi x)$).

---

### 9.3. Podstawowe reguły różniczkowania

> **Twierdzenie 9.2 (Reguły różniczkowania):**  
> Niech funkcje $f$ i $g$ będą różniczkowalne w punkcie $x$:
> 1. **Liniowość:** $(\alpha f + \beta g)'(x) = \alpha f'(x) + \beta g'(x) \quad (\alpha, \beta \in \mathbb{R})$,
> 2. **Pochodna iloczynu:** $(f \cdot g)'(x) = f'(x)g(x) + f(x)g'(x)$,
> 3. **Pochodna ilorazu:** $\left( \frac{f}{g} \right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2} \quad (g(x) \neq 0)$,
> 4. **Reguła łańcuchowa (pochodna złożenia):** $(f \circ g)'(x) = f'(g(x)) \cdot g'(x)$,
> 5. **Pochodna funkcji odwrotnej:** Jeżeli $f$ jest ściśle monotoniczna i różniczkowalna w $x_0$ oraz $f'(x_0) \neq 0$, to funkcja odwrotna $f^{-1}$ jest różniczkowalna w punkcie $y_0 = f(x_0)$ i:
>    $$(f^{-1})'(y_0) = \frac{1}{f'(x_0)} = \frac{1}{f'(f^{-1}(y_0))}$$

#### Pochodna logarytmiczna:
Dla funkcji postaci $y = [u(x)]^{v(x)}$ ($u(x) > 0$):
$$\ln y = v(x) \ln u(x) \implies \frac{y'}{y} = v'(x)\ln u(x) + v(x)\frac{u'(x)}{u(x)}$$
$$y' = [u(x)]^{v(x)} \left( v'(x) \ln u(x) + \frac{v(x) u'(x)}{u(x)} \right)$$

#### Wzór Leibniza na $n$-tą pochodną iloczynu:
Dla funkcji $n$-krotnie różniczkowalnych:
$$(f \cdot g)^{(n)}(x) = \sum_{k=0}^n \binom{n}{k} f^{(k)}(x) g^{(n-k)}(x)$$

---

### 9.4. Różniczka funkcji i jej zastosowania inżynierskie

#### Definicja 9.2 (Różniczka funkcji)
Jeżeli funkcja $f$ jest różniczkowalna w punkcie $x_0$, to wyrażenie:
$$df(x_0, \Delta x) = f'(x_0) \Delta x = f'(x_0) dx$$
liniowe względem przyrostu argumentu $dx = \Delta x$, nazywamy **różniczką funkcji $f$ w punkcie $x_0$**.

Rzeczywisty przyrost funkcji wynosi:
$$\Delta f = f(x_0 + \Delta x) - f(x_0) = f'(x_0)\Delta x + \alpha(\Delta x)\cdot \Delta x = df + o(\Delta x)$$
Różniczka stanowi zatem **liniową część główną przyrostu funkcji**, co pozwala na linearyzację w otoczeniu punktu pracy:
$$f(x_0 + \Delta x) \approx f(x_0) + f'(x_0)\Delta x$$

#### Zastosowanie w teorii obwodów: Linearyzacja nieliniowości małosygnałowych
W złączu p-n diody półprzewodnikowej prąd zależy nieliniowo od napięcia według równania Shockleya:
$$I_D = I_S \left( e^{\frac{U_D}{n V_T}} - 1 \right)$$
W stałoprądowym punkcie pracy $Q(U_{D0}, I_{D0})$ małym zmianom napięcia $u_d(t)$ odpowiada przyrost prądu opisany różniczką:
$$i_d(t) \approx \left. \frac{dI_D}{dU_D} \right|_{Q} \cdot u_d(t) = g_d \cdot u_d(t)$$
Wielkość $g_d = \frac{1}{r_d} = \frac{I_{D0} + I_S}{n V_T} \approx \frac{I_{D0}}{n V_T}$ jest **konduktancją dynamiczną** diody. Pozwala to na zastąpienie nieliniowego elementu rezystorem liniowym $r_d$ dla małych sygnałów zmiennych.

---

## Rozdział 10: Twierdzenia o wartości średniej i wzór Taylora

### 10.1. Twierdzenia Rolle'a, Lagrange'a i Cauchy'ego

> **Lemat Fermata (Warunek konieczny istnienia ekstremum funkcji różniczkowalnej):**  
> Jeżeli funkcja $f$ ma w punkcie $x_0 \in (a, b)$ ekstremum lokalne i jest w nim różniczkowalna, to:
> $$f'(x_0) = 0$$

**Dowód:**  
Niech w $x_0$ będzie maksimum lokalne. Wtedy dla małych $h > 0$: $\frac{f(x_0+h)-f(x_0)}{h} \le 0 \implies f'_+(x_0) \le 0$.  
Dla małych $h < 0$: $\frac{f(x_0+h)-f(x_0)}{h} \ge 0 \implies f'_-(x_0) \ge 0$.  
Z różniczkowalności $f'_+(x_0) = f'_-(x_0) = f'(x_0) \implies f'(x_0) = 0$. $\blacksquare$

> **Twierdzenie 10.1 (Rolle'a):**  
> Jeżeli funkcja $f: [a, b] \to \mathbb{R}$ jest ciągła na $[a, b]$, różniczkowalna na $(a, b)$ oraz $f(a) = f(b)$, to istnieje co najmniej jeden punkt $c \in (a, b)$ taki, że:
> $$f'(c) = 0$$

**Dowód:**  
Z II twierdzenia Weierstrassa funkcja $f$ osiąga na $[a, b]$ swój kres dolny $m$ i górny $M$.  
- Jeżeli $m = M$, to $f$ jest funkcją stałą i $f'(x) = 0$ dla każdego $x \in (a, b)$.  
- Jeżeli $m < M$, to ponieważ $f(a) = f(b)$, co najmniej jeden z kresów musi być osiągany w punkcie wewnętrznym $c \in (a, b)$. W punkcie tym $f$ posiada ekstremum lokalne, skąd z Lematu Fermata $f'(c) = 0$. $\blacksquare$

> **Twierdzenie 10.2 (Lagrange'a o wartości średniej):**  
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$ i różniczkowalna na $(a, b)$, to istnieje punkt $c \in (a, b)$ taki, że:
> $$\frac{f(b) - f(a)}{b - a} = f'(c) \iff f(b) - f(a) = f'(c)(b - a)$$

**Dowód:**  
Wprowadzamy funkcję pomocniczą opisującą odchylenie wykresu od cięciwy łączącej punkty $(a, f(a))$ i $(b, f(b))$:
$$\varphi(x) = f(x) - f(a) - \frac{f(b) - f(a)}{b - a}(x - a)$$
Funkcja $\varphi$ spełnia założenia twierdzenia Rolle'a: jest ciągła na $[a, b]$, różniczkowalna na $(a, b)$ oraz $\varphi(a) = \varphi(b) = 0$. Zatem istnieje $c \in (a, b)$ takie, że $\varphi'(c) = 0$:
$$\varphi'(c) = f'(c) - \frac{f(b) - f(a)}{b - a} = 0 \implies f'(c) = \frac{f(b) - f(a)}{b - a} \quad \blacksquare$$

> **Twierdzenie 10.3 (Cauchy'ego o wartości średniej):**  
> Jeżeli funkcje $f, g$ są ciągłe na $[a, b]$, różniczkowalne na $(a, b)$ oraz $g'(x) \neq 0$ na $(a, b)$, to istnieje punkt $c \in (a, b)$ taki, że:
> $$\frac{f(b) - f(a)}{g(b) - g(a)} = \frac{f'(c)}{g'(c)}$$

---

### 10.2. Reguła de l'Hospitala

> **Twierdzenie 10.4 (Reguła de l'Hospitala):**  
> Niech funkcje $f$ i $g$ będą różniczkowalne w sąsiedztwie $S(x_0)$ oraz $g'(x) \neq 0$. Jeżeli:
> 1. $\lim_{x \to x_0} f(x) = \lim_{x \to x_0} g(x) = 0 \quad (\text{symbol } [0/0])$  
> lub  
> 2. $\lim_{x \to x_0} |g(x)| = +\infty \quad (\text{symbol } [\infty/\infty])$,  
> oraz istnieje granica (właściwa lub niewłaściwa):
> $$\lim_{x \to x_0} \frac{f'(x)}{g'(x)} = K$$
> to istnieje również granica wyjściowa i:
> $$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{x \to x_0} \frac{f'(x)}{g'(x)} = K$$

**Dowód dla przypadku $[0/0]$ w punkcie $x_0$:**  
Kładziemy $f(x_0) = 0$ oraz $g(x_0) = 0$, rozszerzając obie funkcje w sposób ciągły na punkt $x_0$.  
Dla dowolnego $x \in S(x_0)$ funkcje $f$ i $g$ spełniają założenia twierdzenia Cauchy'ego o wartości średniej na przedziale o końcach $x_0$ i $x$. Istnieje zatem punkt $c$ leżący ściśle między $x_0$ a $x$ taki, że:
$$\frac{f(x)}{g(x)} = \frac{f(x) - f(x_0)}{g(x) - g(x_0)} = \frac{f'(c)}{g'(c)}$$
Gdy $x \to x_0$, to na mocy twierdzenia o trzech funkcjach również $c \to x_0$. Przechodząc do granicy:
$$\lim_{x \to x_0} \frac{f(x)}{g(x)} = \lim_{c \to x_0} \frac{f'(c)}{g'(c)} = K \quad \blacksquare$$

---

### 10.3. Wzór Taylora i Maclaurina

> **Twierdzenie 10.5 (Wzór Taylora z resztą w postaci Lagrange'a i Peano):**  
> Jeżeli funkcja $f$ ma ciągłe pochodne do rzędu $n$ w otoczeniu $U(x_0)$ oraz posiada pochodną rzędu $(n+1)$ w tym otoczeniu, to dla każdego $x \in U(x_0)$:
> $$f(x) = \sum_{k=0}^n \frac{f^{(k)}(x_0)}{k!} (x - x_0)^k + R_n(x)$$
> gdzie reszta $R_n(x)$ może być zapisana jako:
> - **Postać Lagrange'a:** $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!} (x - x_0)^{n+1}$ dla pewnego $c \in (x_0, x)$,
> - **Postać Peano:** $R_n(x) = o\big((x - x_0)^n\big)$ przy $x \to x_0$.

Gdy $x_0 = 0$, wzór nazywamy **wzorem Maclaurina**.

#### Standardowe rozwinięcia Maclaurina:
1. $e^x = \sum_{k=0}^n \frac{x^k}{k!} + o(x^n) = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots + \frac{x^n}{n!} + o(x^n)$
2. $\sin x = \sum_{k=0}^n \frac{(-1)^k x^{2k+1}}{(2k+1)!} + o(x^{2n+2}) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$
3. $\cos x = \sum_{k=0}^n \frac{(-1)^k x^{2k}}{(2k)!} + o(x^{2n+1}) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$
4. $\ln(1 + x) = \sum_{k=1}^n \frac{(-1)^{k-1} x^k}{k} + o(x^n) = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$
5. $(1 + x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2!} x^2 + \dots + \binom{\alpha}{n} x^n + o(x^n)$
6. $\frac{1}{1 - x} = 1 + x + x^2 + \dots + x^n + o(x^n)$

---

## Rozdział 11: Badanie przebiegu zmienności funkcji

### 11.1. Monotoniczność i ekstrema lokalne

1. **Kryteria monotoniczności:**
   - Jeżeli $f'(x) > 0$ na $(a, b)$, to funkcja jest ściśle rosnąca na $(a, b)$.
   - Jeżeli $f'(x) < 0$ na $(a, b)$, to funkcja jest ściśle malejąca na $(a, b)$.
2. **Kryterium I pochodnej (warunek wystarczający istnienia ekstremum):**  
   Niech $x_0$ będzie punktem krytycznym ($f'(x_0) = 0$ lub $f'(x_0)$ nie istnieje):
   - zmiana znaku z $+$ na $-$ $\implies$ **maksimum lokalne właściwe**,
   - zmiana znaku z $-$ na $+$ $\implies$ **minimum lokalne właściwe**,
   - brak zmiany znaku $\implies$ brak ekstremum.
3. **Kryterium II pochodnej:**  
   Niech $f'(x_0) = 0$.
   - Jeżeli $f''(x_0) < 0$, to w $x_0$ występuje **maksimum lokalne właściwe**.
   - Jeżeli $f''(x_0) > 0$, to w $x_0$ występuje **minimum lokalne właściwe**.
   - Jeżeli $f''(x_0) = 0$, kryterium nie rozstrzyga (należy badać wyższe pochodne lub zmianę znaku I pochodnej).

---

### 11.2. Wypukłość, wklęsłość i punkty przegięcia

1. **Definicja geometryczna:** Funkcja $f$ jest **wypukła** na przedziale, jeżeli wykres funkcji leży pod każdą cięciwą łączącą dwa punkty wykresu (oraz nad każdą styczną). Funkcja jest **wklęsła**, jeżeli leży nad cięciwami (i pod stycznymi).
2. **Kryteria II pochodnej:**
   - $f''(x) > 0$ na $(a, b) \implies$ funkcja jest ściśle wypukła na $(a, b)$,
   - $f''(x) < 0$ na $(a, b) \implies$ funkcja jest ściśle wklęsła na $(a, b)$.
3. **Punkt przegięcia:** Punkt $(x_0, f(x_0))$ wykresu, w którym funkcja zmienia charakter z wypukłej na wklęsłą (lub odwrotnie). Styczna do wykresu w punkcie przegięcia przecina wykres funkcji!
   - *Warunek konieczny:* $f''(x_0) = 0$ (lub $f''$ nie istnieje).
   - *Warunek dostateczny:* zmiana znaku $f''(x)$ przy przejściu przez $x_0$.

---

### 11.3. Asymptoty wykresu funkcji

1. **Asymptota pionowa $x = x_0$:**  
   Występuje, gdy co najmniej jedna z granic jednostronnych jest nieskończona:
   $$\lim_{x \to x_0^-} f(x) = \pm\infty \quad \text{lub} \quad \lim_{x \to x_0^+} f(x) = \pm\infty$$
2. **Asymptota ukośna $y = ax + b$ (w $+\infty$ lub $-\infty$):**
   $$a = \lim_{x \to \pm\infty} \frac{f(x)}{x}, \quad b = \lim_{x \to \pm\infty} \big( f(x) - ax \big)$$
   Jeżeli $a = 0$, prosta $y = b$ jest **asymptotą poziomą**.

---

### 11.4. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 11.1 (Reguła de l'Hospitala dla potęgi $[1^\infty]$)
Obliczyć granicę:
$$\lim_{x \to 0} \left( \frac{\sin x}{x} \right)^{1/x^2}$$

**Rozwiązanie:**  
Przekształcamy tożsamością wykładniczą:
$$\left( \frac{\sin x}{x} \right)^{1/x^2} = \exp\left( \frac{\ln(\sin x / x)}{x^2} \right)$$
Badamy granicę wykładnika $L = \lim_{x \to 0} \frac{\ln(\sin x / x)}{x^2} = \left[\frac{0}{0}\right]$.  
Stosujemy regułę de l'Hospitala:
$$L = \lim_{x \to 0} \frac{\frac{x}{\sin x} \cdot \frac{x\cos x - \sin x}{x^2}}{2x} = \lim_{x \to 0} \frac{x\cos x - \sin x}{2x^2 \sin x} = \lim_{x \to 0} \left( \frac{x\cos x - \sin x}{2x^3} \cdot \frac{x}{\sin x} \right) = \frac{1}{2} \lim_{x \to 0} \frac{x\cos x - \sin x}{x^3}$$
Ponownie stosujemy regułę de l'Hospitala:
$$\lim_{x \to 0} \frac{\cos x - x\sin x - \cos x}{3x^2} = \lim_{x \to 0} \frac{-x\sin x}{3x^2} = -\frac{1}{3} \lim_{x \to 0} \frac{\sin x}{x} = -\frac{1}{3}$$
Stąd $L = \frac{1}{2} \cdot \left(-\frac{1}{3}\right) = -\frac{1}{6}$. Granica wyjściowa:
$$\lim_{x \to 0} \left( \frac{\sin x}{x} \right)^{1/x^2} = e^{-1/6} = \frac{1}{\sqrt[6]{e}}$$

---

#### Przykład 11.2 (Optymalizacja inżynierska: Twierdzenie o dopasowaniu odbiornika)
Układ zasilający o napięciu Thevenina $E$ i rezystancji wewnętrznej $R_w$ zasila obciążenie $R$. Wyznaczyć wartość rezystancji $R$, dla której moc wydzielana w obciążeniu jest maksymalna.

**Rozwiązanie:**  
Prąd w obwodzie wynosi $I = \frac{E}{R + R_w}$.  
Moc wydzielana w odbiorniku wynosi:
$$P(R) = I^2 R = \frac{E^2 R}{(R + R_w)^2}$$
Różniczkujemy funkcję mocy po $R > 0$:
$$P'(R) = E^2 \frac{1 \cdot (R + R_w)^2 - R \cdot 2(R + R_w)}{(R + R_w)^4} = E^2 \frac{(R + R_w)[(R + R_w) - 2R]}{(R + R_w)^4} = E^2 \frac{R_w - R}{(R + R_w)^3}$$
Punkt stacjonarny: $P'(R) = 0 \iff R = R_w$.  
Badamy znak pochodnej:
- dla $R < R_w$: $P'(R) > 0$ (funkcja rosnąca),
- dla $R > R_w$: $P'(R) < 0$ (funkcja malejąca).
W punkcie $R = R_w$ pochodna zmienia znak z $+$ na $-$, zatem występuje w nim **maksimum absolutne**.  
Maksymalna moc dopasowana:
$$P_{\max} = \frac{E^2 R_w}{(2R_w)^2} = \frac{E^2}{4R_w}$$
Sprawność układu przy dopasowaniu mocy wynosi dokładnie $\eta = 50\%$.

---

#### Przykład 11.3 (Rozwinięcie Taylora do obliczania granic)
Obliczyć granicę:
$$\lim_{x \to 0} \frac{x - \sin x}{x^2 (e^x - 1)}$$

**Rozwiązanie:**  
Stosujemy rozwinięcia Maclaurina:
$$\sin x = x - \frac{x^3}{6} + o(x^3) \implies x - \sin x = \frac{x^3}{6} + o(x^3)$$
$$e^x - 1 = x + o(x) \implies x^2 (e^x - 1) = x^3 + o(x^3)$$
Dzieląc licznik i mianownik przez $x^3$:
$$\lim_{x \to 0} \frac{\frac{1}{6} x^3 + o(x^3)}{x^3 + o(x^3)} = \frac{1/6}{1} = \frac{1}{6}$$

---

#### Przykład 11.4 (Pełne badanie przebiegu zmienności funkcji)
Zbadać przebieg zmienności funkcji $f(x) = \frac{x^3}{x^2 - 4}$.

**Rozwiązanie:**  
1. **Dziedzina i parzystość:**  
   $D_f = \mathbb{R} \setminus \{-2, 2\}$.  
   $f(-x) = \frac{(-x)^3}{(-x)^2 - 4} = -\frac{x^3}{x^2 - 4} = -f(x)$ – funkcja jest **nieparzysta** (wykres symetryczny względem początku układu). Wystarczy badać dla $x \ge 0$.
2. **Miejsca zerowe:** $f(x) = 0 \iff x = 0$.
3. **Asymptoty:**
   - Pionowe: $\lim_{x \to 2^-} f(x) = -\infty$, $\lim_{x \to 2^+} f(x) = +\infty \implies$ asymptota obustronna $x = 2$ (oraz z nieparzystości $x = -2$).
   - Ukośne:
     $$a = \lim_{x \to \infty} \frac{f(x)}{x} = \lim_{x \to \infty} \frac{x^2}{x^2 - 4} = 1$$
     $$b = \lim_{x \to \infty} \big( f(x) - x \big) = \lim_{x \to \infty} \left( \frac{x^3 - x(x^2 - 4)}{x^2 - 4} \right) = \lim_{x \to \infty} \frac{4x}{x^2 - 4} = 0$$
     Prosta $y = x$ jest asymptotą ukośną w obu nieskończonościach ($\pm\infty$).
4. **Pochodna I rzędu i ekstrema:**
   $$f'(x) = \frac{3x^2(x^2 - 4) - x^3(2x)}{(x^2 - 4)^2} = \frac{3x^4 - 12x^2 - 2x^4}{(x^2 - 4)^2} = \frac{x^2(x^2 - 12)}{(x^2 - 4)^2}$$
   Punkty stacjonarne: $x = 0$ oraz $x = \pm\sqrt{12} = \pm 2\sqrt{3}$.
   Dla $x > 0$:
   - $x \in (0, 2) \implies f'(x) < 0$ (maleje),
   - $x \in (2, 2\sqrt{3}) \implies f'(x) < 0$ (maleje),
   - $x \in (2\sqrt{3}, \infty) \implies f'(x) > 0$ (rośnie).
   W punkcie $x = 2\sqrt{3}$ funkcja posiada **minimum lokalne właściwe**:
   $$f_{\min} = f(2\sqrt{3}) = \frac{(2\sqrt{3})^3}{12 - 4} = \frac{24\sqrt{3}}{8} = 3\sqrt{3}$$
   Z nieparzystości: w $x = -2\sqrt{3}$ występuje **maksimum lokalne właściwe** $f_{\max} = -3\sqrt{3}$.
5. **Pochodna II rzędu i punkty przegięcia:**
   $$f''(x) = \frac{8x(x^2 + 12)}{(x^2 - 4)^3}$$
   Dla $x = 0$: $f''(0) = 0$, następuje zmiana znaku z $-$ na $+$ $\implies$ punkt $(0, 0)$ jest **punktem przegięcia**.

---

### 11.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 11.1:** Obliczyć pochodną funkcji $f(x) = (\cos x)^{\ln x}$.  
   *Odpowiedź:* $f'(x) = (\cos x)^{\ln x} \left( \frac{\ln(\cos x)}{x} - \ln x \cdot \operatorname{tg} x \right)$.

2. **Zadanie 11.2:** Wyznaczyć rozwinięcie Maclaurina do rzędu 4 dla funkcji $f(x) = \sqrt{1 + 2x^2}$.  
   *Odpowiedź:* $f(x) = 1 + x^2 - \frac{1}{2}x^4 + o(x^4)$.

3. **Zadanie 11.3:** Wyznaczyć równanie stycznej i normalnej do wykresu funkcji $f(x) = x \ln x$ w punkcie $x_0 = 1$.  
   *Odpowiedź:* $f(1) = 0$, $f'(1) = 1$. Styczna: $y = x - 1$; normalna: $y = -(x - 1) = -x + 1$.

4. **Zadanie 11.4:** Obliczyć granicę: $\lim_{x \to 0} \frac{\operatorname{tg} x - \sin x}{x^3}$.  
   *Odpowiedź:* $\frac{1}{2}$.

5. **Zadanie 11.5:** Wykazać za pomocą wzoru Taylora z resztą Lagrange'a, że dla każdego $x > 0$:  
   $$x - \frac{x^2}{2} < \ln(1 + x) < x$$

6. **Zadanie 11.6:** Znaleźć wymiary cylindrycznej puszki o zadanej objętości $V$, której pole powierzchni całkowitej jest minimalne (minimalizacja zużycia blachy).  
   *Odpowiedź:* $H = 2R = 2 \sqrt[3]{V / (2\pi)}$ (wysokość równa średnicy podstawy).


\newpage

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


\newpage

# Część VII: Całka Oznaczona i Całki Niewłaściwe

Całka oznaczona Riemanna stanowi formalną matematyczną realizację procesu sumowania nieskończonej liczby nieskończenie małych wielkości. Łączy pojęcie pola pod wykresem funkcji z funkcją pierwotną poprzez Podstawowe Twierdzenie Rachunku Całkowego (wzór Newtona-Leibniza). W elektrotechnice całka oznaczona jest podstawą definiowania wartości średniej i skutecznej (RMS) przebiegów okresowych, obliczania energii pobieranej przez odbiorniki nieliniowe, bilansu cieplnego elementów półprzewodnikowych oraz wyznaczania odpowiedzi układów w dziedzinie częstotliwości za pomocą całek niewłaściwych (transformata Fouriera i Laplace'a).

---

## Rozdział 14: Całka oznaczona Riemanna

### 14.1. Konstrukcja Riemanna i Darboux

Niech funkcja $f: [a, b] \to \mathbb{R}$ będzie ograniczona na przedziale domkniętym $[a, b]$ ($a < b$).

#### Definicja 14.1 (Podział przedziału i sumy całkowe)
1. **Podziałem** $\Pi$ przedziału $[a, b]$ nazywamy skończony zbiór punktów:
   $$\Pi: a = x_0 < x_1 < x_2 < \dots < x_n = b$$
   dzielący $[a, b]$ na $n$ podprzedziałów $[x_{i-1}, x_i]$ o długościach $\Delta x_i = x_i - x_{i-1}$.
2. **Średnicą podziału** nazywamy:
   $$\delta(\Pi) = \max_{1 \le i \le n} \Delta x_i$$
3. Wybierając w każdym podprzedziale punkt pośredni $\xi_i \in [x_{i-1}, x_i]$, tworzymy **sumę całkową Riemanna**:
   $$S(f, \Pi, \xi) = \sum_{i=1}^n f(\xi_i) \Delta x_i$$
4. Oznaczmy kresy funkcji na podprzedziale: $m_i = \inf_{x \in [x_{i-1}, x_i]} f(x)$, $M_i = \sup_{x \in [x_{i-1}, x_i]} f(x)$.
   - **Dolną sumą Darboux** nazywamy: $s(f, \Pi) = \sum_{i=1}^n m_i \Delta x_i$,
   - **Górną sumą Darboux** nazywamy: $S(f, \Pi) = \sum_{i=1}^n M_i \Delta x_i$.

Dla dowolnego podziału i wyboru punktów pośrednich: $s(f, \Pi) \le S(f, \Pi, \xi) \le S(f, \Pi)$.

#### Definicja 14.2 (Całka oznaczona Riemanna)
Mówimy, że funkcja $f$ jest **całkowalna w sensie Riemanna** na $[a, b]$ (co zapisujemy $f \in \mathcal{R}([a, b])$), jeżeli istnieje skończona liczba $I \in \mathbb{R}$ taka, że dla każdego normalnego ciągu podziałów ($\lim_{k\to\infty} \delta(\Pi_k) = 0$) i dowolnego doboru punktów pośrednich $\xi$:
$$\lim_{k \to \infty} S(f, \Pi_k, \xi) = I = \int_a^b f(x)\,dx$$

> **Twierdzenie 14.1 (Kryterium całkowalności Darboux):**  
> Funkcja ograniczona $f$ jest całkowalna w sensie Riemanna na $[a, b]$ wtedy i tylko wtedy, gdy:
> $$\lim_{\delta(\Pi) \to 0} \big( S(f, \Pi) - s(f, \Pi) \big) = 0$$

> **Twierdzenie 14.2 (Klasy funkcji całkowalnych):**  
> Następujące klasy funkcji są całkowalne w sensie Riemanna na $[a, b]$:
> 1. Każda funkcja **ciągła** na $[a, b]$.
> 2. Każda funkcja **monotoniczna** na $[a, b]$.
> 3. Każda funkcja ograniczona mająca **co najwyżej przeliczalną liczbę punktów nieciągłości** (w szczególności funkcje kawałkami ciągłe z nieciągłościami skokowymi).

---

### 14.2. Własności całki oznaczonej

Niech $f, g \in \mathcal{R}([a, b])$:
1. **Liniowość:** $\int_a^b \big( \alpha f(x) + \beta g(x) \big)\,dx = \alpha \int_a^b f(x)\,dx + \beta \int_a^b g(x)\,dx$.
2. **Addytywność względem przedziału:** Dla dowolnego $c \in (a, b)$:
   $$\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$$
3. **Monotoniczność:** Jeżeli $f(x) \le g(x)$ na $[a, b]$, to $\int_a^b f(x)\,dx \le \int_a^b g(x)\,dx$.
4. **Nierówność modułowa:** $\left| \int_a^b f(x)\,dx \right| \le \int_a^b |f(x)|\,dx$.
5. **Twierdzenie o wartości średniej:** Jeżeli $f$ jest ciągła na $[a, b]$, to istnieje punkt $c \in [a, b]$ taki, że:
   $$\int_a^b f(x)\,dx = f(c)(b - a) \iff f(c) = \frac{1}{b - a} \int_a^b f(x)\,dx$$
   Liczbę $\mu = \frac{1}{b-a}\int_a^b f(x)\,dx$ nazywamy **wartością średnią funkcji** na przedziale $[a, b]$.

---

### 14.3. Podstawowe Twierdzenie Rachunku Całkowego (Wzór Newtona-Leibniza)

Rozważmy funkcję górnej granicy całkowania dla funkcji ciągłej $f$:
$$\Phi(x) = \int_a^x f(t)\,dt, \quad x \in [a, b]$$

> **Twierdzenie 14.3 (Różniczkowalność całki względem górnej granicy):**  
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$, to funkcja $\Phi(x)$ jest różniczkowalna na $[a, b]$ oraz:
> $$\Phi'(x) = \frac{d}{dx} \left( \int_a^x f(t)\,dt \right) = f(x)$$
> Oznacza to, że każda funkcja ciągła posiada funkcję pierwotną!

**Dowód:**  
Z definicji pochodnej i addytywności całki:
$$\frac{\Phi(x + h) - \Phi(x)}{h} = \frac{1}{h} \left( \int_a^{x+h} f(t)\,dt - \int_a^x f(t)\,dt \right) = \frac{1}{h} \int_x^{x+h} f(t)\,dt$$
Z twierdzenia o wartości średniej dla całek istnieje punkt $c_h$ leżący między $x$ a $x+h$ taki, że:
$$\frac{1}{h} \int_x^{x+h} f(t)\,dt = \frac{1}{h} \cdot f(c_h) \cdot h = f(c_h)$$
Gdy $h \to 0$, to $c_h \to x$. Z ciągłości funkcji $f$: $\lim_{h \to 0} f(c_h) = f(x)$.  
Zatem $\Phi'(x) = f(x)$. $\blacksquare$

> **Twierdzenie 14.4 (Wzór Newtona-Leibniza):**  
> Jeżeli funkcja $f$ jest ciągła na $[a, b]$, a $F$ jest jej dowolną funkcją pierwotną ($F' = f$), to:
> $$\int_a^b f(x)\,dx = F(b) - F(a) = [F(x)]_a^b$$

**Dowód:**  
Ponieważ $\Phi(x) = \int_a^x f(t)\,dt$ jest funkcją pierwotną $f(x)$, to z Twierdzenia 12.1 dowolna inna funkcja pierwotna $F(x)$ różni się od $\Phi(x)$ o stałą $C$:
$$F(x) = \Phi(x) + C = \int_a^x f(t)\,dt + C$$
Wstawiając $x = a$: $F(a) = \int_a^a f(t)\,dt + C = 0 + C = C$.  
Wstawiając $x = b$: $F(b) = \int_a^b f(t)\,dt + F(a) \implies \int_a^b f(t)\,dt = F(b) - F(a)$. $\blacksquare$

#### Całkowanie przez części i przez podstawienie w całce oznaczonej:
1. **Przez części:**
   $$\int_a^b u(x) v'(x)\,dx = [u(x) v(x)]_a^b - \int_a^b u'(x) v(x)\,dx$$
2. **Przez podstawienie (zamiana granic):**
   $$\int_a^b f(\varphi(x)) \varphi'(x)\,dx = \int_{\varphi(a)}^{\varphi(b)} f(t)\,dt$$

---

## Rozdział 15: Zastosowania geometryczne i inżynierskie całki oznaczonej

### 15.1. Obliczanie wielkości geometrycznych

1. **Pole obszaru płaskiego:**  
   - We współrzędnych kartezjańskich: $S = \int_a^b [f_2(x) - f_1(x)]\,dx$.
   - W postaci parametrycznej ($x = x(t), y = y(t), t \in [\alpha, \beta]$):
     $$S = \int_\alpha^\beta y(t) x'(t)\,dt$$
   - We współrzędnych biegunowych ($r = r(\varphi), \varphi \in [\alpha, \beta]$):
     $$S = \frac{1}{2} \int_\alpha^\beta r^2(\varphi)\,d\varphi$$

2. **Długość łuku krzywej:**  
   - Postać jawna $y = f(x)$: $L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$.
   - Postać parametryczna: $L = \int_\alpha^\beta \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt$.
   - Postać biegunowa: $L = \int_\alpha^\beta \sqrt{r^2(\varphi) + [r'(\varphi)]^2}\,d\varphi$.

3. **Objętość bryły obrotowej:**  
   - Obrót wokół osi $OX$: $V_x = \pi \int_a^b [f(x)]^2\,dx$.
   - Obrót wokół osi $OY$ (metoda powłok walcowych): $V_y = 2\pi \int_a^b x f(x)\,dx$.

4. **Pole powierzchni bryły obrotowej:**  
   - Obrót wokół osi $OX$: $P_x = 2\pi \int_a^b f(x) \sqrt{1 + [f'(x)]^2}\,dx$.

---

### 15.2. Zastosowania w elektronice i teorii sygnałów

#### 1. Wartość średnia i skuteczna (RMS) sygnałów okresowych:
Dla sygnału okresowego $u(t)$ o okresie $T$:
- **Wartość średnia:**
  $$U_{\text{śr}} = \frac{1}{T} \int_0^T u(t)\,dt$$
- **Wartość skuteczna (RMS – Root Mean Square):**
  $$U_{\text{RMS}} = \sqrt{\frac{1}{T} \int_0^T u^2(t)\,dt}$$
Wartość skuteczna odpowiada wartości stałego napięcia, które na rezystorze $R$ wydzieliłoby w czasie okresu $T$ taką samą ilość ciepła (energię Joula) co analizowany sygnał zmienny:
$$W = \int_0^T \frac{u^2(t)}{R}\,dt = \frac{U_{\text{RMS}}^2}{R} T$$

#### Kanoniczne sygnały w elektronice:
1. **Sygnał sinusoidalny $u(t) = U_m \sin(\omega t)$:**
   $$U_{\text{RMS}} = \sqrt{\frac{1}{T} \int_0^T U_m^2 \sin^2(\omega t)\,dt} = U_m \sqrt{\frac{1}{T} \int_0^T \frac{1 - \cos(2\omega t)}{2}\,dt} = \frac{U_m}{\sqrt{2}} \approx 0{,}707 U_m$$
2. **Sygnał trójkątny symetryczny o amplitudzie $U_m$:**
   $$U_{\text{RMS}} = \frac{U_m}{\sqrt{3}} \approx 0{,}577 U_m$$
3. **Sygnał prostokątny o wypełnieniu 50% i amplitudzie $\pm U_m$:**
   $$U_{\text{RMS}} = U_m$$

---

## Rozdział 16: Całki niewłaściwe

### 16.1. Całki niewłaściwe I i II rodzaju

#### 1. Całki niewłaściwe I rodzaju (przedział nieograniczony):
$$\int_a^\infty f(x)\,dx = \lim_{B \to \infty} \int_a^B f(x)\,dx$$
$$\int_{-\infty}^\infty f(x)\,dx = \int_{-\infty}^c f(x)\,dx + \int_c^\infty f(x)\,dx \quad (c \in \mathbb{R})$$
Jeżeli granice są skończone, całkę nazywamy **zbieżną**, w przeciwnym razie – **rozbieżną**.

#### 2. Całki niewłaściwe II rodzaju (funkcja nieograniczona):
Jeżeli $f(x)$ dąży do $\pm\infty$ przy $x \to b^-$:
$$\int_a^b f(x)\,dx = \lim_{\varepsilon \to 0^+} \int_a^{b - \varepsilon} f(x)\,dx$$

> **Twierdzenie 16.1 (Całki wzorcowe):**  
> 1. $\int_1^\infty \frac{dx}{x^\alpha}$ jest **zbieżna dla $\alpha > 1$**, a rozbieżna dla $\alpha \le 1$.
> 2. $\int_0^1 \frac{dx}{x^\alpha}$ jest **zbieżna dla $\alpha < 1$**, a rozbieżna dla $\alpha \ge 1$.

---

### 16.2. Kryteria zbieżności i wartość główna Cauchy'ego

> **Twierdzenie 16.2 (Kryterium porównawcze i ilorazowe):**  
> Niech $0 \le f(x) \le g(x)$ dla $x \ge a$.
> - Jeżeli $\int_a^\infty g(x)\,dx$ jest zbieżna, to $\int_a^\infty f(x)\,dx$ jest zbieżna.
> - Jeżeli $\int_a^\infty f(x)\,dx$ jest rozbieżna, to $\int_a^\infty g(x)\,dx$ jest rozbieżna.
> - Jeżeli $\lim_{x \to \infty} \frac{f(x)}{g(x)} = k \in (0, \infty)$, to obie całki są jednocześnie zbieżne albo rozbieżne.

#### Wartość główna całki w sensie Cauchy'ego (v.p.):
Gdy całka $\int_{-\infty}^\infty f(x)\,dx$ jest rozbieżna w sensie klasycznym z powodu przeciwnych nieskończoności, jej wartość główną definiujemy jako granicę symetryczną:
$$\operatorname{v.p.} \int_{-\infty}^\infty f(x)\,dx = \lim_{R \to \infty} \int_{-R}^R f(x)\,dx$$
*Przykład:* $\int_{-\infty}^\infty x\,dx$ jest rozbieżna, lecz $\operatorname{v.p.}\int_{-\infty}^\infty x\,dx = \lim_{R\to\infty} \left[\frac{x^2}{2}\right]_{-R}^R = 0$.

---

### 16.3. Funkcje specjalne Eulera: Gamma i Beta

1. **Funkcja Gamma Eulera:**
   $$\Gamma(s) = \int_0^\infty t^{s-1} e^{-t}\,dt \quad (s > 0)$$
   Własności:
   - Wzór redukcyjny: $\Gamma(s + 1) = s \Gamma(s)$,
   - Dla liczb naturalnych: $\Gamma(n + 1) = n!$ (uogólnienie silni na liczby rzeczywiste i zespolone),
   - Wartość dla $s = 1/2$: $\Gamma(1/2) = \sqrt{\pi}$ (związana z całką Gaussa).

2. **Funkcja Beta Eulera:**
   $$\mathrm{B}(p, q) = \int_0^1 x^{p-1} (1 - x)^{q-1}\,dx = \frac{\Gamma(p) \Gamma(q)}{\Gamma(p + q)} \quad (p, q > 0)$$

---

### 16.4. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 16.1 (Obliczanie pola pętli linii parametrycznej)
Obliczyć pole obszaru ograniczonego pętlą krzywej zadanej parametrycznie:
$$x(t) = 3t^2, \quad y(t) = 3t - t^3$$

**Rozwiązanie:**  
1. **Wyznaczenie punktu samoprzecięcia (pętli):**  
   Szukamy $t_1 \neq t_2$ takich, że $x(t_1) = x(t_2)$ i $y(t_1) = y(t_2)$.
   $$3t_1^2 = 3t_2^2 \implies t_1 = -t_2$$
   $$y(t_1) = 3t_1 - t_1^3 = y(-t_1) = -3t_1 + t_1^3 \implies 2(3t_1 - t_1^3) = 0 \implies t_1(3 - t_1^2) = 0$$
   Nietrywialne parametry pętli: $t = -\sqrt{3}$ do $t = +\sqrt{3}$.
2. **Wzór na pole w postaci parametrycznej:**  
   Z symetrii wykresu względem osi $OX$ ($x(t)$ jest parzysta, $y(t)$ nieparzysta):
   $$S = \int_{-\sqrt{3}}^{\sqrt{3}} y(t) x'(t)\,dt = 2 \int_0^{\sqrt{3}} (3t - t^3) \cdot 6t\,dt = 12 \int_0^{\sqrt{3}} (3t^2 - t^4)\,dt$$
   $$= 12 \left[ t^3 - \frac{t^5}{5} \right]_0^{\sqrt{3}} = 12 \left( 3\sqrt{3} - \frac{9\sqrt{3}}{5} \right) = 12 \cdot \frac{6\sqrt{3}}{5} = \frac{72\sqrt{3}}{5}$$

---

#### Przykład 16.2 (Długość łuku asteroidy)
Obliczyć długość całej asteroidy:
$$x(t) = a \cos^3 t, \quad y(t) = a \sin^3 t \quad (a > 0, \; t \in [0, 2\pi])$$

**Rozwiązanie:**  
Krzywa składa się z 4 symetrycznych łuków (w każdej ćwiartce dla $t \in [0, \pi/2]$).
Pochodne:
$$x'(t) = -3a \cos^2 t \sin t, \quad y'(t) = 3a \sin^2 t \cos t$$
Element łuku:
$$ds = \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt = \sqrt{9a^2 \cos^4 t \sin^2 t + 9a^2 \sin^4 t \cos^2 t}\,dt$$
$$= 3a \sqrt{\sin^2 t \cos^2 t (\cos^2 t + \sin^2 t)}\,dt = 3a |\sin t \cos t|\,dt$$
Dla $t \in [0, \pi/2]$ mamy $\sin t \cos t \ge 0$, więc:
$$L = 4 \int_0^{\pi/2} 3a \sin t \cos t\,dt = 12a \left[ \frac{\sin^2 t}{2} \right]_0^{\pi/2} = 12a \cdot \frac{1}{2} = 6a$$

---

#### Przykład 16.3 (Całka niewłaściwa I rodzaju)
Zbadać zbieżność i obliczyć całkę:
$$\int_0^\infty \frac{dx}{x^2 + 4x + 8}$$

**Rozwiązanie:**  
Mianownik: $x^2 + 4x + 8 = (x + 2)^2 + 4 = 4 \left[ \left(\frac{x+2}{2}\right)^2 + 1 \right]$.  
Funkcja pierwotna:
$$\int \frac{dx}{(x+2)^2 + 2^2} = \frac{1}{2} \operatorname{arctg}\left(\frac{x + 2}{2}\right) + C$$
Obliczamy granicę:
$$\int_0^\infty \frac{dx}{x^2 + 4x + 8} = \lim_{B \to \infty} \left[ \frac{1}{2} \operatorname{arctg}\left(\frac{x + 2}{2}\right) \right]_0^B = \frac{1}{2} \left( \lim_{B \to \infty} \operatorname{arctg}\left(\frac{B + 2}{2}\right) - \operatorname{arctg}\left(\frac{2}{2}\right) \right)$$
$$= \frac{1}{2} \left( \frac{\pi}{2} - \operatorname{arctg}(1) \right) = \frac{1}{2} \left( \frac{\pi}{2} - \frac{\pi}{4} \right) = \frac{1}{2} \cdot \frac{\pi}{4} = \frac{\pi}{8}$$

---

### 16.5. Zadania do samodzielnego rozwiązania

1. **Zadanie 16.1:** Obliczyć całkę oznaczoną: $\int_0^1 x e^{-x}\,dx$.  
   *Odpowiedź:* $1 - \frac{2}{e}$.

2. **Zadanie 16.2:** Obliczyć objętość bryły powstałej przez obrót wokół osi $OX$ łuku sinusoidy $y = \sin x$ dla $x \in [0, \pi]$.  
   *Odpowiedź:* $V = \pi \int_0^\pi \sin^2 x\,dx = \frac{\pi^2}{2}$.

3. **Zadanie 16.3:** Wyznaczyć wartość skuteczną przebiegu $u(t) = U_m |\sin(\omega t)|$ (napięcie wyprostowane dwupołówkowo).  
   *Odpowiedź:* $U_{\text{RMS}} = \frac{U_m}{\sqrt{2}}$.

4. **Zadanie 16.4:** Zbadać zbieżność całki niewłaściwej: $\int_0^1 \frac{\ln x}{\sqrt{x}}\,dx$.  
   *Odpowiedź:* Całka jest zbieżna. Przez części: $[2\sqrt{x}\ln x]_0^1 - \int_0^1 2\sqrt{x}\frac{1}{x}dx = 0 - [4\sqrt{x}]_0^1 = -4$.

5. **Zadanie 16.5:** Korzystając z własności funkcji Gamma, obliczyć całkę $\int_0^\infty x^6 e^{-2x}\,dx$.  
   *Wskazówka:* Podstawienie $t = 2x$.  
   *Odpowiedź:* $\frac{\Gamma(7)}{2^7} = \frac{6!}{128} = \frac{720}{128} = \frac{45}{8}$.


\newpage

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


\newpage



---

# TOM II: Funkcje Wielu Zmiennych, Całki Wielokrotne, Analiza Wektorowa i Równania Różniczkowe

\newpage

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


\newpage

# Część X: Całki Wielokrotne i Ich Zastosowania Inżynierskie

Rachunek całkowy funkcji wielu zmiennych stanowi fundamentalne narzędzie modelowania procesów ciągłych w przestrzeni jedno-, dwu- i trójwymiarowej. W elektrotechnice i teorii pola elektromagnetycznego pozwala na wyznaczanie całkowitego ładunku zgromadzonego w obszarze o zadanej gęstości, pojemności układów przewodników o złożonej geometrii, energii pola elektrostatycznego i magnetycznego, a także na analizę szumów losowych w odbiornikach telekomunikacyjnych (całka prawdopodobieństwa Gaussa).

---

## Rozdział 21: Całka podwójna i jej zastosowania

### 21.1. Definicja całki podwójnej Riemanna

Niech $P = [a, b] \times [c, d] \subset \mathbb{R}^2$ będzie prostokątem domkniętym na płaszczyźnie, a funkcja $f: P \to \mathbb{R}$ niech będzie ograniczona.

#### Definicja 21.1 (Podział prostokąta i sumy całkowe)
1. **Podziałem** prostokąta $P$ nazywamy parę podziałów przedziałów:
   $$\Pi_x: a = x_0 < x_1 < \dots < x_n = b, \quad \Pi_y: c = y_0 < y_1 < \dots < y_m = d$$
   dzielących $P$ na $n \times m$ prostokątów cząstkowych $P_{ij} = [x_{i-1}, x_i] \times [y_{j-1}, y_j]$ o polach $\Delta S_{ij} = \Delta x_i \cdot \Delta y_j = (x_i - x_{i-1})(y_j - y_{j-1})$.
2. **Średnicą podziału** $\delta(\Pi)$ nazywamy największą z przekątnych prostokątów $P_{ij}$:
   $$\delta(\Pi) = \max_{i, j} \sqrt{(\Delta x_i)^2 + (\Delta y_j)^2}$$
3. W każdym prostokącie $P_{ij}$ wybieramy punkt pośredni $\xi_{ij} = (\xi_i, \eta_j) \in P_{ij}$. **Sumą całkową Riemanna** nazywamy:
   $$S(f, \Pi, \xi) = \sum_{i=1}^n \sum_{j=1}^m f(\xi_i, \eta_j) \Delta S_{ij}$$

#### Definicja 21.2 (Całka podwójna Riemanna)
Jeżeli dla każdego normalnego ciągu podziałów $\Pi_k$ (takiego, że $\lim_{k\to\infty} \delta(\Pi_k) = 0$) i dowolnego wyboru punktów pośrednich suma całkowa dąży do skończonej granicy $I$, to granicę tę nazywamy **całką podwójną Riemanna** funkcji $f$ po prostokącie $P$ i oznaczamy:
$$\iint_P f(x, y)\,dx\,dy = \lim_{\delta(\Pi) \to 0} \sum_{i=1}^n \sum_{j=1}^m f(\xi_i, \eta_j) \Delta S_{ij}$$

> **Twierdzenie 21.1 (Całkowalność funkcji ciągłych):**  
> Każda funkcja ciągła na prostokącie domkniętym $P$ jest na nim całkowalna w sensie Riemanna.

---

### 21.2. Własności całki podwójnej

Niech funkcje $f, g: D \to \mathbb{R}$ będą całkowalne na ograniczonym obszarze mierzalnym $D \subset \mathbb{R}^2$.
1. **Liniowość:** Dla dowolnych $\alpha, \beta \in \mathbb{R}$:
   $$\iint_D \big( \alpha f(x, y) + \beta g(x, y) \big)\,dx\,dy = \alpha \iint_D f(x, y)\,dx\,dy + \beta \iint_D g(x, y)\,dx\,dy$$
2. **Addytywność względem obszaru:** Jeżeli obszar $D$ jest sumą dwóch obszarów niemających wspólnych punktów wewnętrznych ($D = D_1 \cup D_2$, $\operatorname{Int}(D_1) \cap \operatorname{Int}(D_2) = \emptyset$):
   $$\iint_D f(x, y)\,dx\,dy = \iint_{D_1} f(x, y)\,dx\,dy + \iint_{D_2} f(x, y)\,dx\,dy$$
3. **Monotoniczność:** Jeżeli $f(x, y) \le g(x, y)$ dla każdego $(x, y) \in D$, to:
   $$\iint_D f(x, y)\,dx\,dy \le \iint_D g(x, y)\,dx\,dy$$
4. **Nierówność modułowa:**
   $$\left| \iint_D f(x, y)\,dx\,dy \right| \le \iint_D |f(x, y)|\,dx\,dy$$
5. **Twierdzenie o wartości średniej:** Jeżeli funkcja $f$ jest ciągła na obszarze domkniętym, ograniczonym i spójnym $D$ o polu $|D|$, to istnieje punkt $(\xi, \eta) \in D$ taki, że:
   $$\iint_D f(x, y)\,dx\,dy = f(\xi, \eta) \cdot |D|$$
   Wielkość $\mu = \frac{1}{|D|} \iint_D f(x, y)\,dx\,dy$ jest **wartością średnią dwuwymiarową** funkcji na obszarze $D$.

---

### 21.3. Twierdzenie Fubiniego i obliczanie całek podwójnych

Podstawowym narzędziem sprowadzającym całkę podwójną do zwykłych całek pojedynczych jest **twierdzenie Fubiniego o zamianie na całki iterowane**.

#### Definicja 21.3 (Obszary normalne na płaszczyźnie)
1. Obszar $D \subset \mathbb{R}^2$ nazywamy **normalnym względem osi $OX$**, jeżeli można go opisać nierównościami:
   $$D = \{ (x, y) \in \mathbb{R}^2 : a \le x \le b, \quad g_1(x) \le y \le g_2(x) \}$$
   gdzie funkcje $g_1, g_2: [a, b] \to \mathbb{R}$ są ciągłe oraz $g_1(x) \le g_2(x)$.
2. Obszar $D \subset \mathbb{R}^2$ nazywamy **normalnym względem osi $OY$**, jeżeli:
   $$D = \{ (x, y) \in \mathbb{R}^2 : c \le y \le d, \quad h_1(y) \le x \le h_2(y) \}$$
   gdzie funkcje $h_1, h_2: [c, d] \to \mathbb{R}$ są ciągłe oraz $h_1(y) \le h_2(y)$.

> **Twierdzenie 21.2 (Fubiniego dla obszarów normalnych):**  
> 1. Jeżeli $f$ jest funkcją ciągłą na obszarze normalnym względem osi $OX$, to:
>    $$\iint_D f(x, y)\,dx\,dy = \int_a^b \left( \int_{g_1(x)}^{g_2(x)} f(x, y)\,dy \right) dx$$
> 2. Jeżeli $f$ jest ciągła na obszarze normalnym względem osi $OY$, to:
>    $$\iint_D f(x, y)\,dx\,dy = \int_c^d \left( \int_{h_1(y)}^{h_2(y)} f(x, y)\,dx \right) dy$$

W przypadku prostokąta $P = [a, b] \times [c, d]$ kolejność całkowania jest dowolna:
$$\iint_P f(x, y)\,dx\,dy = \int_a^b \left( \int_c^d f(x, y)\,dy \right) dx = \int_c^d \left( \int_a^b f(x, y)\,dx \right) dy$$
Ponadto, gdy funkcja ma postać rozdzieloną $f(x, y) = \varphi(x) \cdot \psi(y)$:
$$\iint_P \varphi(x)\psi(y)\,dx\,dy = \left( \int_a^b \varphi(x)\,dx \right) \cdot \left( \int_c^d \psi(y)\,dy \right)$$

---

### 21.4. Zamiana zmiennych w całce podwójnej

Rozważmy przekształcenie dyfeomorficzne $\Phi: \Delta \to D$ płaszczyzny $(u, v)$ na płaszczyznę $(x, y)$:
$$x = x(u, v), \quad y = y(u, v)$$
gdzie funkcje $x(u, v), y(u, v)$ są klasy $C^1$ na obszarze $\Delta \subset \mathbb{R}^2$.

#### Definicja 21.4 (Jakobian przekształcenia)
**Jakobianem (wyznacznikiem Jacobiego)** przekształcenia $\Phi$ nazywamy wyznacznik macierzy pochodnych cząstkowych:
$$J = \frac{\partial(x, y)}{\partial(u, v)} = \det \begin{bmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{bmatrix} = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}$$
Geometrycznie moduł jakobianu $|J|$ określa lokalny współczynnik skalowania elementarnego pola powierzchni: $dx\,dy = |J|\,du\,dv$.

> **Twierdzenie 21.3 (O zamianie zmiennych w całce podwójnej):**  
> Jeżeli przekształcenie $\Phi$ jest różnowartościowe wewnątrz obszaru $\Delta$ oraz jakobian $J \neq 0$, to dla dowolnej funkcji ciągłej $f$ na $D$:
> $$\iint_D f(x, y)\,dx\,dy = \iint_\Delta f\big(x(u, v), y(u, v)\big) \cdot |J|\,du\,dv$$

#### Współrzędne biegunowe:
Związki transformacyjne:
$$x = r \cos \varphi, \quad y = r \sin \varphi \quad (r \ge 0, \; \varphi \in [0, 2\pi) \text{ lub } [-\pi, \pi])$$
Obliczenie jakobianu:
$$J = \det \begin{bmatrix} \cos \varphi & -r \sin \varphi \\ \sin \varphi & r \cos \varphi \end{bmatrix} = r \cos^2 \varphi - (-r \sin^2 \varphi) = r(\cos^2 \varphi + \sin^2 \varphi) = r$$
Ponieważ $r \ge 0$, mamy $|J| = r$.  
Element pola we współrzędnych biegunowych:
$$dx\,dy = r\,dr\,d\varphi$$
Wzór na zamianę zmiennych:
$$\iint_D f(x, y)\,dx\,dy = \iint_\Delta f(r\cos\varphi, r\sin\varphi) \cdot r\,dr\,d\varphi$$

---

### 21.5. Zastosowania geometryczne i fizyczne całek podwójnych

1. **Pole obszaru płaskiego $D$:**
   $$|D| = \iint_D 1\,dx\,dy$$
2. **Objętość bryły $V$:**  
   Bryła ograniczona od góry powierzchnią $z = f(x, y) \ge 0$ i od dołu płaszczyzną $z = 0$ nad obszarem $D$:
   $$|V| = \iint_D f(x, y)\,dx\,dy$$
   Gdy bryła zawarta jest między dwoma powierzchniami $z_1(x, y) \le z \le z_2(x, y)$:
   $$|V| = \iint_D \big( z_2(x, y) - z_1(x, y) \big)\,dx\,dy$$
3. **Pole płata powierzchniowego:**  
   Pole powierzchni płata $z = f(x, y)$ nad obszarem $D$, gdzie $f \in C^1$:
   $$|S| = \iint_D \sqrt{1 + \left( \frac{\partial f}{\partial x} \right)^2 + \left( \frac{\partial f}{\partial y} \right)^2}\,dx\,dy$$
4. **Masa i ładunek powierzchniowy:**  
   Dla płytki o gęstości powierzchniowej masy lub ładunku $\sigma(x, y)$:
   $$M = \iint_D \sigma(x, y)\,dx\,dy, \quad Q = \iint_D \sigma(x, y)\,dx\,dy$$
5. **Środek ciężkości (środek masy):**
   $$x_C = \frac{1}{M} \iint_D x \cdot \sigma(x, y)\,dx\,dy, \quad y_C = \frac{1}{M} \iint_D y \cdot \sigma(x, y)\,dx\,dy$$
6. **Momenty bezwładności:**
   - Względem osi $OX$: $I_x = \iint_D y^2 \sigma(x, y)\,dx\,dy$,
   - Względem osi $OY$: $I_y = \iint_D x^2 \sigma(x, y)\,dx\,dy$,
   - Biegunowy moment bezwładności względem początku układu:
     $$I_0 = \iint_D (x^2 + y^2)\sigma(x, y)\,dx\,dy = I_x + I_y$$

---

## Rozdział 22: Całka potrójna i całki niewłaściwe wielokrotne

### 22.1. Całka potrójna Riemanna i twierdzenie Fubiniego

Rozważmy ograniczoną bryłę przestrzenną $V \subset \mathbb{R}^3$ oraz funkcję ciągłą $f: V \to \mathbb{R}$.

#### Definicja 22.1 (Całka potrójna)
Dzieląc obszar $V$ siatką prostopadłościanów o objętościach $\Delta V_{ijk} = \Delta x_i \Delta y_j \Delta z_k$:
$$\iiint_V f(x, y, z)\,dx\,dy\,dz = \lim_{\delta(\Pi)\to 0} \sum_{i, j, k} f(\xi_i, \eta_j, \zeta_k) \Delta V_{ijk}$$

#### Twierdzenie Fubiniego dla obszaru normalnego w przestrzeni:
Jeżeli bryła $V$ ma postać:
$$V = \{ (x, y, z) \in \mathbb{R}^3 : (x, y) \in D, \quad z_1(x, y) \le z \le z_2(x, y) \}$$
gdzie $D$ jest rzutem bryły na płaszczyznę $OXY$, to:
$$\iiint_V f(x, y, z)\,dx\,dy\,dz = \iint_D \left( \int_{z_1(x, y)}^{z_2(x, y)} f(x, y, z)\,dz \right) dx\,dy$$

---

### 22.2. Układy współrzędnych krzywoliniowych w $\mathbb{R}^3$

#### 1. Współrzędne walcowe (cylindryczne):
Transformacja:
$$x = r \cos \varphi, \quad y = r \sin \varphi, \quad z = z$$
gdzie $r \ge 0$, $\varphi \in [0, 2\pi)$, $z \in \mathbb{R}$.
Jakobian przekształcenia:
$$J = \det \begin{bmatrix}
\cos \varphi & -r \sin \varphi & 0 \\
\sin \varphi & r \cos \varphi & 0 \\
0 & 0 & 1
\end{bmatrix} = 1 \cdot (r \cos^2 \varphi + r \sin^2 \varphi) = r$$
Stąd element objętości:
$$dV = dx\,dy\,dz = r\,dr\,d\varphi\,dz$$
Współrzędne walcowe stosujemy zawsze w układach posiadających **symetrię osiową** (przewodniki walcowe, falowody kołowe, cewki cylindryczne).

#### 2. Współrzędne sferyczne (kuliste):
Transformacja:
$$x = r \sin \theta \cos \varphi, \quad y = r \sin \theta \sin \varphi, \quad z = r \cos \theta$$
gdzie:
- $r \ge 0$ – promień wodzący (odległość od początku układu),
- $\theta \in [0, \pi]$ – kąt zenitalny (odchylenie od dodatniej półosi $OZ$),
- $\varphi \in [0, 2\pi)$ – kąt azymutalny na płaszczyźnie $OXY$.

Obliczenie jakobianu:
$$J = \det \begin{bmatrix}
\sin \theta \cos \varphi & r \cos \theta \cos \varphi & -r \sin \theta \sin \varphi \\
\sin \theta \sin \varphi & r \cos \theta \sin \varphi & r \sin \theta \cos \varphi \\
\cos \theta & -r \sin \theta & 0
\end{bmatrix} = r^2 \sin \theta$$
Ponieważ $\theta \in [0, \pi]$, $\sin \theta \ge 0$, więc $|J| = r^2 \sin \theta$.  
Element objętości:
$$dV = dx\,dy\,dz = r^2 \sin \theta\,dr\,d\theta\,d\varphi$$
Współrzędne sferyczne są podstawowym aparatem w zagadnieniach o **symetrii środkowej/kulistej** (potencjał elektrostatyczny ładunku punktowego, promieniowanie anten izotropowych).

---

### 22.3. Zastosowania fizyczne całek potrójnych w teorii pola

1. **Całkowity ładunek elektrostatyczny:**  
   Jeżeli w przestrzeni $V$ występuje ciągły rozkład ładunku o gęstości objętościowej $\rho(x, y, z)$ [$\text{C}/\text{m}^3$]:
   $$Q = \iiint_V \rho(x, y, z)\,dx\,dy\,dz$$
2. **Potencjał elektrostatyczny:**  
   Potencjał wywołany przez ładunek rozproszony w bryle $V$ w punkcie obserwacji $P(x_0, y_0, z_0)$ poza obszarem ładunku:
   $$V(P) = \frac{1}{4\pi \varepsilon_0} \iiint_V \frac{\rho(x, y, z)}{\sqrt{(x - x_0)^2 + (y - y_0)^2 + (z - z_0)^2}}\,dx\,dy\,dz$$
3. **Energia własna pola elektrostatycznego:**  
   Gęstość energii pola elektrycznego o natężeniu $\vec{E}$ w dielektryku o przenikalności $\varepsilon$:
   $$w_e = \frac{1}{2} \varepsilon \|\vec{E}\|^2 \implies W_e = \iiint_{\mathbb{R}^3} w_e\,dV = \frac{1}{2} \varepsilon \iiint_{\mathbb{R}^3} \|\vec{E}(x, y, z)\|^2\,dx\,dy\,dz$$

---

### 22.4. Całka Poissona-Gaussa i szumy losowe w telekomunikacji

Jednym z najbardziej fundamentalnych rezultatów analizy matematycznej wykorzystującym całkę podwójną jest wyznaczenie wartości całki Poissona-Gaussa:
$$I = \int_{-\infty}^\infty e^{-x^2}\,dx$$
Funkcja podcałkowa $e^{-x^2}$ nie posiada funkcji pierwotnej wyrażalnej przez funkcje elementarne (twierdzenie Liouville'a), jednak jej całka oznaczona po całej prostej może zostać obliczona ściśle.

> **Twierdzenie 22.1 (Całka Gaussa):**  
> $$\int_{-\infty}^\infty e^{-x^2}\,dx = \sqrt{\pi}$$

**Dowód:**  
Rozważmy kwadrat całki $I$:
$$I^2 = \left( \int_{-\infty}^\infty e^{-x^2}\,dx \right) \cdot \left( \int_{-\infty}^\infty e^{-y^2}\,dy \right)$$
Korzystając z twierdzenia Fubiniego, iloczyn całek pojedynczych możemy zapisać jako całkę podwójną po całej płaszczyźnie $\mathbb{R}^2$:
$$I^2 = \iint_{\mathbb{R}^2} e^{-x^2} e^{-y^2}\,dx\,dy = \iint_{\mathbb{R}^2} e^{-(x^2 + y^2)}\,dx\,dy$$
Wprowadzamy współrzędne biegunowe: $x = r \cos \varphi$, $y = r \sin \varphi$, gdzie $r \in [0, \infty)$ oraz $\varphi \in [0, 2\pi)$. Jakobian wynosi $J = r$. Obszar całkowania przekształca się w $\Delta = [0, \infty) \times [0, 2\pi)$:
$$I^2 = \int_0^{2\pi} \left( \int_0^\infty e^{-r^2} \cdot r\,dr \right) d\varphi = \left( \int_0^{2\pi} d\varphi \right) \cdot \left( \int_0^\infty r e^{-r^2}\,dr \right)$$
Całka kątowa wynosi $2\pi$. W całce promieniowej stosujemy podstawienie $t = r^2$, skąd $dt = 2r\,dr \implies r\,dr = \frac{1}{2} dt$:
$$\int_0^\infty r e^{-r^2}\,dr = \frac{1}{2} \int_0^\infty e^{-t}\,dt = \frac{1}{2} \left[ -e^{-t} \right]_0^\infty = \frac{1}{2} (0 - (-1)) = \frac{1}{2}$$
Mnożąc oba rezultaty:
$$I^2 = 2\pi \cdot \frac{1}{2} = \pi \implies I = \sqrt{\pi} \quad \blacksquare$$

#### Zastosowanie w teorii sygnałów i telekomunikacji:
W odbiornikach radiowych i systemach teleinformatycznych fundamentalnym ograniczeniem jest **termiczny szum gaussowski (szum Johnsona-Nyquista)**. Rozkład prawdopodobieństwa napięcia szumu $U$ opisuje gęstość prawdopodobieństwa Gaussa:
$$f_U(u) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(u - m)^2}{2\sigma^2}}$$
Z twierdzenia Gaussa wynika natychmiast warunek normalizacji prawdopodobieństwa:
$$\int_{-\infty}^\infty f_U(u)\,du = \frac{1}{\sigma \sqrt{2\pi}} \int_{-\infty}^\infty e^{-\frac{(u - m)^2}{2\sigma^2}}\,du = 1$$
co po podstawieniu $x = \frac{u-m}{\sigma \sqrt{2}}$ redukuje się do $\frac{1}{\sqrt{\pi}} \int_{-\infty}^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{\sqrt{\pi}} = 1$.

---

### 22.5. Wzorcowe zadania egzaminacyjne z pełnymi rozwiązaniami

#### Przykład 22.1 (Zmiana kolejności całkowania w całce iterowanej)
Zmienić kolejność całkowania w całce:
$$I = \int_0^1 dx \int_{x^2}^{\sqrt{x}} f(x, y)\,dy$$

**Rozwiązanie:**  
1. **Analiza obszaru $D$:**  
   Obszar jest zadany nierównościami:
   $$0 \le x \le 1, \quad x^2 \le y \le \sqrt{x}$$
   Dolna krawędź to parabola $y = x^2$, górna to gałąź paraboli $y = \sqrt{x}$ (czyli $x = y^2$).
   Punkty przecięcia krzywych: $x^2 = \sqrt{x} \implies x^4 = x \implies x(x^3 - 1) = 0 \implies x = 0$ oraz $x = 1$.
   Zakres zmiennej $y$: od $y_{\min} = 0$ do $y_{\max} = 1$.

2. **Opis obszaru jako normalnego względem osi $OY$:**  
   Dla ustalonego $y \in [0, 1]$:
   - lewa granica: $y = \sqrt{x} \implies x = y^2$,
   - prawa granica: $y = x^2 \implies x = \sqrt{y}$.
   Zatem:
   $$0 \le y \le 1, \quad y^2 \le x \le \sqrt{y}$$

3. **Zapis całki po zamianie kolejności:**
   $$I = \int_0^1 dy \int_{y^2}^{\sqrt{y}} f(x, y)\,dx$$

---

#### Przykład 22.2 (Całka podwójna we współrzędnych biegunowych)
Obliczyć całkę podwójną:
$$\iint_D (x^2 + y^2)\,dx\,dy$$
gdzie $D$ jest obszarem w I ćwiartce ograniczonym okręgami $x^2 + y^2 = 1$, $x^2 + y^2 = 4$ oraz prostymi $y = 0$ i $y = x$.

**Rozwiązanie:**  
1. **Przejście na współrzędne biegunowe:**  
   $x = r \cos \varphi$, $y = r \sin \varphi$, $x^2 + y^2 = r^2$, jakobian $J = r$.
2. **Wyznaczenie granic całkowania:**  
   - Okręgi mają promienie $R_1 = 1$ oraz $R_2 = 2 \implies 1 \le r \le 2$.
   - Prosta $y = 0$ to oś $OX$ ($\varphi = 0$).
   - Prosta $y = x$ ma kąt nachylenia $\operatorname{tg} \varphi = 1 \implies \varphi = \frac{\pi}{4}$.
   Obszar transformowany: $\Delta = [1, 2] \times [0, \pi/4]$.

3. **Obliczenie całki:**
   $$\iint_D (x^2 + y^2)\,dx\,dy = \int_0^{\pi/4} d\varphi \int_1^2 r^2 \cdot r\,dr = \left( \int_0^{\pi/4} d\varphi \right) \cdot \left( \int_1^2 r^3\,dr \right)$$
   $$\int_0^{\pi/4} d\varphi = \frac{\pi}{4}$$
   $$\int_1^2 r^3\,dr = \left[ \frac{r^4}{4} \right]_1^2 = \frac{2^4 - 1^4}{4} = \frac{16 - 1}{4} = \frac{15}{4}$$
   Wynik:
   $$\iint_D (x^2 + y^2)\,dx\,dy = \frac{\pi}{4} \cdot \frac{15}{4} = \frac{15\pi}{16}$$

---

#### Przykład 22.3 (Objętość bryły we współrzędnych walcowych)
Obliczyć objętość bryły ograniczonej od dołu paraboloidą $z = x^2 + y^2$, a od góry płaszczyzną $z = 4$.

**Rozwiązanie:**  
1. **Przecięcie powierzchni:**  
   $x^2 + y^2 = 4$ – okrąg o promieniu $R = 2$ na wysokości $z = 4$.
   Rzut bryły na płaszczyznę $OXY$ to koło $D = \{ (x, y) \in \mathbb{R}^2 : x^2 + y^2 \le 4 \}$.
   W każdym punkcie koła $D$ wysokość bryły wynosi: $z_1 = x^2 + y^2 \le z \le z_2 = 4$.

2. **Współrzędne walcowe:**  
   $x = r \cos \varphi$, $y = r \sin \varphi$, $z = z$, $dV = r\,dr\,d\varphi\,dz$.
   Granice: $\varphi \in [0, 2\pi]$, $r \in [0, 2]$, $z \in [r^2, 4]$.

3. **Całkowanie:**
   $$|V| = \int_0^{2\pi} d\varphi \int_0^2 r\,dr \int_{r^2}^4 dz = 2\pi \int_0^2 r (4 - r^2)\,dr = 2\pi \int_0^2 (4r - r^3)\,dr$$
   $$= 2\pi \left[ 2r^2 - \frac{r^4}{4} \right]_0^2 = 2\pi \left( 2(4) - \frac{16}{4} \right) = 2\pi (8 - 4) = 8\pi$$

---

#### Przykład 22.4 (Ładunek elektrostatyczny we współrzędnych sferycznych)
W kuli o promieniu $R$ gęstość objętościowa ładunku elektrycznego zależy od odległości od środka:
$$\rho(r) = \rho_0 \left( 1 - \frac{r^2}{R^2} \right) \quad (\rho_0 > 0)$$
Wyznaczyć całkowity ładunek $Q$ zgromadzony w kuli.

**Rozwiązanie:**  
Stosujemy współrzędne sferyczne ($r, \theta, \varphi$):
$$Q = \iiint_K \rho(r)\,dV = \int_0^{2\pi} d\varphi \int_0^\pi \sin \theta\,d\theta \int_0^R \rho_0 \left( 1 - \frac{r^2}{R^2} \right) r^2\,dr$$
1. Całka po kącie azymutalnym: $\int_0^{2\pi} d\varphi = 2\pi$.
2. Całka po kącie zenitalnym: $\int_0^\pi \sin \theta\,d\theta = [-\cos \theta]_0^\pi = -(-1) - (-1) = 2$.  
   Iloczyn kątowy to pełny kąt bryłowy kuli: $\Omega = 2\pi \cdot 2 = 4\pi$ steradianów.
3. Całka radialna:
   $$\int_0^R \left( r^2 - \frac{r^4}{R^2} \right) dr = \left[ \frac{r^3}{3} - \frac{r^5}{5R^2} \right]_0^R = \frac{R^3}{3} - \frac{R^3}{5} = R^3 \left( \frac{5 - 3}{15} \right) = \frac{2}{15} R^3$$
Ładunek całkowity:
$$Q = 4\pi \rho_0 \cdot \frac{2}{15} R^3 = \frac{8\pi}{15} \rho_0 R^3$$

---

### 22.6. Zadania do samodzielnego rozwiązania

1. **Zadanie 22.1:** Obliczyć całkę podwójną $\iint_D x y\,dx\,dy$, gdzie $D$ jest trójkątem o wierzchołkach $A(0, 0)$, $B(2, 0)$, $C(0, 2)$.  
   *Odpowiedź:* $\int_0^2 dx \int_0^{2-x} xy\,dy = \frac{2}{3}$.

2. **Zadanie 22.2:** Obliczyć pole obszaru ograniczonego kardioidą o równaniu we współrzędnych biegunowych $r = a(1 + \cos \varphi)$, gdzie $a > 0$.  
   *Odpowiedź:* $S = \frac{1}{2} \int_0^{2\pi} r^2\,d\varphi = \frac{1}{2} a^2 \int_0^{2\pi} (1 + 2\cos\varphi + \cos^2\varphi)\,d\varphi = \frac{3}{2}\pi a^2$.

3. **Zadanie 22.3:** Wyznaczyć masę stożka ściętego o promieniu dolnej podstawy $R_1$, górnej $R_2$ i wysokości $H$, jeżeli gęstość masy jest proporcjonalna do odległości od podstawy: $\rho(z) = k z$.  
   *Odpowiedź:* Całka we współrzędnych walcowych: $M = \frac{\pi k H^2}{12}(R_1^2 + 2 R_1 R_2 + 3 R_2^2)$.

4. **Zadanie 22.4:** Obliczyć moment bezwładności jednorodnej kuli o promieniu $R$ i stałej gęstości $\rho_0$ względem jej osi symetrii $OZ$.  
   *Odpowiedź:* $I_z = \iiint_K (x^2 + y^2)\rho_0\,dV$. We współrzędnych sferycznych $x^2 + y^2 = r^2 \sin^2 \theta$. $I_z = \frac{2}{5} M R^2$, gdzie $M = \frac{4}{3}\pi R^3 \rho_0$.

5. **Zadanie 22.5:** Wykazać, że dla $\alpha > 0$:  
   $$\int_{-\infty}^\infty e^{-\alpha x^2}\,dx = \sqrt{\frac{\pi}{\alpha}}$$
   oraz obliczyć całkę momentową $\int_{-\infty}^\infty x^2 e^{-\alpha x^2}\,dx$ przez różniczkowanie po parametrze $\alpha$.  
   *Odpowiedź:* Różniczkując tożsamość $\int_{-\infty}^\infty e^{-\alpha x^2}dx = \pi^{1/2} \alpha^{-1/2}$ po $\alpha$: $-\int_{-\infty}^\infty x^2 e^{-\alpha x^2} dx = -\frac{1}{2}\pi^{1/2}\alpha^{-3/2} \implies \frac{1}{2\alpha}\sqrt{\frac{\pi}{\alpha}}$.


\newpage

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


\newpage

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


\newpage

