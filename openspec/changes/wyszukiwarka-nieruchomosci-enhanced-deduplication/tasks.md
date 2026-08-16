# Plan Wdrożeniowy: Wielopoziomowa Inteligentna Deduplikacja Ofert

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-enhanced-deduplication`  
**Status**: Ukończony (Completed)  

---

## 📋 Lista Zadań (Tasks)

### Faza 1: Rozszerzenie Warstwy Danych SQLite (`src/db.py`)
- [x] **Zadanie 1.1**: Rejestracja funkcji pomocniczej `extract_street` w połączeniach SQLite w `DatabaseManager`.
- [x] **Zadanie 1.2**: Wdrożenie walidacji współrzędnych geograficznych (Bounding Box Polski) w widoku `silver_listings`.
- [x] **Zadanie 1.3**: Dodanie kolumny `street_slug` w widoku `silver_listings`.
- [x] **Zadanie 1.4**: Wdrożenie 3-poziomowego kaskadowego algorytmu `dedup_fingerprint` oraz konsolidacji `MAX(floor)`, `MAX(build_year)`, `MIN(price_pln)` w widoku `gold_listings`.

### Faza 2: Testy Jednostkowe i Regresyjne
- [x] **Zadanie 2.1**: Utworzenie pliku testowego `tests/test_enhanced_deduplication.py` weryfikującego:
  - Scalenie przypadku Benedykta Polaka (Gratka ID: 48425285 + Adresowo).
  - Odrzucanie nieprawidłowych współrzędnych GPS (np. 187.0, 188.0).
  - Tolerancję braku piętra (`floor=1` vs `floor=NULL`).
  - Niezależność różnych mieszkań w tym samym bloku (różna cena / cechy).
- [x] **Zadanie 2.2**: Uruchomienie pełnego pakietu testów jednostkowych (`python3 -m unittest discover tests`) i weryfikacja braku regresji (50/50 testów OK).
- [x] **Zadanie 2.3**: Weryfikacja działania CLI `--cache` i potwierdzenie braku zduplikowanych ofert w generowanym raporcie.
