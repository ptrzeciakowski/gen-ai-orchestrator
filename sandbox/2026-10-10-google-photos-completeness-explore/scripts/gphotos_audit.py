#!/usr/bin/env python3
"""Audyt kompletności Google Photos: porównuje lokalne zdjęcia z paczkami Google Takeout.

Tylko biblioteka standardowa. Paczki ZIP są czytane strumieniowo (nic nie jest rozpakowywane na dysk),
a wyniki lądują w wznawialnej bazie SQLite.

Użycie:
    gphotos_audit.py --db index.sqlite index-local  "<folder ze zdjęciami>"       # czyta pliki (pobiera z chmury!)
    gphotos_audit.py --db index.sqlite index-drive  "88📸Zdjęcia"                  # tylko metadane z Drive API
    gphotos_audit.py --db index.sqlite index-takeout "<folder z takeout-*.zip>" [kolejne ścieżki...]
    gphotos_audit.py --db index.sqlite report --source drive --out raport/

Poziomy dopasowania (od najpewniejszego):
    sha256/md5 - identyczna zawartość pliku (sha256 dla --source local, md5 dla --source drive)
    name+size  - ta sama nazwa i rozmiar
    name+time  - ta sama nazwa i czas wykonania (EXIF vs photoTakenTime z JSON, z tolerancją strefy czasowej)
    name-only  - tylko nazwa (niepewne, do ręcznej kontroli)
    missing    - brak w Takeoucie
"""
from __future__ import annotations

import argparse
import calendar
import csv
import hashlib
import json
import os
import re
import sqlite3
import struct
import sys
import time
import zipfile
from pathlib import Path
from typing import Callable, Iterator, Optional

MEDIA_EXT = {
    ".jpg", ".jpeg", ".png", ".heic", ".heif", ".gif", ".webp", ".bmp", ".tif", ".tiff",
    ".dng", ".cr2", ".nef", ".arw", ".raw",
    ".mp4", ".mov", ".m4v", ".avi", ".3gp", ".mpg", ".mpeg", ".mts", ".mkv", ".wmv",
}
CHUNK = 1024 * 1024
TZ_MAX_OFFSET = 14 * 3600  # największa możliwa różnica strefy czasowej


# --------------------------------------------------------------------------- baza

SCHEMA = """
CREATE TABLE IF NOT EXISTS local (
    path TEXT PRIMARY KEY, name TEXT, size INTEGER, mtime REAL,
    sha256 TEXT, taken_naive INTEGER
);
CREATE TABLE IF NOT EXISTS takeout (
    id INTEGER PRIMARY KEY AUTOINCREMENT, archive TEXT, member TEXT,
    name TEXT, title TEXT, size INTEGER, sha256 TEXT, taken_utc INTEGER, md5 TEXT
);
CREATE INDEX IF NOT EXISTS takeout_sha ON takeout(sha256);
CREATE INDEX IF NOT EXISTS takeout_name ON takeout(name);
CREATE TABLE IF NOT EXISTS archives (
    archive TEXT PRIMARY KEY, size INTEGER, mtime REAL, done INTEGER DEFAULT 0, files INTEGER
);
CREATE TABLE IF NOT EXISTS drive (
    id TEXT PRIMARY KEY, path TEXT, name TEXT, size INTEGER, md5 TEXT,
    taken_naive INTEGER, width INTEGER, height INTEGER, camera TEXT, modified TEXT
);
"""


def open_db(path: str) -> sqlite3.Connection:
    con = sqlite3.connect(path)
    con.executescript(SCHEMA)
    cols = {r[1] for r in con.execute("PRAGMA table_info(takeout)")}
    if "md5" not in cols:  # migracja baz sprzed dodania md5
        con.execute("ALTER TABLE takeout ADD COLUMN md5 TEXT")
    con.execute("CREATE INDEX IF NOT EXISTS takeout_md5 ON takeout(md5)")
    return con


# --------------------------------------------------------------------------- narzędzia

def sha256_stream(f) -> str:
    return hash_stream(f)[0]


def hash_stream(f) -> tuple[str, str]:
    """Zwraca (sha256, md5) w jednym przebiegu po pliku."""
    h = hashlib.sha256()
    m = hashlib.md5()
    while True:
        b = f.read(CHUNK)
        if not b:
            break
        h.update(b)
        m.update(b)
    return h.hexdigest(), m.hexdigest()


def is_media(name: str) -> bool:
    return os.path.splitext(name)[1].lower() in MEDIA_EXT


def read_exif_taken(path: str) -> Optional[int]:
    """Zwraca czas wykonania z EXIF (DateTimeOriginal) jako 'naiwny' epoch (czas lokalny potraktowany jak UTC).

    Minimalny parser JPEG/EXIF w stdlib. Zwraca None, gdy nie ma EXIF-a.
    """
    try:
        with open(path, "rb") as f:
            head = f.read(256 * 1024)
    except OSError:
        return None
    if head[:2] != b"\xff\xd8":
        return None
    i = 2
    while i + 4 <= len(head) and head[i] == 0xFF:
        marker = head[i + 1]
        if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        if marker == 0xDA:  # start of scan
            break
        seglen = struct.unpack(">H", head[i + 2:i + 4])[0]
        seg = head[i + 4:i + 2 + seglen]
        if marker == 0xE1 and seg[:6] == b"Exif\x00\x00":
            return _parse_tiff_date(seg[6:])
        i += 2 + seglen
    return None


def _parse_tiff_date(t: bytes) -> Optional[int]:
    if len(t) < 8:
        return None
    end = "<" if t[:2] == b"II" else ">" if t[:2] == b"MM" else None
    if end is None:
        return None

    def u16(o):
        return struct.unpack(end + "H", t[o:o + 2])[0]

    def u32(o):
        return struct.unpack(end + "I", t[o:o + 4])[0]

    def ifd(off):
        out = {}
        try:
            n = u16(off)
            for k in range(n):
                e = off + 2 + 12 * k
                tag, typ, cnt = u16(e), u16(e + 2), u32(e + 4)
                out[tag] = (typ, cnt, e + 8)
        except struct.error:
            pass
        return out

    def ascii_val(entry):
        typ, cnt, vo = entry
        if typ != 2:
            return None
        start = u32(vo) if cnt > 4 else vo
        return t[start:start + cnt].split(b"\x00")[0].decode("ascii", "ignore")

    try:
        ifd0 = ifd(u32(4))
        s = None
        if 0x8769 in ifd0:
            exif = ifd(u32(ifd0[0x8769][2]))
            if 0x9003 in exif:
                s = ascii_val(exif[0x9003])
        if not s and 0x0132 in ifd0:
            s = ascii_val(ifd0[0x0132])
        if not s:
            return None
        tm = time.strptime(s.strip(), "%Y:%m:%d %H:%M:%S")
        return calendar.timegm(tm)
    except (struct.error, ValueError):
        return None


# --------------------------------------------------------------------------- index-local

def cmd_index_local(args) -> None:
    con = open_db(args.db)
    root = Path(args.root)
    total = hashed = skipped = 0
    t0 = time.time()
    for dirpath, _dirs, files in os.walk(root):
        for fn in files:
            if not is_media(fn):
                continue
            p = os.path.join(dirpath, fn)
            try:
                st = os.stat(p)
            except OSError as e:
                print(f"  ! {p}: {e}", file=sys.stderr)
                continue
            total += 1
            row = con.execute("SELECT size, mtime, sha256 FROM local WHERE path=?", (p,)).fetchone()
            if row and row[0] == st.st_size and row[1] == st.st_mtime and row[2]:
                skipped += 1
                continue
            try:
                with open(p, "rb") as f:
                    sha = sha256_stream(f)
            except OSError as e:
                print(f"  ! {p}: {e}", file=sys.stderr)
                continue
            taken = read_exif_taken(p) if fn.lower().endswith((".jpg", ".jpeg")) else None
            con.execute(
                "INSERT OR REPLACE INTO local(path,name,size,mtime,sha256,taken_naive) VALUES (?,?,?,?,?,?)",
                (p, fn, st.st_size, st.st_mtime, sha, taken),
            )
            hashed += 1
            if hashed % 200 == 0:
                con.commit()
                print(f"  {total} plików, {hashed} zahashowanych, {skipped} pominiętych "
                      f"({time.time() - t0:.0f}s)", flush=True)
    con.commit()
    print(f"Lokalnie: {total} plików multimedialnych ({hashed} nowych/zmienionych, {skipped} bez zmian).")


# --------------------------------------------------------------------------- index-takeout

Entry = tuple  # (dir, basename, size, opener)


def iter_zip_entries(path: str):
    zf = zipfile.ZipFile(path)
    entries = []
    for zi in zf.infolist():
        if zi.is_dir():
            continue
        d, b = os.path.split(zi.filename)
        entries.append((d, b, zi.file_size, (lambda zi=zi: zf.open(zi))))
    return zf, entries


def iter_dir_entries(path: str):
    entries = []
    for dirpath, _d, files in os.walk(path):
        for fn in files:
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(dirpath, path)
            entries.append((rel, fn, os.path.getsize(p), (lambda p=p: open(p, "rb"))))
    return None, entries


def _move_dup_suffix(name: str, dup: Optional[str]) -> str:
    if not dup:
        return name
    stem, ext = os.path.splitext(name)
    return f"{stem}{dup}{ext}"


def json_media_name(json_basename: str) -> str:
    """Z nazwy pliku JSON z Takeoutu wyprowadza nazwę zdjęcia, którego dotyczy.

    Obsługuje: X.jpg.json, X.jpg.supplemental-metadata.json (także obcięte), duplikaty X.jpg(1).json.
    """
    base = re.sub(r"\.json$", "", json_basename, flags=re.I)
    m = re.match(r"^(.*?)\.supplemental[-a-z]*(\(\d+\))?$", base, flags=re.I)
    if m:
        return _move_dup_suffix(m.group(1), m.group(2))
    m = re.match(r"^(.*)(\(\d+\))$", base)
    if m:
        return _move_dup_suffix(m.group(1), m.group(2))
    return base


def strip_edited(name: str) -> str:
    stem, ext = os.path.splitext(name)
    return (stem[:-7] if stem.lower().endswith("-edited") else stem) + ext


def process_archive(con: sqlite3.Connection, archive: str, entries: list) -> int:
    # 1) JSON-y (małe) -> mapa metadanych
    meta_by_name: dict = {}
    meta_by_title: dict = {}
    for d, b, size, opener in entries:
        if b.lower().endswith(".json") and size < 2 * 1024 * 1024:
            try:
                with opener() as f:
                    data = json.loads(f.read().decode("utf-8", "ignore"))
            except (ValueError, OSError):
                continue
            title = data.get("title")
            ts = (data.get("photoTakenTime") or {}).get("timestamp")
            if not title or ts is None:
                continue
            rec = (title, int(ts))
            meta_by_name[(d, json_media_name(b).lower())] = rec
            meta_by_title[(d, title.lower())] = rec

    # 2) media -> hash w locie
    count = 0
    for d, b, size, opener in entries:
        if not is_media(b):
            continue
        original = strip_edited(b)
        rec = (meta_by_name.get((d, b.lower())) or meta_by_name.get((d, original.lower()))
               or meta_by_title.get((d, b.lower())) or meta_by_title.get((d, original.lower())))
        with opener() as f:
            sha, md5 = hash_stream(f)
        con.execute(
            "INSERT INTO takeout(archive,member,name,title,size,sha256,taken_utc,md5) VALUES (?,?,?,?,?,?,?,?)",
            (archive, f"{d}/{b}", b.lower(), (rec[0] if rec else b).lower(), size, sha,
             rec[1] if rec else None, md5),
        )
        count += 1
    return count


def collect_sources(paths: list[str]) -> list[str]:
    out: list[str] = []
    for p in paths:
        pp = Path(p)
        if pp.is_dir():
            zips = sorted(str(z) for z in pp.rglob("*.zip"))
            if zips:
                out.extend(zips)
            else:
                out.append(str(pp))  # już rozpakowany Takeout
        elif pp.is_file():
            out.append(str(pp))
        else:
            print(f"  ! brak ścieżki: {p}", file=sys.stderr)
    return out


def cmd_index_takeout(args) -> None:
    con = open_db(args.db)
    sources = collect_sources(args.paths)
    if not sources:
        sys.exit("Nie znaleziono żadnych paczek ani folderów Takeout.")
    print(f"Źródeł do przetworzenia: {len(sources)}")
    for i, src in enumerate(sources, 1):
        st = os.stat(src)
        is_zip = os.path.isfile(src)
        size, mtime = (st.st_size, st.st_mtime) if is_zip else (0, 0.0)
        row = con.execute("SELECT size, mtime, done FROM archives WHERE archive=?", (src,)).fetchone()
        if row and row[2] and row[0] == size and row[1] == mtime:
            print(f"[{i}/{len(sources)}] pomijam (już przetworzone): {src}")
            continue
        con.execute("DELETE FROM takeout WHERE archive=?", (src,))  # wznowienie przerwanej paczki
        t0 = time.time()
        zf = None
        try:
            zf, entries = iter_zip_entries(src) if is_zip else iter_dir_entries(src)
            n = process_archive(con, src, entries)
        except zipfile.BadZipFile as e:
            print(f"[{i}/{len(sources)}] ! uszkodzony ZIP {src}: {e}", file=sys.stderr)
            con.rollback()
            continue
        finally:
            if zf:
                zf.close()
        con.execute("INSERT OR REPLACE INTO archives(archive,size,mtime,done,files) VALUES (?,?,?,1,?)",
                    (src, size, mtime, n))
        con.commit()
        print(f"[{i}/{len(sources)}] {n} plików z {os.path.basename(src)} ({time.time() - t0:.0f}s)", flush=True)
    total = con.execute("SELECT COUNT(*) FROM takeout").fetchone()[0]
    print(f"Takeout w indeksie: {total} plików multimedialnych.")


# --------------------------------------------------------------------------- index-drive (DriveFS / Drive API)

DRIVE_FILES = "https://www.googleapis.com/drive/v3/files"
FOLDER_MIME = "application/vnd.google-apps.folder"
DEFAULT_GCLOUD_CONFIG = os.path.expanduser("~/.config/gcloud-gphotos-audit")


def find_drivefs_db() -> Optional[str]:
    """Wyszukuje lokalną bazę SQLite aplikacji Google Drive for desktop."""
    import glob
    base = os.path.expanduser("~/Library/Application Support/Google/DriveFS")
    if not os.path.isdir(base):
        return None
    matches = glob.glob(os.path.join(base, "[0-9]*", "metadata_sqlite_db"))
    if not matches:
        matches = glob.glob(os.path.join(base, "*", "metadata_sqlite_db"))
    return matches[0] if matches else None


def get_proto_md5(b: bytes) -> Optional[str]:
    """Wyciąga MD5 (pole 48) z protobuffera Google DriveFS bez zewnętrznych bibliotek."""
    if not b:
        return None
    i, n = 0, len(b)
    while i < n:
        key, shift = 0, 0
        while True:
            if i >= n:
                return None
            byte = b[i]; i += 1
            key |= (byte & 0x7f) << shift
            if not (byte & 0x80):
                break
            shift += 7
        fnum, wire = key >> 3, key & 7
        if wire == 0:
            while True:
                if i >= n:
                    return None
                byte = b[i]; i += 1
                if not (byte & 0x80):
                    break
        elif wire == 2:
            length, shift = 0, 0
            while True:
                if i >= n:
                    return None
                byte = b[i]; i += 1
                length |= (byte & 0x7f) << shift
                if not (byte & 0x80):
                    break
                shift += 7
            if fnum == 48:
                return b[i:i + length].decode("ascii", errors="ignore")
            i += length
        elif wire == 1:
            i += 8
        elif wire == 5:
            i += 4
        else:
            return None
    return None


def index_from_drivefs(con: sqlite3.Connection, folder_name: str, drivefs_db: str) -> int:
    """Skanuje lokalną bazę DriveFS w ułamku sekundy bez pobierania danych z internetu."""
    dfs = sqlite3.connect(f"file:{drivefs_db}?mode=ro", uri=True)
    dfs.text_factory = bytes
    dcur = dfs.cursor()

    dcur.execute("SELECT item_stable_id, parent_stable_id FROM stable_parents")
    parents = dict(dcur.fetchall())
    children: dict = {}
    for item, par in parents.items():
        children.setdefault(par, []).append(item)

    clean_target = folder_name.strip("/").split("/")[-1]
    dcur.execute("SELECT stable_id, local_title FROM items WHERE is_tombstone=0 AND is_folder=1")
    candidates = []
    for sid, title in dcur.fetchall():
        t = title.decode("utf-8", errors="replace") if title else ""
        if t == clean_target or t.lower() == clean_target.lower():
            candidates.append(sid)

    if not candidates:
        sys.exit(f"Nie znaleziono folderu '{clean_target}' w bazie DriveFS ({drivefs_db}).")
    root_id = candidates[0]

    descendants = set()
    stack = [root_id]
    while stack:
        curr = stack.pop()
        for child in children.get(curr, []):
            if child not in descendants:
                descendants.add(child)
                stack.append(child)

    dcur.execute("SELECT stable_id, local_title FROM items")
    titles = {s: t.decode("utf-8", errors="replace") for s, t in dcur.fetchall()}

    dcur.execute(
        "SELECT stable_id, id, file_size, modified_date, proto FROM items "
        "WHERE is_tombstone=0 AND trashed=0"
    )
    kept = 0
    t0 = time.time()
    for sid, fid, size, mtime, proto in dcur.fetchall():
        if sid in descendants:
            name = titles.get(sid, "")
            if not is_media(name):
                continue
            parts = []
            curr = sid
            while curr in parents and curr != root_id:
                parts.append(titles.get(curr, ""))
                curr = parents[curr]
            parts.append(titles.get(root_id, ""))
            rel_path = "/".join(reversed(parts))
            md5 = get_proto_md5(proto)
            file_id = fid.decode("ascii", errors="ignore") if fid else str(sid)
            mod_str = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(mtime / 1000)) if mtime else None
            con.execute(
                "INSERT OR REPLACE INTO drive(id,path,name,size,md5,taken_naive,width,height,camera,modified) "
                "VALUES (?,?,?,?,?,?,?,?,?,?)",
                (file_id, rel_path, name, size, md5, None, None, None, None, mod_str),
            )
            kept += 1
            if kept % 5000 == 0:
                con.commit()
    con.commit()
    dfs.close()
    print(f"DriveFS: zaindeksowano {kept} plików w {time.time() - t0:.2f}s z {drivefs_db}")
    return kept


class DriveClient:
    """Minimalny klient Drive API v3 (stdlib). Token pobierany z gcloud ADC, odświeżany co 30 min."""

    def __init__(self, gcloud_config: Optional[str], quota_project: Optional[str]):
        self.gcloud_config = gcloud_config
        self.quota_project = quota_project
        self._token = None
        self._token_at = 0.0

    def token(self) -> str:
        import subprocess
        if self._token and time.time() - self._token_at < 1800:
            return self._token
        env = os.environ.copy()
        if self.gcloud_config:
            env["CLOUDSDK_CONFIG"] = self.gcloud_config
        r = subprocess.run(["gcloud", "auth", "application-default", "print-access-token"],
                           capture_output=True, text=True, env=env)
        if r.returncode != 0:
            sys.exit(f"Nie udało się pobrać tokenu z gcloud:\n{r.stderr}")
        self._token, self._token_at = r.stdout.strip(), time.time()
        return self._token

    def get(self, params: dict) -> dict:
        import urllib.error
        import urllib.parse
        import urllib.request
        url = f"{DRIVE_FILES}?{urllib.parse.urlencode(params)}"
        for attempt in range(6):
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {self.token()}"})
            if self.quota_project:
                req.add_header("X-Goog-User-Project", self.quota_project)
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as e:
                body = e.read().decode("utf-8", "ignore")
                if e.code in (429, 500, 502, 503, 504) and attempt < 5:
                    time.sleep(2 ** attempt)
                    continue
                if e.code == 401 and attempt < 5:
                    self._token = None
                    continue
                sys.exit(f"Drive API HTTP {e.code}: {body[:800]}")
            except (urllib.error.URLError, TimeoutError):
                if attempt == 5:
                    raise
                time.sleep(2 ** attempt)
        raise RuntimeError("unreachable")

    def list_all(self, q: str, fields: str, on_page: Optional[Callable[[int], None]] = None) -> Iterator[dict]:
        token = None
        n = 0
        while True:
            params = {"q": q, "fields": f"nextPageToken,files({fields})", "pageSize": 1000,
                      "supportsAllDrives": "true", "includeItemsFromAllDrives": "true", "spaces": "drive"}
            if token:
                params["pageToken"] = token
            data = self.get(params)
            for f in data.get("files", []):
                n += 1
                yield f
            if on_page:
                on_page(n)
            token = data.get("nextPageToken")
            if not token:
                return


def _q_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace("'", "\\'")


def parse_exif_time(s: Optional[str]) -> Optional[int]:
    if not s:
        return None
    try:
        return calendar.timegm(time.strptime(s.strip(), "%Y:%m:%d %H:%M:%S"))
    except ValueError:
        return None


def cmd_index_drive(args) -> None:
    con = open_db(args.db)
    cfg = args.gcloud_config or (DEFAULT_GCLOUD_CONFIG if os.path.isdir(DEFAULT_GCLOUD_CONFIG) else None)
    client = DriveClient(cfg, args.quota_project)

    # 1) rozwiąż ścieżkę folderu względem "Mój dysk"
    parent, segs = "root", [s for s in args.folder.strip("/").split("/") if s]
    for seg in segs:
        found = list(client.list_all(
            f"name='{_q_escape(seg)}' and '{parent}' in parents and mimeType='{FOLDER_MIME}' and trashed=false",
            "id,name"))
        if not found:
            sys.exit(f"Nie znaleziono folderu '{seg}' w Drive (ścieżka: {args.folder}).")
        parent = found[0]["id"]
    root_id = parent
    print(f"Folder '{args.folder}' -> id {root_id}")

    # 2) wszystkie foldery -> potomkowie folderu głównego
    folders: dict = {}
    for f in client.list_all(f"mimeType='{FOLDER_MIME}' and trashed=false", "id,name,parents",
                             lambda n: print(f"  foldery: {n}", flush=True)):
        folders[f["id"]] = (f["name"], (f.get("parents") or [None])[0])
    children: dict = {}
    for fid, (_n, par) in folders.items():
        children.setdefault(par, []).append(fid)
    inside = {root_id}
    stack = [root_id]
    while stack:
        for c in children.get(stack.pop(), []):
            if c not in inside:
                inside.add(c)
                stack.append(c)
    print(f"Folderów w '{args.folder}': {len(inside)}")

    def folder_path(fid: str) -> str:
        parts = []
        while fid in folders and fid != root_id:
            name, par = folders[fid]
            parts.append(name)
            fid = par
        parts.append(segs[-1] if segs else "")
        return "/".join(reversed([p for p in parts if p]))

    path_cache: dict = {}

    # 3) pliki multimedialne (tylko metadane!)
    fields = ("id,name,size,md5Checksum,modifiedTime,parents,"
              "imageMediaMetadata(time,width,height,cameraModel)")
    q = "(mimeType contains 'image/' or mimeType contains 'video/') and trashed=false"
    kept = seen = 0
    for f in client.list_all(q, fields, lambda n: print(f"  pliki w Drive: {n}, w folderze: {kept}", flush=True)):
        seen += 1
        par = (f.get("parents") or [None])[0]
        if par not in inside:
            continue
        if par not in path_cache:
            path_cache[par] = folder_path(par)
        im = f.get("imageMediaMetadata") or {}
        con.execute(
            "INSERT OR REPLACE INTO drive(id,path,name,size,md5,taken_naive,width,height,camera,modified) "
            "VALUES (?,?,?,?,?,?,?,?,?,?)",
            (f["id"], f"{path_cache[par]}/{f['name']}", f["name"], int(f["size"]) if f.get("size") else None,
             f.get("md5Checksum"), parse_exif_time(im.get("time")), im.get("width"), im.get("height"),
             im.get("cameraModel"), f.get("modifiedTime")))
        kept += 1
        if kept % 2000 == 0:
            con.commit()
    con.commit()
    print(f"Drive: {kept} plików multimedialnych w '{args.folder}' (przejrzano {seen} w całym Drive).")


# --------------------------------------------------------------------------- report

def time_matches(local_naive: int, takeout_utc: int) -> bool:
    """EXIF jest w czasie lokalnym bez strefy, photoTakenTime w UTC: różnica ma być pełną ćwiartką godziny <= 14h."""
    diff = local_naive - takeout_utc
    if abs(diff) > TZ_MAX_OFFSET + 60:
        return False
    r = diff % 900
    return min(r, 900 - r) <= 1


SOURCES = {
    # źródło: (tabela, kolumna z hashem w tej tabeli i w takeout, etykieta poziomu)
    "local": ("local", "sha256", "sha256"),
    "drive": ("drive", "md5", "md5"),
}


def classify(con: sqlite3.Connection, source: str = "local"):
    table, col, label = SOURCES[source]
    hashes = {r[0] for r in con.execute(f"SELECT DISTINCT {col} FROM takeout") if r[0]}
    name_size: set = set()
    by_name: dict = {}
    for name, title, size, taken in con.execute("SELECT name, title, size, taken_utc FROM takeout"):
        for n in {name, title, strip_edited(name)}:
            name_size.add((n, size))
            by_name.setdefault(n, []).append(taken)
    for path, name, size, h, taken in con.execute(
            f"SELECT path, name, size, {col}, taken_naive FROM {table} ORDER BY path"):
        n = name.lower()
        if h and h in hashes:
            yield path, label
        elif (n, size) in name_size:
            yield path, "name+size"
        elif n in by_name:
            if taken is not None and any(t is not None and time_matches(taken, t) for t in by_name[n]):
                yield path, "name+time"
            else:
                yield path, "name-only"
        else:
            yield path, "missing"


def cmd_report(args) -> None:
    con = open_db(args.db)
    table, col, label = SOURCES[args.source]
    if not con.execute(f"SELECT 1 FROM {table} LIMIT 1").fetchone():
        sys.exit(f"Brak indeksu źródła '{args.source}' (uruchom index-{args.source}).")
    if not con.execute(f"SELECT 1 FROM takeout WHERE {col} IS NOT NULL LIMIT 1").fetchone():
        sys.exit(f"Brak indeksu Takeoutu z kolumną {col} (uruchom index-takeout; starsze wpisy bez md5 wymagają "
                 f"ponownego zaindeksowania).")
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    counts: dict = {}
    files = {lvl: [] for lvl in ("missing", "name-only")}
    for path, level in classify(con, args.source):
        counts[level] = counts.get(level, 0) + 1
        if level in files:
            files[level].append(path)
    for lvl, paths in files.items():
        with open(out / f"{lvl}.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["path"])
            for p in paths:
                w.writerow([p])
    total = sum(counts.values())
    print(f"Plików ({args.source}): {total}")
    for lvl in (label, "name+size", "name+time", "name-only", "missing"):
        print(f"  {lvl:10s} {counts.get(lvl, 0):8d}")
    print(f"Raporty: {out / 'missing.csv'}  (brakujące)\n         {out / 'name-only.csv'}  (niepewne)")


# --------------------------------------------------------------------------- main

def main(argv: Optional[list[str]] = None) -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default="gphotos_audit.sqlite", help="plik bazy SQLite (wznawialny)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("index-local", help="zindeksuj lokalne zdjęcia (czyta zawartość plików)")
    s.add_argument("root")
    s.set_defaults(fn=cmd_index_local)
    s = sub.add_parser("index-drive", help="zindeksuj metadane z Drive API (bez pobierania plików)")
    s.add_argument("folder", help="ścieżka folderu względem 'Mój dysk', np. '88📸Zdjęcia'")
    s.add_argument("--gcloud-config", help=f"katalog CLOUDSDK_CONFIG z ADC (domyślnie {DEFAULT_GCLOUD_CONFIG} jeśli istnieje)")
    s.add_argument("--quota-project", help="projekt GCP z włączonym Drive API (nagłówek X-Goog-User-Project)")
    s.set_defaults(fn=cmd_index_drive)
    s = sub.add_parser("index-takeout", help="zindeksuj paczki ZIP / foldery Takeoutu (streaming)")
    s.add_argument("paths", nargs="+")
    s.set_defaults(fn=cmd_index_takeout)
    s = sub.add_parser("report", help="porównaj i wygeneruj raport")
    s.add_argument("--source", choices=sorted(SOURCES), default="drive",
                   help="drive = metadane z Drive API (md5), local = lokalne pliki (sha256)")
    s.add_argument("--out", default="raport")
    s.set_defaults(fn=cmd_report)
    args = ap.parse_args(argv)
    args.fn(args)


if __name__ == "__main__":
    main()
