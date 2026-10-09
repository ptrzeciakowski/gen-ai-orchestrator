# Architektura Docelowa, Model Zarządzania i Procesy Higieny Cyfrowej Dysku Google

**Właściciel:** Paweł Trzeciakowski (`ptrzeciakowski@gmail.com`)  
**Data opracowania:** 19 września 2026 r. (Aktualizacja: 9 października 2026 r.)  
**Kluczowa decyzja strategiczna:** Odseparowanie archiwum fotograficzno-wideo (**190.0 GB**) ze struktury roboczej Dysku Google i migracja do dedykowanego ekosystemu **Google Photos** (z uprzednim backupem offline).  
**Cel główny:** Przekształcenie Dysku Google ze składowiska wszystkiego w zorganizowane, przejrzyste repozytorium wiedzy, dokumentów i majątku (**Lean Knowledge & Asset Hub** o objętości **15–20 GB**), z realistycznymi regułami utrzymania porządku.

---

## Rozdział 1: Strategiczny Zwrot – Separacja Zdjęć (190 GB) i Zarządzanie Przestrzenią

Decyzja o odpięciu archiwum fotograficznego z Dysku Google to kluczowy krok porządkowy. Zdjęcia i klipy wideo w folderze `88📸Zdjęcia` stanowiły **71.2% całej objętości dysku** (30 958 plików w ponad 530 podkatalogach), drastycznie utrudniając nawigację, synchronizację oraz indeksowanie plików roboczych.

### 1.1. Korzyści oraz Realia Pamięci Google One

1. **Strukturalne odciążenie Dysku Google**: Wolumen plików w strukturze gDrive spada z 267 GB do ~75 GB (a po usunięciu starych obrazów dysków, zipów i duplikatów – do **15–20 GB** dokumentów).
2. **Współdzielona pula Google One (Ważna uwaga)**: Dysk Google, Google Photos oraz Gmail współdzielą tę samą przestrzeń dyskową w ramach subskrypcji Google One. Samo przeniesienie plików 1:1 z Dysku do Photos porządkuje strukturę gDrive, lecz **nie zwalnia miejsca w koncie Google One**, dopóki:
   * Nie usuniemy zbędnych duplikatów i nieudanych ujęć (~18–20 GB),
   * Nie zdecydujemy się na konwersję do trybu *Storage Saver* (Oszczędzanie miejsca) w Photos,
   * Lub nie zarchiwizujemy części surowego materiału wideo/foto na zewnętrznym nośniku (cold storage).
3. **Bufor dyskowy podczas migracji**: W trakcie importu chmurowego przez pewien czas pliki mogą współistnieć w obu usługach, co wymaga zachowania odpowiedniego zapasu wolnego miejsca w pakiecie Google One przed opróżnieniem kosza na Dysku.
4. **Natywne funkcje Google Photos**: Automatyczne rozpoznawanie twarzy domowników, geolokalizacja na mapie, wyszukiwanie semantyczne oraz wygodne albumy rodzinne bez zaśmiecania drzewa katalogów roboczych.
5. **Ulga dla synchronizacji lokalnej (Google Drive for desktop na macOS)**: Znaczące odciążenie bazy SQLite (`metadata_sqlite_db`), brak zapychania cache dyskowego (`File Provider`) i szybsze działanie Spotlighta.

### 1.2. Czteroetapowa Procedura Bezpiecznej Migracji

```
 ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
 │   FAZA 0: BACKUP     │ ──► │  FAZA 1: SANITACJA   │ ──► │   FAZA 2: TRANSFER   │ ──► │ FAZA 3: KWARANTANNA  │
 │  Eksport offline     │     │ Usunięcie duplikatów │     │ Import do Photos     │     │ 30 dni bufora        │
 │  (Takeout / Dysk zew)│     │     (~18.7 GB)       │     │ i weryfikacja EXIF   │     │ i definitywny purge  │
 └──────────────────────┘     └──────────────────────┘     └──────────────────────┘     └──────────────────────┘
```

1. **Faza 0: Obowiązkowa kopia bezpieczeństwa (Zero Data Loss)**:
   * Przed usunięciem jakichkolwiek plików z Dysku należy wykonać kopię zapasową folderu `88📸Zdjęcia`:
     * Pobranie archiwum przez **Google Takeout** (jako archiwa `.zip` / `.tgz`), LUB
     * Skopiowanie całego katalogu na zewnętrzny dysk twardy / SSD / NAS domowy.
   * Dopiero po potwierdzeniu integralności kopii offline przechodzimy do kolejnych kroków.
2. **Faza 1: Oczyszczenie przed migracją**:
   * Usunięcie zidentyfikowanych megaduplikatów:
     * `88📸Zdjęcia / 2017 (1)` (~11.2 GB)
     * `88📸Zdjęcia / 2015 (1)` (~5.9 GB)
     * `88📸Zdjęcia / 2012 / ... / Fotograf / Kopia` (~1.5 GB)
   * Zapobiega to powielaniu tych samych ujęć na osi czasu Google Photos.
3. **Faza 2: Transfer i weryfikacja metadanych**:
   * **Import chmurowy**: w [photos.google.com](https://photos.google.com) wybierz opcję *Prześlij* ➔ *Dysk Google*.
   * **Ważna uwaga o strukturze i EXIF**: Google Photos ignoruje strukturę folderów – nie utworzy automatycznie 530 albumów odpowiadających podkatalogom. Wszystkie zdjęcia trafią na główną oś czasu według daty wykonania (EXIF).
   * **Zdjęcia bez EXIF (skany, grafiki, pobrane z komunikatorów)**: Zostaną zaindeksowane pod datą wgrania. Jeśli chcesz zachować tematyczne zbiory, wgrywaj te konkretne foldery partiami i od razu twórz z nich dedykowane Albumy w Photos.
4. **Faza 3: Kwarantanna i zwolnienie przestrzeni**:
   * Po zweryfikowaniu obecności zdjęć w Photos przenieś folder `88📸Zdjęcia` do katalogu kwarantanny: `_DO_USUNIECIA/`.
   * Zachowaj pliki w kwarantannie przez **30 dni**.
   * Po 30 dniach i braku zgłoszeń o brakujących materiałach opróżnij Kosz gDrive, uwalniając strukturę roboczą dysku.

---

## Rozdział 2: Docelowa Architektura Folderów ("Lean Knowledge & Asset Hub")

Nowa architektura porządkuje przestrzeń w oparciu o zmodyfikowany system Johnny Decimal, eliminując wieloletnie nawarstwienia (m.in. dawne `25📄 Paweł - dokumenty`).

### 2.1. Zasady Konstrukcyjne:
1. **Zasada Zero-Root**: W katalogu głównym (`Mój dysk`) nie leżą żadne pliki luzem. Każdy dokument trafia do podfolderu lub do bufora `00📥 Inbox`.
2. **Spójny Wzorzec Nazewniczy**: `[XX][Emotikon] [Nazwa_Obszaru]` (np. `01👨‍👩‍👧‍👦 Rodzina`, `05💰 Finanse`).
3. **Separacja Uprawnień i Odpowiedzialności (Brak Duplikacji)**:
   * Dokumentacja medyczna znajduje się **wyłącznie** w `03🏥 Zdrowie/`.
   * Edukacja dzieci znajduje się **wyłącznie** w `02🏫 Edukacja_Dzieci/`.
   * Rachunki i paragony trafiają do `05💰 Finanse/`.
4. **Realistyczne Bezpieczeństwo i Poufność**:
   * Dysk Google **nie oferuje natywnego szyfrowania pojedynczych folderów hasłem**.
   * Folder `00🔒 Poufne_Dokumenty` zawiera wyłącznie pliki z ograniczonymi uprawnieniami udostępniania (dostęp wyłącznie właściciel).
   * **Klucze, hasła i kody 2FA**: Bezwzględny zakaz przechowywania haseł i kodów w czystym tekście na Dysku Google. Do haseł służy dedykowany menedżer (np. Bitwarden, 1Password, Apple Keychain).
   * **Wrażliwe skany tożsamości i akty notarialne**: Pliki o najwyższym stopniu poufności powinny być przed wysłaniem do chmury zaszyfrowane po stronie klienta (np. za pomocą [Cryptomator](https://cryptomator.org) lub bezpiecznego archiwum 7-Zip z AES-256).

### 2.2. Drzewo Nowej Struktury

```
📁 Mój dysk/
│
├── 00📥 Inbox/                                    # Główny bufor na nowe pliki
│   ├── AI_Exports/                                # Eksporty z Gemini / Claude / ChatGPT
│   ├── Skany_i_Mobilne/                           # Szybkie skany i dokumenty ze smartfona
│   └── Do_Przejrzenia/                            # Pobrane pliki wymagające kategoryzacji
│
├── 00🔒 Poufne_Dokumenty/                         # Dostęp: wyłącznie właściciel (szyfrowanie po stronie klienta)
│   ├── Tozsamosc/                                 # Zaszyfrowane skany dowodów, paszportów
│   └── Majatek_Akty_Notarialne/                   # Cyfrowe kopie aktów własności (master)
│
├── 01👨‍👩‍👧‍👦 Rodzina/
│   ├── 01_Wazne_Dokumenty/                        # Akty stanu cywilnego, meldunki, ZUS
│   ├── 02_Natalka/                                # Projekty, pasje, sprawy osobiste
│   ├── 03_Nadia/                                  # ZHP, konie, osiągnięcia, pamiątki
│   ├── 04_Michal/                                 # Sport, zainteresowania, pamiątki
│   └── 05_Genealogia/                             # Historia rodziny, drzewo genealogiczne
│
├── 02🏫 Edukacja_Dzieci/                          # Centralne miejsce na szkołę dzieci
│   ├── Michal/                                    # Roczniki szkolne, plany lekcji, materiały
│   └── Nadia/                                     # Roczniki szkolne, zaświadczenia, materiały
│
├── 03🏥 Zdrowie/                                  # JEDYNE repozytorium medyczne rodziny
│   ├── Pawel/                                     # Badania krwi, konsultacje, rehabilitacja
│   ├── Natka/                                     # Konsultacje, badania specjalistyczne
│   ├── Dzieci/                                    # Pediatra, stomatologia, bilanse, szczepienia
│   ├── Rodzice/                                   # Dokumentacja medyczna seniorów
│   └── Archiwum_Medyczne/                         # Zakończone, historyczne leczenie
│
├── 04📄 Dokumenty_Osobiste/                       # Rozwój osobisty i kariera Pawła
│   ├── Dziennik/                                  # Notatki osobiste i refleksje
│   ├── Kariera_i_CV/                              # Historia zatrudnienia, referencje
│   └── Certyfikaty_i_Szkolenia/                   # Uprawnienia inżynierskie, certyfikaty chmurowe
│
├── 05💰 Finanse/                                  # Finanse osobiste i domowe
│   ├── 01_Budzet_i_Analizy/                       # Zestawienia wydatków, arkusze budżetowe
│   ├── 02_Podatki_PIT/                            # Roczne deklaracje podatkowe (rocznikami)
│   ├── 03_Banki_i_Kredyty/                        # Umowy bankowe, harmonogramy spłat
│   ├── 04_Inwestycje_i_Emerytura/                 # IKE/IKZE, fundusze, plany długoterminowe
│   └── 05_Paragony_i_Gwarancje/                   # Bieżące paragony i karty gwarancyjne
│
├── 07🏢 Praca_i_Projekty/                         # Materiały merytoryczne i archiwum zawodowe
│   │                                              # (UWAGA: Zakaz przechowywania danych wrażliwych/kodu objętych NDA pracodawcy)
│   ├── 2026_Biezace/                              # Własne notatki architektoniczne, szkice koncepcyjne
│   ├── Projekty_Historyczne/                      # Archiwum dawnych wdrożeń (Allegro, Roche, itp.)
│   ├── Publikacje_i_Wystapienia/                  # Prezentacje konferencyjne, artykuły, webinary
│   └── Warsztaty_i_Materialy_Szkoleniowe/         # Własne szablony, dbt, Snowflake, Data Mesh
│
├── 10🏠 Mieszkanie_i_Nieruchomosci/               # Sprawy eksploatacyjne i majątkowe
│   ├── 01_Pod_Strzecha_7/                         # Umowy z administracją, wspólnota, bieżące opłaty
│   ├── 02_Remonty_i_Wyposazenie/                  # Projekty wnętrz, faktury za sprzęt AGD/RTV
│   ├── 03_Media_i_Energia/                        # Rozliczenia prądu, gazu, analiza zużycia
│   └── 04_Infrastruktura_Domowa_i_Siec/           # Schematy sieci, routery, konfiguracja Smart Home
│
├── 11🏡 Lewickie/                                 # Działka i dom wiejski
│   ├── Eksploatacja_i_Oplaty/                     # Rachunki bieżące, umowy z dostawcami
│   └── Geodezja_i_Dokumentacja/                   # Mapy geodezyjne, wypisy z rejestru gruntów
│
├── 12🚗 Pojazdy/                                  # Dokumentacja eksploatacji samochodów
│   ├── Toyota_Corolla/                            # Przeglądy, historia serwisowa, polisy OC/AC
│   └── Samochod_Drugi/                            # Dokumenty eksploatacyjne, ubezpieczenia
│
├── 20📚 Wiedza_i_Rozwoj/
│   ├── 01_Inzynieria_Danych_i_AI/                 # Opracowania, artykuły techniczne, notatki
│   ├── 02_Matematyka_i_Nauka/                     # Materiały dydaktyczne, opracowania
│   └── 03_Ebooki_i_Publikacje/                    # Zakupione książki, publikacje PDF
│
├── 21🎵 Audio_i_Multimedia/                       # Audiobooki, materiały dźwiękowe
├── 22🏃 Sport_i_Aktywnosc/                        # Plany treningowe, zawody biegowe, logi
├── 23🎮 Gry_i_Hobby/                              # Notatki hobbystyczne, instrukcje
├── 24🏖️ Podroze_i_Wyjazdy/                        # Rezerwacje, plany wyjazdów (rocznikami)
│
├── 80📱 Aplikacje_i_Synchronizacja/
│   ├── 80_Notability_Backup/                      # Backup notatek z iPada
│   └── 81_Obsidian_Sync/                          # Kopia repozytorium wiedzy Markdown
│
├── 90🗄️ Archiwum/                                 # Zamrożone, nieaktywne zasoby
│   ├── Archiwum_Dzialalnosci_Gospodarczej/        # Zakończona działalność (faktury, ZUS)
│   ├── Archiwum_Studiow/                          # Jedna uporządkowana kopia materiałów z uczelni
│   └── Stare_Projekty/                            # Projekty sprzed 2021 roku
│
└── _DO_USUNIECIA/                                 # Kwarantanna 30-dniowa przed skasowaniem
```

---

## Rozdział 3: Model Zarządzania Przepływem Informacji

Struktura wymaga jasnych zasad wprowadzania danych, aby nie dopuścić do ponownego zaśmiecenia.

### 3.1. Przepływ Informacji i Obsługa Pobierania

```
 ┌─────────────────────────────────────────────────────────┐
 │                   ŹRÓDŁA PLIKÓW                         │
 ├─────────────────────────────────────────────────────────┤
 │ • Pobieranie z przeglądarki Chrome na macOS             │ ──► [Lokalny folder ~/Downloads na Macu]
 │   (instalatory .dmg, pliki tymczasowe, faktury PDF)     │       │ (Pliki tymczasowe nie trafiają do chmury!)
 └─────────────────────────────────────────────────────────┘       │
                                                                   │ Tylko wyselekcjonowane pliki
                                                                   ▼
 ┌─────────────────────────────────────────────────────────┐     ┌─────────────────────────────────┐
 │ • Skany dokumentów ze smartfona                         │ ──► │           00📥 INBOX            │
 │ • Eksporty rozmów / podsumowań z AI (Gemini, Claude)    │ ──► │  (Tranzyt: max 7 dni retencji)  │
 │ • Notatki z iPada / tabletu                             │ ──► └─────────────────────────────────┘
 └─────────────────────────────────────────────────────────┘                       │
                                                                                   │ Proces kategoryzacji (SLA: raz w tygodniu)
                                                                                   ▼
                                                                 ┌─────────────────────────────────┐
                                                                 │      Właściwy Folder Docelowy   │
                                                                 │  (np. 03 Zdrowie / 05 Finanse)  │
                                                                 └─────────────────────────────────┘
```

* **Zasada separacji pobierania z sieci**: Domyślnym folderem pobierania w przeglądarce Chrome pozostaje lokalny katalog systemowy na Macu (`~/Downloads`). Nie ustawiamy pobierania bezpośrednio do zsynchronizowanego folderu Dysku Google – zapobiega to zapychaniu chmury ciężkimi instalatorami `.dmg`, plikami tymczasowymi i jednorazowymi załącznikami.
* Do folderu `00📥 Inbox` na Dysku Google trafiają wyłącznie te dokumenty, które rzeczywiście mają być przechowywane w chmurze.

### 3.2. Standard Nazewnictwa Plików (File Naming Convention)

Jednolite nazwy eliminują konieczność otwierania pliku w celu sprawdzenia jego zawartości:

| Typ Dokumentu | Wzorzec Nazewniczy | Przykład Poprawny |
| :--- | :--- | :--- |
| **Polisa / Umowa formalna** | `YYYY-MM-DD - [Podmiot] - [Przedmiot].ext` | `2026-07-24 - Warta - Polisa Toyota Corolla.pdf` |
| **Rachunek / Faktura / Koszt** | `YYYY-MM - [Wystawca] - [Tytuł] - [Kwota].ext` | `2026-08 - Plus - Abonament Lewickie - 65PLN.pdf` |
| **Dokument medyczny** | `YYYY-MM-DD - [Osoba] - [Badanie/Zabieg] - [Placowka].ext` | `2026-01-14 - Natka - TK Kolana Osiowa - Scanmed.pdf` |
| **Notatka / Opracowanie własne**| `[Temat] - [Tytul_Merytoryczny] - [Status/Wersja].ext` | `DataMesh - Koncepcja Warstwy Semantycznej - V1.gdoc` |
| **Wyjazd / Podróż** | `YYYY-MM - [Miejsce] - [Dokument].ext` | `2026-08 - Tatry - Rezerwacja Schronisko.pdf` |

---

## Rozdział 4: Procesy Utrzymania Higieny Cyfrowej (Rytuały & SLA)

Porządek utrzymywany jest dzięki prostym, krótkim nawykom operacyjnym:

```
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│     DAILY TOUCHPOINT    │ ──► │      WEEKLY REVIEW      │ ──► │      MONTHLY AUDIT      │ ──► │   QUARTERLY ARCHIVAL    │
│        (1 minuta)       │     │       (10 minut)        │     │       (15 minut)        │     │       (20 minut)        │
│    "Zero-Root Rule"     │     │  "Inbox to Zero (SLA)"  │     │ "Purge & Permissions"   │     │  "Zamknięcie okresu"    │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

### 4.1. Rytuał Codzienny: "Zero-Root Rule" (Czas: 1 minuta)
* **Zasada**: Katalog główny (`Mój dysk`) musi pozostać pusty (poza oficjalnymi folderami głównymi).
* **Działanie**: Jeżeli w trakcie pracy jakikolwiek plik został utworzony w katalogu głównym, przesuń go do `00📥 Inbox` lub właściwego podfolderu.

### 4.2. Rytuał Cotygodniowy: "Weekly Inbox Review" (Czas: 10 minut – np. piątek po południu)
1. Przejrzyj zawartość `00📥 Inbox`:
   * **Pliki z AI / Robocze**: Wartościowe materiały przenieś do odpowiednich katalogów tematycznych po nadaniu standardowej nazwy; zbędne szkice wyrzuć do Kosza.
   * **Skany i dokumenty mobilne**: Rozdziel do `03 Zdrowie`, `05 Finanse` lub `10 Mieszkanie`.
2. **Cel**: Opróżnienie bufora `00📥 Inbox` do zera na koniec tygodnia.

### 4.3. Rytuał Miesięczny: "Purge & Permissions Audit" (Czas: 15 minut – początek miesiąca)
1. **Opróżnienie Kwarantanny**: Wejdź do `_DO_USUNIECIA/`. Jeśli pliki spędziły tam **30 dni** i nie były potrzebne, usuń je do Kosza i opróżnij Kosz.
2. **Weryfikacja Uprawnień**: Sprawdź folder `00🔒 Poufne_Dokumenty` – upewnij się, że nie został przypadkowo udostępniony osobom trzecim.
3. **Przegląd plików zewnętrznych**: Przejrzyj sekcję *Udostępnione dla mnie* i usuń skróty do materiałów, które przestały być aktualne.

### 4.4. Rytuał Kwartalny / Sezonowy: "Archiwizacja Cykliczna" (Czas: 20 minut)
1. **Szkoła**: Po zakończeniu semestru przenieś archiwalne sprawdziany i materiały do podfolderów rocznikowych.
2. **Podatki**: Po zamknięciu rocznego PIT przenieś dokumentację danego roku do podfolderu zamkniętego w `05 Finanse / 02_Podatki_PIT`.
3. **Materiały projektowe**: Zakończone projekty i koncepcje przenieś do `Projekty_Historyczne`.

---

## Rozdział 5: Automatyzacja i Konfiguracja Narzędzi

### 5.1. Bezpieczny Strażnik Katalogu Głównego (Google Apps Script)

Skrypt uruchamiany raz na dobę w Google Apps Script, przenoszący zagubione pliki z katalogu głównego do `00📥 Inbox` z bezpieczną obsługą błędów:

```javascript
/**
 * Auto-Triage Katalogu Głównego Google Drive
 * Wyzwalacz: Time-driven (np. raz na dobę o 23:00)
 */
function triageRootFiles() {
  const root = DriveApp.getRootFolder();
  const files = root.getFiles();
  
  // Bezpieczne pobranie folderu Inbox
  const inboxFolders = DriveApp.getFoldersByName("00📥 Inbox");
  if (!inboxFolders.hasNext()) {
    Logger.log("Błąd: Nie znaleziono folderu '00📥 Inbox'. Skrypt przerwany.");
    return;
  }
  const inbox = inboxFolders.next();
  
  // Pobranie lub utworzenie podfolderów docelowych
  const aiFolder = getOrCreateSubfolder(inbox, "AI_Exports");
  const mediaFolder = getOrCreateSubfolder(inbox, "Skany_i_Mobilne");
  const fallbackFolder = getOrCreateSubfolder(inbox, "Do_Przejrzenia");

  const aiKeywords = [
    "czy możesz", "wygeneruj", "podsumuj", "analiza_", "prompt", "gemini", "claude"
  ];
  
  const mobilePhotoRegex = /^(img_|pxl_|dsc_|photo_|\d{8}_\d{6})/i;

  while (files.hasNext()) {
    const file = files.next();
    const name = file.getName();
    const lowerName = name.toLowerCase();

    // 1. Zrzuty zdjęć i skanów mobilnych w katalogu głównym
    if (mobilePhotoRegex.test(lowerName)) {
      file.moveTo(mediaFolder);
      Logger.log("Przeniesiono plik mobilny: " + name);
      continue;
    }

    // 2. Eksporty czatów AI i nienazwane dokumenty robocze
    const isAiExport = aiKeywords.some(keyword => lowerName.startsWith(keyword));
    const isUntitled = lowerName.includes("bez tytułu") || lowerName.includes("untitled");
    
    if (isAiExport || isUntitled) {
      file.moveTo(aiFolder);
      Logger.log("Przeniesiono eksport AI / dokument roboczy: " + name);
      continue;
    }

    // 3. Pozostałe pliki porzucone luzem w Root
    file.moveTo(fallbackFolder);
    Logger.log("Przeniesiono do ogólnego bufora: " + name);
  }
}

function getOrCreateSubfolder(parentFolder, name) {
  const subfolders = parentFolder.getFoldersByName(name);
  if (subfolders.hasNext()) {
    return subfolders.next();
  }
  return parentFolder.createFolder(name);
}
```

### 5.2. Konfiguracja Notability na iPadzie

* **Format kopii zapasowej**:
  * Format `.pdf` zapewnia uniwersalny podgląd na każdym urządzeniu i indeksowanie tekstu przez Google Drive.
  * **Ważna uwaga**: Eksport do PDF uniemożliwia późniejszą edycję odręcznych notatek wektorowych w Notability. Jeśli zależy Ci na zachowaniu pełnej edytowalności notatek, pozostaw natywny format kopii w chmurze iCloud, a do Google Drive przesyłaj wyłącznie wyeksportowane materiały finalne (jako PDF) do folderu `80_Notability_Backup`.

---

## Rozdział 6: Prawidłowe Operatory Wyszukiwania w Google Drive

Wyszukiwarka Google Drive wykorzystuje dedykowane parametry zapytań. Poniższa tabela zawiera zweryfikowane, działające formuły:

| Cel wyszukiwania | Sprawdzona formuła wyszukiwania |
| :--- | :--- |
| **Pliki leżące bezpośrednio w katalogu głównym** | `'root' in parents and trashed = false` *(wyszukiwarka zaawansowana)* |
| **Pliki modyfikowane w ostatnim okresie** | `after:2026-09-01` lub `before:2026-01-01` |
| **Poufne skany tożsamości (audyt bezpieczeństwa)** | `type:pdf ("dowód" or "paszport" or "pesel")` |
| **Dokumenty robocze i artefakty AI** | `title:("bez tytułu" or "untitled" or "wygeneruj")` |
| **Pliki udostępnione mi przez innych** | `-owner:me` |
| **Pliki udostępnione przeze mnie innym osobom** | `owner:me to:*` |
| **Duże pliki do selekcji i zwolnienia miejsca** | `size:>100M` |

---

## Podsumowanie Wdrożeniowe

Zastosowanie powyższych zasad przynosi wymierne rezultaty:
1. **Bezpieczeństwo danych**: Kopia zapasowa offline wykonana przed usunięciem zdjęć z Dysku całkowicie eliminuje ryzyko przypadkowej utraty pamiątek rodzinnych.
2. **Klarowność struktury**: Brak duplikacji obszarów tematycznych (medycyna, edukacja i majątek mają dokładnie jedno, jednoznaczne miejsce).
3. **Świadome zarządzanie pamięcią**: Rozróżnienie między strukturą folderów gDrive a współdzieloną pulą miejsca Google One pozwala uniknąć zaskoczenia stanem konta.
4. **Niski narzut czasowy**: 1 minuta dziennie na czysty katalog główny oraz 10 minut w piątek na opróżnienie bufora `00📥 Inbox` gwarantują stabilny porządek bez konieczności przeprowadzania wielkich, męczących audytów w przyszłości.
