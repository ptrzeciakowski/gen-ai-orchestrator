# OpenSpec Proposal: Integracja Serwisu Gratka.pl w Wyszukiwarce Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-gratka`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

**Gratka.pl** to jeden z najstarszych i najbardziej rozpoznawalnych serwisów ogłoszeniowych w Polsce (grupa Gratka/Morizon / Polska Press), posiadający szerokie pokrycie rynku mieszkaniowego w Warszawie i aglomeracjach. Dołączenie Gratki pozwoli na jeszcze pełniejszą agregację ofert oraz eliminację białych plam w monitoringu rynku.

---

## 2. Architektura i Obsługa Filtrów (Filter Mapping)

Zgodnie z architekturą trójwarstwową (Bronze -> Silver -> Gold):
1. **Bronze**: Zapis surowego HTML/JSON do `bronze_listings`.
2. **Silver**: Normalizacja atrybutów Gratki do wspólnego schematu bazy danych.
3. **Gold**: Rygorystyczne egzekwowanie kryteriów biznesowych z `kryteria.md`.

### 🧭 Zestawienie Obsługi Filtrów dla Gratka.pl:

| Kryterium z `kryteria.md` | Poziom Obsługi | Opis implementacji i ograniczenia |
| :--- | :---: | :--- |
| **Miasto i Dzielnica** | 🟢 **Wejście (URL / Query)** | Obsługiwane w ścieżce URL: `/nieruchomosci/mieszkania/{city_slug}/{district_slug}/sprzedaz`. |
| **Cena minimalna i maksymalna** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry zapytania `cena-calkowita:min` i `cena-calkowita:max`. |
| **Liczba pokoi** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry `liczba-pokoi:min` i `liczba-pokoi:max`. |
| **Powierzchnia min/max** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry `powierzchnia-w-m2:min` i `powierzchnia-w-m2:max`. |
| **Rynek (Pierwotny / Wtórny)** | 🟢 **Wejście (URL / Query)** | Obsługiwane w filtrze URL (rynek wtórny / pierwotny). |
| **Piętro min/max & Wyklucz parter** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Gratka nie pozwala na proste wykluczenie wyłącznie parteru w URL bez odcięcia innych pięter. Piętro jest odczytywane z karty ogłoszenia i selekcjonowane w SQL w warstwie Gold. |
| **Winda** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Brak stabilnego parametru windy w głównym URL wyszukiwania. Weryfikacja następuje w warstwie Gold na podstawie cech dodatkowych. |
| **Rok budowy & Stan wykończenia** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Weryfikowane po stronie bazy danych na podstawie parametrów zebranych w warstwie Bronze/Silver. |
| **Odległość od stacji metra** | 🔴 **Poza zakresem providera** | Obliczane centralnie w module geolokalizacji. |

---

## 3. Wyzwania Techniczne i Ograniczenia Serwisu (Technical Caveats)

* **Format parametrów URL**: Gratka stosuje notację dwukropka w parametrach (np. `cena-calkowita:min=1000000`).
* **Paginacja i audyt**: Obsługa stron przez `page=N` oraz zliczanie łącznej liczby zadeklarowanych ofert w nagłówku wyników do tabeli `run_audit`.
* **Cechy nieruchomości**: Ekstrakcja danych technicznych z listy `cechy` oraz znaczników JSON-LD.

---

## 4. Zakres Prac (Scope of Work)

- [ ] **Moduł `GratkaProvider` (`src/providers/gratka.py`)**: Implementacja pobierania i parsowania ogłoszeń do warstwy Bronze.
- [ ] **Integracja w `main.py`**: Dodanie providera do procesu głównego i obsługa `run_audit`.
- [ ] **Warstwa Silver/Gold (`db.py`)**: Mapowanie pól i zapytań SQL dla ogłoszeń z Gratka.pl.
- [ ] **Deduplikacja międzyserwisowa (`deduplicator.py`)**: Uwzględnienie unikalnych ofert w `dedup_fingerprint`.
- [ ] **Testy jednostkowe (`tests/test_gratka_criteria.py`)**: Pokrycie testami jednostkowymi zgodności z `kryteria.md`.
