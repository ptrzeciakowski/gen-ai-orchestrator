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
  "version": "1.3.0",
  "description": "Dodaje skille OpenSpec z obsługą Zasad Brutalnej Szczerości, Akumulacyjnego Wzbogacania Artefaktów, dwutabelowego summary.md, datowania HHMM oraz rejestru changes-summary.md do interfejsu AGY"
}
EOF

# Treści poszczególnych skilli
EXPLORE_CONTENT='---
name: opsx-explore
description: Rozpocznij proces eksploracji OpenSpec dla nowego pomysłu. Aktywuj ten skill, gdy użytkownik wpisze opsx-explore, /opsx-explore, eksploracja openspec lub poprosi o analize nowego pomyslu.
---
Twoim zadaniem jako Agenta jest załadowanie lokalnego pliku `.ai/tools/opsx-explore.json` oraz wytycznych `.ai/guidelines/brutally-honest-rules.md` z bieżącego repozytorium. Twórz eksplorację przestrzegając Zasad Brutalnej Szczerości i Akumulacyjnego Wzbogacania (nazywanie niepewności wprost, oznaczanie domysłów jako [Hipoteza/Domysł], zakaz zmyślania metryk i źródeł).'

DESIGN_CONTENT='---
name: opsx-design
description: Przygotuj dokument designu OpenSpec (design.md) na bazie eksploracji. Aktywuj ten skill, gdy użytkownik wpisze opsx-design, /opsx-design lub poprosi o wygenerowanie architektury technicznej.
---
Załaduj plik `.ai/tools/opsx-design.json` oraz wytyczne `.ai/guidelines/brutally-honest-rules.md`. Podczas wygenerowania dokumentu architektonicznego bezwzględnie punktuj słabości, prezentuj alternatywne opcje, wzbogacaj artefakty akumulacyjnie i unikaj sztucznej pewności siebie.'

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
Przeczytaj plik `.ai/tools/opsx-archive.json`. Wygeneruj dwutabelowe `summary.md` (wyceny estymatorów + metryki sesji wall-clock/tokeny), zarchiwizuj zmianę pod nazwą w formacie YYYY-MM-DD-HHMM-<change-id>, a na końcu zaktualizuj plik zbiorczy `openspec/changes/archive/changes-summary.md`.'

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
