#!/bin/bash
# Tool: openspec-update-readme
# Opis: Skrypt (tool) do aktualizacji README.md (wymagania od użytkownika) wymuszany przy modyfikacji openspec-gen-ai-orchestrator.

if [ "$#" -lt 1 ]; then
    echo "Użycie: ./update_readme.sh \"<surowe_wymaganie>\""
    exit 1
fi

REQUIREMENT="$1"
CURRENT_DATE=$(date +"%Y-%m-%d %H:%M")
README_PATH="$(git rev-parse --show-toplevel)/README.md"

if [ ! -f "$README_PATH" ]; then
    echo "Nie znaleziono pliku README.md w głównym katalogu."
    exit 1
fi

echo "" >> "$README_PATH"
echo "### $CURRENT_DATE" >> "$README_PATH"

# Jeśli wymaganie zawiera wiele linii, dodajemy znak cytatu `> ` do każdej linii.
echo "$REQUIREMENT" | while IFS= read -r line; do
    echo "> $line" >> "$README_PATH"
done

echo "Aktualizacja README.md zakończona pomyślnie."
