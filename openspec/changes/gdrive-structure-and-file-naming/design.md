# Projekt techniczny: struktura Google Drive i konwencja nazw plików

Skrót decyzji projektowych. Pełne uzasadnienia i historia: [`analysis/`](./analysis/), wyniki planowania: [`reports/`](./reports/). Zakres i kryteria akceptacji: [proposal.md](./proposal.md), zadania: [tasks.md](./tasks.md).

## 1. Źródła prawdy

Dokumenty `analysis/` powstawały kolejno i częściowo sobie przeczą. Obowiązuje następująca kolejność:

| Temat | Obowiązuje | Zastępuje |
|---|---|---|
| Drzewo katalogów i mapowanie folderów | [09 — review](./analysis/09-review-katalogow-i-mapowania-gdrive.md) (§4–6) | drzewo i mapa z [06](./analysis/06-optymalna-struktura-i-procesy-zarzadzania.md), [07](./analysis/07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md) |
| Nazwy plików | [10 — konwencja](./analysis/10-konwencja-nazewnictwa-plikow.md) | tabela wzorców w 06 §3.2 (spacje wokół ` - `) |
| Mapowanie 52 plików z roota | 07 §3, z korektami 09 | — |
| Bezpieczeństwo wykonania | [SAFETY.md](./scripts/gdrive_migration/SAFETY.md) | uwagi o rollbacku w 08 |
| Stan planowania | [raport 12](./reports/12-poprawiony-dry-run-i-plan-bezpiecznej-migracji.md) | [raport 11](./reports/11-raport-dry-run-migracji-2026-10-13.md) (błędny, historyczny) |

Dokumenty `00`–`05` to historia diagnozy z września 2026 (dane: 77 498 plików, 49 plików w roocie) i nie są instrukcjami wykonawczymi.

## 2. Decyzje

**D1. Porządkowanie per folder, struktura i nazwy razem (zmiana z 2026-10-24).** Pierwotnie dwa niezależne etapy (A: foldery, B: nazwy plików) ze skryptowym wykonaniem. Obecnie każdy folder z root przechodzi cały cykl — struktura, przeniesienia i nazwy plików — w jednym półautomatycznym przebiegu z akceptacją użytkownika; małe, pojedyncze i weryfikowane po ID kroki zastępują oddzielne dzienniki etapów.

**D2. Przemianowanie źródeł przed tworzeniem celów.** Istniejące foldery główne zmieniają nazwę *w miejscu* (zachowane ID, uprawnienia i skróty); nowe foldery powstają tylko tam, gdzie nic nie jest przemianowywane. Planer uwzględnia planowane rename'y w wirtualnym indeksie, więc nie powstają równoległe drzewa.

**D3. Kontekst przed rodzajem dokumentu.** Osoba, obiekt (lokal, auto) lub projekt (firma, rok) ma pierwszeństwo przed typem dokumentu. Dlatego zostają osobne gałęzie dzieci w Zdrowiu, Kuba w Rodzinie, `Pod-Strzecha-7`, `VW-Golf-Opole`, firmy i lata w Pracy. Dokument ma jedno miejsce podstawowe, ewentualnie skrót w drugim — bez rozchodzących się kopii.

**D3a. Skróty tylko za zgodą (decyzja z 2026-10-21). Dokument lub folder pasujący do kilku kategorii ma jedno miejsce podstawowe; skrót w drugim miejscu powstaje wyłącznie na wyraźną decyzję użytkownika, osobno dla każdego przypadku. Co do zasady skrótów nie mnożymy. Wyjątek zatwierdzony: skrót do folderu zdrowia danej osoby w jej podfolderze w `02 👪 Rodzina` oraz skrót do dokumentów zdrowotnych z `Edukacja Dzieci`.

**D4. Niezrozumiała nazwa to powód do przeglądu, nie do usunięcia.** Niepewne pliki trafiają do `Inbox/Do-Przejrzenia` lub `…/Do-Przypisania`. Nie ma automatycznego usuwania, deduplikacji ani kasowania zbiorów na podstawie nazwy (Chrome, Gems, backupy, hasła, Takeout).

**D5. Folder `25📄 Paweł - dokumenty` rozbijany w dwóch krokach.** Najpierw całe rozpoznane podfoldery (13) trafiają do dziedzin z zachowaniem pochodzenia (`Import-z-25`); dopiero potem selektywnie włączane są pojedyncze pliki. Osiem plików luzem w 25 idzie do `Inbox/Do-Przejrzenia/Pliki-z-25`. Folder 25 usuwa się, gdy każdy element ma świadomy cel.

**D6. Tryb półautomatyczny (2026-10-24).** Claude czyta Drive przez konektor, proponuje zmiany i wykonuje je dopiero po akceptacji użytkownika (skróty i usunięcia — osobna zgoda); decyzje i stan zapisuje `tracker.md`. `planner.py` (plan `v2`, OAuth `drive.metadata.readonly`) zostaje narzędziem pomocniczym tylko do odczytu; stary `apply` jest wyłączony, a nowy wykonawca nie jest budowany (wznowienie tylko przy operacjach masowych).

**D7. Takeout i zdjęcia poza zakresem.** Zdjęcia zostały przeniesione do Google Photos. Folder `Takeout` (~536 GB) jest przejściowy i obsługiwany ręcznie (pobranie offline, weryfikacja, usunięcie); ta zmiana go nie rusza. Backup przed migracją robi użytkownik ręcznie przez Takeout — bez skryptu.

**D8. Nie traktować wielkości ani „Zero-Root" jako kryterium poprawności.** Cel 15–20 GB i pusty root z dokumentu 06 są pożądane, ale nie warunkiem akceptacji (09 §8). Inbox ma cotygodniowy przegląd, bez automatycznego kasowania po 7 dniach.

## 3. Docelowa struktura (poziom 1–2)

Konwencja nazw folderów (decyzja z 2026-10-21, zastępuje myślniki z 06/07/09): **`NN <emoji> Nazwa Ze Spacjami`** — dwucyfrowy numer, dokładnie jedno emoji (jeden punkt kodowy, bez selektora wariantu U+FE0F i bez sekwencji ZWJ), nazwa ze spacjami i **z polskimi znakami**. Identyfikatorem jest pełna nazwa lub ID, nie prefiks (numery mogą się powtarzać). Poniższa lista to stan root-a na Dysku.

**Podfoldery** (decyzja z 2026-10-21): `NN Nazwa Ze Spacjami` — numer opcjonalny (tam, gdzie kolejność ma znaczenie), **bez emoji**, ze spacjami i z polskimi znakami, np. `01 Tożsamość`, `02 Majątek i Akty Notarialne`, `91 Hasła`. Nazwy podfolderów w drzewie 09 §4 są orientacyjne i zapisane w starej konwencji (myślniki, bez polskich znaków) — przy każdym porządkowanym katalogu stosować nową.

```
00 📥 Inbox
01 🔒 Poufne Dokumenty
02 👪 Rodzina
03 🏥 Zdrowie
04 🏫 Edukacja Dzieci
05 💰 Finanse
07 🏢 Praca i Projekty
08 🌂 Ubezpieczenia            (istnieje na Dysku; 09 rozprasza polisy do aut/nieruchomości/podróży — do decyzji)
10 🏠 Mieszkanie i Nieruchomości
11 🏡 Lewickie i Pokój         (09: rozdzielić, Pokój do potwierdzenia)
12 🚗 Pojazdy
20 📚 Wiedza i Rozwój
21 🎵 Audio i Multimedia
22 🏃 Sport i Aktywność
23 🎮 Gry i Hobby
24 🧳 Podróże i Wyjazdy
80 📱 Aplikacje i Synchronizacja
90 📦 Archiwum
95 💽 Google Takeout          przejściowy
99 🚮 Do Usunięcia             tylko zasoby świadomie wybrane
```

Brak w rootcie względem 09: `Dokumenty Osobiste` (Kariera i CV, Certyfikaty) — do decyzji, czy powstaje jako folder główny. `Dziennik` zostaje w `01 🔒 Poufne Dokumenty` (decyzja z 2026-10-21; zastępuje 09 §4).

Archiwum to głównie *stan sprawy wewnątrz dziedziny* (stare PIT-y zostają w Finansach); `90 📦 Archiwum` służy kompletnym zbiorom i kopiom urządzeń.

Poufność: folder `01 🔒 Poufne Dokumenty` jest granicą dostępu, ale **nie szyfruje**. Skany tożsamości wymagają osobnej kontroli uprawnień i ewentualnego szyfrowania po stronie klienta; przeniesienie zachowuje ID, nie gwarantuje zachowania ani ograniczenia dostępu. Hasła i kody 2FA należą do menedżera haseł.

## 4. Konwencja nazw plików (Etap B)

Wzorzec: `YYYY-MM-DD Temat Opis.ext`, warianty `YYYY-MM …`, `YYYY …`, `Temat Opis.ext` (decyzja z 2026-10-21: spacje zamiast myślników, polskie znaki zachowane — jak w folderach). Szczegóły: [10](./analysis/10-konwencja-nazewnictwa-plikow.md).

- **Zbędne spacje** (decyzja z 2026-10-21): z każdej nazwy pliku usuwamy spacje wiodące i końcowe (także przed rozszerzeniem, np. `Michał .pdf` → `Michał.pdf`) oraz podwójne spacje. Dotyczy wszystkich plików, także tych spoza zakresu Etapu B.
- **Znaki usuwane** (decyzja z 2026-10-22): z nazw plików i folderów usuwamy `/` `\` oraz wszelkie nawiasy (`()` `[]` `{}` `<>`), cudzysłowy (`"` `'` `„` `”` `«` `»`), średniki, dwukropki, przecinki, wykrzykniki, znaki zapytania i podobną interpunkcję, a także podkreślniki oraz sufiksy aplikacyjne (np. `_encrypted_`). Wyjątek: `/` między cyframi w zakresie lub roku szkolnym zamieniamy na `-` (`2021/22` → `2021-22`, `Sezon 25/26` → `Sezon 25-26`). Zostają litery (z polskimi znakami), cyfry, spacja, `-` i kropka przed rozszerzeniem.
- **Rozszerzenia**: plik rozpoznany po MIME, a bez rozszerzenia w nazwie, dostaje rozszerzenie rzeczywiste (np. `.pdf`).
- **Imiona w nazwach**: jedna forma na osobę — `Natalka` (nie `Natalia`); `mama` małą literą; w nazwach dokumentów osobistych `Imię` bez nazwiska, chyba że trzeba rozróżnić osoby.
- **Duplikaty nazw** w jednym folderze to osobne dokumenty do rozpoznania (inna osoba lub wersja), nie do nadpisania; przy identycznej treści zostaje wersja większa/pełniejsza.
- Separator: pojedyncza spacja między słowami i po dacie; myślniki tylko w dacie i w identyfikatorach; wzorzec `Typ - Osoba` dla dokumentów osobistych zostaje; bez podkreślników; polskie znaki zachowane (NFC); zachowanie akronimów i identyfikatorów.
- Data z dowodu w nazwie lub treści dokumentu; data utworzenia/modyfikacji w Drive tylko jako ostateczność dla materiałów bez żadnej daty (decyzja z 2026-10-22; dokładność daty zapisana w raporcie), nigdy gdy dowód istnieje; dwucyfrowy rok (`30.05.23`) wymaga decyzji; bez wymyślonych dni/miesięcy.
- Rozszerzenie rzeczywiste (także wieloczłonowe); dokumentom natywnym Google nie dopisujemy `.gdoc/.gsheet/.gslides` — typ z MIME.
- `V2` → `v2` tylko gdy potwierdzone; brak `v1` z domysłu; `(1)` nie dowodzi duplikatu.
- **Wyjątek: zdjęcia jako materiał szkoleniowy** (decyzja z 2026-10-22): zdjęcia, które są materiałem szkoleniowym (np. analiza techniki, wideoanaliza, `05 Tenis/…/2025-08-25 PIT obóz zdjęcia`), a nie pamiątką, mogą zostać w Drive i zachować oryginalne nazwy plików (`IMG_*`, `_DSC*`); folder wydarzenia nazywamy zgodnie z konwencją. Pozostałe zdjęcia-pamiątki są poza zakresem (D7 — Google Photos).
- Kolizje (też po NFC, też między propozycjami) blokują pozycję; bez auto-numeracji.
- Domyślnie poza zakresem: kopie aplikacyjne, Takeout, foldery zarządzane przez aplikacje, skróty, pliki spoza My Drive, pliki bez prawa zmiany nazwy.
- Raport `stara → nowa`: ID, rodzic, MIME, reguła, źródło i dokładność daty, konflikt, status `unchanged/proposed/blocked/excluded`, decyzja. Raport zawiera prywatne metadane — poza Gitem.

## 5. Narzędzia

```
scripts/gdrive_migration/   plan (read-only) → plan.json v2 + dry_run_report.md
  migrate.py   CLI: plan | verify | apply (odmawia)
  planner.py   make_plan(), mapowanie z 07/09, wykrywanie kolizji
  test_planner.py  12 testów na danych syntetycznych
scripts/analysis/           jednorazowe skrypty czytające lokalną bazę DriveFS (wrzesień 2026)
```

- OAuth poza repozytorium: `~/.config/gdrive-migration/` (`GDRIVE_MIGRATION_CONFIG`). Pliki robocze (`plan.json`, `inventory.json`, `dry_run_report.md`) i `analysis/data/` są lokalne i ignorowane przez Git.
- **Planer** pracuje na rzeczywistym ID roota (nie aliasie `root`), ogranicza skan do potwierdzonych potomków My Drive (bez skrótów i Shared Drives), dopasowuje nazwy dokładnie (NFC), blokuje duplikaty źródeł i kolizje celów.
- **Wykonawca `apply v2`** (wycofany z planu 2026-10-24; poniżej wymagania na wypadek operacji masowych): tylko zatwierdzony plan v2 ze sprawdzeniem skrótu; dziennik zapisywany trwale przed i po każdej operacji (ID, poprzednia nazwa i rodzice, cel, odpowiedź API); zatrzymanie partii przy rozbieżności `before` lub kolizji; weryfikacja każdej operacji po ID; idempotentne wznowienie; warunkowe cofanie w odwrotnej kolejności. Test na osobnym koncie Drive przed użyciem produkcyjnym. Wymagania: [SAFETY.md](./scripts/gdrive_migration/SAFETY.md).
- Nazwy plików (§4) stosowane są przy przeglądzie folderu wg reguł z tego dokumentu; osobny moduł normalizatora jest opcjonalny.

## 6. Stan i ryzyka

Dry-run v2 (raport 12): 42 383 pozycje w My Drive, 28 folderów i 53 pliki w roocie; 77 operacji (11 rename'ów, 22 nowe foldery, 44 przeniesienia); 36 pozycji `blocked`; liczby dotyczą skryptowego dry-run; faktyczne zmiany wykonywane są ręcznie/półautomatycznie — foldery `01`–`05` zakończone (stan: `tracker.md`).

| Ryzyko | Mitygacja |
|---|---|
| Mapa 07 opisuje 52 pliki, root ma 53; część dat i opisów wynika z kontekstu | nieznane pozycje idą do przeglądu; brak dat z domysłu |
| Przeniesienie zrywa zapis z aplikacji (Notability, Chrome, skaner paragonów) | test nowego zapisu przed likwidacją starego miejsca; skrót jako punkt wejścia |
| Zmiana rodzica zmienia dziedziczone uprawnienia | audyt uprawnień źródła i celu przed zapisem; zapis `before` |
| Rollback niemożliwy po późniejszych zmianach | cofanie tylko warunkowe; backup Takeout ręcznie; nie obiecujemy odwracalności |
| Zmiana nazw → kolizje po normalizacji spacji i NFC | blokada kolizji, wyjątki dla zasobów aplikacyjnych, review |
| Takeout nie odtwarza Dysku 1:1 (uprawnienia, wersje) | traktować jako eksport danych, nie jako rollback |

## 7. Otwarte decyzje użytkownika

Bramka zbiorcza zniesiona (2026-10-24); poniższe pozycje rozstrzygamy na bieżąco przy przeglądzie właściwego folderu: przypisanie karty szkolnej (które dziecko), energii z folderu `16🏡Pokój` i `06. Działka Dom` (który obiekt), `Terapia M.`, folderów Chrome i `91🔑Hasła` (treść), dokumentów tożsamości (uprawnienia, szyfrowanie), `Obsidian` i `Gemini Gems` (czy używane), `89 Sterta`, ośmiu plików luzem w 25, projektów Snowflake/HSBC; punkty zapisu aplikacji; potwierdzenie ręcznego backupu.
