# Exploratory Record: Wyszukiwarka Nieruchomości Warszawa & RCN Integracja

**ID**: `001-wyszukiwarka-nieruchomosci-001`  
**Date**: 2026-07-26  
**Topic**: Serwis generowania i odświeżania na żądanie ofert nieruchomości w Warszawie z integracją danych transakcyjnych RCN oraz rekomendacjami AI.

---

## 1. Cel Eksploracji

Zbadanie i określenie architektury serwisu `wyszukiwarka-nieruchomosci/` (lokalizowanego w podkatalogu bieżącego repozytorium), którego zadaniem jest:
1. Pobieranie kryteriów wyszukiwania z pliku `wyszukiwarka-nieruchomosci/kryteria.md`.
2. Wyszukiwanie i agregowanie ofert z najpopularniejszych polskich serwisów nieruchomościowych z ograniczeniem do m.st. Warszawy.
3. Pozyskiwanie danych o rzeczywistych cenach transakcyjnych z warszawskiego serwisu RCN (Rejestr Cen Nieruchomości - https://mapa.um.warszawa.pl/rcn-szukaj/).
4. Odświeżanie na żądanie raportów z prowadzeniem pełnej historii – każdy przebieg tworzy unikalny dokument `YYYY-MM-DD-HH24MISS-oferty.md`.
5. Wzbogacenie ofert o rekomendację i analizę opłacalności (np. porównanie ceny ofertowej do cen transakcyjnych RCN w danej dzielnicy/rejonie).

---

## 2. Krytyczna Analiza & Bezwzględna Uczciwość (12 Rules Check)

### 🔴 Wyrażanie Niepewności & Ograniczenia Techniczne (Rules 1, 3, 4, 5):
1. **Dostępność API vs Web Scraping (Otodom / OLX / Morizon)**:
   - *Fakt*: Serwisy takie jak Otodom czy OLX nie udostępniają darmowego, publicznego API REST dla wyszukiwania ofert dla klientów indywidualnych.
   - *[Hipoteza/Domysł]*: Wyszukiwanie będzie musiało opierać się na dedykowanym scrapperze (np. `playwright`, `puppeteer`, `BeautifulSoup` / `httpx` z czyszczeniem HTML) lub wykorzystaniu narzędzi wyszukiwania sieciowego agenta.
   - *Ograniczenie*: Serwisy te stosują zabezpieczenia anty-botowe (Cloudflare, CAPTCHA). Należy założyć mechanizm fallbacku lub parsowania bezpośredniego wyników.

2. **Integracja z Serwisem RCN Warszawskiego Urzędu Miasta (`mapa.um.warszawa.pl/rcn-szukaj`)**:
   - *Fakt*: Serwis RCN (Rejestr Cen Nieruchomości) pod adresem `https://mapa.um.warszawa.pl/rcn-szukaj/` działa w oparciu o aplikację mapową Geoportal Warszawa (usługi Esri ArcGIS WebMap / WFS / REST mapserver lub formularz ASP.NET/JS).
   - *Niepewność*: Serwis RCN nie posiada otwartej, udokumentowanej biblioteki OpenAPI/Swagger. Wyszukiwanie transakcji wymaga automatyzacji zapytań HTTP POST/GET do wewnętrznych endpointów geoportalowych m.st. Warszawy lub pobierania warstwy wektorowej ArcGIS.
   - *Brakujący Kontekst*: Należy ustalić, czy pobieranie danych RCN ma odbywać się wg obrębu ewidencyjnego/dzielnicy, czy uśrednionej stawki za m² w danej dzielnicy z oficjalnych zestawień RCN.

---

## 3. Propozycja Parametrów w `wyszukiwarka-nieruchomosci/kryteria.md`

Proponujemy zaimplementowanie ustandaryzowanego pliku `kryteria.md` (format YAML/Markdown), zawierającego następujące grupy parametrów:

```markdown
# Kryteria Wyszukiwania Nieruchomości

## 📍 Lokalizacja
- **Miasto**: Warszawa (sztywno wymuszone)
- **Dzielnice**: [np. Mokotów, Ursynów, Ochota, Wola, Żoliborz, Śródmieście, Bemowo]
- **Maksymalna odległość od stacji metra (m)**: [np. 1000]

## 🏠 Parametry Nieruchomości
- **Typ nieruchomości**: Mieszkanie / Dom
- **Rynek**: Pierwotny / Wtórny / Dowolny
- **Cena maksymalna (PLN)**: [np. 850 000]
- **Cena minimalna (PLN)**: [np. 400 000]
- **Maksymalna cena za m² (PLN/m²)**: [np. 16 000]
- **Powierzchnia minimalna (m²)**: [np. 45]
- **Powierzchnia maksymalna (m²)**: [np. 75]
- **Liczba pokoi**: [np. 2, 3]
- **Piętro**: [np. min 1, max 8, nie parter, nie ostatnie]
- **Rok budowy**: [np. od 2000 r.]

## 🛠️ Wyposażenie i Wymagania Dodatkowe
- **Winda**: Tak / Bez znaczenia
- **Balkon / Taras / Ogródek**: Tak / Bez znaczenia
- **Miejsce garażowe / parkingowe**: Wymagane / Opcjonalne
- **Stan wykończenia**: Do zamieszkania / Do odświeżania / Dowolny
- **Stan prawny**: Pełna własność / Spółdzielcze własnościowe z KW
```

---

## 4. Wybór Portali Nieruchomościowych do Wyszukiwania

Na rynku polskim zidentyfikowano 5 domynujących portalów ogłoszeniowych w Warszawie:

| Portal | Typ Ogłoszeń | Wyzwania Techniczne | Rekomendacja w Systemie |
| --- | --- | --- | --- |
| **Otodom.pl** | Największa baza unikalnych ofert (biura + prywatne) | Zabezpieczenia botowe, dynamiczny SSR | **Priorytet 1 (Główne źródło)** |
| **OLX.pl** | Dużo ofert prywatnych (często niższe ceny) | Wymaga filtrowania duplikatów z Otodom | **Priorytet 1 (Główne źródło)** |
| **Morizon.pl / Gratka.pl** | Duży zasięg biur nieruchomości | Stabilna struktura HTML | **Priorytet 2 (Uzupełnienie)** |
| **Nieruchomosci-online.pl** | Dobre filtry lokalizacyjne | Prostsza struktura danych | **Priorytet 2 (Uzupełnienie)** |
| **Adresowo.pl** | Oferty bez pośredników | Dostęp częściowo płatny | **Priorytet 3 (Opcjonalnie)** |

---

## 5. Analiza Integracji z RCN Warszawa (`https://mapa.um.warszawa.pl/rcn-szukaj/`)

Rejestr Cen Nieruchomości m.st. Warszawy zbiera **rzeczywiste ceny transakcyjne** z aktów notarialnych.

### Opcje Pobierania Danych z RCN:
1. **Opcja A (Automatyczny Scraper Endpointów RCN Geoportal)**:
   - Skrypt wykonuje zapytanie HTTP POST do API Geoportalu Warszawy (`https://mapa.um.warszawa.pl/mapa/xyz...`) z geo-query dla wybranej dzielnicy i typu lokalu, wyciągając uśrednioną cenę m² transakcyjną z ostatnich 6-12 miesięcy.
2. **Opcja B (Baza Danych Referencyjnych RCN / Tabela Ceny Transakcyjne Dzielnic)**:
   - Agregacja oficjalnych statystyk RCN per dzielnica Warszawy (np. Śródmieście ~18,500 zł/m², Mokotów ~15,200 zł/m², Bemowo ~13,100 zł/m²) i automatyczne wyliczanie odchylenia procentowego ceny ofertowej ogłoszenia od ceny transakcyjnej RCN.

---

## 6. Architektura Generowania Raportu Ofertywnego

Każde uruchomienie serwisu tworzy plik historii w formacie:
`wyszukiwarka-nieruchomosci/historia/YYYY-MM-DD-HH24MISS-oferty.md` (np. `2026-07-26-213127-oferty.md`).

### Struktura Raportu:
1. **Podsumowanie Uruchomienia**: Data, godzina, liczba przeanalizowanych ofert, liczba zakwalifikowanych nieruchomości.
2. **Kryteria Zastosowane w Generowaniu**: Odnośnik do stanu `kryteria.md`.
3. **Lista Wyselekcjonowanych Ofert**:
   - Tytuł ogłoszenia, Link URL, Cena całkowita, Cena za m², Powierzchnia, Liczba pokoi, Dzielnica.
   - **Porównanie z RCN Warszawa**: Średnia cena transakcyjna RCN w tej dzielnicy oraz odchylenie np. *"+8% pow. średniej RCN"*.
4. **Rekomendacja AI**:
   - Ocena opłacalności (Top 3 najlepsze oferty wg wskaźnika cena/jakość/RCN).
   - Sugestie negocjacyjne (np. *"Cena za m² jest o 12% wyższa niż średnia RCN w Śródmieściu – rekomendowany cel negocjacyjny: 780 000 zł"*).
   - Wykrycie ryzyk (brak KW, wysoki czynsz, parter).

---

## 7. Podsumowanie Decyzyjne Eksploracji

Eksploracja wykazuje pełną wykonalność projektu w podkatalogu `wyszukiwarka-nieruchomosci/`.
Przechodzimy do przygotowania dokumentu **Proposal** (`proposal.md`).
