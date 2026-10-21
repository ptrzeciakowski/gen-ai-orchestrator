# Tracker porządkowania Dysku (poziom folderów w root)

Ręczne porządkowanie katalog po katalogu (od 2026-10-21). Zasady: [design.md](./design.md) §3–4. Stan na **2026-10-21**.

Legenda: ✅ zrobione · 🟡 częściowo / czeka na akcję · ⬜ nie ruszane

## Konwencja nazw (stan wdrożenia)

- ✅ Root: 20 folderów w formacie `NN <emoji> Nazwa Ze Spacjami` (jedno emoji, polskie znaki).
- ✅ Reguły zapisane w `design.md` (foldery, podfoldery, zbędne spacje w nazwach plików, imiona).

## Foldery w root

| Folder | Nazwa root | Zawartość przejrzana | Podfoldery / pliki | Uwagi |
|---|---|---|---|---|
| `00 📥 Inbox` | ✅ | ⬜ | ⬜ | |
| `01 🔒 Poufne Dokumenty` | ✅ | ✅ | ✅ | **Zakończone 2026-10-21.** Szczegóły niżej. |
| `02 👪 Rodzina` | ✅ | ✅ | 🟡 | **W trakcie 2026-10-21.** Szczegóły niżej. |
| `03 🏥 Zdrowie` | ✅ | ⬜ | ⬜ | |
| `04 🏫 Edukacja Dzieci` | ✅ | ⬜ | ⬜ | |
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
- 🟡 Do decyzji: duplikaty względem `01 Tożsamość` — `Pawel - prawo jazdy.pdf`, `Skrócony odpis aktu małżeństwa.pdf`, `Michał - dowód osobisty.heic` (wersje w Rodzinie mogą być inne skany).
- 🟡 Skrót do `00 ‼️ Ważne dokumenty/Karta szczepień - Michał` oraz sam folder `00` — usunąć po decyzji.
- ⬜ Skróty ręczne (konektor ich nie tworzy): zdrowie Natalki w `01 Natalka`; opinia `2026.06.16 - Ocena…` w Zdrowie/Nadia; ewentualnie Pawła.
- ⬜ `Zdrowie/Natka` → rozważyć `Natalka` przy porządkowaniu Zdrowia; wnętrze `04 Edukacja Dzieci/Nadia` i `Zdrowie` bez zmian (osobny przebieg).
- ⬜ Etap B: `Zrzut ekranu …jpeg.png`, pliki bez rozszerzenia w `04 Kuba`, `passa 2021 -wyniki.pdf` itd.

## Do zsynchronizowania w repozytorium po zakończeniu porządków

- ⬜ `ROOT_RENAMES` w `scripts/gdrive_migration/migrate.py` (stare nazwy docelowe z myślnikami) oraz testy `test_planner.py`.
- ⬜ Drzewo i mapowanie w `analysis/07`, `09` (nazwy z myślnikami; oznaczone jako historyczne w `design.md`).
- ⬜ `tasks.md` i `proposal.md`: liczby (53 pliki w root → 5), status Etapu A, zadania wynikające z ręcznej reorganizacji.
- ⬜ Decyzje otwarte z `design.md` §7 (m.in. Pokój/Działka, Ubezpieczenia, `Dokumenty Osobiste`).
