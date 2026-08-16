# Plan Wdrożeniowy OpenSpec (Tasks): Weryfikacja Kompletności Pobierania w Warstwie Bronze

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-brozne-completeness`  
**Data**: 2 Sierpnia 2026  
**Status**: W Trakcie Wdrożenia (In Progress)  

---

## 🏗️ Faza 1: Odczyt Liczników Ofert i Dynamiczna Paginacja Providerów

- [x] **Modyfikacja `CommercialProvider` (`src/providers/commercial.py`)**:
  - Wyciąganie `totalCount` z JSON-a Otodom (`searchAds.pagination.totalCount`).
  - Dynamiczne pobieranie kolejnych stron aż do osięgnięcia `saved_count >= totalCount`.

- [x] **Modyfikacja `AdresowoProvider` (`src/providers/adresowo.py`)**:
  - Wyciąganie liczby deklarowanych ofert ze strony `ursynow-Q/` (`re.search(r'(\d+)\s*oferty', html)`).
  - Dynamiczne pobieranie kolejnych stron (`_l1`, `_l2`, `_l3`...) aż do osiągnięcia `saved_count >= total_count`.

---

## 📊 Faza 2: Audyt Bazy Danych i Raportowanie Kompletności

- [x] **Tabela `run_audit` w `src/db.py`**:
  - Utworzenie tabeli `run_audit` rejestrującej `run_id`, `source_portal`, `expected_total`, `saved_bronze`, `completeness_pct`.

- [x] **Raportowanie Kompletności w CLI i Raportach Markdown (`report_generator.py` & `main.py`)**:
  - Wyświetlanie statystyk kompletności w konsoli podczas uruchomienia.
  - Dodanie podsumowania kompletności w nagłówku generowanego pliku raportu w `historia/`.

---

## 🧪 Faza 3: Testy i Empiryczna Weryfikacja End-to-End

- [x] **Zestaw Testów Kompletności (`tests/test_completeness.py`)**:
  - Testowanie poprawności wyliczania wskaźnika kompletności na próbkach danych.

- [x] **Uruchomienie End-to-End (`main.py`)**:
  - Weryfikacja, że Bronze zawiera 100% zadeklarowanych ofert z Otodom oraz Adresowo.pl.
