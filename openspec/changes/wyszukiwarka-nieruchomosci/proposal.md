# Proposal: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `wyszukiwarka-nieruchomosci`  
**Date**: 2026-07-26  

## Summary
Stworzenie serwisu w podkatalogu `wyszukiwarka-nieruchomosci/`, który na żądanie generuje i odświeża dokumentację aktualnych ofert nieruchomości z rynku warszawskiego (zarówno z portali komercyjnych, jak i serwisów z ogłoszeniami bezpośrednimi od właścicieli, np. Adresowo.pl, Sprzedajemy.pl, Lento.pl), dopasowanych do kryteriów w pliku `wyszukiwarka-nieruchomosci/kryteria.md`, wzbogaconych o dane o cenach transakcyjnych z warszawskiego Rejestru Cen Nieruchomości (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/) z rozkładem kwantylowym (N, P10, P25, P50, P75, P90), rekomendacje AI oraz **rejestrację faktycznie zastosowanych kryteriów wyszukiwania dla zapewnienia pełnej audytowalności**.

---

## Motivation
Poszukiwanie nieruchomości na rynku warszawskim wymaga automatyzacji pobierania ofert nie tylko z dużych portali zdominowanych przez agencje (Otodom, OLX), ale w szczególności z serwisów skupionych na ogłoszeniach bezpośrednich od właścicieli (Adresowo, Sprzedajemy, Lento). W połączeniu z weryfikacją cen transakcyjnych z RCN Warszawa pozwala to inwestorowi/kupującemu na:
- Natychmiastowe wyłapywanie okazji bez marży pośrednika,
- Zestawianie cen ofertowych z oficjalnymi cenami transakcyjnymi z aktów notarialnych (RCN Warszawa) z uwzględnieniem liczby transakcji $N$, okresu i centyli ($P10, P25, P50, P75, P90$),
- Prowadzenie historii wyników w plikach `YYYY-MM-DD-HH24MISS-oferty.md`,
- Zachowanie **pełnej audytowalności** poprzez wyraźne rejestrowanie w nagłówku każdego raportu faktycznie zastosowanych kryteriów odczytanych z `kryteria.md`,
- Generowanie bezstronnych rekomendacji AI i ocen potencjału negocjacyjnego.

---

## Proposed Changes

### 1. Struktura Katalogu `wyszukiwarka-nieruchomosci/`
Utworzenie podkatalogu zawierającego:
- `kryteria.md`: Konfigurowalny plik z parametrami wyszukiwania (budżet, cena za m², powierzchnia, dzielnice, piętro, stan prawny, filtr `Typ ogłoszeniodawcy: Bezpośrednio / Agencja / Dowolny`).
- `historia/`: Katalog na wygenerowane pliki wyników w formacie `YYYY-MM-DD-HH24MISS-oferty.md`.
- `src/`: Skrypty pobierające i agregujące oferty z wielu źródeł, deduplikator oraz integracja z RCN Warszawa.

### 2. Integracja z Rozszerzoną Listą Portali Nieruchomościowych
Wyszukiwanie ofert w oparciu o kryteria na portalach:
- **Główne Portale**: Otodom.pl, OLX.pl, Morizon.pl, Nieruchomosci-online.pl.
- **Portale Bezpośrednie & Mniej Popularne Wśród Agencji**: Adresowo.pl, Sprzedajemy.pl, Lento.pl, Nethouse.pl.

### 3. Integracja z RCN Warszawa (https://mapa.um.warszawa.pl/rcn-szukaj/)
- Zbieranie danych o cenach transakcyjnych w dzielnicach oraz obszarach MSI Warszawy (np. Kabaty, Natolin, Służew, Filtry) z bazy RCN.
- Prezentowanie wskaźników: Okres danych, Liczba transakcji $N$, Średnia, $10.$ Centyl (P10), $1.$ Kwartyl (P25), Mediana (P50), $3.$ Kwartyl (P75) oraz $90.$ Centyl (P90).
- Porównywanie cen ofertowych wyselekcjonowanych ogłoszeń do cen transakcyjnych RCN w danej dzielnicy (wyliczanie % odchylenia).

### 4. Audytowalność i Format Wyników (`YYYY-MM-DD-HH24MISS-oferty.md`)
Każde uruchomienie tworzy nowy plik zawierający:
- **Sekcję `## ⚙️ Faktycznie Zastosowane Kryteria Wyszukiwania`** (rejestrującą ścieżkę do `kryteria.md` oraz dokładne wartości parametrów użyte w wywołaniu),
- Zestawienie dopasowanych ofert wraz z oznaczeniem źródła, typu ogłoszeniodawcy i metryk RCN,
- Sekcję **Rekomendacja AI** (Top 3 najopłacalniejsze nieruchomości, potencjał negocjacyjny vs RCN kwantyle, analiza ryzyk).

---

## Non-Goals
- Wynoszenie modułu do osobnego repozytorium (zgodnie z prośbą pozostajemy w podkatalogu `wyszukiwarka-nieruchomosci/`).
- Wyszukiwanie ofert poza obszarem m.st. Warszawy.
- Tworzenie dedykowanego interfejsu graficznego GUI.
