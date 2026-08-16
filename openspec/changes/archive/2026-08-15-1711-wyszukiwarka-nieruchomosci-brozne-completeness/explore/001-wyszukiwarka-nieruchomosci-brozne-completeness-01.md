# Dokument Eksploracyjny OpenSpec: Weryfikacja Kompletności Pobierania w Warstwie Bronze (`wyszukiwarka-nieruchomosci-brozne-completeness`)

**Kod Zmiany**: `wyszukiwarka-nieruchomosci-brozne-completeness`  
**Data**: 2 Sierpnia 2026  
**Wersja Dokumentu**: `001-wyszukiwarka-nieruchomosci-brozne-completeness-01.md`  
**Status**: W Trakcie Eksploracji (In Exploration)  
**Dokumenty Referencyjne**:
- `file:///Users/pawel/git/gen-ai-orchestrator/wyszukiwarka-nieruchomosci/kryteria.md`
- `file:///Users/pawel/git/gen-ai-orchestrator/.ai/guidelines/brutally-honest-rules.md`

---

## 1. Cel Zmiany i Wymagania Biznesowe

Głównym celem zmiany jest **bezwzględne zagwarantowanie i weryfikacja 100% kompletności danych zapisywanych w warstwie Bronze** dla każdego uruchomienia.

### Główne Problemy i Potrzeby:
1. **Ryzyko Niepełnego Zrzutu (Partial Fetching Risk)**:
   - Dotychczas pobieranie bazowało na sztywnej liczbie stron (`max_pages`).
   - W serwisie Adresowo.pl na Ursynowie znajduje się np. **133-136 ofert**, a pobranie tylko pierwszych stron zapisywało jedynie część bazy.
2. **Dynamiczny Odczyt Licznika Ofert z Portali**:
   - **Adresowo.pl**: Odczyt całkowitej liczby ofert z tekstu nagłówkowego/odznaki strony (`"133 oferty"` / `"Zobacz 133 aktualnych mieszkań"` z linku `ursynow-Q/`).
   - **Otodom.pl**: Odczyt wartości `searchAds.pagination.totalCount` z natywnej struktury `__NEXT_DATA__`.
3. **Automatyczna Paginacja do 100% Pokrycia**:
   - Pętla pobierająca musi kontynuować paginację dopóki liczba zapisanych ogłoszeń nie osiągnie całkowitej liczby zadeklarowanej przez portal.
4. **Raportowanie i Audyt Kompletności**:
   - Dodanie w nagłówku raportu oraz w logach CLI jasnego wskaźnika kompletności (np. `Otodom: 126/126 (100%)`, `Adresowo: 133/133 (100%)`).

---

## 2. Metoda Ekstrakcji Liczników Ofert z Portali

### 🌐 Adresowo.pl (Link: `https://adresowo.pl/mieszkania/warszawa/ursynow-Q/`)
W kodzie HTML strony kategorii Adresowo.pl pod adresem `ursynow-Q/` licznik znajduje się w badge'u oraz w treści paragrafu intro:
```python
# Odczyt liczby z badge'a "133 oferty" lub z tekstu intro
count_match = re.search(r'(\d+)\s*oferty', html, re.IGNORECASE) or re.search(r'Zobacz\s*(\d+)\s*aktualnych', html, re.IGNORECASE)
expected_total = int(count_match.group(1)) if count_match else None
```

### 🟧 Otodom.pl (Link z parametrami w `__NEXT_DATA__`)
Struktura JSON z tagu `<script id="__NEXT_DATA__">` zawiera bezpośrednie pole:
```python
total_count = data['props']['pageProps']['data']['searchAds']['pagination']['totalCount']
```

---

## 3. Algorytm Automatycznej Paginacji i Walidacji

```python
# Przykładowa pętla w Providerze
page = 1
saved_count = 0
expected_total = None

while True:
    html = fetch_page(page)
    if expected_total is None:
        expected_total = extract_expected_total(html)
        
    page_items = parse_items(html)
    if not page_items:
        break
        
    for item in page_items:
        save_to_bronze(item)
        saved_count += 1
        
    if expected_total and saved_count >= expected_total:
        break
        
    page += 1
```

---

## 4. Nazywanie Niepewności i Ograniczeń (Brutally Honest Assessment)

1. **Różnice Liczników w Czasie Rzeczywistym**:
   - **[Hipoteza/Domysł]**: Licznik ofert na portalu (np. 133) może ulegać minimalnym wahaniom w trakcie stronicowania, jeśli nowe oferty zostaną dodane w trakcie zrzutu.
   - **Mitigacja**: Paginowanie kontynuowane jest do momentu pobrania wszystkich stron lub osiągnięcia liczby zadeklarowanej na stronie 1.

2. **Oferty Duplikowane na Liście Portalu**:
   - Jeśli portal zawiera duplikaty wewnętrzne na liście wyników, unikalnych zapisanych rekordów może być nieznacznie mniej niż `totalCount`. Warstwa Bronze przechowuje `UNIQUE(run_id, source_portal, external_id)`, gwarantując brak duplikatów wewnątrz jednego uruchomienia.

---

## 5. Następne Kroki

- [x] Utworzenie dokumentu eksploracji `explore/001-wyszukiwarka-nieruchomosci-brozne-completeness-01.md`.
- [ ] Przygotowanie propozycji `proposal.md`.
- [ ] Opracowanie specyfikacji technicznej `design.md`.
- [ ] Przygotowanie planu zadań `tasks.md`.
