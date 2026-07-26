#!/bin/bash
# Skrypt inicjujący integrację systemu OpenSpec z interfejsem Google Antigravity (AGY)

PLUGIN_DIR="$HOME/.gemini/config/plugins/openspec"
mkdir -p "$PLUGIN_DIR"

echo "Instalowanie wtyczki OpenSpec dla AGY..."

cat << 'EOF' > "$PLUGIN_DIR/plugin.json"
{
  "name": "openspec-agy-integration",
  "version": "1.0.0",
  "description": "Dodaje komendy OpenSpec do interfejsu slash commands w AGY",
  "slash_commands": [
    {
      "name": "opsx-explore",
      "description": "Rozpocznij proces eksploracji OpenSpec dla nowego pomysłu",
      "prompt": "Uruchomiono slash komendę /opsx-explore. Twoim zadaniem jako Agenta jest natychmiastowe załadowanie lokalnego pliku .ai/tools/opsx-explore.json z obecnego repozytorium i wykonanie ukrytej w nim instrukcji."
    },
    {
      "name": "opsx-design",
      "description": "Przygotuj dokument designu OpenSpec (design.md) na bazie eksploracji",
      "prompt": "Uruchomiono slash komendę /opsx-design. Załaduj plik .ai/tools/opsx-design.json z bieżącego repozytorium i wygeneruj odpowiedni dokument bazując na instrukcjach."
    },
    {
      "name": "opsx-tasks",
      "description": "Rozbij design na listę zadań (tasks.md)",
      "prompt": "Uruchomiono slash komendę /opsx-tasks. Przeczytaj plik .ai/tools/opsx-tasks.json i stwórz listę dekompozycji w oparciu o jego zasady."
    },
    {
      "name": "opsx-implement",
      "description": "Uruchom implementację kolejnego zadania z pliku tasks.md",
      "prompt": "Uruchomiono slash komendę /opsx-implement. Sprawdź, które zadanie w tasks.md nie jest jeszcze odhaczone i przystąp do modyfikacji kodu zgodnie z planem."
    },
    {
      "name": "opsx-archive",
      "description": "Zarchiwizuj obecną zmianę (uruchamia też auto-estymację)",
      "prompt": "Uruchomiono slash komendę /opsx-archive. Przeczytaj .ai/tools/opsx-archive.json. Odpal subagentów wyceniających, zrób summary.md i domknij zmianę poleceniem openspec archive."
    }
  ]
}
EOF

echo "✅ Zainstalowano z sukcesem w: $PLUGIN_DIR"
echo "♻️ Zrestartuj terminal i wywołaj komendę 'agy', aby ukośnikowe komendy zaczęły być widoczne."
