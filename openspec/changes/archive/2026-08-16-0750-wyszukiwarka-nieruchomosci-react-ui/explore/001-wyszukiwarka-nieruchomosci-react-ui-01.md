# Eksploracja Architektoniczna: Nowoczesny Interfejs React dla Wyszukiwarki Nieruchomości

**Dokument**: `001-wyszukiwarka-nieruchomosci-react-ui-01.md`  
**Kod Zmiany**: `wyszukiwarka-nieruchomosci-react-ui`  
**Autor / Agent**: Antigravity Assistant  
**Data**: 16 Sierpnia 2026  
**Status**: Analiza Eksploracyjna (OpenSpec Exploration)  

---

## 1. Kontekst i Stan Obecny (Current State Analysis)

Projekt `wyszukiwarka-nieruchomosci` posiada w pełni zaimplementowaną architekturę ELT w oparciu o lokalną bazę SQLite (`data/listings.db`):
- **Warstwa Bronze (`bronze_listings`)**: Tabela przechowująca surowe obiekty JSON pobierane z 6 portali (`Otodom`, `Adresowo`, `Gratka`, `Morizon`, `Nieruchomosci-online`, `OLX`).
- **Warstwa Silver (`silver_listings`)**: Widok SQL normalizujący ceny, metraże, pokoje, piętra, geolokalizację (lat/lon) oraz opisy.
- **Warstwa Gold (`gold_listings`)**: Widok SQL dokonujący deduplikacji międzyportalowej (łączący to samo ogłoszenie z wielu portali w 1 rekord) oraz oznaczający nowe ogłoszenia (`is_new_listing`).
- **Audyt Kompletności (`run_audit`)**: Tabela przechowująca informacje o liczbie ofert oczekiwanych vs pobranych dla każdego zrzutu (`run_id`).
- **Wyceny Referencyjne RCN (`src/rcn_client.py`)**: Integracja z Rejestrem Cen Nieruchomości m.st. Warszawy, wyliczająca mediany (P50), średnie cen oraz odchylenia procentowe.

### Ograniczenie:
Prezentacja wyników opiera się wyłącznie na skrypcie CLI `main.py` generującym pliki Markdown do katalogu `historia/`.

---

## 2. Analiza Wymagań Użytkownika

| Wymaganie | Koncepcja Realizacji w UI | Wpływ na Backend / Bazę |
| :--- | :--- | :--- |
| **1. Dynamiczne zmienianie filtrów (`kryteria.md`)** | Panel boczny z filtrami (cena, metraż, pokoje, piętro, winda, rynek, typ sprzedawcy, dzielnice). Zmiana filtrów od razu odpytuje widok Gold z parametrami WHERE w SQLite. | Endpoint `GET /api/listings` przyjmujący parametry filtrów i zwracający przefiltrowane oferty z obliczonym RCN. Endpoint `POST /api/criteria` do zapisu stanu do pliku `kryteria.md`. |
| **2. Przeglądanie ofert z linkami** | Karty ofert z bezpośrednimi odnośnikami do wszystkich portali, w których oferta występuje (np. Otodom, Gratka, Adresowo). Podgląd kluczowych parametrów, wskaźnika okazji RCN (zielony/żółty badge) i nowości. | Wykorzystanie pola `source_portals_list` i `url` z widoku `gold_listings`. |
| **3. Podsumowanie danych z każdej z warstw** | Sekcja "Medallion Pipeline Health":<br>• Bronze: suma pobranych ofert per portal + audyt kompletności<br>• Silver: liczba poprawnie znormalizowanych rekordów<br>• Gold: liczba unikalnych ofert po scaleniu duplikatów. | Endpoint `GET /api/layers/summary` agregujący dane z `bronze_listings`, `run_audit`, `silver_listings` i `gold_listings`. |
| **4. Historyczne statystyki poprzednich runów** | Selektor runów w nagłówku + zakładka analityczna prezentująca trendy liczby ofert i średnich cen dla poszczególnych `run_id`. | Endpoint `GET /api/runs` zwracający listę unikalnych `run_id` z datami i wolumenem. |
| **5. Data ostatniego odświeżenia danych** | Widoczny element w nagłówku: data i dokładna godzina ostatniego zrzutu w Bronze, identyfikator runu oraz status połączenia. | Endpoint `GET /api/status` zwracający `last_scraped_at` i `run_id`. |
| **6. Nowoczesna aplikacja w React** | SPA w React (Vite) ze starannie dobraną typografią, czytelną hierarchią wizualną, responsywnością i brakiem niepotrzebnych ozdobników. | Lekki serwer FastAPI w Pythonie (lub Flask/Uvicorn) komunikujący się bezpośrednio z lokalnym SQLite. |
| **7. Lokalna baza danych** | Działanie w 100% lokalne w oparciu o `data/listings.db`. | Brak konieczności instalacji zewnętrznych baz (Postgres/Cloud). |

---

## 3. Proponowana Struktura Plików

```
wyszukiwarka-nieruchomosci/
├── src/
│   ├── api.py                   # FastAPI REST API serwujące dane z SQLite i kryteria.md
│   ├── config.py                # Istniejący CriteriaConfig
│   ├── db.py                    # Istniejący DatabaseManager
│   ├── deduplicator.py          # Istniejący Deduplicator
│   ├── rcn_client.py            # Istniejący RCNClient
│   └── report_generator.py      # Istniejący ReportGenerator
├── web/                         # Aplikacja React (Vite)
│   ├── package.json
│   ├── vite.config.js
│   ├── src/
│   │   ├── main.jsx
│   │   ├── App.jsx
│   │   ├── index.css            # Dopracowany system stylów
│   │   ├── components/
│   │   │   ├── Header.jsx       # Data odświeżenia, selektor run_id, status
│   │   │   ├── LayerSummary.jsx # Kafelki warstw Bronze / Silver / Gold + Audyt
│   │   │   ├── FilterBar.jsx    # Suwaki i przełączniki filtrów
│   │   │   ├── ListingCard.jsx  # Karta pojedynczej oferty ze wskaźnikami i linkami
│   │   │   ├── ListingsGrid.jsx # Siatka / Tabela ofert
│   │   │   └── RunHistory.jsx   # Widok historycznych statystyk zrzutów
│   │   └── services/
│   │       └── api.js           # Klient fetch do lokalnego backendu
├── run_ui.sh                    # Skrypt startowy (uruchamia backend API + vite dev server)
├── kryteria.md
└── main.py
```

---

## 4. Wnioski i Następne Kroki

Przygotowany proposal w pliku [proposal.md](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-react-ui/proposal.md) zawiera pełną specyfikację wymagań, opcje architektoniczne oraz plan wdrożenia. Kolejnym krokiem po zatwierdzeniu kierunku przez użytkownika będzie refinement i wygenerowanie dokumentu technicznego `design.md` oraz listy zadań `tasks.md`.
