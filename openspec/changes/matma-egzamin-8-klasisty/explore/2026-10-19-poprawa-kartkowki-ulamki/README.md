# Poprawa kartkówki: ułamki i zaokrąglanie

Pięć kart supermocy, po jednym celu z kartkówki. Każda karta i każdy arkusz to **jedna strona A4**.

## Kolejność

| # | Cel | Karta | Arkusz dla Nadii | Klucz dla Pawła |
|---|-----|-------|------------------|-----------------|
| 1 | Odwrotność vs liczba przeciwna | `karty/1-odwrotnosc.pdf` | `quizy/1-arkusz.pdf` | `quizy/1-klucz.pdf` |
| 2 | Rozwinięcia skończone czy nieskończone | `karty/2-skonczone-nieskonczone.pdf` | `quizy/2-arkusz.pdf` | `quizy/2-klucz.pdf` |
| 3 | Minuty na godziny w ułamku dziesiętnym | `karty/3-minuty-na-godziny.pdf` | `quizy/3-arkusz.pdf` | `quizy/3-klucz.pdf` |
| 4 | Porównywanie ułamków | `karty/4-porownywanie.pdf` | `quizy/4-arkusz.pdf` | `quizy/4-klucz.pdf` |
| 5 | Zaokrąglanie | `karty/5-zaokraglanie.pdf` | `quizy/5-arkusz.pdf` | `quizy/5-klucz.pdf` |

## Jak pracować

1. Karta to ściągawka: najpierw reguła, potem ilustracja, potem przykłady.
2. Arkusz to 5-minutowy sprawdzian (6 pkt). Klucz **nie jest dla Nadii**.
3. Po każdej karcie: arkusz, klucz, poprawa.

## Struktura folderu

- `preambula.tex` – wspólny szablon (A4, kolory, ramki `regula` i `pulapka`, nagłówek `naglowekKarty`).
- `karty/` – pliki `.tex` i `.pdf` kart.
- `quizy/` – arkusze (`-arkusz`) i klucze (`-klucz`).
- `build.sh` – kompiluje wszystko i sprawdza, czy każdy PDF ma jedną stronę.
- `karta-supermocy-cheat-sheet.*` oraz `quizy-sukcesu-5-minut.*` – poprzednia wersja, do usunięcia po akceptacji.

## Budowanie

```bash
brew install tectonic   # raz
./build.sh
```

Czcionka w `preambula.tex` to Arial z `/System/Library/Fonts` (macOS). Na innym systemie trzeba ją zmienić.
