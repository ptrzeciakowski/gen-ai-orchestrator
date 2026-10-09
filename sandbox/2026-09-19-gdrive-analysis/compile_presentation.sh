#!/usr/bin/env bash
# Skrypt kompilacji prezentacji Beamer do formatu PDF
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEX_FILE="prezentacja_gdrive_beamer.tex"
PDF_FILE="prezentacja_gdrive_beamer.pdf"

cd "$DIR"

echo "=== Kompilacja prezentacji Beamer: $TEX_FILE ==="

if command -v tectonic >/dev/null 2>&1; then
    echo "Kompilacja za pomocą silnika Tectonic..."
    tectonic "$TEX_FILE"
    echo "SUKCES! Wygenerowano plik: $DIR/$PDF_FILE"
elif command -v pdflatex >/dev/null 2>&1; then
    echo "[1/2] Pierwszy przebieg pdflatex..."
    pdflatex -interaction=nonstopmode "$TEX_FILE" >/dev/null
    echo "[2/2] Drugi przebieg pdflatex (spójność numeracji stron)..."
    pdflatex -interaction=nonstopmode "$TEX_FILE"
    echo "SUKCES! Wygenerowano plik: $DIR/$PDF_FILE"
elif command -v docker >/dev/null 2>&1; then
    echo "Wykryto Docker. Uruchamianie kompilacji w kontenerze TeX Live..."
    docker run --rm -v "$DIR":/work -w /work texlive/texlive:latest sh -c \
      "pdflatex -interaction=nonstopmode $TEX_FILE && pdflatex -interaction=nonstopmode $TEX_FILE"
    echo "SUKCES! Wygenerowano plik za pomocą Dockera: $DIR/$PDF_FILE"
else
    echo "UWAGA: Brak lokalnego kompilatora 'pdflatex' oraz 'docker'."
    echo "Możesz skompilować plik na kilka sposobów:"
    echo "  1. Zainstaluj MacTeX/TeX Live: brew install --cask mactex-no-gui"
    echo "  2. Otwórz plik w Overleaf (https://www.overleaf.com) metodą Drag & Drop"
    echo "  3. Użyj dowolnego środowiska LaTeX (VS Code z rozszerzeniem LaTeX Workshop, TeXShop itp.)"
    exit 1
fi
