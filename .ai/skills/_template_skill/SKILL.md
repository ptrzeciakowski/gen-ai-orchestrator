---
name: template-skill
description: >-
  Krótki opis (do 1024 znaków) mówiący o tym, co robi ten skill i kiedy agent powinien go użyć. Zawsze używaj małych liter i myślników w 'name'.
---

# Template Skill

## Overview (Przegląd)
Zwięzły opis celu istnienia tego skilla oraz problemu, który rozwiązuje w ramach repozytorium.

## Dependencies (Zależności)
- Wylistuj tutaj ewentualne inne skille, narzędzia lub biblioteki wymagane do działania tego skilla.

## Quick Start (Szybki start)
Przykłady promptów wyzwalających ten skill:
- "Użyj skilla template-skill, aby zaktualizować indeks notatek."
- "Znajdź powiązania używając template-skill."

## Workflow (Zasady działania)
Jeśli skill polega na instrukcjach dla agenta (bez kodu), opisz je w krokach:
1. **Analiza:** Najpierw przeczytaj plik X.
2. **Przetwarzanie:** Zwróć uwagę na tagi Y.
3. **Wynik:** Sformatuj odpowiedź w postaci tabeli.

## Utility Scripts (Skrypty pomocnicze - jeśli dotyczy)
Jeśli skill korzysta ze skryptów (np. `scripts/run.sh`), opisz jak je wywołać i z jakimi parametrami. Zawsze każ agentowi pisać wyniki skryptów do pliku zamiast wyrzucać potężne dane na standardowe wyjście (stdout).

## Common Mistakes (Częste błędy)
- **Błąd 1:** Wyjaśnij, co agenty najczęściej psują używając tego skilla i jak tego uniknąć (np. omijanie autoryzacji).
