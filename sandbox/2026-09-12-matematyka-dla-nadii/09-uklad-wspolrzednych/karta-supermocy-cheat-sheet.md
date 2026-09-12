# KARTA SUPERMOCY: UKŁAD WSPÓŁRZĘDNYCH (Klasa 7 & 8)
## Sprytne Metody Nadii – Nawigacja GPS, Średnia Współrzędnych i Pitagoras na Kratkach

---

### 📍 1. NAWIGACJA GPS: PUNKT $(x, y)$
- **$x$ (oś pozioma $OX$):** idziesz po korytarzu w lewo ($-$) lub w prawo ($+$).
- **$y$ (oś pionowa $OY$):** jedziesz windą w dół ($-$) lub w górę ($+$).
> 🚨 **Pułapka zer:**
> - Punkt na osi $OX$ ma postać $(x, 0)$, np. $(5, 0)$.
> - Punkt na osi $OY$ ma postać $(0, y)$, np. $(0, -3)$.

---

### 🎯 2. ŚRODEK ODCINKA = ZWYKŁA ŚREDNIA ARYTMETYCZNA!
Masz punkty $A(x_1, y_1)$ i $B(x_2, y_2)$? Środek $S$ to po prostu średnia z ich współrzędnych:
$$S = \left( \frac{x_1 + x_2}{2}, \; \frac{y_1 + y_2}{2} \right)$$
*Przykład: $A(1, 7)$ i $B(5, 3) \implies S = \left(\frac{1+5}{2}, \frac{7+3}{2}\right) = \mathbf{(3, 5)}$*

---

### 📏 3. DŁUGOŚĆ ODCINKA (Pitagoras na Kratkach)
Nie ucz się skomplikowanego wzoru na pamięć!
Dorysuj trójkąt prostokątny na kratkach i policz boki:
- Poziomy bok: $\Delta x = |x_2 - x_1|$
- Pionowy bok: $\Delta y = |y_2 - y_1|$
- Długość odcinka: **$d = \sqrt{(\Delta x)^2 + (\Delta y)^2}$**
*Przykład: Od $(2, 1)$ do $(6, 4)$ $\implies$ w poziomie 4, w pionie 3 $\implies$ święta trójka 3-4-5 $\implies$ **długość = 5!***

---

### 🪞 4. LUSTRA I SYMETRIE
- **Odbicie w osi $OX$:** punkt przeskakuje góra-dół $\implies$ **$y$ zmienia znak**: $(x, \mathbf{-y})$
  *$(3, 4) \to (3, -4)$*
- **Odbicie w osi $OY$:** punkt przeskakuje lewo-prawo $\implies$ **$x$ zmienia znak**: $(\mathbf{-x}, y)$
  *$(3, 4) \to (-3, 4)$*
- **Odbicie w początku $(0,0)$:** punkt przeskakuje po skosie $\implies$ **OBA znaki się zmieniają**: $(\mathbf{-x}, \mathbf{-y})$
  *$(3, 4) \to (-3, -4)$*

---

### 📦 5. METODA PUDEŁKA NA POLE FIGURY NA KRATKACH
Gdy masz obliczyć pole skośnego trójkąta w układzie współrzędnych:
1. Narysuj wokół niego prostokątne "pudełko" o bokach równoległych do osi.
2. Policz pole prostokąta: $P_{\text{box}} = a \cdot b$.
3. Odejmij pola narożnych trójkątów prostokątnych!
