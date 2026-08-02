# Plan Wdrożeniowy OpenSpec (Tasks): Integracja Adresowo.pl i Retencja Danych Historycznych

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-adresowo`  
**Data**: 2 Sierpnia 2026  
**Status**: W Trakcie Wdrożenia (In Progress)  
**Dokumenty Referencyjne**:
- `file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-adresowo/design.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-adresowo/proposal.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`

---

## 🏗️ Faza 1: Implementacja Providera Adresowo i Retencja Historyczna SQLite

- [x] **Moduł `AdresowoProvider` (`wyszukiwarka-nieruchomosci/src/providers/adresowo.py`)**
  - Utwórz klasę `AdresowoProvider` pobierającą oferty dla miast/dzielnic z `kryteria.md`.
  - Zaimplementuj parsowanie znaczników `JSON-LD` (`schema.org/Offer`, `schema.org/Place`) oraz parametrów HTML (`rok budowy`, `winda`, `bez pośredników`).
  - **Kryterium Akceptacji**: Pobrane surowe obiekty z Adresowo.pl lądują w tabeli `bronze_listings` z `source_portal='adresowo'`.

- [x] **Retencja Historyczna w Bazie Danych (`wyszukiwarka-nieruchomosci/src/db.py` & `main.py`)**
  - Usuń automatyczne czyszczenie bazy (`clear_bronze()`) przy każdym odświeżeniu.
  - Zapewnij pełne wsparcie dla unikalnych kluczy `UNIQUE(run_id, source_portal, external_id)`.
  - **Kryterium Akceptacji**: Kilkukrotne uruchomienie skryptu zachowuje wpisy z poprzednich `run_id` w tabeli `bronze_listings`.

---

## 🧪 Faza 2: Walidacja Kryteriów i Pakiet Testowy (`tests/test_adresowo_criteria.py`)

- [x] **Dedykowany Pakiet Testów Kryteriów (`wyszukiwarka-nieruchomosci/tests/test_adresowo_criteria.py`)**
  - Napisz automatyczny pakiet testowy sprawdzający każde kryterium z `kryteria.md` (cena, pokoje, metraż, piętro, winda, rok budowy, typ ogłoszeniodawcy) na dostarczonych próbkach danych z Adresowo.pl.
  - Udokumentuj i jawnie wykaż obostrzenia dotyczące zapytań URL vs filtracji SQL.
  - **Kryterium Akceptacji**: `pytest wyszukiwarka-nieruchomosci/tests/test_adresowo_criteria.py` przechodzi bez błędów.

---

## 🥇 Faza 3: Deduplikacja i Wykrywanie Nowości (Gold Layer & Novelty Detection)

- [x] **Konsolidacja w Widoku Gold (`wyszukiwarka-nieruchomosci/src/deduplicator.py`)**
  - Zaktualizuj widok `gold_listings` tak, aby łączył oferty z Otodom i Adresowo.pl o tym samym kluczu geolokalizacyjno-metrażowym.
  - Przefiltruj dane w `Deduplicator.get_gold_listings(config, run_id)` tak, aby raport zawierał **wyłącznie oferty z zadanej uruchomieniowej identyfikacji `run_id`**.

- [x] **Oznaczanie Nowych Ofert (`is_new_listing`)**
  - Zaimplementuj wyliczanie flagi nowości: oferta jest nowa, jeśli dany `external_id` / `dedup_fingerprint` nie pojawiał się w żadnym wcześniejszym `run_id`.
  - **Kryterium Akceptacji**: Pierwsze uruchomienie oznacza oferty jako `NOWA`, drugie uruchomienie o tym samym zrzucie oznacza je jako `ZNAJOMA`.

---

## 📊 Faza 4: Integracja Orkiestracji i Generowanie Raportu End-to-End

- [x] **Orkiestracja w `main.py` & Generator Raportów (`report_generator.py`)**
  - Dodaj `AdresowoProvider` do pętli pobierającej w `main.py`.
  - Uwzględnij oznaczenie flagi `NOWA` przy ofertach w wygenerowanym raporcie Markdown.
  - **Weryfikacja**: Uruchomienie `python3 wyszukiwarka-nieruchomosci/main.py` generuje raport zawierający unikalne oferty z Otodom oraz Adresowo.pl.
