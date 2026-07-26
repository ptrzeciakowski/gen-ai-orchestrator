#!/bin/bash
# Tool: opsx-validate-repo
# Sprawdza bezpieczeństwo i stan zewnętrznego repozytorium (symlinka / locka gita).

REPO_PATH="$1"

if [ -z "$REPO_PATH" ]; then
    echo "Użycie: ./opsx-validate-repo.sh <sciezka_do_repo>"
    exit 1
fi

# 1. Walidacja symlinka i zapobieganie pętlom rekurencyjnym
REAL_PATH=$(realpath "$REPO_PATH" 2>/dev/null)
if [ $? -ne 0 ] || [ ! -d "$REAL_PATH" ]; then
    echo "❌ BŁĄD: Ścieżka $REPO_PATH nie istnieje lub nie jest poprawnym katalogiem."
    exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null)"
if [ -n "$REPO_ROOT" ]; then
    REAL_REPO_ROOT=$(realpath "$REPO_ROOT")
    if [[ "$REAL_PATH" == "$REAL_REPO_ROOT"* ]] && [[ "$REAL_PATH" != "$REAL_REPO_ROOT" ]]; then
        echo "❌ BŁĄD: Symlink $REPO_PATH próbuje wskazywać na podkatalog orkiestratora ($REAL_PATH)."
        exit 1
    fi
fi

# 2. Sprawdzanie blokady .git/index.lock
INDEX_LOCK="$REAL_PATH/.git/index.lock"
if [ -f "$INDEX_LOCK" ]; then
    echo "⚠️ BŁĄD: Repozytorium w $REAL_PATH jest zablokowane przez inny proces ($INDEX_LOCK)."
    echo "Poczekaj na zakończenie operacji lub sprawdź czy plik .git/index.lock nie pozostał po awarii."
    exit 2
fi

echo "✅ Repozytorium $REAL_PATH jest bezpieczne i gotowe do pracy."
exit 0
