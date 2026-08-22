# OpenSpec Proposal: Pełny Wgląd w Warstwy Medallion dla Oferty (Medallion Lineage Drill-Down: Gold -> Silver -> Bronze)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-medallion-drill-down`  
**Data**: 22 Sierpnia 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**:
- [`src/db.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/db.py)
- [`src/deduplicator.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/deduplicator.py)
- [`src/api.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/api.py)
- [`.ai/guidelines/brutally-honest-rules.md`](file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md)

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Architektura Medallion (`Bronze` -> `Silver` -> `Gold`) scala i deduplikuje oferty z 6 portali w jeden rekord w warstwie Gold. Jednak użytkownik widzi wyłącznie wynik końcowy i nie może zbadać:
1. Z jakich dokładnie ogłoszeń z poszczególnych portali powstał dany rekord Gold (np. 1 ogłoszenie z Gratki, 1 z Otodomu, 1 bezpośrednie z Adresowo).
2. Jakie były różnice w danych pomiędzy portalami (np. czy jedna agencja podała wyższą cenę, inny metraż lub ukryła piętro/rok budowy).
3. Jak wyglądał oryginalny, surowy zrzut JSON (`raw_payload`) pobrany przez scraper (przydatne przy weryfikacji szczegółów i debugowaniu).

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

1. **Endpoint Data Lineage (`GET /api/listings/lineage?fingerprint=...&run_id=...`)**:
   - Zwraca rekord Gold wraz z listą wszystkich powiązanych rekordów Silver oraz ich surowymi obiektami JSON z Bronze.
2. **Komponent Drill-Down Modal / Drawer w React (`ListingDrillDownModal.jsx`)**:
   - **Zakładka 1: Warstwa Gold**: Scalone parametry oferty, geolokalizacja, kalkulacja opłacalności RCN i lista źródeł.
   - **Zakładka 2: Warstwa Silver (Porównanie Duplikatów)**: Tabela porównawcza parametrów podanych przez każdy z portali (cena, metraż, piętro, typ ogłoszeniodawcy).
   - **Zakładka 3: Warstwa Bronze (Inspektor JSON)**: Interaktywne drzewo JSON dla każdego portalu z podświetlaniem składni i przyciskiem kopiowania.

---

## 3. Zakres Prac (Scope of Work)

- [ ] **Zapytanie SQL i Logika w `src/db.py` / `src/api.py`**: Ekstrakcja powiązanych rekordów Bronze/Silver dla danego odcisku palca (`dedup_fingerprint` / `bronze_id`).
- [ ] **Komponenty React (`ui/src/components/ListingDrillDownModal.jsx`, `JsonViewer.jsx`)**: Interaktywny modal z trzema poziomami inspekcji.
- [ ] **Integracja z Siatką i Tabelą Ofert**: Kliknięcie w kartę lub przycisk "Szczegóły / Lineage" otwiera modal.
- [ ] **Testy Jednostkowe & Regresja**: Weryfikacja spójności relacji Gold -> Silver -> Bronze.

---

## 4. Oczekiwane Korzyści (Impact & Metrics)

* 🔍 **100% transparentność danych (Data Lineage)**: Użytkownik widzi pełną historię każdego ogłoszenia i może porównać oferty bezpośrednie z agencyjnymi.
* 🛡️ **Pewność analityczna**: Błyskawiczna weryfikacja poprawności deduplikacji i parsowania cech.
