# OpenSpec Proposal: Architektura Danych ELT (Bronze / Silver / Gold) dla Wyszukiwarki Nieruchomości

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-data-arch`  
**Data**: 27 Lipca 2026  
**Status**: Propozycja (Proposal)  
**Dokumenty Referencyjne**: 
- `file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/wyszukiwarka-nieruchomosci-data-arch/explore/001-wyszukiwarka-nieruchomosci-data-arch-01.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Dlaczego Ta Zmiana Jest Potrzebna? (Problem Statement)

Dotychczasowy model pozyskiwania danych o nieruchomościach polegał na bezpośrednim nakładaniu wąskich parametrów filtrujących (cena, pokoje, winda, piętro) w zapytaniach API lub parametrach URL wysyłanych do portali ogłoszeniowych (np. Otodom, OLX). 

Taki model ujawniał szereg istotnych wad architektonicznych:
1. **Utrata Kontekstu i Brak Retencji Danych**: Odrzucenie oferty na etapie HTTP uniemożliwiało jej późniejsze przeanalizowanie przy zmianie kryteriów wyszukiwania (np. rozszerzenie budżetu z 1.2M na 1.3M PLN wymuszało ponowne skrapowanie całego serwisu).
2. **Niemożność Deduplikacji Międzyserwisowej**: Portale często zawierają to samo ogłoszenie od różnych agencji z inaczej sformułowanym tytułem lub inną ceną. Brak surowego archiwum uniemożliwiał wykrywanie duplikatów.
3. **Brak Historii Zmian Ceny**: Brak trwałego surowego pasma danych uniemożliwiał analizę trendów obniżek cen w czasie dla danej nieruchomości.

---

## 2. Proponowane Rozwiązanie (Proposed Solution)

Przechodzimy na elastyczną architekturę **ELT (Extract, Load, Transform)** opartą o bazę danych **SQLite** z podziałem na warstwy jakościowe (Medallion Architecture: Bronze, Silver, Gold):

### 🥉 Warstwa Bronze (Surowe Zdarzenia / Zrzut JSON)
- Pobieranie ogłoszeń wyłącznie w oparciu o szeroki parametr terytorialny (np. **Miasto: Warszawa**).
- Zapis pełnego surowego obiektu JSON (`raw_payload`) lub fragmentu HTML (`__NEXT_DATA__`) bezpośrednio do tabeli `bronze_listings`.
- Brak walidacji i odrzucania rekordów w kodzie skrapera.

### 🥈 Warstwa Silver (Parsowanie i Filtracja Biznesowa)
- Wyciąganie pól z surowego JSON-a z wykorzystaniem funkcji `json_extract()` dostępnych w rozszerzeniu JSON1 SQLite.
- Nakładanie filtrujących kryteriów biznesowych zdefiniowanych w `kryteria.md` (np. cena 800k - 1.2M PLN, 3 pokoje, piętro 1-8 bez parteru, winda, Ursynów).

### 🥇 Warstwa Gold (Deduplikacja i Analityka)
- Generowanie unikalnego klucza nieruchomości (w oparciu o geolokalizację z zaokrągleniem do ~111m, metraż oraz liczbę pokoi).
- Agregacja ofert z różnych portali, śledzenie historii zmian cen i generowanie końcowych raportów dla użytkownika.

---

## 3. Nazywanie Niepewności i Ograniczeń (Brutally Honest Assessment)

Zgodnie ze standardem `.ai/guidelines/brutally-honest-rules.md`, poniżej wprost punktujemy ryzyka techniczne i hipotezy wymagające weryfikacji:

1. **Paginacja Portali (Limity Pobierania)**:
   - **Fakt**: Portale ogłoszeniowe (Otodom/OLX) stosują sztywne limity paginacji (np. max 50 stron po 24/36 ofert, co daje limit ~1200-2000 ogłoszeń na zapytanie).
   - **Niepewność**: Liczba aktywnych mieszkań w całej Warszawie przekracza ten limit (szacunkowo 5 000 - 15 000 ogłoszeń).
   - **[Hipoteza/Domysł]**: Zapytanie portalu o "całą Warszawę" bez podziału spowoduje ucięcie wyników i pominięcie części ofert. Pobieranie w warstwie Bronze będzie wymagało zastosowania tzw. *Extraction Chunks* (np. podział na rynek pierwotny/wtórny lub podział na sub-dzielnice/zakresy cenowe na poziomie zapytania HTTP).

2. **Brakujące Pola w JSON (Kompletność Schematu)**:
   - **Niepewność**: Wykluczenie ostatniego piętra wymaga informacji o całkowitej liczbie pięter w budynku (`total_floors`). Część portali nie udostępnia tego pola w ustrukturyzowanym JSON-ie.
   - **[Hipoteza/Domysł]**: Sprawdzenie czy piętro jest ostatnie lub jaki jest stan prawny mieszkania (np. *spółdzielcze własnościowe z KW*) w części ogłoszeń będzie wymagało parsowania regexem treści opisów w języku naturalnym.

3. **Obliczanie Odległości (Geolokalizacja w SQLite)**:
   - **Fakt**: Kryterium odległości od stacji metra wymaga funkcji trygonometrycznych (wzór Haversine'a), które nie występują domyślnie w standardowym SQLite.
   - **Rozwiązanie**: Zarejestrowanie customowej funkcji C/Python w SQLite (`sqlite3.create_function`) lub wyliczanie dystansu na etapie przejścia Silver -> Gold w Pythonie.

---

## 4. Zakres Prac (Scope of Work)

- [ ] **Baza Danych**: Utworzenie tabeli `bronze_listings` oraz widoku/tabeli `silver_listings` w SQLite.
- [ ] **Moduł Ekstrakcji (Extract & Load)**: Dostosowanie skryptu pobierającego do zapisu surowych JSON-ów z podziałem na *Extraction Chunks*.
- [ ] **Moduł Transformacji (Transform)**: Zbudowanie logiki parsowania JSON1 i odzwierciedlenie filtru kryteriów w widoku SQL.
- [ ] **Moduł Deduplikacji (Gold)**: Algorytm deduplikacji ofert międzyserwisowych i obliczania wskaźnika cena/m².

---

## 5. Porównanie Opcji Architektonicznych (Architectural Trade-offs)

| Wariant Architektury | Zalety | Wady / Trade-offy | Rekomendacja |
| :--- | :--- | :--- | :--- |
| **Opcja 1: Czyste widoki SQL (`CREATE VIEW`)** | Brak duplikacji danych, natychmiastowe odzwierciedlenie zmian w Bronze. | Wysokie obciążenie CPU przy dużych wolumenach JSON. | Dobra na start (MVP). |
| **Opcja 2: Materializowane tabele Silver (`CREATE TABLE AS`)** | Bardzo wysoka wydajność zapytań dzięki indeksowaniu kolumn `price`, `district`. | Wymaga uruchamiania procesu odświeżania tabeli Silver po każdym pobraniu. | **Rekomendowana** |
| **Opcja 3: Parsowanie Python -> Tabela SQL** | Wyciąganie skomplikowanych pól z tekstu opisów za pomocą regexów przed zapisem. | Wyższa skomplikowanie kodu Pythona, mnóstwo kolumn w tabeli. | Opcja alternatywna. |
