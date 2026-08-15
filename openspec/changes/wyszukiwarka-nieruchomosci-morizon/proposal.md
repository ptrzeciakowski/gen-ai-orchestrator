# OpenSpec Proposal: Integracja Serwisu Morizon.pl w Wyszukiwarce Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-morizon`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

**Morizon.pl** (część grupy Gratka/Morizon) to jeden z kluczowych portali nieruchomościowych w Polsce, charakteryzujący się bogatą bazą ofert agencyjnych, inwestycji deweloperskich oraz unikalnymi ogłoszeniami z rynku wtórnego. Jego integracja zwiększy kompletność danych rynkowych i precyzję analizy statystycznej w zestawieniu z rejestrem RCN.

---

## 2. Architektura i Obsługa Filtrów (Filter Mapping)

Projekt zakłada pobieranie szerokiego strumienia danych do warstwy **Bronze**, normalizację w warstwie **Silver** oraz rygorystyczne egzekwowanie reguł biznesowych z `kryteria.md` w warstwie **Gold**.

### 🧭 Zestawienie Obsługi Filtrów dla Morizon:

| Kryterium z `kryteria.md` | Poziom Obsługi | Opis implementacji i ograniczenia |
| :--- | :---: | :--- |
| **Miasto i Dzielnica** | 🟢 **Wejście (URL / Query)** | Obsługiwane w ścieżce URL: `/mieszkania/sprzedaz/{city_slug}/{district_slug}/`. |
| **Cena minimalna i maksymalna** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry query `ps[price_from]` oraz `ps[price_to]`. |
| **Liczba pokoi** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry `ps[number_of_rooms_from]` i `ps[number_of_rooms_to]`. |
| **Powierzchnia min/max** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametry `ps[living_area_from]` i `ps[living_area_to]`. |
| **Rynek (Pierwotny / Wtórny)** | 🟢 **Wejście (URL / Query)** | Obsługiwane przez parametr rynku (np. `ps[market_type]`). |
| **Piętro min/max & Wyklucz parter** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Morizon nie zawsze precyzyjnie filtruje wykluczenie skrajnych kondygnacji w zapytaniu bazowym. Piętro jest ekstrahowane ze znaczników oferty i filtrowane w SQL w warstwie Gold. |
| **Winda** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Brak stabilnego parametru URL dla windy na liście wyników. Weryfikacja następuje w Silver/Gold poprzez analizę parametrów technicznych budynku lub opisu. |
| **Rok budowy & Stan wykończenia** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Filtrowane po stronie bazy danych na podstawie metadanych oferty wyciągniętych z JSON-LD lub selektorów HTML. |
| **Odległość od stacji metra** | 🔴 **Poza zakresem providera** | Obliczane centralnie w module geolokalizacji. |

---

## 3. Wyzwania Techniczne i Ograniczenia Serwisu (Technical Caveats)

* **Struktura slugów i filtrów tablicowych**: Morizon używa parametrów query w notacji tablicowej (`ps[...]`) oraz specyficznych slugów dzielnicowych (np. `warszawa/ursynow`).
* **Format danych**: Dane na stronach Morizon zawierają mikrodane Schema.org oraz obiekty JSON-LD, z których można wyciągnąć precyzyjne współrzędne geograficzne i metraż.
* **Audyt kompletności**: Ekstrakcja łącznej liczby ogłoszeń z nagłówka wyników i rejestracja w `run_audit`.

---

## 4. Zakres Prac (Scope of Work)

- [ ] **Moduł `MorizonProvider` (`src/providers/morizon.py`)**: Implementacja pobierania i parsowania stron z Morizon.pl.
- [ ] **Integracja w `main.py`**: Dodanie wywołania `MorizonProvider` do pipeline'u ELT i rejestracja metryk w `run_audit`.
- [ ] **Dostosowanie warstwy Silver/Gold (`db.py`)**: Mapowanie schematu danych Morizon na ujednoliconą strukturę bazy danych.
- [ ] **Deduplikacja międzyserwisowa (`deduplicator.py`)**: Integracja ofert Morizon w procesie unifikacji `dedup_fingerprint`.
- [ ] **Testy jednostkowe (`tests/test_morizon_criteria.py`)**: Testy pobierania, parsowania JSON-LD oraz testy filtrów Gold.
