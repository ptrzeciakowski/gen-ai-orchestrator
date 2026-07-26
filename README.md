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
