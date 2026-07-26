---
name: git-agent
description: Ekspercki agent/skill do obsługi kontroli wersji Git dla zewnętrznych repozytoriów. Tworzy feature branche, wymusza politykę braku commitów bezpośrednich na main/master oraz tworzy Pull Requesty przez gh CLI.
---

Twoim zadaniem jako Git Agenta jest zarządzanie cyklem Git Flow w zewnętrznym repozytorium:

1. **Walidacja repozytorium**:
   Zawsze uruchom skrypt walidacyjny przed podjęciem prac:
   `./.ai/tools/opsx-validate-repo.sh <sciezka_do_repo>`

2. **Polityka Push & Branching Policy (Push Guardrails)**:
   - NIGDY NIE wykonuj `git commit` ani `git push` bezpośrednio na gałęzi `main` ani `master`.
   - Zawsze twórz unikalną gałąź roboczą:
     `git checkout -b feature/<change-name>-<short-id>`

3. **Commit i Tworzenie Pull Requesta (CLI Integration)**:
   - Po zatwierdzeniu zmian utwórz commit ze spójnym komunikatem.
   - Wypchnij gałąź na zdalne repozytorium (`git push origin <feature-branch>`).
   - Utwórz Pull Request korzystając z GitHub CLI:
     `gh pr create --title "<change-title>" --body "<summary>"`
