# Architektura Docelowa, Model Zarządzania i Procesy Higieny Cyfrowej Dysku Google

> **Uwaga (2026-10-21):** konwencja nazw folderów zmieniona na `NN <emoji> Nazwa Ze Spacjami` z polskimi znakami i jednym emoji — zob. [design.md](../design.md) §3. Opis „bezspacyjnych” nazw poniżej jest historyczny.

**Właściciel:** Paweł Trzeciakowski (`ptrzeciakowski@gmail.com`)  
**Data opracowania:** 19 września 2026 r. (Aktualizacja: 11 października 2026 r.)  
**Kluczowa decyzja strategiczna:** Odseparowanie archiwum fotograficzno-wideo ze struktury roboczej Dysku Google i migracja do ekosystemu **Google Photos** (**zrealizowane** – folder `88📸Zdjęcia` został usunięty). Nowe wyzwanie operacyjne: bezpieczna obsługa nowo powstałego archiwum **Takeout (~536 GB)** w chmurze i jego transfer do cold storage offline.  
**Cel główny:** Przekształcenie Dysku Google ze składowiska wszystkiego w zorganizowane, przejrzyste repozytorium wiedzy, dokumentów i majątku (**Lean Knowledge & Asset Hub** o docelowej objętości **15–20 GB** dokumentów roboczych), z rygorystycznymi, bezspacyjnymi regułami nazewnictwa.

---

## Rozdział 1: Separacja Zdjęć (Zrealizowana) i Nowe Wyzwanie: Katalog Takeout (~536 GB)

Kluczowy krok porządkowy w postaci odpięcia archiwum fotograficznego z Dysku Google został pomyślnie wykonany. Folder `88📸Zdjęcia` (który stanowił pierwotnie **71.2% całej objętości dysku**, licząc 30 958 plików) został usunięty ze struktury roboczej Dysku Google.

Jednocześnie, w wyniku procedury tworzenia kopii zapasowej przed usunięciem danych (eksport przez usługę **Google Takeout** z opcją zapisu na Dysku), w katalogu głównym pojawił się folder `Takeout` zawierający **535.8 GB** spakowanych archiwów `.zip` (wolumeny po ~10–50 GB, w tym `archive_browser.html` dla Zdjęć Google).

### 1.1. Realia Pamięci Google One i Problem Podwójnego Obciążenia

1. **Strukturalne odciążenie vs przestrzeń w chmurze**: Usunięcie zdjęć odciążyło drzewo folderów, ale obecność katalogu `Takeout` na Dysku Google oznacza, że archiwa te zajmują gigantyczną przestrzeń dyskową (~536 GB).
2. **Współdzielona pula Google One**: Dysk Google, Google Photos oraz Gmail współdzielą tę samą przestrzeń dyskową w ramach subskrypcji Google One. Posiadanie zdjęć w Google Photos ORAZ ich wielogigabajtowego archiwum ZIP w folderze `Takeout` na Dysku oznacza **podwójne zajęcie limitu konta**.
3. **Problem z aplikacją Google Drive for desktop (macOS)**: Próba synchronizacji lub indeksowania przez mechanizm File Provider tak wielkich paczek ZIP (pliki po 50 GB) generuje błędy systemowe (np. `Stale NFS file handle`) oraz zapycha lokalną przestrzeń podręczną dysku Maca.
4. **Cel operacyjny**: Katalog `Takeout` nie może pozostać na stałe w chmurze. Stanowi on jedynie tymczasowy bufor tranzytowy, który musi zostać zrzucony na nośnik fizyczny offline, a następnie skasowany z Dysku Google.

### 1.2. Procedura Obsługi i Rozliczenia Archiwum Takeout (Zero Data Loss)

```
 ┌──────────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────────┐     ┌──────────────────────────┐
 │ KROK 1: STANDARYZACJA    │ ──► │ KROK 2: TRANSFER OFFLINE │ ──► │ KROK 3: WERYFIKACJA SUM  │ ──► │ KROK 4: DEFINITYWNY PURGE│
 │ Włączenie do struktury:  │     │ Pobranie archiwów ZIP    │     │ Sprawdzenie spójności    │     │ Trwałe usunięcie z gDrive│
 │ 95-💽-Takeout/           │     │ na dysk zew. SSD/HDD/NAS │     │ (archive_browser.html)   │     │ i odzyskanie 536 GB G-One│
 └──────────────────────────┘     └──────────────────────────┘     └──────────────────────────┘     └──────────────────────────┘
```

1. **Krok 1: Włączenie do struktury (`95-💽-Takeout/`)**:
   * Zmiana nazwy niesformatowanego folderu `Takeout` na ustandaryzowaną nazwę `95-💽-Takeout/` w celu zachowania ładu Johnny Decimal w fazie przejściowej.
2. **Krok 2: Pobranie archiwów na nośnik zewnętrzny (Cold Storage)**:
   * Pobranie wszystkich partii plików `takeout-*.zip` bezpośrednio przez interfejs webowy Google Drive (lub dedykowany transfer rclone/skrypt) na zewnętrzny dysk SSD/HDD lub domowy NAS.
   * Dzięki temu archiwum rodzinne jest w 100% bezpieczne w formule offline (zgodnie z zasadą 3-2-1 backupu).
3. **Krok 3: Weryfikacja spójności i integralności**:
   * Weryfikacja obecności pliku `archive_browser.html` oraz testowe rozpakowanie losowych paczek z mediami na dysku zewnętrznym w celu potwierdzenia poprawności archiwum.
4. **Krok 4: Definitywny purge i uwolnienie przestrzeni**:
   * Trwałe usunięcie folderu `95-💽-Takeout/` z Dysku Google i natychmiastowe opróżnienie Kosza.
   * Operacja ta natychmiast uwalnia **535.8 GB** w subskrypcji Google One i doprowadza Dysk Google do docelowego pułapu **Lean Hub (15–20 GB)**.

---

## Rozdział 2: Docelowa Architektura Folderów ("Lean Knowledge & Asset Hub")

Nowa architektura porządkuje przestrzeń w oparciu o zmodyfikowany system Johnny Decimal, eliminując wieloletnie nawarstwienia (m.in. dawne `25📄 Paweł - dokumenty`).

### 2.1. Zasady Konstrukcyjne:
1. **Zasada Zero-Root**: W katalogu głównym (`Mój dysk`) nie leżą żadne pliki luzem. Każdy dokument trafia do podfolderu lub do bufora `00-📥-Inbox/`.
2. **Spójny Wzorzec Nazewniczy**: `[XX]-[Emotikon]-[Nazwa-Obszaru]` (np. `01-👨‍👩‍👧‍👦-Rodzina`, `05-💰-Finanse`).
   * **Całkowity brak spacji**: W nazwach katalogów nie stosujemy odstępów – wszystkie człony oddzielane są łącznikiem `-`.
   * **Emoji traktowane jak wyrazy**: Emotikony stanowią samodzielne wyrazy w nazwie i są oddzielane łącznikami `-` z obu stron (np. `00-📥-Inbox`, `03-🏥-Zdrowie`, `95-💽-Takeout`).
   * **Łącznik `-` zamiast podkreślnika `_`**: Wszystkie człony wielowyrazowe i podkatalogi łączymy wyłącznie łącznikiem `-` (kebab-case, np. `Poufne-Dokumenty`, `AI-Exports`, `01-Wazne-Dokumenty`).
3. **Separacja Uprawnień i Odpowiedzialności (Brak Duplikacji)**:
   * Dokumentacja medyczna znajduje się **wyłącznie** w `03-🏥-Zdrowie/`.
   * Edukacja dzieci znajduje się **wyłącznie** w `02-🏫-Edukacja-Dzieci/`.
   * Rachunki i paragony trafiają do `05-💰-Finanse/`.
   * Archiwum Takeout znajduje się **wyłącznie** w buforze `95-💽-Takeout/` (do czasu pobrania offline).
4. **Realistyczne Bezpieczeństwo i Poufność**:
   * Dysk Google **nie oferuje natywnego szyfrowania pojedynczych folderów hasłem**.
   * Folder `00-🔒-Poufne-Dokumenty` zawiera wyłącznie pliki z ograniczonymi uprawnieniami udostępniania (dostęp wyłącznie właściciel).
   * **Klucze, hasła i kody 2FA**: Bezwzględny zakaz przechowywania haseł i kodów w czystym tekście na Dysku Google (eliminacja dawnego `91🔑Hasła`). Do haseł służy dedykowany menedżer (np. Bitwarden, 1Password, Apple Keychain).
   * **Wrażliwe skany tożsamości i akty notarialne**: Pliki o najwyższym stopniu poufności (np. zidentyfikowane w root `Dowód osobisty - Paweł Trzeciakowski.pdf`, `Dowód osobisty - mama.pdf`) powinny być przed wysłaniem do chmury zaszyfrowane po stronie klienta (np. za pomocą [Cryptomator](https://cryptomator.org) lub bezpiecznego archiwum 7-Zip z AES-256).

### 2.2. Drzewo Nowej Struktury

```
📁 Mój-Dysk/
│
├── 00-📥-Inbox/                                    # Główny bufor na nowe pliki (retencja max 7 dni)
│   ├── AI-Exports/                                # Eksporty z Gemini / Claude / ChatGPT
│   ├── Skany-i-Mobilne/                           # Szybkie skany i dokumenty ze smartfona (np. IMG_*)
│   └── Do-Przejrzenia/                            # Pobrane pliki wymagające kategoryzacji
│
├── 00-🔒-Poufne-Dokumenty/                         # Dostęp: wyłącznie właściciel (szyfrowanie po stronie klienta)
│   ├── Tozsamosc/                                 # Zaszyfrowane skany dowodów, paszportów
│   └── Majatek-Akty-Notarialne/                   # Cyfrowe kopie aktów własności (master)
│
├── 01-👨‍👩‍👧‍👦-Rodzina/
│   ├── 01-Wazne-Dokumenty/                        # Akty stanu cywilnego, meldunki, ZUS
│   ├── 02-Natalka/                                # Projekty, pasje, sprawy osobiste
│   ├── 03-Nadia/                                  # ZHP, konie, osiągnięcia, pamiątki
│   ├── 04-Michal/                                 # Sport, zainteresowania, pamiątki
│   └── 05-Genealogia/                             # Historia rodziny, drzewo genealogiczne
│
├── 02-🏫-Edukacja-Dzieci/                          # Centralne miejsce na szkołę dzieci
│   ├── Michal/                                    # Roczniki szkolne, plany lekcji, materiały
│   └── Nadia/                                     # Roczniki szkolne, zaświadczenia, materiały
│
├── 03-🏥-Zdrowie/                                  # JEDYNE repozytorium medyczne rodziny
│   ├── Pawel/                                     # Badania krwi, konsultacje, rehabilitacja
│   ├── Natka/                                     # Konsultacje, badania specjalistyczne
│   ├── Dzieci/                                    # Pediatra, stomatologia, bilanse, szczepienia
│   ├── Rodzice/                                   # Dokumentacja medyczna seniorów
│   └── Archiwum-Medyczne/                         # Zakończone, historyczne leczenie
│
├── 04-📄-Dokumenty-Osobiste/                       # Rozwój osobisty i kariera Pawła
│   ├── Dziennik/                                  # Notatki osobiste i refleksje (np. Dziennik.gdoc)
│   ├── Kariera-i-CV/                              # Historia zatrudnienia, referencje
│   └── Certyfikaty-i-Szkolenia/                   # Uprawnienia inżynierskie, certyfikaty chmurowe
│
├── 05-💰-Finanse/                                  # Finanse osobiste i domowe
│   ├── 01-Budzet-i-Analizy/                       # Zestawienia wydatków, arkusze budżetowe (np. home_budget_*.csv)
│   ├── 02-Podatki-PIT/                            # Roczne deklaracje podatkowe (rocznikami)
│   ├── 03-Banki-i-Kredyty/                        # Umowy bankowe, harmonogramy spłat
│   ├── 04-Inwestycje-i-Emerytura/                 # IKE/IKZE, fundusze, plany długoterminowe
│   └── 05-Paragony-i-Gwarancje/                   # Bieżące paragony i karty gwarancyjne
│
├── 07-🏢-Praca-i-Projekty/                         # Materiały merytoryczne i archiwum zawodowe
│   │                                              # (UWAGA: Zakaz przechowywania danych wrażliwych/kodu objętych NDA pracodawcy)
│   ├── 2026-Biezace/                              # Własne notatki architektoniczne, szkice koncepcyjne (Snowflake, Data Mesh)
│   ├── Projekty-Historyczne/                      # Archiwum dawnych wdrożeń (Allegro, Roche, itp.)
│   ├── Publikacje-i-Wystapienia/                  # Prezentacje konferencyjne, artykuły, LinkedIn posts
│   └── Warsztaty-i-Materialy-Szkoleniowe/         # Własne szablony, dbt, Snowflake, Data Mesh
│
├── 10-🏠-Mieszkanie-i-Nieruchomosci/               # Sprawy eksploatacyjne i majątkowe
│   ├── 01-Pod-Strzecha-7/                         # Umowy z administracją, wspólnota, bieżące opłaty
│   ├── 02-Remonty-i-Wyposazenie/                  # Projekty wnętrz, faktury za sprzęt AGD/RTV
│   ├── 03-Media-i-Energia/                        # Rozliczenia prądu, gazu, analiza zużycia fotowoltaiki
│   └── 04-Infrastruktura-Domowa-i-Siec/           # Schematy sieci, routery, konfiguracja Smart Home
│
├── 11-🏡-Lewickie/                                 # Działka i dom wiejski
│   ├── Eksploatacja-i-Oplaty/                     # Rachunki bieżące, umowy z dostawcami
│   └── Geodezja-i-Dokumentacja/                   # Mapy geodezyjne, wypisy z rejestru gruntów
│
├── 12-🚗-Pojazdy/                                  # Dokumentacja eksploatacji samochodów
│   ├── Toyota-Corolla/                            # Przeglądy, historia serwisowa, polisy OC/AC
│   └── Samochod-Drugi/                            # Dokumenty eksploatacyjne drugiego auta (np. Golf)
│
├── 20-📚-Wiedza-i-Rozwoj/
│   ├── 01-Inzynieria-Danych-i-AI/                 # Opracowania, artykuły techniczne, notatki
│   ├── 02-Matematyka-i-Nauka/                     # Materiały dydaktyczne (np. Analiza Matematyczna WEiTI)
│   └── 03-Ebooki-i-Publikacje/                    # Zakupione książki, publikacje PDF
│
├── 21-🎵-Audio-i-Multimedia/                       # Audiobooki, materiały dźwiękowe (dawne 92🎵 Muzyka)
├── 22-🏃-Sport-i-Aktywnosc/                        # Plany treningowe, zawody biegowe, logi (dawne 85🏃 Bieganie)
├── 23-🎮-Gry-i-Hobby/                              # Notatki hobbystyczne, instrukcje
├── 24-🏖️-Podroze-i-Wyjazdy/                        # Rezerwacje, plany wyjazdów (rocznikami, Tatry itp.)
│
├── 80-📱-Aplikacje-i-Synchronizacja/
│   ├── 80-Notability-Backup/                      # Backup notatek z iPada
│   └── 81-Obsidian-Sync/                          # Kopia repozytorium wiedzy Markdown
│
├── 90-🗄️-Archiwum/                                 # Zamrożone, nieaktywne zasoby
│   ├── Archiwum-Dzialalnosci-Gospodarczej/        # Zakończona działalność (faktury, ZUS)
│   ├── Archiwum-Studiow/                          # Jedna uporządkowana kopia materiałów z uczelni
│   └── Stare-Projekty/                            # Projekty sprzed 2021 roku
│
├── 95-💽-Takeout/                                  # TYMCZASOWY bufor archiwów Google Takeout (~536 GB)
│   │                                              # (Zadanie: pobrać na dysk zewnętrzny SSD/HDD i usunąć z gDrive!)
│   ├── takeout-20261010T210123Z-*.zip             # Paczki eksportu Google Photos / konta
│   └── takeout-20261011T044419Z-*.zip             # Kolejne wolumeny archiwum (części 1-3)
│
└── 99-🗑️-Do-Usuniecia/                             # Kwarantanna 30-dniowa przed definitywnym skasowaniem
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
 │ • Skany dokumentów ze smartfona                         │ ──► │          00-📥-INBOX            │
 │ • Eksporty rozmów / podsumowań z AI (Gemini, Claude)    │ ──► │  (Tranzyt: max 7 dni retencji)  │
 │ • Notatki z iPada / tabletu                             │ ──► └─────────────────────────────────┘
 └─────────────────────────────────────────────────────────┘                       │
                                                                                   │ Proces kategoryzacji (SLA: raz w tygodniu)
                                                                                   ▼
                                                                 ┌─────────────────────────────────┐
                                                                 │      Właściwy Folder Docelowy   │
                                                                 │(np. 03-🏥-Zdrowie / 05-💰-Finanse)│
                                                                 └─────────────────────────────────┘
```

* **Zasada separacji pobierania z sieci**: Domyślnym folderem pobierania w przeglądarce Chrome pozostaje lokalny katalog systemowy na Macu (`~/Downloads`). Nie ustawiamy pobierania bezpośrednio do zsynchronizowanego folderu Dysku Google – zapobiega to zapychaniu chmury ciężkimi instalatorami `.dmg`, plikami tymczasowymi i jednorazowymi załącznikami.
* Do folderu `00-📥-Inbox/` na Dysku Google trafiają wyłącznie te dokumenty, które rzeczywiście mają być przechowywane w chmurze.

### 3.2. Standard Nazewnictwa Plików (File Naming Convention)

Jednolite nazwy eliminują konieczność otwierania pliku w celu sprawdzenia jego zawartości:

| Typ Dokumentu | Wzorzec Nazewniczy | Przykład Poprawny |
| :--- | :--- | :--- |
| **Polisa / Umowa formalna** | `YYYY-MM-DD - [Podmiot] - [Przedmiot].ext` | `2026-07-24 - Warta - Polisa Toyota Corolla.pdf` |
| **Rachunek / Faktura / Koszt** | `YYYY-MM - [Wystawca] - [Tytuł] - [Kwota].ext` | `2026-08 - Plus - Abonament Lewickie - 65PLN.pdf` |
| **Dokument medyczny** | `YYYY-MM-DD - [Osoba] - [Badanie/Zabieg] - [Placowka].ext` | `2026-01-14 - Natka - TK Kolana Osiowa - Scanmed.pdf` |
| **Notatka / Opracowanie własne**| `[Temat] - [Tytul-Merytoryczny] - [Status/Wersja].ext` | `DataMesh - Koncepcja Warstwy Semantycznej - V1.gdoc` |
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
* **Działanie**: Jeżeli w trakcie pracy jakikolwiek plik został utworzony w katalogu głównym, przesuń go do `00-📥-Inbox/` lub właściwego podfolderu.

### 4.2. Rytuał Cotygodniowy: "Weekly Inbox Review" (Czas: 10 minut – np. piątek po południu)
1. Przejrzyj zawartość `00-📥-Inbox/`:
   * **Pliki z AI / Robocze**: Wartościowe materiały przenieś do odpowiednich katalogów tematycznych po nadaniu standardowej nazwy; zbędne szkice wyrzuć do Kosza.
   * **Skany i dokumenty mobilne**: Rozdziel do `03-🏥-Zdrowie/`, `05-💰-Finanse/` lub `10-🏠-Mieszkanie-i-Nieruchomosci/`.
2. **Cel**: Opróżnienie bufora `00-📥-Inbox/` do zera na koniec tygodnia.

### 4.3. Rytuał Miesięczny: "Purge & Permissions Audit" (Czas: 15 minut – początek miesiąca)
1. **Opróżnienie Kwarantanny**: Wejdź do `99-🗑️-Do-Usuniecia/`. Jeśli pliki spędziły tam **30 dni** i nie były potrzebne, usuń je do Kosza i opróżnij Kosz.
2. **Weryfikacja Uprawnień**: Sprawdź folder `00-🔒-Poufne-Dokumenty` – upewnij się, że nie został przypadkowo udostępniony osobom trzecim.
3. **Nadzór nad Buforem Archiwów (`95-💽-Takeout/`)**: Sprawdź, czy archiwum Takeout (~536 GB) zostało w całości pobrane na dysk zewnętrzny SSD/HDD lub domowy NAS. Po potwierdzeniu kopii offline usuń folder z Dysku Google i opróżnij Kosz, uwalniając ponad 530 GB w Google One.
4. **Przegląd plików zewnętrznych**: Przejrzyj sekcję *Udostępnione dla mnie* i usuń skróty do materiałów, które przestały być aktualne.

### 4.4. Rytuał Kwartalny / Sezonowy: "Archiwizacja Cykliczna" (Czas: 20 minut)
1. **Szkoła**: Po zakończeniu semestru przenieś archiwalne sprawdziany i materiały do podfolderów rocznikowych w `02-🏫-Edukacja-Dzieci/`.
2. **Podatki**: Po zamknięciu rocznego PIT przenieś dokumentację danego roku do podfolderu zamkniętego w `05-💰-Finanse / 02-Podatki-PIT/`.
3. **Materiały projektowe**: Zakończone projekty i koncepcje przenieś do `Projekty-Historyczne/`.

---

## Rozdział 5: Automatyzacja i Konfiguracja Narzędzi

### 5.1. Bezpieczny Strażnik Katalogu Głównego (Google Apps Script)

Skrypt uruchamiany raz na dobę w Google Apps Script, przenoszący zagubione pliki z katalogu głównego do `00-📥-Inbox/` z bezpieczną obsługą błędów:

```javascript
/**
 * Auto-Triage Katalogu Głównego Google Drive
 * Wyzwalacz: Time-driven (np. raz na dobę o 23:00)
 */
function triageRootFiles() {
  const root = DriveApp.getRootFolder();
  const files = root.getFiles();
  
  // Bezpieczne pobranie folderu Inbox
  const inboxFolders = DriveApp.getFoldersByName("00-📥-Inbox");
  if (!inboxFolders.hasNext()) {
    Logger.log("Błąd: Nie znaleziono folderu '00-📥-Inbox'. Skrypt przerwany.");
    return;
  }
  const inbox = inboxFolders.next();
  
  // Pobranie lub utworzenie podfolderów docelowych (kebab-case bez spacji)
  const aiFolder = getOrCreateSubfolder(inbox, "AI-Exports");
  const mediaFolder = getOrCreateSubfolder(inbox, "Skany-i-Mobilne");
  const fallbackFolder = getOrCreateSubfolder(inbox, "Do-Przejrzenia");

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
  * **Ważna uwaga**: Eksport do PDF uniemożliwia późniejszą edycję odręcznych notatek wektorowych w Notability. Jeśli zależy Ci na zachowaniu pełnej edytowalności notatek, pozostaw natywny format kopii w chmurze iCloud, a do Google Drive przesyłaj wyłącznie wyeksportowane materiały finalne (jako PDF) do folderu `80-Notability-Backup`.

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
1. **Bezpieczeństwo danych i separacja multimediów**: Archiwum fotograficzne zostało z powodzeniem odseparowane ze struktury roboczej do Google Photos. Bufor `95-💽-Takeout/` zabezpiecza pełną kopię offline i po pobraniu na fizyczny nośnik (cold storage) zostanie usunięty z chmury.
2. **Spójny bezspacyjny wzorzec nazewnictwa**: Format `[XX]-[Emotikon]-[Nazwa]` (z łącznikiem `-` zamiast spacji i podkreślników oraz traktowaniem emoji jako wyrazów) zapewnia pełną kompatybilność ze skryptami, systemem plików macOS/POSIX i narzędziami synchronizacji.
3. **Klarowność struktury**: Brak duplikacji obszarów tematycznych (medycyna, edukacja i majątek mają dokładnie jedno, jednoznaczne miejsce).
4. **Świadome zarządzanie pamięcią**: Usunięcie z chmury paczek Takeout natychmiast uwalnia >530 GB w puli Google One, sprowadzając Dysk do docelowego pułapu 15–20 GB czystych dokumentów roboczych.
5. **Niski narzut czasowy**: 1 minuta dziennie na czysty katalog główny oraz 10 minut w piątek na opróżnienie bufora `00-📥-Inbox/` gwarantują stabilny porządek bez konieczności przeprowadzania wielkich, męczących audytów w przyszłości.
