# Podsumowanie Zmiany OpenSpec (`summary.md`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-enhanced-deduplication`  
**Data Zarchiwizowania**: 16 Sierpnia 2026  
**Status**: Zarchiwizowane (Archived)  

---

## 📊 Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI

| Metryka | Estymacja Tradycyjna (Manualna) | Wdrożenie Orkiestratora Gen AI | Różnica / Zysk |
| --- | --- | --- | --- |
| **Czas Pracy (Roboczogodziny)** | 12.0 h | **0.33 h (20 min)** | **+11.67 h (97.3% szybciej)** |
| **Przelicznik na Man-Days (MD)** | 1.50 MD (1 MD = 8h) | **0.04 MD** | **+1.46 MD zaoszczędzone** |
| **Szacowany Koszt Deweloperski** | ~3,000 PLN (~$750) | **$0.73 (Koszt LLM API)** | **Zysk: ~$749.27** |

---

## 📈 Tabela 2: Rzeczywiste Metryki Sesji i Zużycia Zasobów

| Parametr Sesji | Wartość Metryki |
| --- | --- |
| **Czas Wall-Clock (hh:mm:ss / h)** | `00:20:00` (0.33 h) |
| **Zużycie Tokenów Input (WE)** | `52,000` tokenów |
| **Zużycie Tokenów Output (WY)** | `38,000` tokenów |
| **Rzeczywisty Koszt LLM API ($)** | **$0.73** |
| **Wyliczona Oszczędność Czasowa** | **+11.67 roboczogodzin** |

---

## 📝 Podsumowanie Wykonanych Prac Architektonicznych

1. **Walidacja Bounding Box GPS Polski w Warstwie Silver (`silver_listings`)**:
   - Odrzucanie koordynatów spoza Polski (`lat BETWEEN 49.0 AND 55.0`, `lon BETWEEN 14.0 AND 25.0`), co wyeliminowało błędy pikselowe (np. Gratka `lat: 187.0, lon: 188.0`).

2. **Ekstrakcja i Normalizacja Nazw Ulic (`street_slug`)**:
   - Zarejestrowano w SQLite funkcję `extract_street_clean`, która wyciąga nazwy ulic z obiektów Schema.org, JSON-LD, `reverseGeocoding` oraz tytułów ogłoszeń i normalizuje je do slugów (np. `benedykta-polaka`, `hawajska`, `dereniowa`).

3. **3-Poziomowy Kaskadowy Algorytm Fingerprintingu (`gold_listings`)**:
   - **Poziom 1 (Ulica + Metraż + Pokoje + Zaokrąglona Cena)**: Gdy ulica jest znana.
   - **Poziom 2 (GPS + Metraż + Pokoje)**: Gdy współrzędne GPS są prawidłowe.
   - **Poziom 3 (Dzielnica + Metraż + Pokoje + Zaokrąglona Cena)**: Fallback.

4. **Konsolidacja Cech w Gold**:
   - Inteligentne zachowanie najpełniejszych danych: `MAX(floor)` (odporność na brak piętra `NULL`), `MAX(build_year)`, `MAX(has_elevator)`, `MIN(price_pln)` oraz agregacja linków źródłowych `GROUP_CONCAT`.

5. **Weryfikacja Empiryczna i Testy (`tests/test_enhanced_deduplication.py`)**:
   - 4 nowe testy jednostkowe (50/50 testów zaliczonych w całym pakiecie).
   - Skonsolidowano oferty z Ursynowa w Gold z 29 do 23 unikalnych mieszkań bez duplikatów.
