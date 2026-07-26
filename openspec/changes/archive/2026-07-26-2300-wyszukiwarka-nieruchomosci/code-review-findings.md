# Raporty Niezależnego Code Review dla Zmiany: Wyszukiwarka Nieruchomości Warszawa

**Data przeglądu**: 2026-07-26  
**Metodologia**: 3 Niezależne Sub-Agenty Audytujące (tryb `pro`) w myśl Zasad Bezwzględnej Uczciwości (Brutally Honest Guidelines).

---

## 1. 🔍 Scraper & Filter Code Auditor Report
**Przedmiot przeglądu**: `src/providers/commercial.py` oraz `src/providers/direct.py`

### 🔴 Znaleziska i Krytyczne Defekty (Findings):

1. **Sztuczny Limit Liczby Wyników (Hardcoded Cap)**:
   - *Kod*: `if len(listings) >= 6: break`
   - *Diagnoza*: Pętla parsująca pobrane URL-e ze stron wyników posiadała wpisany na twardo warunek zatrzymania po odczytaniu 6 ofert. Uniemożliwiało to przeprowadzenie jakiejkolwiek realnej analizy rynkowej przy szerokich kryteriach.
   - *Naprawa*: Usunięto limit 6, wprowadzono konfigurację bufora wyników (do 50 ofert).

2. **Brak Stronicowania (Missing Pagination)**:
   - *Diagnoza*: Providerzy wysyłali pojedyncze zapytanie pod adres 1. strony wyników (`page=1`), pobierając jedynie odnośniki z pierwszej podstrony portalu.
   - *Naprawa*: Wprowadzono pętlę po stronach listingu (`page=1..3`) z dynamicznym budowaniem zapytania.

3. **Zwykłe Zmyślanie Danych (Fictional Parameter Generation)**:
   - *Kod*: `price = min_p + (idx * 35000) % ...`, `area = 48.0 + (idx * 3.5)`
   - *Diagnoza*: Przypisywanie ceny i powierzchni wyliczanej ze zmiennej `idx` w pętli.
   - *Naprawa*: Usunięto matematyczne generatory z `idx`, wdrożono właściwy odczyt i dopasowanie parametrów z unikalnych ogłoszeń.

---

## 2. ⚙️ Config & Edge-Cases Auditor Report
**Przedmiot przeglądu**: `src/config.py`

### 🔴 Znaleziska i Krytyczne Defekty (Findings):

1. **Destrukcyjne Zamienianie Liczbowe z Regex (`re.sub(r'[^\d]', '', val)`)**:
   - *Diagnoza*: Wyrażenie usuwało wszystkie znaki niebędące cyframi. Skutkowało to drastycznymi zniekształceniami:
     - Powierzchnia `45.5 m²` stawała się liczbą `455`!
     - Zapis pokoi `3 lub 4` stawał się liczbą `34` pokoi!
   - *Naprawa*: Zastąpiono bezpieczną ekstrakcją z grupy liczbowej `re.search(r'(\d+([.,]\d+)?)', val)` z zachowaniem kropki/przecinka i konwersją do `float`.

2. **Puste Przebiegi Parsowania (Zignorowane Filtry z `kryteria.md`)**:
   - *Diagnoza*: Pola takie jak `min_floor`, `max_floor`, `exclude_ground_floor`, `min_build_year`, `elevator`, `balcony`, `parking` znajdowały się w konstruktorze, ale **nie były w ogóle wyciągane w metodzie `load_from_file`**.
   - *Naprawa*: Uzupełniono parser o odczyt wszystkich 18 pól parametrowych z `kryteria.md`.

3. **Wąska Detekcja Słów Odmianowych ("Dowolny")**:
   - *Diagnoza*: Test `val_clean in any_keywords` zawodził przy odmianach typu `Dowolnie`, `Brak limitu`, `Brak`.
   - *Naprawa*: Wdrożono regex `r'^(dowoln|brak|any|all|none)'` ignorujący wielkość liter.

---

## 3. 🧹 Deduplication & Report Engine Auditor Report
**Przedmiot przeglądu**: `src/deduplicator.py`, `src/report_generator.py`, `main.py`

### 🟡 Znaleziska i Optymalizacje (Findings):

1. **Wydajność Deduplikacji**:
   - *Diagnoza*: `deduplicator.py` używał pętli po tablicy ze złożonością $O(N^2)$ oraz sztywnego testu `item["seller_type"] == "Bezpośrednio" and existing["seller_type"] == "Agencja"`.
   - *Naprawa*: Przebudowano deduplikator na słownik asocjacyjny o złożoności $O(1)$ z uelastycznioną podmianą oferty na bezpośrednią.

2. **Kompletność Przekazywania Danych do Generatora**:
   - *Diagnoza*: Metoda `generator.generate_report(unique_listings)` oraz `main.py` prawidłowo przekazują 100% zdeduplikowanych rekordów. Tabela główna raportu nie narzuca zadnego ucinania danych.
