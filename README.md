# gen-ai-orchestrator

Repository containing gen-ai-orchestration layer with skills, agents, toolset and integration with OpenSpec standard.

## Założenia repozytorium

- **Struktura Agnostyczna**: Projekt posiada generyczną architekturę konfiguracji AI zorganizowaną w katalogu `.ai/` (zawierającym podkatalogi `agents/`, `skills/`, `tools/`). Dodatkowo w `.agents/` utworzono symlinki zgodne z systemem `agy`.
- **Gen AI Tool Agnostic**: Architektura pozwala na niezależność od konkretnych frameworków AI i na uruchamianie skryptów/logiki bezpośrednio z terminala.
- **Kompletność**: Jest to repozytorium z kompletem używanych przez Ciebie skilli, agentów i narzędzi. Do repozytorium dołączone są szablony definicji artefaktów skopiowane z projektu referencyjnego.
- **Przestrzeń robocza i uprawnienia**: 
  - Operacje do odczytu systemu plików oraz z Twojego katalogu Google Drive (`/Users/pawel/Library/CloudStorage/GoogleDrive-ptrzeciakowski@gmail.com/Mój dysk`) mają być wykonywane przez agentów bez pytania.
  - Operacje uruchomienia, zapisu, czy usuwania w ramach tego wyznaczonego folderu (przestrzeń robocza) są uruchamiane bez pytania. Celem jest umożliwienie zdefiniowania agentowi zadania do nieprzerwanego działania.
- **Zgodność z Open Spec**: Wszystkie zmiany w tym repozytorium są realizowane zgodnie ze standardem [Open Spec](https://openspec.dev/). Proces obejmuje korzystanie ze specyfikacji (`openspec/specs/`) i definiowanie propozycji zmian w dedykowanym katalogu (`openspec/changes/`).
- **Ślady exploracji (Explores)**: Każda eksploracja pozostawia po sobie ślad w postaci pliku markdown o zadanej konwencji nazewnictwa (np. `001-explore-name-001.md`), z pierwszą eksploracją zapisaną w `openspec/changes/explore-orchestrator-setup/`.

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
