# Architektura Docelowa, Model Zarządzania i Procesy Higieny Cyfrowej Dysku Google

**Właściciel:** Paweł Trzeciakowski (`ptrzeciakowski@gmail.com`)  
**Data opracowania:** 19 września 2026 r.  
**Kluczowa decyzja strategiczna:** Przeniesienie całego archiwum fotograficzno-wideo (**190.0 GB**) z Dysku Google do **Google Photos**.  
**Cel główny:** Przekształcenie Dysku Google z przeciążonego, 267-gigabajtowego „magazynu wszystkiego” w sterylny, zwinny system zarządzania wiedzą, projektami i majątkiem (**Lean Knowledge & Asset Hub** o wadze poniżej **15–20 GB**), z automatyczną ochroną przed nawrotem chaosu.

---

## Rozdział 1: Strategiczny Zwrot – Migracja Zdjęć do Google Photos (190 GB)

Decyzja o odpięciu archiwum fotograficznego z Dysku Google to najważniejszy krok optymalizacyjny całego audytu. Zdjęcia i klipy wideo w folderze `88📸Zdjęcia` stanowiły **71.2% całej objętości dysku** (30 958 plików) i generowały ponad 530 podkatalogów, drastycznie utrudniając nawigację i wyszukiwanie dokumentów.

### 1.1. Korzyści z separacji
1. **Redukcja objętości dysku o ponad 70%**: Wolumen Dysku Google spada z 267 GB do ~75 GB (a po usunięciu duplikatów i starych backupów – do zaledwie **15–20 GB**).
2. **Natywne funkcje Google Photos**: Automatyczne rozpoznawanie twarzy domowników (Nadia, Michał, Natalka, Paweł), geolokalizacja na mapie, zaawansowane wyszukiwanie semantyczne (np. *"Narty Livigno 2024"*, *"tenis Michała"*), automatyczne albumy i udostępnianie rodzinne bez zaśmiecania struktury folderów.
3. **Zmniejszenie narzutu na klienta lokalnego (DriveFS / File Provider na macOS)**: Znaczące odciążenie bazy SQLite (`metadata_sqlite_db`), szybsze indeksowanie Spotlight i eliminacja błędów synchronizacji.

### 1.2. Trzyetapowa Procedura Migracji do Google Photos

```
 ┌─────────────────────────┐       ┌─────────────────────────┐       ┌─────────────────────────┐
 │   FAZA 1: SANITACJA     │  ──►  │    FAZA 2: TRANSFER     │  ──►  │   FAZA 3: PURGE Z DYSKU │
 │ Eliminacja megaduplikatów│       │ Import do Google Photos │       │ Kwarantanna i zwolnienie│
 │  (odrzucenie ~18.7 GB)  │       │ (Web Import / Uploader) │       │   miejsca na gDrive     │
 └─────────────────────────┘       └─────────────────────────┘       └─────────────────────────┘
```

1. **Krok 1: Oczyszczenie przed migracją (Zero Garbage to Photos)**:
   * **Bezwzględny zakaz wgrywania wykrytych megaduplikatów**:
     * `88📸Zdjęcia / 2017 (1)` (11.21 GB) – usunąć.
     * `88📸Zdjęcia / 2015 (1)` (5.94 GB) – usunąć.
     * `88📸Zdjęcia / 2012 / ... / Fotograf / Kopia` (1.54 GB) – usunąć.
   * Eliminacja ta zapobiega zaśmieceniu osi czasu w Google Photos tysiącami powielonych kadrów.
2. **Krok 2: Wykonanie migracji**:
   * **Metoda A (Natywny import chmurowy – rekomendowana, bez zużycia transferu domowego)**:
     1. Otwórz [photos.google.com](https://photos.google.com).
     2. Kliknij **Prześlij (Upload)** ➔ **Dysk Google (Google Drive)**.
     3. Zaznacz foldery rocznikowe z `88📸Zdjęcia` (od 2005 do 2026).
     4. Google przetworzy pliki po stronie serwerów (bez pobierania na Twój komputer).
   * **Metoda B (Dla zachowania oryginalnych metadanych EXIF i albumów)**: Użycie aplikacji komputerowej Google Drive z włączoną opcją synchronizacji wskazanego folderu do Google Photos.
3. **Krok 3: Weryfikacja i likwidacja folderu na Dysku**:
   * Po zweryfikowaniu obecności zdjęć w bibliotece Google Photos:
   * Przenieś folder `88📸Zdjęcia` do `_DO_USUNIECIA /` na 14 dni.
   * Opróżnij Kosz Google Drive – uwolnienie **190 GB przestrzeni**.

---

## Rozdział 2: Docelowa Architektura Folderów ("Lean Knowledge & Asset Hub")

Po wyłączeniu zdjęć i wchłonięciu przestarzałego megafolderu `25📄 Paweł - dokumenty`, nowa struktura staje się przejrzysta, kompaktowa i ściśle dopasowana do Twojego sposobu myślenia.

### 2.1. Złote Zasady Architektury:
1. **Zasada Zero-Root**: W katalogu głównym (`Mój dysk`) znajduje się **dokładnie 0 plików luzem**. Każdy plik musi mieć swoje miejsce w podfolderze.
2. **System Bloków Dekadowych Johnny Decimal**: Główne obszary życia pogrupowane są w dziesiątki.
3. **Spójny Wzorzec Nazewniczy**: `[XX][Emotikon] [Nazwa_Obszaru]` – zawsze spacja po emotikonie, brak kropek, jednolite kodowanie.
4. **Izolacja Aplikacji w Bloku 80+**: Notability, wtyczki Chrome czy Gemini Gems nie mają prawa tworzyć folderów na pierwszym poziomie obok Rodziny i Pracy.

### 2.2. Pełne Drzewo Nowej Struktury

```
📁 Mój dysk/
│
├── 00_SYSTEM/
│   ├── 00📥 Inbox/                                # Jedyny oficjalny punkt zrzutu
│   │   ├── 🤖_AI_Exports/                         # Eksporty z Gemini / ChatGPT
│   │   ├── 🌐_Chrome_Downloads/                   # Pliki pobierane z sieci
│   │   ├── 📱_Notability_Staging/                 # Notatki z iPada do sklasyfikowania
│   │   └── 📥_Zrzuty_i_Skaner/                    # Szybkie skany i zdjęcia ze smartfona
│   └── 00🔒 Zaszyfrowany_Sejf/                    # Dostęp wyłącznie dla Pawła
│       ├── Tozsamosc_i_RODO/                      # Dowody osobiste, paszporty, akty urodzenia
│       ├── Hasla_i_Klucze/                        # Eksporty haseł, kody zapasowe 2FA
│       └── Akty_Wlasnosci_Notarialne/             # Akty notarialne zakupu nieruchomości
│
├── 01-09 OSOBISTE & RODZINA/
│   ├── 01👨‍👩‍👧‍👦 Rodzina/
│   │   ├── 00_Wazne_Dokumenty_Rodzinne/           # ZUS, meldunki, sprawy urzędowe
│   │   ├── 01_Natalka/                            # Dokumentacja medyczna, pasje
│   │   ├── 02_Nadia/                              # Konie, ZHP, historia rozwoju, wzrost
│   │   ├── 03_Michal/                             # Tenis, I Komunia, pokój
│   │   ├── 04_Kuba/                               # Materiały dydaktyczne, matematyka
│   │   └── 10_Drzewo_Genealogiczne/               # Genealogia rodziny
│   ├── 02🏫 Edukacja_Dzieci/
│   │   ├── Michal/                                # Roczniki szkolne (Klasa 2a -> 5d)
│   │   └── Nadia/                                 # Roczniki szkolne (Klasa 1c -> 7c)
│   ├── 03🏥 Zdrowie/                              # Wyłącznie dokumentacja medyczna
│   │   ├── Pawel/                                 # Kolano, fizjoterapia, badania krwi
│   │   ├── Natka/                                 # Konsultacje Kraków, tomografia
│   │   ├── Dzieci/                                # Pediatra, stomatolog, szczepienia
│   │   ├── Rodzice/                               # Dokumentacja zdrowotna rodziców
│   │   └── Archiwum_Medyczne/                     # Zakończone terapie
│   ├── 04📄 Dokumenty_Osobiste/                   # Osobista przestrzeń Pawła
│   │   ├── Dziennik/                              # Dziennik osobisty (plik Dziennik.gdoc)
│   │   ├── Kariera_i_CV/                          # Historia CV, referencje, dyplomy
│   │   └── Certyfikaty_i_Uprawnienia/             # AWS, certyfikacje inżynierskie
│   ├── 05💰 Finanse/
│   │   ├── 01_Budzet_i_Wydatki/                   # Pliki analizy budżetu (CSV, gsheet)
│   │   ├── 02_Podatki/                            # PITy roczne (2022-2025), rozliczenia
│   │   ├── 03_Banki_i_Kredyty/                    # mBank, PKO BP, spłaty hipoteczne
│   │   └── 04_Inwestycje_i_Emerytura/             # IKE/IKZE, plany emerytalne
│   └── 07🏢 Praca/
│       ├── 2026_HSBC/                             # Bieżące projekty architektoniczne
│       ├── 2025_Allegro/                          # Wdrożenie Data Mesh
│       ├── 2018_Roche/                            # Projekty DWH / AWS
│       ├── Publikacje_i_Wystapienia/              # Snowflake Summit, posty LinkedIn, webinary
│       └── Szkolenia_i_Warsztaty/                 # dbt Bootcamp, prezentacje techniczne
│
├── 10-19 MAJĄTEK & INFRASTRUKTURA DOMOWA/
│   ├── 10🏠 Mieszkanie/                           # Dawne 06 + 16 (scalenie!)
│   │   ├── 01_Pod_Strzecha_7/                     # Zakup, umowy, wspólnota
│   │   ├── 02_Remonty_i_Wyposazenie/              # 2017 Remont, 2026 pokój Michała
│   │   ├── 03_Energia_i_Fotowoltaika/             # Analizy zużycia, stacja ładowania
│   │   └── 04_Siec_Domowa_i_SmartHome/            # Routery, adresacja, okablowanie
│   ├── 11🏡 Lewickie/                             # Działka i dom wiejski
│   │   ├── Eksploatacja_i_Rachunki/               # Koszty bieżące, Plus abonament
│   │   └── Geodezja_i_Podzial/                    # Mapy, podział działki, księgi
│   └── 12🚗 Samochod/                             # Dawne 09 + polisy z 10
│       ├── Toyota_Corolla/                        # Serwis, przeglądy, polisa OC/AC
│       └── VW_Golf/                               # Dokumenty, naprawy, ubezpieczenie
│
├── 20-29 WIEDZA, PASJE & ROZWÓJ/
│   ├── 20📚 Nauka_i_Wiedza/
│   │   ├── 01_Matematyka_PW_WEiTI/                # Wchłonięty folder Analiza Matematyczna
│   │   ├── 02_Inzynieria_Danych/                  # Materiały Snowflake, dbt, SQL, Python
│   │   └── 03_Ebooki_i_Ksiazki/                   # Literatura faktu, podręczniki PDF
│   ├── 21🎵 Audio_i_Muzyka/                       # E-bookpoint, audiobooki dorosłych
│   ├── 22🏃 Sport_i_Bieganie/                     # Dawne 85 (plany, maratony, wyniki)
│   ├── 23🎮 Gry_i_Rozrywka/                       # Dawne 93 (Heroes III, VCMI, Minecraft)
│   └── 24🏖️ Podroze_i_Wycieczki/                  # Dawne 08 (wg lat: 2022, 2023, 2024, 2026 Tatry)
│
├── 80-89 APLIKACJE & INTEGRACJE/
│   ├── 80📱 Notability_Backup/                    # Wyłącznie wektorowy PDF z OCR
│   ├── 81📝 Obsidian_Vault/                       # Zsynchronizowany vault markdown
│   └── 82🤖 Gemini_Gems/                          # Boty systemowe (Tauron, Nauczyciel Matmy)
│
└── 90-99 SYSTEM, KONTROLA & ARCHIWUM/
    ├── 95💽 Kopie_Zapasowe/                       # Tylko bieżące, kompaktowe kopie
    ├── 98🧾 Paragony/                             # Mobilny strumień paragonów OCR
    ├── 99🗄️ Archiwum/                             # Historyczne, zamrożone projekty
    │   ├── Archiwum_Firm_i_Dzialalnosci/          # 2020 Działalność Gospodarcza
    │   ├── Archiwum_Studiow/                      # Jedna kopia studia.zip (zamiast trzech!)
    │   └── Archiwum_Historyczne_Pawel_2021/       # Przesortowane resztki z folderu 25
    └── _DO_USUNIECIA/                             # Kwarantanna 30-dniowa (ukryty / techniczny)
```

---

## Rozdział 3: Model Zarządzania Dyskiem (Operating Model & Workflows)

Aby nowa struktura nie uległa ponownej degradacji, definiujemy formalny model przepływu informacji bazujący na metodologiach GTD (Getting Things Done) i PARA.

### 3.1. Zasada "One-Way Inflow" (Jedna Brama Wjazdowa)

Wszystkie nowe, nieskategoryzowane pliki trafiają **wyłącznie** do `00_SYSTEM / 00📥 Inbox`:

```
                ┌────────────────────────────────────────────────────────┐
                │                  ŹRÓDŁA ZASILANIA                      │
                ├────────────────────────────────────────────────────────┤
                │ • Eksport z czatu Gemini / ChatGPT                     │
                │ • Pobieranie z Chrome na macOS                         │
                │ • Zrzut skanu dowodu / faktury z telefonu              │
                │ • Nowy szkic z Notability na iPadzie                   │
                └────────────────────────────────────────────────────────┘
                                             │
                                             ▼
                                ┌─────────────────────────┐
                                │      00📥 INBOX         │
                                │ (Strefa Tranzytowa SLA) │
                                └─────────────────────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
            [Wartość trwała > 7 dni]                     [Śmieć / Ephemera AI]
                       │                                           │
                       ▼                                           ▼
             Właściwy podfolder                             Kosz / Kwarantanna
           (np. 07 Praca / 10 Dom)                           _DO_USUNIECIA/
```

### 3.2. Standard Nazewnictwa Plików (File Naming Convention)
Koniec z nazwami będącymi promptami (`Czy możesz...`) lub losowymi hashami (`0d5a2m...`). Wprowadzamy rygorystyczny format:

| Typ Dokumentu | Wzorzec Nazewniczy | Przykład Poprawny |
| :--- | :--- | :--- |
| **Dokument urzędowy / polisa** | `YYYY-MM-DD - [Podmiot] - [Przedmiot].ext` | `2026-07-24 - Warta - Polisa Toyota Corolla.pdf` |
| **Rachunek / Faktura / Koszt** | `YYYY-MM - [Wystawca] - [Za co] - [Kwota].ext` | `2026-08 - Plus - Abonament Lewickie - 65PLN.pdf` |
| **Dokument medyczny** | `YYYY-MM-DD - [Osoba] - [Typ badania] - [Lekarz/Placówka].ext` | `2026-01-14 - Natka - TK Kolana Osiowa - dr Felus.pdf` |
| **Projekt zawodowy / Artykuł**| `[Kontekst] - [Tytuł merytoryczny] - [Wersja/Status].ext` | `Snowflake - Architektura Warstwy Semantycznej - Final.gdoc` |
| **Wyjazd / Podróż** | `YYYY-MM - [Kraj/Miejsce] - [Opis dokumentu].ext` | `2026-08 - Tatry - Plan Wycieczki V2.gdoc` |

---

## Rozdział 4: Procesy Utrzymania Higieny Cyfrowej (Rytuały & SLA)

Porządek nie jest stanem statycznym – jest procesem. Aby utrzymać sterylność dysku przy minimalnym nakładzie czasu, wdrażamy 4 cykliczne rytuały:

```
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│     DAILY TOUCHPOINT    │ ──► │      WEEKLY REVIEW      │ ──► │     MONTHLY AUDIT       │
│        (1 minuta)       │     │       (10 minut)        │     │       (15 minut)        │
│    "Zero-Root Rule"     │     │  "Inbox to Zero (SLA)"  │     │ "Purge & Permissions"   │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

### 4.1. Rytuał Codzienny: "Zero-Root Rule" (Czas: 1 minuta)
* **Zasada**: Nigdy nie kończ dnia z plikiem leżącym bezpośrednio w `Mój dysk`.
* **Działanie**: Jeśli podczas pracy wygenerowałeś cokolwiek w Root – przeciągnij to jednym ruchem do `00📥 Inbox`. Root musi być zawsze czysty.

### 4.2. Rytuał Cotygodniowy: "Weekly Inbox Zero" (Czas: 10 minut – np. piątek 16:30)
1. **Otwórz `00📥 Inbox`**:
   * **Podfolder `🤖_AI_Exports`**:
     * Jeśli treść była potrzebna jednorazowo ➔ `KOSZ`.
     * Jeśli ma stać się dokumentem ➔ zmień nazwę według standardu i przenieś do folderu docelowego (`07 Praca`, `10 Mieszkanie`).
   * **Podfolder `📥_Zrzuty_i_Skaner`**:
     * Rozrzucenie faktur do `05 Finanse`, paragonów do `98 Paragony`, skanów medycznych do `03 Zdrowie`.
   * **Podfolder `📱_Notability_Staging`**:
     * Usunięcie brudnopisów, przeniesienie wartościowych wykładów/notatek do właściwych gałęzi.
2. **Kryterium sukcesu**: Folder `00📥 Inbox` ma w piątek po południu 0 plików.

### 4.3. Rytuał Miesięczny: "Purge & Permissions Check" (Czas: 15 minut – 1. dzień miesiąca)
1. **Opróżnienie Kwarantanny**: Wejdź do `_DO_USUNIECIA /`. Jeżeli w plikach przeniesionych miesiąc wcześniej nikt nie grzebał – zaznacz wszystko i wyślij do Kosza.
2. **Audyt Uprawnień RODO**:
   * Upewnij się, że do folderu `00🔒 Zaszyfrowany_Sejf` dostęp masz wyłącznie Ty.
   * Sprawdź filtr `sharedwithme` w wyszukiwarce dysku – jeśli pojawiły się nowe cudze zasoby, utwórz skrót lub usuń je z widoku.
3. **Detekcja duplikatów**: Szybki rzut oka na obecność plików z sufiksami ` (1)` w folderach roboczych.

### 4.4. Rytuał Kwartalny / Sezonowy: "Vaulting & Cold Archival" (Czas: 30 minut)
1. **Zamknięcie okresu**: Po zakończeniu semestru szkolnego dzieci przenieś materiały z bieżących klas do podfolderu rocznika.
2. **Podatki**: Po złożeniu deklaracji PIT za dany rok przenieś całą teczkę do `05 Finanse / 02_Podatki / YYYY` i oznacz jako statyczną.
3. **Projekty IT**: Zakończone wdrożenia przenieś do archiwum danego pracodawcy (np. `07 Praca / 2025_Allegro / _Archiwum_Projektu`).

---

## Rozdział 5: Automatyzacja Ekosystemu (Skrypty i Konfiguracja Narzędzi)

Czystość systemu powinna być wspierana technologicznie, a nie tylko siłą woli.

### 5.1. Automatyczny Strażnik Roota (Google Apps Script)
Poniższy skrypt, uruchamiany bezpłatnie w tle Twojego konta Google raz na dobę (lub co godzinę), automatycznie wykrywa pliki-prompty z Gemini oraz porzucone zrzuty foto w katalogu głównym i przenosi je do właściwych podfolderów Inboxa:

```javascript
/**
 * Auto-Cleaner Katalogu Głównego Google Drive dla Pawła
 * Wyzwalacz: Time-driven (np. codziennie o 23:00)
 */
function cleanRootDirectory() {
  const root = DriveApp.getRootFolder();
  const files = root.getFiles();
  
  // Pobranie folderów docelowych w 00_SYSTEM / 00📥 Inbox
  const inboxFolder = DriveApp.getFoldersByName("00📥 Inbox").next();
  const aiFolder = inboxFolder.getFoldersByName("🤖_AI_Exports").next();
  const mediaFolder = inboxFolder.getFoldersByName("📥_Zrzuty_i_Skaner").next();
  
  const aiKeywords = ["czy możesz", "serio?", "super,", "dobrze,", "jeszcze raz", "wygeneruj mi", "zrób z tego"];
  
  while (files.hasNext()) {
    const file = files.next();
    const name = file.getName().toLowerCase();
    const mime = file.getMimeType();
    
    // 1. Wykrywanie artefaktów AI (prompt exports)
    const isAiPrompt = aiKeywords.some(keyword => name.startsWith(keyword));
    if (isAiPrompt) {
      file.moveTo(aiFolder);
      Logger.log(`Przeniesiono artefakt AI do Inbox: ${file.getName()}`);
      continue;
    }
    
    // 2. Wykrywanie surowych zrzutów zdjęć z iPhone'a w Root
    if (name.startsWith("img_23") && (name.endsWith(".jpeg") || name.endsWith(".jpg"))) {
      file.moveTo(mediaFolder);
      Logger.log(`Przeniesiono zdjęcie z Root do Inbox: ${file.getName()}`);
      continue;
    }
    
    // 3. Puste/szczątkowe dokumenty bez tytułu
    if (name.startsWith("dokument bez tytułu") || name.startsWith("arkusz kalkulacyjny bez tytułu")) {
      file.moveTo(aiFolder);
      Logger.log(`Przeniesiono dokument bez tytułu do Inbox: ${file.getName()}`);
      continue;
    }
  }
}
```

### 5.2. Konfiguracja Notability na iPadzie
1. Otwórz **Ustawienia Notability** ➔ **Kopia zapasowa (Auto-Backup)**.
2. Zmień format z `Notability (.note)` na **`PDF`** (z włączonym przeszukiwaniem OCR).
3. Przestań generować podwójne pliki `.note` i `.pdf` dla każdej notatki – PDF jest uniwersalny, indeksowalny przez Spotlight i gDrive, oraz waży 3x mniej.
4. Ustaw ścieżkę docelową kopii na: `80-89 APLIKACJE & INTEGRACJE / 80📱 Notability_Backup`.

### 5.3. Konfiguracja Przeglądarki Chrome
1. W ustawieniach wtyczki Google Drive / rozszerzeń zapisu zmień domyślną lokalizację pobierania z `Root` na `00_SYSTEM / 00📥 Inbox / 🌐_Chrome_Downloads`.
2. Zlikwiduj zdublowany folder `Zapisane z Chrome (1)` po weryfikacji jego zawartości.

---

## Rozdział 6: Formuły i Filtry Wyszukiwania w Codziennej Pracy

Zamiast przeklikiwać się przez dziesiątki podfolderów na telefonie czy komputerze, korzystaj z precyzyjnych operatorów wyszukiwania Google Drive:

| Cel wyszukiwania | Dokładna formuła wyszukiwania w Google Drive |
| :--- | :--- |
| **Wszystkie pliki w Root (kontrola czystości)** | `'root' in parents and trashed = false` |
| **Pliki otwierane w tym tygodniu (HOT)** | `viewed:today` lub `viewed:7d` |
| **Poufne skany tożsamości (audyt RODO)** | `type:pdf ("dowód" or "paszport" or "pesel")` |
| **Śmieci AI do usunięcia** | `title:("czy możesz" or "wygeneruj" or "bez tytułu")` |
| **Cudze pliki współdzielone na dysku** | `to:me -owner:me` |
| **Wielkie zamrożone pliki (>100 MB, starsze niż 2 lata)**| `size:>100M before:2024-01-01` |

---

## Podsumowanie i Gotowość do Wdrożenia

Dzięki połączeniu:
1. **Odciążenia dysku ze zdjęć (190 GB przeniesione do Google Photos)**,
2. **Eliminacji udowodnionych duplikatów i starych backupów (ponad 80 GB)**,
3. **Sterylnej architektury z buforem `00📥 Inbox` i Cyfrowym Sejfem**,
4. **10-minutowego cotygodniowego rytuału Inbox Zero**,

Twój Dysk Google stanie się wzorowym, nowoczesnym środowiskiem pracy, w którym odnalezienie dowolnego dokumentu zajmuje maksymalnie 5 sekund, a ryzyko wycieku danych wrażliwych zostaje całkowicie zredukowane do zera.
