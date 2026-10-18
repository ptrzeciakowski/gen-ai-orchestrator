#!/usr/bin/env python3
"""
Migracja zdjęć i wideo z Dysku Google (zamontowanego lokalnie) do Google Photos
przez Photos Library API (zakres photoslibrary.appendonly).

Co zachowuje:
  * oryginalne bajty pliku -> cały EXIF (data, GPS, aparat) trafia do Photos bez zmian,
  * oryginalną ścieżkę folderu (w opisie zdjęcia - da się po niej wyszukiwać w Photos),
  * opcjonalnie: album na rocznik / folder.

Czego API NIE potrafi (ograniczenia Google, nie skryptu):
  * ustawić daty zdjęcia bez EXIF (dlatego jest opcja --stamp-missing, która robi
    KOPIĘ pliku z dopisaną datą - oryginał na Dysku nigdy nie jest modyfikowany),
  * odczytać / zweryfikować biblioteki po wgraniu (od 2025 API widzi tylko treści
    utworzone przez własną aplikację) - weryfikacja = statusy z batchCreate,
  * więcej niż 10 000 żądań dziennie -> skrypt sam zatrzymuje się przy budżecie
    i wznawia od miejsca przerwania przy następnym uruchomieniu.

Użycie:  patrz README.md
"""

import argparse
import hashlib
import mimetypes
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import requests
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

HERE = Path(__file__).resolve().parent
STATE_DIR = HERE / ".state"
CREDENTIALS_FILE = HERE / "credentials.json"  # klient OAuth typu "Desktop app"
TOKEN_FILE = STATE_DIR / "token.json"
DB_FILE = STATE_DIR / "state.db"

SCOPES = ["https://www.googleapis.com/auth/photoslibrary.appendonly"]
API = "https://photoslibrary.googleapis.com/v1"

DEFAULT_SRC = os.path.expanduser(
    "~/Library/CloudStorage/GoogleDrive-ptrzeciakowski@gmail.com/Mój dysk/88📸Zdjęcia"
)

# Duplikaty wykryte w audycie (dopasowanie po komponentach ścieżki względnej).
DEFAULT_EXCLUDES = [r"(^|/)2017 \(1\)(/|$)", r"(^|/)2015 \(1\)(/|$)", r"(^|/)Fotograf/Kopia(/|$)"]

# Rozszerzenia akceptowane przez Google Photos -> MIME.
MIME = {
    ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".gif": "image/gif",
    ".webp": "image/webp", ".heic": "image/heic", ".heif": "image/heif", ".tif": "image/tiff",
    ".tiff": "image/tiff", ".bmp": "image/bmp", ".dng": "image/x-adobe-dng",
    ".mp4": "video/mp4", ".mov": "video/quicktime", ".m4v": "video/x-m4v", ".avi": "video/x-msvideo",
    ".3gp": "video/3gpp", ".mkv": "video/x-matroska", ".mpg": "video/mpeg", ".mpeg": "video/mpeg",
    ".wmv": "video/x-ms-wmv", ".mts": "video/mp2t", ".webm": "video/webm",
}
VIDEO_EXT = {e for e, m in MIME.items() if m.startswith("video/")}

BATCH_SIZE = 50                 # limit batchCreate
DEFAULT_DAILY_BUDGET = 9500     # zapas względem limitu 10 000/dzień
HARD_LIMIT = 9900               # ostatnie żądania zarezerwowane na flush batcha
PACIFIC = ZoneInfo("America/Los_Angeles")  # kwoty Google resetują się o północy PT


class QuotaExhausted(Exception):
    pass


# ----------------------------------------------------------------------------- stan

class State:
    def __init__(self):
        STATE_DIR.mkdir(exist_ok=True)
        self.db = sqlite3.connect(DB_FILE)
        self.db.executescript(
            """
            CREATE TABLE IF NOT EXISTS files(
              rel TEXT PRIMARY KEY, size INTEGER, sha1 TEXT, status TEXT NOT NULL,
              media_id TEXT, note TEXT, error TEXT, updated TEXT);
            CREATE TABLE IF NOT EXISTS albums(name TEXT PRIMARY KEY, album_id TEXT NOT NULL);
            CREATE TABLE IF NOT EXISTS quota(day TEXT PRIMARY KEY, used INTEGER NOT NULL);
            """
        )
        self.budget = DEFAULT_DAILY_BUDGET

    @staticmethod
    def today():
        return datetime.now(PACIFIC).date().isoformat()

    def used_today(self):
        row = self.db.execute("SELECT used FROM quota WHERE day=?", (self.today(),)).fetchone()
        return row[0] if row else 0

    def spend(self, reserve=False):
        limit = HARD_LIMIT if reserve else self.budget
        used = self.used_today()
        if used >= limit:
            raise QuotaExhausted(f"Wyczerpany budżet żądań na dziś ({used}/{limit}).")
        self.db.execute(
            "INSERT INTO quota(day, used) VALUES(?, 1) ON CONFLICT(day) DO UPDATE SET used=used+1",
            (self.today(),),
        )
        self.db.commit()

    def register(self, rels_sizes):
        self.db.executemany(
            "INSERT OR IGNORE INTO files(rel, size, status, updated) VALUES(?, ?, 'pending', datetime('now'))",
            rels_sizes,
        )
        self.db.commit()

    def pending(self, include_failed):
        statuses = ("pending", "failed") if include_failed else ("pending",)
        q = f"SELECT rel FROM files WHERE status IN ({','.join('?' * len(statuses))}) ORDER BY rel"
        return [r[0] for r in self.db.execute(q, statuses)]

    def mark(self, rel, status, **kw):
        kw.update(status=status)
        cols = ", ".join(f"{k}=?" for k in kw)
        self.db.execute(f"UPDATE files SET {cols}, updated=datetime('now') WHERE rel=?", (*kw.values(), rel))
        self.db.commit()

    def sha_done(self, sha1):
        row = self.db.execute(
            "SELECT rel FROM files WHERE sha1=? AND status IN ('uploaded','duplicate') LIMIT 1", (sha1,)
        ).fetchone()
        return row[0] if row else None

    def album(self, name):
        row = self.db.execute("SELECT album_id FROM albums WHERE name=?", (name,)).fetchone()
        return row[0] if row else None

    def save_album(self, name, album_id):
        self.db.execute("INSERT OR REPLACE INTO albums(name, album_id) VALUES(?, ?)", (name, album_id))
        self.db.commit()


# ----------------------------------------------------------------------------- API

class Photos:
    def __init__(self, state: State):
        self.state = state
        self.http = requests.Session()
        self.creds = self._load_creds()

    def _load_creds(self):
        creds = None
        if TOKEN_FILE.exists():
            creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not CREDENTIALS_FILE.exists():
                    sys.exit(f"Brak {CREDENTIALS_FILE} - patrz README.md (krok 1).")
                flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
                creds = flow.run_local_server(port=0)
            TOKEN_FILE.write_text(creds.to_json())
            TOKEN_FILE.chmod(0o600)
        return creds

    def _headers(self, extra=None):
        if not self.creds.valid:
            self.creds.refresh(Request())
            TOKEN_FILE.write_text(self.creds.to_json())
        return {"Authorization": f"Bearer {self.creds.token}", **(extra or {})}

    def _call(self, method, url, headers=None, json=None, data_fn=None, reserve=False):
        """Jedno logiczne żądanie z retry/backoff. Każda próba zużywa budżet."""
        last = None
        for attempt in range(6):
            self.state.spend(reserve=reserve)
            data = data_fn() if data_fn else None
            try:
                r = self.http.request(
                    method, url, headers=self._headers(headers), json=json, data=data, timeout=(15, 3600)
                )
            except requests.RequestException as e:
                last = e
                time.sleep(min(2 ** attempt, 60))
                continue
            finally:
                if data is not None and hasattr(data, "close"):
                    data.close()
            if r.status_code == 429:
                if attempt >= 2:
                    raise QuotaExhausted("API zwraca 429 (limit dzienny/minutowy) - wznów później.")
                time.sleep(30 * (attempt + 1))
                continue
            if r.status_code >= 500:
                last = RuntimeError(f"{r.status_code}: {r.text[:200]}")
                time.sleep(min(2 ** attempt, 60))
                continue
            if r.status_code == 401:
                self.creds.refresh(Request())
                continue
            return r
        raise RuntimeError(f"Żądanie nie powiodło się po 6 próbach: {last}")

    def upload_bytes(self, path: Path, mime: str):
        r = self._call(
            "POST",
            f"{API}/uploads",
            headers={
                "Content-type": "application/octet-stream",
                "X-Goog-Upload-Content-Type": mime,
                "X-Goog-Upload-Protocol": "raw",
            },
            data_fn=lambda: open(path, "rb"),
        )
        if r.status_code != 200 or not r.text:
            raise RuntimeError(f"upload {r.status_code}: {r.text[:200]}")
        return r.text  # upload token

    def create_album(self, title):
        r = self._call("POST", f"{API}/albums", json={"album": {"title": title[:500]}})
        if r.status_code != 200:
            raise RuntimeError(f"albums.create {r.status_code}: {r.text[:200]}")
        return r.json()["id"]

    def batch_create(self, items, album_id=None):
        body = {"newMediaItems": items}
        if album_id:
            body["albumId"] = album_id
        r = self._call("POST", f"{API}/mediaItems:batchCreate", json=body, reserve=True)
        if r.status_code != 200:
            raise RuntimeError(f"batchCreate {r.status_code}: {r.text[:300]}")
        return r.json().get("newMediaItemResults", [])


# ----------------------------------------------------------------------------- pliki

def scan(src: Path, excludes):
    """Zwraca (obsługiwane [(rel, size)], pominięte_nieobsługiwane [rel], wykluczone int)."""
    ok, unsupported, excluded = [], [], 0
    rx = [re.compile(p) for p in excludes]
    for root, dirs, files in os.walk(src):
        dirs.sort()
        for name in sorted(files):
            if name.startswith("."):
                continue
            full = Path(root) / name
            rel = full.relative_to(src).as_posix()
            if any(p.search(rel) for p in rx):
                excluded += 1
                continue
            if full.suffix.lower() not in MIME:
                unsupported.append(rel)
                continue
            try:
                ok.append((rel, full.stat().st_size))
            except OSError:
                unsupported.append(rel)
    return ok, unsupported, excluded


def sha1_of(path: Path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def album_name(rel: str, mode: str):
    parts = rel.split("/")[:-1]
    if not parts or mode == "none":
        return None
    return parts[0] if mode == "year" else " / ".join(parts)


# --- uzupełnianie brakujących dat (tylko na KOPII, wymaga exiftool) -----------------

DATE_IN_NAME = re.compile(r"(?<!\d)((?:19|20)\d{2})[-_.]?(0[1-9]|1[0-2])[-_.]?(0[1-9]|[12]\d|3[01])(?!\d)")
YEAR_DIR = re.compile(r"^((?:19|20)\d{2})(?!\d)")


def has_capture_date(path: Path):
    out = subprocess.run(
        ["exiftool", "-s3", "-DateTimeOriginal", "-CreateDate", "-MediaCreateDate", "--", str(path)],
        capture_output=True, text=True,
    ).stdout
    return any(line.strip() and not line.startswith("0000") for line in out.splitlines())


def guess_date(rel: str):
    """(data 'YYYY:MM:DD 12:00:00', źródło) z nazwy pliku, a w ostateczności z roku w nazwie folderu."""
    m = DATE_IN_NAME.search(rel.split("/")[-1])
    if m:
        return f"{m[1]}:{m[2]}:{m[3]} 12:00:00", "z nazwy pliku"
    for part in rel.split("/")[:-1]:
        m = YEAR_DIR.match(part)
        if m:
            return f"{m[1]}:01:01 12:00:00", "z roku folderu"
    return None, None


def stamped_copy(path: Path, rel: str, tmpdir: Path):
    """Jeśli plik nie ma daty - zwraca (ścieżka_kopii, notatka); inaczej (path, None)."""
    if has_capture_date(path):
        return path, None
    date, source = guess_date(rel)
    if not date:
        return path, "BEZ DATY (Photos użyje daty wgrania)"
    copy = tmpdir / path.name
    shutil.copy2(path, copy)
    if path.suffix.lower() in VIDEO_EXT:
        tags = [f"-QuickTime:CreateDate={date}", f"-QuickTime:MediaCreateDate={date}", f"-QuickTime:TrackCreateDate={date}"]
    else:
        tags = [f"-DateTimeOriginal={date}", f"-CreateDate={date}"]
    subprocess.run(["exiftool", "-overwrite_original", "-q", *tags, str(copy)], check=True)
    return copy, f"data dopisana {source}: {date}"


# ----------------------------------------------------------------------------- komendy

def cmd_scan(args):
    src = Path(args.src)
    if not src.exists():
        sys.exit(f"Brak katalogu źródłowego: {src}")
    print("Skanuję (tylko metadane plików)...")
    ok, unsupported, excluded = scan(src, args.exclude)
    total = sum(s for _, s in ok)
    by_ext = {}
    for rel, size in ok:
        e = Path(rel).suffix.lower()
        n, b = by_ext.get(e, (0, 0))
        by_ext[e] = (n + 1, b + size)
    print(f"\nDo migracji:   {len(ok):>7} plików, {total / 1e9:8.1f} GB")
    print(f"Wykluczone:    {excluded:>7} (duplikaty z audytu)")
    print(f"Nieobsługiwane:{len(unsupported):>7} (zostaną pominięte)")
    for e, (n, b) in sorted(by_ext.items(), key=lambda kv: -kv[1][1]):
        print(f"   {e:<6} {n:>7} plików {b / 1e9:8.1f} GB")
    requests_needed = len(ok) + len(ok) // BATCH_SIZE + 1
    print(f"\nSzacunek żądań API: ~{requests_needed}  =>  ~{requests_needed / DEFAULT_DAILY_BUDGET:.1f} dnia/dni przy budżecie {DEFAULT_DAILY_BUDGET}/dzień")
    if unsupported[:15]:
        print("\nPrzykłady pominiętych:", *unsupported[:15], sep="\n  ")
    if args.check_dates:
        if not shutil.which("exiftool"):
            sys.exit("Brak exiftool (brew install exiftool).")
        print("\nSzukam plików bez daty wykonania (exiftool, może potrwać)...")
        exts = [x for e in MIME for x in ("-ext", e.lstrip("."))]
        cmd = ["exiftool", "-r", "-q", "-if", "not ($DateTimeOriginal or $CreateDate or $MediaCreateDate)",
               "-p", "$FilePath", *exts, str(src)]
        out = subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()
        print(f"Bez daty wykonania: {len(out)} plików (skrypt z --stamp-missing spróbuje je uzupełnić)")
        for line in out[:15]:
            print("  ", line)


def cmd_status(args):
    st = State()
    for status, n in st.db.execute("SELECT status, COUNT(*) FROM files GROUP BY status ORDER BY 2 DESC"):
        print(f"{status:<10} {n}")
    print(f"\nŻądania API dziś (doba PT): {st.used_today()} / {st.budget}")
    for rel, err in st.db.execute("SELECT rel, error FROM files WHERE status='failed' LIMIT 10"):
        print(f"  FAILED {rel}: {err}")
    nodate = st.db.execute("SELECT COUNT(*) FROM files WHERE note LIKE 'BEZ DATY%'").fetchone()[0]
    if nodate:
        print(f"\nPliki bez daty (po wgraniu mają datę wgrania): {nodate}")


def cmd_upload(args):
    src = Path(args.src)
    if not src.exists():
        sys.exit(f"Brak katalogu źródłowego: {src}")
    if args.stamp_missing and not shutil.which("exiftool"):
        sys.exit("--stamp-missing wymaga exiftool (brew install exiftool).")

    st = State()
    st.budget = args.daily_budget
    ok, _, _ = scan(src, args.exclude)
    st.register(ok)
    todo = st.pending(args.retry_failed)
    if args.limit:
        todo = todo[: args.limit]
    print(f"Do wgrania: {len(todo)} plików. Budżet żądań dziś: {st.used_today()}/{st.budget} użyte.")

    photos = Photos(st)
    tmp_root = Path(tempfile.mkdtemp(prefix="photos_migrate_"))
    batch, batch_album, done, started = [], None, 0, time.time()

    def flush():
        nonlocal batch, batch_album
        if not batch:
            return
        album_id = None
        if batch_album:
            album_id = st.album(batch_album)
            if not album_id:
                album_id = photos.create_album(batch_album)
                st.save_album(batch_album, album_id)
        results = photos.batch_create([b["item"] for b in batch], album_id)
        by_token = {r.get("uploadToken"): r for r in results}
        for b in batch:
            r = by_token.get(b["token"], {})
            status = r.get("status", {})
            media = r.get("mediaItem", {})
            if media.get("id"):
                st.mark(b["rel"], "uploaded", media_id=media["id"], sha1=b["sha1"], note=b["note"], error=None)
            else:
                st.mark(b["rel"], "failed", sha1=b["sha1"], error=status.get("message", "brak mediaItem w odpowiedzi"))
        batch, batch_album = [], None

    try:
        for i, rel in enumerate(todo, 1):
            path = src / rel
            try:
                sha = None
                if not args.no_dedup:
                    sha = sha1_of(path)
                    twin = st.sha_done(sha)
                    if twin:
                        st.mark(rel, "duplicate", sha1=sha, note=f"identyczny z {twin}")
                        continue
                upload_path, note = path, None
                if args.stamp_missing:
                    upload_path, note = stamped_copy(path, rel, tmp_root)
                mime = MIME[path.suffix.lower()]
                token = photos.upload_bytes(upload_path, mime)
                if upload_path != path:
                    upload_path.unlink(missing_ok=True)
            except QuotaExhausted:
                raise
            except Exception as e:  # pojedynczy plik nie zatrzymuje całości
                st.mark(rel, "failed", error=str(e)[:300])
                print(f"  ! {rel}: {e}")
                continue

            album = album_name(rel, args.albums)
            if batch and (album != batch_album or len(batch) >= BATCH_SIZE):
                flush()
            batch_album = album
            batch.append({
                "rel": rel, "token": token, "sha1": sha, "note": note,
                "item": {
                    "description": f"Źródło: Dysk Google / {rel}"[:1000],
                    "simpleMediaItem": {"uploadToken": token, "fileName": path.name},
                },
            })
            done += 1
            if done % 25 == 0:
                rate = done / max(time.time() - started, 1)
                print(f"  [{i}/{len(todo)}] {rate:.2f} plik/s, żądania dziś: {st.used_today()}")
        flush()
    except QuotaExhausted as e:
        print(f"\n⏸  {e} Zatrzymuję się - uruchom ponownie po północy czasu PT (ok. 9:00 w Polsce).")
        try:
            flush()
        except Exception as e2:
            print(f"   (niezflushowane tokeny wygasną, pliki zostaną ponowione: {e2})")
    except KeyboardInterrupt:
        print("\nPrzerwano - zapisuję rozpoczęty batch...")
        try:
            flush()
        except Exception:
            pass
    finally:
        shutil.rmtree(tmp_root, ignore_errors=True)
    print()
    cmd_status(args)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--src", default=DEFAULT_SRC, help="katalog ze zdjęciami (domyślnie 88📸Zdjęcia na zamontowanym Dysku)")
    p.add_argument("--exclude", action="append", default=None, help="regex ścieżki względnej do pominięcia (można wielokrotnie)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scan", help="raport: ile plików/GB/dni, bez wgrywania")
    s.add_argument("--check-dates", action="store_true", help="policz pliki bez daty EXIF (wymaga exiftool)")
    s.set_defaults(fn=cmd_scan)

    u = sub.add_parser("upload", help="wgraj do Google Photos (wznawialne)")
    u.add_argument("--albums", choices=["none", "year", "folder"], default="year",
                   help="albumy: none / year (pierwszy folder, domyślnie) / folder (pełna ścieżka)")
    u.add_argument("--limit", type=int, help="wgraj tylko N plików (pilotaż)")
    u.add_argument("--stamp-missing", action="store_true",
                   help="dla plików bez daty wgraj KOPIĘ z datą z nazwy pliku / roku folderu (exiftool)")
    u.add_argument("--no-dedup", action="store_true", help="pomiń deduplikację po SHA-1")
    u.add_argument("--retry-failed", action="store_true", help="ponów też pliki ze statusem failed")
    u.add_argument("--daily-budget", type=int, default=DEFAULT_DAILY_BUDGET)
    u.set_defaults(fn=cmd_upload)

    t = sub.add_parser("status", help="stan migracji i zużycie kwoty")
    t.set_defaults(fn=cmd_status)

    args = p.parse_args()
    if args.exclude is None:
        args.exclude = DEFAULT_EXCLUDES
    args.fn(args)


if __name__ == "__main__":
    main()
