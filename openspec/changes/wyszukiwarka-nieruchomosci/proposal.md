# Proposal: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `wyszukiwarka-nieruchomosci`  
**Date**: 2026-07-26  

## Summary
Stworzenie serwisu w podkatalogu `wyszukiwarka-nieruchomosci/`, który na żądanie generuje i odświeża dokumentację aktualnych ofert nieruchomości z rynku warszawskiego, dopasowanych do kryteriów w pliku `wyszukiwarka-nieruchomosci/kryteria.md`, wzbogaconych o dane o cenach transakcyjnych z warszawskiego Rejestru Cen Nieruchomości (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/) oraz rekomendacje i analizę opłacalności AI.

---

## Motivation
Poszukiwanie nieruchomości na rynku warszawskim wymaga ręcznego sprawdzania wielu portali (Otodom, OLX, Morizon) oraz trudnego dostępu do wiedzy o rzeczywistych cenach transakcyjnych (zawieranych u notariusza, a nie cenach ofertowych). 
Wprowadzenie dedykowanego serwisu w podkatalogu `wyszukiwarka-nieruchomosci/` pozwoli na:
- Automatyczne sprawdzanie ofert na żądanie pod kątem zdefiniowanych kryteriów,
- Zestawianie cen ofertowych z oficjalnymi cenami transakcyjnymi RCN Warszawa,
- Zachowanie pełnej historii wyszukiwań w plikach z datownikiem `YYYY-MM-DD-HH24MISS-oferty.md`,
- Generowanie czytelnych rekomendacji negocjacyjnych i opłacalnościowych przez AI.

---

## Proposed Changes

### 1. Struktura Katalogu `wyszukiwarka-nieruchomosci/`
Utworzenie podkatalogu zawierającego:
- `kryteria.md`: Konfigurowalny plik z parametrami wyszukiwania (budżet, cena za m², powierzchnia, dzielnice, piętro, stan prawny).
- `historia/`: Katalog na wygenerowane pliki wyników w formacie `YYYY-MM-DD-HH24MISS-oferty.md`.
- `scripts/` / `src/`: Skrypty pobierające i agregujące oferty oraz pobierające statystyki/ceny transakcyjne z RCN Warszawa.

### 2. Integracja z Portalami Nieruchomościowymi
Wyszukiwanie ofert w oparciu o kryteria na najpopularniejszych portalach w Polsce:
- **Otodom.pl** & **OLX.pl** (priorytetowe źródła z największą bazą w Warszawie)
- **Morizon.pl** & **Nieruchomosci-online.pl** (uzupełniające źródła)

### 3. Integracja z RCN Warszawa (https://mapa.um.warszawa.pl/rcn-szukaj/)
- Zbieranie danych o cenach transakcyjnych w dzielnicach Warszawy z bazy RCN.
- Porównywanie cen ofertowych wyselekcjonowanych ogłoszeń do cen transakcyjnych RCN w danej dzielnicy/rejonie (wyliczanie % odchylenia).

### 4. Historia i Format Wyników (`YYYY-MM-DD-HH24MISS-oferty.md`)
Każde uruchomienie tworzy nowy plik zawierający:
- Zastosowane kryteria,
- Zestawienie dopasowanych ofert wraz z metrykami RCN,
- Sekcję **Rekomendacja AI** (Top 3 najopłacalniejsze nieruchomości, potencjał negocjacyjny, analiza ryzyk).

---

## Non-Goals
- Wynoszenie modułu do osobnego repozytorium (zgodnie z prośbą pozostajemy w podkatalogu `wyszukiwarka-nieruchomosci/`).
- Wyszukiwanie ofert poza obszarem m.st. Warszawy.
- Tworzenie dedykowanego interfejsu graficznego GUI.
