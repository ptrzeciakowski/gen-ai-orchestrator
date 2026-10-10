# Weryfikacja kompletności zdjęć w Google Photos (Takeout → Dysk Google)

Data: 2026-10-10 | Status: **pomysł do sprawdzenia** (nic jeszcze nie zrobione)

## Cel

Sprawdzić, które z ok. 30 000 lokalnych zdjęć (`~/Library/CloudStorage/GoogleDrive-.../Mój dysk/88📸Zdjęcia/`) **nie** są jeszcze w Google Photos.

## Ustalenia z sesji

- Google Photos Library API (od 31.03.2025) widzi tylko treści wgrane przez samą aplikację → nie nadaje się do audytu całej biblioteki. `rclone` i `gphotos-sync` odpadają z tego samego powodu.
- Automatyzacja przeglądarki (subagent `browser` + Chrome z `chrome://inspect/#remote-debugging`) działa, ale jest za wolna na 30 000 zdjęć. Nadaje się do punktowej weryfikacji.
- Test na `IMG_3264.jpg` (2009_03, Canon PowerShot A580): znaleziony w Google Photos, nazwa, data 17:15:37, wymiary 3264×2448 i rozmiar 814 488 B się zgadzają. Wyszukiwanie po nazwie jest „rozmyte", więc skuteczne okazało się wyszukiwanie po dacie.
- Takeout **nie ma** opcji „tylko JSON". Plik JSON zawiera `title` i `photoTakenTime`, ale nie ma w nim rozmiaru, wymiarów, modelu aparatu ani hasha.
- Pełne dopasowanie wymaga hasha zdjęcia, więc zdjęcia trzeba przetworzyć, ale **nie trzeba ich trzymać** (streaming ZIP-ów).

## Pomysł

Takeout z Google Photos zapisany na Dysku Google → paczki ZIP synchronizują się na Maca → skrypt przetwarza je po kolei (indeksuje i usuwa) → porównanie z indeksem lokalnych plików.

## Kroki

### 1. Przygotowanie
- [ ] Sprawdzić wolne miejsce na dysku Maca i na Dysku Google. Paczki Takeout zajmą na Dysku tyle, ile cała biblioteka. Zwiększyć limit albo zdecydować, że paczki będą kasowane po przetworzeniu.
- [ ] Zainstalować `exiftool` (`brew install exiftool`) i zdecydować, czy używać `uv` do skryptu Pythona.
- [ ] Ustalić folder roboczy np. `sandbox/<data>-google-photos-completeness/` i plik indeksu `index.sqlite` (wznawialny).

### 2. Zamówienie Takeoutu
- [ ] Wejść na [takeout.google.com](https://takeout.google.com) → „Odznacz wszystko" → zaznaczyć tylko **Google Photos**.
- [ ] Wybrać albumy: najlepiej rocznikami („Photos from 2009", „Photos from 2010", ...) albo wszystko, jeśli jest mało miejsca na Dysku, to roczniami.
- [ ] Metoda dostarczenia: **Dodaj do Dysku**. Format `.zip`, rozmiar paczki np. **2 GB** (małe paczki ułatwiają streaming i wznawianie).
- [ ] Zamówić jednorazowy eksport. Ewentualnie zrobić najpierw próbny eksport jednego rocznika (np. 2009).
- [ ] Poczekać na mail od Google. Eksport może trwać od godzin do dni.

### 3. Indeks lokalnych zdjęć
- [ ] Skrypt przechodzi po `88📸Zdjęcia` i zapisuje: ścieżkę, nazwę, rozmiar, SHA-256, datę wykonania (EXIF `DateTimeOriginal`), wymiary, model aparatu.
- [ ] Indeks jest wznawialny. Hash liczony tylko dla plików zmienionych od ostatniego przebiegu (po rozmiarze i mtime).
- [ ] Uwaga: pliki w `CloudStorage` mogą być „tylko online". Odczyt może je pobierać, więc sprawdzić tryb synchronizacji (Dublowanie vs Strumieniowanie).

### 4. Indeks Takeoutu (streaming)
- [ ] Skrypt czyta kolejne ZIP-y z folderu Dysku Google i **nie rozpakowuje ich w całości**.
- [ ] Dla każdego zdjęcia z ZIP-a liczy SHA-256 i zapisuje rozmiar. Z JSON obok bierze `title`, `photoTakenTime`, `creationTime`.
- [ ] Obsługuje przyrostek `-edited`, duplikaty w wielu albumach i nazwy typu `IMG_3264(1).jpg`. Uzupełnia indeks i zapisuje, które paczki zostały już przetworzone.
- [ ] Po przetworzeniu paczki można ją usunąć lokalnie. Najpierw zrobić próbę na jednej paczce.

### 5. Dopasowanie
Kolejność kryteriów, od najpewniejszego:
1. identyczny SHA-256 → **jest w Google Photos**,
2. ta sama nazwa + rozmiar,
3. ta sama data wykonania (co do sekundy) + wymiary + model aparatu. To dla zdjęć wgranych w trybie „Oszczędzanie miejsca", które mają inny rozmiar i hash,
4. zapasowo: nazwa + `photoTakenTime` z JSON.

### 6. Raport
- [ ] **Brakujące:** pliki bez żadnego dopasowania. Lista do wgrania.
- [ ] **Niepewne:** dopasowania tylko po kryterium 3 lub 4. Lista do ręcznej kontroli (np. subagentem `browser` po dacie).
- [ ] **Duplikaty lokalne:** pliki o identycznym SHA-256 w kilku miejscach.
- [ ] Podsumowanie: liczba plików, ile dopasowanych na którym poziomie, ile brakuje.

### 7. Po audycie
- [ ] Wgrać brakujące zdjęcia (Google Photos / Drive for desktop z włączonym backupem folderu) i powtórzyć porównanie na nowym Takeoucie albo punktowo.
- [ ] Usunąć paczki Takeout z Dysku Google, żeby nie zajmowały miejsca.

## Otwarte pytania / ryzyka

- Ile miejsca zajmuje biblioteka Google Photos i czy mieści się na Dysku Google?
- Czy zdjęcia były wgrywane w jakości oryginalnej, czy „Oszczędzanie miejsca"? Od tego zależy, ile dopasowań będzie tylko po metadanych.
- Czy Takeout nie zmienia EXIF dla części plików (np. dodając lokalizację)? Hash może wtedy nie pasować, więc potrzebne jest kryterium 3.
- Pliki wideo: czy też sprawdzamy?
- Wcześniejsza analiza Dysku (`sandbox/2026-09-19-gdrive-analysis`, skrypty `scan_drive.py`, `flatten_photos.py`) może dać gotowy lokalny indeks do wykorzystania.

## Następny krok

Zrobić **próbny Takeout jednego rocznika** (np. 2009, folder `2009_03` z `IMG_3264.jpg` jako przypadek testowy), zmierzyć czas eksportu i rozmiar. Potem napisać skrypt.

## Skrypt i wyniki testów (2026-10-10)

Skrypt: [`scripts/gphotos_audit.py`](scripts/gphotos_audit.py) (tylko stdlib, `python3`), testy: [`scripts/test_gphotos_audit.py`](scripts/test_gphotos_audit.py).

```bash
cd sandbox/2026-10-10-google-photos-completeness-explore/scripts
python3 gphotos_audit.py --db ../index.sqlite index-local  "<folder ze zdjęciami>"
python3 gphotos_audit.py --db ../index.sqlite index-takeout "<folder z takeout-*.zip>"   # lub kilka ścieżek / rozpakowany Takeout
python3 gphotos_audit.py --db ../index.sqlite report --out ../raport
python3 test_gphotos_audit.py -v   # testy
```

- Oba indeksowania są wznawialne: lokalne pomija pliki o niezmienionym rozmiarze i mtime, a Takeout pomija przetworzone paczki.
- Paczki ZIP są czytane strumieniowo, nic nie jest rozpakowywane. Skrypt **niczego nie usuwa**, paczki kasujesz samodzielnie po przetworzeniu.
- Raport zapisuje `missing.csv` (brakujące) i `name-only.csv` (niepewne) oraz liczby na każdym poziomie dopasowania.

**Wyniki testów:**
- 6 testów jednostkowych na syntetycznym Takeoucie przechodzi. Obejmują wszystkie poziomy (`sha256`, `name+size`, `name+time`, `name-only`, `missing`), plik `-edited`, nazwy JSON (`.supplemental-metadata`, obcięte, `(1)`), strefy czasowe i wznawianie.
- Test na prawdziwym pliku: sztuczna paczka z `IMG_3264.jpg` + folder `2009_03` (26 plików). Wynik: 2 × `sha256`. Drugi plik to lokalny duplikat `2009_03_08/IMG_3264.JPG`, więc dopasowanie jest poprawne.

**Uwagi:**
- Indeksowanie 26 plików z Dysku Google trwało ok. **16 minut**, bo pliki w `CloudStorage` były pobierane z chmury (tryb strumieniowania). Przy 30 000 plików przełącz folder na „Dublowanie plików" albo pobierz go wcześniej.
- Raport jeszcze nie pokazuje lokalnych duplikatów (identyczny SHA-256 w kilku miejscach). Dane są w bazie, brakuje tylko komendy raportu.
- Do sprawdzenia na prawdziwym Takeoucie: nazwy JSON i sposób zapisu `photoTakenTime`, bo zależą od wersji eksportu.
