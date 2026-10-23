# Tracker porządkowania Dysku (poziom folderów w root)

Ręczne porządkowanie katalog po katalogu (od 2026-10-21). Zasady: [design.md](./design.md) §3–4. Stan na **2026-10-23**.

Legenda: ✅ zrobione · 🟡 częściowo / czeka na akcję · ⬜ nie ruszane

## Konwencja nazw (stan wdrożenia)

- ✅ Root: 20 folderów w formacie `NN <emoji> Nazwa Ze Spacjami` (jedno emoji, polskie znaki).
- ✅ Reguły zapisane w `design.md` (foldery, podfoldery, zbędne spacje w nazwach plików, imiona).

## Foldery w root

| Folder | Nazwa root | Zawartość przejrzana | Podfoldery / pliki | Uwagi |
|---|---|---|---|---|
| `00 📥 Inbox` | ✅ | ⬜ | ⬜ | |
| `01 🔒 Poufne Dokumenty` | ✅ | ✅ | ✅ | **Zakończone 2026-10-21.** Szczegóły niżej. |
| `02 👪 Rodzina` | ✅ | ✅ | ✅ | **Zakończone 2026-10-22.** Szczegóły niżej. |
| `03 🏥 Zdrowie` | ✅ | ✅ | ✅ | **Zakończone 2026-10-23.** Szczegóły niżej. |
| `04 🏫 Edukacja Dzieci` | ✅ | ⬜ | ⬜ | Następny w kolejce (od 2026-10-24). |
| `05 💰 Finanse` | ✅ | ⬜ | ⬜ | |
| `07 🏢 Praca i Projekty` | ✅ | ⬜ | ⬜ | |
| `08 🌂 Ubezpieczenia` | ✅ | ⬜ | ⬜ | Do decyzji: osobny folder czy rozproszenie wg 09. |
| `10 🏠 Mieszkanie i Nieruchomości` | ✅ | ⬜ | ⬜ | |
| `11 🏡 Lewickie i Pokój` | ✅ | ⬜ | ⬜ | 09: rozdzielić, Pokój do potwierdzenia. |
| `12 🚗 Pojazdy` | ✅ | ⬜ | ⬜ | |
| `20 📚 Wiedza i Rozwój` | ✅ | ⬜ | ⬜ | |
| `21 🎵 Audio i Multimedia` | ✅ | ⬜ | ⬜ | |
| `22 🏃 Sport i Aktywność` | ✅ | ⬜ | ⬜ | |
| `23 🎮 Gry i Hobby` | ✅ | ⬜ | ⬜ | |
| `24 🧳 Podróże i Wyjazdy` | ✅ | ⬜ | ⬜ | |
| `80 📱 Aplikacje i Synchronizacja` | ✅ | ⬜ | ⬜ | Sprawdzić punkty zapisu Notability. |
| `90 📦 Archiwum` | ✅ | ⬜ | ⬜ | |
| `95 💽 Google Takeout` | ✅ | ⬜ | ⬜ | Tymczasowy; obsługa ręczna poza tą zmianą. |
| `99 🚮 Do Usunięcia` | ✅ | ⬜ | ⬜ | |

Pliki luzem w root: ⬜ 5 plików (3 arkusze/prezentacja/dokument Google, 1 `.doc`, 1 dokument Google) — bez przypisania do folderów.

## Szczegóły: `01 🔒 Poufne Dokumenty`

- ✅ Podfoldery: `01 Tożsamość`, `02 Majątek i Akty Notarialne`, `91 Hasła`; `Dziennik` zostaje w tym folderze.
- ✅ Nazwy plików: usunięta spacja w dowodzie (Michał), `Natalia` → `Natalka`, rozróżnione odpisy aktów urodzenia (Michał/Nadia).
- ✅ Zdublowany dowód Pawła: do kosza wersja mniejsza (`… Paweł Trzeciakowski.pdf`), zostaje `… Paweł.pdf`.
- ✅ Jawne eksporty haseł (3 × CSV) przeniesione do kosza.
- ✅ Uprawnienia: odebrany dostęp konta `natalia.trzeciakowska` do `91 Hasła` i `hasla.kdbx`; arkusz `hasla - porównanie` usunięty. Zweryfikowane przez konektor: folder 01, podfoldery, `Dziennik`, wszystkie pliki — wyłącznie właściciel.
- ⬜ Drobne: opróżnić kosz (CSV z hasłami, arkusz, zdublowany dowód) po upewnieniu się, że `hasla.kdbx` jest aktualna.

## Szczegóły: `02 👪 Rodzina`

- ✅ Podfoldery: `01 Natalka`, `02 Nadia`, `03 Michał`, `04 Kuba`, `05 Dzieci`, `10 Genealogia`.
- ✅ Do `01 🔒 Poufne Dokumenty`: `Prawo jazdy - Natalka`, `Akt zgonu - tata` (→ `01 Tożsamość`), akt notarialny Pod Strzechą (→ `02 Majątek i Akty Notarialne`).
- ✅ `Projekt pokoju` (Michał) → `10 🏠 …/05. Pod Strzechą 7`.
- ✅ Do `03 🏥 Zdrowie`: `Pantomogram`, `TK kolana lewego` → `Natka`; `Karta szczepień - Nadia` → `Nadia`.
- ✅ Do `04 🏫 Edukacja Dzieci/Nadia`: dwie opinie psychologiczne (skrót do pierwszej już jest w Zdrowie/Nadia).
- ✅ Nazwy: `2026-06-20 Wzrost Nadii i Michała` (data ostatniego pomiaru), `2024-06-04 Nadia brzydki list do Taty.pdf` (data ze skanu). Wzrost zostaje w `02 👪 Rodzina` jako pamiątka.
- ✅ Duplikaty względem `01 Tożsamość` rozwiązane (2026-10-22): w `02 Rodzina` nie ma już `Pawel - prawo jazdy.pdf` ani `Skrócony odpis aktu małżeństwa.pdf`; zostają wersje w Tożsamości. Pliki luzem w roocie Rodziny wyczyszczone (0).
- ✅ Skrót `Karta szczepień - Michał` (z `03 Michał`) usunięty; karta jest w `03 🏥 Zdrowie`, skrót w Zdrowiu wskazuje poprawnie. Folder `00 ‼️ Ważne dokumenty` — do ponownego sprawdzenia przy przeglądzie root-a.
- ✅ **`03 Michał` zakończony (2026-10-22)**, w tym ręcznie dodany folder-link do zdrowia.
- ✅ **`01 Natalka` zakończony (2026-10-22):** `Natalka - Studniówka 2006.iso` → `2006 Natalka Studniówka.iso` (zostaje w miejscu); folder-link do zdrowia dodany ręcznie.
- ✅ **`02 Nadia` zakończony (2026-10-22):** `04. ZHP` → `04 ZHP`; zmienione nazwy plików i folderów w roocie, `03 Konie` (`2026-04-12 Becker Sport` + zawartość) i `04 ZHP`; `Waga - dziennik.xlsx` → `Zdrowie/Nadia/Nadia Waga Dziennik.xlsx`. Skan `2026-03-20 Nadia Konie skan.pdf` nazwany bez sprawdzenia treści.
- ✅ **`04 Kuba` zakończony (2026-10-22):** Kuba to bratanek — materiały zostają w Rodzinie (bez skrótu do Edukacji). Folder `Matematyka` usunięty przez użytkownika. Wszystkie 19 plików w roocie z nazwami zgodnymi z konwencją i rozszerzeniami (`.pdf`, `.png`); daty z nazw lub z daty utworzenia pliku (PDF-y: 2022-03-20/27, 2022-12-04/25; PNG zadań: 2022-11-06/16; `Franek i Latarnie`: 2022-11-05). Prefiksy kodów zadań (`PIN`, `WLM`, …) zachowane jako część tematu.
- ✅ **`05 Dzieci` zakończony (2026-10-22):** `#Archiwum` → `09 Archiwum`; folder `10. Niania` (rozliczenia godzin, wzór umowy, zdjęcia 2014–2015) przeniesiony do kosza — do opróżnienia; `Basen/2020/2021` → `Basen/2020-2021`; nazwy plików/dokumentów dostosowane do konwencji (m.in. `2021 Passa wyniki.pdf`, `2023 Bieg passy`, `Urządzenia cyfrowe` bez emoji). Daty z daty utworzenia pliku.
- ✅ **`10 Genealogia` zakończony (2026-10-22):** folder na Dysku nazywał się `10 Drzewo genealogiczne` → `10 Genealogia`. 18 plików z 2024-01-21: 14 zrzutów ekranu ponumerowanych `2024-01-21 Genealogia zrzut 01…14.png` (w kolejności godzin, bez `.jpeg.png`), `Bartek`, `Nadunia`, `Brat` oraz PDF → `2024-01-21 Genealogia dokument.pdf`. Treści plików nie sprawdzano — nazwy opisowe do poprawy, jeśli będzie potrzeba.
- ✅ Skróty ręczne (konektor ich nie tworzy) wykonane przez użytkownika (2026-10-22).
- ⬜ `Zdrowie/Natka` → rozważyć `Natalka` przy porządkowaniu Zdrowia; wnętrze `04 Edukacja Dzieci/Nadia` i `Zdrowie` bez zmian (osobny przebieg).
- ✅ **`03 Michał` (2026-10-22):** root przejrzany ✅ — zostają skróty `01 Zdrowie`, `02 Szkoła` (wyjątek D3a), folder `05 Tenis` i nowy `09 Archiwum`. Usunięty `Michał - dowód osobisty.heic` (jest PDF w Tożsamości) oraz `OSWIADCZENIE.pdf`. Do `09 Archiwum` trafiły `Pamiętnik Michała` i `I Komunia` (zmieniona nazwa, bez numeru; 4 pliki wewnątrz bez zmian nazw — `Winowajcy - zaliczka.pdf` do Etapu B). ✅ `05 Tenis` (2026-10-22): pliki i foldery wydarzeń ułożone płasko w folderach `2021`, `2024`, `2025`, `2026`; `00 Podsumowanie sezonów tenisowych` zostaje w roocie. Nazwy zgodne z konwencją (bez ` - `, z rozszerzeniami `.pdf`, bez `_encrypted_`); `LTADallenglish1.pdf` → `2025-05 Tennis Canada LTAD.pdf`. Poza zakresem: zdjęcia `IMG_*`/`_DSC*` (bez daty i tematu), `UMOWA Kadra WMZT 2026.pdf`. ✅ Wnętrza folderów wydarzeń i `2025-08-25 PIT obóz zdjęcia` (~40 zdjęć) zaakceptowane jako wyjątek — zdjęcia to materiał szkoleniowy, nie pamiątka (design.md §4).
- ⬜ Etap B: `Zrzut ekranu …jpeg.png`, pliki bez rozszerzenia w `04 Kuba`, `passa 2021 -wyniki.pdf` itd.

## Szczegóły: `03 🏥 Zdrowie`

- ✅ Root (2026-10-23): podfoldery `01 Natalka` (było `Natka`), `02 Nadia`, `03 Michał`, `04 Paweł` (było `Pawel`), `05 mama`, `09 Archiwum` (było `_Archiwum`) — numeracja zgodna z `02 👪 Rodzina`.
- ✅ `Terapia M.` → `03 Michał/Terapia` (później przeniesiona przez użytkownika do roota Zdrowia). Skan `Zeskanowano 14 gru 2025…pdf` (wniosek LUX MED Swoboda Leczenia, dziecko ur. 2016 — Michał wg użytkownika) → `03 Michał/2025-12-14 LuxMed Swoboda Leczenia Wniosek.pdf` (data z nazwy skanu).
- ✅ `2024 - LuxMed w Roche` → `04 Paweł/2024 LuxMed w Roche` (umowy i oferty benefitu z pracy; wnętrze bez zmian nazw).
- ✅ `01 Natalka` (2026-10-23): nazwy w roocie zgodne z konwencją (m.in. `2025-11 Tomografia Komputerowa Osiowa` z poprawioną literówką, `TK kolana lewego`); wnętrza folderów `Pantomogram`, `TK kolana lewego`, `2025-11 …`, `2026-01 …` nie przeglądane.
- ✅ `02 Nadia` (2026-10-23): 24 pliki/skrót przemianowane; numery zleceń laboratoryjnych usunięte z nazw (`Morfologia`, `Panel testów wziewnych`), `Morfologia płytki rozmaz T4 wolne TSH` i `Panel pyłki …` datowane datą utworzenia 2024-10-05 (dokładność: data utworzenia). Pantomogram `.dcm`/`.jpg` → `2025-12-29 Pantomogram Nadia`. ⬜ Do decyzji: duplikat `Trzeciakowska_Nadia_20251229_181948.jpg` (ten sam rozmiar co zdatowany JPG).
- ✅ `03 Michał` (2026-10-23): ~40 pozycji przemianowanych (w roocie i `2025-06 Złamanie kości śródstopia`); `szkoda.pdf` → `2025-08-05 Szkoda.pdf` (data utworzenia). Duplikaty rozstrzygnięte przez użytkownika: dwa pliki z 2026-04-20 rozróżnione ręcznie (`2026-04-20 Morfologia`, `2026-04-20 Glukoza`), nowszy duplikat `Rozmowa redukująca stres` usunięty. Podfoldery `Konsultacje` i `Badania` w `2025-06 …` nieprzejrzane.
- 🟡 `Terapia` (użytkownik przeniósł ją z `03 Michał` do roota Zdrowia jako `07 Terapia m.`, 2026-10-23): pliki w środku przemianowane; użytkownik zmienił nazwę na `Terapia małżeńska` — ✅ zakończone.
- 🟡 `04 Paweł` (2026-10-23): ~40 pozycji przemianowanych w roocie, `2024 LuxMed w Roche`, `2024-05 Nerwy w konserwy by Tomek Zieliński` i `Kolano` (`#Kolano` → `Kolano`). Numery zleceń laboratoryjnych usunięte z nazw; `Badanie_lekarskie_506129921.pdf` → `2024-05-06 Badanie lekarskie.pdf` (data utworzenia); `endomondo-2020-12-10.zip` → `2020-12-10 Endomondo.zip`; poprawiona literówka `rekominanty` → `Rekomendacje`. ✅ Duplikat `Tomografia.pdf` (ten sam rozmiar co `2025-10-27 Tomografia nerwu wzrokowego.pdf`) przeniesiony do kosza — do opróżnienia. `Dziedzic etal 1.docx` w `Kolano` bez daty.
- ✅ `05 mama` (2026-10-23): 2 pliki — `2026-02-09 USG.jpg` (godzina z nazwy pominięta), `2023-08-11 MRI stawu barkowego.pdf`.
- ✅ `09 Archiwum` (2026-10-23): podfolder `Tato` → `tata`; w środku `2023 Wniosek o ZOL` (załączniki `Załącznik 1…6`) i dokumenty taty (`2022-06-28 Karta informacyjna szpitalna tata.pdf` itd.). Daty z nazw lub z daty utworzenia (`2022-07-05/07`, `2023-07-23`); pliki bez rozszerzenia dostały `.pdf`; poprawiona literówka `opieka` → `opieką`.
- ⬜ Weryfikacja: skróty z `02 Rodzina` do podfolderów Zdrowia wskazują po ID, więc powinny działać po zmianach nazw. Nieprzejrzane wnętrza: `Pantomogram`, `TK kolana lewego`, `2025-11 …`, `2026-01 …` (Natalka), `Konsultacje`, `Badania` (Michał/złamanie).

## Do zsynchronizowania w repozytorium po zakończeniu porządków

- ⬜ `ROOT_RENAMES` w `scripts/gdrive_migration/migrate.py` (stare nazwy docelowe z myślnikami) oraz testy `test_planner.py`.
- ⬜ Drzewo i mapowanie w `analysis/07`, `09` (nazwy z myślnikami; oznaczone jako historyczne w `design.md`).
- ⬜ `tasks.md` i `proposal.md`: liczby (53 pliki w root → 5), status Etapu A, zadania wynikające z ręcznej reorganizacji.
- ⬜ Decyzje otwarte z `design.md` §7 (m.in. Pokój/Działka, Ubezpieczenia, `Dokumenty Osobiste`).
