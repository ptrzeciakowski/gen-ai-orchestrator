## Surowe wymagania od Użytkownika

### 2026-07-26 18:00
> - ma mieć strukturę a agentami jaką utworzyliśmy razem dzisiaj w repozytorium: /Users/pawel/git/obsydian
> - ma być gen ai tool agnostic, umożliwiając uruchamianie z terminala
> - ma być repozytorium z kompletem skill-i, agentów i tool-i używanymi przeze mnie
> - ma być przestrzenią roboczą gdzie operacje do odczytu systemu plików czy mojego gDrive (/Users/pawel/Library/CloudStorage/GoogleDrive-ptrzeciakowski@gmail.com/Mój dysk) są wykonywane bez pytania, operacje uruchomienia i zapisu czy usuwania w ramach wyznaczonego folderu (przestrzeń robocza) są uruchamiane bez pytania, żeby można było zdefiniować cel i agent mógł nieprzerwanie działać
> - ma być realizowane zgodnie ze standardem Open Spec (https://openspec.dev/) - wszystkie zmiany mają być tak realizowane w takim trybie
> - wszystkie explory mają pozostawiać po sobie ślad (w postaci pliku markdown o pewnej konwencji, np. 001-explore-name-001.md)
> - wszystkie założenia do tego repozytorium (w tym te wymagania w postaci surowej - na końcu) muszą być dodawane i aktualizowane w pliku @[README.md]

### 2026-07-26 18:18
> Kontekst wykonanych prac, do których odnoszą się uwagi:
> 1. Struktura Agentów: Utworzono katalog `.agents` z podkatalogami.
> 2. Standard Open Spec: Utworzono strukturę katalogów `openspec/specs` oraz `openspec/changes`.
> 3. Ślady Eksploracji: Stworzono katalog `explorations` ze śladem z sesji konfiguracyjnej.
> 4. Zaktualizowane założenia: Zaktualizowano README opierając się na zgłoszeniach.
> 
> Odpowiedź Użytkownika:
> Ad 1. Zróbmy strukturę agnostyczną, tj. katalog .ai w którym będą właściwe skille, agenty i toole. Pod agy zróbmy .agents/skills, .agents/agents, .agents/tools będący symlinkami do odpowiednich folderów w podkatalogu .ai. Dodaj tam szablony dla każdego z typów artefaktów z repozytorium obsydian.
> 
> Pamiętaj o zaktualizowaniu @[README.md]. Struktura pliku
> - # gen-ai-orchestrator i podrozdziały to klasyczne readme
> - ## Założenia repozytorium - to założenia repozytrium będące jedną spójną wersją
> - ## Surowe wymagania od Użytkownika - historia wymagań ode mnie z podrozdziałami
> - ### 2026-07-26 18:00 i kolejne.
> 
> Ad 2 i 3. Spoko. Explorations powinien być pierwszą zmianą w podkatalogu openspec/changes/explore-orchestrator-setup
> Ad 4. OK.

### 2026-07-26 18:27
> Niech to będzie pierwsza komenda (tool) - aktualizacja readme w ten sposób wymuszana każdorazowo przy modyfikacji openspec-gen-ai-orchestrator. Przeniosłem do tego katalogu zmianę 001-explore-orchestrator-setup-001.md
> 
> Popraw jeszcze .agents, bo w tej chwili to nie są symlinki do .ai a powinny być, żeby w jednym miejscu definiować zmianę.

### 2026-07-26 18:46
> Chciałbym móc krótko wywoływać komendy openSpec tak jak /opsx-design - jak to mogę dodać, żeby było agnostyczne? Dodaś w .ai/tools opsx-design.json z odpowiednim opisem?

### 2026-07-26 18:53
> Dobrze, dodaj w takim razie pozostałe komendy open spec, czyli opsx-explore (do explore dodaj konwencję o której pisałem wcześniej 001-change-name-001.md, opsx-archive, komendę implementującą design. Chciałbym też mieć zapewnione tworzenie i aktualizację pliku .session gdzie będą zapisywany identyfikatory sesji z agy, po to żeby potem można było łatwo sięgać do starych sesji po podsumowanie (wall clock, i inne statystki sesji (liczba tokenów, liczba interakcji, etc.) w ramach których realizowana była zmiana).

### 2026-07-26 18:56
> plik .session powinien się nazywać .sessions i być w katalogu zmiany, np. plik @[.session] powinien leżeć tu openspec/changes/archive/explore-ochestrator-setup/

### 2026-07-26 18:58
> W pliku @[openspec/changes/explore-orchestrator-setup/.sessions] powinny być tylko id sesji i info o tym jaki tool zostały użyty (w tym przypadku AGY)

### 2026-07-26 19:06
> Dobrze. Dodaj proszę jeszcze tool szacujący czas w roboczo godzinach i przeliczający to na roboczo-dni który szacuje reazlizację zmiany opisanej w proposa i potem design. Tool ma wywoływać 5 niezależnych sub-agentów, którzy takie szacowanie przygotują. Potem ma być w podsumowaniu to pokazane. Tool miałby być wywoływany w momencie archiwizacji zmiany gdzie miałby powstawać plik summary.md.
