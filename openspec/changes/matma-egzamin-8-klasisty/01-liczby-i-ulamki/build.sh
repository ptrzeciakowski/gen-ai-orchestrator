#!/usr/bin/env bash
# Kompiluje wszystkie karty i quizy do PDF (wymaga tectonic: brew install tectonic).
# Każda karta i każdy arkusz musi mieścić się na jednej stronie A4.
set -euo pipefail

cd "$(dirname "$0")"

for tex in karty/*.tex quizy/*.tex; do
  tectonic -X compile --keep-logs "$tex"
  pages=$(grep -o '([0-9]* pages\?' "${tex%.tex}.log" | tr -dc '0-9')
  if [ "$pages" != "1" ]; then
    echo "UWAGA: $tex ma $pages stron (oczekiwano 1)" >&2
    exit 1
  fi
done

# Porządki po kompilacji: logi i pliki pośrednie
rm -f karty/*.log karty/*.xdv quizy/*.log quizy/*.xdv
echo "Gotowe: karty/ i quizy/ (każdy PDF = 1 strona A4)"
