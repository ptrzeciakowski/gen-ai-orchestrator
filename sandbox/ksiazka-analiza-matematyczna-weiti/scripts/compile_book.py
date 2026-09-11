#!/usr/bin/env python3
"""
compile_book.py - Skrypt kompilacji podręcznika akademickiego do formatu DOCX / Google Docs
Automatycznie konwertuje rozdziały Markdown ze wzorami LaTeX na format Word/Google Docs
z zachowaniem natywnych równań OMML za pomocą silnika Pandoc.
"""

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
import zipfile

BOOK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BOOK_DIR, "dist")


def find_google_drive():
    candidates = glob.glob(
        os.path.expanduser(
            "~/Library/CloudStorage/GoogleDrive-*/Mój dysk"
        )
    ) + glob.glob(
        os.path.expanduser(
            "~/Library/CloudStorage/GoogleDrive-*/My Drive"
        )
    )
    return candidates[0] if candidates else None


def count_omml(docx_path):
    try:
        with zipfile.ZipFile(docx_path, "r") as z:
            xml = z.read("word/document.xml")
        root = ET.fromstring(xml)
        ns = {"m": "http://schemas.openxmlformats.org/officeDocument/2006/math"}
        return len(root.findall(".//m:oMath", ns)), len(
            root.findall(".//m:oMathPara", ns)
        )
    except Exception:
        return 0, 0


def compile_chapter(md_file, output_docx):
    os.makedirs(os.path.dirname(output_docx), exist_ok=True)
    cmd = [
        "pandoc",
        md_file,
        "-f",
        "markdown+tex_math_dollars+tex_math_single_backslash",
        "-t",
        "docx",
        "--toc",
        "--toc-depth=3",
        "-o",
        output_docx,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Błąd pandoc: {res.stderr}")
    return count_omml(output_docx)


def compile_full_book(output_docx):
    chapter_files = sorted(
        [
            f
            for f in os.listdir(BOOK_DIR)
            if re.match(r"^\d{2}-.*\.md$", f)
        ]
    )
    if not chapter_files:
        print("Nie znaleziono plików rozdziałów (np. 01-*.md).", file=sys.stderr)
        return

    merged_md = os.path.join(BOOK_DIR, "Analiza_Matematyczna_WEiTI_PW_Podrecznik.md")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(merged_md, "w", encoding="utf-8") as out:
        out.write(
            "# Analiza Matematyczna dla Informatyków i Elektroników\n"
            "## Podręcznik akademicki dla studentów Wydziału Elektroniki i Technik Informacyjnych Politechniki Warszawskiej (WEiTI PW)\n"
            "### Opracowany według kanonu dydaktycznego prof. W. Żakowskiego i doc. J. Decewicza\n\n"
            "---\n\n"
            "# TOM I: Funkcje Jednej Zmiennej, Szeregi i Rachunek Całkowy\n\n"
            "\\newpage\n\n"
        )
        for cf in chapter_files:
            num = int(cf[:2])
            if num == 9:
                out.write(
                    "\n\n---\n\n"
                    "# TOM II: Funkcje Wielu Zmiennych, Całki Wielokrotne, Analiza Wektorowa i Równania Różniczkowe\n\n"
                    "\\newpage\n\n"
                )
            cpath = os.path.join(BOOK_DIR, cf)
            with open(cpath, "r", encoding="utf-8") as f:
                content = f.read()
            out.write(content)
            out.write("\n\n\\newpage\n\n")

    print(f"Połączono {len(chapter_files)} rozdziałów do {merged_md}")
    inline, block = compile_chapter(merged_md, output_docx)
    print(f"Kompilacja całości zakończona: {output_docx}")
    print(f"Formuły OMML: {inline} (blokowe: {block})")


def main():
    parser = argparse.ArgumentParser(
        description="Kompilator podręcznika Analizy Matematycznej do DOCX / Google Docs"
    )
    parser.add_argument(
        "chapter",
        nargs="?",
        default=None,
        help="Plik konkretnego rozdziału (np. 01-fundamenty-analizy.md)",
    )
    parser.add_argument(
        "--all", action="store_true", help="Kompiluj wszystkie rozdziały do jednego tomu"
    )
    parser.add_argument(
        "--gdrive",
        action="store_true",
        help="Zsynchronizuj z Dyskiem Google",
    )
    args = parser.parse_args()

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    if args.all:
        target = os.path.join(
            OUTPUT_DIR, "Analiza_Matematyczna_WEiTI_PW_Podrecznik.docx"
        )
        compile_full_book(target)
    elif args.chapter:
        src = os.path.join(BOOK_DIR, args.chapter) if not os.path.isabs(args.chapter) else args.chapter
        base = os.path.splitext(os.path.basename(src))[0]
        target = os.path.join(OUTPUT_DIR, f"{base}.docx")
        inline, block = compile_chapter(src, target)
        print(f"Kompilacja rozdziału {src} -> {target}")
        print(f"Formuły OMML: {inline} (blokowe: {block})")
    else:
        parser.print_help()
        return

    if args.gdrive and os.path.exists(target):
        gdrive = find_google_drive()
        if gdrive:
            gdest = os.path.join(
                gdrive, "Analiza_Matematyczna_WEiTI", os.path.basename(target)
            )
            os.makedirs(os.path.dirname(gdest), exist_ok=True)
            shutil.copy2(target, gdest)
            print(f"☁️ Zsynchronizowano z Dyskiem Google: {gdest}")


if __name__ == "__main__":
    main()
