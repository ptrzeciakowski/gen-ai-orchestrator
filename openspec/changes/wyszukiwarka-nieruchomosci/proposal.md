# Proposal: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `wyszukiwarka-nieruchomosci`  
**Date**: 2026-07-26  

## Summary
Stworzenie serwisu w podkatalogu `wyszukiwarka-nieruchomosci/`, który na żądanie generuje i odświeża dokumentację aktualnych ofert nieruchomości z rynku warszawskiego (zarówno z portali komercyjnych, jak i bezpośrednich od właścicieli), dopasowanych do kryteriów w pliku `wyszukiwarka-nieruchomosci/kryteria.md`, wzbogaconych o dane o cenach transakcyjnych z Rejestru Cen Nieruchomości (RCN - https://mapa.um.warszawa.pl/rcn-szukaj/) w tym rozkład kwantylowy (P10, P25, P50, P75, P90), rekomendacje AI oraz **rejestrację faktycznie zastosowanych kryteriów wyszukiwania dla zapewnienia pełnej audytowalności**.

---

## Proposed Changes

1. **Struktura Katalogu**: `wyszukiwarka-nieruchomosci/` (`kryteria.md`, `historia/YYYY-MM-DD-HH24MISS-oferty.md`, `src/`).
2. **Pełna Audytowalność Raportu**: Każdy plik raportowy w sekcji `## ⚙️ Faktycznie Zastosowane Kryteria Wyszukiwania` rejestruje ścisły odczyt użytych parametrów z `kryteria.md` (odrzucono ogólne domyślne hasła).
3. **Statystyki RCN Warszawa**: Pełny rozkład kwantylowy per dzielnica i obszar MSI (N, Średnia, P10, P25, Mediana P50, P75, P90).
4. **Rekomendacje i Rekordy**: Prawdziwe, sprawne linki ogłoszeń rynkowych i porady negocjacyjne AI.
