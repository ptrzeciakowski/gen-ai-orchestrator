# Exploratory Record: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

**ID**: `001-wyszukiwarka-nieruchomosci-001`  
**Date**: 2026-07-26  
**Topic**: Serwis generowania i odświeżania na żądanie ofert nieruchomości w Warszawie z integracją danych transakcyjnych RCN, rozszerzoną analizą kwantylową (N, P10, P25, P50, P75, P90, P95, P99) per dzielnice i obszary MSI, obsługą słów kluczowych odmianowych ("dowolny", "dowolna", "dowolne") dla zwalniania filtrów, spisem treści (TOC) oraz wklejaniem surowej treści pliku kryteriów dla pełnej audytowalności.

---

## 1. Cel Eksploracji

Zbadanie i określenie architektury serwisu `wyszukiwarka-nieruchomosci/` (lokalizowanego w podkatalogu bieżącego repozytorium), którego zadaniem jest:
1. Odczyt i parsowanie parametrów z pliku `wyszukiwarka-nieruchomosci/kryteria.md` z obsługą słów kluczowych odmianowych ("dowolny", "dowolna", "dowolne", "brak limitu") skutkujących wyłączeniem ograniczenia filtrującego oraz z wklejaniem surowej treści tego pliku do raportu w sekcji `## ⚙️ Kryteria Wyszukiwania`.
2. Agregację ogłoszeń z serwisów komercyjnych oraz serwisów z przewagą ofert bezpośrednich od właścicieli (Adresowo, Sprzedajemy, Lento).
3. Integrację z bazą RCN Warszawa (`https://mapa.um.warszawa.pl/rcn-szukaj/`) z rozbiciem na dzielnice i obszary MSI oraz 7-elementowym rozkładem kwantylowym ($N$, Średnia, P10, P25, P50-mediana, P75, P90, P95, P99) umieszczanym na samym końcu dokumentu.
4. Generowanie raportów historii `YYYY-MM-DD-HH24MISS-oferty.md` ze spisem treści (Table of Contents), czytelnym czasem HH:MM:SS i sekcją rekomendacji AI.

---

## 2. Rozszerzony Układ Raportu (`YYYY-MM-DD-HH24MISS-oferty.md`)

- **Czytelny Czas**: Datownik w nagłówku w formacie `YYYY-MM-DD HH:MM:SS`.
- **Wypunktowane Metadane**: Czytelna lista metadanych generowania na początku pliku.
- **📌 Spis Treści (TOC)**: Klikalne odnośniki wewnątrz-dokumentowe na początku raportu.
- **⚙️ Kryteria Wyszukiwania**: Bezpośrednie wklejenie surowego kodu pliku `kryteria.md`.
- **🏠 Wyselekcjonowane Oferty Rynkowe**: Tabela ofert z klikalnymi aktywnymi adresami URL.
- **💡 Rekomendacje & Analiza Opłacalności AI**: Rekomendacja Top 3 i checklisty.
- **📊 Rozkład Cen Transakcyjnych RCN Warszawa**: Na samym końcu dokumentu z centylami $P10, P25, P50, P75, P90, P95, P99$.
