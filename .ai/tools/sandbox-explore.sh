#!/bin/bash
# Tool: sandbox-explore
# Opis: Zarządza strukturą folderów w katalogu sandbox/ w konwencji YYYY-MM-DD-nazwa-explore
#       oraz automatycznie wyznacza kolejny plik sesji (001.md, 002.md, itd.).

set -e

if [ -z "$1" ]; then
    echo "Użycie: ./sandbox-explore.sh <folder_name> [session_id] [title]"
    echo "Przykład: ./sandbox-explore.sh 2026-09-07-narty-austria-ferie-2027-explore be037837-af4c-4ac5-923f-97a1e668b620 \"Wybór ofert narciarskich\""
    exit 1
fi

FOLDER_NAME="$1"
SESSION_ID="${2:-brak-id}"
TITLE="${3:-Sesja eksploracyjna}"

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
SANDBOX_DIR="$REPO_ROOT/sandbox"
TARGET_DIR="$SANDBOX_DIR/$FOLDER_NAME"

# Utworzenie folderów
mkdir -p "$TARGET_DIR"

# Ustalenie kolejnego numeru pliku (001, 002, ...)
LAST_NUM=$(ls "$TARGET_DIR"/[0-9][0-9][0-9]*.md 2>/dev/null | sed -E 's/.*\/([0-9]{3}).*/\1/' | sort -n | tail -n 1)

if [ -z "$LAST_NUM" ]; then
    NEXT_NUM=1
else
    NEXT_NUM=$(( 10#$LAST_NUM + 1 ))
fi

# Ustalenie 3-5 wyrazowego sluga tematycznego
SLUG="$4"
if [ -z "$SLUG" ]; then
    # Wygenerowanie sluga z tytułu (małe litery, usunięcie znaków specjalnych, do 5 wyrazów)
    SLUG=$(echo "$TITLE" | tr '[:upper:]' '[:lower:]' | iconv -c -t ascii//TRANSLIT 2>/dev/null || echo "$TITLE" | tr '[:upper:]' '[:lower:]')
    SLUG=$(echo "$SLUG" | sed -E 's/[^a-z0-9]+/ /g' | awk '{for(i=1;i<=NF && i<=5;i++) printf("%s%s", $i, (i<NF && i<5)?"-":"")}')
fi

if [ -z "$SLUG" ]; then
    SLUG="sesja-badawcza"
fi

FORMATTED_NUM=$(printf "%03d" "$NEXT_NUM")
TARGET_FILE="$TARGET_DIR/${FORMATTED_NUM}-${SLUG}.md"

echo "TARGET_DIR: $TARGET_DIR"
echo "NEXT_FILE: $TARGET_FILE"
echo "SESSION_ID: $SESSION_ID"
echo "TITLE: $TITLE"
echo "SLUG: $SLUG"

# Jeśli plik jeszcze nie istnieje, możemy zainicjalizować szablon
if [ ! -f "$TARGET_FILE" ]; then
    CURRENT_DATE=$(date "+%Y-%m-%d %H:%M:%S %Z")
    cat << TEMPLATE > "$TARGET_FILE"
# ${FORMATTED_NUM}: ${TITLE}

- **Data i godzina sesji:** ${CURRENT_DATE}
- **ID sesji:** \`${SESSION_ID}\`
- **Tytuł:** ${TITLE}

---

TEMPLATE
    echo "✅ Utworzono plik sesji: $TARGET_FILE"
else
    echo "ℹ️ Plik $TARGET_FILE już istnieje."
fi
