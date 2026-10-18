# OpenSpec Proposal: Dynamiczna Pełna Paginacja i 100% Zrzut Dzielnicy w Warstwie Bronze (Full Dynamic Pagination)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-full-dynamic-pagination`  
**Data**: 22 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`src/providers/commercial.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/commercial.py)
- [`src/providers/direct.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/direct.py)
- [`src/providers/gratka.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/gratka.py)
- [`src/providers/morizon.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/morizon.py)
- [`src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py)
- [`src/providers/olx.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/olx.py)
- [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Zgodnie z architekturą Medallion (Bronze -> Silver -> Gold), zadaniem scraperów w warstwie **Bronze** jest pobranie **kompletnego, surowego zrzutu wszystkich ogłoszeń z wybranej dzielnicy** (np. Ursynów), bez wcześniejszego odrzucania ofert po cenie, pokojach czy metrażu w Pythonie.

W dotychczasowej implementacji klasy providerów posiadały sztywne, sztuczne ograniczenia liczby stron:
* `CommercialProvider` (Otodom): `max_pages = 3` (pobierał zaledwie 108 z ponad 1100 ogłoszeń na Ursynowie – poniżej 10% rynku!).
* `GratkaProvider`: `max_pages = 5` (zamiast wszystkich ~30 stron).
* `MorizonProvider`: `max_pages = 5` (zamiast wszystkich ~30 stron).
* `NieruchomosciOnlineProvider`: `max_pages = 5`.
* `OLXProvider`: `max_pages = 5`.

W efekcie ogłoszenia znajdujące się na stronach od 4 wzwyż (w tym oferty nadesłane przez użytkownika) **nigdy nie trafiały do bazy danych Bronze**, co wypaczało kompletność warstwy surowej.

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Dynamiczna Detekcja Końca Paginacji (`totalPages`)**:
   - Wykorzystanie metadanych paginacyjnych zwracanych przez portale (np. `pagination.totalPages` w Otodom, numery stron w JSON-LD/HTML w Gratce i Morizonie, `page_count` w OLX).
   - Dynamiczne pobieranie wszystkich dostępnych stron aż do wyczerpania listy (`page > total_pages` lub pusta lista ogłoszeń).
2. **Konfigurowalny Limit Bezpieczeństwa (Opcjonalny `max_pages`)**:
   - Domyślnie brak sztywnego limitu (pobieranie 100% zrzutu dzielnicy).
   - Możliwość przekazania parametru `max_pages` dla szybkich testów debugowania.
3. **Optymalizacja i Bezpieczeństwo Sieciowe**:
   - Utrzymanie nagłówków przeglądarkowych i politeness delay.
   - Prawidłowe raportowanie audytu kompletności (100% zrzutu) w `run_audit`.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **`src/providers/commercial.py` & `src/providers/direct.py`**: Dynamiczna paginacja na bazie `search_ads.get('pagination', {}).get('totalPages')`.
- [ ] **`src/providers/gratka.py`**: Paginacja aż do ostatniej strony (detekcja braku kolejnych ofert / `page > total_pages`).
- [ ] **`src/providers/morizon.py`**: Paginacja aż do wyczerpania wyników dla danej dzielnicy.
- [ ] **`src/providers/nieruchomosci_online.py` & `src/providers/olx.py`**: Dynamiczne przejście wszystkich stron.
- [ ] **Testy Jednostkowe & Regresja**: Aktualizacja testów mockujących paginację dla wszystkich 6 providerów.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🎯 **100% kompletności w warstwie Bronze**: Wszystkie ogłoszenia z danej dzielnicy trafiają do bazy danych.
* 🔍 **Brak utraconych ofert**: Żadne ogłoszenie z dalszych podstron portali nie zostaje pominięte.
