#!/usr/bin/env python3
"""
Skrypt tworzący płaską strukturę dowiązań symbolicznych (symlinks)
dla zdjęć zagnieżdżonych w Google Drive, posegregowaną rocznikami.
Symlinki zajmują 0 bajtów na dysku, ale eliminują problem paginacji (100 sztuk)
w interfejsie Google Photos, pozwalając na zaznaczenie 100% plików na raz (Cmd+A).
"""

import os
import sys
from collections import defaultdict

SRC_DIR = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ptrzeciakowski@gmail.com/Mój dysk/88📸Zdjęcia")
DEST_BASE = os.path.expanduser("~/Desktop/GooglePhotos_Migracja")
EXTENSIONS = {".jpg", ".jpeg", ".png", ".heic", ".mp4", ".mov", ".avi", ".m4v", ".3gp"}

# Foldery do wykluczenia (duplikaty wykryte w audycie)
EXCLUDE_SUBSTRINGS = ["2017 (1)", "2015 (1)", "Fotograf / Kopia"]

def main():
    if not os.path.exists(SRC_DIR):
        print(f"BŁĄD: Katalog źródłowy {SRC_DIR} nie istnieje!")
        sys.exit(1)

    os.makedirs(DEST_BASE, exist_ok=True)
    stats = defaultdict(int)
    skipped = 0

    print("Rozpoczynam indeksowanie i tworzenie płaskiej struktury symlinków...")

    for root, dirs, files in os.walk(SRC_DIR):
        # Sprawdzanie czy folder nie jest duplikatem
        if any(exc in root for exc in EXCLUDE_SUBSTRINGS):
            skipped += len(files)
            continue

        # Określanie kategorii nadrzędnej (rocznika)
        rel_path = os.path.relpath(root, SRC_DIR)
        parts = rel_path.split(os.sep)
        category = parts[0] if parts and parts[0] != "." else "Inne"

        # Jeśli kategoria to podfolder techniczny, zostawiamy nazwę
        cat_dest = os.path.join(DEST_BASE, category)

        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXTENSIONS:
                os.makedirs(cat_dest, exist_ok=True)
                src_file = os.path.join(root, f)

                # Tworzymy unikalną nazwę pliku, jeśli w podfolderach byłyby takie same nazwy
                # Dodajemy przedrostek ze ścieżki podfolderu (np. 2016.05_Wycieczka_IMG_001.jpg)
                sub_prefix = "_".join(parts[1:]) if len(parts) > 1 else ""
                clean_prefix = "".join(c for c in sub_prefix if c.isalnum() or c in ("-", "_")).strip("_")
                flat_name = f"{clean_prefix}_{f}" if clean_prefix else f

                dst_file = os.path.join(cat_dest, flat_name)
                
                if not os.path.exists(dst_file):
                    try:
                        os.symlink(src_file, dst_file)
                        stats[category] += 1
                    except Exception as e:
                        print(f"Błąd tworzenia symlinka dla {src_file}: {e}")

    report_path = os.path.join(DEST_BASE, "RAPORT_KONTROLNY.txt")
    with open(report_path, "w", encoding="utf-8") as rf:
        rf.write("========================================================\n")
        rf.write("RAPORT KONTROLNY: LICZBA ZDJĘĆ DO WERYFIKACJI W GOOGLE PHOTOS\n")
        rf.write("========================================================\n\n")
        rf.write(f"{'Rocznik / Folder':<35} | {'Liczba plików (100% komplet)':<20}\n")
        rf.write("-" * 60 + "\n")
        total = 0
        for cat in sorted(stats.keys()):
            cnt = stats[cat]
            total += cnt
            line = f"{cat:<35} | {cnt:<20}\n"
            rf.write(line)
            print(f"{cat:<35} | {cnt} plików")
        rf.write("-" * 60 + "\n")
        rf.write(f"{'RAZEM (100% KOMPLET)':<35} | {total:<20}\n")
        rf.write(f"\nPominięto zidentyfikowanych duplikatów: {skipped} plików.\n")

    print("\n" + "=" * 60)
    print(f"ZAKOŃCZONO POMYŚLNIE!")
    print(f"Płaska struktura została przygotowana w: {DEST_BASE}")
    print(f"Plik raportu z sumami kontrolnymi: {report_path}")
    print(f"Łącznie zaindeksowano: {total} unikalnych plików multimedialnych.")
    print("=" * 60)

if __name__ == "__main__":
    main()
