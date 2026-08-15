# OpenSpec Proposal: Integracja Serwisu OLX.pl w Wyszukiwarce Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-olx`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Portal **OLX.pl** jest jednym z największych serwisów ogłoszeniowych w Polsce, skupiającym unikalną bazę ogłoszeń bezpośrednich ("od właściciela") oraz lokalnych ofert biur nieruchomości. Włączenie OLX do ekosystemu Wyszukiwarki Nieruchomości znacząco zwiększy pokrycie rynku i wykrywalność okazji cenowych poniżej stawek rynkowych RCN.

---

## 2. Architektura i Obsługa Filtrów (Filter Mapping)

Zgodnie ze standardem ELT przyjętym w projekcie:
1. **Warstwa Bronze (Ekstrakcja szerokiego strumienia)**: Pobiera surowe dane ogłoszeń z OLX i zapisuje payload JSON/HTML do tabeli `bronze_listings`.
2. **Warstwa Silver (Normalizacja)**: Przekształca atrybuty OLX na zunifikowany schemat nieruchomości.
3. **Warstwa Gold (Ścisłe filtrowanie i deduplikacja)**: Realizuje dokładną selekcję ofert zgodnie z `kryteria.md`.

### 🧭 Zestawienie Obsługi Filtrów dla OLX:

| Kryterium z `kryteria.md` | Poziom Obsługi | Opis implementacji i ograniczenia |
| :--- | :---: | :--- |
| **Miasto i Dzielnica** | 🟢 **Wejście (URL / Query)** | Obsługiwane w URL (`/nieruchomosci/mieszkania/sprzedaz/{city_slug}/`) oraz parametrze dzielnicy (`filter_enum_district`). |
| **Cena minimalna i maksymalna** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry zapytania `search[filter_float_price:from]` i `search[filter_float_price:to]`. |
| **Liczba pokoi** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametr `search[filter_enum_rooms][0]=three` (lub odpowiednik numeryczny). |
| **Rynek (Pierwotny / Wtórny)** | 🟡 **Warstwa Gold / Treść** | *Ograniczenie*: OLX posiada parametr rynku w części kategorii, lecz w ogłoszeniach prywatnych jest on często niespójny lub pomijany. Ścisła weryfikacja i filtrowanie następuje w warstwie Gold na podstawie metadanych oferty. |
| **Piętro min/max & Wyklucz parter** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Wstępne zapytanie OLX nie gwarantuje precyzyjnego wykluczenia parteru w query URL. Parametr piętra jest wyciągany z cech ogłoszenia i filtrowany regułą SQL w warstwie Gold. |
| **Winda** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Brak natywnego filtra URL dla windy w OLX. Weryfikacja następuje na poziomie parsowania opisu i listy udogodnień w Silver/Gold. |
| **Rok budowy & Stan wykończenia** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Brak stabilnego filtra wejściowego w URL. Parsowane z atrybutów ogłoszenia i weryfikowane w warstwie Gold. |
| **Odległość od stacji metra** | 🔴 **Poza zakresem providera** | Obliczane centralnie w module geolokalizacji na podstawie współrzędnych geograficznych. |

---

## 3. Wyzwania Techniczne i Ograniczenia Serwisu (Technical Caveats)

* **Ochrona antybotowa / Cloudflare**: OLX stosuje zaawansowaną ochronę nagłówków i zapytań HTTP. Wymagane jest przekazywanie realistycznych nagłówków `User-Agent`, `Sec-Ch-Ua` oraz obsługa stanu `window.__PRERENDERED_STATE__` / JSON osadzonego w kodzie strony.
* **Paginacja**: Implementacja dynamicznej paginacji (`page=N`) z audytem kompletności `run_audit` (zliczanie zadeklarowanej liczby ogłoszeń vs pobrane).

---

## 4. Zakres Prac (Scope of Work)

- [ ] **Moduł `OLXProvider` (`src/providers/olx.py`)**: Implementacja pobierania strumienia ofert i parsowania struktury danych do warstwy Bronze.
- [ ] **Integracja w `main.py`**: Podpięcie providera do głównego pipeline'u ELT i rejestracja audytu `run_audit`.
- [ ] **Mapowanie atrybutów w `db.py` (Silver & Gold Views)**: Dostosowanie widoków do struktury JSON zwracanej przez OLX.
- [ ] **Deduplikacja w `deduplicator.py`**: Włączenie ofert z OLX do międzyserwisowego wyliczania `dedup_fingerprint`.
- [ ] **Testy jednostkowe (`tests/test_olx_criteria.py`)**: Pokrycie testami parsowania parametrów, paginacji i zgodności z kryteriami.
