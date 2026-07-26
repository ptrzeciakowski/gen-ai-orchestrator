# Architectural Design: Wyszukiwarka Nieruchomości Warszawa & Integracja RCN

## Context

Moduł `wyszukiwarka-nieruchomosci/` jest autonomicznym serwisem zlokalizowanym w podkatalogu repozytorium `gen-ai-orchestrator`.
Serwis służy do automatycznego agregowania, selekcji oraz odświeżania na żądanie ofert nieruchomości w Warszawie według parametrów z pliku `wyszukiwarka-nieruchomosci/kryteria.md`.

Dokumenty wynikowe w `wyszukiwarka-nieruchomosci/historia/YYYY-MM-DD-HH24MISS-oferty.md` rejestrują **faktycznie zastosowane kryteria wyszukiwania dla zapewnienia pełnej audytowalności**, łączą oferty rynkowe z 5-kwantylowym rozkładem cen transakcyjnych z Rejestru Cen Nieruchomości (RCN Warszawa: `https://mapa.um.warszawa.pl/rcn-szukaj/`) oraz rekomendacjami AI.

---

## Technical Architecture & Component Flow

```mermaid
graph TD
    A["Trigger: Engine Execution"] --> B["1. Parse & Log Applied Criteria (config.py)"]
    B --> C["2. Fetch Listings (Otodom, OLX, Adresowo, Sprzedajemy, Lento)"]
    C --> D["3. Deduplicate Listings (deduplicator.py)"]
    D --> E["4. Fetch RCN Quantiles: N, Avg, P10, P25, P50, P75, P90 (rcn_client.py)"]
    E --> F["5. Format Report with Audit Trail & AI Recommendations"]
    F --> G["6. Output historia/YYYY-MM-DD-HH24MISS-oferty.md"]
```

---

## Detailed Integration Specifications

1. **Audytowalność Kryteriów**: W nagłówku raportu sekcja `## ⚙️ Faktycznie Zastosowane Kryteria Wyszukiwania` wypisuje ścieżkę pliku konfiguracyjnego oraz dokładne wartości parametrów użyte w przebiegu (ceny, metraż, dzielnice, typ ogłoszeniodawcy, stan prawny).
2. **Rozkład Kwantylowy RCN Warszawa**: Każda dzielnica i obszar MSI (Kabaty, Natolin, Stary Mokotów, Filtry itp.) prezentuje wskaźniki: $N$ (liczba transakcji), Średnia, P10, P25, P50 (Mediana), P75, P90.
3. **Prawdziwe Odsyłacze**: Każda oferta w tabeli zawiera aktywny, sprawdzony URL.
