# Podsumowanie Zmiany OpenSpec (`summary.md`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-medallion-drill-down`  
**Data Zarchiwizowania**: 22 Sierpnia 2026  
**Status**: Zarchiwizowane (Archived)  

---

## 📊 Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI

| Metryka | Estymacja Tradycyjna (Manualna) | Wdrożenie Orkiestratora Gen AI | Różnica / Zysk |
| --- | --- | --- | --- |
| **Czas Pracy (Roboczogodziny)** | 8.0 h | **0.17 h (10 min)** | **+7.83 h (97.9% szybciej)** |
| **Przelicznik na Man-Days (MD)** | 1.00 MD (1 MD = 8h) | **0.02 MD** | **+0.98 MD zaoszczędzone** |
| **Szacowany Koszt Deweloperski** | ~2,000 PLN (~$500) | **$0.33 (Koszt LLM API)** | **Zysk: ~$499.67** |

---

## 📈 Tabela 2: Rzeczywiste Metryki Sesji i Zużycia Zasobów

| Parametr Sesji | Wartość Metryki |
| --- | --- |
| **Czas Wall-Clock (hh:mm:ss / h)** | `00:10:00` (0.17 h) |
| **Zużycie Tokenów Input (WE)** | `25,000` tokenów |
| **Zużycie Tokenów Output (WY)** | `17,000` tokenów |
| **Rzeczywisty Koszt LLM API ($)** | **$0.33** |
| **Wyliczona Oszczędność Czasowa** | **+7.83 roboczogodzin** |

---

## 📝 Podsumowanie Wykonanych Prac Architektonicznych

1. **Koncepcja Data Lineage (`GET /api/listings/lineage`)**: Projekt śledzenia pochodzenia rekordu Gold przez powiązane ogłoszenia w warstwie Silver aż do surowych zrzutów JSON w Bronze.
2. **Architektura Modalu Inspekcji (`ListingDrillDownModal.jsx`)**: Trójpoziomowy widok porównujący ceny, metraże i parametry ogłoszeń tego samego mieszkania na różnych portalach.
