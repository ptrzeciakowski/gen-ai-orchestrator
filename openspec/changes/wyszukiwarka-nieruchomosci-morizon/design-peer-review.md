# Raport z Przeglądu Architektonicznego (Peer Review): Morizon.pl

Ten dokument gromadzi niezależne recenzje inżynierskie i architektoniczne dla projektu integracji serwisu Morizon.pl (`design_initial.md`).

---

## 🧐 Recenzja Architektoniczna: Architekt OLX

**Recenzent**: Architekt Oprogramowania (Wyszukiwarka Nieruchomości - OLX Provider)  
**Data Recenzji**: 15 Sierpnia 2026  
**Dokument Oceniany**: [design_initial.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-morizon/design_initial.md)  
**Status Oceny**: 🟡 **Zaakceptowany Warunkowo z Rekomendacjami Wydajnościowymi (Approved with Performance Concerns)**

---

### 1. Spójność z Architekturą ELT (Bronze -> Silver -> Gold) i Bazy Danych (`db.py`)
* **Warstwa Bronze**: Koncepcja zapisu surowego słownika JSON do `bronze_listings` z oznaczeniem `source_portal = 'morizon'` i przypisaniem `run_id` jest w 100% zgodna z regułami systemu.
* **Warstwa Silver**: Prawidłowo zaproponowano mapowanie `raw_json_ld` oraz pól pochodnych (`price_per_m2`, `is_last_floor`).
* **Warstwa Gold**: Konsolidacja w `gold_listings` zadziała poprawnie przy założeniu, że pola `lat`, `lon`, `area_m2`, `rooms` zostaną wyekstrahowane w Silver.

---

### 2. Poprawność Mapowania Kryteriów Biznesowych (`kryteria.md`)
* **Struktura Zapytania URL**: Bardzo dobre i precyzyjne mapowanie parametrów tablicowych Morizona `ps[price_from]`, `ps[price_to]`, `ps[number_of_rooms_from]`, `ps[living_area_from]`.
* **Uczciwość Inżynierska**: Wzorcowe oznaczenie etykietą `[Hipoteza/Domysł]` parametru `ps[market_type]`. Rekomenduję, aby w implementacji `MorizonProvider` w razie wątpliwości zrezygnować z przekazywania `ps[market_type]` w URL i pobrać pełen strumień (Broad Fetch), cedując weryfikację rynku na SQL w warstwie Gold.

---

### 3. Odporność na Błędy, Antyboty i Audytowalność (`run_audit`)
* **Audyt Kompletności**: Zdefiniowany poprawnie. Ekstrakcja liczby ofert z nagłówka wyników i rejestracja w `run_audit` zapewnia pełną audytowalność zrzutu.
* **Nagłówki i Odporność**: Pełny zestaw nagłówków HTTP oraz obsługa wyjątków z logowaniem błędów.

---

### 4. ⚠️ Główna Uwaga Architektoniczna: Ryzyko Wydajnościowe Wariantu 1 (Scraping Dwuetapowy)
* **Zidentyfikowany Problem**:
  W sekcji 6 wybrano **Wariant 1 (Scraper Dwuetapowy: Listing -> Pobranie podstrony każdej oferty)**.
  W przypadku wyszukiwania dla 3 dzielnic (Ursynów, Mokotów, Wilanów), przy 30–40 ofertach na dzielnicę, scraper wyśle **ok. 100–150 osobnych zapytań HTTP**. Przy bezpiecznym opóźnieniu `0.2s` oraz czasie odpowiedzi serwera `0.3-0.5s` na zapytanie:
  $$\text{Czas wykonania} \approx 120 \times 0.6\text{s} \approx 72\text{ sekundy!}$$
  Jest to znaczący narzut czasowy w porównaniu do providerów `Otodom` (~1-2s) i `OLX` (~1-2s), a dodatkowo wysoka liczba kolejnych zapytań z jednego IP drastycznie zwiększa ryzyko otrzymania kodu **HTTP 429 Too Many Requests** lub blokady WAF.
* **Rekomendowane Rozwiązanie (Usprawnienie do tasks.md)**:
  Wdrożenie **Podejścia Hybrydowego (jak w projekcie Gratka)**:
  1. Pobieraj szczegółową podstronę oferty **wyłącznie wtedy**, gdy na karcie listingu brakuje kluczowych pól (np. windy lub koordynatów GPS).
  2. Jeśli karta listy zawiera już metraż, cenę, pokoje, piętro i windę, utwórz `raw_payload` bezpośrednio z danych listy bez wysyłania kolejnego żądania HTTP.
  3. Zredukuje to liczbę requestów o 60–80%, skracając czas wykonania do kilku sekund.

---

### 5. Deduplikacja Międzyserwisowa (`dedup_fingerprint`)
* Brak zastrzeżeń. Zapewnienie dokładnych koordynatów GPS z `geo.latitude` / `geo.longitude` w JSON-LD pozwoli na precyzyjną deduplikację ofert publikowanych równolegle na Morizonie, Gratce i OLX.

---
*Podsumowanie: Projekt jest bardzo solidny merytorycznie. Rekomenduję uwzględnienie optymalizacji hybrydowej podczas planowania zadań w tasks.md.*
