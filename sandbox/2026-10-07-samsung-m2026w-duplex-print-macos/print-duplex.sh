#!/usr/bin/env bash
# ==============================================================================
# Skrypt: print-duplex.sh
# Opis:   Szybkie wysyłanie dokumentu do druku dwustronnego (Manual Duplex)
#         na drukarce Samsung M2026W z poziomu terminala.
# Autor:  Antigravity (Sesja Pawła, 2026-10-07)
# ==============================================================================

set -euo pipefail

QUEUE_NAME="Samsung_M2026W_Duplex"

# Kolory
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

if [[ $# -eq 0 || "$1" == "-h" || "$1" == "--help" ]]; then
    echo -e "${BOLD}Użycie:${NC} $0 <ścieżka_do_pliku.pdf> [opcjonalne_argumenty_lp...]"
    echo ""
    echo "Przykłady:"
    echo "  $0 dokument.pdf"
    echo "  $0 raport.pdf -o page-ranges=1-8"
    echo ""
    exit 0
fi

FILE="$1"
shift

if [[ ! -f "$FILE" ]]; then
    echo -e "${RED}[BŁĄD]${NC} Plik '$FILE' nie istnieje lub nie jest zwykłym plikiem."
    exit 1
fi

# Sprawdzenie czy kolejka istnieje
if ! lpstat -p "$QUEUE_NAME" >/dev/null 2>&1; then
    echo -e "${RED}[BŁĄD]${NC} Kolejka '$QUEUE_NAME' nie została odnaleziona w systemie CUPS."
    echo -e "Uruchom najpierw konfigurator: ${BOLD}./setup-duplex.sh${NC}"
    exit 1
fi

# Sprawdzenie uprawnień bufora
if [[ -f "/Library/Caches/com.sec.printer" ]]; then
    perms=$(stat -f "%OLp" "/Library/Caches/com.sec.printer" 2>/dev/null || echo "000")
    if [[ "$perms" != "666" && "$perms" != "777" ]]; then
        echo -e "${YELLOW}[UWAGA]${NC} Plik /Library/Caches/com.sec.printer ma uprawnienia $perms zamiast 666."
        echo -e "Naprawiam uprawnienia bufora, aby uniknąć błędu sterownika..."
        sudo chmod 666 /Library/Caches/com.sec.printer 2>/dev/null || true
    fi
fi

echo -e "${CYAN}Wysyłanie zadania do kolejki:${NC} ${BOLD}${QUEUE_NAME}${NC}..."
JOB_OUT=$(lp -d "$QUEUE_NAME" "$@" "$FILE")
echo -e "${GREEN}[OK]${NC} $JOB_OUT"

echo ""
echo -e "${BOLD}${YELLOW}====================================================================${NC}"
echo -e "${BOLD}${YELLOW} INSTRUKCJA DRUKU DWUSTRONNEGO (SAMSUNG M2026W)                     ${NC}"
echo -e "${BOLD}${YELLOW}====================================================================${NC}"
echo -e "1. Drukarka pobierze papier i wydrukuje ${BOLD}pierwszą partię stron${NC} (parzyste)."
echo -e "2. Po wydrukowaniu partii dioda na drukarce ${BOLD}zacznie migać na pomarańczowo/zielono${NC}."
echo -e "3. ${BOLD}Wyjmij cały plik kartek z górnej tacy odbiorczej${NC}."
echo -e "4. ${BOLD}Włóż go prosto do dolnego podajnika papieru${NC}:"
echo -e "   - ${GREEN}NIE odwracaj pojedynczych kartek!${NC}"
echo -e "   - Sterownik ułożył strony tak, że bierzesz stos i wsuwasz go z powrotem do zasobnika."
echo -e "5. Naciśnij fizyczny przycisk na drukarce: ${BOLD}WPS / Print Screen / Zasilania${NC}."
echo -e "6. Drukarka pobierze kartki, zadrukuje drugą stronę i zakończy pracę."
echo -e "${BOLD}${YELLOW}====================================================================${NC}"
echo ""
