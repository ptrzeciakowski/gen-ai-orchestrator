# Behawioralna Rekonstrukcja Stylu Pracy, Architektura PKM i Automatyzacja Ekosystemu Google Drive

**Użytkownik:** Paweł Trzeciakowski  
**Data analizy:** 19 września 2026 r.  
**Autor:** Ekspert ds. Analizy Nawyków Cyfrowych, Personal Knowledge Management (PKM) i Automatyzacji Workflow  
**Baza telemetryczna:** 77 498 plików, 8 185 folderów, 267.0 GB przestrzeni, 49 plików w Root (`Mój dysk`), baza metadanych SQLite `metadata_sqlite_db` (DriveFS).

---

## Executive Summary & Diagnoza Behawioralna (Archetyp Cyfrowy)

Analiza danych telemetrycznych oraz artefaktów zgromadzonych na Dysku Google pozwala na precyzyjną rekonstrukcję profilu cyfrowego użytkownika:

> **Archetyp użytkownika:** *High-Velocity Knowledge Worker & Data Architect with "Flat-Dump Drift" & Multi-Device Tool Fragmentation*.

Paweł to zaawansowany inżynier i architekt danych (projekty Snowflake, HSM, Allegro, Roche, DWH), aktywny ojciec dbający o edukację dzieci (tenis, matematyka, szkoła, konkurs Kangur), a także osoba stale rozwijająca własne kompetencje akademickie (Analiza Matematyczna WEiTI PW, edukacja technologiczna).

Mimo wysokich kompetencji technicznych i intuicyjnego stosowania logicznej numeracji dziesiętnej (`01 Rodzina`, `02 Szkoła`, `05 Finanse`, `07 Praca`), na dysku uwidacznia się **strukturalny kryzys przepływu pracy (workflow crisis)** wynikający ze starcia nowoczesnych, wieloplatformowych narzędzi (Google Gemini AI, iPad/Notability, macOS Chrome, Obsidian) ze statyczną strukturą tradycyjnego dysku w chmurze.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │               ZJAWISKO ROZDWOJENIA DYSKU                │
                    └─────────────────────────────────────────────────────────┘
                                                 │
         ┌───────────────────────────────────────┴──────────────────────────────────────┐
         ▼                                                                              ▼
┌──────────────────────────────────────┐                       ┌──────────────────────────────────────┐
│       CMENTARZYSKO CYFROWE           │                       │       OPERACYJNY STRUMIEŃ BIEŻĄCY    │
│            (85.1% dysku)             │                       │             (0.6% dysku)             │
├──────────────────────────────────────┤                       ├──────────────────────────────────────┤
│ • 36 587 plików nietkniętych > 3 lata│                       │ • 105 plików aktywnych w ost. 30 dni │
│ • 29 360 plików NIGDY nieotwieranych │                       │ • 352 pliki aktywne 1-6 mies. temu   │
│ • 95💽 Kopia zapasowa (50.8 GB,     │                       │ • 49 plików w Root (Flat-Dump Drift) │
│   24 470 plików ze starych telefonów)│                       │ • Bieżące analizy Snowflake / PW     │
│ • 88📸 Zdjęcia (190.0 GB, 71% dysku) │                       │ • Aktywne notatki i materiały dzieci │
└──────────────────────────────────────┘                       └──────────────────────────────────────┘
```

Dysk Google pełni u Pawła trzy sprzeczne ze sobą role:
1. **Zimny skarbiec / cmentarzysko kopii zapasowych** – 240 GB (blisko 90% przestrzeni) to zrzuty starych telefonów (Galaxy S3/S4/S7, HTC, routery) oraz nieuporządkowane repozytorium fotograficzne.
2. **Aktywny warsztat inżynierski i edukacyjny** – gdzie powstają zaawansowane materiały do analizy matematycznej, prezentacje dla szkoły, posty branżowe na LinkedIn i architektury hurtowni danych.
3. **Przypadkowe lądowisko transmisyjne (Flat-Dump Landing Zone)** – do którego narzędzia trzecie (Gemini, wtyczki Chrome, zrzuty z iOS) automatycznie wrzucają pliki o roboczych nazwach wprost do głównego katalogu (`Root`), powodując szum informacyjny i degradację porządku.

Poniższy raport przedstawia rekonstrukcję behawioralną tych zjawisk, specyfikację wzorca **Inbox/Staging** oraz gotowe procedury automatyzacji i higieny cyfrowej.

---

# Rozdział 1: Szczegółowa Rekonstrukcja Stylu Pracy i Zachowań Użytkownika

Na podstawie analizy 49 plików leżących w `Root`, podfolderów systemowych oraz dokładnych znaczników czasu modyfikacji i odczytu (`mdate`, `vdate`), zrekonstruowano 5 kluczowych mechanizmów behawioralnych Pawła.

---

### 1.1. Praca z AI (Gemini, ChatGPT): Syndrom "Plików-Promptów" w Root

W katalogu głównym znajduje się aż **8 plików**, których tytułami są dosłowne zdania promptowe wpisane przez Pawła do modeli LLM.

#### Identyfikacja artefaktów promptowych w Root:
| Data i godzina | Nazwa pliku w Root | Mime / Typ | Zidentyfikowany kontekst zadaniowy |
| :--- | :--- | :--- | :--- |
| **2026-04-05 21:47** | `jeszcze raz poproszę o te wykresy, ale pokaż sumę....gdoc` | Google Doc | Analiza zużycia energii elektrycznej i fotowoltaiki |
| **2026-04-12 17:56** | `Czy możesz załączyć podsumowanie o które prosiłem?.gdoc` | Google Doc | Podsumowanie konwersacji badawczej / roboczej |
| **2026-05-22 22:30** | `zrób z tego tabelę - w kolumnach fazy życia, a w....gdoc` | Google Doc | Tabela cyklu życia / planowania finansowo-rodzinnego |
| **2026-06-04 19:37** | `Super, dodaj jeszcze do dokumentu kartę z całą tą ....gdoc` | Google Doc | Warsztat architektoniczny: Warstwa Semantyczna Snowflake |
| **2026-06-04 19:40** | `Serio? Nie możesz wyciągnąć całej tej konwersacji ....gdoc` | Google Doc | Warsztat architektoniczny: Warstwa Semantyczna Snowflake |
| **2026-07-19 11:13** | `dobrze, biorąc pod uwagę te kryteria przygotuj mi....gsheet` | Google Sheet | Zestawienie tabelaryczne / porównanie wariantów |
| **2026-09-04 21:15** | `wygeneruj mi podsumowanie tej rozmowy z osateczny....gdoc` | Google Doc | Synteza dyskusji projektowej (kliknięcie 1) |
| **2026-09-04 21:15** | `wygeneruj mi podsumowanie tej rozmowy z osateczny... (1).gdoc` | Google Doc | Synteza dyskusji projektowej (kliknięcie 2 – duplikat!) |

#### Mechanizm powstania (Technical Root Cause):
1. **Domyślne zachowanie interfejsu Google Gemini (Export to Docs / Sheets):**  
   Gdy użytkownik rozmawia z Gemini w przeglądarce i klika przycisk *„Eksportuj do Dokumentów Google”* lub *„Eksportuj do Arkuszy”*, interfejs webowy Google automatycznie tworzy nowy plik. Jeśli czat nie miał ręcznie nadanego tytułu na pasku bocznym, Gemini pobiera pierwsze słowa **ostatniego promptu użytkownika** jako `title` dokumentu.
2. **Brak selektora folderu docelowego w Gemini:**  
   Google Workspace nie pyta użytkownika: *„W którym folderze chcesz zapisać wyeksportowany dokument?”*. Zamiast tego wykonuje wywołanie API Drive v3 z `parents=['root']`.
3. **Fluktuacja uwagi i podwójne kliknięcia:**  
   Pliki `wygeneruj mi podsumowanie...` oraz `wygeneruj mi podsumowanie... (1)` z 2026-09-04 o godz. 21:15 dowodzą zniecierpliwienia: brak natychmiastowego feedbacku w UI spowodował ponowne kliknięcie eksportu, tworząc duplikat. Minutę później (21:16) powstał kolejny porzucony szkic: `Dokument bez tytułu (2).gdoc`.
4. **Powiązanie z Gemini Gems:**  
   W folderze `Gemini Gems` znajdują się dwa zdefiniowane boty systemowe:
   - `Nauczyciel Matematyki` (utworzony 2025-11-29)
   - `Ekspert od energii w Tauron` (utworzony 2026-04-05 22:03)  
   Chronologia artefaktów z 5 kwietnia 2026 r. odsłania pełny łańcuch pracy:
   ```
   21:47 - Eksport promptu: "jeszcze raz poproszę o te wykresy, ale pokaż sumę..." (Root)
   21:52 - Utworzenie dokumentu: "Analiza zużycia energii i fotowoltaiki.gdoc" (Root)
   22:03 - Utworzenie dedykowanego bota: "Ekspert od energii w Tauron" (Gemini Gems)
   ```
   Paweł przechodzi od iteracyjnego promptowania w oknie czatu do formalizacji wiedzy w postaci dedykowanego Gema, ale artefakty pośrednie (pliki promptowe i robocze gdoc) pozostają w `Root` jako cyfrowy osad.

---

### 1.2. Notability i Ekosystem Apple (iPad + Apple Pencil): Odcięty Silos Wiedzy

Folder `Notability` w `Root` zawiera **232 pliki** o łącznej wadze **421.9 MB**, rozlokowane w 28 podfolderach.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │               SILOS NOTABILITY W ROOT                   │
                    │               (232 pliki / 421.9 MB)                    │
                    └─────────────────────────────────────────────────────────┘
                                                 │
      ┌──────────────────┬───────────────────────┼──────────────────────┬──────────────────┐
      ▼                  ▼                       ▼                      ▼                  ▼
┌──────────────┐   ┌──────────────┐        ┌──────────────┐       ┌──────────────┐   ┌──────────────┐
│  Matematyka  │   │  Szkolenia   │        │     Daily    │       │     Praca    │   │    Zdrowie   │
│  (41 plików) │   │  (31 plików) │        │  (27 plików) │       │  (Roche/All) │   │  (27 plików) │
├──────────────┤   ├──────────────┤        ├──────────────┤       ├──────────────┤   ├──────────────┤
│• Kangur 2025 │   │• Szkolenia   │        │• Notatki     │       │• GODW 400    │   │• 2025-03-20  │
│• Maluch 2006 │   │  techniczne  │        │  dzienne     │       │• Metadata mgmt│  │  wykład ADHD │
│• Wprawki     │   │• Certyfikaty │        │• Zapiski spotkań│    │• Merch. Fin. │   │• Notatki med.│
└──────────────┘   └──────────────┘        └──────────────┘       └──────────────┘   └──────────────┘
      │                                                                 │                  │
      ▼                                                                 ▼                  ▼
Dubluje: 02🏫Szkoła                                             Dubluje: 07🏢Praca     Dubluje: 03🏥Zdrowie
```

#### Dystrybucja rozszerzeń w Notability:
- `.note` (natywny format Notability): 98 plików
- `.ntb` (archiwalny format zapisu): 69 plików
- `.pdf` (wektorowy eksport z warstwą pisma odręcznego): 63 pliki
- `.gdoc` / `.zip`: 2 pliki

#### Diagnoza konfliktu architektonicznego:
1. **Niezależna ontologia kognitywna:**  
   W Notability na iPadzie Paweł stworzył strukturę kategorii (Dividers & Subjects), która stanowi dokładne zwierciadło jego życia:
   - `Matematyka` (41 plików) – konkursy Kangur, zadania dzieci, wykresy;
   - `Szkolenia` (31 plików) oraz `Daily` (27 plików) – operacyjne notatki z dnia pracy;
   - `Pawel` (27 plików) – m.in. kluczowa notatka `2025-03-20 - wykład o ADHD.note`;
   - `Merchant Finance` (12 plików) – notatki z analizy lejków w Allegro;
   - `Roche / GODW folders 400` oraz `Augumented metadata management` (7 plików) – architektura danych Roche;
   - `Sycylia` (11 plików) oraz `Wakacje` – plany podróży;
   - `Dzieci / Tenis` oraz `Linde klasa 6c` – bieżące sprawy szkolne dzieci.
2. **Izolacja od taksonomii Dysku:**  
   Włączona w Notability funkcja *Auto-Backup* ma sztywno zdefiniowaną ścieżkę `/Notability`. W efekcie notatka dotycząca projektu w Allegro ląduje w `/Notability/Merchant Finance/`, podczas gdy na Dysku istnieje oficjalny folder `07🏢Praca/2025 - Allegro`. Notatka o zdrowiu ląduje w `/Notability/Zdrowie/Pawel`, podczas gdy badania krwi i wypisy lekarskie znajdują się w `03🏥Zdrowie`.
3. **Puchnięcie przestrzeni przez dublowanie formatów:**  
   Notability zapisuje każdą notatkę w dwóch formatach: zamkniętym `.note` (dostępnym tylko z aplikacji) oraz `.pdf`. Prowadzi to do podwojenia liczby obiektów i uniemożliwia pełnotekstowe przeszukiwanie zasobów z poziomu wyszukiwarki Google Drive.

---

### 1.3. Pobieranie z Przeglądarki Chrome: Rozdwojenie `(1)` i Zrzuty Portali

Dysk zawiera dwa foldery wygenerowane przez oficjalne rozszerzenie Google Chrome:
- `Zapisane z Chrome` (Stable ID: 325, utworzony: 2024-10-12, 9 plików, 74.6 MB)
- `Zapisane z Chrome (1)` (Stable ID: 30329, utworzony: 2026-02-04, 15 plików, 10.7 MB)

#### Analiza zawartości pobranej z przeglądarki:
1. **Sport i turnieje dzieci (Tenis):**
   - `regulamin_turniejowy_tenis10_na_2024_rok.pdf` (2024)
   - `Tenisowa_Talentiada_2024_zasady_gry.pdf` (2025)
   - `TENIS10_CHŁ.pdf`, `DRABINKI_DMW_2026.pdf`, `REGULAMIN_DMW_2026.pdf` (kwiecień 2026)
2. **Karty pracy i szkoła dzieci:**
   - `karty_pracy_4_v_6_dodawanie_i_odejmowanie_ulamkow_karty_v_6_1_v_6_2.pdf` (kwiecień 2026)
   - `powtórzenie_1_Test___ekowydruk.pdf` (październik 2025)
3. **Sport i rekreacja Pawła:**
   - `Skipass-Livigno-mappa-impianti-attivita-A3-2025_2026.pdf` (luty 2026)
   - `WynikiMaraton.pdf` (47.9 MB), `Wyniki10km.pdf` (26.5 MB) (październik 2025)
4. **Haszowane zrzuty sesyjne z systemów e-usług:**
   - `0q652g12310r3w0z2n270k042831012b0m021v0q08270h092f000q2a0m032b0m05260i0d1137332d.pdf`
   - W `Root`: `0d5a2mpppx6h1lwz06r0m4okatv9.pdf` (6.3 MB)

#### Przyczyna powstania duplikatu `(1)`:
Folder z przyrostkiem `(1)` powstał 4 lutego 2026 r. o godz. 13:24. Jest to klasyczny objaw **kolizji identyfikatora Drive API**:
Gdy Paweł przesiadł się na nową maszynę, zalogował do innego profilu w Google Chrome lub zreinstalował rozszerzenie *Save to Google Drive*, wtyczka wysłała zapytanie o utworzenie folderu `Zapisane z Chrome`. Ponieważ nie odnalazła poprzedniego ID w lokalnym cache rozszerzenia, Google Drive API utworzyło nowy folder o tej samej nazwie bazowej, dodając automatyczny sufiks `(1)`. Od tego momentu pliki z 2026 roku trafiały do nowego folderu, a stary z 2024-2025 roku pozostał osierocony.

---

### 1.4. Obsydian, Analiza Matematyczna WEiTI PW i Edukacja

#### Tajemnica pustego folderu `11. Obsydian`:
- Utworzony: **2026-07-11 22:39**
- Ostatnio otwarty: **2026-07-23 19:42**
- Liczba plików: **0**, Rozmiar: **0.0 B**

**Diagnoza PKM:**  
Folder z numerem `11.` dowodzi, że w lipcu 2026 r. Paweł podjął próbę wdrożenia metodologii Second Brain / Obsidian do swojej taksonomii. Próba została porzucona po 12 dniach bez zapisania ani jednego pliku w chmurze.  
Przyczyna jest natury technologicznej: **Obsidian Mobile na systemach iOS/iPadOS nie potrafi natywnie otwierać sejfów (vaults) zlokalizowanych w usłudze Google Drive**. Wymaga to albo natywnego iCloud Drive, płatnej usługi Obsidian Sync, albo skomplikowanych wtyczek synchronizujących przez protokół S3/WebDAV (np. Remotely Save). Po napotkaniu tarcia synchronizacyjnego między iPadem a Makiem proces został przerwany, a pusty folder pozostał w `Root`.

#### Świeży strumień akademicki: `Analiza Matematyczna WEiTI`:
W dniach **11-16 września 2026 r.** (kilka dni przed niniejszą analizą!) na dysku nastąpiła intensywna aktywność związana z kursem akademickim:
1. W `Root` pojawił się folder bez numeru: `Analiza_Matematyczna_WEiTI`.
2. Wewnątrz folderu wygenerowano serię plików DOCX:
   - `01-fundamenty-analizy.docx`
   - Aż **7 kolejnych instancji** pliku `Analiza_Matematyczna_WEiTI_PW_Podrecznik.docx` (powstałych w pętli kompilacji skryptów ze skillów agentowych, takich jak `markdown-latex-to-gdoc`).
3. W `Root` wylądowały luźne pliki z tej samej sesji roboczej:
   - `Analiza_Matematyczna_WEiTI_PW_Podrecznik.gdoc` (126.7 KB)
   - `wprowadzenie-do-calek.gdoc` (9.2 KB)
   - `wprowadzenie-do-calek.docx` (15.7 KB)

Zjawisko to pokazuje, że Paweł używa agentów AI i środowiska terminalowego do konwersji notatek Markdown/LaTeX na format Google Docs. Brak precyzyjnie określonej ścieżki wyjściowej w skryptach powoduje, że skompilowane dokumenty lądują bezpośrednio w `Root` Dysku zamiast w dedykowanym podfolderze tematycznym.

---

### 1.5. Zrzuty Zdjęć i Plików Ad-hoc do Root (Zjawisko "Flat Dump Drift")

W katalogu `Root` znajduje się grupa plików wrzuconych „w biegu”, bez jakiejkolwiek próby kategoryzacji:
1. **Pakiet 12 zdjęć ze smartfona:**  
   Pliki od `IMG_2312.jpeg` do `IMG_2323.jpeg` (łączna waga: ~60 MB) posiadają identyczny znacznik czasu modyfikacji: **2026-04-14 17:38:xx**.  
   *Przyczyna:* Masowy upload zdjęć z poziomu aplikacji Google Drive na telefonie lub zaznaczenie grupy plików w Finderze i upuszczenie ich w oknie przeglądarki na stronę `drive.google.com`.
2. **Krytyczne zagrożenie bezpieczeństwa i prywatności (Dokumenty Tożsamości w Root):**  
   W katalogu głównym leżą dwa skany dowodów osobistych:
   - `Dowód osobisty - Paweł Trzeciakowski.pdf` (857.4 KB, modyfikowany: 2024-02-05)
   - `Dowód osobisty - mama.pdf` (817.7 KB, modyfikowany: 2024-02-05)  
   Oraz folder `91🔑Hasła`.  
   *Ryzyko:* Pliki leżące w `Root` są najbardziej narażone na przypadkowe udostępnienie linkiem, błąd uprawnień dziedziczonych lub ekspozycję podczas udostępniania ekranu na spotkaniach roboczych.
3. **Śmieci i porzucone szkice (Ghost Drafts):**
   - `Dokument bez tytułu.gdoc` (1.7 KB, 2026-06-05)
   - `Dokument bez tytułu (1).gdoc` (367.3 KB, 2026-07-26)
   - `Dokument bez tytułu (2).gdoc` (5.3 KB, 2026-09-04)
   - `Arkusz kalkulacyjny bez tytułu.gsheet` (43.0 KB, 2026-06-21)  
   Są to efekty otwarcia narzędzi skrótem przeglądarkowym (`doc.new`, `sheet.new`), wklejenia fragmentu tekstu w celu szybkiej edycji i zamknięcia karty bez nadania nazwy ani przeniesienia do folderu.

---

# Rozdział 2: Wdrożenie Wzorca Inbox / Staging (`00📥Inbox`)

### 2.1. Filozofia Wzorca: Rozdzielenie Przechwytywania od Organizacji

Główną przyczyną zaśmiecania `Root` jest **tarcie poznawcze (cognitive friction)**:
Gdy Paweł szybko eksportuje tabelę z Gemini, pobiera regulamin turnieju tenisowego córki albo zrzuca 12 zdjęć z telefonu, nie ma czasu ani energii mentalnej na przeklikiwanie się przez 8 185 podfolderów w poszukiwaniu ścieżki `Mój dysk / 01 Rodzina / 03 Nadia / Turnieje / 2026`. Wybiera najprostszą ścieżkę – zrzuca plik w pierwsze dostępne miejsce.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                    ZASADA ŻELAZNA ARCHITEKTURY DYSKU                         │
│                                                                              │
│       Katalog główny "Mój dysk" (Root) musi mieć ZAWSZE DOKŁADNIE 0 PLIKÓW   │
│             Wszystkie zrzuty "w biegu" trafiają wyłącznie do:                │
│                                00📥Inbox                                     │
└──────────────────────────────────────────────────────────────────────────────┘
```

Wzorzec **Inbox / Staging** pozwala zachować maksymalną prędkość pracy (Zero Friction Capture), przenosząc decyzję o docelowej kategoryzacji na dedykowany, bezstresowy moment w tygodniu.

---

### 2.2. Specyfikacja Folderu `00📥Inbox`

W katalogu głównym tworzymy jeden uniwersalny bufor o ustalonej strukturze wewnętrznej:

```
Mój dysk/
└── 00📥Inbox/
    ├── 📥_Zrzuty_i_Skaner/        <-- Domyślny folder dla telefonu, skanów i uploadu z Maca
    ├── 🤖_AI_Exports/             <-- Dedykowany bufor dla eksportów z Gemini / ChatGPT / skryptów
    ├── 🌐_Chrome_Downloads/       <-- Jedyny punkt docelowy wtyczki "Save to Google Drive"
    ├── 📱_Notability_Staging/     <-- Punkt zrzutu eksportów z iPada (PDF / Notatki)
    └── 📐_Studia_i_Matematyka/    <-- Bufor skryptów kompilacji LaTeX/DOCX dla WEiTI i dzieci
```

#### Etykiety i identyfikacja wizualna:
- Przedrostek `00📥` gwarantuje, że folder znajduje się **na samej górze listy alfabetycznej** zarówno w widoku webowym, jak i w mobilnej aplikacji Google Drive oraz w oknie dialogowym wyboru folderu w Chrome.
- Kolor folderu w Google Drive: **Czerwony (Flamingo / Tomato)** – sygnalizuje tymczasowość i konieczność przetworzenia.

---

### 2.3. Twarde Zasady Retencji i SLA dla Inboxa

Inbox nie jest miejscem przechowywania – jest buforem tranzytowym o określonym czasie życia danych:

| Typ zawartości | SLA w Inbox | Akcja po przekroczeniu SLA | Reguła decyzyjna |
| :--- | :--- | :--- | :--- |
| **Pliki bez tytułu (`Dokument bez tytułu*`)** | **7 dni** | Automatyczny Kosz (Trash) | Jeśli przez 7 dni plik nie zyskał tytułu, był jednorazowym brudnopisem. |
| **Pobrane regulaminy i bilety sportowe** | **14 dni** | Przeniesienie do `01 Rodzina` lub `08 Wakacje` | Po zakończeniu wydarzenia: archiwum lub kosz. |
| **Eksporty rozmów z AI (`_AI_Exports`)** | **14 dni** | Przeniesienie do Projektu lub usunięcie | Jeśli synteza trafiła do notatki głównej, plik roboczy usuwamy. |
| **Zrzuty zdjęć (`IMG_*.jpeg`)** | **7 dni** | Przeniesienie do `88📸Zdjęcia/YYYY/MM` | Dysk Google nie służy do przechowywania surowych zdjęć w buforze. |
| **Skan dowodu tożsamości / Umowy** | **24 godziny** | Natychmiastowe przeniesienie do Sejfu | Bezwzględny zakaz przebywania danych wrażliwych w buforze. |

---

# Rozdział 3: Automatyzacja i Integracja Ekosystemu

Prawdziwy sukces wdrożenia zależy od odciążenia woli człowieka przez automatyzację techniczną. Poniżej znajdują się konkretne instrukcje konfiguracji poszczególnych narzędzi.

---

### 3.1. Przechwytywanie Eksportów z AI (Gemini i ChatGPT)

Ponieważ webowy interfejs Google Gemini nie posiada w ustawieniach opcji wyboru folderu zapisu, rozwiązujemy ten problem za pomocą **Google Apps Script (GAS)**, który działa w tle na serwerach Google bez konieczności instalowania czegokolwiek na komputerze Pawła.

#### Gotowy skrypt do wdrożenia w Google Apps Script:
Skrypt ten monitoruje katalog `Root`, wykrywa pliki o charakterystycznych nazwach promptowych lub utworzone przez aplikacje webowe Google i automatycznie przenosi je do podfolderu `00📥Inbox/🤖_AI_Exports`.

```javascript
/**
 * Auto-Triage Root to Inbox for Google Drive
 * Autor: Workflow & Automation Agent for Paweł Trzeciakowski
 * Wyzwalacz: Uruchamianie co 1 godzinę (Time-driven trigger)
 */
function triageRootToInbox() {
  const root = DriveApp.getRootFolder();
  const inboxName = "00📥Inbox";
  const aiSubfolderName = "🤖_AI_Exports";
  
  // 1. Znajdź lub utwórz folder Inbox oraz podfolder AI
  let inboxFolder = getOrCreateFolder(root, inboxName);
  let aiFolder = getOrCreateFolder(inboxFolder, aiSubfolderName);
  
  // 2. Wzorce promptowe charakterystyczne dla eksportów LLM
  const promptRegex = /^(czy możesz|super, dodaj|serio\?|dobrze, biorąc|jeszcze raz|wygeneruj mi|zrób z tego|napisz mi|podsumuj|analiza|dokument bez tytułu|arkusz kalkulacyjny bez tytułu)/i;
  
  const files = root.getFiles();
  let movedCount = 0;
  
  while (files.hasNext()) {
    let file = files.next();
    let name = file.getName();
    
    // Ignorujemy skróty i pliki już będące w podfolderach
    // Sprawdzamy czy rodzicem pliku jest bezpośrednio Root
    let parents = file.getParents();
    let isDirectRootChild = false;
    while (parents.hasNext()) {
      if (parents.next().getId() === root.getId()) {
        isDirectRootChild = true;
        break;
      }
    }
    
    if (!isDirectRootChild) continue;
    
    // Wykrywanie eksportów promptowych z AI
    if (promptRegex.test(name) || name.includes("... (1)") || name.endsWith("....gdoc")) {
      Logger.log("Przenoszenie pliku AI: " + name);
      file.moveTo(aiFolder);
      movedCount++;
    } 
    // Wykrywanie luźnych zdjęć z telefonu w Root
    else if (name.match(/^IMG_\d{4}\.(jpe?g|png)$/i)) {
      let photoInbox = getOrCreateFolder(inboxFolder, "📥_Zrzuty_i_Skaner");
      Logger.log("Przenoszenie zdjęcia do zrzutów: " + name);
      file.moveTo(photoInbox);
      movedCount++;
    }
  }
  
  Logger.log("Pomyślnie uporządkowano " + movedCount + " plików z Root.");
}

function getOrCreateFolder(parent, folderName) {
  let folders = parent.getFoldersByName(folderName);
  if (folders.hasNext()) {
    return folders.next();
  }
  return parent.createFolder(folderName);
}
```

> **Procedura instalacji (5 minut):**
> 1. Wejdź na stronę [script.google.com](https://script.google.com) i kliknij **Nowy projekt**.
> 2. Nadaj projektowi nazwę: `GDrive_Root_AutoTriage`.
> 3. Wklej powyższy kod do pliku `Kod.gs`.
> 4. Kliknij ikonę zegara po lewej stronie (**Wyzwalacze**) -> **Dodaj wyzwalacz**:
>    - Funkcja: `triageRootToInbox`
>    - Źródło zdarzenia: `Uruchamiane w czasie`
>    - Typ wyzwalacza: `Licznik godzinowy` -> `Co godzinę`.
> 5. Zezwól na uprawnienia konta Google przy pierwszym uruchomieniu. Od tej pory każdy plik promptowy z Gemini samoczynnie zniknie z `Root` i wyląduje w `00📥Inbox/🤖_AI_Exports`.

---

### 3.2. Unifikacja i Konfiguracja Pobierania z Chrome

Rozwiązanie problemu folderów `Zapisane z Chrome` oraz `Zapisane z Chrome (1)`:

```
KROK 1: Konsolidacja danych
┌───────────────────────────┐    ┌───────────────────────────┐
│     Zapisane z Chrome     │    │   Zapisane z Chrome (1)   │
│   (9 plików, 74.6 MB)     │    │   (15 plików, 10.7 MB)    │
└─────────────┬─────────────┘    └─────────────┬─────────────┘
              │                                │
              └───────────────┬────────────────┘
                              ▼
        Przeniesienie wartościowych plików do:
        • Regulaminy tenisa -> 01 Rodzina / Turnieje
        • Wyniki maratonu   -> 85 Bieganie
        • Skipass Livigno   -> 08 Wakacje / 2026 Zima
                              │
                              ▼
KROK 2: Usunięcie starych pustych folderów
KROK 3: Przepięcie wtyczki "Save to Google Drive" na:
        00📥Inbox / 🌐_Chrome_Downloads
```

#### Instrukcja konfiguracji wtyczki w Chrome:
1. Kliknij prawym przyciskiem myszy ikonę wtyczki **Save to Google Drive** na pasku rozszerzeń Chrome -> wybierz **Opcje rozszerzenia (Options)**.
2. W polu **Save to Folder** kliknij **Change Folder**.
3. Wskaż nowo utworzony folder: `00📥Inbox / 🌐_Chrome_Downloads`.
4. W sekcji **Convert to Google format** upewnij się, że opcja automatycznej konwersji dokumentów HTML na format Google Docs jest **wyłączona** (zapobiega to powstawaniu zniekształconych dokumentów).

---

### 3.3. Integracja Notability z Ekosystemem Dysku

Aplikacja Notability posiada wbudowany moduł *Auto-Backup*, który obecnie zaśmieca `Root` równoległą strukturą. Należy dokonać rekonfiguracji parametrów kopii zapasowej na iPadzie Pawła.

```
                    ┌─────────────────────────────────────────────────────────┐
                    │       REKONFIGURACJA NOTABILITY AUTO-BACKUP NA IPADZIE  │
                    └─────────────────────────────────────────────────────────┘
                                                 │
         ┌───────────────────────────────────────┴──────────────────────────────────────┐
         ▼                                                                              ▼
┌──────────────────────────────────────┐                       ┌──────────────────────────────────────┐
│        LOKALIZACJA DOCELOWA          │                       │            FORMAT ZAPISU             │
├──────────────────────────────────────┤                       ├──────────────────────────────────────┤
│ Zmień ścieżkę z:                     │                       │ Zmień z "Note + PDF" na:             │
│   /Notability                        │                       │   WYŁĄCZNIE "PDF" (Wektorowy)        │
│ Na:                                  │                       │                                      │
│   /95💽Kopia zapasowa/Notability_Sync│                       │ Korzyści:                            │
│                                      │                       │ • Wyszukiwarka Google Drive indeksuje│
│ Korzyść:                             │                       │   odręczne pismo (OCR Google Drive)  │
│ Cały folder znika z Roota i ląduje w │                       │ • Likwidacja zdublowanych plików .note│
│ sekcji bezpiecznych backupów.        │                       │ • Możliwość podglądu na telefonie    │
└──────────────────────────────────────┘                       └──────────────────────────────────────┘
```

#### Procedura krok po kroku na iPadzie:
1. Otwórz **Notability** na iPadzie -> kliknij ikonę **Ustawień** (koło zębate w lewym dolnym rogu).
2. Przejdź do zakładki **Auto-Backup**.
3. Wybierz usługę **Google Drive**:
   - **Destination Folder:** Kliknij i wybierz ścieżkę `95💽Kopia zapasowa / Notability_Backup` (zamiast domyślnego `/Notability`).
   - **Format:** Wybierz format **PDF** (opcjonalnie: PDF with Audio, jeśli Paweł nagrywa wykłady z matematyki).
4. Jeśli Paweł chce eksportować pojedyncze wypracowane notatki (np. gotowy arkusz z zadaniami dla syna czy schemat architektoniczny z pracy):
   - Nie polegaj na Auto-Backupie!
   - Użyj funkcji **Udostępnij (Share) -> Dysk Google** i wskaż bezpośrednio `00📥Inbox/📱_Notability_Staging` lub konkretny folder docelowy (`02🏫Szkoła`).

---

### 3.4. Rozwiązanie Problemu Obsidiana i Matematyki (WEiTI PW)

#### Rekomendacja dla Obsidiana (Second Brain):
Próba trzymania Vaulta Obsidiana na Dysku Google w folderze `11. Obsydian` zakończyła się fiaskiem z przyczyn technicznych. Dysk Google na macOS działa w trybie wirtualnego systemu plików (DriveFS / CloudProvider), co generuje blokady plików konfiguracyjnych `.obsidian/workspace.json` i uniemożliwia pracę na iPadzie.

**Zalecana architektura dwutorowa:**
1. **Dla notatek technicznych i kodu (macOS):**  
   Vault powiązany z lokalnym systemem plików i synchronizowany przez **prywatne repozytorium Git (GitHub / GitLab)**.  
   - W repozytorium `gen-ai-orchestrator` istnieje już infrastruktura agentowa. Notatki markdownowe powinny leżeć lokalnie w repozytorium gita.
2. **Dla notatek mobilnych (iPad/iPhone):**  
   Jeśli Paweł chce czytać i edytować notatki na iPadzie, najprostszym i w 100% bezawaryjnym rozwiązaniem w ekosystemie Apple jest przeniesienie folderu Vault do **iCloud Drive** lub skorzystanie z wtyczki `Remotely Save` (skonfigurowanej z bezpiecznym bucketem Cloud Storage / WebDAV), a całkowite usunięcie martwego folderu `11. Obsydian` z Dysku Google.

#### Uporządkowanie Strumienia "Analiza Matematyczna WEiTI":
Pliki w Root (`Analiza_Matematyczna_WEiTI_PW_Podrecznik.gdoc`, `wprowadzenie-do-calek.gdoc`) oraz luźny folder `Analiza_Matematyczna_WEiTI` wymagają włączenia do jednolitej taksonomii:
1. Przenieś folder `Analiza_Matematyczna_WEiTI` do:  
   `02🏫Szkoła / Studia_WEiTI_PW / Analiza_Matematyczna`  
   (lub jeśli dotyczy to projektów własnych / pasji matematycznej: `20📚 ebooks + audobooks / Studia_i_Nauka`).
2. Skonfiguruj skrypty generujące DOCX/GDOC (ze skilli `markdown-latex-to-gdoc`):
   - Zmień parametr wyjściowy docelowego katalogu: zamiast generować pliki w bieżącym katalogu roboczym (co skutkuje zrzutem do Roota w przypadku odpalania z poziomu DriveFS), skrypt musi jawnie zapisywać wynik do:  
     `/Volumes/GoogleDrive/My Drive/00📥Inbox/📐_Studia_i_Matematyka/` lub bezpośrednio do folderu przedmiotu.

---

### 3.5. Protokół Bezpieczeństwa dla Danych Wrażliwych (RODO / Tożsamość)

Znajdujące się w `Root` skany dowodów tożsamości oraz folder haseł muszą zostać natychmiast zabezpieczone:
1. Utwórz folder o podwyższonym rygorze:  
   `01👨‍👩‍👧‍👦 Rodzina / 00 ‼️ Ważne dokumenty / 🔒_Dokumenty_Tozsamosci`
2. Przenieś tam natychmiast:
   - `Dowód osobisty - Paweł Trzeciakowski.pdf`
   - `Dowód osobisty - mama.pdf`
   - Zawartość folderu `91🔑Hasła` (po czym usuń folder `91` z Roota).
3. **Audyt uprawnień (Sharing Audit):**  
   Upewnij się, że folder `00 ‼️ Ważne dokumenty` ma wyłączone udostępnianie linkiem (`Ogólny dostęp: Zastrzeżony`), a dostęp mają wyłącznie zweryfikowane, prywatne konta Pawła i żony.

---

# Rozdział 4: Nawyki Utrzymania Porządku (Weekly Review wg GTD & PARA)

System techniczny jest tylko tak skuteczny, jak nawyki człowieka, który z niego korzysta. Aby zapobiec powtórnemu narastaniu chaosu, wdrażamy 15-minutowy rytuał przeglądu tygodniowego oparty o metodologię **Getting Things Done (David Allen)** oraz **PARA (Tiago Forte)**.

---

### 4.1. Architektura Docelowa Dysku po Wdrożeniu PARA

Łączymy intuicyjną numerację dziesiętną Pawła ze sprawdzonym podziałem PARA (Projects, Areas, Resources, Archives):

```
MÓJ DYSK (ROOT) - MAKSYMALNIE 12 FOLDERÓW, 0 PLIKÓW LUZEM:
├── 00📥Inbox                        <-- [INBOX] Jedyne lądowisko dla tymczasowych zrzutów
│
├── 01👨‍👩‍👧‍👦 Rodzina                   <-- [AREAS] Sprawy domowe, zdrowie, tożsamość, dzieci
│   ├── 00 ‼️ Ważne dokumenty (w tym 🔒_Dokumenty_Tozsamosci)
│   ├── 03 Nadia (tenis, osiągnięcia)
│   ├── 04 Michał (szkoła, sport)
│   └── 05 Kuba
├── 02🏫Szkoła                       <-- [AREAS / PROJECTS] Edukacja dzieci i studia WEiTI PW
├── 03🏥Zdrowie                      <-- [AREAS] Dokumentacja medyczna, wyniki badań, zalecenia
├── 05💰Finanse                      <-- [AREAS] Budżet domowy, podatki, inwestycje, nieruchomości
├── 06🏠Mieszkanie / Nieruchomości   <-- [AREAS] Sprawy lokalowe (scalenie z 15 Lewickie, 16 Pokój)
├── 07🏢Praca                        <-- [PROJECTS / AREAS] Aktywne projekty i historia zatrudnienia
│   ├── 2026 - HSBC
│   ├── 2025 - Allegro
│   └── 2018 - Roche
├── 08🏖️Wakacje                      <-- [PROJECTS] Wyjazdy i plany turystyczne
├── 09🚗Samochód                     <-- [AREAS] Pojazdy, ubezpieczenia (przeniesione z 10 Ubezpieczenia)
│
├── 20📚Wiedza i Zasoby              <-- [RESOURCES] E-booki, materiały edukacyjne, podręczniki PW
└── 95💽Archiwum i Kopie             <-- [ARCHIVES] Scalone: 95 Kopie zapasowe, 96 Archiwum, 25 Stare dokumenty
```

*Zlikwidowane / Scalone z Roota:*
- `Analiza_Matematyczna_WEiTI` -> włączona do `02🏫Szkoła`.
- `Gemini Gems` -> przeniesione do `20📚Wiedza i Zasoby / AI_Gems` lub pozostawione jako ukryty folder aplikacji.
- `Notability` -> przekierowane do `95💽Archiwum i Kopie / Notability_Backup`.
- `Zapisane z Chrome` oraz `(1)` -> usunięte, ruch skierowany do `00📥Inbox`.
- `11. Obsydian` -> usunięty (pusty).
- `91🔑Hasła` -> przeniesione do bezpiecznego sejfu w `01 Rodzina`.
- `10 Ubezpieczenie` -> włączone do `09 Samochód` i `01 Rodzina`.

---

### 4.2. Gotowa Checklista: 15-Minutowy Rytuał "Weekly Review"

Rytuał wykonywany w każdy **piątek o 16:30** (przed zakończeniem tygodnia pracy) lub w **niedzielę o 20:00**:

```markdown
# [ ] CHECKLISTA COTYGODNIOWEGO PRZEGLĄDU DYSKU (WEEKLY REVIEW)

### Faza 1: Zero Root (Czas: 2 minuty)
- [ ] Otwórz "Mój dysk" na komputerze.
- [ ] Czy w katalogu głównym leżą jakiekolwiek pliki luzem?
  - Jeśli TAK: Zaznacz wszystkie i przeciągnij jednym ruchem do "00📥Inbox".
  - Upewnij się, że widok główny wyświetla wyłącznie foldery systemowe (Zero Files in Root).

### Faza 2: Opróżnianie Inboxa (Triage) (Czas: 8 minut)
- [ ] Otwórz folder "00📥Inbox".
- [ ] Przejdź do podfolderu "🤖_AI_Exports":
  - Czy podsumowanie z Gemini/ChatGPT jest powiązane z aktywnym projektem? 
    -> TAK: Zmień nazwę pliku na merytoryczną (np. "Snowflake - Architektura Semantyczna") i przenieś do "07🏢Praca".
    -> NIE: Przenieś do Kosza.
- [ ] Przejdź do podfolderu "🌐_Chrome_Downloads":
  - Pobrane regulaminy tenisowe / karty pracy -> przenieś do "01 Rodzina" lub "02 Szkoła".
  - Haszowane pliki tymczasowe / bilety po terminie -> Kosz.
- [ ] Przejdź do podfolderu "📥_Zrzuty_i_Skaner":
  - Zdjęcia rodzinne -> przenieś do "88📸Zdjęcia/2026/09".
  - Skany dokumentów urzędowych -> przenieś do właściwego podfolderu "01 Rodzina".

### Faza 3: Higiena Śmieci i Brudnopisów (Czas: 3 minuty)
- [ ] Wpisz w wyszukiwarkę Dysku: `title:"Dokument bez tytułu" OR title:"Arkusz kalkulacyjny bez tytułu"`
- [ ] Zaznacz znalezione puste szkice i naciśnij [Delete].
- [ ] Opróżnij Kosz (jeśli nie ma w nim nic krytycznego) lub pozwól na automatyczne czyszczenie po 30 dniach.

### Faza 4: Bezpieczeństwo i Spokój Umysłu (Czas: 2 minuty)
- [ ] Sprawdź czy żaden plik tożsamościowy nie został przypadkowo udostępniony publicznym linkiem.
- [ ] GOTOWE! Czysty dysk, pełna jasność umysłu przed nowym tygodniem.
```

---

### 4.3. Instrukcja Szybkiej Realizacji na Dziś (Action Plan)

Aby natychmiast odzyskać kontrolę nad dyskiem, zaleca się wykonanie poniższych 4 kroków:

1. **Krok 1 (Stworzenie Inboxa):** Utwórz w katalogu głównym folder `00📥Inbox` oraz jego 4 podfoldery (`_Zrzuty_i_Skaner`, `_AI_Exports`, `_Chrome_Downloads`, `_Studia_i_Matematyka`).
2. **Krok 2 (Ewakuacja 49 plików z Root):**  
   - Przenieś 2 dowody osobiste i folder `91🔑Hasła` do `01👨‍👩‍👧‍👦 Rodzina / 00 ‼️ Ważne dokumenty`.
   - Przenieś 4 pliki bez tytułu do Kosza.
   - Przenieś 12 zdjęć `IMG_2312-2323` do `88📸Zdjęcia / 2026 / 04`.
   - Przenieś pliki `Analiza_Matematyczna...` i `wprowadzenie-do-calek` do `00📥Inbox / 📐_Studia_i_Matematyka`.
   - Pozostałe 25 plików z promptami i analizami przenieś do `00📥Inbox / 🤖_AI_Exports`.
   - **Efekt natychmiastowy:** Licznik plików w `Root` spada z 49 do **DOKŁADNIE 0**.
3. **Krok 3 (Wdrożenie automatyzacji GAS):** Skopiuj i uruchom przygotowany w rozdziale 3.1 skrypt Google Apps Script, aby automatyzacja na bieżąco pilnowała czystości `Root`.
4. **Krok 4 (Rekonfiguracja narzędzi):** Zmień ścieżkę zapisu we wtyczce Chrome na `00📥Inbox / 🌐_Chrome_Downloads` oraz przestaw Auto-Backup w Notability na iPadzie do `95💽Kopia zapasowa / Notability_Backup`.

---
*Raport opracowany w ramach projektu optymalizacji procesowej środowiska cyfrowego Pawła Trzeciakowskiego.*
