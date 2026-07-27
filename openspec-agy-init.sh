#!/bin/bash
# Skrypt inicjujący integrację systemu OpenSpec z interfejsem Google Antigravity (AGY)

PLUGIN_DIR="$HOME/.gemini/config/plugins/openspec"
PLUGIN_SKILLS_DIR="$PLUGIN_DIR/skills"
REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
SRC_SKILLS_DIR="$REPO_ROOT/.ai/skills"

echo "Instalowanie wtyczki OpenSpec dla AGY..."

# Tworzenie struktury katalogów wtyczki globalnej
mkdir -p "$PLUGIN_DIR"
mkdir -p "$PLUGIN_SKILLS_DIR"

# Plik plugin.json (podstawowe metadane)
cat << 'EOF' > "$PLUGIN_DIR/plugin.json"
{
  "name": "openspec-agy-integration",
  "version": "1.4.0",
  "description": "Dodaje skille OpenSpec z obsługą Single Source of Truth w SKILL.md, Zasad Brutalnej Szczerości, podfolderu explore/, dwutabelowej estymacji i rejestru zmian"
}
EOF

# Kopiowanie skilli z repozytorium (.ai/skills) jako Single Source of Truth
if [ -d "$SRC_SKILLS_DIR" ]; then
  echo "Kopiowanie skilli z repozytorium ($SRC_SKILLS_DIR) do wtyczki globalnej AGY..."
  cp -r "$SRC_SKILLS_DIR"/* "$PLUGIN_SKILLS_DIR/"
  echo "✅ Synchronizacja zakończona pomyślnie."
else
  echo "⚠️ Ostrzeżenie: Katalog $SRC_SKILLS_DIR nie został odnaleziony."
fi

echo "✅ Zainstalowano z sukcesem w: $PLUGIN_DIR"
