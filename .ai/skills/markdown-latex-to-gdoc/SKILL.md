---
name: markdown-latex-to-gdoc
description: Konwertuje pliki Markdown z notacją matematyczną LaTeX ($...$, $$...$$) do formatu DOCX w pełni kompatybilnego z Dokumentami Google (Google Docs), zachowując natywne symbole i równania matematyczne (OMML). Opcjonalnie synchronizuje dokument bezpośrednio z Dyskiem Google.
---

# Markdown LaTeX to Google Docs (DOCX / OMML)

## Overview (Przegląd)
Skill ten służy do bezstratnej konwersji plików Markdown zawierających formuły matematyczne w notacji LaTeX (`$ ... $` dla wzorów w linii tekstu oraz `$$ ... $$` dla równań blokowych) do formatu DOCX. 

Wykorzystuje silnik `pandoc`, który przekształca notację LaTeX bezpośrednio w natywne obiekty matematyczne Microsoft Office Math (OMML - `<m:oMath>` i `<m:oMathPara>`). Po otwarciu takiego pliku w **Dokumentach Google** (Google Docs) lub zapisaniu go jako Dokument Google, formuły są natywnie edytowalne i czytelnie wyrenderowane jako wbudowane równania Google Docs.

---

## Dependencies (Zależności)
1. **Pandoc**: Wymagany do parsowania Markdown i kompilacji równań do OMML.
   - Weryfikacja: `which pandoc`
   - Instalacja (jeśli brak): `brew install pandoc`
2. **Python 3**: Do uruchamiania skryptu pomocniczego `scripts/convert.py`.
3. **Dysk Google (opcjonalnie)**: Lokalny punkt montowania Dysku Google na macOS (np. `~/Library/CloudStorage/GoogleDrive-*/Mój dysk`), jeśli użytkownik chce natychmiastowej synchronizacji w chmurze.

---

## Quick Start (Szybki start)
Przykładowe polecenia i prompty wyzwalające ten skill:
- *"Skonwertuj plik notatki.md do formatu Google Docs / DOCX z zachowaniem wzorów."*
- *"Przekształć ten plik markdown z wzorami matematycznymi na dokument gdoc."*
- *"Zapisz plik Markdown z równaniami LaTeX do Google Docs i wrzuć na mój Dysk Google."*

---

## Workflow (Procedura postępowania agenta)

Gdy użytkownik poprosi o konwersję dokumentu Markdown z matematyką do formatu DOCX/Google Docs:

1. **Weryfikacja zależności**:
   Upewnij się, że w systemie zainstalowany jest `pandoc`:
   ```bash
   which pandoc || brew install pandoc
   ```

2. **Formatowanie LaTeX w pliku Markdown**:
   Upewnij się, że wzory w Markdown są sformatowane zgodnie ze standardem:
   - Formuły wewnątrz wiersza: `$x^2 + y^2 = z^2$` (bez spacji bezpośrednio po otwierającym i przed zamykającym znakiem `$`).
   - Równania blokowe (wyeksponowane):
     ```markdown
     $$
     \int_{a}^{b} f(x) \, dx = F(b) - F(a)
     $$
     ```
   - Standardowe makra LaTeX (np. `\frac{a}{b}`, `\sqrt{x}`, `\sum`, `\int`, `\operatorname{tg}`) są w pełni wspierane.

3. **Uruchomienie konwersji**:
   Wywołaj skrypt `scripts/convert.py` dołączony do tego skilla:
   ```bash
   /Users/pawel/git/gen-ai-orchestrator/.agents/skills/markdown-latex-to-gdoc/scripts/convert.py "<SCIEZKA_DO_PLIKU_MD>"
   ```
   
   Opcjonalne flagi:
   - `-o <SCIEZKA_WYJSCIOWA.docx>` – określenie własnej ścieżki wyjściowej.
   - `--gdrive` – automatyczne skopiowanie wygenerowanego pliku do lokalnego katalogu synchronizacji Dysku Google (`~/Library/CloudStorage/GoogleDrive-.../Mój dysk`).
   - `--gdrive-folder "Podkatalog"` – zapisanie w konkretnym podfolderze na Dysku Google.

4. **Weryfikacja jakościowa**:
   Skrypt automatycznie zlicza liczbę równań inline (`<m:oMath>`) i blokowych (`<m:oMathPara>`) w wynikowym pliku XML dokumentu. Upewnij się, że liczba ta odpowiada oczekiwaniom.

5. **Raport dla użytkownika**:
   Poinformuj użytkownika o wygenerowaniu pliku, podaj klikalny link `file://...` oraz instrukcję otwarcia w Google Docs (np. "Wystarczy otworzyć plik .docx w Dokumentach Google – równania zostaną automatycznie zaimportowane jako edytowalne formuły").

---

## Skrypty pomocnicze (Utility Scripts)

Główny skrypt konwersji:
`scripts/convert.py`

### Przykłady wywołania:
```bash
# Standardowa konwersja do tego samego folderu:
./scripts/convert.py raport.md

# Konwersja z określeniem nazwy docelowej:
./scripts/convert.py raport.md -o ~/Dokumenty/RaportMatematyczny.docx

# Konwersja z natychmiastowym wysłaniem na Dysk Google:
./scripts/convert.py raport.md --gdrive
```

---

## Common Mistakes (Częste błędy i jak ich unikać)

- **Błąd 1: Używanie `python-docx` ze zwykłym tekstem:**
  Biblioteki takie jak `python-docx` wstawiają surowy ciąg znaków `$x^2$`, co nie tworzy struktur matematycznych w dokumencie. Należy bezwzględnie używać `pandoc` lub dedykowanego parsera OMML.
- **Błąd 2: Spacje wewnątrz znaczników dolara:**
  Zapis `$ x + y $` może być potraktowany przez pandoc jako zwykły tekst ze znakami waluty. Zawsze formatuj formuły bez wewnętrznych spacji: `$x + y$`.
- **Błąd 3: Złożone niestandardowe pakiety LaTeX:**
  Pandoc obsługuje rdzeń AMS-LaTeX (`amsmath`, `amssymb`), jednak specyficzne pakiety układu stron (np. `geometry`, `tikz`) nie są przekładane na obiekty Worda/Google Docs. Dla diagramów należy stosować obrazy SVG/PNG.
