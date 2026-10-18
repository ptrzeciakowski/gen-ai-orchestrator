# 09: Review propozycji katalogów i mapowania Google Drive

- **Data sesji:** 2026-10-12, Europe/Warsaw (CEST); odczyt danych do review: 07:33:39.
- **ID wątku Codex:** `01a12e8f-7786-70fa-a3e8-7a2a72988071` (identyfikator zwrócony przez narzędzie podglądu pliku).
- **Autor review:** Codex.
- **Baza repozytorium:** commit `1e22804`; materiały 00–08, zapisane zestawienia JSON i kontekst dla agentów.
- **Numeracja:** kolejna transza po dokumencie 08; dwucyfrowy prefiks zgodny z wcześniejszymi plikami tego explore-a i wskazaniem użytkownika.
- **Zakres końcowy:** architektura katalogów, mapowanie istniejących zasobów i kolejność reorganizacji. Migracja zdjęć jest zakończonym tematem i pozostaje poza rekomendacjami tego review.
- **Charakter dokumentu:** rekomendacja, bez zmian na Google Drive i bez nadpisywania wcześniejszych analiz.

## Zlecenie użytkownika

> Przejrzyj proszę gdrive analysis i zrób review zapisując rekomendację w kolejnym pliku explore.

**Doprecyzowanie zakresu:**

> Kontyynuuj, ale skup się na propozycji katalogów i mapowaniu mojego folderów na dysku google a nie na skrypcie do zdjęć. To już jest zakończony temat.

## 1. Rekomendacja główna

**Przyjąć układ dziedzinowy z dokumentu 07 jako punkt wyjścia, ale skorygować mapowanie przed reorganizacją.** Największym problemem nie jest liczba katalogów ani emoji, lecz przypisania, które usuwają kontekst osoby, nieruchomości, pracodawcy albo historycznej wersji zasobów.

Rekomenduję zachować osobne obszary Rodzina, Edukacja dzieci, Zdrowie, Finanse, Praca, Mieszkanie, Lewickie i Pojazdy. Do tego potrzebne są prosty Inbox, obszar poufny, zasoby wiedzy, zainteresowania, dane aplikacji i archiwum. Nie rekomenduję nowej rundy projektowania całej numeracji ani wdrożenia pięciu wymiarów klasyfikacji jako pięciu zagnieżdżonych poziomów folderów.

Najważniejsze korekty:

1. Zachować Kubę oraz osobne gałęzie zdrowia Michała i Nadii; nie archiwizować osoby i nie spłaszczać dokumentacji tylko dla uproszczenia drzewa.
2. Nie scalać automatycznie energii z folderu Pokój z konkretnym mieszkaniem; najpierw potwierdzić, którego lokalu dotyczy.
3. Przenosić historyczne podfoldery z `25📄 Paweł - dokumenty` z zachowaniem ich pochodzenia, zamiast wymieszać je od razu z bieżącymi plikami.
4. Nie traktować `Gemini Gems`, obu folderów Chrome i pustego Obsidiana jako zasobów do automatycznej likwidacji.
5. Najpierw uporządkować i przemianować istniejące katalogi, potem mapować pliki do ostatecznych miejsc. Nie tworzyć równoległych folderów docelowych, które później mają powstać przez zmianę nazwy źródła.

## 2. Na czym opiera się ocena

Podstawą propozycji docelowej są [06 — architektura i procesy](06-optymalna-struktura-i-procesy-zarzadzania.md), [07 — mapa migracji](07-mapa-katalogow-i-istniejacych-plikow-do-nowej-struktury.md) i [08 — uprawnienia i nazewnictwo](08-uprawnienia-automatyzacja-i-dylemat-emoji.md). Starsze dokumenty 00–05 traktuję jako historię diagnozy, a nie równoległe instrukcje wykonawcze.

Sprawdziłem również [zestawienie szczegółowe](drive_dataset_complete.json) i [zestawienie analityczne](drive_analysis_data.json). Zawierają stan opisany jako wrześniowy: 28 katalogów głównych i 49 plików luzem. Dokument 07 opisuje październikowy stan z 52 plikami i innym zestawem folderów. Taka aktualizacja jest możliwa, ale w tym katalogu nie ma odpowiadającego jej nowego eksportu metadanych. **Nie przedstawiam zapisanej mapy jako zweryfikowanego aktualnego stanu konta.**

JSON zawiera nazwy bezpośrednich podfolderów i zagregowane liczby plików, nie pełny spis wszystkich 77 498 plików. Nie zawiera też audytu uprawnień. To wystarcza do wskazania luk w mapowaniu, ale nie do rozstrzygnięcia zawartości niejednoznacznych folderów.

W dalszych tabelach:

- **Przyjąć** — mapowanie ma logiczne oparcie w istniejącej strukturze.
- **Skorygować** — proponuję konkretną poprawkę do dokumentu 07.
- **Potwierdzić** — nazwa i agregaty nie wystarczają do bezpiecznego przypisania.

## 3. Najważniejsze uwagi do obecnej propozycji

| Priorytet | Ustalenie i źródło | Rekomendowana korekta |
| :--- | :--- | :--- |
| Wysoki | Dokument 07, wiersz 21, kieruje `05 Kuba` do archiwum rodziny. W JSON jest to osobna gałąź z 24 plikami; nie ma dowodu, że jest nieaktualna. | Zachować `Rodzina/Kuba`. Archiwizować zakończone sprawy, nie osobę na podstawie samej nazwy folderu. |
| Wysoki | Dokument 07, wiersz 23, scala Michała i Nadię do `Zdrowie/Dzieci`, a `Terapia M.` kieruje do archiwum. Nie wykazano zakończenia terapii ani pełnego przypisania do osoby. | Zachować `Zdrowie/Dzieci/Michal` i `Zdrowie/Dzieci/Nadia`. Terapię pozostawić jako osobny zbiór do potwierdzenia osoby i statusu. |
| Wysoki | Dokument 07 przypisuje `16🏡Pokój/Energia Elektryczna` do energii mieszkania Pod Strzechą. Pomija też osobne mapowanie `06🏠Mieszkanie/06. Działka   Dom`. | Zachować te zbiory oddzielnie do potwierdzenia nieruchomości. Nazwa obszaru nie dowodzi, że chodzi o ten sam lokal lub działkę. |
| Wysoki | Dokument 07, rozdział 2.1, opisuje całe `25/06. Praca` jako umowy i dokumenty formalne do CV. JSON wskazuje 5 416 plików w tej gałęzi. | Najpierw zachować ją pod `Praca/Historia/Import-z-25/06-Praca`. Dopiero przegląd zawartości wyodrębni formalne dokumenty do `Dokumenty-Osobiste/Kariera-i-CV`. |
| Wysoki | Dokument 07, wiersz 44 i etap 4, kieruje definicje `Gemini Gems` do Inboxa o krótkiej retencji. | Wielokrotnie używane prompty przechowywać w `Wiedza-i-Rozwoj/01-Inzynieria-Danych-i-AI/Prompty-i-Gems`. Najpierw sprawdzić, czy pierwotny folder jest używany przez aplikację. |
| Wysoki | Dokument 07 uznaje `Zapisane z Chrome (1)` za duplikat do kwarantanny. Dane pokazują 15 plików i 10,7 MB wobec 9 plików i 74,6 MB w drugim folderze. | Oba foldery traktować jako odrębne kolejki do przeglądu. Powtórzony tytuł folderu nie oznacza powielonej treści. |
| Średni | Pliki są kierowane do nowych miejsc w etapie 2 dokumentu 07, a przemianowanie źródłowych katalogów następuje dopiero w etapie 3. Niektóre cele powstają już w etapie 1. | Ustalić po jednym folderze docelowym dla każdego obszaru i najpierw przemianować źródła. Inaczej mogą powstać dwa katalogi o identycznej nazwie lub dwa równoległe drzewa. |
| Średni | `2026-Biezace` usuwa informację o firmie, a `Samochod-Drugi` zastępuje rozpoznawalny `VW Golf - Opole`. | Zachować kontekst: `Praca/Projekty/2026-HSBC`, `Praca/Historia/2018-Roche`, `Pojazdy/VW-Golf-Opole`. Nie uzależniać nazwy auta od jego pozycji w domowej flocie. |
| Średni | Dokument 07 pomija szczegółowe mapowanie części istniejących podfolderów, np. finansowego `99. Archiwum` oraz `96/2012 Wesele`. | Dopisać mapowanie z zachowaniem roczników i pochodzenia, a nie przenosić wszystko do ogólnego worka Archiwum. |
| Średni | Dokument 08 stwierdza unikalność prefiksów, choć są dwa foldery `00-`. Dokument 07 zapowiada 19 katalogów, ale jego drzewo zawiera 20. | Traktować pełną nazwę lub ID jako identyfikator. W tym wariancie jest 18 stałych obszarów i dwa foldery przejściowe: Takeout i kwarantanna. |

Nie są to dowody, że użytkownik źle organizuje pliki. Są to miejsca, gdzie propozycja wykracza poza dostępne dane albo nie zachowuje informacji już zawartej w obecnym układzie.

## 4. Rekomendowane drzewo katalogów

Zachowuję nazwy głównych obszarów z dokumentu 07. Emoji mogą pozostać na pierwszym poziomie jako element wygody użytkownika; nie są warunkiem poprawności struktury. Podfoldery powinny mieć czytelne nazwy i stabilne znaczenie. Pokazuję tylko gałęzie potrzebne do najważniejszych korekt, nie obowiązkowy komplet folderów do utworzenia z góry.

```text
Mój dysk/
├── 00-📥-Inbox/
│   ├── AI-Exports/
│   ├── Skany-i-Mobilne/
│   └── Do-Przejrzenia/
├── 00-🔒-Poufne-Dokumenty/
│   ├── Tozsamosc/
│   └── Majatek-Akty-Notarialne/
├── 01-👨‍👩‍👧‍👦-Rodzina/
│   ├── Wazne-Dokumenty/
│   ├── Natalka/
│   ├── Nadia/
│   ├── Michal/
│   ├── Kuba/
│   ├── Wspolne-Sprawy-Dzieci/
│   └── Genealogia/
├── 02-🏫-Edukacja-Dzieci/
│   ├── Michal/<rok-szkolny>/
│   └── Nadia/<rok-szkolny>/
├── 03-🏥-Zdrowie/
│   ├── Pawel/
│   ├── Natka/
│   ├── Dzieci/Michal/
│   ├── Dzieci/Nadia/
│   ├── Rodzice/Mama/
│   └── Do-Przypisania/           # np. Terapia-M, do potwierdzenia
├── 04-📄-Dokumenty-Osobiste/
│   ├── Dziennik/
│   ├── Kariera-i-CV/
│   └── Certyfikaty-i-Uprawnienia/
├── 05-💰-Finanse/
│   ├── 01-Budzet-i-Analizy/
│   ├── 02-Podatki/<rok>/
│   ├── 03-Banki-i-Kredyty/
│   ├── 04-Inwestycje-i-Emerytura/
│   ├── 05-Paragony-i-Gwarancje/
│   └── Archiwum/
├── 07-🏢-Praca-i-Projekty/
│   ├── Projekty/2026-HSBC/
│   ├── Historia/                 # zachowane firmy i dawne nazwy
│   ├── Publikacje-i-Wystapienia/
│   └── Warsztaty-i-Materialy-Szkoleniowe/
├── 10-🏠-Mieszkanie-i-Nieruchomosci/
│   ├── Pod-Strzecha-7/
│   │   ├── Zakup-i-Umowy/
│   │   ├── Media-i-Energia/
│   │   └── Remonty-i-Wyposazenie/
│   ├── Infrastruktura-Domowa-i-Siec/
│   ├── Archiwum/
│   └── Do-Przypisania/           # Pokoj i Dzialka-Dom, jeśli kontekst nieznany
├── 11-🏡-Lewickie/
│   ├── Eksploatacja-i-Oplaty/
│   ├── Geodezja-i-Dokumentacja/
│   └── Media-i-Lacznosc/
├── 12-🚗-Pojazdy/
│   ├── Toyota-Corolla/
│   ├── VW-Golf-Opole/
│   └── Archiwum/
├── 20-📚-Wiedza-i-Rozwoj/
│   ├── 01-Inzynieria-Danych-i-AI/Prompty-i-Gems/
│   ├── 02-Matematyka-i-Nauka/
│   └── 03-Ebooki-i-Publikacje/
├── 21-🎵-Audio-i-Multimedia/
├── 22-🏃-Sport-i-Aktywnosc/
├── 23-🎮-Gry-i-Hobby/
├── 24-🏖️-Podroze-i-Wyjazdy/<rok>/<wyjazd>/
├── 80-📱-Aplikacje-i-Synchronizacja/
│   ├── Notability-Backup/
│   └── Obsidian-Backup/          # wyłącznie jeśli faktycznie istnieje potrzeba kopii
├── 90-🗄️-Archiwum/
│   ├── Dzialalnosc-Gospodarcza/
│   ├── Stare-Projekty/
│   ├── Studia/
│   └── Kopie-Urzadzen/           # zachować rozdzielenie według urządzenia i daty
├── 95-💽-Takeout/                # folder przejściowy z dokumentów 06–07
└── 99-🗑️-Do-Usuniecia/           # tylko zasoby faktycznie wybrane do usunięcia
```

**Granice obszarów:** Rodzina przechowuje sprawy i pamiątki osób; Edukacja dzieci — naukę szkolną; Zdrowie — dokumentację medyczną; Finanse — rozliczenia, podatki i finanse domowe; nieruchomości — sprawy konkretnego obiektu; Wiedza — materiały do ponownego użycia; Praca — kontekst projektów i zatrudnienia. Dokument dotyczący kilku obszarów ma jedno miejsce podstawowe i ewentualny skrót w drugim, zamiast dwóch rozchodzących się kopii.

Archiwum to głównie **stan sprawy wewnątrz dziedziny**: stare PIT-y pozostają w Finansach, a stare badania przy właściwej osobie. Główny `90-🗄️-Archiwum` służy kompletnym zbiorom historycznym i kopiom urządzeń, których rozbieranie nie daje bieżącej korzyści.

## 5. Skorygowana mapa istniejących folderów głównych

W poniższej tabeli krótkie nazwy celów, np. `Rodzina` lub `Pojazdy`, oznaczają pełne katalogi z drzewa powyżej. Lista obejmuje 27 źródeł z wrześniowego zestawienia po wyłączeniu zakończonego tematu zdjęć oraz `Takeout` opisany w dokumentach październikowych. Nie jest deklaracją, że wszystkie 28 pozycji nadal istnieje na koncie.

| Istniejący folder | Rekomendowany cel | Decyzja i uwagi |
| :--- | :--- | :--- |
| `01👨‍👩‍👧‍👦 Rodzina` | `Rodzina` | **Skorygować.** Zachować Natalkę, Nadię, Michała, Kubę i Genealogię. `02 Dzieci` → `Wspolne-Sprawy-Dzieci`, dopóki nie ma podstaw do podziału. |
| `02🏫Szkoła` | `Edukacja-Dzieci/Michal` i `Edukacja-Dzieci/Nadia` | **Przyjąć.** Zachować roczniki i klasy; studia Pawła nie trafiają do Edukacji dzieci. |
| `03🏥Zdrowie` | `Zdrowie/<osoba>` | **Skorygować.** Osobne gałęzie dzieci i mamy. `Terapia M.` oraz zbiorcze archiwa wymagają przypisania; nie uznawać ich z góry za zakończone. |
| `05💰Finanse` | `Finanse` | **Przyjąć z uzupełnieniem.** Podatki → `02-Podatki`, Budżet → `01-Budzet-i-Analizy`, Emerytura → `04-Inwestycje-i-Emerytura`, Kredyty → `03-Banki-i-Kredyty`; zachować `99. Archiwum` jako `Archiwum`. |
| `06🏠Mieszkanie` | `Mieszkanie-i-Nieruchomosci` | **Skorygować.** Pod Strzechą zachować jako konkretny obiekt, z własnymi mediami i remontami. `00. Archiwum` pozostaje w tym obszarze. `06. Działka   Dom` wymaga potwierdzenia nieruchomości. |
| `07🏢Praca` | `Praca-i-Projekty` | **Skorygować.** Zachować firmy i lata. Świadectwa pracy → `Dokumenty-Osobiste/Kariera-i-CV`, materiały szkoleniowe → szkolenia. Nie przesądzać, że wszystkie dokumenty Snowflake dotyczą HSBC. |
| `08🏖️Wakacje` | `Podroze-i-Wyjazdy` | **Przyjąć.** Zachować lata i konkretny wyjazd, w tym `2027.02 - Narty`; dopiero potem ujednolicać zapis nazw. |
| `09🚗Samochód` | `Pojazdy` | **Skorygować.** Toyota → `Toyota-Corolla`; `#Archive` → `Archiwum`. Nie mieszać dokumentów poprzednich aut z aktualną Toyotą. |
| `10 ☂️ Ubezpieczenie` | właściwy samochód, nieruchomość, podróż albo Rodzina | **Przyjąć z kontrolą.** Toyota i VW mają konkretne nazwy. NNW dzieci → `Rodzina/Wspolne-Sprawy-Dzieci/Ubezpieczenia`; Słowacja Natalki → podróż z 2025 r. Foldery z zerową liczbą plików też wymagają sprawdzenia przed usunięciem. |
| `11. Obsydian` | bez przenoszenia do rzekomo aktywnego Sync | **Potwierdzić.** Zapisane dane pokazują pusty folder. Można zrezygnować z niego po potwierdzeniu braku użycia; folder nie dowodzi konfiguracji synchronizacji ani porzuconego projektu. |
| `15🏡Lewickie` | `Lewickie` | **Przyjąć.** Eksploatacja → `Eksploatacja-i-Oplaty`, działka → `Geodezja-i-Dokumentacja`, zestawy Plus → `Media-i-Lacznosc/Plus`, z zachowaniem rozróżnienia umów i dat. |
| `16🏡Pokój` | `Mieszkanie-i-Nieruchomosci/Do-Przypisania/Pokoj` | **Potwierdzić.** Po ustaleniu lokalu jego energię przenieść do tego konkretnego obiektu. Nie do ogólnego katalogu energii wszystkich nieruchomości. |
| `20📚 ebooks + audobooks` | `Wiedza-i-Rozwoj/03-Ebooki-i-Publikacje` oraz `21-Audio-i-Multimedia` | **Skorygować.** Matematyka → `02-Matematyka-i-Nauka`. Nie rozrywać zakupionego pakietu ebook + audiobook na podstawie nazwy folderu; wspólny komplet może pozostać w jednym miejscu ze skrótem z drugiego obszaru. |
| `25📄 Paweł - dokumenty` | dziedziny zgodnie z tabelą w rozdziale 6 | **Skorygować.** Najpierw zachować pochodzenie historycznych zbiorów. Osiem plików poza wymienionymi podfolderami wymaga osobnego mapowania. |
| `85🏃 Bieganie` | `Sport-i-Aktywnosc/Bieganie` | **Przyjąć.** Zachować wszystkie dotychczasowe roczniki. Folder Sport nie powinien zgubić nazwy konkretnej aktywności. |
| `91🔑Hasła` | menedżer haseł; na Drive najwyżej właściwa zaszyfrowana kopia | **Potwierdzić zawartość.** Nazwa nie dowodzi, że wszystkie pięć plików zawiera jawne hasła. Nie kierować całej gałęzi do usunięcia przed rozpoznaniem i sprawdzeniem przeniesienia potrzebnych danych. |
| `92🎵 Muzyka` | `Audio-i-Multimedia/Audiobooki` | **Przyjąć.** Zachować tytuły i kompletne pakiety. Skróty z Rodziny mogą ułatwiać dzieciom dostęp. |
| `93🎮Gry` | `Gry-i-Hobby` | **Przyjąć.** Zachować Minecraft i VCMI jako osobne gałęzie. |
| `94🧑‍💻Oprogramowanie` | `Archiwum/Stare-Projekty/Oprogramowanie` | **Potwierdzić retencję.** Reorganizacja nie oznacza automatycznego skasowania instalatorów; pozostawić nazwy programów i wersji. |
| `95💽Kopia zapasowa` | `Archiwum/Kopie-Urzadzen` albo dotychczasowe miejsce do odrębnej decyzji o nośniku | **Skorygować.** Zachować każde urządzenie, użytkownika i datę kopii. Nie rozbierać backupu telefonu lub laptopa na bieżące dziedziny i nie uznawać różnych dat za duplikaty. |
| `96🗄️Archiwum` | `Archiwum` i właściwe dziedziny | **Uzupełnić.** `2020 Działalność Gospodarcza` → `Dzialalnosc-Gospodarcza/2020`; `2018 SVN` → `Stare-Projekty/SVN/2018`; `2012 Wesele` → `Rodzina/Archiwum/2012-Wesele`; `89 Sterta` → przegląd z zachowaniem zbioru. |
| `98🧾Paragony` | `Finanse/05-Paragony-i-Gwarancje` | **Przyjąć warunkowo.** Przepiąć miejsce zapisu skanera i sprawdzić nowy zapis. Stary punkt wejścia może pozostać skrótem, jeśli to pomaga w nawigacji i jest obsługiwane przez używane narzędzie. |
| `Analiza_Matematyczna_WEiTI` | `Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/WEiTI` | **Przyjąć.** Jedna gałąź dla podręcznika i materiałów z roota, bez umieszczania ich w Edukacji dzieci. |
| `Gemini Gems` | `Wiedza-i-Rozwoj/01-Inzynieria-Danych-i-AI/Prompty-i-Gems` | **Skorygować.** Trwałe definicje narzędzi, a nie krótkotrwałe eksporty do Inboxa. Jeśli katalog jest zarządzany przez aplikację, najpierw ustalić obsługiwany sposób reorganizacji. |
| `Notability` | `Aplikacje-i-Synchronizacja/Notability-Backup` | **Przyjąć warunkowo.** Zachować strukturę aplikacji. Do dziedzin kierować dopiero świadomie wybrane eksporty; sprawdzić zapis nowej kopii po zmianie lokalizacji. |
| `Zapisane z Chrome` | tymczasowo `Inbox/Do-Przejrzenia/Chrome-1` | **Skorygować.** Posegregować wartościowe dokumenty. Nie nadawać zbiorowej decyzji Usuń. |
| `Zapisane z Chrome (1)` | tymczasowo `Inbox/Do-Przejrzenia/Chrome-2` | **Skorygować.** Taka sama procedura jak dla pierwszego zbioru; dopiero po przeglądzie scalać kolejki. |
| `Takeout` (opisany w 06–07) | `95-💽-Takeout` lub dotychczasowa lokalizacja przejściowa | **Poza bieżącą reorganizacją dziedzin.** Nie dzielić paczek między Rodzinę, Wiedzę i Archiwum. Bez ponownego otwierania zakończonego tematu zdjęć. |

## 6. Szczegółowa rekomendacja dla `25📄 Paweł - dokumenty`

Kierunek rozdzielenia folderu 25 jest sensowny, ale natychmiastowe wymieszanie jego plików z bieżącymi zasobami może stworzyć trudniejsze do wykrycia kolizje. **Pierwszy etap powinien przenosić całe rozpoznane podfoldery do odpowiadających im dziedzin, zachowując pochodzenie `Import-z-25`.** Drugi etap to selektywne włączenie konkretnych plików do bieżących spraw.

| Podfolder źródłowy | Rekomendowany cel pierwszego etapu | Korekta / uzasadnienie |
| :--- | :--- | :--- |
| `00. Michaś` | `Rodzina/Michal/Import-z-25` | Zachować zestaw jako całość; szkolne i medyczne dokumenty rozdzielić dopiero po przeglądzie. |
| `00. Nadia` | `Rodzina/Nadia/Import-z-25` | 39 plików zajmuje około 3,1 w jednostce opisanej przez eksport jako GB; nie zakładać, że to wyłącznie dokumenty szkolne. |
| `01. Natalka` | `Rodzina/Natalka/Import-z-25` | Zachować kontekst osoby; konkretne medyczne dokumenty mogą trafić do Zdrowia. |
| `02. Finanse` | `Finanse/Archiwum/Import-z-25` | Stare wyciągi i rozliczenia nie są automatycznie bieżącymi kredytami. |
| `03. NFZ` | `Zdrowie/Do-Przypisania/NFZ-z-25` | Najpierw ustalić osoby; dopiero potem właściwe gałęzie. |
| `04. CV` | `Dokumenty-Osobiste/Kariera-i-CV/Archiwum-z-25` | Zachować historyczne wersje, nie zastępować nimi aktualnego CV. |
| `05. DWH` | `Praca-i-Projekty/Historia/Import-z-25/DWH` | Rozdzielić projektowe archiwa od wiedzy do ponownego użycia dopiero po przeglądzie; nie rozpraszać całego zbioru od razu. |
| `05. Samochód` | `Pojazdy/Archiwum/Import-z-25` | Zachować podział na wcześniejsze auta; nie dołączać wszystkiego do Toyoty. |
| `06. Praca` | `Praca-i-Projekty/Historia/Import-z-25/06-Praca` | 5 416 plików nie daje podstaw do klasyfikacji całej gałęzi jako umowy i CV. |
| `11. Instrukcje obsługi` | `Mieszkanie-i-Nieruchomosci/Archiwum/Instrukcje-z-25` | Docelowo przypisać instrukcje do sprzętów lub nieruchomości, jeśli da się to ustalić. |
| `50. Zdrowie` | `Zdrowie/Do-Przypisania/Zdrowie-z-25` | W dokumencie 07 całość przypisano Pawłowi bez pokazania dowodu. Nie zakładać jednej osoby dla 705 plików. |
| `90. SVN Repo` | `Archiwum/Stare-Projekty/SVN-z-25` | Zachować kompletną strukturę repozytoriów. |
| `96. Studia` | `Archiwum/Studia/Import-z-25` | Zachować archiwum jako zbiór. Materiały regularnie używane można później przenieść do Wiedzy. |
| Pliki bezpośrednio w folderze 25 | `Inbox/Do-Przejrzenia/Pliki-z-25` | Zestawienie wskazuje 7 586 plików łącznie i 7 578 w wymienionych podfolderach: pozostaje osiem pozycji, których rozdział 2.1 dokumentu 07 nie mapuje. |

`Import-z-25` opisuje pochodzenie, nie dowodzi nieaktualności. Nie zmienia automatycznie statusu aktywnego pliku. Folder 25 można usunąć dopiero wtedy, gdy wszystkie elementy mają świadomie przypisane cele, a nie tylko dlatego, że przeniesiono 13 widocznych podfolderów.

## 7. Reguły, które usuwają niejednoznaczność mapowania

### Osoba, obiekt i projekt przed rodzajem dokumentu

- Badanie dziecka: `Zdrowie/Dzieci/<osoba>/<rok>`, nie zbiorczy `Zdrowie/Dzieci` bez rozróżnienia.
- Rachunek za energię: folder właściwej nieruchomości; w Finansach może być skrót lub zestawienie do rozliczeń.
- Polisa auta: konkretne auto. NNW obojga dzieci: wspólne sprawy dzieci, bez tworzenia dwóch rozchodzących się kopii.
- Dokument formalny dotyczący zatrudnienia: `Dokumenty-Osobiste/Kariera-i-CV`. Materiał konkretnego projektu: `Praca-i-Projekty/<projekt>`. Artykuł użyteczny niezależnie od projektu: `Wiedza-i-Rozwoj`.
- Notatka z Notability: kopia aplikacyjna pozostaje w obszarze aplikacji, a wybrany materiał finalny trafia do właściwej dziedziny.

### Nie klasyfikować treści wyłącznie po tytule

Dokument 07 poprawia wcześniejszą ocenę losowo nazwanego PDF-a, kierując go do przeglądu zamiast nadać mu niepotwierdzony tytuł. Tę samą regułę należy stosować do plików bez tytułu, eksportów AI, dokumentów `(1)` i zbiorów `Temp` lub `Sterta`: **niezrozumiała nazwa to wskazanie do rozpoznania, nie decyzja o usunięciu.**

Karta Zielonej Szkoły jest w dokumencie 03 przypisana do Nadii lub Michała, a w 07 już konkretnie do Michała. W zapisanych metadanych nie ma dowodu tej zmiany. Przed docelowym przeniesieniem trzeba sprawdzić, którego dziecka dotyczy. Podobnie wersje planu podróży mogą pozostać razem; samo `V2` nie dowodzi, że `V1` jest zbędna.

### Folder poufny jest granicą dostępu, nie tylko nazwą

Obszar poufny poza folderem rodzinnym jest rozsądnym kierunkiem. Dokument 08 opisuje zachowanie ID przy przenoszeniu, ale nie należy utożsamiać zachowanego linku z zachowanym dostępem wszystkich osób: dostęp zależy także od uprawnień folderu docelowego. Zapisane eksporty nie potwierdzają ani wcześniejszego naruszenia, ani prywatności skanów.

Rekomendowane mapowanie dokumentów poufnych wymaga kontroli dostępu źródła i celu. Samo przeniesienie do folderu z ikoną kłódki lub zmiana rozszerzenia na `.cpt` nie szyfruje pliku. Szyfrowana kopia, jeśli jest potrzebna, powstaje w osobnej procedurze. Ten review jej nie wykonuje.

### Nazwy mają ułatwiać nawigację, nie stać się osobnym projektem

Rekomenduję pozostawić wariant z emoji na pierwszym poziomie, żeby zachować ciągłość z propozycją 07. Alternatywa ASCII z dokumentu 08 jest dopuszczalna, ale nie rozwiązuje niejednoznacznego mapowania. Nie ma potrzeby jednocześnie zmieniać wszystkich nazw plików, wszystkich podfolderów i numeracji. Spacje oraz polskie znaki nie są same w sobie błędem systemu plików; stosowane narzędzia powinny poprawnie obsługiwać istniejące nazwy.

Nie trzeba numerować każdego podfolderu ani zapełniać luk numeracji. Dwa prefiksy `00` są świadomym wyróżnieniem stref systemowych, ale nie unikalnymi kluczami. Numerów nie używać jako jedynego sposobu identyfikacji katalogów.

## 8. Rekomendowana kolejność reorganizacji

1. **Uaktualnić mapę źródeł.** Potwierdzić aktualne katalogi i pliki; rozróżnić dane wrześniowe od październikowych dopisków. Przy każdej pozycji zapisać źródło, cel, rodzaj operacji i ewentualną niepewność.
2. **Ustalić cele istniejących obszarów.** Najpierw przemianować Rodzinę, Szkołę, Zdrowie, Finanse, Pracę, Mieszkanie, Lewickie i Pojazdy. Nowy folder utworzyć tylko wtedy, gdy nie zastępuje katalogu, który ma być przemianowany.
3. **Zachować kontekst osób i zasobów.** Uzupełnić Kubę, osobne gałęzie dzieci w Zdrowiu, konkretne auta, firmy i nieruchomości. Niejednoznaczne zbiory pozostawić oddzielnie z oznaczeniem do przypisania.
4. **Mapować pliki z roota do już istniejących celów.** Niepewne treści kierować do Inboxa, a nie do kwarantanny do usunięcia. Dokumenty poufne obsłużyć zgodnie z rzeczywistymi uprawnieniami.
5. **Rozdzielić folder 25 całymi podfolderami.** Zachować pochodzenie, potem osobno uporządkować osiem plików luzem. Przenoszenie nie jest deduplikacją.
6. **Przepiąć punkty wejścia aplikacji.** Notability, Chrome i skaner paragonów sprawdzić na nowo zapisanym dokumencie przed likwidacją starych miejsc. Nie tworzyć aktywnego `Obsidian-Sync` wyłącznie przez nazwanie folderu.
7. **Sprawdzić rezultat na codziennych zadaniach.** Czy można szybko znaleźć badanie każdego dziecka, polisę każdego auta, dokument konkretnego lokalu, PIT danego roku i materiał z dawnej firmy? Czy nowe dokumenty trafiają tam, gdzie zakłada mapa?
8. **Dopiero potem usuwać puste katalogi i oceniać zbędne treści.** Kwarantanna jest wynikiem świadomej decyzji dotyczącej zawartości; nie zastępuje analizy. Nie kasować zbiorów tylko dlatego, że zakończono zmianę struktury.

Nie traktowałbym `15–20 GB` ani idealnego `Zero-Root` jako kryterium poprawności taksonomii. Wielkość zależy od retencji i nośników, a brak luźnych plików nie dowodzi, że da się odnaleźć właściwy dokument. Inbox powinien mieć cotygodniowy przegląd i przypomnienie o zaległościach, nie automatyczne kasowanie po siedmiu dniach.

## 9. Co zachować z wcześniejszych analiz

- Rozdzielenie domen oraz prosty Inbox — kierunek jest sensowny i odpowiada istniejącym nawykom.
- Osobny obszar poufny — pod warunkiem realnego zarządzania dostępem.
- Relokację polis do właściwego auta, nieruchomości i podróży — z zachowaniem rzeczywistego kontekstu.
- Jedną lokalizację główną dokumentu z ewentualnymi skrótami — zamiast dublowania aktywnych wersji.
- Oddzielenie kopii aplikacji od finalnych materiałów tematycznych.
- Etapową reorganizację i zachowanie wcześniejszych artefaktów jako historii ustaleń.

W tym zakresie review zastępuje zalecenia o archiwizacji Kuby, spłaszczaniu dokumentacji dzieci, przenoszeniu Gems do Inboxa i zbiorowym usuwaniu drugiego folderu Chrome. Nie podważa pozostałych, zakończonych prac.

## 10. Wynik i granice weryfikacji

**Wynik:** propozycja katalogów nadaje się jako baza, lecz mapa z dokumentu 07 wymaga powyższych korekt. Rekomendowany następny krok to finalna mapa przypisań zgodna z tym drzewem, ze wskazanymi pozycjami do potwierdzenia, a następnie etapowa reorganizacja.

Zweryfikowano lokalnie spójność tabel z JSON, obecność pominiętych podfolderów, liczby plików w folderze 25 i liczbę głównych gałęzi drzewa w dokumencie 07. Nie odczytywano aktualnego konta Google Drive, zawartości prywatnych dokumentów ani uprawnień; nie wykonywano przeniesień ani usunięć. Dostęp do publicznej dokumentacji producentów przez sieć był niedostępny w trakcie próby, dlatego nie oznaczam zasad zależnych od usług jako przetestowanych na bieżącym koncie.

Wcześniejsze materiały pozostają bez zmian. Ten plik dopisuje ocenę i skorygowaną rekomendację do istniejącego explore-a.
