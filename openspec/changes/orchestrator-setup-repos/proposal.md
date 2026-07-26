# Proposal: orchestrator-setup-repos

## Why
Obecnie `gen-ai-orchestrator` zarządza własną strukturą i infrastrukturą narzędziową (`.ai/`). Prawdziwa moc warstwy orkiestracji ujawnia się jednak, gdy zaczyna ona obsługiwać i wprowadzać zmiany w zewnętrznych projektach (innych repozytoriach). Potrzebujemy ustandaryzowanego, bezpiecznego środowiska, które pozwoli agentom lokalizować te projekty oraz aplikować w nich zmiany z zachowaniem najwyższych standardów higieny kodu (Git flow).

## What Changes
1. **Zarządzanie Repozytoriami (Symlinki)**: Wprowadzenie dedykowanego obszaru (np. katalogu `.ai/repositories/` oraz kompatybilnego symlinku `.repositories/`), w którym znajdować się będą lokalne dowiązania (symlinki) do innych, klonowanych lokalnie repozytoriów. Dzięki temu agent zawsze będzie miał dostęp do nich wprost z poziomu swojego bazowego folderu.
2. **Polityka Zmian (Feature Branches & PR)**: Restrykcyjne ustalenie zasad, w których agenci pracujący w tych zlinkowanych repozytoriach nie mają prawa commitować bezpośrednio do gałęzi głównej (`main`/`master`). Każda operacja musi opierać się na cyklu: `git checkout -b <feature-branch>` -> modyfikacje -> `git commit` -> utworzenie Pull Requesta.
3. **Wdrożenie `git-agent`**: Dodanie wyspecjalizowanego Agenta lub Skilla (`git-agent`), który będzie pełnił rolę eksperta od obsługi VCS. To na niego będzie spadać odpowiedzialność za poprawne żonglowanie repozytoriami, weryfikowanie statusów git, tworzenie zrzutów oraz docelowo – wywoływanie CLI (np. `gh pr create` lub podobnych rozwiązań terminalowych) w celu podpinania Pull Requestów.

## Decyzja Architektoniczna
Zgodnie z weryfikacją w `001-orchestrator-setup-repos-001.md`, podjęto celową decyzję o wyborze **Opcji C** – twardego użycia symlinków dla zewnętrznych repozytoriów, akceptując świadomie ryzyka związane z kolizją edycji, indeksowania oraz wychodzeniem poza sandboxing. Podejście to oferuje największą prostotę początkowej konfiguracji.
