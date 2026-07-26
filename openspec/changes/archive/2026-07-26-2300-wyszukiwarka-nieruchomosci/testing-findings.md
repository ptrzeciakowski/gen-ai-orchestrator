# Wyniki Testowania Funkcjonalnego i Diagnostycznego (Live Testing Findings)

**Data testowania**: 2026-07-26  
**Metodologia**: 3 Sub-Agenty Diagnostyczne (w tym Live HTTP Testing i Pipeline Benchmarks) w połączeniu z testami zapytań terminala.

---

## 1. 🌐 Testy Zapytań HTTP i Scraperów Bezpośrednich (`direct.py`)

### 🔴 Znalezisko: Błąd HTTP 404 w Adresowo.pl i Odcięcie Ofert Bezpośrednich
- **Pojawiający się błąd**: `HTTP Error 404: Not Found` przy uderzeniu na URL `https://adresowo.pl/ogloszenia/mieszkania/warszawa/?p=1`.
- **Diagnoza Live**: Serwis Adresowo zmienił schemat adresacji URL i zwraca kod HTTP 404 dla ścieżki `/ogloszenia/`.
- **Prawidłowy Schemat URL**: Poprawny i autentyczny endpoint z listą mieszkań na Adresowo.pl to `https://adresowo.pl/mieszkania/warszawa/` (lub z podziałem na dzielnice np. `https://adresowo.pl/mieszkania/warszawa-mokotow/`).
- **Skutek**: Z powodu błędu 404 provider ogłoszeń bezpośrednich zwracał 0 wyników, przez co w raporcie znajdowały się wyłącznie ogłoszenia agencji z OLX.

---

## 2. 🗺️ Testy Dzielnicowe i Etykietowania Sprzedawcy (`commercial.py`)

### 🔴 Znalezisko 1: Wszędzie Przypisany "Mokotów" (Dominacja Pierwszej Dzielnicy)
- **Diagnoza**: Kod wysyłał ogólne zapytanie na całą Warszawę `.../sprzedaz/warszawa/`, a następnie sprawdzał obecność słowa kluczowego dzielnicy w ścieżce URL oferty (`if d.lower() in clean_href.lower()`).
- **Powód usterki**: OLX nie generuje nazw dzielnic w slugach URL (np. `/d/oferta/piekne-mieszkanie-ID123.html`). W efekcie instrukcja warunkowa zawsze wpadała w fallback: `district = self.config.districts[0]`, który ustawiał pierwszą dzielnicę z pliku `kryteria.md` (Mokotów).
- **Poprawka**: Należy odpytywać dedykowane URL-e dla każdej dzielnicy z osobna:
  - `https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa-mokotow/`
  - `https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa-ursynow/`
  - `https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/warszawa-wilanow/`

### 🔴 Znalezisko 2: Zduplikowane Linki HTML i Wyłączny Tag "Agencja"
- **Diagnoza**: Na stronach OLX każda karta oferty zawiera 2 linki HTML (jeden w miniaturce zdjęcia, drugi w tytule). Pętla parsująca iterowała po wszystkich linkach z `idx=1,2,3,4...` i wyznaczała typ sprzedawcy wyrażeniem: `seller = "Bezpośrednio" if idx % 2 == 0 else "Agencja"`.
- **Powód usterki**: Linki parzyste (`idx=2,4,6...`) były odrzucane przez `seen_urls.add()` jako duplikaty. W efekcie wszystkie nieodrzucone oferty otrzymywały indeksy nieparzyste (`idx=1,3,5...`) i sztywną etykietę "Agencja".
- **Poprawka**: Usuwanie duplikatów ze zbioru linków przed wyznaczaniem parametru oraz wysyłanie do serwisu OLX oficjalnego parametru filtrującego `&search%5Bprivate_business%5D=private` dla pobierania autentycznych ofert prywatnych!

---

## 3. ⚙️ Testy Funkcjonalne Pipeline'u Executora (`main.py`)

### 📊 Statystyki Przepływu Ofert przed Naprawą:
1. Pobranie z Adresowo.pl: `0 ofert` (błąd 404).
2. Pobranie z OLX.pl: `18 ofert` (wszystkie przypisane do Mokotowa).
3. Przydział Dzielnic: `Mokotów: 100%`, `Ursynów: 0%`, `Wilanów: 0%`.
4. Typ Sprzedawcy: `Agencja: 100%`, `Bezpośrednio: 0%`.
