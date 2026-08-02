# OpenSpec Proposal: Integracja Serwisu Adresowo.pl oraz Retencja Historyczna w Wyszukiwarce Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-adresowo`  
**Data**: 2 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-adresowo/explore/001-wyszukiwarka-nieruchomosci-adresowo-01.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Dotychczasowy system pobierał oferty wyłącznie z serwisu Otodom.pl oraz czyścił bazę danych przed każdym nowym uruchomieniem. Rodziło to trzy kluczowe niedogodności architektoniczne:

1. **Monokultura Źródeł Danych**: Ograniczenie się do jednego portalu uniemożliwiało dostęp do unikalnych ofert (zwłaszcza prywatnych ogłoszeń "bez pośredników") publikowanych w serwisie Adresowo.pl.
2. **Brak Śledzenia Historii i Nowości**: Kasowanie warstwy Bronze przy każdym uruchomieniu uniemożliwiało sprawdzanie, które oferty są całkowicie nowe, a które zmieniły cenę w czasie.
3. **Brak Dedykowanej Walidacji Kryteriów dla Nowych Dostawców**: Każdy nowy dostawca wymaga jawnego przetestowania i zamapowania wszystkich parametrów z `kryteria.md`.

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Wdrożenie Providera `AdresowoProvider` (`src/providers/adresowo.py`)**:
   - Pobieranie surowych struktur (HTML/JSON-LD) dla zadanego miasta i dzielnicy do warstwy Bronze.
2. **Wielouruchomieniowa Retencja Danych w Bronze & Silver**:
   - Zachowywanie historycznych rekordów z oznaczeniem `run_id` i `scraped_at`.
   - Zapewnienie, że generowany raport filtruje dane ściśle dla bieżącego uruchomienia `run_id`, zachowując dane z przeszłości do detekcji nowości.
3. **Deduplikacja w Warstwie Gold (`gold_listings`)**:
   - Agregacja ofert z Otodom i Adresowo.pl na podstawie wspólnego `dedup_fingerprint`.
4. **Zestaw Testów i Raport Walidacji Kryteriów**:
   - Zbudowanie automatu testowego weryfikującego obsługę każdego kryterium z `kryteria.md`.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Moduł `AdresowoProvider`**: Pobieranie i parsowanie ofert z Adresowo.pl.
- [ ] **Modyfikacja Bazy Danych (`db.py`)**: Zniesienie automatycznego czyszczenia Bronze i wsparcie dla `run_id` w Gold.
- [ ] **Moduł Deduplikacji (`deduplicator.py`)**: Konsolidacja ofert międzyserwisowych.
- [ ] **Zestaw Testów Jednostkowych (`tests/test_adresowo_criteria.py`)**: 100% pokrycia kryteriów z `kryteria.md`.
