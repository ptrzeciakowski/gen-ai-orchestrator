# Analiza Operacyjna: Uprawnienia, Automatyzacja Migracji i Rozstrzygnięcie Kwestii Emoji

**Identyfikator dokumentu:** `08-explore`  
**Autor:** Antigravity  
**Właściciel zasobów:** Paweł Trzeciakowski (`ptrzeciakowski@gmail.com`)  
**Data opracowania:** 11 października 2026 r.  
**Kontekst:** Wdrożenie nowej architektury katalogów Dysku Google ("Lean Knowledge & Asset Hub") w oparciu o mapę migracji [`07-mapa.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/gdrive-structure-and-file-naming/07-mapa.md) oraz specyfikację z [`06-optymalna-struktura-i-procesy-zarzadzania.md`](file:///Users/pawel/git/gen-ai-orchestrator/openspec/changes/gdrive-structure-and-file-naming/06-optymalna-struktura-i-procesy-zarzadzania.md).

---

## Rozdział 1: Mechanika Uprawnień po Przeniesieniu Plików i Folderów

Wdrożenie nowej struktury rodzi kluczowe pytanie o bezpieczeństwo: **co dzieje się z dostępem osób trzecich, linkami oraz poufnością po relokacji zasobów?**

Dysk Google zarządza uprawnieniami w modelu hybrydowym, łączącym **uprawnienia jawne (Explicit / Direct)** z **uprawnieniami dziedziczonymi (Inherited)**.

```
                    CYKL ŻYCIA UPRAWNIEŃ PRZY OPERACJI MOVE
                    
    [ Stary Folder ]                                    [ Nowy Folder ]
  (np. Mój dysk / Root)                             (np. 01-👨‍👩‍👧‍👦-Rodzina)
          │                                                   │
     [ Plik X ] ────────────────────────────────────────► [ Plik X ]
   ID pliku: STAŁE                                     ID pliku: IDENTYCZNE!
   
   • Uprawnienia bezpośrednie (nadane imiennie):       POZOSTAJĄ (100% zachowane)
   • Dostęp przez link (Anyone with link):             POZOSTAJE (linki nie wygasają)
   • Dziedziczenie ze starego folderu:                 UTRACONE
   • Dziedziczenie z nowego folderu:                   AUTOMATYCZNIE NABYTE
```

### 1.1. Niezmienność Identyfikatora Obiektu (`file_id`)
* W Dysku Google operacja przeniesienia (`move`) to zmiana wskaźnika rodzica (`parents`). **Plik nie jest kopiowany ani kasowany**.
* Identyfikator pliku (`file_id` w URL, np. `drive.google.com/file/d/1A2B3C...`) pozostaje **dokładnie taki sam**.
* Oznacza to, że:
  1. Wszystkie wysłane wcześniej linki do Dokumentów, Arkuszy i PDF-ów **będą działać bez zakłóceń**.
  2. Historia wersji, komentarze, sugestie i historia zmian zostają nienaruszone.
  3. Skróty lokalne i zakładki w przeglądarce nie ulegają uszkodzeniu.

### 1.2. Uprawnienia Jawne (Explicit Permissions) vs Dziedziczone
* **Uprawnienia nadane bezpośrednio na pliku**: Jeśli udostępniłeś dany plik konkretnej osobie (np. księgowej lub żonie) z rolą *Edytor* lub *Przeglądający*, uprawnienie to podróżuje razem z plikiem, niezależnie od tego, do jakiego podfolderu go przesuniesz.
* **Uprawnienia dziedziczone z folderu docelowego**:
  * Plik natychmiast **przejmuje uprawnienia folderu, do którego wpada**.
  * *Scenariusz praktyczny:* Jeśli folder `01-👨‍👩‍👧‍👦-Rodzina/` jest współdzielony z żoną, a Ty przeniesiesz tam plik `Wzrost Nadii i Michała.gsheet` z katalogu głównego, żona natychmiast zyska do niego dostęp.
  * *Ostrzeżenie interfejsu:* Gdy wykonujesz przeniesienie przez przeglądarkę, Dysk wyświetla monit: *"Przeniesienie tego elementu spowoduje zmianę osób, które mają do niego dostęp"*. Jest to oczekiwane zachowanie systemu.

### 1.3. Strefa Podwyższonej Poufności: `00-🔒-Poufne-Dokumenty/`
* Pliki leżące obecnie luzem w Root (`Dowód osobisty - Paweł Trzeciakowski.pdf`, `Dowód osobisty - mama.pdf`) miały dotychczas uprawnienia prywatne (dostęp wyłącznie właściciel).
* **Zasada Sejfu**: Folder docelowy `00-🔒-Poufne-Dokumenty/` musi pozostać w 100% prywatny (`Współdzielenie: Wyłączone`, brak uprawnień dla osób trzecich).
* Przeniesienie tam skanów tożsamości izoluje je od przypadkowego udostępnienia całych gałęzi tematycznych. Dodatkowo pliki te powinny zostać zaszyfrowane kliencko (np. Cryptomator / 7-Zip AES-256).

### 1.4. Pliki Niebędące Własnością Pawła (`is_owner = False` – 73 pliki)
* Pliki dodane z widoku *Udostępnione dla mnie* funkcjonują w `Mój dysk` jako **skróty (Shortcuts)**.
* Przeniesienie skrótu w nową strukturę katalogów porządkuje Twój widok, ale **w żaden sposób nie ingeruje w uprawnienia pliku oryginalnego** ani w strukturę u właściwego właściciela.

---

## Rozdział 2: Automatyzacja Procesu Migracji

Ręczne przeklikiwanie 28 folderów głównych, setek podfolderów i 52 plików w przeglądarce byłoby czasochłonne i podatne na błędy ludzkie. **Całość można zrealizować w pełni automatycznie.**

### 2.1. Porównanie Dostępnych Ścieżek Automatyzacji

| Kryterium | Ścieżka A: Skrypt Python CLI (macOS) | Ścieżka B: Google Apps Script (Cloud) | Ścieżka C: Google Drive API v3 |
| :--- | :--- | :--- | :--- |
| **Środowisko** | Lokalnie w terminalu Maca | Przeglądarka / Serwery Google | Aplikacja Python + token OAuth2 |
| **Mechanizm** | Operacje na `~/Library/CloudStorage/...` | Natywne API `DriveApp.moveTo()` | REST API v3 (patch `parents`) |
| **Zużycie łącza / pobieranie** | **Zero pobierania** (metadane w File Provider) | **Zero pobierania** (100% po stronie Google) | Zero pobierania |
| **Tryb bezpieczny (Dry-Run)** | **Tak** (pełna symulacja w konsoli) | Wymaga ręcznego kodowania logów | Tak |
| **Obsługa wielkich plików (Takeout)** | Wymaga jawnego pominięcia (ochrona przed I/O) | Bez znaczenia (operacja w chmurze) | Bez znaczenia |
| **Trudność uruchomienia** | **Bardzo niska** (zwykły skrypt `.py`) | Niska (wklejenie kodu w Apps Script) | Średnia (konfiguracja GCP Console) |

### 2.2. Rekomendowana Strategia: Skrypt Python na macOS z Trybem `--dry-run`

Ponieważ Dysk Google jest zamontowany w macOS jako wirtualny system plików (`File Provider`), system udostępnia lokalny punkt montowania:
```bash
/Users/pawel/Library/CloudStorage/GoogleDrive-ptrzeciakowski@gmail.com/Mój dysk/
```

**Dlaczego to działa bez pobierania gigabajtów danych?**
* W systemie plików macOS operacja `os.rename(sciezka_zrodlowa, sciezka_docelowa)` w ramach tego samego wolumenu chmurowego jest **operacją atomową na metadanych** (POSIX rename).
* System nie przesyła treści plików przez łącze internetowe – aplikacja Google Drive for desktop jedynie rejestruje zmianę wskaźnika katalogu i wysyła do chmury lekkie zapytanie aktualizujące rodzica (`update parent folder`).

### 2.3. Trzypoziomowy Protokół Bezpieczeństwa Skryptu
1. **Faza 0 (Pre-Flight Checks)**: Skrypt sprawdza dostępność ścieżek, normalizuje znaki Unicode (obsługa dekompozycji NFD typowej dla macOS) i weryfikuje istnienie plików.
2. **Faza 1 (Dry-Run)**: Domyślny tryb symulacji. Skrypt generuje szczegółowy raport w terminalu:
   ```text
   [DRY-RUN] Przeniesienie: "Dziennik.gdoc" -> "04-📄-Dokumenty-Osobiste/Dziennik/Dziennik Pawla.gdoc"
   [DRY-RUN] Przemianowanie: "01👨‍👩‍👧‍👦 Rodzina" -> "01-👨‍👩‍👧‍👦-Rodzina"
   [SKIP] Ignorowanie bufora Takeout (535.8 GB) - ochrona I/O File Providera
   ```
3. **Faza 2 (Execution)**: Uruchomienie z flagą `--execute` po Twojej akceptacji raportu symulacji.

---

## Rozdział 3: Głęboka Analiza Inżynierska: Dylemat Emoji w Nazwach Folderów

Stosowanie piktogramów emoji w nazwach zasobów systemowych to zagadnienie, w którym estetyka i ergonomia wizualna zderzają się z rygorem inżynierii systemowej i automatyzacji.

```
       WIZUALNY INTERFEJS GUI                           TERMINAL / CLI / AUTOMATYZACJA
 ┌───────────────────────────────────┐               ┌───────────────────────────────────┐
 │ 01-👨‍👩‍👧‍👦-Rodzina                    │               │ $ cd 01-[???]                     │
 │ 03-🏥-Zdrowie                      │      VS       │ Unicode ZWJ: 25 bajtów UTF-8!     │
 │ • Natychmiastowe rozpoznawanie     │               │ Glitche kursora, brak na klawiaturze│
 │ • Estetyka Notion / modern app    │               │ Kłopoty w regexach i skryptach CLI│
 └───────────────────────────────────┘               └───────────────────────────────────┘
```

### 3.1. Zalety Stosowania Emoji (Ergonomia Kognitywna w GUI)
1. **Szybkość skanowania wzrokiem (Cognitive Scanning)**: Ludzki mózg przetwarza piktogramy i kolory w ułamku sekundy, znacznie szybciej niż czytanie tekstu. W aplikacjach mobilnych i widoku kafelkowym Google Drive emoji wyróżnia najważniejsze obszary.
2. **Redukcja zmęczenia decyzyjnego**: Przy 20 folderach głównych wzrok automatycznie "kotwiczy się" na piktogramie szpitala (`🏥`), pieniędzy (`💰`) czy domu (`🏠`).

---

### 3.2. Ciemna Strona Emoji: Wady Techniczne i Pułapki Inżynierskie

Mimo zalet wizualnych, stosowanie emoji niesie za sobą realne koszty techniczne:

#### 1. Koszmar Pracy w Terminalu (CLI / Shell UX)
* **Brak dedykowanego klawisza na klawiaturze**: Wpisanie nazwy folderu w terminalu wymaga wciskania skrótu `Cmd + Ctrl + Space` na macOS, wyszukiwania piktogramu w oknie dialogowym i wklejania go do polecenia.
* **Rozjeżdżanie się kursora (Terminal Glitches)**: Większość terminali (Terminal.app, iTerm2, Alacritty) ma problem z kalkulacją szerokości znaków Unicode o podwójnej szerokości (double-width glyphs). Kursor terminala często ląduje w połowie znaku, co powoduje zniekształcenia linii poleceń i błędy przy edycji komend.
* **Autouzupełnianie (Tab Completion)**: Jeśli w nazwie jest emoji zaraz po numerze, autouzupełnianie działa, ale w przypadku kolizji prefiksów edycja ścieżki w konsoli staje się uciążliwa.

#### 2. Pułapka Zero-Width Joiner (ZWJ) i Rozmiar w Bajtach
Pojedyncze emoji to często nie pojedynczy znak, lecz złożona sekwencja kodowa!
* **Drastyczny przykład: `👨‍👩‍👧‍👦` (używane w `01-👨‍👩‍👧‍👦-Rodzina`)**:
  To emoji **nie jest jednym znakiem**. Jest to sekwencja aż **7 punktów kodowych Unicode** spiętych niewidzialnymi łącznikami `U+200D` (Zero-Width Joiner):
  $$\text{Mężczyzna (U+1F468)} + \text{ZWJ} + \text{Kobieta (U+1F469)} + \text{ZWJ} + \text{Dziewczynka (U+1F467)} + \text{ZWJ} + \text{Chłopiec (U+1F466)}$$
  * **W kodowaniu UTF-8 ta pojedyncza "ikonka" zajmuje aż 25 bajtów!**
  * Wiele narzędzi CLI, starszych wersji Pythona, skryptów bashowych czy systemów plików obcina takie ciągi, traktując je jako 7 oddzielnych znaków lub rzucając błędy przepełnienia bufora.

#### 3. Problem Normalizacji Unicode na macOS (NFC vs NFD)
* macOS (systemy plików APFS i HFS+) historycznie stosuje dekompozycję znaków **NFD** (rozbija znaki na literę bazową i akcent), podczas gdy chmura Google Drive i serwery Linux stosują kanoniczną kompozycję **NFC**.
* Niektóre emoji posiadają warianty prezentacji (tzw. Variation Selectors, np. `U+FE0F` wymuszający kolorowy render vs `U+FE0E` dla czarno-białego). Niedopasowanie tych bajtów powoduje, że proste polecenie:
  ```bash
  cd 03-🏥-Zdrowie
  # Zwraca: No such file or directory (ponieważ bajty w terminalu różnią się od bajtów w systemie plików)
  ```

#### 4. Wrażliwość Narzędzi Inżynierii Danych i Skryptów
* Narzędzia takie jak Git, rclone, Docker, dbt, Apache Airflow, skrypty backupowe czy parser CSV mogą zgłaszać wyjątki `UnicodeEncodeError` lub logować nieczytelne sekwencje typu `\xf0\x9f\x91\xa8...` w środowiskach bez zainstalowanych czcionek wielokolorowych.

---

## Rozdział 4: Rozstrzygnięcie i Rekomendacja Architektoniczna

Aby pogodzić zalety czytelności w GUI z rygorem inżynierskim, poddajemy ocenie dwa spójne modele architektoniczne:

### Model A: Kompromis Hybrydowy ("Strict Root Only") – Rekomendowany dla użytkownika domowego

```
POZIOM ROOT (Katalogi Główne):   01-👨‍👩‍👧‍👦-Rodzina/      ◄── Emoji dozwolone (tylko w Root)
                                     │
POZIOM PODFOLDERÓW:                  ├── 01-Wazne-Dokumenty/  ◄── BEZWZGLĘDNY ZAKAZ EMOJI!
                                     ├── 02-Natalka/          ◄── Czysty kebab-case
                                     └── 04-Michal/           ◄── Zero problemów CLI
```

**Zasady Modelu Hybrydowego:**
1. **Emoji wyłącznie na poziomie 0 (katalog główny)**: Użycie emoji jest dozwolone **wyłącznie w 18 folderach głównych**.
2. **Neutralizacja terminalowa przez prefiks Johnny Decimal**: Ponieważ każdy folder główny zaczyna się od unikalnego numeru (`00-`, `01-`, `02-`, `03-`, `05-`, `10-`), w terminalu **nigdy nie musisz wpisywać emoji ręcznie!**  
   Wystarczy wpisać:
   ```bash
   cd 01-[Naciśnij Tab]  ──►  automatycznie rozwinie do: cd 01-👨‍👩‍👧‍👦-Rodzina/
   ```
3. **Bezwzględny zakaz emoji w podfolderach**: Wszystkie podfoldery (poziomy 2, 3, 4...) mają nazwy czysto tekstowe w formacie kebab-case (np. `01-Wazne-Dokumenty`, `AI-Exports`, `Toyota-Corolla`).
4. **Eliminacja sekwencji ZWJ**: Zastąpienie wieloznakowego `👨‍👩‍👧‍👦` (25 bajtów) prostym, jednoelementowym znakiem `👪` (U+1F46A, 4 bajty) lub `👥`.

---

### Model B: Czysty Inżynierski ("Pure UNIX / Clean Kebab") – Rekomendowany dla programisty/architekta

Jeśli często operujesz na Dysku Google z poziomu skryptów, terminala, repozytoriów kodu lub automatyzacji cron:

```
📁 Mój-Dysk/
├── 00-inbox/
├── 00-poufne-dokumenty/
├── 01-rodzina/
├── 02-edukacja-dzieci/
├── 03-zdrowie/
├── 04-dokumenty-osobiste/
├── 05-finanse/
├── 07-praca-i-projekty/
├── 10-mieszkanie-i-nieruchomosci/
├── 11-lewickie/
├── 12-pojazdy/
├── 20-wiedza-i-rozwoj/
├── 21-audio-i-multimedia/
├── 22-sport-i-aktywnosc/
├── 23-gry-i-hobby/
├── 24-podroze-i-wyjazdy/
├── 80-aplikacje-i-synchronizacja/
├── 90-archiwum/
├── 95-takeout/
└── 99-do-usuniecia/
```

**Zalety Modelu B:**
* **100% odporność na błędy kodowania**: Żadne narzędzie programistyczne, skrypt czy parser nigdy nie napotka problemu z interpretacją ścieżki.
* **Błyskawiczne pisanie w terminalu**: Nawet bez klawisza Tab wpisujesz ścieżki jednym ciągiem bez przełączania tablic znaków.
* **Profesjonalny minimalizm**: Styl stosowany w repozytoriach Git, chmurach AWS/GCP S3/GCS oraz architekturze enterprise data lakes.

---

## Rozdział 5: Podsumowanie Decyzyjne

| Aspekt | Model A (Hybrydowy: Emoji w Root) | Model B (Czysty: Zero Emoji) |
| :--- | :--- | :--- |
| **Ergonomia w aplikacji mobilnej i www** | ⭐⭐⭐⭐⭐ Wybitna (ikony ułatwiają nawigację) | ⭐⭐⭐ Dobra (czytelna numeracja) |
| **Praca w terminalu (macOS / zsh)** | ⭐⭐⭐⭐ Bardzo dobra (dzięki prefiksom numerycznym i Tab) | ⭐⭐⭐⭐⭐ Perfekcyjna (czysty tekst ASCII) |
| **Bezpieczeństwo skryptów i automatyzacji** | ⭐⭐⭐⭐ Wysokie (pod warunkiem unikania ZWJ) | ⭐⭐⭐⭐⭐ Absolutne (zero ryzyka kodowania) |
| **Rekomendacja końcowa** | **Wybierz Model A**, jeśli z dysku korzysta rodzina na telefonach i zależy Ci na estetyce GUI. | **Wybierz Model B**, jeśli gDrive traktujesz głównie jako środowisko inżynierskie i developerskie. |

---

## Status Wdrożeniowy

Wszystkie ustalenia dotyczące mechaniki uprawnień, skryptowej automatyzacji oraz wariantów nazewnictwa zostały udokumentowane w niniejszym pliku. Kolejnym krokiem technicznym jest wygenerowanie i uruchomienie skryptu migracyjnego w wybranym wariancie nazewnictwa.
