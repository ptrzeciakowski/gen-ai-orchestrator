# Peer Review Architektoniczny: Integracja Nieruchomosci-online.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-nieruchomosci-online`  
**Recenzent**: Architekt Oprogramowania (Autor projektu `wyszukiwarka-nieruchomosci-morizon`)  
**Data Recenzji**: 15 Sierpnia 2026  
**Dokument Recenzowany**: [`design_initial.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-nieruchomosci-online/design_initial.md)  
**Standard Oceny**: [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md) & Architektura ELT

---

## 🧐 Recenzja Architektoniczna: Architekt Morizon

### 1. Ogólna Ocena Jakości Projektu
Projekt techniczny integracji portalu Nieruchomosci-online.pl charakteryzuje się wzorową czystością architektoniczną. Wybór dwufazowej strategii scrapingu (List + Detail) jest w 100% spójny z podejściem zastosowanym w `AdresowoProvider` oraz `MorizonProvider`, co gwarantuje najwyższą jakość danych atrybutowych i geolokalizacyjnych.

Szczególnie na pochwałę zasługuje podejście do standaryzacji schematu `raw_payload`, które minimalizuje konieczność inwazyjnych zmian w istniejącym kodzie bazy danych [`src/db.py`](file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/src/db.py).

---

### 2. Szczegółowa Ocena w Wymiarach Architektonicznych

#### 2.1. Spójność z Architekturą ELT i Modyfikacje `db.py`
* **Mocne strony**:
  - Projektant słusznie zauważył (sekcja 4.2), że wystarczy ujednolicić klucze obiektu `raw_payload` po stronie providera Pythona, aby istniejący widok `silver_listings` bez żadnych modyfikacji obsłużył nowego providera.
  - Zastosowanie struktury:
    ```json
    "price_pln": ..., "area_m2": ..., "rooms": ..., "floor": ..., "has_elevator": ..., "location": {"coordinates": {"latitude": ..., "longitude": ...}}
    ```
    jest wzorcowym podejściem eliminującym dług technologiczny w SQL.

#### 2.2. Poprawność Mapowania Kryteriów Biznesowych (`kryteria.md`)
* **Mocne strony**:
  - Poprawne rozdzielenie filtrów zgrubnych (URL: cena, pokoje, lokalizacja) od filtrów restrykcyjnych w warstwie Gold (winda, piętra, wykluczenie parteru).
  - Wychwycenie rzadkich przypadków brzegowych, takich jak waluty obce (EUR/USD) i mapowanie niestandardowych określeń kondygnacji ("Wysoki parter" -> 0).
* **Zidentyfikowane ryzyko architektoniczne (Positional URL Query)**:
  - Format pozycyjny `szukaj.html?3,mieszkanie,sprzedaz,rynek-wtorny,warszawa:ursynow,1000000-1050000,,3-3&p=1` jest wysoce wrażliwy na liczbę i kolejność przecinków.
  - Jeśli portal zmieni kolejność slotów lub doda nowy filtr (np. rodzaj budynku) między metrażem a pokojami, zapytanie zwróci 0 wyników bez błędu HTTP.
  - *Rekomendacja*: Metoda `build_search_url()` musi być pokryta precyzyjnymi testami jednostkowymi weryfikującymi dokładną pozycję każdego parametru przy różnych kombinacjach kryteriów (np. pusty metraż, brak określonego rynku).

#### 2.3. Odporność na Błędy, Antybot i Audyt Kompletności (`run_audit`)
* **Mocne strony**:
  - Sekwencyjne odpytywanie z bezpiecznym odstępem czasowym `0.2 - 0.5s` oraz pełnym zestawem nagłówków Chromium macOS.
  - Zdefiniowanie strategii Exponential Backoff na kody HTTP 429 i 403.
  - Graceful degradation – błąd pojedynczego ogłoszenia nie zatrzymuje przetwarzania pozostałych ofert ani pracy innych providerów.
* **Uwaga do audytu kompletności**:
  - Wyszukiwanie może obejmować wiele dzielnic (`config.districts = ["Ursynów", "Mokotów"]`). Należy upewnić się, że `expected_total` jest sumowane dla wszystkich iterowanych dzielnic przed finalnym wywołaniem `save_run_audit` dla providera `nieruchomosci_online`.

#### 2.4. Deduplikacja Międzyportalowa (`gold_listings`)
* **Mocne strony**:
  - Dzięki pobieraniu podstron ofert i wyciąganiu danych GPS z JSON-LD (`Place.geo`) lub skryptów mapy, oferty z Nieruchomosci-online będą bezproblemowo łączone w widoku `gold_listings` po pierwszym członie fingerprinta:
    $$\text{ROUND}(lat, 3) \mathbin{\Vert} \text{ROUND}(lon, 3) \mathbin{\Vert} \text{ROUND}(area\_m2, 1) \mathbin{\Vert} rooms$$
  - W przypadku braku koordynatów, przygotowany fallback na `district_area_rooms_floor_price` zapewnia ciągłość deduplikacji.

---

### 3. Rekomendacje Usprawnień
1. **Defensywna konstrukcja URL**: Zaimplementować walidator liczby segmentów w generowanym adresie URL przed wysłaniem żądania HTTP.
2. **Słownik synonimów windy**: Rozszerzyć regex detekcji windy w opisie o frazy branżowe: `(?i)(winda|windą|windy|dźwig osobowy|cichobieżna)`.
3. **Akumulacja metryk audytowych**: Zapewnić sumowanie `expected_total` przy wielu dzielnicach w pojedynczym `run_id`.

---
*Status Recenzji: **Zatwierdzony bez zastrzeżeń blokujących (Pełna rekomendacja do wdrożenia).***
