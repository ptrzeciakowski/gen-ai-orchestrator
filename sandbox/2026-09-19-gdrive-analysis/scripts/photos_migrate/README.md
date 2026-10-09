# Migracja Dysk Google → Google Photos (API)

Skrypt: [migrate_to_photos.py](migrate_to_photos.py). Czyta zdjęcia z zamontowanego Dysku
(`~/Library/CloudStorage/GoogleDrive-.../Mój dysk/88📸Zdjęcia`) i wgrywa **oryginalne pliki**
do Google Photos, więc cały EXIF (data, GPS) zostaje.

## Ważne ograniczenia (stan na 2025/2026)
* API pozwala tylko **dodawać** (`photoslibrary.appendonly`) – nie odczyta ani nie zmieni Twojej biblioteki.
* Limit **10 000 żądań/dzień** na projekt → ~31 tys. plików = **ok. 4 dni**. Skrypt sam się zatrzymuje
  (budżet 9 500) i wznawia od miejsca przerwania. Doba kwotowa kończy się o północy PT (~9:00 w Polsce).
* Folderów nie da się przenieść jako albumów 1:1. Domyślnie: **album na rocznik** (`--albums year`),
  a w **opisie każdego zdjęcia** jest `Źródło: Dysk Google / <ścieżka>` (da się po tym wyszukiwać).
* Pliki **bez daty EXIF** dostaną datę wgrania, chyba że użyjesz `--stamp-missing` (wgrywa KOPIĘ z datą
  z nazwy pliku lub z roku w nazwie folderu; oryginał na Dysku nie jest ruszany).
* Wgrane pliki **zużywają miejsce w Google One** (ta sama pula co Dysk) – oryginał na Dysku usuwasz dopiero
  po weryfikacji i kopii offline (Faza 0 z dokumentu 06).

## Krok 1 – jednorazowa konfiguracja Google Cloud (ok. 10 min)
1. <https://console.cloud.google.com> → nowy projekt (np. `photos-migrate`).
2. *APIs & Services → Library* → włącz **Photos Library API**.
3. *OAuth consent screen* → typ External → dodaj siebie (`ptrzeciakowski@gmail.com`) jako **Test user**.
   (W trybie Testing token odświeżania wygasa po 7 dniach – wystarczy na ~4 dni migracji.)
4. *Credentials → Create credentials → OAuth client ID → Desktop app* → pobierz JSON
   i zapisz jako `credentials.json` **w tym folderze** (jest w `.gitignore`).

## Krok 2 – środowisko
```bash
cd sandbox/2026-09-19-gdrive-analysis/scripts/photos_migrate
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
brew install exiftool        # opcjonalnie: tylko dla scan --check-dates i --stamp-missing
```

## Krok 3 – użycie
```bash
# 1) Raport bez wgrywania (pliki, GB, ile dni, które formaty pominięte)
.venv/bin/python migrate_to_photos.py scan --check-dates

# 2) PILOTAŻ: 20 plików. Sprawdź w photos.google.com daty, mapę, opis, album.
.venv/bin/python migrate_to_photos.py upload --limit 20 --stamp-missing

# 3) Pełna migracja – uruchamiaj raz dziennie, aż status pokaże pending = 0
.venv/bin/python migrate_to_photos.py upload --stamp-missing

# Stan / błędy
.venv/bin/python migrate_to_photos.py status
.venv/bin/python migrate_to_photos.py upload --retry-failed
```
Przy pierwszym uruchomieniu otworzy się przeglądarka z logowaniem Google (zakres: tylko dodawanie).

## Bezpieczeństwo danych
* Skrypt **niczego nie usuwa ani nie modyfikuje** na Dysku (tylko czyta).
* Stan w `.state/state.db` (SQLite): plik jest `uploaded` dopiero po potwierdzeniu `batchCreate`.
  Przerwanie w dowolnym momencie jest bezpieczne – wznowienie nie dubluje plików.
* Deduplikacja po SHA-1 (identyczne pliki w różnych folderach wgrywane raz; wyłączysz `--no-dedup`).
* Wykluczenia z audytu (`2017 (1)`, `2015 (1)`, `Fotograf/Kopia`) – nadpisz przez `--exclude REGEX`.
