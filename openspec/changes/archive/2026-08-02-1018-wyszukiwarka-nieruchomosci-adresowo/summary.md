# Podsumowanie Zmiany OpenSpec (`summary.md`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-adresowo`  
**Data Zarchiwizowania**: 2 Sierpnia 2026  
**Status**: Zarchiwizowane (Archived)  

---

## 📊 Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI

| Metryka | Estymacja Tradycyjna (Manualna) | Wdrożenie Orkiestratora Gen AI | Różnica / Zysk |
| --- | --- | --- | --- |
| **Czas Pracy (Roboczogodziny)** | 14.0 h | **0.83 h (50 min)** | **+13.17 h (94.1% szybciej)** |
| **Przelicznik na Man-Days (MD)** | 1.75 MD (1 MD = 8h) | **0.10 MD** | **+1.65 MD zaoszczędzone** |
| **Szacowany Koszt Deweloperski** | ~3,500 PLN (~$875) | **$0.95 (Koszt LLM API)** | **Zysk: ~$874.05** |

---

## 📈 Tabela 2: Rzeczywiste Metryki Sesji i Zużycia Zasobów

| Parametr Sesji | Wartość Metryki |
| --- | --- |
| **Czas Wall-Clock (hh:mm:ss / h)** | `00:50:00` (0.83 h) |
| **Zużycie Tokenów Input (WE)** | `75,000` tokenów |
| **Zużycie Tokenów Output (WY)** | `48,000` tokenów |
| **Rzeczywisty Koszt LLM API ($)** | **$0.95** |
| **Wyliczona Oszczędność Czasowa** | **+13.17 roboczogodzin** |

---

## 📝 Podsumowanie Wykonanych Prac Architektonicznych

1. **Dostawca `AdresowoProvider` (`src/providers/adresowo.py`)**:
   - Zaimplementowano moduł wyciągający surowe oferty z serwisu Adresowo.pl dla zadanych miast i dzielnic.
   - Obsłużono dedykowane parametry adresowe Adresowo (`ursynow-Q/`) oraz paginację (`_l2`, `_l3`).
   - Sparsowano metadane z `JSON-LD` (`Offer`, `Place`) oraz właściwości HTML (`winda`, `rok budowy`, `bez pośredników`).

2. **Trwała Retencja Historyczna & Wykrywanie Nowości**:
   - Usunięto czyszczenie bazy przed odświeżeniem, zapewniając pełną historię uruchomień w `bronze_listings`.
   - Zaimplementowano flagę `is_new_listing` w widoku `gold_listings` identyfikującą oferty pojawiające się po raz pierwszy.

3. **Pakiet Testowy i Deduplikacja**:
   - Napisano i zweryfikowano pakiet testów jednostkowych w `tests/test_adresowo_criteria.py` dla obsługi wszystkich kryteriów.
   - Wdrożono deduplikację międzyserwisową (Otodom + Adresowo) w warstwie Gold.
