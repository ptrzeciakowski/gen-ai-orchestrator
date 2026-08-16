# OpenSpec Design: Wielopoziomowa Inteligentna Deduplikacja Ofert (Enhanced Multi-Level Deduplication)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-enhanced-deduplication`  
**Data**: 16 Sierpnia 2026  
**Status**: Projekt Techniczny (Design)  
**Dokumenty Wejściowe**:
- [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-enhanced-deduplication/proposal.md)
- [db.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
- [deduplicator.py](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/deduplicator.py)

---

## 1. Cel i Zakres Architektury (Context & Goals)

Celem zmiany jest eliminacja duplikatów ofert występujących równolegle w wielu portalach (`Otodom`, `Adresowo`, `Gratka`, `Morizon`, `Nieruchomosci-online`, `OLX`) poprzez wdrożenie 3-poziomowego kaskadowego algorytmu fingerprintingu oraz zaawansowanej konsolidacji cech lokalu w warstwie Gold.

### Główne cele:
1. **Walidacja współrzędnych GPS (Bounding Box Polski)**: Eliminacja błędnych koordynatów (np. Gratka `lat=187, lon=188`) poprzez ograniczenie `lat BETWEEN 49.0 AND 55.0` oraz `lon BETWEEN 14.0 AND 25.0`.
2. **Ekstrakcja i normalizacja ulicy (`street_slug`)**: Wyciąganie i slugifikacja nazwy ulicy z obiektów adresowych Schema.org (`place_ld.address.streetAddress`), `location.address.street.name`, JSON-LD oraz tytułów ogłoszeń.
3. **Kaskadowy Fingerprinting (3 poziomy)**:
   - **Poziom 1 (Ulica + Metraż + Pokoje + Zaokrąglona Cena)**: Gdy nazwa ulicy jest dostępna.
   - **Poziom 2 (GPS + Metraż + Pokoje)**: Gdy współrzędne GPS są prawidłowe.
   - **Poziom 3 (Dzielnica + Metraż + Pokoje + Zaokrąglona Cena)**: Fallback przy braku ulicy i GPS.
4. **Inteligentna Konsolidacja w Gold**:
   - Wybór najpełniejszych danych: `MAX(floor)` (odporność na brak piętra `NULL`), `MAX(build_year)`, `MAX(has_elevator)`, `MIN(price_pln)`.
   - Zachowanie listy wszystkich portali źródłowych (`GROUP_CONCAT(source_portal || ':' || external_id)`).
5. **Kompleksowe testy regresyjne**: Zapewnienie testów scalania asymetrycznych ofert (GPS vs brak GPS, floor vs brak floor, drobne różnice cenowe).

---

## 2. Architektura i Przepływ Danych (System Architecture & Flow)

```
                            [bronze_listings: raw_payload]
                                          │
                                          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ Warstwa Silver (silver_listings)                                            │
│ ├─ Bounding box GPS: lat IN [49..55], lon IN [14..25] -> valid_lat/lon      │
│ ├─ extract_street(title, raw_payload) -> street_slug (np. benedykta-polaka) │
│ └─ Normalizacja podstawowa: price_pln, area_m2, rooms, floor, build_year    │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ Warstwa Gold (gold_listings) - Kaskadowy Fingerprint                        │
│ ├─ IF street_slug:  'street_' || district || '_' || street || '_' || ...    │
│ ├─ ELIF valid_gps:  'gps_' || lat || '_' || lon || '_' || area || '_' || ... │
│ └─ ELSE:            'dist_' || district || '_' || area || '_' || rooms ...  │
│ ───► GROUP BY dedup_fingerprint, run_id                                     │
│      MAX(floor), MAX(build_year), MAX(has_elevator), MIN(price_pln)         │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│ Deduplicator & ReportGenerator                                              │
│ 1 unikalny rekord z kompletem danych i linkami do wszystkich źródeł         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Kontrakty Schematów i Zapytań SQL

### 3.1. Rejestracja funkcji pomocniczej `extract_street`:
Funkcja Python zarejestrowana w silniku SQLite:
```python
def extract_street_clean(title, payload_str):
    # Ekstrakcja z JSON-LD, address, reverseGeocoding oraz regexu z tytułu
    # Zwraca znormalizowany slug, np. 'benedykta-polaka', 'hawajska', 'dereniowa'
```

### 3.2. Widok `silver_listings`:
```sql
CASE 
    WHEN CAST(COALESCE(...) AS REAL) BETWEEN 49.0 AND 55.0 
    THEN CAST(COALESCE(...) AS REAL) 
    ELSE NULL 
END AS lat,

CASE 
    WHEN CAST(COALESCE(...) AS REAL) BETWEEN 14.0 AND 25.0 
    THEN CAST(COALESCE(...) AS REAL) 
    ELSE NULL 
END AS lon,

extract_street(title, raw_payload) AS street_slug
```

### 3.3. Widok `gold_listings`:
```sql
COALESCE(
    CASE 
        WHEN street_slug IS NOT NULL AND street_slug != '' AND area_m2 IS NOT NULL AND rooms IS NOT NULL AND price_pln IS NOT NULL
        THEN 'street_' || LOWER(COALESCE(district, '')) || '_' || street_slug || '_' || ROUND(area_m2, 0) || '_' || rooms || '_' || CAST(ROUND(price_pln / 1000.0) AS INT)
        WHEN lat IS NOT NULL AND lon IS NOT NULL AND area_m2 IS NOT NULL AND rooms IS NOT NULL
        THEN 'gps_' || ROUND(lat, 3) || '_' || ROUND(lon, 3) || '_' || ROUND(area_m2, 0) || '_' || rooms
        WHEN district IS NOT NULL AND area_m2 IS NOT NULL AND rooms IS NOT NULL AND price_pln IS NOT NULL
        THEN 'dist_' || LOWER(district) || '_' || ROUND(area_m2, 0) || '_' || rooms || '_' || CAST(ROUND(price_pln / 1000.0) AS INT)
        ELSE NULL
    END,
    'raw_' || bronze_id
) AS dedup_fingerprint
```

---

## 4. Wybory Architektoniczne i Trade-offy (Architectural Trade-offs)

1. **Ulica jako priorytet przed GPS**:
   - *Dlaczego*: Portale często geokodują ogłoszenia losowo w promieniu 500m od centrum dzielnicy lub podają koordynaty z błędem, natomiast nazwa ulicy w opisie/tytule jest ściśle wprowadzana przez właściciela/agenta.
   - *Zaokrąglenie ceny*: `ROUND(price_pln / 1000.0)` eliminuje sztuczne rozbieżności 1 zł (np. `999 999 zł` vs `1 000 000 zł`).
2. **Konsolidacja `MAX(floor)`**:
   - Gdy jeden portal podaje `floor = 1`, a inny `floor = NULL`, w rekordzie wynikowym zachowane zostaje piętro `1`, co zapobiega odrzuceniu oferty przy włączonym filtrze `Wyklucz parter: Tak`.

---

## 5. Obsługa Sytuacji Awaryjnych i Krawędziowych (Edge Cases)

1. **Wiele mieszkań o tym samym metrażu w jednym bloku**:
   - Różne piętra (np. piętro 1 vs piętro 8) o różnej cenie otrzymają różne klucze, jeśli cena różni się powyżej 1000 zł lub brak ulicy.
2. **Brak danych o ulicy i koordynatach**:
   - Bezpieczny fallback do `dist_` (Dzielnica + Metraż + Pokoje + Cena).
