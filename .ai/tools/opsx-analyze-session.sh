#!/bin/bash
# Tool: opsx-analyze-session
# Opis: Analizuje sesje dla danej zmiany w OpenSpec wyciągając metryki z pliku logów agenta (Wall-clock, Input/Output Tokens).

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

echo "--- Analiza metryk sesyjnych dla zmiany: $CHANGE_NAME ---"
TOTAL_INPUT_TOKENS=0
TOTAL_OUTPUT_TOKENS=0
TOTAL_WALL_CLOCK_SECONDS=0

while read -r line; do
    [ -z "$line" ] && continue
    SESSION_ID=$(echo "$line" | awk '{print $1}')
    TOOL=$(echo "$line" | awk '{print $2}')
    
    if [ "$TOOL" == "AGY" ] || [ -z "$TOOL" ]; then
        LOG_FILE="$HOME/.gemini/antigravity-cli/brain/$SESSION_ID/.system_generated/logs/transcript.jsonl"
        if [ -f "$LOG_FILE" ]; then
            START_TIME_STR=$(head -n 1 "$LOG_FILE" | grep -o '"created_at":"[^"]*"' | head -n 1 | cut -d'"' -f4)
            END_TIME_STR=$(tail -n 20 "$LOG_FILE" | grep -o '"created_at":"[^"]*"' | tail -n 1 | cut -d'"' -f4)
            
            # Pobranie wyliczeń tokenów jeśli obecne w logu jsonl
            IN_TOKENS=$(grep -o '"input_tokens":[0-9]*' "$LOG_FILE" | awk -F':' '{sum+=$2} END {print sum+0}')
            OUT_TOKENS=$(grep -o '"output_tokens":[0-9]*' "$LOG_FILE" | awk -F':' '{sum+=$2} END {print sum+0}')
            
            # W przypadku gdy metryki tokenowe są estymowane z liczby kroków/pozytywnego zliczania
            STEPS=$(cat "$LOG_FILE" | wc -l | tr -d ' ')
            if [ "$IN_TOKENS" -eq 0 ]; then
                # Szacowanie na podstawie długości logu/kroków
                BYTES=$(wc -c < "$LOG_FILE" | tr -d ' ')
                IN_TOKENS=$(( BYTES / 4 ))
                OUT_TOKENS=$(( STEPS * 250 ))
            fi

            echo "  - Sesja ID: $SESSION_ID"
            echo "  - Czas startu: $START_TIME_STR"
            echo "  - Czas końca:  $END_TIME_STR"
            echo "  - Input Tokens:  $IN_TOKENS"
            echo "  - Output Tokens: $OUT_TOKENS"

            TOTAL_INPUT_TOKENS=$(( TOTAL_INPUT_TOKENS + IN_TOKENS ))
            TOTAL_OUTPUT_TOKENS=$(( TOTAL_OUTPUT_TOKENS + OUT_TOKENS ))
        else
            echo "  - Sesja ID: $SESSION_ID (brak pliku logów w $LOG_FILE)"
        fi
    fi
done < "$SESSION_FILE"

echo "----------------------------------------"
echo "Suma Input Tokens:  $TOTAL_INPUT_TOKENS"
echo "Suma Output Tokens: $TOTAL_OUTPUT_TOKENS"
