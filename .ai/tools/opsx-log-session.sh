#!/bin/bash
# Tool: opsx-log-session
# Opis: Skrypt do tworzenia i aktualizacji pliku .sessions z logami identyfikatorów sesji oraz metryk, umieszczanego w katalogu odpowiedniej zmiany.

if [ "$#" -lt 2 ]; then
    echo "Użycie: ./opsx-log-session.sh <session_id> <change_name> [statystyki_np_tokens_time]"
    exit 1
fi

SESSION_ID="$1"
CHANGE_NAME="$2"
STATS="${3:-Brak szczegółowych danych}"
CURRENT_DATE=$(date +"%Y-%m-%d %H:%M:%S")

REPO_ROOT="$(git rev-parse --show-toplevel)"
CHANGE_DIR="$REPO_ROOT/openspec/changes/$CHANGE_NAME"

# Jeżeli nie znaleziono w bieżących zmianach, szukaj w archiwum
if [ ! -d "$CHANGE_DIR" ]; then
    CHANGE_DIR="$REPO_ROOT/openspec/changes/archive/$CHANGE_NAME"
    if [ ! -d "$CHANGE_DIR" ]; then
        echo "Katalog zmiany $CHANGE_NAME nie istnieje (zostanie zachowane w root)."
        CHANGE_DIR="$REPO_ROOT"
    fi
fi

SESSION_FILE_PATH="$CHANGE_DIR/.sessions"

if [ ! -f "$SESSION_FILE_PATH" ]; then
    echo "# Logi Sesji Agentów (AGY) dla $CHANGE_NAME" > "$SESSION_FILE_PATH"
    echo "=========================" >> "$SESSION_FILE_PATH"
fi

echo "[$CURRENT_DATE] Session ID: $SESSION_ID | Stats: $STATS" >> "$SESSION_FILE_PATH"
echo "Log sesji $SESSION_ID dopisany do $SESSION_FILE_PATH pomyślnie."
