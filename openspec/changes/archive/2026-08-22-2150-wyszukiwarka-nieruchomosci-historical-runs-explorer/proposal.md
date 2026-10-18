# OpenSpec Proposal: Eksplorator Sesji i Analiza Historyczna Ofert (Historical Runs Explorer)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-historical-runs-explorer`  
**Data**: 22 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`src/db.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
- [`src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
- [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Baza danych `listings.db` gromadzi historyczne zrzuty (`run_id`), jednak w interfejsie użytkownika brakuje wygodnego mechanizmu przeglądania i porównywania historycznych sesji pobierania:
1. Brak dedykowanego widoku tabelarycznego prezentującego wszystkie historyczne zrzuty z ich metrykami (czas trwania, liczba ofert w warstwach Bronze/Silver/Gold, audyt kompletności portali).
2. Użytkownik nie może w prosty sposób przełączyć się na wybrany historyczny zrzut, aby porównać, jak wyglądały dostępne mieszkania i wyceny w przeszłości (mechanizm Time-Travel / Historical Snapshot).

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Widok "Historia Zrzutów" (`RunsView.jsx`)**:
   - Dedykowana zakładka w menu głównym aplikacji (przełącznik pomiędzy widokiem bieżących ofert a historią sesji).
   - Tabela wszystkich sesji zrzutów z bazy (`SELECT * FROM run_audit`, agregacje `bronze_listings` i `gold_listings`).
2. **Karty Szczegółów Sesji (Run Detail View)**:
   - Rozkład pobranych ofert per portal (Otodom, Adresowo, Gratka, Morizon, NOL, OLX).
   - Wskaźnik kompletności scrapingu oraz kompresji w warstwie Gold.
3. **Akcja "Przeglądaj oferty z tej sesji"**:
   - Przycisk pozwalający załadować oferty danego `run_id` bezpośrednio do głównej siatki ofert i tabeli analitycznej.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Endpointy API (`src/api.py`)**: Rozbudowa `/api/runs` oraz `/api/runs/{run_id}/summary` o szczegółowe metryki audytowe.
- [ ] **Komponenty React (`ui/src/components/RunsView.jsx`)**: Tabela historii, filtry daty, kafelki statystyk.
- [ ] **Zarządzanie Stanem w React**: Obsługa parametru `activeRunId` w kontekście aplikacji.
- [ ] **Testy Jednostkowe & API**: Weryfikacja poprawności danych historycznych.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 📈 **Pełna audytowalność potoku**: Użytkownik widzi historię każdego zrzutu i skuteczność scraperów.
* 🕰️ **Analiza trendów rynkowych**: Możliwość weryfikacji, które oferty zniknęły z rynku (zostały sprzedane), a które nadal wiszą.
