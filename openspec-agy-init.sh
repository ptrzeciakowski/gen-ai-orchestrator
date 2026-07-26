#!/bin/bash
# Skrypt inicjujący integrację systemu OpenSpec z interfejsem Google Antigravity (AGY)

PLUGIN_DIR="$HOME/.gemini/config/plugins/openspec"
SKILLS_DIR="$PLUGIN_DIR/skills"

echo "Instalowanie wtyczki OpenSpec dla AGY..."

# Tworzenie struktury katalogów
mkdir -p "$PLUGIN_DIR"
mkdir -p "$SKILLS_DIR/opsx-explore"
mkdir -p "$SKILLS_DIR/opsx-design"
mkdir -p "$SKILLS_DIR/opsx-tasks"
mkdir -p "$SKILLS_DIR/opsx-implement"
mkdir -p "$SKILLS_DIR/opsx-archive"

# Plik plugin.json (podstawowe metadane)
cat << 'EOF' > "$PLUGIN_DIR/plugin.json"
{
  "name": "openspec-agy-integration",
  "version": "1.0.1",
  "description": "Dodaje skille OpenSpec do interfejsu AGY"
}
EOF

# Definicje poszczególnych skilli
cat << 'EOF' > "$SKILLS_DIR/opsx-explore/SKILL.md"
---
name: opsx-explore
description: Rozpocznij proces eksploracji OpenSpec dla nowego pomysłu
---
Twoim zadaniem jako Agenta jest natychmiastowe załadowanie lokalnego pliku `.ai/tools/opsx-explore.json` z obecnego repozytorium i wykonanie ukrytej w nim instrukcji. Zastosuj się do niej przy obecnym zadaniu.
EOF

cat << 'EOF' > "$SKILLS_DIR/opsx-design/SKILL.md"
---
name: opsx-design
description: Przygotuj dokument designu OpenSpec (design.md) na bazie eksploracji
---
Załaduj plik `.ai/tools/opsx-design.json` z bieżącego repozytorium i wygeneruj odpowiedni dokument bazując na instrukcjach.
EOF

cat << 'EOF' > "$SKILLS_DIR/opsx-tasks/SKILL.md"
---
name: opsx-tasks
description: Rozbij design na listę zadań (tasks.md)
---
Przeczytaj plik `.ai/tools/opsx-tasks.json` i stwórz listę dekompozycji w oparciu o jego zasady.
EOF

cat << 'EOF' > "$SKILLS_DIR/opsx-implement/SKILL.md"
---
name: opsx-implement
description: Uruchom implementację kolejnego zadania z pliku tasks.md
---
Sprawdź, które zadanie w `tasks.md` nie jest jeszcze odhaczone i przystąp do modyfikacji kodu zgodnie z planem.
EOF

cat << 'EOF' > "$SKILLS_DIR/opsx-archive/SKILL.md"
---
name: opsx-archive
description: Zarchiwizuj obecną zmianę (uruchamia też auto-estymację)
---
Przeczytaj plik `.ai/tools/opsx-archive.json`. Odpal subagentów wyceniających, przygotuj `summary.md` i domknij zmianę poleceniem `openspec archive`.
EOF

echo "✅ Zainstalowano z sukcesem w: $PLUGIN_DIR"
echo "♻️ Zrestartuj aplikację AGY. Twoje komendy będą teraz dostępne jako skille, poprzez wpisanie np. @opsx-explore, @opsx-design."
