#!/usr/bin/env python3
"""
generate_pdf.py
Generuje plik PDF z pliku HTML zoptymalizowanego pod wydruk A4
przy użyciu silnika Google Chrome w trybie headless.
"""

import sys
import os
import shutil
import subprocess
import argparse

def find_chrome_binary():
    """Znajduje ścieżkę do wykonywalnego pliku Chrome/Chromium."""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for c in candidates:
        if c and os.path.isfile(c) and os.access(c, os.X_OK):
            return c
    return None

def main():
    parser = argparse.ArgumentParser(description="Generuj PDF z HTML przez Google Chrome headless.")
    parser.add_argument("input_html", help="Ścieżka do pliku wejściowego .html")
    parser.add_argument("-o", "--output", dest="output_pdf", help="Ścieżka do pliku wyjściowego .pdf")
    args = parser.parse_args()

    input_path = os.path.abspath(os.path.expanduser(args.input_html))
    if not os.path.isfile(input_path):
        print(f"❌ Błąd: Plik HTML nie istnieje: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output_pdf:
        output_path = os.path.abspath(os.path.expanduser(args.output_pdf))
    else:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    chrome_bin = find_chrome_binary()
    if not chrome_bin:
        print("❌ Błąd: Nie znaleziono przeglądarki Google Chrome ani Chromium w systemie.", file=sys.stderr)
        sys.exit(1)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={output_path}",
        input_path
    ]

    print(f"🔄 Renderowanie PDF przez Chrome: {input_path} -> {output_path}")
    res = subprocess.run(cmd, capture_output=True, text=True)

    if not os.path.isfile(output_path) or os.path.getsize(output_path) == 0:
        print(f"❌ Błąd generowania PDF. Kod: {res.returncode}", file=sys.stderr)
        if res.stderr:
            print(f"Stderr: {res.stderr}", file=sys.stderr)
        sys.exit(1)

    size_kb = os.path.getsize(output_path) // 1024
    print(f"✅ Sukces! Wygenerowano PDF: {output_path} ({size_kb} KB)")

if __name__ == "__main__":
    main()
