# Plan Dekompozycji Zadań Wdrożeniowych (tasks.md)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-full-dynamic-pagination`  
**Data**: 22 Sierpnia 2026  
**Status**: Plan Wdrożenia (Tasks - Ukończony)  
**Dokumenty Referencyjne**:
- [`proposal.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-full-dynamic-pagination/proposal.md)
- [`design.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-full-dynamic-pagination/design.md)
- [`src/providers/commercial.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/commercial.py)
- [`src/providers/direct.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/direct.py)
- [`src/providers/gratka.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/gratka.py)
- [`src/providers/morizon.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/morizon.py)
- [`src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py)
- [`src/providers/olx.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/olx.py)

---

## 📋 Lista Zadań Wdrożeniowych (Decomposition)

### Faza 1: Otodom Scraper (`commercial.py` & `direct.py`)

- [x] **1.1. Dynamiczna paginacja Otodom**
  - **Pliki**: [`src/providers/commercial.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/commercial.py), [`src/providers/direct.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/direct.py)
  - **Opis**: Zastąpienie sztywnego `max_pages = 3` dynamicznym czytaniem `totalPages` z `pagination` w `__NEXT_DATA__`.
  - **Kryteria Akceptacji**: Pętla przechodzi wszystkie podstrony (np. 1..31 dla Ursynowa) aż do wyczerpania ofert.

---

### Faza 2: Pozostałe Portale (`gratka.py`, `morizon.py`, `nieruchomosci_online.py`, `olx.py`, `adresowo.py`)

- [x] **2.1. Dynamiczna paginacja Gratka & Morizon**
  - **Pliki**: [`src/providers/gratka.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/gratka.py), [`src/providers/morizon.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/morizon.py)
  - **Opis**: Usunięcie `self.max_pages = 5` i pętla do ostatniej dostępnej strony z ofertami.

- [x] **2.2. Dynamiczna paginacja Nieruchomości-online, OLX & Adresowo**
  - **Pliki**: [`src/providers/nieruchomosci_online.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/nieruchomosci_online.py), [`src/providers/olx.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/olx.py), [`src/providers/adresowo.py`](file:///Users/pawel/git/wyszukiwarka-nieruchomosci/src/providers/adresowo.py)
  - **Opis**: Pętla do wyczerpania `page_count` / braku ogłoszeń na kolejnych stronach.

---

### Faza 3: Weryfikacja i Testy Regresyjne

- [x] **3.1. Uruchomienie testów jednostkowych**
  - **Kryteria Akceptacji**: Wszystkie testy jednostkowe przechodzą pomyślnie (`OK`).
  - **Weryfikacja**: `python3 -m unittest discover tests`.
