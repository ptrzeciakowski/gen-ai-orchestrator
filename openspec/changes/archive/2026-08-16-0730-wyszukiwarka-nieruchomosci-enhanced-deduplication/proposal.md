# OpenSpec Proposal: Wielopoziomowa Inteligentna Deduplikacja Ofert (Enhanced Multi-Level Deduplication)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-enhanced-deduplication`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/deduplicator.py`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

W wygenerowanym raporcie wykryto przypadek niescalonych duplikatów tej samej nieruchomości wystawionej w dwóch różnych serwisach:
- **Gratka.pl**: `Mieszkanie na sprzedaż, 59 m² Ursynów, Benedykta Polaka` | 59.0 m² | 3 pok. | 999 999 zł | ID: `48425285`
- **Adresowo.pl**: `Warszawa Ursynów, ul. Benedykta Polaka Mieszkanie - 3 pokoje - 59 m² - 1 piętro` | 59.0 m² | 3 pok. | 999 999 zł | ID: `...-benedykta-polaka-3-pokojowe-x7w7g8`

### 🔍 Przyczyny niescalenia w obecnym algorytmie:
1. **Nieprawidłowe współrzędne GPS w niektórych serwisach**: Gratka przekazała wartości pikselowe/wewnętrzne `lat: 187.0, lon: 188.0` zamiast współrzędnych geograficznych Polski (`52.148, 21.051`), co uniemożliwiło dopasowanie po GPS.
2. **Brak piętra w jednym ze źródeł**: Adresowo posiadało `floor: 1`, natomiast Gratka miała `floor: NULL`. Fallback fingerprint `district_area_rooms_floor_price` wygenerował dwa różne klucze (`Ursynów_59.0_3__999999` vs `Ursynów_59.0_3_1_999999`).
3. **Brak normalizacji nazwy ulicy**: Klucz deduplikacji pomijał znormalizowaną nazwę ulicy (`benedykta-polaka`), która była jednoznacznie obecna w obu ofertach.

---

## 2. Architektura Usprawnionej Deduplikacji (Target Architecture)

Wdrożenie **3-poziomowego kaskadowego algorytmu fingerprintingu** w widoku `silver_listings` / `gold_listings` oraz module `Deduplicator`:

```
                                [Surowy Rekord Silver]
                                          │
    ┌─────────────────────────────────────┼─────────────────────────────────────┐
    ▼                                     ▼                                     ▼
[Poziom 1: Prawidłowy GPS]    [Poziom 2: Ulica + Metraż + Cena]    [Poziom 3: Dzielnica + Cechy]
lat: 49..55, lon: 14..25      street_slug + area + rooms + price    district + area + rooms + price
(tolerancja 100m + 0.5m²)     (np. benedykta-polaka_59.0_3_999999)  (tolerancja floor IS NULL)
```

### 🧭 Kluczowe Założenia Techniczne:
1. **Walidacja Współrzędnych GPS (Bounding Box Polski)**:
   - Koordynaty są uznawane za ważne tylko gdy `lat BETWEEN 49.0 AND 55.0` oraz `lon BETWEEN 14.0 AND 25.0`. Wszelkie wartości spoza tego zakresu są traktowane jako `NULL`.
2. **Ekstrakcja i Normalizacja Ulicy (`street_slug`)**:
   - Wyciąganie ulicy z dedykowanych pól adresowych lub regexu z tytułu (`ul. Benedykta Polaka` -> `benedykta-polaka`, `al. KEN` -> `ken`).
3. **Tolerancja Piętra w Fallbacku (`NULL-safe Floor Tolerance`)**:
   - Jeśli jedna oferta ma `floor = 1`, a druga `floor IS NULL`, a pozostałe parametry (ulica/dzielnica, metraż ±0.5 m², liczba pokoi, cena ±2%) są identyczne – rekordy zostają połączone.
4. **Agregacja Metadanych w Gold**:
   - Scalony rekord przyjmuje najdokładniejsze dane z obu źródeł (np. `floor=1` z Adresowo, a dodatkowe zdjęcia/opis z Gratki).

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Walidacja GPS w `silver_listings` (`src/db.py`)**: Odrzucanie współrzędnych spoza terytorium Polski.
- [ ] **Kolumna `street_slug` w `silver_listings` (`src/db.py`)**: Normalizacja nazw ulic z JSON-LD i tytułów ogłoszeń.
- [ ] **Wielopoziomowy `dedup_fingerprint` w `gold_listings` (`src/db.py`)**: Kaskadowe reguły (GPS -> Ulica + Parametry -> Dzielnica + Parametry).
- [ ] **Konsolidacja Danych w `Deduplicator` (`src/deduplicator.py`)**: Uzupełnianie brakujących pól (`floor`, `build_year`, `total_floors`) z innych wystąpień scalonego ogłoszenia.
- [ ] **Testy Regresji Deduplikacji (`tests/test_enhanced_deduplication.py`)**:
  - Test scalenia oferty Gratka (ID 48425285) z Adresowo (ul. Benedykta Polaka).
  - Test odporności na nieprawidłowe GPS (`lat: 187, lon: 188`).
  - Test scalania ofert, z których jedna ma `floor=NULL`, a druga `floor=1`.
  - Test zapobiegania fałszywym połączeniom różnych mieszkań w tym samym bloku (np. 1 piętro vs 8 piętro).

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🎯 **Zero widocznych duplikatów w raporcie**: Identyczne lokale wystawione w wielu portalach będą zawsze prezentowane jako 1 rekord z listą wszystkich linków źródłowych.
* 📈 **Większa kompletność danych**: Jeśli jeden portal nie podał piętra lub roku budowy, a drugi podał – raport w Gold będzie kompletny.
* ⚡ **Bezstratność w warstwie Bronze**: Wszystkie surowe dane pozostają nienaruszone w `bronze_listings`.
