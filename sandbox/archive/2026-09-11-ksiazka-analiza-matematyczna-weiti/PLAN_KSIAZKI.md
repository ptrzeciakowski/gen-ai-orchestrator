# Analiza Matematyczna dla Informatyków i Elektroników
## Podręcznik akademicki dla studentów Wydziału Elektroniki i Technik Informacyjnych Politechniki Warszawskiej (WEiTI PW)
### Opracowany według kanonu dydaktycznego prof. W. Żakowskiego i doc. J. Decewicza

---

## 🧭 Założenia metodologiczne i format podręcznika
Podręcznik łączy ścisły aparat aksjomatyczny współczesnej analizy matematycznej z aparatem pojęciowym i zastosowaniami niezbędnymi w elektrotechnice teoretycznej, teorii obwodów i sygnałów, telekomunikacji oraz informatyce.

Każdy moduł/rozdział zorganizowany jest w ścisłej strukturze:
1. **Wstęp i motywacja fizyczna/inżynierska**: skąd dane pojęcie wynika w praktyce (np. stany nieustalone, analiza widmowa, transmitancje).
2. **Definicje formalne**: precyzyjne sformułowania w języku logiki i teorii mnogości ($\forall, \exists, \varepsilon, \delta$).
3. **Twierdzenia wraz ze ścisłymi dowodami**: dowody konstrukcyjne, nie wprost oraz indukcyjne.
4. **Wnioski i uwagi krytyczne**: pułapki pojęciowe, typowe błędy studenckie na kolokwiach i egzaminach WEiTI.
5. **Wzorcowe przykłady obliczeniowe z pełnymi komentarzami**: techniki rachunkowe od elementarnych do zaawansowanych.
6. **Zadania do samodzielnego rozwiązania z odpowiedziami i wskazówkami**.

---

## 📚 Globalny spis treści i podział na tomy/rozdziały

### TOM I: Ciągi, Szeregi i Rachunek Różniczkowy Funkcji Jednej Zmiennej

#### Część I: Fundamenty analizy matematycznej
- **Rozdział 1**: Ciało liczb rzeczywistych $\mathbb{R}$
  - Aksjomaty ciała, porządku i ciągłości (Dedekind, Cantor).
  - Kresy zbiorów: supremum i infimum, zasada Archimedesa.
  - Wartość bezwzględna, metryka euklidesowa na prostej.
  - Topologia prostej $\mathbb{R}$: otoczenia, zbiory otwarte, domknięte, punkty skupienia, zwartość (Heine-Borel).
- **Rozdział 2**: Ciało liczb zespolonych $\mathbb{C}$
  - Definicja aksjomatyczna i postać algebraiczna ($z = x + iy$).
  - Moduł, sprzężenie i nierówność trójkąta.
  - Postać trygonometryczna i wykładnicza ($z = r e^{i\varphi}$), tożsamość Eulera.
  - Potęgowanie (wzór de Moivre'a) i pierwiastkowanie liczb zespolonych.
  - Interpretacja w teorii obwodów: wskaz napięciowy/prądowy (fazor), impedancja zespolona.

#### Część II: Ciągi liczbowe
- **Rozdział 3**: Granica ciągu liczbowego
  - Definicja Cauchy'ego ($\varepsilon-N$) granicy właściwej.
  - Jedyność granicy i ograniczoność ciągu zbieżnego.
  - Granice niewłaściwe ($\pm\infty$) i symbole nieoznaczone.
- **Rozdział 4**: Twierdzenia o granicach ciągów
  - Arytmetyka granic (suma, iloczyn, iloraz).
  - Twierdzenie o trzech ciągach i o dwóch ciągach.
  - Monotoniczność i ograniczoność a zbieżność (twierdzenie Weierstrassa).
  - Liczba $e$ jako granica ciągu $(1 + 1/n)^n$.
  - Podciągi, twierdzenie Bolzano-Weierstrassa, granice górne i dolne ($\limsup, \liminf$).
  - Warunek zbieżności Cauchy'ego.

#### Część III: Szeregi liczbowe
- **Rozdział 5**: Zbieżność szeregów o wyrazach dodatnich
  - Sumy częściowe i definicja zbieżności.
  - Warunek konieczny zbieżności szeregu ($\lim a_n = 0$).
  - Kryteria porównawcze (zwykłe i ilorazowe).
  - Kryterium d'Alemberta i Cauchy'ego.
  - Kryterium całkowe Maclaurina-Cauchy'ego.
  - Szereg harmoniczny rzędu $\alpha$.
- **Rozdział 6**: Szeregi o wyrazach dowolnych
  - Zbieżność bezwzględna i warunkowa.
  - Szeregi naprzemienne i kryterium Leibniza (oszacowanie reszty).
  - Kryteria Dirichleta i Abla.
  - Przemienność szeregów (twierdzenie Riemanna o permutacjach).
  - Iloczyn Cauchy'ego szeregów (twierdzenie Mertensa).

#### Część IV: Granica i ciągłość funkcji jednej zmiennej
- **Rozdział 7**: Granica funkcji
  - Definicja Cauchy'ego ($\varepsilon-\delta$) oraz Heinego (ciągowa) i dowód ich równoważności.
  - Granice jednostronne i granice w nieskończoności.
  - Arytmetyka granic funkcji i twierdzenie o trzech funkcjach.
  - Granice podstawowych wyrażeń nieoznaczonych ($\frac{\sin x}{x}$, $\frac{e^x-1}{x}$, $\frac{\ln(1+x)}{x}$).
- **Rozdział 8**: Ciągłość funkcji
  - Definicja ciągłości w punkcie i na zbiorze.
  - Klasyfikacja punktów nieciągłości (I i II rodzaju, skoki, osobliwości usuwalne).
  - Własności funkcji ciągłych na przedziale zwartym: twierdzenie Weierstrassa o osiąganiu kresów.
  - Twierdzenie Bolzano-Cauchy'ego (o wartościach pośrednich / własność Darboux) i lokalizacja pierwiastków.
  - Ciągłość jednostajna i twierdzenie Cantora.

#### Część V: Rachunek różniczkowy funkcji jednej zmiennej
- **Rozdział 9**: Pochodna i różniczka funkcji
  - Iloraz różnicowy i definicja pochodnej. Interpretacja geometryczna (styczna) i fizyczna (prędkość chwilowa, prąd elektryczny $i = dq/dt$).
  - Pochodne jednostronne i pochodne nieskończone. Ciągłość a różniczkowalność.
  - Reguły różniczkowania: liniowość, iloczyn, iloraz, pochodna funkcji złożonej i odwrotnej.
  - Różniczka funkcji i jej zastosowanie do rachunku błędów i linearyzacji obwodów nieliniowych.
  - Pochodne wyższych rzędów, wzór Leibniza na $n$-tą pochodną iloczynu.
- **Rozdział 10**: Twierdzenia o wartości średniej i wzór Taylora
  - Lemat Fermata. Twierdzenia Rolle'a, Lagrange'a i Cauchy'ego.
  - Reguła de l'Hospitala (obliczanie symboli nieoznaczonych $\left[\frac{0}{0}\right], \left[\frac{\infty}{\infty}\right], [0 \cdot \infty], [1^\infty]$).
  - Wzór Taylora i Maclaurina z resztą w postaci Peano i Lagrange'a.
  - Rozwinięcia Maclaurina funkcji elementarnych ($e^x, \sin x, \cos x, \ln(1+x), (1+x)^\alpha$).
- **Rozdział 11**: Badanie przebiegu zmienności funkcji
  - Warunki konieczne i dostateczne monotoniczności.
  - Ekstrema lokalne (kryteria z I i II pochodną).
  - Wypukłość, wklęsłość i punkty przegięcia (kryteria z drugą pochodną).
  - Asymptoty pionowe, poziome i ukośne.
  - Algorytm pełnego badania przebiegu zmienności i konstrukcja wykresu.

---

### TOM II: Rachunek Całkowy i Szeregi Funkcyjne

#### Część VI: Całka nieoznaczona
- **Rozdział 12**: Pojęcie funkcji pierwotnej i całki nieoznaczonej
  - Definicja i podstawowe własności.
  - Tablica podstawowych całek elementarnych.
  - Metoda całkowania przez części.
  - Metoda całkowania przez podstawienie (zamiana zmiennych).
- **Rozdział 13**: Techniki całkowania wybranych klas funkcji
  - Całkowanie funkcji wymiernych: algorytm rozkładu na ułamki proste I i II rodzaju.
  - Całkowanie wyrażeń trygonometrycznych: podstawienie uniwersalne $t = \operatorname{tg}\frac{x}{2}$ oraz podstawienia specjalne ($t = \operatorname{tg} x, t = \sin x, t = \cos x$).
  - Całkowanie wyrażeń niewymiernych: pierwiastki liniowe i ułamkowo-liniowe.
  - Podstawienia Eulera (I, II i III) dla całek $\int R(x, \sqrt{ax^2+bx+c})\,dx$.

#### Część VII: Całka oznaczona i całki niewłaściwe
- **Rozdział 14**: Całka oznaczona Riemanna
  - Podział przedziału, sumy Darboux i sumy Riemanna.
  - Warunki całkowalności (całkowalność funkcji ciągłych i monotonicznych).
  - Własności całki oznaczonej: liniowość, addytywność, twierdzenie o wartości średniej.
  - Podstawowe Twierdzenie Rachunku Całkowego (wzór Newtona-Leibniza).
  - Całkowanie przez części i przez podstawienie w całce oznaczonej (zamiana granic).
- **Rozdział 15**: Zastosowania geometryczne i inżynierskie całki oznaczonej
  - Obliczanie pól obszarów płaskich (we współrzędnych kartezjańskich i biegunowych).
  - Długość łuku krzywej (postać jawna, parametryczna, biegunowa).
  - Objętość i pole powierzchni brył obrotowych.
  - Zastosowania w elektronice i fizyce: praca, energia pola, ładunek elektryczny, wartość skuteczna (RMS) i średnia przebiegów okresowych.
- **Rozdział 16**: Całki niewłaściwe
  - Całki niewłaściwe I rodzaju (w przedziale nieskończonym).
  - Całki niewłaściwe II rodzaju (funkcji nieograniczonej).
  - Kryteria zbieżności całek niewłaściwych (porównawcze, ilorazowe, Dirichleta, Abla).
  - Wartość główna całki w sensie Cauchy'ego (v.p.).

#### Część VIII: Szeregi funkcyjne, potęgowe i wprowadzenie do analizy fourierowskiej
- **Rozdział 17**: Szeregi funkcyjne i potęgowe
  - Zbieżność punktowa i jednostajna ciągu i szeregu funkcyjnego.
  - Kryterium Weierstrassa zbieżności jednostajnej.
  - Własności sumy szeregu jednostajnie zbieżnego (ciągłość, różniczkowanie i całkowanie wyraz po wyrazie).
  - Szeregi potęgowe: twierdzenie Cauchy'ego-Hadamarda, promień i przedział zbieżności.
  - Szereg Taylora i Maclaurina: analityczność funkcji, warunki rozwijalności.
- **Rozdział 18**: Trygonometryczne szeregi Fouriera
  - Układ ortogonalny funkcji trygonometrycznych.
  - Współczynniki Fouriera Eulera.
  - Warunki Dirichleta zbieżności szeregu Fouriera.
  - Rozwijanie funkcji parzystych, nieparzystych i okresowych.
  - Tożsamość Parsevala i widmo sygnału (zastosowanie w teorii sygnałów i telekomunikacji).

---

### TOM II: Funkcje Wielu Zmiennych, Całki Wielokrotne, Analiza Wektorowa i Równania Różniczkowe

#### Część IX: Rachunek różniczkowy funkcji wielu zmiennych
- **Rozdział 19**: Topologia przestrzeni $\mathbb{R}^n$, granice i ciągłość
  - Przestrzeń euklidesowa $\mathbb{R}^n$, iloczyn skalarny, norma euklidesowa, metryka, kule otwarte i domknięte.
  - Topologia w $\mathbb{R}^n$: punkty wewnętrzne, brzegowe, skupienia, zbiory otwarte, domknięte, zwarte (twierdzenie Heinego-Borela), zbiory spójne i obszary.
  - Ciągi punktów w $\mathbb{R}^n$ i zbieżność po współrzędnych.
  - Granice funkcji wielu zmiennych (definicja Heinego i Cauchy'ego), granice iterowane a granica podwójna.
  - Ciągłość funkcji wielu zmiennych, twierdzenie Weierstrassa o osiąganiu kresów na zbiorze zwartym, własność Darboux dla obszarów spójnych.
- **Rozdział 20**: Różniczkowalność, gradient, wzór Taylora i ekstrema
  - Pochodne cząstkowe I rzędu, interpretacja geometryczna (przekroje płaszczyznami).
  - Różniczkowalność (Frechet), różniczka zupełna, macierz Jacobiego, wektor gradientu $\nabla f$.
  - Płaszczyzna styczna do powierzchni $z=f(x,y)$ i prosta normalna.
  - Pochodna kierunkowa: definicja, związek z gradientem $\frac{\partial f}{\partial \vec{v}} = \nabla f \cdot \vec{v}$, kierunek najszybszego wzrostu i spadek gradientowy (uczenie maszynowe, sieci neuronowe), linie ekwipotencjalne a wektor natężenia pola elektrycznego $\vec{E} = -\nabla V$.
  - Pochodne cząstkowe wyższych rzędów, twierdzenie Schwarza o równości pochodnych mieszanych.
  - Różniczki wyższych rzędów, wzór Taylora i Maclaurina dla funkcji wielu zmiennych z resztą Peano i Lagrange'a.
  - Macierz Hessego (hesjan), formy kwadratowe, kryterium Sylvestera określoności macierzy.
  - Ekstrema lokalne bezwarunkowe (warunek konieczny Fermata $\nabla f = \vec{0}$, warunki dostateczne z hesjanem, punkty siodłowe).
  - Ekstrema warunkowe i metoda mnożników Lagrange'a (optymalizacja parametrów obwodów i filtrów, dopasowanie impedancji).
  - Funkcje uwikłane: twierdzenie o istnieniu i różniczkowalności funkcji uwikłanej jednej i wielu zmiennych, wyznaczanie pochodnych i ekstremów funkcji uwikłanej.

#### Część X: Całki wielokrotne
- **Rozdział 21**: Całka podwójna i jej zastosowania
  - Całka podwójna Riemanna po prostokącie i obszarach regularnych (normalnych), twierdzenie Fubiniego o zamianie na całki iterowane.
  - Zamiana zmiennych w całce podwójnej, jakobian przekształcenia, współrzędne biegunowe.
  - Zastosowania całek podwójnych: pole obszaru, objętość bryły, pole płata powierzchniowego ($dS = \sqrt{1 + (f'_x)^2 + (f'_y)^2}\,dx\,dy$).
  - Masa obszaru płaskiego o zmiennej gęstości powierzchniowej $\sigma(x,y)$, momenty statyczne, środek ciężkości, momenty bezwładności (biegunowe, osiowe).
- **Rozdział 22**: Całka potrójna i całki niewłaściwe wielokrotne
  - Całka potrójna Riemanna: definicja, twierdzenie Fubiniego po prostopadłościanie i obszarach przestrzennych regularnych.
  - Zamiana zmiennych w całkach potrójnych: współrzędne walcowe (cylindryczne) i współrzędne sferyczne (kuliste), jakobiany przekształceń ($J=r$ oraz $J=r^2\sin\theta$).
  - Zastosowania fizyczne w elektrodynamice: całkowity ładunek w objętości $Q = \iiint \rho(x,y,z)\,dV$, masa bryły, środek masy, tensor momentu bezwładności, potencjał grawitacyjny i elektrostatyczny ciągłego rozkładu masy/ładunku.
  - Całki niewłaściwe wielokrotne: całka Poissona-Gaussa $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt{\pi}$ (dowód przez całkę podwójną we współrzędnych biegunowych - fundament statystyki, teorii szumów gaussowskich i przetwarzania sygnałów).

#### Część XI: Całki krzywoliniowe, powierzchniowe i analiza wektorowa
- **Rozdział 23**: Całki krzywoliniowe i twierdzenie Greena
  - Krzywe w $\mathbb{R}^3$, wektor styczny, regularność, łukowa parametryzacja.
  - Całka krzywoliniowa nieskierowana (I rodzaju) i jej zastosowania (masa drutu, ładunek linijowy).
  - Całka krzywoliniowa skierowana (II rodzaju), praca pola sił/elektrycznego $W = \int_K \vec{F} \cdot d\vec{r}$, cyrkulacja pola wektorowego.
  - Warunek niezależności całki od drogi całkowania, pole potencjalne, gradient, warunek bezwirowości ($\operatorname{rot} \vec{F} = \vec{0}$), wyznaczanie potencjału skalarnego.
  - Twierdzenie Greena na płaszczyźnie, obliczanie pól za pomocą całki krzywoliniowej, związek z prawem Ampère'a.
- **Rozdział 24**: Całki powierzchniowe, twierdzenia Gaussa-Ostrogradskiego i Stokesa oraz elektrodynamika Maxwella
  - Płaty powierzchniowe zorientowane, wektor normalny.
  - Całka powierzchniowa nieskierowana (I rodzaju - masa powłoki, ładunek powierzchniowy).
  - Całka powierzchniowa skierowana (II rodzaju - strumień pola wektorowego przez powierzchnię $\iint_S \vec{F} \cdot d\vec{S}$).
  - Operatory różniczkowe pola: gradient ($\nabla f$), dywergencja ($\operatorname{div} \vec{F} = \nabla \cdot \vec{F}$), rotacja ($\operatorname{rot} \vec{F} = \nabla \times \vec{F}$), laplasjan ($\Delta f = \nabla^2 f$). Tożsamości wektorowe ($\operatorname{rot}(\nabla f) = \vec{0}$, $\operatorname{div}(\operatorname{rot} \vec{F}) = 0$).
  - Twierdzenie Gaussa-Ostrogradskiego (o dywergencji) - interpretacja fizyczna źródeł pola.
  - Twierdzenie Stokesa (o rotacji) - interpretacja cyrkulacji pola i zjawiska indukcji Faradaya.
  - Zwieńczenie analizy wektorowej: Układ równań elektrodynamiki Maxwella w postaci różniczkowej i całkowej (prawa Gaussa dla elektryczności i magnetyzmu, prawo Faradaya, prawo Ampère'a-Maxwella) wraz z wyprowadzeniem równania falowego dla fal elektromagnetycznych.

#### Część XII: Równania różniczkowe zwyczajne (ODE) w elektronice i informatyce
- **Rozdział 25**: Równania różniczkowe rzędu pierwszego
  - Podstawowe pojęcia: rząd równania, rozwiązanie ogólne (CORZ), szczególne (CSRZ), osobliwe, zagadnienie początkowe Cauchy'ego, twierdzenie Picarda-Lindelöfa o istnieniu i jedyności.
  - Równania o zmiennych rozdzielonych.
  - Równania jednorodne względem zmiennych ($y' = f(y/x)$).
  - Równania liniowe I rzędu: metoda uzmienniania stałej (Lagrange) i czynnik całkujący.
  - Równanie różniczkowe Bernoulliego.
  - Równania zupełne i wyznaczanie czynnika całkującego $\mu(x)$ lub $\mu(y)$.
  - Zastosowania I rzędu: obwody RC i RL, stan nieustalony, stała czasowa $\tau = RC$ lub $\tau = L/R$, ładowanie i rozładowanie kondensatora.
- **Rozdział 26**: Równania liniowe wyższych rzędów i metoda transformaty Laplace'a
  - Przestrzeń liniowa rozwiązań równania jednorodnego, liniowa niezależność funkcji i wrońskian (twierdzenie Liouville'a).
  - Równania liniowe o stałych współczynnikach rzędu drugiego i $n$-tego: wielomian charakterystyczny, pierwiastki rzeczywiste proste, wielokrotne, zespolone sprzężone.
  - Wyznaczanie CSRZ: metoda przewidywań (dla wymuszeń wielomianowych, wykładniczych, trygonometrycznych i ich iloczynów z rezonansem) oraz uniwersalna metoda uzmienniania stałych Lagrange'a.
  - Modelowanie zjawisk oscylacyjnych i rezonansowych: szeregowy i równoległy obwód RLC, oscylacje tłumione (nadkrytyczne, aperiodyczne krytyczne, podkrytyczne oscylacyjne), dobroć obwodu $Q$, rezonans napięć/prądów.
  - Wprowadzenie do operatorowej metody transformaty Laplace'a: definicja transformaty Laplace'a jednostronnej, własności (liniowość, przesunięcie w czasie/częstotliwości, pochodna, całka, splot).
  - Odpowiedź impulsowa (funkcja delta Diraca $\delta(t)$) i skokowa (funkcja Heaviside'a $\mathbf{1}(t)$).
  - Rozwiązywanie równań różniczkowych z warunkami początkowymi metodą operatorową, rozkład na ułamki proste w dziedzinie $s$.
  - Transmitancja operatorowa $H(s) = Y(s)/X(s)$ układu liniowego, bieguny i zera transmitancji a stabilność układu (kryterium Hurwitza).

