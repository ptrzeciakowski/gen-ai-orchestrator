#!/bin/bash
# Skrypt inicjujący integrację systemu OpenSpec z interfejsem Google Antigravity (AGY)

PLUGIN_DIR="$HOME/.gemini/config/plugins/openspec"
PLUGIN_SKILLS_DIR="$PLUGIN_DIR/skills"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
REPO_SKILLS_DIR="$REPO_ROOT/.agents/skills"

echo "Instalowanie wtyczki OpenSpec dla AGY..."

# Tworzenie struktury katalogów wtyczki globalnej
mkdir -p "$PLUGIN_DIR"
mkdir -p "$PLUGIN_SKILLS_DIR/opsx-explore"
mkdir -p "$PLUGIN_SKILLS_DIR/opsx-design"
mkdir -p "$PLUGIN_SKILLS_DIR/opsx-tasks"
mkdir -p "$PLUGIN_SKILLS_DIR/opsx-implement"
mkdir -p "$PLUGIN_SKILLS_DIR/opsx-archive"

# Jeśli jesteśmy w repozytorium git z katalogiem .agents/skills, twórzmy również lokalnie
if [ -n "$REPO_ROOT" ] && [ -d "$REPO_ROOT/.agents" ]; then
  echo "Wykryto lokalne repozytorium AGY ($REPO_ROOT). Instalacja w .agents/skills..."
  mkdir -p "$REPO_SKILLS_DIR/opsx-explore"
  mkdir -p "$REPO_SKILLS_DIR/opsx-design"
  mkdir -p "$REPO_SKILLS_DIR/opsx-tasks"
  mkdir -p "$REPO_SKILLS_DIR/opsx-implement"
  mkdir -p "$REPO_SKILLS_DIR/opsx-archive"
fi

# Plik plugin.json (podstawowe metadane)
cat << 'EOF' > "$PLUGIN_DIR/plugin.json"
{
  "name": "openspec-agy-integration",
  "version": "1.0.2",
  "description": "Dodaje skille OpenSpec do interfejsu AGY"
}
EOF

# Treści poszczególnych skilli
EXPLORE_CONTENT='---
name: opsx-explore
description: Rozpocznij proces eksploracji OpenSpec dla nowego pomysłu. Aktywuj ten skill, gdy użytkownik wpisze opsx-explore, /opsx-explore, eksploracja openspec lub poprosi o analize nowego pomyslu.
---
Twoim zadaniem jako Agenta jest natychmiastowe załadowanie lokalnego pliku `.ai/tools/opsx-explore.json` z obecnego repozytorium i wykonanie ukrytej w nim instrukcji. Zastosuj się do niej przy obecnym zadaniu.'

DESIGN_CONTENT='---
name: opsx-design
description: Przygotuj dokument designu OpenSpec (design.md) na bazie eksploracji. Aktywuj ten skill, gdy użytkownik wpisze opsx-design, /opsx-design lub poprosi o wygenerowanie architektury technicznej.
---
Załaduj plik `.ai/tools/opsx-design.json` z bieżącego repozytorium i wygeneruj odpowiedni dokument bazując na instrukcjach.'

TASKS_CONTENT='---
name: opsx-tasks
description: Rozbij design na listę zadań (tasks.md) w OpenSpec. Aktywuj ten skill, gdy użytkownik wpisze opsx-tasks, /opsx-tasks lub poprosi o plan wdrożeniowy / dekompozycję zadań.
---
Przeczytaj plik `.ai/tools/opsx-tasks.json` i stwórz listę dekompozycji w oparciu o jego zasady.'

IMPLEMENT_CONTENT='---
name: opsx-implement
description: Uruchom implementację kolejnego zadania z pliku tasks.md w OpenSpec. Aktywuj ten skill, gdy użytkownik wpisze opsx-implement, /opsx-implement lub poprosi o realizację zadań OpenSpec.
---
Sprawdź, które zadanie w `tasks.md` nie jest jeszcze odhaczone i przystąp do modyfikacji kodu zgodnie z planem.'

ARCHIVE_CONTENT='---
name: opsx-archive
description: Zarchiwizuj obecną zmianę w OpenSpec (uruchamia też auto-estymację). Aktywuj ten skill, gdy użytkownik wpisze opsx-archive, /opsx-archive lub poprosi o zarchiwizowanie/zamknięcie zmiany.
---
Przeczytaj plik `.ai/tools/opsx-archive.json`. Odpal subagentów wyceniających, przygotuj `summary.md` i domknij zmianę poleceniem `openspec archive`.'

# Zapis do wtyczki globalnej
echo "$EXPLORE_CONTENT" > "$PLUGIN_SKILLS_DIR/opsx-explore/SKILL.md"
echo "$DESIGN_CONTENT" > "$PLUGIN_SKILLS_DIR/opsx-design/SKILL.md"
echo "$TASKS_CONTENT" > "$PLUGIN_SKILLS_DIR/opsx-tasks/SKILL.md"
echo "$IMPLEMENT_CONTENT" > "$PLUGIN_SKILLS_DIR/opsx-implement/SKILL.md"
echo "$ARCHIVE_CONTENT" > "$PLUGIN_SKILLS_DIR/opsx-archive/SKILL.md"

# Zapis do repozytorium (jeśli istnieje .agents/skills)
if [ -n "$REPO_ROOT" ] && [ -d "$REPO_SKILLS_DIR" ]; then
  echo "$EXPLORE_CONTENT" > "$REPO_SKILLS_DIR/opsx-explore/SKILL.md"
  echo "$DESIGN_CONTENT" > "$REPO_SKILLS_DIR/opsx-design/SKILL.md"
  echo "$TASKS_CONTENT" > "$REPO_SKILLS_DIR/opsx-tasks/SKILL.md"
  echo "$IMPLEMENT_CONTENT" > "$REPO_SKILLS_DIR/opsx-implement/SKILL.md"
  echo "$ARCHIVE_CONTENT" > "$REPO_SKILLS_DIR/opsx-archive/SKILL.md"
fi

echo "✅ Zainstalowano z sukcesem w: $PLUGIN_DIR"
if [ -n "$REPO_SKILLS_DIR" ] && [ -d "$REPO_SKILLS_DIR" ]; then
  echo "✅ Zainstalowano także w repozytorium: $REPO_SKILLS_DIR"
fi
echo ""
echo "ℹ️  UWAGA DOTYCZĄCA UŻYCIA SKILLI W ANTIGRAVITY:"
echo "   - W Antigravity symbol '@' służy do załączania plików (np. @openspec-agy-init.sh)."
echo "   - Aby uruchomić skill, po prostu wpisz w czacie polecenie dla Agenta, np.:"
echo "     • 'opsx-explore dla nowego modułu'"
echo "     • '/opsx-design'"
echo "     • 'Uruchom opsx-tasks'"
echo "     • 'Zrealizuj zadanie z opsx-implement'"
echo "     • 'opsx-archive'"

