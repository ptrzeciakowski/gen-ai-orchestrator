# Proposal: Wyszukiwarka Nieruchomości Warszawa & Integracja z RCN

## Summary
Projekt zakłada stworzenie dedykowanego serwisu w języku Python (`wyszukiwarka-nieruchomosci/`), który w pierwszym etapie skupia się na precyzyjnym pobieraniu autentycznych ogłoszeń sprzedaży mieszkań z portalu **Otodom.pl** dla m.st. Warszawy. Zbiór pobranych ofert jest filtrowany, deduplikowany i zestawiany z oficjalną bazy danych Rejestru Cen Nieruchomości (RCN m.st. Warszawy) w celu wyliczenia odchyleń cenowych i wskazania okazjonalnych mieszkań.

---

## Directives & System Context (Bezwzględna Uczciwość)

1. **Focus na Otodom.pl (Etap 1)**: Skupienie na jednym wiodącym portalu (Otodom.pl) w celu wyeliminowania błędnych linków kategorialnych, ofert wynajmu oraz złych dzielnic i przekroczeń budżetowych.
2. **Bezwzględne Filtrowanie Rynkowe**:
   - **Wyłącznie Sprzedaż**: Kategoryczny zakaz przemycania ogłoszeń wynajmu (`wynajem`, `/do-wynajecia/`).
   - **Tylko Indywidualne Oferty Lokali**: Kategoryczny zakaz zapisywania linków kategorialnych (np. `.../mieszkania.html`).
   - **Ścisły Budżet i Dzielnica**: Przestrzeganie `max_price` (np. max 1,200,000 PLN) oraz wybranej dzielnicy (np. Ursynów). Brak przemycania ofert z Pragi czy Bielan.
3. **Analiza RCN i Statystyki**: 7 kwantyli ($P10, P25, P50\text{-Mediana}, P75, P90, P95, P99$) oraz próba autentycznych aktów notarialnych ($Rej.A/...$).
4. **Rozszerzalność (Etap 2+)**: Po ustabilizowaniu i 100% weryfikacji Otodom.pl, dołączane będą kolejne portale (OLX, Morizon, Adresowo, Sprzedajemy, Lento).

---

## Planned Artifacts & Code Architecture
- `wyszukiwarka-nieruchomosci/kryteria.md`: Dedykowany plik parametrów wyszukiwania.
- `wyszukiwarka-nieruchomosci/src/config.py`: Parser konfiguracyjny.
- `wyszukiwarka-nieruchomosci/src/providers/commercial.py`: Dedykowany provider **Otodom.pl**.
- `wyszukiwarka-nieruchomosci/src/providers/direct.py`: Zaślepka dla Etapu 2.
- `wyszukiwarka-nieruchomosci/src/deduplicator.py`: Moduł deduplikacji $O(1)$.
- `wyszukiwarka-nieruchomosci/src/rcn_client.py`: Klient bazy RCN m.st. Warszawy.
- `wyszukiwarka-nieruchomosci/src/report_generator.py`: Generator raportu Markdown ze spisem treści (TOC).
