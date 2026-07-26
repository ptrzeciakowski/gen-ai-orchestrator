# Eksploracja: orchestrator-setup-repos
*Status: Krytyczna analiza założeń z proposal.md*

W ramach fazy badawczej przyjrzeliśmy się idei dodania wsparcia dla zewnętrznych repozytoriów w warstwie orkiestracji poprzez mechanizm symlinków lokalnych (tworzonych w `.ai/repositories` bądź podobnych lokalizacjach) oraz obsługi feature branchy przez dedykowanego "git-agenta". Rozwiązanie to na papierze wygląda tanio i prosto, niemniej niesie za sobą krytyczne ryzyka w kontekście autonomicznych agentów.

## 🔴 Krytyka Propozycji z Proposal.md

### 1. Pętla symlinków i złamanie piaskownicy (Sandboxing)
Oparcie się na symlinkach do lokalnych folderów deweloperskich (np. `~/git/inne-repo`) sprawia, że orkiestrator otrzymuje swobodny, niefiltrowany dostęp do żywych środowisk pracy programisty. Agent błądzący w ścieżkach lub dokonujący nieostrożnych zrzutów po plikach może zniszczyć pracę lokalną użytkownika. Jeśli symlink wskazuje repo z innymi symlinkami, parsery agentowe mogą ugrzęznąć w pętlach odczytu.
**Wniosek:** Środowisko pracy AI musi ulegać mocniejszej izolacji niż tylko poleganie na dyscyplinie językowej modelu (LLM) podczas modyfikacji plików.

### 2. Ślepe zaułki i locki na repozytoriach (Git index.lock)
Kiedy proces agentowy działa asynchronicznie, operowanie w lokalnym katalogu `inne-repo` podczas gdy sam użytkownik również wykonuje tam zmiany (lub ma otwarte IDE) skończy się wybuchem blokad indeksu Gita (`index.lock`). Autonomiczny agent próbujący dokonać zmiany `git checkout -b` czy skasować branch nie poradzi sobie z rozgrzebanymi plikami z tzw. "brudnego working tree". To doprowadzi do zawieszenia zadania i wypluwania kaskadowych błędów, niszcząc koncepcję "działania nieprzerwanego".

### 3. Trudności w zarządzaniu kluczami uwierzytelniającymi (Push / PR)
Powołanie `git-agenta` ma sens merytorycznie, lecz pojawia się problem delegacji uprawnień. By w ogóle wrzucać zmiany (push) i kreować Pull Requesty, agent musi mieć zdefiniowany tunel SSH / HTTPS bądź poświadczenia z `gh cli` autoryzowane dla danych repozytoriów, które nie zawsze będą ustandaryzowane w lokalnych powiązaniach symlinków.

---

## 🟢 Opcje do decyzji

### Opcja A: Ulotne kopie tymczasowe (Ephemeral Workspaces / Clones)
Zamiast symlinków łączących się bezpośrednio z pracą dewelopera, orkiestrator na zadanie "wprowadź zmianę w Repozytorium X" **klonuje czystą kopię repozytorium do katalogu `/tmp/orchestrator-runs/<id>`**.
* **Zalety:** Agent działa w 100% zdezolowanym, brudnopisie. Nie ma prawa uderzyć w Twoje aktywne pliki, psuć twojego indexu gita ani pętli dyskowych. Gdy skończy pisać kod, robi commit, pushuje nowy feature branch na remote, klika PR (przez `gh pr create`) i usuwa tymczasową przestrzeń. Całość środowiskowa jest nietknięta.
* **Wady:** Wymaga konfiguracji z kluczem autoryzacyjnym, nie pozwala deweloperowi "podglądać na żywo" prac agenta we własnym środowisku (chyba że zrobi pull). Wolniejsze ze względu na pobieranie (clone) całych repo.

### Opcja B: Symlinki, ale tylko w trybie ścisłego odizolowanego "Git Worktree"
Rozwiązanie pośrednie. Zamiast symlinkować całe Twoje żywe repo, orkiestrator powołuje do życia tzw. `git worktree` wskazanego repozytorium w chronionym katalogu `.ai/repositories/<nazwa>`.
* **Zalety:** Nie klonujemy kodu na nowo (operujemy na tej samej dyskowej pamięci gitowej co u Ciebie). Zmiany nie psują Twojego `working tree` (siedzisz na `main`, agent na oddzielnym branchu w innym folderze fizycznym `worktree`). Podglądasz zmiany natychmiast u siebie.
* **Wady:** Nadal naraża to repozytorium na ewentualne przypadkowe globalne zniszczenia gita (np. reset gałęzi). Trzeba oprogramować w `git-agent` komendy dodawania i czyszczenia `git worktree`.

### Opcja C: Wariant klasyczny zgodnie z Proposal (Local Symlinks + `git-agent`)
Pozostajemy przy prostej strukturze zaproponowanej w `proposal.md`.
* **Zalety:** Najłatwiejsze we wdrożeniu – po prostu linkujesz i masz dostępne z poziomu kodu bez używania klonowań.
* **Wady:** Wszystkie ryzyka opisane w punkcie 1, 2 i 3.

---

## 🔥 Decyzja
W którą stronę kierujemy architekturę dla modułu integracji projektowej? Czy wdrażamy Opcję A (bezpieczne jednorazówki klonujące kod z GitHuba), czy Opcję B (natywne Git Worktrees z szybkością ale lekkim ryzykiem), czy jednak twardo Opcja C (prosty symlink)? Zależą od tego narzędzia i wytyczne jakimi nakarmimy docelowego `git-agenta`.
