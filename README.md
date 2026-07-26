# gen-ai-orchestrator

Repository containing gen-ai-orchestration layer with skills, agents, toolset and integration with OpenSpec standard.

## 🗺️ Struktura Katalogów i Architektura

```
gen-ai-orchestrator/
├── .ai/                       # Główna agnostyczna struktura konfiguracji AI
│   ├── agents/                # Definicje i instrukcje agentów
│   ├── guidelines/            # Kanoniczne zasady i wytyczne (np. brutally-honest-rules.md)
│   ├── repositories/          # Rejestr powiązanych repozytorium zewnętrznych
│   ├── skills/                # Skille i umiejętności agentów
│   └── tools/                 # Narzędzia, komendy i skrypty automatyzacji (.json / .sh)
├── .agents/                   # Dowiązania symboliczne (symlinks) do .ai/ dla zgodności z AGY CLI
│   ├── agents -> ../.ai/agents
│   ├── skills -> ../.ai/skills
│   └── tools  -> ../.ai/tools
├── .repositories/             # Symlink wskazujący na .ai/repositories
├── openspec/                  # Przestrzeń robocza i specyfikacje OpenSpec
│   ├── config.yaml            # Główna konfiguracja projektu OpenSpec (workflow schemas, rules)
│   ├── specs/                 # Stan docelowy i kanoniczne specyfikacje modułów
│   └── changes/               # Zmiany w trakcie realizacji oraz ich archiwum
│       ├── archive/           # Zarchiwizowane i wdrożone zmiany (nazewnictwo YYYY-MM-DD-HHMM-<name>)
│       │   ├── changes-summary.md  # Zbiorczy rejestr metryk, tokenów i kosztów zarchiwizowanych zmian
│       │   ├── 2026-07-26-1914-explore-orchestrator-setup/
│       │   ├── 2026-07-26-2012-orchestrator-setup-repos/
│       │   └── 2026-07-26-2052-orch-constructive-criticizm/
│       └── wyszukiwarka-nieruchomosci/  # Obecnie realizowana zmiana OpenSpec
├── wyszukiwarka-nieruchomosci/ # Dedykowany podkatalog modułu wyszukiwania nieruchomości Warszawa
│   ├── kryteria.md            # Konfiguracja parametrów wyszukiwania
│   ├── historia/              # Wygenerowane raporty YYYY-MM-DD-HH24MISS-oferty.md
│   └── src/                   # Kod źródłowy (providers, rcn_client, report_generator)
├── specs/                     # Dodatkowe specyfikacje i dokumenty pomocnicze
├── README.md                  # Dokumentacja główna repozytorium
└── openspec-agy-init.sh       # Skrypt instalujący i synchronizujący skille wtyczki AGY
```

---

## 📌 Założenia i Zasady Repozytorium

- **Struktura Agnostyczna**: Projekt posiada generyczną architekturę konfiguracji AI zorganizowaną w katalogu `.ai/`. Dla narzędzi takich jak `agy` utworzono symlinki w `.agents/`.
- **Gen AI Tool Agnostic**: Architektura pozwala na niezależność od konkretnych frameworków AI i na uruchamianie skryptów/logiki bezpośrednio z terminala.
- **Konstruktywna Krytyka & Brutalna Szczerość (12 Rules + Rule 13)**:
  - Agenci mają obowiązek bezwzględnie stosować wytyczne z `.ai/guidelines/brutally-honest-rules.md` (nazywanie niepewności wprost, zakaz zmyślania źródeł/statystyk/URL-i, prezentowanie alternatywnych ścieżek).
  - **Rule 13 (Akumulacyjne Wzbogacanie Artefaktów OpenSpec)**: Podczas trwania czatu i dyskusji przed archiwizacją, każde doprecyzowanie, poprawka czy obserwacja z pierwszych testów **MUSI być wplatana akumulacyjnie do artefaktów OpenSpec**, bez destrukcyjnego kasowania czy skracania dotychczasowych wartościowych sekcji.
- **Zgodność z Open Spec**: Wszystkie zmiany są realizowane zgodnie ze standardem [Open Spec](https://openspec.dev/). Proces obejmuje korzystanie ze specyfikacji (`openspec/specs/`) oraz propozycji zmian w dedykowanych katalogach (`openspec/changes/`).
- **Standard Estymacji & Rejestr Metryk (`changes-summary.md`)**: Każda zmiana kończy się generowaniem dwutabelowego podsumowania w `summary.md` (estymacje sub-agentów oraz metryki sesji: czas wall-clock, tokeny input/output, oszczędność czasowa). Zbiorczy rejestr w `openspec/changes/archive/changes-summary.md` gromadzi historyczne metryki wszystkich zarchiwizowanych zmian pod nazwami `YYYY-MM-DD-HHMM-<name>`.
