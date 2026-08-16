# Peer Review Architektoniczny: Integracja Gratka.pl

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-gratka`  
**Recenzent**: Architekt Oprogramowania (Autor projektu `wyszukiwarka-nieruchomosci-morizon`)  
**Data Recenzji**: 15 Sierpnia 2026  
**Dokument Recenzowany**: [`design_initial.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-gratka/design_initial.md)  
**Standard Oceny**: [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md) & Architektura ELT

---

## 🧐 Recenzja Architektoniczna: Architekt Morizon

### 1. Ogólna Ocena Jakości Projektu
Projekt techniczny integracji serwisu Gratka.pl prezentuje wysoki poziom dojrzałości inżynierskiej, precyzyjnie definiuje przepływ ELT (Bronze -> Silver -> Gold) oraz poprawnie identyfikuje parametry filtrowania serwisu.

Ze względu na fakt, że portale **Gratka.pl** oraz **Morizon.pl** należą do tej samej grupy kapitałowej (Gratka-Morizon), oba serwisy wykazują częściowe pokrewieństwo domenowe, a wzajemna spójność modeli danych ma kluczowe znaczenie dla deduplikacji międzyserwisowej.

---

### 2. Szczegółowa Ocena w Wymiarach Architektonicznych

#### 2.1. Spójność z Architekturą ELT i Modyfikacje `db.py` (`silver_listings`)
* **Mocne strony**:
  - Zachowanie bezstratnej warstwy Bronze i wykorzystanie funkcji JSON1 SQLite w widoku `silver_listings`.
  - Uwzględnienie specyficznych ścieżek JSON Gratki (`features.winda`, `floorsInBuilding`, `offer_ld.price`).
* **Zidentyfikowana słabość architektoniczna**:
  - W sekcji 4.2 zaproponowano warunek:
    `WHEN b.source_portal = 'gratka' THEN 'https://gratka.pl/nieruchomosci/ob/' || b.external_id`
    Oraz rozbudowane gałęzie `COALESCE` per portal.
  - *Rekomendacja architektoniczna*: Im więcej providerów dodajemy (Otodom, Adresowo, Morizon, Gratka, OLX, Nieruchomości-online), tym bardziej widok `silver_listings` staje się przeciążony i podatny na regresje. Lepszą praktyką jest **standaryzacja kontraktu `raw_payload` na poziomie providera** (zapisywanie znormalizowanych kluczy `url`, `price_pln`, `area_m2`, `rooms`, `floor`, `has_elevator` bezpośrednio w korzeniu słownika JSON). Widok `silver_listings` powinien w pierwszej kolejności odczytywać pola generyczne, a ścieżki specyficzne traktować jako fallback.

#### 2.2. Poprawność Mapowania Kryteriów Biznesowych (`kryteria.md`)
* **Mocne strony**:
  - Prawidłowe przeniesienie rygorystycznych filtrów biznesowych (winda, wykluczenie parteru, piętra 1–8) do warstwy SQL (`gold_listings` / `Deduplicator`).
  - Użycie parametrów dwukropkowych `cena-calkowita:min`, `liczba-pokoi:min`, `powierzchnia-w-m2:min`.
* **Uwaga krytyczna**:
  - Parametr rynku (`&rynek=wtorny` / `/wtorny`) został oznaczony jako `[Hipoteza/Domysł]`. Ponieważ domyślne kryteria w `kryteria.md` wskazują `Rynek: Dowolny`, provider Gratka nie powinien wymuszać zawężenia rynku na poziomie URL, aby nie odrzucić ofert z rynku pierwotnego.

#### 2.3. Analiza Wyboru Wariantu Crawlera (Opcja 3 vs Opcja 1)
* **Zastrzeżenie do Opcji 3 (Hybrydowej: lista + selektywne dociąganie szczegółów)**:
  - W Opcji 3 zaproponowano pobieranie podstrony oferty tylko wtedy, gdy na liście brakuje piętra lub windy.
  - *Ryzyko*: Kafelki na liście wyników Gratki rzadko zawierają dokładne współrzędne geograficzne GPS (`geo.latitude`, `geo.longitude`). Jeśli ogłoszenie z listy posiada informację o windzie w krótkim opisie, ale nie posiada współrzędnych GPS, crawler w Opcji 3 **nie pobierze** podstrony szczegółowej. W efekcie rekord trafi do Bronze bez współrzędnych GPS.
  - *Konsekwencja w Gold*: Rekord bez GPS nie zmatchuje się w widoku `gold_listings` po pierwszym członie `dedup_fingerprint` (koordynaty GPS), co obniży skuteczność deduplikacji z ofertami z Otodom i Morizona!
  - *Rekomendacja*: Rekomenduję rozważenie **Wariantu 1 (Scraper Dwuetapowy dla wszystkich ofert)**, analogicznie jak w `AdresowoProvider` i `MorizonProvider`, co gwarantuje 100% kompletność koordynatów GPS i atrybutów technicznych.

#### 2.4. Audyt Kompletności (`run_audit`) i Antybot
* **Mocne strony**:
  - Rejestracja `expected_total` vs `saved_bronze` w tabeli `run_audit`.
  - Realistyczny zestaw nagłówków Chromium na macOS.
* **Uwaga do regexa nagłówka**:
  - Wyrażenie `r'(\d+)\s*(ogłoszeń|ogłoszenia|ofert)'` powinno być ograniczone do kontenera nagłówka wyników (`<h1...>`, `<div class="listing-header"...>`), aby uniknąć błędnego dopasowania do bocznych boksów reklamowych lub sekcji "Podobne ogłoszenia w innych miastach".

---

### 3. Rekomendacje Standaryzacyjne
1. **Unifikacja korzenia `raw_payload`**: Upewnić się, że `GratkaProvider` zapisuje klucze `price_pln`, `area_m2`, `rooms`, `floor`, `has_elevator`, `location.coordinates` na pierwszym poziomie JSON-a.
2. **Spójność Geograficzna**: Zagwarantować obecność współrzędnych GPS w celu bezbłędnej fuzji ogłoszeń Gratka $\leftrightarrow$ Morizon $\leftrightarrow$ Otodom w `gold_listings`.
3. **Audyt per-dzielnica**: W przypadku pętli po wielu dzielnicach upewnić się, że `run_audit` rejestruje zagregowaną sumę oczekiwanych ofert lub audytuje każdy chunk.

---
*Status Recenzji: **Zatwierdzony warunkowo z zaleceniami optymalizacji geolokalizacji i schematu Silver.***
