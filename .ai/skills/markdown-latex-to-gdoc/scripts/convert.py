#!/usr/bin/env python3
"""
markdown-latex-to-gdoc / convert.py
Konwertuje dokumenty Markdown zawierające wzory LaTeX ($...$ oraz $$...$$)
do formatu Microsoft Word (.docx) z zachowaniem natywnych równań Office Math (OMML),
które są w 100% kompatybilne z Dokumentami Google (Google Docs).
"""

import argparse
import glob
import os
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile


def find_google_drive_path():
    """Wyszukuje lokalny punkt montowania Dysku Google na macOS."""
    candidates = glob.glob(
        os.path.expanduser(
            "~/Library/CloudStorage/GoogleDrive-*/Mój dysk"
        )
    ) + glob.glob(
        os.path.expanduser(
            "~/Library/CloudStorage/GoogleDrive-*/My Drive"
        )
    ) + glob.glob(
        os.path.expanduser(
            "~/Library/CloudStorage/GoogleDrive-*"
        )
    )
    if candidates:
        return candidates[0]
    return None


def verify_pandoc():
    """Sprawdza obecność programu pandoc w systemie."""
    pandoc_path = shutil.which("pandoc")
    if not pandoc_path:
        # Sprawdzenie standardowych ścieżek Homebrew na macOS
        for candidate in ["/opt/homebrew/bin/pandoc", "/usr/local/bin/pandoc"]:
            if os.path.isfile(candidate) and os.access(candidate, os.X_OK):
                return candidate
        return None
    return pandoc_path


def count_omml_equations(docx_path):
    """Liczy liczbę skonwertowanych równań OMML w wygenerowanym pliku .docx."""
    try:
        with zipfile.ZipFile(docx_path, "r") as z:
            xml_content = z.read("word/document.xml")
        root = ET.fromstring(xml_content)
        ns = {"m": "http://schemas.openxmlformats.org/officeDocument/2006/math"}
        inline_math = root.findall(".//m:oMath", ns)
        display_math = root.findall(".//m:oMathPara", ns)
        return len(inline_math), len(display_math)
    except Exception as e:
        return 0, 0


def convert_markdown_to_docx(input_md, output_docx, pandoc_exec="pandoc"):
    """Wykonuje konwersję za pomocą pandoc."""
    cmd = [
        pandoc_exec,
        input_md,
        "-f",
        "markdown+tex_math_dollars+tex_math_single_backslash",
        "-t",
        "docx",
        "-o",
        output_docx,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Błąd pandoc: {res.stderr}")


def main():
    parser = argparse.ArgumentParser(
        description="Konwertuje Markdown z wzorami LaTeX do formatu DOCX kompatybilnego z Google Docs."
    )
    parser.add_argument("input_md", help="Ścieżka do pliku wejściowego .md")
    parser.add_argument(
        "-o",
        "--output",
        dest="output_docx",
        help="Ścieżka do pliku wyjściowego .docx (domyślnie taka sama nazwa jak .md)",
    )
    parser.add_argument(
        "--gdrive",
        action="store_true",
        help="Kopiuje wygenerowany dokument .docx bezpośrednio do zsynchronizowanego katalogu Dysku Google",
    )
    parser.add_argument(
        "--gdrive-folder",
        dest="gdrive_folder",
        default="",
        help="Opcjonalny podkatalog w Dysku Google (np. 'Notatki/Matematyka')",
    )

    args = parser.parse_args()

    input_path = os.path.abspath(os.path.expanduser(args.input_md))
    if not os.path.isfile(input_path):
        print(f"❌ Błąd: Plik wejściowy nie istnieje: {input_path}", file=sys.stderr)
        sys.exit(1)

    if args.output_docx:
        output_path = os.path.abspath(os.path.expanduser(args.output_docx))
    else:
        output_path = os.path.splitext(input_path)[0] + ".docx"

    # Weryfikacja pandoc
    pandoc_bin = verify_pandoc()
    if not pandoc_bin:
        print(
            "❌ Błąd: Nie znaleziono narzędzia 'pandoc'. Zainstaluj je za pomocą:\n"
            "   brew install pandoc",
            file=sys.stderr,
        )
        sys.exit(1)

    # Upewnij się, że katalog docelowy istnieje
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"🔄 Konwertowanie: {input_path}")
    print(f"📄 Wyjście: {output_path}")

    try:
        convert_markdown_to_docx(input_path, output_path, pandoc_bin)
    except Exception as e:
        print(f"❌ Błąd podczas konwersji: {e}", file=sys.stderr)
        sys.exit(1)

    inline_count, block_count = count_omml_equations(output_path)
    print(f"✅ Sukces! Wygenerowano plik: {output_path}")
    print(f"   🧮 Wykryto formuły matematyczne OMML:")
    print(f"      - Równania blokowe (display math): {block_count}")
    print(f"      - Łącznie wyrażeń matematycznych: {inline_count}")

    # Obsługa Dysku Google
    if args.gdrive:
        gdrive_root = find_google_drive_path()
        if not gdrive_root:
            print(
                "⚠️ Ostrzeżenie: Nie wykryto zamontowanego Dysku Google w ~/Library/CloudStorage/.",
                file=sys.stderr,
            )
        else:
            target_dir = gdrive_root
            if args.gdrive_folder:
                target_dir = os.path.join(target_dir, args.gdrive_folder)
                os.makedirs(target_dir, exist_ok=True)

            gdrive_dest = os.path.join(target_dir, os.path.basename(output_path))
            shutil.copy2(output_path, gdrive_dest)
            print(f"☁️ Skopiowano na Dysk Google: {gdrive_dest}")
            print(
                "   Plik zostanie automatycznie zsynchronizowany i jest gotowy do otwarcia w Dokumentach Google!"
            )


if __name__ == "__main__":
    main()
