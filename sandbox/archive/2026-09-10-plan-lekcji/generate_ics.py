#!/usr/bin/env python3
"""
Generator plików iCalendar (.ics) dla osobnych kalendarzy Michała i Nadii.
Zgodny ze standardem RFC 5545, zoptymalizowany pod kątem Kalendarza Google.
"""

import hashlib
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

TIMEZONE_DEF = """BEGIN:VTIMEZONE
TZID:Europe/Warsaw
X-LIC-LOCATION:Europe/Warsaw
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE"""

# Daty pierwszych wystąpień w roku szkolnym 2026/2027 (początek września 2026)
FIRST_DATES = {
    2: "20260907",  # Poniedziałek
    3: "20260901",  # Wtorek (1 września)
    4: "20260902",  # Środa
    5: "20260903",  # Czwartek
    6: "20260904",  # Piątek
}

DAY_NAMES = {
    2: "Poniedziałek",
    3: "Wtorek",
    4: "Środa",
    5: "Czwartek",
    6: "Piątek",
}

UNTIL_DATE = "20270626T000000Z"  # Koniec roku szkolnego (ostatni piątek to 25.06.2027)


def parse_html_lessons(html_path: Path):
    html = html_path.read_text(encoding="utf-8")
    pattern = re.compile(
        r'<div class="lesson\s*([^"]*)"[^>]*style="[^"]*--col:\s*(\d+)[^>]*--h:\s*(\d+)[^>]*--m:\s*(\d+)[^>]*--d:\s*(\d+)[^"]*">([^<]+)<span class="time">([^<]+)</span>',
        re.DOTALL,
    )
    lessons = []
    for css_class, col, h, m, d, name, time_str in pattern.findall(html):
        name = name.strip()
        lessons.append(
            {
                "css_class": css_class.strip(),
                "col": int(col),
                "h": int(h),
                "m": int(m),
                "d": int(d),
                "name": name,
                "time_str": time_str.strip(),
                "is_lunch": "lunch" in css_class or "obiad" in name.lower(),
            }
        )
    return lessons


def classify_category(name: str) -> str:
    s = name.lower()
    if "obiad" in s:
        return "Obiad"
    if "tenis" in s:
        return "Trening tenisowy"
    if "early stage" in s or "native speaker" in s or "angielski" in s or "hiszpański" in s:
        return "Języki obce"
    if "terapeutyczn" in s or "psycholog" in s or "rewalidacj" in s:
        return "Zajęcia terapeutyczne"
    if any(k in s for k in ["fizyczne", "wf", "sportow", "trening"]):
        return "Sport"
    return "Szkoła"


def generate_ics(lessons, person_name: str, include_lunch: bool, use_prefix: bool, cal_name: str) -> str:
    now_utc = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Antigravity//Plan Lekcji//PL",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{cal_name}",
        "X-WR-TIMEZONE:Europe/Warsaw",
        TIMEZONE_DEF,
    ]

    for item in lessons:
        if not include_lunch and item["is_lunch"]:
            continue

        col = item["col"]
        first_date = FIRST_DATES.get(col, "20260907")
        start_h = item["h"]
        start_m = item["m"]
        duration = item["d"]

        start_min_total = start_h * 60 + start_m
        end_min_total = start_min_total + duration
        end_h = end_min_total // 60
        end_m = end_min_total % 60

        dtstart = f"{first_date}T{start_h:02d}{start_m:02d}00"
        dtend = f"{first_date}T{end_h:02d}{end_m:02d}00"

        prefix = f"{person_name}: " if use_prefix else ""
        summary = f"{prefix}{item['name']}"
        category = classify_category(item["name"])

        # Generuj stabilny, unikalny UID
        prefix_flag = "p" if use_prefix else "np"
        uid_raw = f"{person_name}-{prefix_flag}-{col}-{start_h:02d}{start_m:02d}-{item['name']}"
        uid_hash = hashlib.md5(uid_raw.encode("utf-8")).hexdigest()[:12]
        uid = f"{uid_hash}-{col}-{start_h:02d}{start_m:02d}@planlekcji"

        lines.extend(
            [
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{now_utc}",
                f"DTSTART;TZID=Europe/Warsaw:{dtstart}",
                f"DTEND;TZID=Europe/Warsaw:{dtend}",
                f"RRULE:FREQ=WEEKLY;UNTIL={UNTIL_DATE}",
                f"SUMMARY:{summary}",
                f"DESCRIPTION:Zajęcia: {item['name']}\\nGodziny: {item['time_str']}\\nDzień: {DAY_NAMES.get(col, '')}\\nUczeń: {person_name}",
                f"CATEGORIES:{category}",
                "STATUS:CONFIRMED",
                "TRANSP:OPAQUE",
                "END:VEVENT",
            ]
        )

    lines.append("END:VCALENDAR")
    return "\r\n".join(lines) + "\r\n"


def main():
    base_dir = Path("/Users/pawel/git/gen-ai-orchestrator/sandbox/archive/2026-09-10-plan-lekcji")
    downloads_dir = Path("/Users/pawel/Downloads")

    # ================= 1. MICHAŁ =================
    html_michal = base_dir / "michal-plan-lekcji.html"
    lessons_m = parse_html_lessons(html_michal)
    print(f"Załadowano {len(lessons_m)} pozycji z planu Michała.")

    # A) Wersja czysta (BEZ prefiksu 'Michał: ') - domyślna do dedykowanego kalendarza Michała
    ics_m_clean = generate_ics(
        lessons_m,
        person_name="Michał",
        include_lunch=False,
        use_prefix=False,
        cal_name="Michał - plan lekcji",
    )
    p_m_clean = base_dir / "michal-plan-lekcji.ics"
    p_m_clean.write_text(ics_m_clean, encoding="utf-8")
    shutil.copy(p_m_clean, downloads_dir / "michal-plan-lekcji.ics")
    print(f"Zapisano czysty plan Michała: {p_m_clean} -> Downloads/michal-plan-lekcji.ics (37 zdarzeń cyklicznych)")

    # B) Wersja z prefiksem 'Michał: '
    ics_m_pref = generate_ics(
        lessons_m,
        person_name="Michał",
        include_lunch=False,
        use_prefix=True,
        cal_name="Michał - plan lekcji",
    )
    p_m_pref = base_dir / "michal-plan-lekcji-z-prefiksem.ics"
    p_m_pref.write_text(ics_m_pref, encoding="utf-8")

    # C) Wersja z obiadami
    ics_m_lunch = generate_ics(
        lessons_m,
        person_name="Michał",
        include_lunch=True,
        use_prefix=False,
        cal_name="Michał - plan lekcji (z obiadami)",
    )
    p_m_lunch = base_dir / "michal-plan-lekcji-z-obiadami.ics"
    p_m_lunch.write_text(ics_m_lunch, encoding="utf-8")

    # ================= 2. NADIA =================
    html_nadia = base_dir / "nadia-plan-lekcji.html"
    lessons_n = parse_html_lessons(html_nadia)
    print(f"Załadowano {len(lessons_n)} pozycji z planu Nadii.")

    # A) Wersja czysta (BEZ prefiksu 'Nadia: ') - domyślna do dedykowanego kalendarza Nadii
    ics_n_clean = generate_ics(
        lessons_n,
        person_name="Nadia",
        include_lunch=False,
        use_prefix=False,
        cal_name="Nadia - plan lekcji",
    )
    p_n_clean = base_dir / "nadia-plan-lekcji.ics"
    p_n_clean.write_text(ics_n_clean, encoding="utf-8")
    shutil.copy(p_n_clean, downloads_dir / "nadia-plan-lekcji.ics")
    print(f"Zapisano czysty plan Nadii: {p_n_clean} -> Downloads/nadia-plan-lekcji.ics (40 zdarzeń cyklicznych)")

    # B) Wersja z prefiksem 'Nadia: '
    ics_n_pref = generate_ics(
        lessons_n,
        person_name="Nadia",
        include_lunch=False,
        use_prefix=True,
        cal_name="Nadia - plan lekcji",
    )
    p_n_pref = base_dir / "nadia-plan-lekcji-z-prefiksem.ics"
    p_n_pref.write_text(ics_n_pref, encoding="utf-8")

    # C) Wersja z obiadami
    ics_n_lunch = generate_ics(
        lessons_n,
        person_name="Nadia",
        include_lunch=True,
        use_prefix=False,
        cal_name="Nadia - plan lekcji (z obiadami)",
    )
    p_n_lunch = base_dir / "nadia-plan-lekcji-z-obiadami.ics"
    p_n_lunch.write_text(ics_n_lunch, encoding="utf-8")

    print("\nGotowe! Obie wersje .ics zostały przygotowane i skopiowane do folderu Pobrane.")


if __name__ == "__main__":
    main()
