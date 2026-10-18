# Raport Audytu: Bezpieczeństwo, Uprawnienia i Strategia Architektury Danych (Google Drive)
**Data audytu:** 19 września 2026 r.
**Autor:** Antigravity (Ekspert ds. Cyberbezpieczeństwa & Information Governance)
**Cel:** Niezależna, dogłębna ocena uprawnień, bezpieczeństwa danych PII/PHI oraz opracowanie polityki retencji (Cold Storage) dla dysku Pawła (267.0 GB, ~77.5 tys. plików).

---

## 1. Audyt Uprawnień i Polityka Współdzielenia (Information Sharing)

### 1.1. Analiza plików cudzych (`is_owner = False`)
W przestrzeni dyskowej zidentyfikowano **73 pliki i foldery** niebędące własnością użytkownika (np. dodane ze strumienia *Udostępnione dla mnie*). Pliki te wprowadzają szum strukturalny i narażają dysk główny na niekontrolowane zmiany ze strony osób trzecich. 

**Typologia współpracy zewnętrznej:**
*   **Współpraca szkolna/rodzinna:** Pliki dot. dzieci (np. `Nadia - prace domowe`, `rekomendacje dla szkoły.pdf`, `Karta kwalifikacyjna`).
*   **Rozrywka i hobby:** Turnieje e-sportowe (np. `Regulamin turnieju Heroes 30th Anniversary Cup`, `Narty 2027`).
*   **Współpraca zawodowa:** `Complete dbt Bootcamp slides`, `Materiały prasowe WFP18`.

### 1.2. Rekomendowana Polityka: Oddzielenie własności (Separation of Ownership)
Obecnie współdzielone zasoby są "rozrzucone" po całym dysku, co grozi przypadkową utratą dostępu (jeśli właściciel usunie plik) lub złośliwym nadpisaniem.

**Matryca docelowa zarządzania współdzieleniem:**
| Typ udostępnienia | Status obecny | Rekomendowane działanie | Ochrona przed utratą |
| :--- | :--- | :--- | :--- |
| **Bilety / Umowy / Regulaminy** | Podpięte do *Mój dysk* | Zrobić lokalną kopię (Make a copy) | Całkowita niezależność |
| **Aktywna praca zespołowa (turnieje/szkoła)** | Luźne pliki we współdzieleniu | Używać "Skrótów" (Shortcuts) zamiast "Dodaj do mojego dysku" | Zabezpiecza przed kasowaniem struktury |
| **Zakończone projekty cudze** | Zalegają na dysku | Usunąć skrót z *Mój Dysk*. W razie potrzeby plik jest w *Udostępnione dla mnie* | Porządek w root |

---

## 2. Identyfikacja Zagrożeń Bezpieczeństwa (Security & Privacy Risk Assessment)

Zidentyfikowano poważne naruszenia zasady **Least Privilege** i **Data Masking**. Brak wyizolowanej strefy dla krytycznych danych wrażliwych (PII - Personally Identifiable Information; PHI - Protected Health Information).

### 2.1. Tabela Ryzyka i Ekspozycji (Risk Matrix)

| Zagrożenie / Kategoria | Znalezione Artefakty | Poziom Ryzyka | Konsekwencje w razie wycieku (np. link sharing) |
| :--- | :--- | :--- | :--- |
| **Kradzież tożsamości (PII)** | `Dowód osobisty - Paweł Trzeciakowski.pdf` oraz `...mama.pdf` w katalogu ROOT. | **KRYTYCZNY** | Pełna kradzież tożsamości, wyłudzenia kredytowe. Brak szyfrowania spoczynkowego na poziomie pliku. |
| **Utrata dostępu (Hasła)** | Folder `91🔑Hasła` leżący w otwartej strukturze. | **KRYTYCZNY** | Potencjalne przejęcie całej cyfrowej tożsamości i kont finansowych. |
| **Dane Notarialne / Majątkowe** | `Akt notarialny`, `Umowa kupna - sprzedaży.gdoc` w starych katalogach. | **WYSOKI** | Ujawnienie statusu majątkowego, adresów, wartości transakcji, aktów własności. |
| **Dane Medyczne (PHI)** | Folder `03🏥Zdrowie` (wyniki badań, dokumenty dzieci: np. `uzasadnienie oceny zachowania.pdf`). | **WYSOKI** | Naruszenie poufności medycznej, wrażliwe dane nieletnich eksponowane w publicznej chmurze. |

### 2.2. Rekomendacja: Wdrożenie "Cyfrowego Sejfu" (Zero-Trust Data Vault)
Dane krytyczne (dowody osobiste, hasła, akty notarialne) **nie mogą** znajdować się w luźnych folderach lub, co gorsza, w katalogu Root, gdzie przypadkowe kliknięcie "Udostępnij link każdemu" naraża je na indeksację.

**Zasady Cyfrowego Sejfu:**
1. Stworzenie dedykowanego, wyizolowanego folderu (np. `00🔒Zaszyfrowany_Sejf`).
2. Pliki o najwyższym stopniu wrażliwości powinny być zaszyfrowane programem zewnętrznym (np. VeraCrypt, Cryptomator) przed wrzuceniem na gDrive.
3. Natychmiastowa relokacja skanów dowodów osobistych z katalogu głównego do wysoce zabezpieczonej przestrzeni (lub dedykowanego menedżera haseł, np. 1Password).

---

## 3. Strategia Cold Storage & Retencji Danych

Z analizy telemetrii wynika, że gospodarka danymi jest wysoce nieefektywna z perspektywy kosztowej i operacyjnej. Dysk jest w 85% "martwy".

### 3.1. Analiza stanu "zamrożenia" (Recency)
*   **Aktywne pliki (Hot):** Tylko ~1.5% plików (otwierane w ostatnich 3 latach).
*   **Całkowicie nieaktywne (Cold):** 85% plików (ponad 66 tys.) nie było otwieranych od **ponad 3 lat** lub **nigdy** (np. `95💽Kopia zapasowa` - 24 470 plików starych telefonów od 2013 r., waga 50.8 GB).
*   **Multimedialny "Słoń" w salonie:** Folder `88📸Zdjęcia` zajmuje 190 GB (75% pojemności dysku).

### 3.2. Proponowana Architektura Warstwowa (Tiering Strategy)

| Warstwa (Tier) | Charakterystyka Danych | Rekomendowane Środowisko i Akcje |
| :--- | :--- | :--- |
| **HOT STORAGE (Szybki Dostęp)** | Aktywne dokumenty, bieżące pliki pracy, domowe budżety, organizacja podróży. (ok. 1-2 GB) | Pozostawienie na standardowym Google Drive. Uporządkowanie struktury bieżącej. |
| **WARM STORAGE (Średni Dostęp)** | Dokumentacja księgowa/domowa z ostatnich lat, faktury, paragony, polisy, archiwa medyczne do konsultacji. (ok. 10-15 GB) | Google Drive, w głębszej i logicznie odseparowanej architekturze (`96🗄️Archiwum`). |
| **COLD STORAGE (Głębokie Archiwum)** | Backup starych telefonów (50.8 GB) z lat 2013-2018 (Galaxy S3, HTC), stare instalki oprogramowania, kopie systemowe. | **Należy bezwzględnie usunąć z płatnego gDrive!** Eksport do taniego nośnika (Lokalny serwer NAS / fizyczny dysk SSD / Google Cloud Storage w klasie *Coldline* lub *Archive*). |
| **MEDIA (Multimedia)** | Zdjęcia i wideo - 190 GB (`88📸Zdjęcia`). | **Migracja usługi:** Przeniesienie całych zasobów fotograficznych do dedykowanego Google Photos lub serwera Synology Photos (NAS), które oferują lepsze algorytmy zarządzania, rozpoznawanie twarzy i odciążają strukturę dokumentów. |

---

## 4. Harmonogram Wdrożenia (Action Plan)

1. **Natychmiastowe (24h):**
   * Usunąć lub przenieść `Dowód osobisty - Paweł Trzeciakowski.pdf` oraz `Dowód osobisty - mama.pdf` z katalogu głównego (Root) do szyfrowanego kontenera lub bezpiecznego menedżera haseł.
   * Zweryfikować uprawnienia udostępniania w folderze `03🏥Zdrowie` i `91🔑Hasła`.
2. **Krótkoterminowe (7 dni):**
   * Pobrać lokalnie (np. na dysk zewnętrzny) zawartość `95💽Kopia zapasowa` (50.8 GB zrzuconych danych z telefonów 2013-2018), a następnie usunąć je z Google Drive. Odzyska to ~20% całkowitej powierzchni.
   * Uporządkować współdzielone pliki cudze (utworzyć skróty).
3. **Długoterminowe (1 miesiąc):**
   * Dokonać pełnej migracji `88📸Zdjęcia` (190 GB) do rozwiązania typowo mediowego.
   * Zbudować w pełni audytowalny, zablokowany dostępem dwuskładnikowym "Cyfrowy Sejf" dla archiwów medycznych i notarialnych.
