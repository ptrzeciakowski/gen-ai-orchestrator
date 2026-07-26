# Proposal: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `wyszukiwarka-nieruchomosci`  
**Date**: 2026-07-26  

## Summary
Stworzenie serwisu w podkatalogu `wyszukiwarka-nieruchomosci/`, który na żądanie generuje i odświeża dokumentację aktualnych ofert nieruchomości z rynku warszawskiego (zarówno z głównych portali, jak i serwisów z ogłoszeniami bezpośrednimi od właścicieli, np. Adresowo.pl, Sprzedajemy.pl, Lento.pl), dopasowanych do kryteriów w pliku `wyszukiwarka-nieruchomosci/kryteria.md`, wzbogaconych o dane o cenach transakcyjnych z warszawskiego Rejestru Cen Nieruchomości (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/) oraz rekomendacje i analizę opłacalności AI.

---

## Motivation
Poszukiwanie nieruchomości na rynku warszawskim wymaga automatyzacji pobierania ofert nie tylko z dużych portali zdominowanych przez agencje (Otodom, OLX), ale w szczególności z serwisów skupionych na ogłoszeniach bezpośrednich od właścicieli (Adresowo, Sprzedajemy, Lento). W połączeniu z weryfikacją cen transakcyjnych z RCN Warszawa pozwala to inwestorowi/kupującemu na:
- Natychmiastowe wyłapywanie okazji bez marży pośrednika,
- Zestawianie cen ofertowych z oficjalnymi cenami transakcyjnymi z aktów notarialnych (RCN Warszawa),
- Prowadzenie historii wyników w plikach `YYYY-MM-DD-HH24MISS-oferty.md`,
- Generowanie bezstronnych rekomendacji AI i ocen potencjału negocjacyjnego.

---

## Proposed Changes

### 1. Struktura Katalogu `wyszukiwarka-nieruchomosci/`
- `kryteria.md`: Konfigurowalny plik z parametrami wyszukiwania (w tym filtr `Typ ogłoszeniodawcy: Bezpośrednio / Agencja / Dowolnie`).
- `historia/`: Katalog na wygenerowane pliki wyników w formacie `YYYY-MM-DD-HH24MISS-oferty.md`.
- `scripts/` / `src/`: Skrypty pobierające i agregujące oferty z wielu źródeł oraz pobierające statystyki/ceny transakcyjne z RCN Warszawa.

### 2. Integracja z Rozszerzoną Listą Portali Nieruchomościowych
- **Główne Portale**: Otodom.pl, OLX.pl, Morizon.pl, Nieruchomosci-online.pl.
- **Portale Bezpośrednie & Mniej Popularne Wśród Agencji**: Adresowo.pl, Sprzedajemy.pl, Lento.pl, Nethouse.pl.

### 3. Integracja z RCN Warszawa (https://mapa.um.warszawa.pl/rcn-szukaj/)
- Zbieranie danych o cenach transakcyjnych w dzielnicach Warszawy z bazy RCN.
- Porównywanie cen ofertowych wyselekcjonowanych ogłoszeń do cen transakcyjnych RCN w danej dzielnicy (wyliczanie % odchylenia).

### 4. Historia i Format Wyników (`YYYY-MM-DD-HH24MISS-oferty.md`)
Każde uruchomienie tworzy nowy plik zawierający:
- Zastosowane kryteria,
- Zestawienie dopasowanych ofert wraz z oznaczeniem źródła, typu ogłoszeniodawcy i metryk RCN,
- Sekcję **Rekomendacja AI** (Top 3 najopłacalniejsze nieruchomości, potencjał negocjacyjny vs RCN, analiza ryzyk).

---

## Non-Goals
- Wynoszenie modułu do osobnego repozytorium (zgodnie z prośbą pozostajemy w podkatalogu `wyszukiwarka-nieruchomosci/`).
- Wyszukiwanie ofert poza obszarem m.st. Warszawy.
