# OpenSpec Proposal: Weryfikacja Kompletności Pobierania w Warstwie Bronze (`wyszukiwarka-nieruchomosci-brozne-completeness`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-brozne-completeness`  
**Data**: 2 Sierpnia 2026  
**Status**: Propozycja (Proposal)  

---

## 1. Problem Statement

Obecny mechanizm pobierania bazuje na sztywnej liczbie stron (`max_pages`). Rodziło to dwa ryzyka:
1. **Ryzyko pobrania tylko części bazy**: Na portalach o większej liczbie ogłoszeń (np. 133 na Adresowo dla Ursynowa) sztywny limit 2 stron powodował pomijanie pozostałych stron.
2. **Brak audytowalnego dowodu kompletności**: System nie sprawdzał i nie raportował, czy pobrane oferty stanowią 100% bazy ogłoszeń dostępnych na danym portalu w danym uruchomieniu.

---

## 2. Proposed Solution

1. **Odczyt Deklarowanej Liczby Ofert z Portalu**:
   - **Adresowo.pl**: Ekstrakcja z tekstu/badge'a strony `ursynow-Q/` (np. `"133 oferty"`).
   - **Otodom.pl**: Ekstrakcja z pola `totalCount` w surowym obiekcie JSON `__NEXT_DATA__`.
2. **Dynamiczne Paginowanie**:
   - Kontynuowanie pobierania do momentu zgromadzenia 100% ogłoszeń w tabeli Bronze.
3. **Raportowanie Wskaźnika Kompletności (Completeness Ratio)**:
   - Wyświetlanie jasnych podsumowań w CLI oraz w nagłówku pliku Markdown:
     `Otodom: 126/126 (100.0%)`, `Adresowo: 133/133 (100.0%)`.
