#!/bin/bash
# Tool: opsx-log-session
# Opis: Skrypt do tworzenia i aktualizacji pliku .sessions zawierającego id sesji oraz tool-a dla danej zmiany.

if [ "$#" -lt 2 ]; then
    echo "Użycie: ./opsx-log-session.sh <session_id> <change_name> [tool_name]"
    exit 1
fi

SESSION_ID="$1"
CHANGE_NAME="$2"
TOOL_NAME="${3:-AGY}"

REPO_ROOT="$(git rev-parse --show-toplevel)"
CHANGE_DIR="$REPO_ROOT/openspec/changes/$CHANGE_NAME"

if [ ! -d "$CHANGE_DIR" ]; then
    CHANGE_DIR="$REPO_ROOT/openspec/changes/archive/$CHANGE_NAME"
    if [ ! -d "$CHANGE_DIR" ]; then
        echo "Katalog zmiany $CHANGE_NAME nie istnieje (zostanie zachowane w root)."
        CHANGE_DIR="$REPO_ROOT"
    fi
fi

SESSION_FILE_PATH="$CHANGE_DIR/.sessions"

echo "$SESSION_ID $TOOL_NAME" >> "$SESSION_FILE_PATH"
echo "Zalogowano: $SESSION_ID $TOOL_NAME do $SESSION_FILE_PATH"
