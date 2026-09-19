import sqlite3
import os
import json
from datetime import datetime
from collections import defaultdict, Counter

DB_PATH = "/Users/pawel/Library/Application Support/Google/DriveFS/113301283206781212965/metadata_sqlite_db"

def format_size(s):
    if s is None:
        return "0 B"
    for u in ["B", "KB", "MB", "GB"]:
        if s < 1024:
            return f"{s:.1f} {u}"
        s /= 1024
    return f"{s:.1f} TB"

def format_ts(ts):
    if not ts or ts <= 0:
        return "NIGDY"
    try:
        dt = datetime.fromtimestamp(ts / 1000)
        return dt.strftime("%Y-%m-%d %H:%M")
    except Exception:
        return str(ts)

def main():
    conn = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    conn.text_factory = bytes
    c = conn.cursor()

    c.execute("""
        SELECT i.stable_id, i.id, i.local_title, i.is_folder, i.mime_type, i.file_size,
               i.is_owner, i.trashed, i.starred, i.modified_date, i.shared_with_me_date,
               i.viewed_by_me_date, p.parent_stable_id
        FROM items i
        LEFT JOIN stable_parents p ON i.stable_id = p.item_stable_id
        WHERE i.is_tombstone = 0
    """)
    rows = c.fetchall()
    print(f"Total rows in DB (excluding tombstones): {len(rows)}")

    items = {}
    children = defaultdict(list)
    parent_map = {}

    for r in rows:
        sid, item_id, title_b, is_f, mime_b, size, is_own, trashed, starred, mdate, sdate, vdate, parent_sid = r
        title = title_b.decode("utf-8", "ignore") if title_b else ""
        mime = mime_b.decode("utf-8", "ignore") if mime_b else ""
        iid = item_id.decode("utf-8", "ignore") if item_id else ""
        items[sid] = {
            "sid": sid,
            "id": iid,
            "title": title,
            "is_folder": bool(is_f),
            "mime": mime,
            "size": size or 0,
            "is_owner": bool(is_own),
            "trashed": bool(trashed),
            "starred": bool(starred),
            "mdate": mdate or 0,
            "sdate": sdate or 0,
            "vdate": vdate or 0,
            "parent_sid": parent_sid
        }
        if parent_sid is not None:
            children[parent_sid].append(sid)
            parent_map[sid] = parent_sid

    root_sid = 101 # "Mój dysk"

    def get_path(sid):
        curr = sid
        parts = []
        visited = set()
        while curr in items and curr not in visited:
            visited.add(curr)
            parts.append(items[curr]["title"])
            curr = parent_map.get(curr)
            if curr == root_sid:
                parts.append("Mój dysk")
                break
        parts.reverse()
        return " / ".join(parts)

    def get_subtree_stats(sid):
        total_files = 0
        total_folders = 0
        total_size = 0
        max_vdate = 0
        max_mdate = 0
        min_vdate = float('inf')
        never_opened = 0
        mime_counts = Counter()
        stack = [sid]
        while stack:
            curr = stack.pop()
            for ch_sid in children.get(curr, []):
                ch = items.get(ch_sid)
                if not ch or ch["trashed"]:
                    continue
                if ch["is_folder"]:
                    total_folders += 1
                    stack.append(ch_sid)
                else:
                    total_files += 1
                    total_size += ch["size"]
                    mime_counts[ch["mime"]] += 1
                    if ch["vdate"] > max_vdate:
                        max_vdate = ch["vdate"]
                    if ch["mdate"] > max_mdate:
                        max_mdate = ch["mdate"]
                    if ch["vdate"] > 0 and ch["vdate"] < min_vdate:
                        min_vdate = ch["vdate"]
                    elif ch["vdate"] == 0:
                        never_opened += 1
        if min_vdate == float('inf'):
            min_vdate = 0
        return {
            "files": total_files,
            "folders": total_folders,
            "size": total_size,
            "max_vdate": max_vdate,
            "max_mdate": max_mdate,
            "never_opened": never_opened,
            "top_mimes": mime_counts.most_common(3)
        }

    # Analyze root items
    root_children_sids = children.get(root_sid, [])
    top_items = [items[sid] for sid in root_children_sids if sid in items and not items[sid]["trashed"]]

    folders = [it for it in top_items if it["is_folder"]]
    root_files = [it for it in top_items if not it["is_folder"]]

    folders.sort(key=lambda x: x["title"])
    root_files.sort(key=lambda x: x["title"])

    print("\n" + "="*80)
    print(f"FOLDERÓW GŁÓWNYCH: {len(folders)} | PLIKÓW LUZEM W ROOT: {len(root_files)}")
    print("="*80)

    folder_summaries = []
    for f in folders:
        stats = get_subtree_stats(f["sid"])
        summary = {
            "title": f["title"],
            "id": f["id"],
            "files": stats["files"],
            "folders": stats["folders"],
            "size": stats["size"],
            "size_str": format_size(stats["size"]),
            "last_viewed": format_ts(stats["max_vdate"]),
            "last_modified": format_ts(stats["max_mdate"]),
            "never_opened_files": stats["never_opened"],
            "top_mimes": stats["top_mimes"]
        }
        folder_summaries.append(summary)
        print(f"DIR: {summary['title']:<38} | Pliki: {summary['files']:<6} | Rozmiar: {summary['size_str']:<9} | Max Otwarty: {summary['last_viewed']}")

    print("\n" + "="*80)
    print("PLIKI W ROOT (MÓJ DYSK):")
    print("="*80)
    root_file_summaries = []
    for rf in root_files:
        r_sum = {
            "title": rf["title"],
            "id": rf["id"],
            "size": rf["size"],
            "size_str": format_size(rf["size"]),
            "mime": rf["mime"],
            "is_owner": rf["is_owner"],
            "last_viewed": format_ts(rf["vdate"]),
            "last_modified": format_ts(rf["mdate"])
        }
        root_file_summaries.append(r_sum)
        print(f"FILE: {r_sum['title']:<45} | {r_sum['size_str']:<9} | Otwarty: {r_sum['last_viewed']:<16} | Zmodyf: {r_sum['last_modified']}")

    # Ownership and sharing analysis across entire Drive
    total_active_files = sum(1 for it in items.values() if not it["is_folder"] and not it["trashed"])
    total_active_folders = sum(1 for it in items.values() if it["is_folder"] and not it["trashed"])
    owned_files = sum(1 for it in items.values() if not it["is_folder"] and not it["trashed"] and it["is_owner"])
    shared_with_me = sum(1 for it in items.values() if not it["is_folder"] and not it["trashed"] and not it["is_owner"])
    starred_count = sum(1 for it in items.values() if not it["trashed"] and it["starred"])
    trashed_count = sum(1 for it in items.values() if it["trashed"])

    # Global recency distribution
    now_ms = 1789800000000 # ~2026
    # Let's inspect real max timestamps in DB
    max_db_ts = max(it["mdate"] for it in items.values())
    print(f"\nMax modified ts in DB: {max_db_ts} ({format_ts(max_db_ts)})")

    # Group files by viewed_by_me recency
    recency_buckets = {
        "Ostatnie 30 dni": 0,
        "1 - 6 miesięcy temu": 0,
        "6 - 12 miesięcy temu": 0,
        "1 - 3 lata temu": 0,
        "Ponad 3 lata temu": 0,
        "Nigdy nie otwierane (recency = 0)": 0
    }
    ms_day = 86400 * 1000
    for it in items.values():
        if it["is_folder"] or it["trashed"]: continue
        v = it["vdate"]
        if v == 0:
            recency_buckets["Nigdy nie otwierane (recency = 0)"] += 1
        else:
            diff_days = (max_db_ts - v) / ms_day
            if diff_days <= 30:
                recency_buckets["Ostatnie 30 dni"] += 1
            elif diff_days <= 180:
                recency_buckets["1 - 6 miesięcy temu"] += 1
            elif diff_days <= 365:
                recency_buckets["6 - 12 miesięcy temu"] += 1
            elif diff_days <= 1095:
                recency_buckets["1 - 3 lata temu"] += 1
            else:
                recency_buckets["Ponad 3 lata temu"] += 1

    # Candidates for deletion/cleanup
    candidates_for_deletion = []
    for it in items.values():
        if it["trashed"] or it["is_folder"]: continue
        t = it["title"]
        lower = t.lower()
        reasons = []
        if lower.startswith("dokument bez tytułu") or lower.startswith("arkusz kalkulacyjny bez tytułu") or lower.startswith("prezentacja bez tytułu"):
            reasons.append("Plik bez tytułu (prawdopodobnie pusty/porzucony szkic)")
        if lower.endswith("(1).gdoc") or lower.endswith("(1).csv") or lower.endswith("(2).gdoc"):
            reasons.append("Prawdopodobna duplikacja z sufiksem (1)/(2)")
        if lower.startswith("czy możesz") or lower.startswith("serio? nie możesz") or lower.startswith("super, dodaj jeszcze") or lower.startswith("dobrze, biorąc pod uwagę") or lower.startswith("jeszcze raz poproszę") or lower.startswith("wygeneruj mi podsumowanie") or lower.startswith("zrób z tego tabelę"):
            reasons.append("Tymczasowy zrzut / prompt eksportowany z czatu LLM do root")
        if lower.startswith("img_23") and lower.endswith(".jpeg") and it["parent_sid"] == root_sid:
            reasons.append("Pojedyncze surowe zdjęcie w głównym katalogu (do przeniesienia/usunięcia)")
        if it["size"] > 100 * 1024 * 1024 and it["vdate"] == 0 and (max_db_ts - it["mdate"]) > 3 * 365 * ms_day:
            reasons.append(f"Bardzo duży stary plik ({format_size(it['size'])}), nigdy nie otwierany, nie modyfikowany od lat")

        if reasons:
            candidates_for_deletion.append({
                "sid": it["sid"],
                "id": it["id"],
                "title": it["title"],
                "size": it["size"],
                "size_str": format_size(it["size"]),
                "path": get_path(it["sid"]),
                "last_viewed": format_ts(it["vdate"]),
                "last_modified": format_ts(it["mdate"]),
                "reasons": reasons
            })

    output_data = {
        "summary": {
            "total_active_files": total_active_files,
            "total_active_folders": total_active_folders,
            "owned_files": owned_files,
            "shared_with_me": shared_with_me,
            "starred_count": starred_count,
            "trashed_count": trashed_count,
            "top_folders_count": len(folders),
            "root_loose_files_count": len(root_files)
        },
        "recency_distribution": recency_buckets,
        "top_folders": folder_summaries,
        "root_files": root_file_summaries,
        "candidates_for_deletion_sample": candidates_for_deletion[:100],
        "total_candidates_found": len(candidates_for_deletion)
    }

    out_file = "/Users/pawel/git/gen-ai-orchestrator/sandbox/2026-09-19-gdrive-analysis/drive_analysis_data.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\nSaved analysis data to {out_file}")
    print("\nGlobal Recency Distribution:")
    for k, v in recency_buckets.items():
        print(f"  {k: <35}: {v} plików ({v/total_active_files*100:.1f}%)")

    print(f"\nTotal deletion candidates identified: {len(candidates_for_deletion)}")

if __name__ == "__main__":
    main()
