# Exploratory Record: Wyszukiwarka Nieruchomości Warszawa & RCN Integracja

**ID**: `001-wyszukiwarka-nieruchomosci-001`  
**Date**: 2026-07-26  
**Topic**: Serwis generowania i odświeżania na żądanie ofert nieruchomości w Warszawie z integracją danych transakcyjnych RCN, obsługą źródeł bezpośrednich (bez pośredników) oraz rekomendacjami AI.

---

## 1. Cel Eksploracji

Zbadanie i określenie architektury serwisu `wyszukiwarka-nieruchomosci/` (lokalizowanego w podkatalogu bieżącego repozytorium), którego zadaniem jest:
1. Pobieranie kryteriów wyszukiwania z pliku `wyszukiwarka-nieruchomosci/kryteria.md`.
2. Wyszukiwanie i agregowanie ofert zarówno z największych portali ogólnych, jak i z serwisów o wysokim udziale ofert bezpośrednich (bez agencji nieruchomości).
3. Pozyskiwanie danych o rzeczywistych cenach transakcyjnych z warszawskiego serwisu RCN (Rejestr Cen Nieruchomości - https://mapa.um.warszawa.pl/rcn-szukaj/).
4. Odświeżanie na żądanie raportów z prowadzeniem pełnej historii – każdy przebieg tworzy unikalny dokument `YYYY-MM-DD-HH24MISS-oferty.md`.
5. Wzbogacenie ofert o rekomendację i analizę opłacalności (porównanie ceny ofertowej do cen transakcyjnych RCN w danej dzielnicy/rejonie).

---

## 2. Rozszerzona Lista Źródeł Ogłoszeń (z uwzględnieniem portali bezpośrednich i niszowych)

Na rynku polskim zidentyfikowano 2 kategorie źródeł ogłoszeniowych w Warszawie:

### Kategoria A: Główne Portale Ogłoszeniowe (Agencje + Prywatne)
1. **Otodom.pl**: Największa baza unikalnych ofert na rynku warszawskim.
2. **OLX.pl**: Ogromny udział ogłoszeń prywatnych i biurowych.
3. **Morizon.pl / Gratka.pl**: Szeroki zasięg biur nieruchomości.
4. **Nieruchomosci-online.pl**: Precyzyjne filtry lokalizacyjne.

### Kategoria B: Portale Bezpośrednie & Mniej Popularne Wśród Agencji (Bez Pośredników / Prywatne)
5. **Adresowo.pl**: Portal wyspecjalizowany w ogłoszeniach bezpośrednich od właścicieli (weryfikacja braku agencji).
6. **Sprzedajemy.pl**: Portal z dużą ilością bezpłatnych ogłoszeń prywatnych, rzadziej używany przez masowe agencje.
7. **Lento.pl**: Portal ogłoszeniowy charakteryzujący się ofertami od osób prywatnych omijających płatne pakiety agencji.
8. **Nethouse.pl / Podlupa.pl**: Niszowe serwisy agragujące i publikujące bezpośrednie oferty właścicieli.
9. **Facebook Marketplace & Grupy Warszawskie** (np. *"Mieszkania Warszawa Bez Pośredników"*): Kluczowe źródło najświeższych ofert prywatnych.

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
- **Typ ogłoszeniodawcy**: Bezpośrednio (właściciel) / Agencja / Dowolnie
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

## 4. Analiza Integracji z RCN Warszawa (`https://mapa.um.warszawa.pl/rcn-szukaj/`)

Rejestr Cen Nieruchomości m.st. Warszawy zbiera **rzeczywiste ceny transakcyjne** z aktów notarialnych.

### Opcje Pobierania Danych z RCN:
1. **Opcja A (Automatyczny Scraper Endpointów RCN Geoportal)**:
   - Skrypt wykonuje zapytanie HTTP POST do API Geoportalu Warszawy (`https://mapa.um.warszawa.pl/mapa/xyz...`) z geo-query dla wybranej dzielnicy i typu lokalu, wyciągając uśrednioną cenę m² transakcyjną z ostatnich 6-12 miesięcy.
2. **Opcja B (Baza Danych Referencyjnych RCN / Tabela Ceny Transakcyjne Dzielnic)**:
   - Agregacja oficjalnych statystyk RCN per dzielnica Warszawy i automatyczne wyliczanie odchylenia procentowego ceny ofertowej ogłoszenia od ceny transakcyjnej RCN.

---

## 5. Podsumowanie Decyzyjne Eksploracji

Eksploracja wykazuje pełną wykonalność projektu w podkatalogu `wyszukiwarka-nieruchomosci/` z rozszerzeniem o portale bezpośrednie (Adresowo, Sprzedajemy, Lento, FB Marketplace). Przechodzimy do aktualizacji dokumentu **Proposal** (`proposal.md`).
