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

3. **Push & Tworzenie Pull Requesta (Automated PR Flow)**:
   - Po zatwierdzeniu zmian commitem wypchnij gałąź na zdalne repozytorium:
     `git push -u origin <feature-branch>`
   - Jeśli narządzie `gh` (GitHub CLI) jest dostępne, utwórz Pull Request automatycznie:
     `gh pr create --title "<change-title>" --body "<summary>"`
   - Jeśli `gh` nie jest zainstalowane, zwróć użytkownikowi bezpośredni link do utworzenia PR podany przez Gita w komunikacie po `git push` (np. `https://github.com/user/repo/pull/new/<feature-branch>`).
