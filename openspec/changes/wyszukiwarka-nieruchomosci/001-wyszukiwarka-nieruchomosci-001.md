# Exploratory Record: Wyszukiwarka Nieruchomości Warszawa & RCN Integracja

**ID**: `001-wyszukiwarka-nieruchomosci-001`  
**Date**: 2026-07-26  
**Topic**: Serwis generowania i odświeżania na żądanie ofert nieruchomości w Warszawie z integracją danych transakcyjnych RCN, 5-kwantylową analizą rynkową oraz rejestrowaniem faktycznie zastosowanych kryteriów dla pełnej audytowalności.

---

## 1. Zakres Eksploracji

Eksploracja obejmuje przygotowanie serwisu `wyszukiwarka-nieruchomosci/`:
1. Odczyt i parsowanie **faktycznie zastosowanych kryteriów wyszukiwania** z pliku `wyszukiwarka-nieruchomosci/kryteria.md` z dołączeniem ich pełnego zapisu w raporcie dla zachowania pełnej audytowalności.
2. Agregację ogłoszeń z serwisów komercyjnych oraz serwisów z przewagą ofert bezpośrednich od właścicieli (Adresowo, Sprzedajemy, Lento).
3. Integrację z bazą RCN Warszawa (`https://mapa.um.warszawa.pl/rcn-szukaj/`) z rozbiciem na dzielnice i obszary MSI oraz 5-elementowym rozkładem kwantylowym ($N$, Średnia, P10, P25, P50-mediana, P75, P90).
4. Generowanie raportów historii `YYYY-MM-DD-HH24MISS-oferty.md` z sekcją rekomendacji AI.

---

## 2. Zastosowane Rozwiązania i Pełna Audytowalność

- **Sekcja Kryteriów**: Zamiast uśrednionych haseł, raport wyjściowy prezentuje nagłówek `## ⚙️ Faktycznie Zastosowane Kryteria Wyszukiwania` wraz z podaniem ścieżki pliku źródłowego, faktycznie przyjętych cen min/max, ceny m², metrażu i dzielnic.
- **RCN Statystyki**: 5-kwantylowy rozkład transakcyjny (P10, P25, P50, P75, P90) pozwalający precyzyjnie porównać ofertę rynkową z rynkiem notarialnym.
