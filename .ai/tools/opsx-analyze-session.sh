#!/bin/bash
# Tool: opsx-analyze-session
# Opis: Analizuje sesje dla danej zmiany w OpenSpec wyciągając metryki z pliku logów agenta.

CHANGE_NAME=$1
if [ -z "$CHANGE_NAME" ]; then
    echo "Użycie: ./opsx-analyze-session.sh <change_name>"
    exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
SESSION_FILE="$REPO_ROOT/openspec/changes/$CHANGE_NAME/.sessions"
if [ ! -f "$SESSION_FILE" ]; then
    SESSION_FILE="$REPO_ROOT/openspec/changes/archive/$CHANGE_NAME/.sessions"
    if [ ! -f "$SESSION_FILE" ]; then
        echo "Brak pliku .sessions dla zmiany $CHANGE_NAME"
        exit 1
    fi
fi

echo "--- Analiza statystyk dla zmiany: $CHANGE_NAME ---"
while read -r line; do
    # Zakładamy format: <SESSION_ID> <TOOL>
    SESSION_ID=$(echo "$line" | awk '{print $1}')
    TOOL=$(echo "$line" | awk '{print $2}')
    
    echo "Sesja: $SESSION_ID (Tool: $TOOL)"
    if [ "$TOOL" == "AGY" ]; then
        LOG_FILE="$HOME/.gemini/antigravity-cli/brain/$SESSION_ID/.system_generated/logs/transcript.jsonl"
        if [ -f "$LOG_FILE" ]; then
            STEPS=$(cat "$LOG_FILE" | wc -l | tr -d ' ')
            USER_MSGS=$(grep -c '"type":"USER_INPUT"' "$LOG_FILE")
            START_TIME=$(head -n 1 "$LOG_FILE" | grep -o '"Created At":"[^"]*"' | cut -d'"' -f4)
            END_TIME=$(tail -n 1 "$LOG_FILE" | grep -o '"Created At":"[^"]*"' | cut -d'"' -f4)
            
            echo "  - Czas startu: $START_TIME"
            echo "  - Czas końca:  $END_TIME"
            echo "  - Całkowita liczba kroków (steps): $STEPS"
            echo "  - Liczba interakcji z Użytkownikiem: $USER_MSGS"
        else
            echo "  - Brak lokalnego pliku logów w systemie ($LOG_FILE)."
        fi
    else
        echo "  - Brak natywnej integracji analizy statystyk dla toola: $TOOL"
    fi
    echo ""
done < "$SESSION_FILE"
