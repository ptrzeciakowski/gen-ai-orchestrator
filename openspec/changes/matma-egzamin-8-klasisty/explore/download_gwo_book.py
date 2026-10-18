#!/usr/bin/env python3
"""
Skrypt do pobierania podręczników z Multiteki GWO (multipodreczniki.apps.gwo.pl)
i bezstratnego składania ich w pojedynczy plik PDF (200 DPI, /DCTDecode).

Wymagania:
- Zalogowana sesja i otwarty podręcznik w przeglądarce Google Chrome (macOS).
  Skrypt automatycznie wyciąga aktualny token X-Authorization z bazy LocalStorage Chrome'a.

Użycie:
  python3 download_gwo_book.py
  python3 download_gwo_book.py --book-id 0533be48-b6cd-46e7-9225-69d5723e2b4a --delay 1.0 --out Matematyka-z-plusem-6-Podrecznik.pdf
"""

import argparse
import glob
import json
import os
import re
import struct
import subprocess
import sys
import time
import urllib.request

DEFAULT_BOOK_ID = "0533be48-b6cd-46e7-9225-69d5723e2b4a"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def detect_book_id_from_chrome():
    """Próbuje odczytać UUID aktualnie otwartego podręcznika z karty Google Chrome."""
    try:
        cmd = [
            "osascript",
            "-e",
            'tell application "Google Chrome" to repeat with w in windows\n'
            "  repeat with t in tabs of w\n"
            '    if URL of t contains "multipodreczniki.apps.gwo.pl/textbooks/" then return URL of t\n'
            "  end repeat\n"
            "end repeat",
        ]
        out = subprocess.check_output(cmd, stderr=subprocess.DEVNULL, text=True).strip()
        m = re.search(r"/textbooks/([0-9a-fA-F-]{36})", out)
        if m:
            return m.group(1)
    except Exception:
        pass
    return None


def get_latest_token():
    """Wyciąga najnowszy token autoryzacyjny GWO z plików LevelDB LocalStorage Google Chrome."""
    files = glob.glob(
        os.path.expanduser("~/Library/Application Support/Google/Chrome/*/Local Storage/leveldb/*")
    )
    files.sort(key=os.path.getmtime)
    latest_token = None
    for f in files:
        try:
            with open(f, "rb") as fp:
                data = fp.read()
            for m in re.finditer(
                rb"multipodreczniki\.apps\.gwo\.pl.{0,20}token.{0,10}([0-9a-f]{40})",
                data,
                re.DOTALL,
            ):
                latest_token = m.group(1).decode("ascii")
        except Exception:
            pass
    return latest_token


def api_get_json(url, token):
    req = urllib.request.Request(
        url,
        headers={
            "X-Authorization": token,
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
            ),
            "Referer": "https://multipodreczniki.apps.gwo.pl/",
            "Origin": "https://multipodreczniki.apps.gwo.pl",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def get_jpeg_dimensions(jpeg_bytes):
    """Odczytuje (width, height, components) z nagłówka SOF0/SOF1/SOF2 pliku JPEG."""
    i = 2
    n = len(jpeg_bytes)
    while i < n:
        while i < n and jpeg_bytes[i] != 0xFF:
            i += 1
        while i < n and jpeg_bytes[i] == 0xFF:
            i += 1
        if i >= n:
            break
        marker = jpeg_bytes[i]
        i += 1
        if marker in (0xD8, 0xD9) or (0xD0 <= marker <= 0xD7) or marker == 0x01:
            continue
        if i + 2 > n:
            break
        seg_len = struct.unpack(">H", jpeg_bytes[i : i + 2])[0]
        if marker in (0xC0, 0xC1, 0xC2):
            height, width = struct.unpack(">HH", jpeg_bytes[i + 3 : i + 7])
            components = jpeg_bytes[i + 7]
            return width, height, components
        i += seg_len
    raise ValueError("Nie udało się odczytać wymiarów obrazu JPEG.")


def build_pdf_from_jpegs(jpeg_paths, out_pdf_path):
    """Buduje bezstratny plik PDF osadzając surowe strumienie JPEG (/Filter /DCTDecode)."""
    objects = []

    def add_obj(content_bytes):
        objects.append(content_bytes)
        return len(objects)  # 1-based object ID

    catalog_id = add_obj(b"")
    pages_id = add_obj(b"")

    page_ids = []
    for p in jpeg_paths:
        with open(p, "rb") as f:
            jpg_data = f.read()
        w, h, comps = get_jpeg_dimensions(jpg_data)
        cs = b"/DeviceRGB" if comps == 3 else b"/DeviceGray"

        # Rozmiar strony w punktach PDF przy oryginalnym 200 DPI
        pt_w = round(w * 72.0 / 200.0, 2)
        pt_h = round(h * 72.0 / 200.0, 2)

        img_header = (
            f"<< /Type /XObject /Subtype /Image /Width {w} /Height {h} "
            f"/ColorSpace {cs.decode()} /BitsPerComponent 8 /Filter /DCTDecode "
            f"/Length {len(jpg_data)} >>\nstream\n"
        ).encode("ascii")
        img_obj_id = add_obj(img_header + jpg_data + b"\nendstream")

        content_stream = f"q {pt_w} 0 0 {pt_h} 0 0 cm /Im0 Do Q".encode("ascii")
        content_obj_id = add_obj(
            f"<< /Length {len(content_stream)} >>\nstream\n".encode("ascii")
            + content_stream
            + b"\nendstream"
        )

        page_obj_id = add_obj(
            f"<< /Type /Page /Parent {pages_id} 0 R "
            f"/MediaBox [0 0 {pt_w} {pt_h}] "
            f"/Resources << /XObject << /Im0 {img_obj_id} 0 R >> >> "
            f"/Contents {content_obj_id} 0 R >>".encode("ascii")
        )
        page_ids.append(page_obj_id)

    kids_str = " ".join(f"{pid} 0 R" for pid in page_ids)
    objects[pages_id - 1] = f"<< /Type /Pages /Kids [{kids_str}] /Count {len(page_ids)} >>".encode(
        "ascii"
    )
    objects[catalog_id - 1] = f"<< /Type /Catalog /Pages {pages_id} 0 R >>".encode("ascii")

    with open(out_pdf_path, "wb") as f:
        f.write(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = []
        for i, obj_bytes in enumerate(objects, start=1):
            offsets.append(f.tell())
            f.write(f"{i} 0 obj\n".encode("ascii"))
            f.write(obj_bytes)
            f.write(b"\nendobj\n")
        xref_offset = f.tell()
        f.write(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
        f.write(b"0000000000 65535 f \n")
        for off in offsets:
            f.write(f"{off:010d} 00000 n \n".encode("ascii"))
        f.write(
            f"trailer\n<< /Size {len(objects) + 1} /Root {catalog_id} 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF\n".encode("ascii")
        )


def slugify(text):
    text = text.strip().replace(" ", "-")
    return re.sub(r"[^a-zA-Z0-9ąćęłńóśźżĄĆĘŁŃÓŚŹŻ._-]", "", text)


def main():
    parser = argparse.ArgumentParser(description="Pobieranie podręcznika GWO do pliku PDF.")
    parser.add_argument(
        "--book-id",
        default=None,
        help="UUID podręcznika z URL-a (domyślnie wykrywa z otwartej karty Chrome lub używa Matematyki 6)",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.0,
        help="Odstęp w sekundach pomiędzy pobieraniem kolejnych stron (domyślnie: 1.0s)",
    )
    parser.add_argument(
        "--out",
        default=None,
        help="Ścieżka wyjściowego pliku PDF (domyślnie w katalogu skryptu na podstawie tytułu książki)",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Opcjonalny token X-Authorization (domyślnie odczytywany automatycznie z Chrome)",
    )
    args = parser.parse_args()

    book_id = args.book_id or detect_book_id_from_chrome() or DEFAULT_BOOK_ID
    token = args.token or get_latest_token()
    if not token:
        print("BŁĄD: Nie znaleziono tokenu w Google Chrome LocalStorage. Otwórz podręcznik w Chrome.")
        sys.exit(1)

    print(f"Book ID: {book_id}")
    meta_url = f"https://multipodreczniki.apps.gwo.pl/api/textbooks/{book_id}"
    meta = api_get_json(meta_url, token)["data"]
    title = meta.get("title", f"GWO-{book_id}")
    print(f"Tytuł: {title} (liczba stron: {meta.get('numberOfPages')})")

    out_pdf = args.out or os.path.join(SCRIPT_DIR, f"{slugify(title)}.pdf")
    img_dir = f"/tmp/gwo_pages_{book_id}"
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(out_pdf)), exist_ok=True)

    pages_url = f"https://multipodreczniki.apps.gwo.pl/api/textbooks/{book_id}/pages"
    pages = api_get_json(pages_url, token)["data"]
    pages.sort(key=lambda x: x["pageNumber"])

    # Zapisz również warstwę tekstową (textual-pages), jeśli jest dostępna
    try:
        textual_url = f"https://multipodreczniki.apps.gwo.pl/api/textbooks/{book_id}/textual-pages"
        textual_data = api_get_json(textual_url, token)
        textual_out = os.path.splitext(out_pdf)[0] + "-textual-pages.json"
        with open(textual_out, "w", encoding="utf-8") as tf:
            json.dump(textual_data, tf, ensure_ascii=False, indent=2)
        print(f"Zapisano warstwę tekstową do: {textual_out}")
    except Exception as e:
        print(f"Info: Nie udało się pobrać warstwy tekstowej: {e}")

    print(f"Rozpoczynam pobieranie {len(pages)} stron z opóźnieniem {args.delay}s...")
    sys.stdout.flush()

    jpeg_paths = []
    for idx, p in enumerate(pages):
        pnum = p["pageNumber"]
        res_id = p["jpegResourceId"]
        out_jpg = os.path.join(img_dir, f"page_{idx:03d}_{pnum}.jpg")
        jpeg_paths.append(out_jpg)

        if os.path.exists(out_jpg) and os.path.getsize(out_jpg) > 1000:
            continue

        url = f"https://multipodreczniki.apps.gwo.pl/api/resources/{res_id}"
        for attempt in range(3):
            try:
                req = urllib.request.Request(
                    url,
                    headers={
                        "X-Authorization": token,
                        "User-Agent": (
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
                        ),
                        "Referer": "https://multipodreczniki.apps.gwo.pl/",
                        "Origin": "https://multipodreczniki.apps.gwo.pl",
                    },
                )
                with urllib.request.urlopen(req, timeout=30) as resp:
                    data = resp.read()
                if len(data) < 1000:
                    raise ValueError(f"Plik zbyt mały ({len(data)} B)")
                with open(out_jpg, "wb") as out_f:
                    out_f.write(data)
                break
            except Exception as e:
                print(f"Próba {attempt + 1} nieudana dla strony {pnum}: {e}")
                sys.stdout.flush()
                token = get_latest_token() or token
                time.sleep(2.0)
        else:
            print(f"BŁĄD KRYTYCZNY: Nie udało się pobrać strony {pnum}")
            sys.exit(1)

        if (idx + 1) % 10 == 0 or idx == 0 or idx == len(pages) - 1:
            print(f"[{idx + 1}/{len(pages)}] Pobrano stronę {pnum} ({len(data) // 1024} KB)")
            sys.stdout.flush()

        time.sleep(args.delay)

    print("Składanie pliku PDF...")
    sys.stdout.flush()
    build_pdf_from_jpegs(jpeg_paths, out_pdf)
    size_mb = os.path.getsize(out_pdf) / (1024 * 1024)
    print(f"GOTOWE! Plik PDF zapisany w: {out_pdf} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
