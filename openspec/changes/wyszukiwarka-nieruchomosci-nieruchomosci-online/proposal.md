# OpenSpec Proposal: Integracja Serwisu Nieruchomosci-online.pl w Wyszukiwarce Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-nieruchomosci-online`  
**Data**: 15 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

**Nieruchomosci-online.pl** to jeden z czołowych portali nieruchomościowych w Polsce, charakteryzujący się bardzo wysoką jakością i rzetelnością opisów ofert (zarówno z rynku wtórnego, jak i pierwotnego). Integracja tego źródła pozwoli na poszerzenie bazy unikalnych ofert oraz wzbogaci analizę porównawczą z transakcjami RCN.

---

## 2. Architektura i Obsługa Filtrów (Filter Mapping)

Zgodnie z zasadami systemu: pobranie szerokiego strumienia ogłoszeń do warstwy **Bronze**, znormalizowanie do **Silver** oraz rygorystyczne wyselekcjonowanie spełniających kryteria rekordów w warstwie **Gold**.

### 🧭 Zestawienie Obsługi Filtrów dla Nieruchomosci-online:

| Kryterium z `kryteria.md` | Poziom Obsługi | Opis implementacji i ograniczenia |
| :--- | :---: | :--- |
| **Miasto i Dzielnica** | 🟢 **Wejście (URL / Pozycyjny)** | Obsługiwane w formacie ścieżki i parametrów pozycyjnych (np. `szukaj.html?3,mieszkanie,sprzedaz,,{city}:{district}`). |
| **Cena minimalna i maksymalna** | 🟢 **Wejście (URL / Pozycyjny)** | Obsługiwane w sekcji cenowej zapytania (`{price_min}-{price_max}`). |
| **Liczba pokoi** | 🟢 **Wejście (URL / Pozycyjny)** | Obsługiwane w sekcji liczby pokoi w query URL. |
| **Rynek (Pierwotny / Wtórny)** | 🟢 **Wejście (URL / Pozycyjny)** | Obsługiwane przez wybór kategorii rynku w URL (wtórny / pierwotny). |
| **Piętro min/max & Wyklucz parter** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Serwis nie udostępnia w prostym URL wykluczenia parteru z zachowaniem elastycznych pięter. Piętro jest pobierane z metadanych i filtrowane w SQL w warstwie Gold. |
| **Winda** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Brak możliwości wymuszenia windy na poziomie zapytania głównego. Informacja o windzie jest odczytywana z atrybutów budynku w warstwie Silver/Gold. |
| **Rok budowy & Stan wykończenia** | 🔴 **Wyłącznie Warstwa Gold** | *Ograniczenie*: Weryfikowane po stronie bazy danych na podstawie szczegółowych parametrów oferty. |
| **Odległość od stacji metra** | 🔴 **Poza zakresem providera** | Obliczane centralnie w module geolokalizacji. |

---

## 3. Wyzwania Techniczne i Ograniczenia Serwisu (Technical Caveats)

* **Specyficzny format URL**: Nieruchomosci-online stosuje autorski, pozycyjny format parametrów w adresie URL (rozdzielanych przecinkami), który wymaga dedykowanego generatora zapytań dla miast i dzielnic.
* **Struktura HTML i metadane**: Oferty posiadają ustrukturyzowane znaczniki danych oraz tabele parametrów technicznych wewnątrz karty ogłoszenia.
* **Audyt kompletności**: Parsowanie deklarowanej liczby wyników i zapis do `run_audit`.

---

## 4. Zakres Prac (Scope of Work)

- [ ] **Moduł `NieruchomosciOnlineProvider` (`src/providers/nieruchomosci_online.py`)**: Implementacja pobierania i ekstrakcji ofert do warstwy Bronze.
- [ ] **Integracja w `main.py`**: Podpięcie providera do pipeline'u ELT i rejestracja audytu `run_audit`.
- [ ] **Widoki Silver i Gold (`db.py`)**: Zapewnienie kompatybilności schematu danych z nowym źródłem.
- [ ] **Deduplikacja międzyserwisowa (`deduplicator.py`)**: Uwzględnienie ofert Nieruchomosci-online w generowaniu `dedup_fingerprint`.
- [ ] **Testy jednostkowe (`tests/test_nieruchomosci_online_criteria.py`)**: Pokrycie testami parsera, paginacji oraz zgodności z `kryteria.md`.
