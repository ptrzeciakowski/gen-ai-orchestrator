# Proposal: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `wyszukiwarka-nieruchomosci`  
**Date**: 2026-07-26  

## Summary
Stworzenie serwisu w podkatalogu `wyszukiwarka-nieruchomosci/`, który na żądanie generuje i odświeża dokumentację aktualnych ofert nieruchomości z rynku warszawskiego (zarówno z portali komercyjnych, jak i serwisów z ogłoszeniami bezpośrednimi od właścicieli, np. Adresowo.pl, Sprzedajemy.pl, Lento.pl), dopasowanych do kryteriów w pliku `wyszukiwarka-nieruchomosci/kryteria.md` (z obsługą fraz odmianowych "dowolny/dowolna/dowolne"), wzbogaconych o dane o cenach transakcyjnych z warszawskiego Rejestru Cen Nieruchomości (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/) z rozkładem kwantylowym (N, P10, P25, P50, P75, P90, P95, P99), rekomendacje AI, Spis Treści (TOC) oraz **wklejenie pełnego pliku kryteriów dla zapewnienia pełnej audytowalności**.

---

## Motivation
Poszukiwanie nieruchomości na rynku warszawskim wymaga automatyzacji pobierania ofert nie tylko z dużych portali zdominowanych przez agencje (Otodom, OLX), ale w szczególności z serwisów skupionych na ogłoszeniach bezpośrednich od właścicieli (Adresowo, Sprzedajemy, Lento). W połączeniu z weryfikacją cen transakcyjnych z RCN Warszawa pozwala to inwestorowi/kupującemu na:
- Natychmiastowe wyłapywanie okazji bez marży pośrednika,
- Zestawianie cen ofertowych z oficjalnymi cenami transakcyjnymi z aktów notarialnych (RCN Warszawa) z uwzględnieniem liczby transakcji $N$, okresu i rozszerzonych centyli ($P10, P25, P50, P75, P90, P95, P99$),
- Prowadzenie historii wyników w plikach `YYYY-MM-DD-HH24MISS-oferty.md` z czytelnym formatem czasu HH:MM:SS oraz spisem treści (TOC),
- Zachowanie **pełnej audytowalności** poprzez wklejenie surowej zawartości `kryteria.md` w sekcji `## ⚙️ Kryteria Wyszukiwania`,
- Generowanie bezstronnych rekomendacji AI i ocen potencjału negocjacyjnego.

---

## Proposed Changes

### 1. Struktura Katalogu `wyszukiwarka-nieruchomosci/`
- `kryteria.md`: Konfigurowalny plik z parametrami wyszukiwania (w tym obsługa fraz odmianowych `dowolny` / `dowolna` / `dowolne` wyłączających filtr).
- `historia/`: Katalog na wygenerowane pliki wyników w formacie `YYYY-MM-DD-HH24MISS-oferty.md`.
- `src/`: Skrypty pobierające i agregujące oferty z wielu źródeł, deduplikator oraz integracja z RCN Warszawa.

### 2. Integracja z Rozszerzoną Listą Portali Nieruchomościowych
- **Główne Portale**: Otodom.pl, OLX.pl, Morizon.pl, Nieruchomosci-online.pl.
- **Portale Bezpośrednie & Mniej Popularne Wśród Agencji**: Adresowo.pl, Sprzedajemy.pl, Lento.pl, Nethouse.pl.

### 3. Integracja z RCN Warszawa (https://mapa.um.warszawa.pl/rcn-szukaj/)
- Zbieranie danych o cenach transakcyjnych w dzielnicach oraz obszarach MSI Warszawy (np. Kabaty, Natolin, Służew, Filtry) z bazy RCN.
- Prezentowanie wskaźników na samym końcu raportu: Okres danych, Liczba transakcji $N$, Średnia, $P10, P25, P50, P75, P90, P95, P99$.

### 4. Audytowalność i Format Wyników (`YYYY-MM-DD-HH24MISS-oferty.md`)
Każde uruchomienie tworzy nowy plik zawierający:
- Nagłówek z czasem HH:MM:SS oraz czytelną listą metadanych,
- **Spis Treści (Table of Contents)** z linkami do rozdziałów,
- Sekcję `## ⚙️ Kryteria Wyszukiwania` z bezpośrednim wklejeniem pliku `kryteria.md`,
- Tabelę wyselekcjonowanych ofert rynkowych,
- Sekcję Rekomendacji AI,
- Sekcję Rozkładu Cen Transakcyjnych RCN na samym końcu dokumentu.
