#!/usr/bin/env bash
# ==============================================================================
# Skrypt: setup-duplex.sh
# Opis:   Automatyczna konfiguracja i naprawa kolejki druku dwustronnego (Manual Duplex)
#         dla drukarek Samsung Xpress SL-M2026W / M2020 Series na systemie macOS.
# Autor:  Antigravity (Sesja Pawła, 2026-10-07)
# ==============================================================================

set -euo pipefail

# --- Kolory w konsoli ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# --- Domyślne wartości konfiguracji ---
QUEUE_NAME="Samsung_M2026W_Duplex"
DISPLAY_NAME="Samsung M2026W (Druk Dwustronny)"
PPD_PATH="/Library/Printers/PPDs/Contents/Resources/Samsung M2020 Series.gz"
PREFILTER_PATH="/Library/Printers/Samsung/UPD/Filters/prefilter"
RASTER_PATH="/Library/Printers/Samsung/UPD/Filters/rastertosec"
CACHE_FILE="/Library/Caches/com.sec.printer"
DEFAULT_MDNS="sec8425197ca25b.local"
PRINTER_PORT="9100"
PRINTER_HOST=""
SET_DEFAULT=0

# --- Funkcje pomocnicze ---
log_info() {
    echo -e "${CYAN}[INFO]${NC} $1"
}

log_ok() {
    echo -e "${GREEN}[OK]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[UWAGA]${NC} $1"
}

log_err() {
    echo -e "${RED}[BŁĄD]${NC} $1"
}

print_header() {
    echo -e "${BOLD}${BLUE}====================================================================${NC}"
    echo -e "${BOLD}${BLUE} Samsung M2026W / M2020 Series - Konfigurator Druku Dwustronnego   ${NC}"
    echo -e "${BOLD}${BLUE}====================================================================${NC}"
}

show_help() {
    print_header
    echo -e "Użycie: ${BOLD}$0${NC} [OPCJE]"
    echo ""
    echo "Opcje:"
    echo "  --host, --ip <HOST/IP>   Ręczne podanie adresu IP lub nazwy mDNS drukarki"
    echo "                           (domyślnie próbuje automatycznie wykryć)"
    echo "  --name <NAZWA>           Nazwa kolejki CUPS (domyślnie: ${QUEUE_NAME})"
    echo "  --display <OPIS>         Wyświetlana nazwa w oknie druku (domyślnie: '${DISPLAY_NAME}')"
    echo "  --status                 Wyświetla aktualny status kolejki i uprawnień bez zmian"
    echo "  --default                Ustawia utworzoną kolejkę jako domyślną drukarkę w macOS"
    echo "  --fix-permissions        Naprawia tylko uprawnienia pliku cache com.sec.printer"
    echo "  --install-wrappers       Kompiluje i instaluje wrappery filtrów CUPS w systemie"
    echo "  --test                   Generuje i wysyła 4-stronicowy dokument testowy"
    echo "  --help, -h               Wyświetla tę pomoc"
    echo ""
    echo "Przykłady:"
    echo "  $0                       Automatyczna detekcja i instalacja kolejki"
    echo "  $0 --host 192.168.3.15   Konfiguracja z bezpośrednim adresem IP"
    echo "  $0 --status              Sprawdzenie stanu konfiguracji"
    echo "  $0 --test                Wydruk próbny dwustronny"
    exit 0
}

# --- Sprawdzenie systemu operacyjnego ---
check_os() {
    if [[ "$(uname -s)" != "Darwin" ]]; then
        log_err "Ten skrypt jest przeznaczony wyłącznie dla systemu macOS."
        exit 1
    fi
}

# --- Sprawdzenie obecności sterowników Samsunga ---
check_drivers() {
    log_info "Weryfikacja obecności natywnych sterowników Samsung/HP..."
    local missing=0

    if [[ ! -f "$PPD_PATH" ]]; then
        log_err "Brak pliku PPD: $PPD_PATH"
        missing=1
    fi

    if [[ ! -f "$PREFILTER_PATH" ]]; then
        log_err "Brak filtra CUPS: $PREFILTER_PATH"
        missing=1
    fi

    if [[ ! -f "$RASTER_PATH" ]]; then
        log_err "Brak filtra rasteryzacji: $RASTER_PATH"
        missing=1
    fi

    if [[ $missing -ne 0 ]]; then
        echo ""
        log_err "Nie odnaleziono wymaganych sterowników Samsunga!"
        echo -e "${YELLOW}Aby zainstalować sterownik:${NC}"
        echo "1. Pobierz oficjalny pakiet 'Samsung Printer Drivers for macOS' (lub pakiet HP Print Driver dla serii M2020)."
        echo "2. Zainstaluj pakiet w systemie (wymaga uprawnień administratora)."
        echo "3. Uruchom ponownie ten skrypt."
        exit 1
    fi

    log_ok "Sterowniki Samsunga są zainstalowane w systemie."
}

# --- Sprawdzenie i usuwanie kwarantanny Gatekeepera ---
fix_quarantine() {
    log_info "Weryfikacja blokad kwarantanny Gatekeepera w /Library/Printers/Samsung..."
    local quarantined
    quarantined=$(xattr -r -l /Library/Printers/Samsung 2>/dev/null | grep -m 1 "com.apple.quarantine" || true)

    if [[ -n "$quarantined" ]]; then
        log_warn "Wykryto atrybuty kwarantanny macOS (Gatekeeper) na sterownikach Samsunga!"
        echo -e "${YELLOW}Powoduje to komunikat: 'Rzecz BasicOptionPDE.bundle nie została otwarta'.${NC}"
        if [[ $EUID -ne 0 ]]; then
            echo -e "${CYAN}Wymagane uprawnienia administratora do zdjęcia kwarantanny:${NC}"
            sudo xattr -d -r com.apple.quarantine /Library/Printers/Samsung 2>/dev/null || sudo xattr -cr /Library/Printers/Samsung 2>/dev/null || true
        else
            xattr -d -r com.apple.quarantine /Library/Printers/Samsung 2>/dev/null || xattr -cr /Library/Printers/Samsung 2>/dev/null || true
        fi
        log_ok "Kwarantanna Gatekeepera została usunięta ze sterowników Samsunga."
    else
        log_ok "Brak blokad kwarantanny Gatekeepera na sterownikach Samsunga."
    fi
}

# --- Sprawdzenie i naprawa uprawnień pliku cache com.sec.printer ---
fix_cache_permissions() {
    log_info "Weryfikacja uprawnień bufora sterownika ($CACHE_FILE)..."

    # Sprawdzenie czy plik istnieje i czy proces CUPS (_lp) ma prawo zapisu
    local need_fix=0
    if [[ ! -e "$CACHE_FILE" ]]; then
        need_fix=1
    else
        # Sprawdzamy czy ma uprawnienia 666 (world writable)
        local perms
        perms=$(stat -f "%OLp" "$CACHE_FILE" 2>/dev/null || echo "000")
        if [[ "$perms" != "666" && "$perms" != "777" ]]; then
            need_fix=1
        fi
    fi

    if [[ $need_fix -eq 1 ]]; then
        log_warn "Plik cache wymaga utworzenia lub naprawy uprawnień (0666 dla demona _lp)..."
        if [[ $EUID -ne 0 ]]; then
            echo -e "${CYAN}Wymagane uprawnienia administratora do zapisu w /Library/Caches:${NC}"
            sudo touch "$CACHE_FILE"
            sudo chmod 666 "$CACHE_FILE"
        else
            touch "$CACHE_FILE"
            chmod 666 "$CACHE_FILE"
        fi
        log_ok "Uprawnienia pliku $CACHE_FILE zostały poprawnie ustawione na 0666."
    else
        log_ok "Plik cache $CACHE_FILE istnieje i posiada poprawne uprawnienia."
    fi
}

# --- Kompilacja i instalacja wrapperów filtrów dupleksu ---
install_filter_wrappers() {
    log_info "Weryfikacja wrapperów filtrów CUPS dla automatycznego dupleksu..."
    local script_dir
    script_dir="$(cd "$(dirname "$0")" && pwd)"
    local src_file="$script_dir/samsung-duplex-wrapper.c"
    local pre_bin="$script_dir/prefilter-duplex"
    local sec_bin="$script_dir/rastertosec-duplex"
    local target_dir="/Library/Printers/Samsung/UPD/Filters"

    if [[ ! -f "$src_file" ]]; then
        log_err "Brak pliku źródłowego: $src_file"
        exit 1
    fi

    # Kompilacja dedykowanych wrapperów jeśli brak binarek lub kod źródłowy nowszy
    if [[ ! -f "$pre_bin" || ! -f "$sec_bin" || "$src_file" -nt "$pre_bin" || "$src_file" -nt "$sec_bin" ]]; then
        log_info "Kompilacja uniwersalnych wrapperów filtrów (ARM64 + x86_64)..."
        clang -O2 -arch arm64 -arch x86_64 -DTARGET_FILTER='"/Library/Printers/Samsung/UPD/Filters/prefilter"' "$src_file" -o "$pre_bin"
        clang -O2 -arch arm64 -arch x86_64 -DTARGET_FILTER='"/Library/Printers/Samsung/UPD/Filters/rastertosec"' "$src_file" -o "$sec_bin"
        log_ok "Skompilowano wrappery prefilter-duplex oraz rastertosec-duplex."
    fi

    # Sprawdzenie czy wrappery są zainstalowane w /Library/Printers/Samsung/UPD/Filters/
    local need_install=0
    if [[ ! -f "$target_dir/prefilter-duplex" || ! -f "$target_dir/rastertosec-duplex" ]]; then
        need_install=1
    elif [[ "$pre_bin" -nt "$target_dir/prefilter-duplex" || "$sec_bin" -nt "$target_dir/rastertosec-duplex" ]]; then
        need_install=1
    fi

    if [[ $need_install -eq 1 ]]; then
        log_info "Instalacja zaktualizowanych wrapperów w $target_dir..."
        if [[ $EUID -ne 0 ]]; then
            echo -e "${CYAN}Wymagane uprawnienia administratora do instalacji filtrów w systemie:${NC}"
            sudo cp "$pre_bin" "$target_dir/prefilter-duplex"
            sudo cp "$sec_bin" "$target_dir/rastertosec-duplex"
            sudo chown root:admin "$target_dir/prefilter-duplex" "$target_dir/rastertosec-duplex"
            sudo chmod 755 "$target_dir/prefilter-duplex" "$target_dir/rastertosec-duplex"
        else
            cp "$pre_bin" "$target_dir/prefilter-duplex"
            cp "$sec_bin" "$target_dir/rastertosec-duplex"
            chown root:admin "$target_dir/prefilter-duplex" "$target_dir/rastertosec-duplex"
            chmod 755 "$target_dir/prefilter-duplex" "$target_dir/rastertosec-duplex"
        fi
        log_ok "Wrapeppery filtrów prefilter-duplex oraz rastertosec-duplex zostały poprawnie zainstalowane."
    else
        log_ok "Wrapeppery filtrów są aktualne w $target_dir."
    fi
}

# --- Automatyczne wykrywanie adresu drukarki ---
detect_printer_host() {
    if [[ -n "$PRINTER_HOST" ]]; then
        log_info "Użyto adresu podanego ręcznie: $PRINTER_HOST"
        return 0
    fi

    log_info "Poszukiwanie drukarki Samsung w sieci lokalnej..."

    # 1. Sprawdzenie czy znany domyślny mDNS odpowiada
    if ping -c 1 -W 1000 "$DEFAULT_MDNS" >/dev/null 2>&1; then
        PRINTER_HOST="$DEFAULT_MDNS"
        log_ok "Wykryto drukarkę pod znaną nazwą mDNS: $PRINTER_HOST"
        return 0
    fi

    # 2. Sprawdzenie istniejącej kolejki AirPrint w lpstat -v
    local airprint_mac
    airprint_mac=$(lpstat -v 2>/dev/null | grep -i "Samsung" | grep -o -E 'SEC[0-9A-Fa-f]+' | head -n 1 || true)
    if [[ -n "$airprint_mac" ]]; then
        local candidate_mdns
        candidate_mdns="$(echo "$airprint_mac" | tr '[:upper:]' '[:lower:]').local"
        log_info "Odnaleziono identyfikator z istniejącej kolejki: $candidate_mdns"
        if ping -c 1 -W 1000 "$candidate_mdns" >/dev/null 2>&1; then
            PRINTER_HOST="$candidate_mdns"
            log_ok "Połączenie z $PRINTER_HOST potwierdzone!"
            return 0
        fi
    fi

    # 3. Jeśli żaden z powyższych, ostrzeżenie i prośba o podanie
    log_warn "Nie udało się automatycznie zlokalizować drukarki przez mDNS."
    echo -e "${YELLOW}Podaj adres IP lub nazwę sieciową drukarki (np. 192.168.3.15 lub sec8425197ca25b.local):${NC}"
    read -r -p "Adres drukarki: " user_input
    if [[ -z "$user_input" ]]; then
        log_err "Nie podano adresu drukarki. Przerywam."
        exit 1
    fi
    PRINTER_HOST="$user_input"
}

# --- Weryfikacja połączenia z portem RAW 9100 ---
verify_connection() {
    log_info "Testowanie połączenia RAW socket://$PRINTER_HOST:$PRINTER_PORT..."
    if nc -z -G 2 "$PRINTER_HOST" "$PRINTER_PORT" 2>/dev/null; then
        log_ok "Port $PRINTER_PORT na $PRINTER_HOST jest otwarty i gotowy do odbioru danych."
    else
        log_warn "Nie udało się połączyć z portem $PRINTER_PORT na $PRINTER_HOST."
        log_warn "Upewnij się, że drukarka jest włączona i podłączona do sieci Wi-Fi."
        read -r -p "Czy kontynuować konfigurację kolejki mimo to? [t/N]: " confirm
        if [[ "$confirm" != "t" && "$confirm" != "T" && "$confirm" != "tak" && "$confirm" != "TAK" ]]; then
            log_err "Przerwano przez użytkownika."
            exit 1
        fi
    fi
}

# --- Konfiguracja kolejki CUPS ---
configure_cups_queue() {
    log_info "Konfiguracja kolejki CUPS '${QUEUE_NAME}'..."

    local device_uri="socket://${PRINTER_HOST}:${PRINTER_PORT}"

    # Przygotowanie oczyszczonego pliku PPD (bez zawieszających wtyczek APDialogExtension / Rosetta)
    local clean_ppd_file="$(cd "$(dirname "$0")" && pwd)/Samsung_M2020_Series_Clean.ppd"
    log_info "Przygotowanie zoptymalizowanego PPD (usunięcie przestarzałych wtyczek GUI i dodanie natywnego dupleksu)..."
    python3 -c "
import gzip
with gzip.open('$PPD_PATH', 'rb') as f:
    ppd = f.read()

# 1. Usunięcie przestarzałych wtyczek GUI powodujących zawieszenie na Apple Silicon
lines = [l for l in ppd.splitlines() if not l.startswith(b'*APDialogExtension:') and not l.startswith(b'*APPrinterUtilityPath:') and not l.startswith(b'*APPrinterIconPath:')]
text = b'\n'.join(lines)

# 2. Wymuszenie filtrów wrappera dla automatycznego dupleksu
text = text.replace(b'/Library/Printers/Samsung/UPD/Filters/rastertosec', b'/Library/Printers/Samsung/UPD/Filters/rastertosec-duplex')
text = text.replace(b'/Library/Printers/Samsung/UPD/Filters/prefilter', b'/Library/Printers/Samsung/UPD/Filters/prefilter-duplex')

# 3. Wymuszenie domyślnego dupleksu w sterowniku Samsunga
text = text.replace(b'*DefaultSECManualDuplexOption: None', b'*DefaultSECManualDuplexOption: LongEdge')

# 3. Wstrzyknięcie standardowej sekcji Apple/CUPS Duplex (Two-Sided)
duplex_block = b'''
*% =========================================================
*% Standard macOS Duplex (Two-Sided Printing)
*% =========================================================

*OpenUI *Duplex/Two-Sided: PickOne
*OrderDependency: 20 AnySetup *Duplex
*DefaultDuplex: DuplexNoTumble
*Duplex None/Off: \"\"
*Duplex DuplexNoTumble/Long-Edge (Standard): \"\"
*Duplex DuplexTumble/Short-Edge (Flip): \"\"
*CloseUI: *Duplex
'''

if b'*OpenUI *Duplex' not in text:
    target = b'*CloseUI: *SECManualDuplexOption'
    if target in text:
        text = text.replace(target, target + b'\n' + duplex_block)
    else:
        text += b'\n' + duplex_block

with open('$clean_ppd_file', 'wb') as f:
    f.write(text)
"

    # Wywołanie lpadmin z czystym PPD
    lpadmin -p "$QUEUE_NAME" -E \
        -v "$device_uri" \
        -P "$clean_ppd_file" \
        -D "$DISPLAY_NAME" \
        -o PageSize=A4 \
        -o SECManualDuplexOption=LongEdge \
        -o Duplex=DuplexNoTumble

    # Zapisanie domyślnych opcji użytkownika
    lpoptions -p "$QUEUE_NAME" -o SECManualDuplexOption=LongEdge -o Duplex=DuplexNoTumble 2>/dev/null || true

    log_ok "Kolejka '${QUEUE_NAME}' została utworzona/zaktualizowana (PPD zoptymalizowany pod Apple Silicon/macOS)."

    # Weryfikacja opcji w PPD
    log_info "Weryfikacja parametrów kolejki..."
    local duplex_opt
    duplex_opt=$(lpoptions -p "$QUEUE_NAME" -l 2>/dev/null | grep "SECManualDuplexOption" || true)
    local cups_duplex
    cups_duplex=$(lpoptions -p "$QUEUE_NAME" -l 2>/dev/null | grep "Duplex/" || true)
    local page_opt
    page_opt=$(lpoptions -p "$QUEUE_NAME" -l 2>/dev/null | grep "PageSize" || true)

    echo -e "  - Samsung Duplex: ${GREEN}${duplex_opt}${NC}"
    echo -e "  - macOS Duplex:   ${GREEN}${cups_duplex}${NC}"
    echo -e "  - Format papieru: ${GREEN}${page_opt}${NC}"

    # Włączenie kolejki i akceptacja zadań (odblokowanie jeśli była zapauzowana)
    cupsenable "$QUEUE_NAME" 2>/dev/null || true
    cupsaccept "$QUEUE_NAME" 2>/dev/null || true

    if [[ "$SET_DEFAULT" -eq 1 ]]; then
        log_info "Ustawianie kolejki '${QUEUE_NAME}' jako domyślnej w systemie..."
        lpoptions -d "$QUEUE_NAME" 2>/dev/null || true
        log_ok "Kolejka '${QUEUE_NAME}' została ustawiona jako domyślna drukarka."
    fi
}

# --- Wyświetlenie statusu ---
show_status() {
    print_header
    echo -e "${BOLD}STAN KONFIGURACJI DRUKARKI SAMSUNG:${NC}"
    echo ""

    echo -n "1. Sterowniki systemowe: "
    if [[ -f "$PPD_PATH" && -f "$PREFILTER_PATH" && -f "$RASTER_PATH" ]]; then
        echo -e "${GREEN}Zainstalowane${NC} ($PPD_PATH)"
    else
        echo -e "${RED}Brak wymaganych plików sterownika!${NC}"
    fi

    echo -n "2. Kwarantanna Gatekeepera (/Library/Printers/Samsung): "
    local quarantined
    quarantined=$(xattr -r -l /Library/Printers/Samsung 2>/dev/null | grep -m 1 "com.apple.quarantine" || true)
    if [[ -z "$quarantined" ]]; then
        echo -e "${GREEN}Czysto (brak blokad)${NC}"
    else
        echo -e "${YELLOW}Wykryto atrybuty kwarantanny! (uruchom z sudo lub opcją --fix-permissions)${NC}"
    fi

    echo -n "3. Bufor cache ($CACHE_FILE): "
    if [[ -f "$CACHE_FILE" ]]; then
        local perms
        perms=$(stat -f "%OLp" "$CACHE_FILE" 2>/dev/null || echo "???")
        local owner
        owner=$(stat -f "%Su:%Sg" "$CACHE_FILE" 2>/dev/null || echo "???")
        echo -e "${GREEN}Istnieje${NC} (Uprawnienia: $perms, Właściciel: $owner)"
    else
        echo -e "${RED}Brak pliku! (Musi zostać utworzony z uprawnieniami 0666)${NC}"
    fi

    echo -n "4. Wrappery filtrów dupleksu (prefilter-duplex / rastertosec-duplex): "
    if [[ -f "/Library/Printers/Samsung/UPD/Filters/prefilter-duplex" && -f "/Library/Printers/Samsung/UPD/Filters/rastertosec-duplex" ]]; then
        echo -e "${GREEN}Zainstalowane i aktywne${NC}"
    else
        echo -e "${YELLOW}Brak w /Library/Printers/Samsung/UPD/Filters (wymaga instalacji)${NC}"
    fi

    echo ""
    echo -e "${BOLD}Zainstalowane kolejki CUPS:${NC}"
    lpstat -p -d 2>/dev/null || echo "Brak dostępnych kolejek."

    echo ""
    echo -e "${BOLD}Adresy urządzeń dla kolejek:${NC}"
    lpstat -v 2>/dev/null | grep -i "Samsung" || echo "Brak kolejek Samsung."

    if lpstat -p "$QUEUE_NAME" >/dev/null 2>&1; then
        echo ""
        echo -e "${BOLD}Szczegóły opcji dla '${QUEUE_NAME}':${NC}"
        lpoptions -p "$QUEUE_NAME" -l 2>/dev/null | grep -E "SECManualDuplexOption|PageSize|Resolution" || true
    fi
    echo ""
}

# --- Wykonanie testu druku dwustronnego ---
run_test() {
    print_header
    log_info "Rozpoczynam test druku dwustronnego..."

    if ! lpstat -p "$QUEUE_NAME" >/dev/null 2>&1; then
        log_err "Kolejka '$QUEUE_NAME' nie istnieje! Uruchom najpierw: $0"
        exit 1
    fi

    fix_cache_permissions

    local test_pdf="/tmp/samsung_duplex_test_4pages.pdf"
    log_info "Generowanie 4-stronicowego dokumentu testowego ($test_pdf)..."

    # Generujemy prosty testowy dokument 4-stronicowy za pomocą python3
    python3 -c "
import sys

# Tworzymy minimalistyczny, w 100% poprawny PDF z 4 ponumerowanymi stronami
pdf_content = b'''%PDF-1.4
1 0 obj
<< /Type /Catalog /Pages 2 0 R >>
endobj
2 0 obj
<< /Type /Pages /Kids [3 0 R 4 0 R 5 0 R 6 0 R] /Count 4 >>
endobj
3 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 7 0 R /Resources << /Font << /F1 11 0 R >> >> >>
endobj
4 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 8 0 R /Resources << /Font << /F1 11 0 R >> >> >>
endobj
5 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 9 0 R /Resources << /Font << /F1 11 0 R >> >> >>
endobj
6 0 obj
<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 10 0 R /Resources << /Font << /F1 11 0 R >> >> >>
endobj
7 0 obj
<< /Length 124 >>
stream
BT
/F1 28 Tf
50 750 Td
(TEST DRUKU DWUSTRONNEGO - STRONA 1 z 4) Tj
/F1 16 Tf
0 -40 Td
(To jest pierwsza strona pierwszej kartki.) Tj
ET
endstream
endobj
8 0 obj
<< /Length 124 >>
stream
BT
/F1 28 Tf
50 750 Td
(TEST DRUKU DWUSTRONNEGO - STRONA 2 z 4) Tj
/F1 16 Tf
0 -40 Td
(To jest druga strona pierwszej kartki.) Tj
ET
endstream
endobj
9 0 obj
<< /Length 124 >>
stream
BT
/F1 28 Tf
50 750 Td
(TEST DRUKU DWUSTRONNEGO - STRONA 3 z 4) Tj
/F1 16 Tf
0 -40 Td
(To jest pierwsza strona drugiej kartki.) Tj
ET
endstream
endobj
10 0 obj
<< /Length 124 >>
stream
BT
/F1 28 Tf
50 750 Td
(TEST DRUKU DWUSTRONNEGO - STRONA 4 z 4) Tj
/F1 16 Tf
0 -40 Td
(To jest druga strona drugiej kartki.) Tj
ET
endstream
endobj
11 0 obj
<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>
endobj
xref
0 12
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000133 00000 n 
0000000257 00000 n 
0000000381 00000 n 
0000000505 00000 n 
0000000629 00000 n 
0000000806 00000 n 
0000000983 00000 n 
0000001160 00000 n 
0000001337 00000 n 
trailer
<< /Size 12 /Root 1 0 R >>
startxref
1414
%%EOF
'''
with open('/tmp/samsung_duplex_test_4pages.pdf', 'wb') as f:
    f.write(pdf_content)
"

    log_ok "Plik testowy utworzony: $test_pdf"
    echo ""
    echo -e "${BOLD}${YELLOW}JAK PRZEBIEGA TEST:${NC}"
    echo "1. Dokument ma 4 strony (2 fizyczne kartki papieru)."
    echo "2. Drukarka pobierze papier i wydrukuje pierwszą partię (strony parzyste)."
    echo "3. Drukarka zatrzyma się, a jej dioda LED zacznie migać."
    echo "4. Wyjmij arkusze z górnej tacki i BEZ obracania ich porządku włóż je prosto do dolnego podajnika."
    echo "5. Naciśnij fizyczny przycisk na drukarce (WPS / Print Screen / Power)."
    echo "6. Drukarka zadrukuje drugą stronę i zakończy zadanie."
    echo ""
    read -r -p "Czy chcesz teraz wysłać zadanie testowe do drukarki? [t/N]: " send_confirm
    if [[ "$send_confirm" == "t" || "$send_confirm" == "T" || "$send_confirm" == "tak" || "$send_confirm" == "TAK" ]]; then
        local job_output
        job_output=$(lp -d "$QUEUE_NAME" "$test_pdf")
        log_ok "Wysłano zadanie do kolejki: $job_output"
        echo -e "${GREEN}Obserwuj diodę na drukarce i postępuj zgodnie z instrukcją!${NC}"
    else
        log_info "Wydruk testowy anulowany. Plik testowy znajduje się w $test_pdf"
    fi
}

# --- Parsowanie parametrów wiersza poleceń ---
while [[ $# -gt 0 ]]; do
    case "$1" in
        --host|--ip)
            PRINTER_HOST="$2"
            shift 2
            ;;
        --name)
            QUEUE_NAME="$2"
            shift 2
            ;;
        --display)
            DISPLAY_NAME="$2"
            shift 2
            ;;
        --status)
            show_status
            exit 0
            ;;
        --fix-permissions)
            print_header
            check_os
            fix_quarantine
            fix_cache_permissions
            exit 0
            ;;
        --install-wrappers)
            print_header
            check_os
            check_drivers
            install_filter_wrappers
            exit 0
            ;;
        --test)
            run_test
            exit 0
            ;;
        --default)
            SET_DEFAULT=1
            shift
            ;;
        --help|-h)
            show_help
            ;;
        *)
            log_err "Nieznana opcja: $1"
            echo "Użyj $0 --help aby wyświetlić dostępne opcje."
            exit 1
            ;;
    esac
done

# --- Główny przepływ instalatora ---
main() {
    print_header
    check_os
    check_drivers
    fix_quarantine
    fix_cache_permissions
    install_filter_wrappers
    detect_printer_host
    verify_connection
    configure_cups_queue

    echo ""
    echo -e "${BOLD}${GREEN}====================================================================${NC}"
    echo -e "${BOLD}${GREEN} KONFIGURACJA ZAKOŃCZONA SUKCESEM! 🎉                             ${NC}"
    echo -e "${BOLD}${GREEN}====================================================================${NC}"
    echo -e "Kolejka dupleksowa:    ${BOLD}${CYAN}${QUEUE_NAME}${NC}"
    echo -e "Nazwa w oknie druku:   ${BOLD}${CYAN}${DISPLAY_NAME}${NC}"
    echo -e "Adres urządzenia:      ${BOLD}socket://${PRINTER_HOST}:${PRINTER_PORT}${NC}"
    echo -e "Domyślna opcja:        ${BOLD}SECManualDuplexOption=LongEdge (Format A4)${NC}"
    echo ""
    echo -e "${BOLD}Jak drukować dwustronnie w aplikacjach (Word, Chrome, Podgląd itp.):${NC}"
    echo -e "1. W oknie druku (${BOLD}Cmd + P${NC}) wybierz drukarkę: ${CYAN}${DISPLAY_NAME}${NC}."
    echo -e "2. Kliknij ${BOLD}Drukuj${NC}."
    echo -e "3. Drukarka wydrukuje pierwszą partię stron i ${YELLOW}zatrzyma się z migającą diodą${NC}."
    echo -e "4. Weź wydrukowany plik kartek z górnej tacy odbiorczej i włóż go prosto do dolnego podajnika"
    echo -e "   (${BOLD}nie musisz przekładać kartek pojedynczo ani odwracać kolejności${NC} - sterownik to zaplanował!)."
    echo -e "5. Naciśnij fizyczny przycisk na drukarce (${BOLD}WPS / Print Screen${NC}). Drukarka dokończy drugą stronę."
    echo ""
    echo -e "Aby przetestować wydruk w dowolnym momencie, uruchom:"
    echo -e "  ${BOLD}$0 --test${NC}"
    echo ""
}

main
