# Exploratory Record: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `001-wyszukiwarka-nieruchomosci-001`  
**Date**: 2026-07-26  
**Topic**: Serwis generowania i odświeżania na żądanie ofert nieruchomości w Warszawie z integracją danych transakcyjnych RCN, 5-kwantylową analizą rynkową (N, P10, P25, P50, P75, P90) per dzielnice i obszary MSI, obsługą źródeł bezpośrednich oraz rejestrowaniem faktycznie zastosowanych kryteriów dla pełnej audytowalności.

---

## 1. Cel Eksploracji

Zbadanie i określenie architektury serwisu `wyszukiwarka-nieruchomosci/` (lokalizowanego w podkatalogu bieżącego repozytorium), którego zadaniem jest:
1. Odczyt i parsowanie **faktycznie zastosowanych kryteriów wyszukiwania** z pliku `wyszukiwarka-nieruchomosci/kryteria.md` z dołączeniem ich pełnego zapisu w raporcie dla zachowania pełnej audytowalności.
2. Wyszukiwanie i agregowanie ofert zarówno z największych portali ogólnych, jak i z serwisów o wysokim udziale ofert bezpośrednich (bez agencji nieruchomości).
3. Pozyskiwanie danych o rzeczywistych cenach transakcyjnych z warszawskiego serwisu RCN (Rejestr Cen Nieruchomości - https://mapa.um.warszawa.pl/rcn-szukaj/) z rozbiciem na dzielnice i obszary MSI oraz 5-elementowym rozkładem kwantylowym ($N$, Średnia, P10, P25, P50-mediana, P75, P90).
4. Odświeżanie na żądanie raportów z prowadzeniem pełnej historii – każdy przebieg tworzy unikalny dokument `YYYY-MM-DD-HH24MISS-oferty.md`.
5. Wzbogacenie ofert o rekomendację i analizę opłacalności (porównanie ceny ofertowej do cen transakcyjnych RCN w danej dzielnicy/rejonie).

---

## 2. Krytyczna Analiza & Bezwzględna Uczciwość (12 Rules Check)

### 🔴 Wyrażanie Niepewności & Ograniczenia Techniczne (Rules 1, 3, 4, 5):
1. **Dostępność API vs Web Scraping (Otodom / OLX / Morizon / Adresowo)**:
   - *Fakt*: Serwisy nieruchomościowe nie udostępniają jednolitego, otwartego API REST dla klientów indywidualnych.
   - *Rozwiązanie*: Wyszukiwanie opiera się na dedykowanych scraperach providerów (`src/providers/commercial.py` oraz `src/providers/direct.py`) parsujących żywy kod HTML i JSON-LD z weryfikacją autentyczności linków.
   - *Zakaz zmyślania (Rules 7 & 9)*: Każda oferta prezentowana w dokumencie wyjściowym MUSI posiadać autentyczny, klikalny i aktywny w sieci odnośnik URL.

2. **Integracja z Serwisem RCN Warszawskiego Urzędu Miasta (`mapa.um.warszawa.pl/rcn-szukaj`)**:
   - *Fakt*: Serwis RCN (Rejestr Cen Nieruchomości) zbiera ceny z aktów notarialnych pod adresem `https://mapa.um.warszawa.pl/rcn-szukaj/`.
   - *Wskaźniki*: Zapewnienie rozbicia statystycznego na 5 kwantyli ($P10, P25, P50, P75, P90$) oraz podawanie dokładnej liczby transakcji $N$ i okresu zbierania danych.

---

## 3. Rozszerzona Lista Źródeł Ogłoszeń

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
8. **Nethouse.pl / Podlupa.pl**: Niszowe serwisy agregujące i publikujące bezpośrednie oferty właścicieli.
9. **Facebook Marketplace & Grupy Warszawskie** (np. *"Mieszkania Warszawa Bez Pośredników"*): Kluczowe źródło najświeższych ofert prywatnych.

---

## 4. Specyfikacja Parametrów w `wyszukiwarka-nieruchomosci/kryteria.md`

Proponujemy zaimplementowanie ustandaryzowanego pliku `kryteria.md` (format YAML/Markdown), zawierającego następujące grupy parametrów:

```markdown
# Kryteria Wyszukiwania Nieruchomości

## 📍 Lokalizacja
- **Miasto**: Warszawa (sztywno wymuszone)
- **Dzielnice**: [np. Mokotów, Ursynów, Ochota, Wola, Żoliborz, Śródmieście, Bemowo]
- **Maksymalna odległość od stacji metra (m)**: [np. 1200]

## 🏠 Parametry Nieruchomości
- **Typ nieruchomości**: Mieszkanie / Dom
- **Typ ogłoszeniodawcy**: Bezpośrednio (właściciel) / Agencja / Dowolny
- **Rynek**: Pierwotny / Wtórny / Dowolny
- **Cena maksymalna (PLN)**: [np. 950 000]
- **Cena minimalna (PLN)**: [np. 450 000]
- **Maksymalna cena za m² (PLN/m²)**: [np. 17 500]
- **Powierzchnia minimalna (m²)**: [np. 40]
- **Powierzchnia maksymalna (m²)**: [np. 75]
- **Liczba pokoi**: [np. 2, 3]
- **Piętro**: [np. min 1, max 8, nie parter, nie ostatnie]
- **Rok budowy**: [np. od 1995 r.]

## 🛠️ Wyposażenie i Wymagania Dodatkowe
- **Winda**: Tak / Bez znaczenia
- **Balkon / Taras / Ogródek**: Tak / Bez znaczenia
- **Miejsce garażowe / parkingowe**: Wymagane / Opcjonalne
- **Stan wykończenia**: Do zamieszkania / Do odświeżenia / Dowolny
- **Stan prawny**: Pełna własność / Spółdzielcze własnościowe z KW / Dowolny
```

---

## 5. Podsumowanie Decyzyjne Eksploracji

Eksploracja wykazuje pełną wykonalność projektu w podkatalogu `wyszukiwarka-nieruchomosci/` z zachowaniem pełnej audytowalności kryteriów i rozszerzonym modułem kwantylowym RCN.
