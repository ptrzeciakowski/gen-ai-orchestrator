# Mapa Migracji Katalogów i Plików do Nowej Struktury ("Lean Knowledge & Asset Hub")

**Identyfikator dokumentu:** `07-mapa`  
**Właściciel:** Paweł Trzeciakowski (`ptrzeciakowski@gmail.com`)  
**Data opracowania:** 11 października 2026 r.  
**Stan wyjściowy Dysku Google:**
* **Folderów głównych w `Mój dysk`**: 28
* **Plików leżących luzem w katalogu głównym (Root drift)**: 52 pliki
* **Status zdjęć**: Odseparowane ze struktury roboczej do ekosystemu Google Photos (dawny folder `88📸Zdjęcia` usunięty)
* **Katalog Takeout**: Obecny w katalogu głównym (535.8 GB w spakowanych archiwach `.zip`)
* **Standard docelowy**: Bezspacyjny Johnny Decimal (`[XX]-[Emotikon]-[Nazwa-Obszaru]`, kebab-case, emoji jako wyrazy, `-` zamiast spacji i podkreślników `_`).

---

## Rozdział 1: Zbiorcza Matryca Migracji Folderów Głównych (28 Folderów w Root)

Poniższa tabela stanowi jednoznaczną mapę relokacji każdego z 28 folderów znajdujących się obecnie w katalogu głównym Dysku Google.

| Lp. | Istniejący Folder (Źródło) | Elementy / Rozmiar | Docelowa Lokalizacja (Cel) | Typ Działania | Szczegółowe Wytyczne i Reguły Przejścia |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 1 | `01👨‍👩‍👧‍👦 Rodzina` | 7 podf., 6 plików / 5.5 GB | `01-👨‍👩‍👧‍👦-Rodzina/` | **Rename & Standardize** | Przemianowanie folderu głównego na `01-👨‍👩‍👧‍👦-Rodzina/`. Standaryzacja podfolderów na kebab-case (`01-Wazne-Dokumenty`, `02-Natalka`, `03-Nadia`, `04-Michal`, `05-Genealogia`). Scalenie podfolderu `05 Kuba` do archiwum rodziny. |
| 2 | `02🏫Szkoła` | 2 podf., 2 pliki / 300.3 MB | `02-🏫-Edukacja-Dzieci/` | **Rename & Standardize** | Zmiana nazwy na `02-🏫-Edukacja-Dzieci/`. Podfoldery `Michał/` i `Nadia/` otrzymują nazwy bez polskich znaków w ścieżkach: `Michal/` oraz `Nadia/`. |
| 3 | `03🏥Zdrowie` | 8 podf., 1 plik / 562.2 MB | `03-🏥-Zdrowie/` | **Rename & Standardize** | Zmiana nazwy na `03-🏥-Zdrowie/`. Standaryzacja podfolderów: `Pawel/`, `Natka/`, `Dzieci/` (scalenie Michała i Nadii), `Rodzice/` (przeniesienie podfolderu `Mama/`), `Archiwum-Medyczne/` (przeniesienie `_Archiwum/`, `2024 - LuxMed w Roche/`, `Terapia M./`). |
| 4 | `05💰Finanse` | 5 podf., 3 pliki / 212.1 MB | `05-💰-Finanse/` | **Rename & Consolidate** | Zmiana nazwy na `05-💰-Finanse/`. Reorganizacja podfolderów do schematu: `01-Budzet-i-Analizy/`, `02-Podatki-PIT/`, `03-Banki-i-Kredyty/`, `04-Inwestycje-i-Emerytura/`, `05-Paragony-i-Gwarancje/` (tutaj trafia zawartość `98🧾Paragony`). |
| 5 | `06🏠Mieszkanie` | 5 podf., 1 plik / 791.8 MB | `10-🏠-Mieszkanie-i-Nieruchomosci/` | **Merge & Reorganize** | Zmiana numeru i nazwy na `10-🏠-Mieszkanie-i-Nieruchomosci/`. `05. Pod Strzechą 7/` ➔ `01-Pod-Strzecha-7/`. `10. Sieć/` ➔ `04-Infrastruktura-Domowa-i-Siec/`. `90. Kupno mieszkania/` oraz `00. Archiwum/` trafiają do podfolderu umów lub archiwum mieszkaniowego. |
| 6 | `07🏢Praca` | 7 podf., 13 plików / 185.2 MB | `07-🏢-Praca-i-Projekty/` | **Rename & Reorganize** | Zmiana nazwy na `07-🏢-Praca-i-Projekty/`. Bieżące sprawy trafiają do `2026-Biezace/`. Dawne firmy (`2015/`, `2018 - Roche/`, `2025 - Allegro/`) do `Projekty-Historyczne/`. Świadectwa pracy do `04-📄-Dokumenty-Osobiste/Kariera-i-CV/`. |
| 7 | `08🏖️Wakacje` | 6 podf. / 43.7 MB | `24-🏖️-Podroze-i-Wyjazdy/` | **Merge & Renumber** | Przeniesienie i zmiana nazwy na `24-🏖️-Podroze-i-Wyjazdy/`. Zachowanie podziału rocznikowego (`2022/`, `2023/`, `2024/`, `2025/`, `2026/`, `2027-Narty/`). |
| 8 | `09🚗Samochód` | 2 podf., 1 plik / 349.1 MB | `12-🚗-Pojazdy/` | **Merge & Renumber** | Zmiana nazwy i numeru na `12-🚗-Pojazdy/`. Podfolder `2023 - Toyota Corolla/` ➔ `Toyota-Corolla/`. Pliki drugiego auta (z folderu ubezpieczeń) ➔ `Samochod-Drugi/`. |
| 9 | `10 ☂️ Ubezpieczenie` | 5 podf. / 18.3 MB | *Rozproszenie tematyczne* | **Split & Eliminate** | Likwidacja folderu parasolowego. Polisa Toyoty ➔ `12-🚗-Pojazdy/Toyota-Corolla/`. Polisa VW Golf ➔ `12-🚗-Pojazdy/Samochod-Drugi/`. Polisa mieszkania ➔ `10-🏠-Mieszkanie-i-Nieruchomosci/01-Pod-Strzecha-7/`. NNW dzieci ➔ `01-👨‍👩‍👧‍👦-Rodzina/01-Wazne-Dokumenty/`. Wyjazd Słowacja ➔ `24-🏖️-Podroze-i-Wyjazdy/2025/`. |
| 10 | `11. Obsydian` | 0 elementów / 0 B | `80-📱-Aplikacje-i-Synchronizacja/81-Obsidian-Sync/` | **Relocate** | Pusty folder przenieść do `80-📱-Aplikacje-i-Synchronizacja/81-Obsidian-Sync/` jako repozytorium synchronizacji notatek Markdown. |
| 11 | `15🏡Lewickie` | 4 podf., 8 plików / 600.8 MB | `11-🏡-Lewickie/` | **Rename & Standardize** | Zmiana nazwy na `11-🏡-Lewickie/`. Podfolder `00. Eksploatacja domu.../` oraz rachunki Plus ➔ `Eksploatacja-i-Oplaty/`. `01. Podział działki.../` ➔ `Geodezja-i-Dokumentacja/`. |
| 12 | `16🏡Pokój` | 1 podf., 1 plik / 26.2 MB | `10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia/` | **Merge & Eliminate** | Podfolder `Energia Elektryczna/` oraz pliki analizy prądu scalić z `10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia/`. Usunąć pusty folder `16🏡Pokój`. |
| 13 | `20📚 ebooks + audobooks` | 2 podf., 7 plików / 1.2 GB | `20-📚-Wiedza-i-Rozwoj/03-Ebooki-i-Publikacje/` | **Merge & Renumber** | Ebooki przenieść do `20-📚-Wiedza-i-Rozwoj/03-Ebooki-i-Publikacje/`. Podfolder `03. Math/` przenieść do `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/`. Audiobooki przenieść do `21-🎵-Audio-i-Multimedia/`. |
| 14 | `25📄 Paweł - dokumenty` | 13 podf., 8 plików / 8.2 GB | *Dekompozycja modułowa* | **Decompose & Eliminate** | Całkowity demontaż dawnego "worka na wszystko". Szczegółowa dekompozycja 13 podfolderów w Rozdziale 2.1. Likwidacja folderu głównego `25`. |
| 15 | `85🏃 Bieganie` | 6 podf., 6 plików / 21.0 MB | `22-🏃-Sport-i-Aktywnosc/` | **Rename & Renumber** | Zmiana nazwy i numeru na `22-🏃-Sport-i-Aktywnosc/`. Zachowanie podziału rocznikowego (`2018/`–`2025/`). |
| 16 | `91🔑Hasła` | 0 podf., 5 plików / 84.6 KB | `99-🗑️-Do-Usuniecia/` *(po migracji)* | **Migrate & Purge** | Kategoryczny zakaz trzymania haseł w czystym tekście na gDrive! Hasła przepisać do menedżera haseł (Bitwarden / Apple Keychain), a pliki z folderu przenieść do `99-🗑️-Do-Usuniecia/`. |
| 17 | `92🎵 Muzyka` | 3 podf., 1 plik / 1.1 GB | `21-🎵-Audio-i-Multimedia/` | **Rename & Renumber** | Folder zawiera audiobooki i słuchowiska dla dzieci (Astrid Lindgren, Narnia). Zmiana numeru i nazwy na `21-🎵-Audio-i-Multimedia/`. |
| 18 | `93🎮Gry` | 2 podf., 1 plik / 66.9 MB | `23-🎮-Gry-i-Hobby/` | **Rename & Renumber** | Zmiana nazwy na `23-🎮-Gry-i-Hobby/`. Podfoldery `Minecraft/` i `VCMI HoMM 3/` zachowane jako hobby/gry. |
| 19 | `94🧑‍💻Oprogramowanie` | 2 podf. / 653.0 MB | `90-🗄️-Archiwum/Stare-Projekty/` | **Archive / Cold Storage** | Przestarzałe instalatory (Unreal Commander, Virtual Pool 3 z 2021 r.). Przenieść do archiwum lub zrzucić na dysk offline i usunąć. |
| 20 | `95💽Kopia zapasowa` | 18 podf., 2 pliki / 50.8 GB | `90-🗄️-Archiwum/` *(lub Cold Storage)* | **Archive Offline & Purge** | Zawiera archaiczne backupy telefonów i routerów (2013–2020: Galaxy S3/S4/S7, HTC, Xiaomi). Pliki te nie są potrzebne w chmurze – zgrać na domowy dysk twardy/NAS i usunąć z gDrive, uwalniając ~51 GB. |
| 21 | `96🗄️Archiwum` | 4 podf., 17 plików / 330.4 MB | `90-🗄️-Archiwum/` | **Rename & Standardize** | Przemianowanie na `90-🗄️-Archiwum/`. `2020 Działalność Gospodarcza/` ➔ `Archiwum-Dzialalnosci-Gospodarczej/`. `89 Sterta/` do kwarantanny lub posegregowania. |
| 22 | `98🧾Paragony` | 0 podf., 54 pliki / 31.5 MB | `05-💰-Finanse/05-Paragony-i-Gwarancje/` | **Merge & Eliminate** | Wszystkie 54 pliki paragonów przenieść bezpośrednio do `05-💰-Finanse/05-Paragony-i-Gwarancje/`. Folder `98🧾Paragony` usunąć. |
| 23 | `Analiza_Matematyczna_WEiTI` | 0 podf., 2 pliki / 215.2 KB | `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/` | **Merge & Eliminate** | Przenieść pliki podręcznika do `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/`. Usunąć folder z katalogu głównego. |
| 24 | `Gemini Gems` | 0 podf., 2 pliki / 1.4 KB | `00-📥-Inbox/AI-Exports/` | **Merge & Eliminate** | Przenieść definicje promptów/Gems do `00-📥-Inbox/AI-Exports/`. Usunąć folder z katalogu głównego. |
| 25 | `Notability` | 10 podf., 3 pliki / 421.9 MB | `80-📱-Aplikacje-i-Synchronizacja/80-Notability-Backup/` | **Relocate & Rename** | Cały folder przenieść do `80-📱-Aplikacje-i-Synchronizacja/80-Notability-Backup/` jako backup notatek wektorowych/PDF z iPada. |
| 26 | `Takeout` | 1 podf., 16 plików / **535.8 GB** | `95-💽-Takeout/` ➔ **Offline Purge** | **Transit & Cold Purge** | Przemianować tymczasowo na `95-💽-Takeout/`. Pobrać paczki `.zip` na dysk zewnętrzny SSD/HDD, zweryfikować sumy i trwale skasować z gDrive, uwalniając 536 GB w Google One. |
| 27 | `Zapisane z Chrome` | 0 podf., 9 plików / 74.6 MB | `99-🗑️-Do-Usuniecia/` | **Triage & Quarantine** | Przypadkowe zrzuty stron WWW z przeglądarki. Po weryfikacji przenieść do kwarantanny i usunąć po 30 dniach. |
| 28 | `Zapisane z Chrome (1)` | 0 podf., 15 plików / 10.7 MB | `99-🗑️-Do-Usuniecia/` | **Triage & Quarantine** | Duplikat folderu zapisu stron Chrome. Przenieść do kwarantanny `99-🗑️-Do-Usuniecia/`. |

---

## Rozdział 2: Szczegółowa Dekompozycja Folderów Złożonych

### 2.1. Rozbicie "Wora na Wszystko": `25📄 Paweł - dokumenty` (8.2 GB, 13 podfolderów)

Folder `25📄 Paweł - dokumenty` to historyczne nagromadzenie plików z lat 2012–2025. Poniższa tabela przedstawia precyzyjną ścieżkę docelową dla każdego z jego 13 podfolderów:

| Podfolder w `25` | Zawartość / Rola | Ścieżka Docelowa w Nowej Strukturze |
| :--- | :--- | :--- |
| `00. Michaś/` | Sprawy Michała, dokumenty, pamiątki | `01-👨‍👩‍👧‍👦-Rodzina/04-Michal/` |
| `00. Nadia/` | Sprawy Nadii, ZHP, zaświadczenia | `01-👨‍👩‍👧‍👦-Rodzina/03-Nadia/` |
| `01. Natalka/` | Sprawy osobiste, pasje, projekty żony | `01-👨‍👩‍👧‍👦-Rodzina/02-Natalka/` |
| `02. Finanse/` | Stare wyciągi, umowy kredytowe, analizy | `05-💰-Finanse/03-Banki-i-Kredyty/` (lub `01-Budzet-i-Analizy/`) |
| `03. NFZ/` | Deklaracje NFZ, zaświadczenia zdrowotne | `03-🏥-Zdrowie/Archiwum-Medyczne/` |
| `04. CV/` | Archiwalne wersje życiorysu, certyfikaty | `04-📄-Dokumenty-Osobiste/Kariera-i-CV/` |
| `05. DWH/` | Materiały z inżynierii danych i hurtowni | `07-🏢-Praca-i-Projekty/Projekty-Historyczne/` |
| `05. Samochód/` | Dokumentacja serwisowa i kupna aut | `12-🚗-Pojazdy/` |
| `06. Praca/` | Umowy, aneksy, dokumenty formalne | `04-📄-Dokumenty-Osobiste/Kariera-i-CV/` |
| `11. Instrukcje obsługi/`| Instrukcje AGD/RTV i sprzętu domowego | `10-🏠-Mieszkanie-i-Nieruchomosci/02-Remonty-i-Wyposazenie/` |
| `50. Zdrowie/` | Wyniki badań, konsultacje lekarskie | `03-🏥-Zdrowie/Pawel/` |
| `90. SVN Repo/` | Dawne repozytoria kodu źródłowego | `90-🗄️-Archiwum/Stare-Projekty/` |
| `96. Studia/` | Materiały, skrypty i notatki z uczelni | `90-🗄️-Archiwum/Archiwum-Studiow/` |

### 2.2. Rozproszenie Parasolowego Folderu `10 ☂️ Ubezpieczenie`

Folder `10 ☂️ Ubezpieczenie` naruszał zasadę jedynego źródła prawdy (Single Source of Truth), dublując ubezpieczenia aut, nieruchomości i wyjazdów:

1. `02 Toyota Corolla - ubezpieczenie/` ➔ przenieść do `12-🚗-Pojazdy/Toyota-Corolla/`
2. `VW Golf - Opole/` ➔ przenieść do `12-🚗-Pojazdy/Samochod-Drugi/`
3. `20. Mieszkanie Pod Strzechą Ubezpieczenie/` ➔ przenieść do `10-🏠-Mieszkanie-i-Nieruchomosci/01-Pod-Strzecha-7/`
4. `NNW Nadii i Michasia/` ➔ przenieść do `01-👨‍👩‍👧‍👦-Rodzina/01-Wazne-Dokumenty/`
5. `2025 Słowacja Natalki/` ➔ przenieść do `24-🏖️-Podroze-i-Wyjazdy/2025/`

### 2.3. Konsolidacja Nieruchomości: `06🏠Mieszkanie`, `15🏡Lewickie` i `16🏡Pokój`

* **Pod Strzechą 7**: Foldery `06🏠Mieszkanie/05. Pod Strzechą 7/` oraz rachunki za energię z `16🏡Pokój/Energia Elektryczna/` zostają połączone w spójny moduł:
  * `10-🏠-Mieszkanie-i-Nieruchomosci/01-Pod-Strzecha-7/`
  * `10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia/`
* **Lewickie**: Zachowuje autonomię jako dedykowany zasób `11-🏡-Lewickie/` z podfolderami `Eksploatacja-i-Oplaty/` oraz `Geodezja-i-Dokumentacja/`.

---

## Rozdział 3: Kompletna Mapa Wszystkich 52 Plików Leżących Luzem w Root

Poniższa tabela przypisuje **każdy pojedynczy plik** zdiagnozowany w katalogu głównym `Mój dysk` do jego właściwego miejsca w nowej strukturze oraz proponuje ujednoliconą nazwę zgodną ze standardem.

| Lp. | Aktualna Nazwa Pliku w Root | Rozmiar | Typ | Docelowy Folder | Sugerowana Nazwa Docelowa | Uzasadnienie / Instrukcja |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `0d5a2mpppx6h1lwz06r0m4okatv9.pdf` | 6.0 MB | PDF | `00-📥-Inbox/Do-Przejrzenia/` | `Do-Weryfikacji-0d5a2mpp.pdf` | Plik o nazwie hashowej, wymaga jednorazowego otwarcia i właściwego nazwania. |
| 2 | `Analiza zużycia energii i fotowoltaiki.gdoc` | 3.7 KB | GDOC | `10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia/` | `2026 - Analiza zuzycia energii i fotowoltaiki.gdoc` | Opracowanie analizy rachunków za prąd i PV dla mieszkania. |
| 3 | `Analiza_Matematyczna_WEiTI_PW_Podrecznik.gdoc` | 123.8 KB | GDOC | `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/` | `Analiza Matematyczna WEiTI PW Podrecznik.gdoc` | Materiały dydaktyczne z analizy matematycznej Politechniki Warszawskiej. |
| 4 | `Apteki ALK 30.05.23.xlsx` | 27.2 KB | XLSX | `03-🏥-Zdrowie/Archiwum-Medyczne/` | `2023-05-30 - Apteki ALK Zestawienie.xlsx` | Historyczne zestawienie apteczne; przenieść do archiwum medycznego. |
| 5 | `Arkusz kalkulacyjny bez tytułu.gsheet` | 42.1 KB | GSHEET | `99-🗑️-Do-Usuniecia/` | `Arkusz kalkulacyjny bez tytulu.gsheet` | Porzucony arkusz roboczy bez danych kluczowych; kwarantanna i purge. |
| 6 | `Bilet - WH64222365.pdf` | 94.9 KB | PDF | `24-🏖️-Podroze-i-Wyjazdy/2026/` | `2026-08 - Bilet Podrozny WH64222365.pdf` | Bilet wakacyjny z sierpnia 2026 r. |
| 7 | `Czy możesz załączyć podsumowanie o które prosiłem?.gdoc` | 4.9 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Podsumowanie Rozmowy - 2026-05.gdoc` | Eksport czatu Gemini/Claude; do weryfikacji wartości merytorycznej. |
| 8 | `Dokument bez tytułu (1).gdoc` | 358.7 KB | GDOC | `99-🗑️-Do-Usuniecia/` | `Dokument bez tytulu 1.gdoc` | Porzucony szkic roboczy; kwarantanna. |
| 9 | `Dokument bez tytułu (2).gdoc` | 5.2 KB | GDOC | `99-🗑️-Do-Usuniecia/` | `Dokument bez tytulu 2.gdoc` | Porzucony szkic roboczy; kwarantanna. |
| 10 | `Dokument bez tytułu.gdoc` | 1.7 KB | GDOC | `99-🗑️-Do-Usuniecia/` | `Dokument bez tytulu.gdoc` | Pusty szkic; kwarantanna. |
| 11 | `Dowód osobisty - Paweł Trzeciakowski.pdf` | 837.3 KB | PDF | `00-🔒-Poufne-Dokumenty/Tozsamosc/` | `Dowod Osobisty - Pawel Trzeciakowski.pdf.cpt` | **UWAGA:** Skan tożsamości. Należy zaszyfrować (Cryptomator / 7-Zip AES-256) przed chmurą! |
| 12 | `Dowód osobisty - mama.pdf` | 798.6 KB | PDF | `00-🔒-Poufne-Dokumenty/Tozsamosc/` | `Dowod Osobisty - Mama.pdf.cpt` | **UWAGA:** Skan tożsamości. Wymagane szyfrowanie klienckie. |
| 13 | `Dziennik.gdoc` | 8.7 MB | GDOC | `04-📄-Dokumenty-Osobiste/Dziennik/` | `Dziennik Pawla.gdoc` | Główny dziennik refleksji i notatek osobistych Pawła. |
| 14 | `IMG_2312.jpeg` | 4.4 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2312.jpeg` | Zdjęcie/skan ze smartfona; przenieść do bufora lub do Google Photos. |
| 15 | `IMG_2313.jpeg` | 5.2 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2313.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 16 | `IMG_2314.jpeg` | 2.9 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2314.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 17 | `IMG_2315.jpeg` | 5.8 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2315.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 18 | `IMG_2316.jpeg` | 5.0 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2316.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 19 | `IMG_2317.jpeg` | 5.1 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2317.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 20 | `IMG_2318.jpeg` | 5.8 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2318.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 21 | `IMG_2319.jpeg` | 4.9 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2319.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 22 | `IMG_2320.jpeg` | 4.9 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2320.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 23 | `IMG_2321.jpeg` | 4.2 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2321.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 24 | `IMG_2322.jpeg` | 3.5 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2322.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 25 | `IMG_2323.jpeg` | 5.2 MB | JPEG | `00-📥-Inbox/Skany-i-Mobilne/` | `IMG_2323.jpeg` | Zdjęcie ze smartfona; przenieść do bufora / Photos. |
| 26 | `Karta kwalifikacyjna ZIELONEJ SZKOŁY CAMP DRAWA.gdoc` | 13.9 KB | GDOC | `02-🏫-Edukacja-Dzieci/Michal/` | `2026-05 - Zielona Szkola Camp Drawa - Karta Kwalifikacyjna.gdoc` | Karta wyjazdowa szkolna dziecka. |
| 27 | `LinkedIn Post - Snowflake Summit '26 Closing Draft.gdoc` | 2.7 KB | GDOC | `07-🏢-Praca-i-Projekty/Publikacje-i-Wystapienia/` | `2026-06 - LinkedIn Post Snowflake Summit Closing Draft.gdoc` | Publikacja branżowa i szkic postu na LinkedIn. |
| 28 | `OWU Warta Travel - C0517.pdf` | 379.7 KB | PDF | `24-🏖️-Podroze-i-Wyjazdy/2026/` | `2026 - OWU Warta Travel C0517.pdf` | Warunki ubezpieczenia podróżnego Warta. |
| 29 | `Pierścionek Rocznicowy Casa Batlló.gdoc` | 497.1 KB | GDOC | `01-👨‍👩‍👧‍👦-Rodzina/02-Natalka/` | `Pierscionek Rocznicowy Casa Batllo.gdoc` | Notatka i pamiątka rocznicowa (sprawy Natalki). |
| 30 | `Plan Projektu: Warstwa Semantyczna Snowflake dla FinTech & eCommerce.gdoc` | 11.8 KB | GDOC | `07-🏢-Praca-i-Projekty/2026-Biezace/` | `Plan Projektu - Warstwa Semantyczna Snowflake FinTech.gdoc` | Bieżący projekt architektoniczny Snowflake Pawła. |
| 31 | `Plan wycieczki - Tatry Wysokie (Słowacja) V2.gdoc` | 5.3 KB | GDOC | `24-🏖️-Podroze-i-Wyjazdy/2026/` | `2026-08 - Tatry Wysokie Slowacja - Plan Wycieczki V2.gdoc` | Plan wyjazdu w Tatry Słowackie (wersja aktualna). |
| 32 | `Plan wycieczki - Tatry Wysokie (Słowacja).gdoc` | 4.0 KB | GDOC | `24-🏖️-Podroze-i-Wyjazdy/2026/` | `2026-08 - Tatry Wysokie Slowacja - Plan Wycieczki V1.gdoc` | Wcześniejszy szkic planu wyjazdu. |
| 33 | `Pomysły na mieszkanie.gdoc` | 3.3 KB | GDOC | `10-🏠-Mieszkanie-i-Nieruchomosci/02-Remonty-i-Wyposazenie/` | `Pomysly na mieszkanie i remont.gdoc` | Notatki aranżacyjne i koncepcje wyposażenia wnętrz. |
| 34 | `Serio? Nie możesz wyciągnąć całej tej konwersacji ....gdoc` | 5.1 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Eksport Konwersacji Roboczej.gdoc` | Eksport rozmowy z asystentem AI. |
| 35 | `Strategia i Architektura Nowoczesnej Warstwy Semantycznej w Snowflake.gdoc` | 7.8 KB | GDOC | `07-🏢-Praca-i-Projekty/2026-Biezace/` | `Strategia i Architektura Warstwy Semantycznej Snowflake.gdoc` | Główny dokument koncepcyjny architektury danych. |
| 36 | `Super, dodaj jeszcze do dokumentu kartę z całą tą ....gdoc` | 3.6 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Szkic Dokumentu Roboczego.gdoc` | Eksport sesji LLM. |
| 37 | `Tak.gdoc` | 1.1 KB | GDOC | `99-🗑️-Do-Usuniecia/` | `Tak.gdoc` | Plik jednoznakowy, przypadkowo utworzony; kwarantanna. |
| 38 | `Ubezpieczenie - Toyota Corolla.gprj` | 0.0 B | GPRJ | `12-🚗-Pojazdy/Toyota-Corolla/` | `2026 - Ubezpieczenie Toyota Corolla.gprj` | Projekt / formularz ubezpieczenia Toyoty. |
| 39 | `Ubezpieczenie - Vw Golf.gprj` | 0.0 B | GPRJ | `12-🚗-Pojazdy/Samochod-Drugi/` | `2026 - Ubezpieczenie VW Golf.gprj` | Projekt / formularz ubezpieczenia Golfa. |
| 40 | `Wzrost Nadii i Michała.gsheet` | 3.0 KB | GSHEET | `01-👨‍👩‍👧‍👦-Rodzina/01-Wazne-Dokumenty/` | `Wzrost Nadii i Michala.gsheet` | Pomiary rozwojowe dzieci (rodzina / zdrowie). |
| 41 | `Zróżnicowanie Przyrodnicze Rosji - klasa 6C.gslides` | 1.3 MB | GSLIDES | `02-🏫-Edukacja-Dzieci/Nadia/` | `Klasa 6C - Zroznicowanie Przyrodnicze Rosji.gslides` | Prezentacja szkolna córki z geografii. |
| 42 | `dobrze, biorąc pod uwagę te kryteria przygotuj mi....gsheet` | 2.0 KB | GSHEET | `00-📥-Inbox/AI-Exports/` | `AI - Analiza Tabelaryczna Szkic.gsheet` | Eksport tabelaryczny wygenerowany przez AI. |
| 43 | `home_budget_categorized_2026-06-21 (1).csv` | 61.2 KB | CSV | `99-🗑️-Do-Usuniecia/` | `home_budget_categorized_duplikat.csv` | Duplikat pliku budżetowego z 21.06.2026 r.; kwarantanna. |
| 44 | `home_budget_categorized_2026-06-21.csv` | 83.4 KB | CSV | `05-💰-Finanse/01-Budzet-i-Analizy/` | `2026-06-21 - Home Budget Categorized.csv` | Plik główny kategoryzacji wydatków budżetu domowego. |
| 45 | `jeszcze raz poproszę o te wykresy, ale pokaż sumę....gdoc` | 132.7 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Analiza Wykresow Robocza.gdoc` | Eksport czatu z analizą wykresów. |
| 46 | `wprowadzenie-do-calek.docx` | 45.0 KB | DOCX | `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/` | `Wprowadzenie do calek.docx` | Opracowanie matematyczne (plik Word). |
| 47 | `wprowadzenie-do-calek.gdoc` | 4.8 KB | GDOC | `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/` | `Wprowadzenie do calek.gdoc` | Wersja Dokumentów Google tego samego opracowania. |
| 48 | `wygeneruj mi podsumowanie tej rozmowy z osateczny... (1).gdoc` | 3.5 KB | GDOC | `99-🗑️-Do-Usuniecia/` | `AI - Podsumowanie Rozmowy Duplikat.gdoc` | Duplikat eksportu AI; kwarantanna. |
| 49 | `wygeneruj mi podsumowanie tej rozmowy z osateczny....gdoc` | 3.5 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Podsumowanie Rozmowy Finalne.gdoc` | Eksport z AI; do bufora `AI-Exports`. |
| 50 | `wytnij seneta i planszowki z tekstu.gdoc` | 4.1 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Redakcja Tekstu Gry Planszowe.gdoc` | Eksport z sesji redakcyjnej AI. |
| 51 | `zostawmy ryzunki poglądowe, ale chciałbym aby był....gdoc` | 3.9 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Rysunki Pogladowe Szkic.gdoc` | Eksport z sesji LLM. |
| 52 | `zrób z tego tabelę - w kolumnach fazy życia, a w....gdoc` | 4.2 KB | GDOC | `00-📥-Inbox/AI-Exports/` | `AI - Fazy Zycia Tabela Robocza.gdoc` | Eksport promptu/tabeli z AI. |

---

## Rozdział 4: Docelowa Architektura Referencyjna ("Lean Knowledge & Asset Hub")

Wszystkie powyższe zasoby (z 28 folderów oraz 52 plików) po migracji utworzą czyste, bezspacyjne drzewo o docelowym wolumenie **15–20 GB**:

```
📁 Mój-Dysk/
│
├── 00-📥-Inbox/                                    # Główny bufor tranzytowy (retencja max 7 dni)
│   ├── AI-Exports/                                # 11 plików eksportów czatów AI z Root + Gemini Gems
│   ├── Skany-i-Mobilne/                           # 12 zdjęć IMG_2312-2323 + szybkie skany
│   └── Do-Przejrzenia/                            # Plik 0d5a2mpp... i niesklasyfikowane materiały
│
├── 00-🔒-Poufne-Dokumenty/                         # Dostęp: wyłącznie właściciel (szyfrowanie klienckie)
│   ├── Tozsamosc/                                 # Skany dowodów osobistych (Paweł, Mama) zaszyfrowane Cryptomatorem
│   └── Majatek-Akty-Notarialne/                   # Cyfrowe kopie aktów notarialnych
│
├── 01-👨‍👩‍👧‍👦-Rodzina/                                # Dawne 01 + podfoldery dzieci z dawnego folderu 25
│   ├── 01-Wazne-Dokumenty/                        # Akty stanu cywilnego, meldunki, ZUS, Wzrost Nadii i Michała
│   ├── 02-Natalka/                                # Projekty, pamiątki (np. Pierścionek Casa Batlló), sprawy osobiste
│   ├── 03-Nadia/                                  # ZHP, konie, osiągnięcia (z 01 oraz dawnego 25)
│   ├── 04-Michal/                                 # Sport, pasje, pamiątki (z 01 oraz dawnego 25)
│   └── 05-Genealogia/                             # Drzewo genealogiczne i historia rodziny
│
├── 02-🏫-Edukacja-Dzieci/                          # Centralne repozytorium szkolne
│   ├── Michal/                                    # Karta Zielonej Szkoły Camp Drawa, roczniki szkolne
│   └── Nadia/                                     # Prezentacja Rosja Klasa 6C, zaświadczenia, lektury
│
├── 03-🏥-Zdrowie/                                  # Jedyne repozytorium medyczne rodziny
│   ├── Pawel/                                     # Badania krwi, konsultacje, dawne 25/50. Zdrowie
│   ├── Natka/                                     # Konsultacje, badania specjalistyczne
│   ├── Dzieci/                                    # Pediatra, stomatologia, bilanse, szczepienia
│   ├── Rodzice/                                   # Dokumentacja medyczna seniorów (dawne Mama/)
│   └── Archiwum-Medyczne/                         # Dawne _Archiwum, NFZ, LuxMed Roche, Apteki ALK
│
├── 04-📄-Dokumenty-Osobiste/                       # Rozwój osobisty i kariera Pawła
│   ├── Dziennik/                                  # Dziennik.gdoc z katalogu głównego
│   ├── Kariera-i-CV/                              # Dawne 25/04. CV, świadectwa pracy, umowy
│   └── Certyfikaty-i-Szkolenia/                   # Uprawnienia inżynierskie, certyfikaty Snowflake/Cloud
│
├── 05-💰-Finanse/                                  # Finanse osobiste i budżet domowy
│   ├── 01-Budzet-i-Analizy/                       # Arkusze home_budget_categorized_2026-06-21.csv
│   ├── 02-Podatki-PIT/                            # Roczne deklaracje podatkowe (rocznikami)
│   ├── 03-Banki-i-Kredyty/                        # Umowy kredytowe z dawnego 05 i 25
│   ├── 04-Inwestycje-i-Emerytura/                 # IKE/IKZE, plany emerytalne (dawne 97. Emerytura)
│   └── 05-Paragony-i-Gwarancje/                   # Pełne scalenie dawnego folderu 98🧾Paragony (54 pliki)
│
├── 07-🏢-Praca-i-Projekty/                         # Projekty zawodowe i wiedza inżynierska
│   ├── 2026-Biezace/                              # Warstwa Semantyczna Snowflake, notatki bieżące
│   ├── Projekty-Historyczne/                      # Allegro, Roche, HSBC, dawne 25/05. DWH
│   ├── Publikacje-i-Wystapienia/                  # Posty LinkedIn Summit '26, prezentacje
│   └── Warsztaty-i-Materialy-Szkoleniowe/         # Własne szablony architektoniczne i dbt
│
├── 10-🏠-Mieszkanie-i-Nieruchomosci/               # Sprawy majątkowe Pod Strzechą 7
│   ├── 01-Pod-Strzecha-7/                         # Umowy z administracją, ubezpieczenie mieszkania
│   ├── 02-Remonty-i-Wyposazenie/                  # Pomysły na mieszkanie, faktury AGD, instrukcje z 25
│   ├── 03-Media-i-Energia/                        # Analiza energii i fotowoltaiki, rachunki z 16 Pokój
│   └── 04-Infrastruktura-Domowa-i-Siec/           # Schematy sieci domowej z dawnego 06/10. Sieć
│
├── 11-🏡-Lewickie/                                 # Działka i dom wiejski
│   ├── Eksploatacja-i-Oplaty/                     # Rachunki Plus, opłaty bieżące
│   └── Geodezja-i-Dokumentacja/                   # Podział działki, mapy geodezyjne
│
├── 12-🚗-Pojazdy/                                  # Eksploatacja floty domowej
│   ├── Toyota-Corolla/                            # Przeglądy, polisa z dawnego 10, projekt ubezpieczenia .gprj
│   └── Samochod-Drugi/                            # Dokumentacja i polisa VW Golf z dawnego 10, projekt .gprj
│
├── 20-📚-Wiedza-i-Rozwoj/                          # Nauka i materiały merytoryczne
│   ├── 01-Inzynieria-Danych-i-AI/                 # Artykuły, whitepapery
│   ├── 02-Matematyka-i-Nauka/                     # Podręcznik WEiTI PW, wprowadzenie do całek (.docx/.gdoc)
│   └── 03-Ebooki-i-Publikacje/                    # Ebooki z dawnego folderu 20 (Sila komunikacji itp.)
│
├── 21-🎵-Audio-i-Multimedia/                       # Dawne 92🎵 Muzyka (audiobooki dzieci: Narnia, Karlsson)
├── 22-🏃-Sport-i-Aktywnosc/                        # Dawne 85🏃 Bieganie (plany, zawody, logi 2018-2025)
├── 23-🎮-Gry-i-Hobby/                              # Dawne 93🎮 Gry (Minecraft, VCMI)
├── 24-🏖️-Podroze-i-Wyjazdy/                        # Dawne 08🏖️ Wakacje + plany Tatry 2026, bilety, OWU Warta
│
├── 80-📱-Aplikacje-i-Synchronizacja/
│   ├── 80-Notability-Backup/                      # Backup notatek z iPada (dawny folder Notability)
│   └── 81-Obsidian-Sync/                          # Kopia repozytorium Obsidian Markdown (dawne 11. Obsydian)
│
├── 90-🗄️-Archiwum/                                 # Zamrożone zasoby archiwalne
│   ├── Archiwum-Dzialalnosci-Gospodarczej/        # Dawna działalność gospodarcza (2020)
│   ├── Archiwum-Studiow/                          # Dawne materiały studenckie (25/96. Studia)
│   └── Stare-Projekty/                            # Dawne 94 Oprogramowanie, SVN repo, archiwa pre-2021
│
├── 95-💽-Takeout/                                  # TYMCZASOWY bufor Takeout (~536 GB)
│   └── takeout-20261010T...-*.zip                 # ➔ Zrzut na zewnętrzny dysk SSD/HDD i definitywny purge z gDrive!
│
└── 99-🗑️-Do-Usuniecia/                             # Kwarantanna 30-dniowa (arkusze bez tytułu, duplikaty, Chrome)
```

---

## Rozdział 5: 6-Etapowy Algorytm Wdrożenia (Playbook Migracji)

Aby proces migracji przebiegł bezbłędnie, bez kolizji i bez ryzyka utraty danych, należy go wykonać w następującej sekwencji:

### Etap 1: Utworzenie Nowych Folderów Szkieletowych
W katalogu głównym tworzymy nowe foldery o ustandaryzowanych nazwach (jeśli jeszcze nie istnieją):
1. `00-📥-Inbox/` (oraz podfoldery `AI-Exports/`, `Skany-i-Mobilne/`, `Do-Przejrzenia/`)
2. `00-🔒-Poufne-Dokumenty/` (`Tozsamosc/`, `Majatek-Akty-Notarialne/`)
3. `10-🏠-Mieszkanie-i-Nieruchomosci/`
4. `12-🚗-Pojazdy/` (`Toyota-Corolla/`, `Samochod-Drugi/`)
5. `21-🎵-Audio-i-Multimedia/`
6. `22-🏃-Sport-i-Aktywnosc/`
7. `23-🎮-Gry-i-Hobby/`
8. `24-🏖️-Podroze-i-Wyjazdy/`
9. `80-📱-Aplikacje-i-Synchronizacja/`
10. `99-🗑️-Do-Usuniecia/`

### Etap 2: Triage i Sprzątnięcie Katalogu Głównego (52 Pliki w Root)
Przeniesienie wszystkich 52 plików luzem zgodnie z tabelą w Rozdziale 3:
* 11 plików eksportów AI ➔ `00-📥-Inbox/AI-Exports/`
* 12 zdjęć `IMG_2312`–`IMG_2323` ➔ `00-📥-Inbox/Skany-i-Mobilne/`
* 2 skany dowodów ➔ `00-🔒-Poufne-Dokumenty/Tozsamosc/` (po zaszyfrowaniu)
* Dziennik ➔ `04-📄-Dokumenty-Osobiste/Dziennik/`
* Pliki Snowflake i projekty pracy ➔ `07-🏢-Praca-i-Projekty/2026-Biezace/`
* Pliki całek i podręcznik PW ➔ `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/`
* Pliki Tatr i bilety ➔ `24-🏖️-Podroze-i-Wyjazdy/2026/`
* Pliki śmieciowe i duplikaty ➔ `99-🗑️-Do-Usuniecia/`

### Etap 3: Przemianowanie i Standaryzacja Istniejących Folderów Bazowych
* `01👨‍👩‍👧‍👦 Rodzina` ➔ zmiana nazwy na `01-👨‍👩‍👧‍👦-Rodzina`
* `02🏫Szkoła` ➔ zmiana nazwy na `02-🏫-Edukacja-Dzieci`
* `03🏥Zdrowie` ➔ zmiana nazwy na `03-🏥-Zdrowie`
* `05💰Finanse` ➔ zmiana nazwy na `05-💰-Finanse`
* `07🏢Praca` ➔ zmiana nazwy na `07-🏢-Praca-i-Projekty`
* `15🏡Lewickie` ➔ zmiana nazwy na `11-🏡-Lewickie`
* `96🗄️Archiwum` ➔ zmiana nazwy na `90-🗄️-Archiwum`
* `Takeout` ➔ zmiana nazwy na `95-💽-Takeout`

### Etap 4: Scalanie i Dekompozycja Folderów Specjalnych
1. **Likwidacja `98🧾Paragony`**: Przeniesienie 54 plików do `05-💰-Finanse/05-Paragony-i-Gwarancje/` i usunięcie pustego folderu `98`.
2. **Likwidacja `10 ☂️ Ubezpieczenie`**: Przeniesienie polis do aut, mieszkania i wyjazdów zgodnie z Rozdziałem 2.2.
3. **Likwidacja `16🏡Pokój`**: Przeniesienie energii do `10-🏠-Mieszkanie-i-Nieruchomosci/03-Media-i-Energia/`.
4. **Likwidacja `Analiza_Matematyczna_WEiTI`**: Przeniesienie 2 plików do `20-📚-Wiedza-i-Rozwoj/02-Matematyka-i-Nauka/`.
5. **Likwidacja `Gemini Gems`**: Przeniesienie do `00-📥-Inbox/AI-Exports/`.
6. **Dekompozycja `25📄 Paweł - dokumenty`**: Rozdzielenie 13 podfolderów zgodnie z Rozdziałem 2.1 i usunięcie folderu nadrzędnego.
7. **Przeniesienie aplikacji**: `Notability` ➔ `80-📱-Aplikacje-i-Synchronizacja/80-Notability-Backup/`, `11. Obsydian` ➔ `80-📱-Aplikacje-i-Synchronizacja/81-Obsidian-Sync/`.

### Etap 5: Obsługa i Definitywne Rozliczenie Katalogu `95-💽-Takeout/` (535.8 GB)
1. Pobranie archiwów `takeout-*.zip` przez interfejs przeglądarkowy lub narzędzie dedykowane na zewnętrzny dysk HDD/SSD lub domowy NAS.
2. Zweryfikowanie integralności archiwów (`archive_browser.html`, wyrywkowe rozpakowanie próbek zdjęć).
3. Usunięcie folderu `95-💽-Takeout/` z Dysku Google do Kosza.
4. Opróżnienie Kosza na Dysku Google ➔ **odzyskanie ponad 530 GB wolnej pamięci w Google One**.

### Etap 6: Ostateczne Czyszczenie Kwarantanny
1. Sprawdzenie zawartości `99-🗑️-Do-Usuniecia/` (obejmującej porzucone arkusze, foldery `Zapisane z Chrome`, duplikaty).
2. Po 30 dniach od wykonania migracji – trwałe usunięcie zawartości kwarantanny.
3. Potwierdzenie osiągnięcia stanu **Zero-Root**: katalog główny `Mój dysk` zawiera wyłącznie 19 ustandaryzowanych folderów głównych, bez ani jednego pliku leżącego luzem.
