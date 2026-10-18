# Podsumowanie Zmiany OpenSpec (`summary.md`)

**Kod Zmiany**: `wzory-matematyczne-gdocs`  
**Data Zarchiwizowania**: 11 Września 2026  
**Status**: Zarchiwizowane (Archived)  

---

## 📊 Tabela 1: Porównanie Estymacji Deweloperskiej i Automatyzacji AI

| Metryka | Estymacja Tradycyjna (Manualna) | Wdrożenie Orkiestratora Gen AI | Różnica / Zysk |
| --- | --- | --- | --- |
| **Czas Pracy (Roboczogodziny)** | 4.0 h | **0.17 h (10 min)** | **+3.83 h (95.8% szybciej)** |
| **Przelicznik na Man-Days (MD)** | 0.50 MD (1 MD = 8h) | **0.02 MD** | **+0.48 MD zaoszczędzone** |
| **Szacowany Koszt Deweloperski** | ~1,000 PLN (~$250) | **$0.31 (Koszt LLM API)** | **Zysk: ~$249.69** |

---

## 📈 Tabela 2: Rzeczywiste Metryki Sesji i Zużycia Zasobów

| Parametr Sesji | Wartość Metryki |
| --- | --- |
| **Czas Wall-Clock (hh:mm:ss / h)** | `00:10:00` (0.17 h) |
| **Zużycie Tokenów Input (WE)** | `22,000` tokenów |
| **Zużycie Tokenów Output (WY)** | `16,000` tokenów |
| **Rzeczywisty Koszt LLM API ($)** | **$0.31** |
| **Wyliczona Oszczędność Czasowa** | **+3.83 roboczogodzin** |

---

## 📝 Podsumowanie Wykonanych Prac Architektonicznych

1. **Opracowanie Dydaktyczne (`wprowadzenie-do-calek.md`)**: Wprowadzenie do rachunku całkowego (całka nieoznaczona i oznaczona, metody całkowania) z pełną notacją matematyczną LaTeX.
2. **Konwersja do Natywnego OMML (`wprowadzenie-do-calek.docx`)**: Wygenerowanie dokumentu Word/Google Docs z edytowalnymi równaniami matematycznymi OMML.
