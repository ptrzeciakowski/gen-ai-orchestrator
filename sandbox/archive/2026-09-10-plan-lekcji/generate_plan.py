#!/usr/bin/env python3
"""
Generator planu lekcji (Timeline View & A4 Print)
Konwertuje pliki Markdown z tabelą planu lekcji do formatu HTML i PDF (1 strona A4).
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path


def parse_time_range(text: str):
    """
    Ekstraktuje (start_h, start_m, end_h, end_m, duration_m) z tekstu np. '08:00 - 08:45'
    """
    m = re.search(r"(\d{1,2})[:.](\d{2})\s*[-–—]\s*(\d{1,2})[:.](\d{2})", text)
    if not m:
        return None
    h1, m1, h2, m2 = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4))
    start_total = h1 * 60 + m1
    end_total = h2 * 60 + m2
    duration = end_total - start_total
    return h1, m1, h2, m2, duration


def classify_subject(name: str) -> str:
    """
    Automatyczna klasyfikacja przedmiotu do klasy CSS na podstawie nazwy.
    """
    s = name.lower()
    if any(k in s for k in ["odwołan", "odwolane", "cancelled", "anulowan", "szar", "muted"]):
        return "muted"
    if any(k in s for k in ["obiad", "lunch"]):
        return "lunch"
    if any(k in s for k in ["w domu", "domowe", "home"]):
        return "home"
    if any(k in s for k in ["early stage"]):
        return "es"
    if any(k in s for k in ["terapeutyczn", "psycholog", "rewalidacj", "pedagog"]):
        return "therapy"
    if any(k in s for k in ["fizyczne", "wf", "sportow", "trening", "tenis", "basen", "pływani"]):
        return "sport"
    return "general"


def parse_markdown_plan(md_path: Path):
    """
    Parsuje plik Markdown zawierający tytuł i tabelę z planem lekcji.
    Zwraca: (title, lessons, max_hour)
    """
    content = md_path.read_text(encoding="utf-8")
    lines = [line.strip() for line in content.splitlines()]

    # Wykryj tytuł z pierwszego nagłówka #
    title = md_path.stem.replace("-", " ").title()
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    # Dni tygodnia i mapowanie kolumn
    days_map = {
        "poniedziałek": 2,
        "wtorek": 3,
        "środa": 4,
        "czwartek": 5,
        "piątek": 6,
    }

    table_lines = [l for l in lines if l.startswith("|") and l.endswith("|")]
    if not table_lines:
        raise ValueError(f"Nie znaleziono tabeli Markdown w pliku {md_path}")

    # Znajdź nagłówek tabeli
    header_idx = -1
    col_day_mapping = {}
    for idx, line in enumerate(table_lines):
        raw_cells = [c.strip().lower() for c in line.split("|")[1:-1]]
        matched_days = False
        for c_idx, cell in enumerate(raw_cells):
            for day_name, col_num in days_map.items():
                if day_name in cell:
                    col_day_mapping[c_idx] = col_num
                    matched_days = True
        if matched_days:
            header_idx = idx
            break

    if header_idx == -1:
        # Domyślny układ: kolumna 0 = Godziny, 1 = Poniedziałek ... 5 = Piątek
        col_day_mapping = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
        header_idx = 0

    lessons = []
    max_end_minutes = 18 * 60  # domyślnie min. do 18:00

    # Przetwarzaj rzędy tabeli
    for line in table_lines[header_idx + 1 :]:
        # Pomiń linię podziału | :--- | :--- |
        if re.search(r"^\|(\s*:?-+:?\s*\|)+$", line):
            continue

        raw_cells = [c.strip() for c in line.split("|")[1:-1]]
        if not raw_cells:
            continue

        # Czas domyślny z pierwszej kolumny (np. 08:00 - 08:45)
        row_time_raw = raw_cells[0]
        row_time = parse_time_range(row_time_raw)

        for c_idx, cell_text in enumerate(raw_cells[1:], start=1):
            if not cell_text or cell_text == "-" or cell_text == "—":
                continue
            if c_idx not in col_day_mapping:
                continue

            col_num = col_day_mapping[c_idx]

            # Sprawdź czy komórka ma własne godziny np. (16:30 - 18:00)
            cell_time = parse_time_range(cell_text)
            lesson_time = cell_time if cell_time else row_time

            if not lesson_time:
                continue

            h1, m1, h2, m2, duration = lesson_time

            # Usuń zapis godzin z tekstu komórki
            clean_name = re.sub(
                r"\(?\s*\d{1,2}[:.]\d{2}\s*[-–—]\s*\d{1,2}[:.]\d{2}\s*\)?", "", cell_text
            ).strip()

            # Sprawdź czy jest ręczny tag stylu np. [sport], [lunch]
            explicit_tag = None
            tag_match = re.search(r"\[([a-zA-Z0-9_-]+)\]", clean_name)
            if tag_match:
                explicit_tag = tag_match.group(1)
                clean_name = re.sub(r"\[([a-zA-Z0-9_-]+)\]", "", clean_name).strip()

            cls = explicit_tag if explicit_tag else classify_subject(clean_name)
            time_display = f"{h1}:{m1:02d}-{h2}:{m2:02d}"

            end_total = h2 * 60 + m2
            if end_total > max_end_minutes:
                max_end_minutes = end_total

            lessons.append(
                {
                    "col": col_num,
                    "h": h1,
                    "m": m1,
                    "d": duration,
                    "name": clean_name,
                    "time_display": time_display,
                    "class": cls,
                }
            )

    # Oblicz maksymalną pełną godzinę dla siatki (np. 18:30 -> 19:00)
    max_hour = (max_end_minutes + 59) // 60
    if max_hour < 18:
        max_hour = 18

    return title, lessons, max_hour


def generate_html(title: str, lessons: list, max_hour: int = 19) -> str:
    """
    Generuje kompletny kod HTML zoptymalizowany pod pojedynczą stronę A4.
    """
    min_hour = 8
    total_hours = max_hour - min_hour
    intervals = total_hours * 12

    # Generuj etykiety czasu i linie siatki
    time_labels_html = []
    for h in range(min_hour, max_hour + 1):
        row_idx = (h - min_hour) * 12 + 3
        time_labels_html.append(
            f'        <div class="time-label" style="grid-row: {row_idx};">{h}:00</div><div class="grid-line" style="grid-row: {row_idx};"></div>'
        )

    # Sortuj i generuj lekcje
    lessons_by_day = {2: "PONIEDZIAŁEK", 3: "WTOREK", 4: "ŚRODA", 5: "CZWARTEK", 6: "PIĄTEK"}
    lessons_html = []

    for col, day_name in lessons_by_day.items():
        day_lessons = [l for l in lessons if l["col"] == col]
        day_lessons.sort(key=lambda x: (x["h"], x["m"]))

        lessons_html.append(f"\n        <!-- ==================== {day_name} (--col: {col}) ==================== -->")
        for l in day_lessons:
            lessons_html.append(
                f'        <div class="lesson {l["class"]}" style="--col: {l["col"]}; --h: {l["h"]}; --m: {l["m"]}; --d: {l["d"]};">{l["name"]} <span class="time">{l["time_display"]}</span></div>'
            )

    time_labels_str = "\n".join(time_labels_html)
    lessons_str = "\n".join(lessons_html)

    html_template = f"""<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        :root {{
            /* 1 interwał (5 min) = 6px wysokości (idealne dopasowanie do pojedynczej strony A4) */
            --grid-scale: 6px; 
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f8fafc;
            padding: 16px;
            color: #334155;
            margin: 0;
        }}

        .actions {{
            text-align: center;
            margin-bottom: 12px;
        }}

        .btn-print {{
            background-color: #2563eb;
            color: #ffffff;
            border: none;
            padding: 8px 18px;
            font-size: 13px;
            font-weight: 600;
            border-radius: 6px;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(37, 99, 235, 0.2);
            transition: background-color 0.15s ease, transform 0.1s ease;
        }}

        .btn-print:hover {{
            background-color: #1d4ed8;
            transform: translateY(-1px);
        }}

        h2 {{
            text-align: center;
            color: #1e293b;
            margin: 0 0 10px 0;
            font-size: 20px;
        }}

        .calendar {{
            display: grid;
            /* Kolumny: 1 dla godzin, 5 dla dni roboczych */
            grid-template-columns: 65px repeat(5, 1fr);
            /* Rzędy: Nagłówek (38px) + odstęp nad 8:00 (14px) + {intervals} interwałów 5-minutowych (od 8:00 do {max_hour}:00) + odstęp pod {max_hour}:00 (14px) */
            grid-template-rows: 38px 14px repeat({intervals}, var(--grid-scale)) 14px;
            gap: 1px;
            background-color: #e2e8f0;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
            max-width: 1050px;
            margin: 0 auto;
            page-break-inside: avoid;
            break-inside: avoid;
        }}

        .header {{
            background-color: #ffffff;
            font-weight: 600;
            font-size: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 2px solid #cbd5e1;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        /* Linie siatki godzin w tle */
        .grid-line {{
            grid-column: 2 / -1;
            border-top: 1px dashed #cbd5e1;
            z-index: 1;
        }}

        /* Etykiety czasu po lewej stronie */
        .time-label {{
            grid-column: 1;
            font-size: 12px;
            color: #64748b;
            text-align: right;
            padding-right: 12px;
            transform: translateY(-50%); 
            z-index: 2;
        }}

        /* Główna logika pozycjonowania lekcji */
        .lesson {{
            /* (Godzina - 8) * 12 interwałów na godzinę + minuty/5 + 3 (korekta na nagłówek i odstęp) */
            grid-row-start: calc( ((var(--h) - 8) * 12) + (var(--m) / 5) + 3 );
            grid-row-end: span calc(var(--d) / 5);
            grid-column: var(--col);

            margin: 2px 3px;
            border-radius: 6px;
            padding: 3px 4px;
            font-size: 12px;
            font-weight: 500;
            color: #fff;
            box-shadow: 0 2px 4px rgba(0,0,0,0.08);
            z-index: 10;
            
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            line-height: 1.18;
            transition: transform 0.15s ease;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        .lesson:hover {{
            transform: scale(1.03);
            z-index: 20;
        }}

        .lesson .time {{
            font-size: 10px;
            opacity: 0.92;
            margin-top: 3px;
            font-weight: 400;
        }}

        /* Kolorystyka przedmiotów */
        .general {{ background-color: #3b82f6; }} /* Domyślny niebieski */
        .sport {{ background-color: #14b8a6; }}   /* WF / Szkolenie sportowe - Morski */
        .therapy {{ background-color: #8b5cf6; }} /* Zajęcia terapeutyczne - Fioletowy */
        .es {{ background-color: #f59e0b; }}      /* Szkoła językowa / Early Stage - Bursztynowy */
        .lunch {{ background-color: #ea580c; }}   /* Blok obiadowy - Ciepły pomarańcz */
        .home {{ background-color: #6366f1; }}    /* Zajęcia w domu - Indygo */
        .muted, .cancelled, .gray {{ background-color: #94a3b8; opacity: 0.9; }} /* Wyszarzone / opcjonalne / odwołane - Szary */

        /* Druk na A4 */
        @page {{
            size: A4 portrait;
            margin: 8mm;
        }}

        @media print {{
            body {{
                background-color: #ffffff;
                padding: 0;
            }}
            .no-print {{
                display: none !important;
            }}
            h2 {{
                margin: 0 0 8px 0;
                font-size: 18px;
            }}
            .calendar {{
                box-shadow: none;
                max-width: 100%;
                border-color: #cbd5e1;
            }}
            .lesson {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>

    <div class="actions no-print">
        <button onclick="window.print()" class="btn-print">🖨️ Drukuj plan lekcji (A4)</button>
    </div>
    <h2>{title}</h2>

    <div class="calendar">
        <!-- Nagłówki -->
        <div class="header" style="grid-column: 1; grid-row: 1;">Godzina</div>
        <div class="header" style="grid-column: 2; grid-row: 1;">Poniedziałek</div>
        <div class="header" style="grid-column: 3; grid-row: 1;">Wtorek</div>
        <div class="header" style="grid-column: 4; grid-row: 1;">Środa</div>
        <div class="header" style="grid-column: 5; grid-row: 1;">Czwartek</div>
        <div class="header" style="grid-column: 6; grid-row: 1;">Piątek</div>

        <!-- Oś czasu -->
{time_labels_str}
{lessons_str}
    </div>
</body>
</html>
"""
    return html_template


def compile_pdf(html_path: Path, pdf_path: Path):
    """
    Kompiluje plik HTML do PDF za pomocą headless Google Chrome i sprawdza liczbę stron.
    """
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]
    chrome_bin = next((p for p in chrome_paths if os.path.exists(p)), None)
    if not chrome_bin:
        print("Ostrzeżenie: Nie znaleziono Google Chrome, pomijanie generowania PDF.")
        return False

    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path.resolve()}",
        f"file://{html_path.resolve()}",
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Błąd kompilacji PDF: {res.stderr}")
        return False

    # Weryfikacja liczby stron
    try:
        data = pdf_path.read_bytes()
        pages = re.findall(rb"/Type\s*/Page[^s]", data)
        page_count = len(pages)
        if page_count == 1:
            print(f"✅ PDF wygenerowany pomyślnie: {pdf_path} (dokładnie 1 strona A4)")
        else:
            print(f"⚠️ Ostrzeżenie: Wygenerowany PDF ma {page_count} stron! Powinna być dokładnie 1.")
    except Exception as e:
        print(f"Nie udało się zweryfikować liczby stron PDF: {e}")

    return True


def process_file(md_file: Path, no_pdf: bool = False):
    """
    Przetwarza pojedynczy plik Markdown na HTML i PDF.
    """
    print(f"--- Przetwarzanie: {md_file} ---")
    title, lessons, max_hour = parse_markdown_plan(md_file)
    print(f"Tytuł: '{title}', liczba lekcji: {len(lessons)}, zakres osi: 8:00 - {max_hour}:00")

    html_content = generate_html(title, lessons, max_hour)
    html_path = md_file.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")
    print(f"✅ HTML zapisany: {html_path}")

    if not no_pdf:
        pdf_path = md_file.with_suffix(".pdf")
        compile_pdf(html_path, pdf_path)


def main():
    parser = argparse.ArgumentParser(description="Kompiluj plik Markdown z planem lekcji do HTML i PDF A4")
    parser.add_argument("markdown_files", nargs="*", type=str, help="Pliki Markdown do skompilowania")
    parser.add_argument("--all", action="store_true", help="Kompiluj wszystkie pliki *-plan-lekcji.md w bieżącym katalogu")
    parser.add_argument("--no-pdf", action="store_true", help="Nie generuj plików PDF")

    args = parser.parse_args()

    files_to_process = []
    if args.all or not args.markdown_files:
        files_to_process = list(Path(".").glob("*-plan-lekcji.md"))
        if not files_to_process and not args.all:
            parser.print_help()
            sys.exit(1)
    else:
        for f in args.markdown_files:
            p = Path(f)
            if p.exists():
                files_to_process.append(p)
            else:
                print(f"Błąd: Plik nie istnieje: {f}")

    if not files_to_process:
        print("Brak plików do przetworzenia.")
        sys.exit(0)

    for md_file in files_to_process:
        process_file(md_file, no_pdf=args.no_pdf)


if __name__ == "__main__":
    main()
