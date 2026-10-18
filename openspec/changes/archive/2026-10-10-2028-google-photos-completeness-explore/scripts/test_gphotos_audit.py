"""Testy gphotos_audit.py na syntetycznym Takeoucie (uruchom: python3 test_gphotos_audit.py)."""
import calendar
import csv
import json
import struct
import tempfile
import time
import unittest
import zipfile
from pathlib import Path

import gphotos_audit as ga


def make_jpeg(taken: str | None, payload: bytes) -> bytes:
    """Minimalny JPEG z opcjonalnym EXIF DateTimeOriginal ('YYYY:MM:DD HH:MM:SS')."""
    out = b"\xff\xd8"
    if taken:
        s = taken.encode() + b"\x00"  # 20 bajtów
        # TIFF little-endian: IFD0 z jednym wpisem 0x8769 -> Exif IFD z jednym wpisem 0x9003
        ifd0_off = 8
        exif_off = ifd0_off + 2 + 12 + 4
        data_off = exif_off + 2 + 12 + 4
        tiff = b"II*\x00" + struct.pack("<I", ifd0_off)
        tiff += struct.pack("<H", 1) + struct.pack("<HHII", 0x8769, 4, 1, exif_off) + struct.pack("<I", 0)
        tiff += struct.pack("<H", 1) + struct.pack("<HHII", 0x9003, 2, len(s), data_off) + struct.pack("<I", 0)
        tiff += s
        seg = b"Exif\x00\x00" + tiff
        out += b"\xff\xe1" + struct.pack(">H", len(seg) + 2) + seg
    return out + b"\xff\xda\x00\x02" + payload + b"\xff\xd9"


def meta(title: str, taken_utc: int) -> str:
    return json.dumps({"title": title, "photoTakenTime": {"timestamp": str(taken_utc)}})


class AuditTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.local = self.root / "local"
        (self.local / "2009").mkdir(parents=True)
        self.db = str(self.root / "idx.sqlite")

        # 8 mar 2009 17:15:37 czasu lokalnego (CET = UTC+1) -> UTC 16:15:37
        self.exif = "2009:03:08 17:15:37"
        utc = calendar.timegm(time.strptime("2009:03:08 16:15:37", "%Y:%m:%d %H:%M:%S"))

        a = make_jpeg(self.exif, b"A" * 500)          # identyczny w Takeoucie -> sha256
        b = make_jpeg("2009:03:09 10:00:00", b"B" * 400)   # brak w Takeoucie -> missing
        c = make_jpeg(None, b"C" * 300)                # ta sama nazwa i rozmiar, inna treść -> name+size
        d = make_jpeg(self.exif, b"D" * 600)           # w Takeoucie inna treść/rozmiar, ale ten sam czas -> name+time
        e = make_jpeg("2001:01:01 00:00:00", b"E" * 200)   # nazwa jest, ale czas inny -> name-only
        f = make_jpeg(self.exif, b"F" * 250)           # w Takeoucie jako -edited z JSON-em oryginału
        for n, data in [("a.jpg", a), ("b.jpg", b), ("c.jpg", c), ("d.jpg", d), ("e.jpg", e), ("f.jpg", f)]:
            (self.local / "2009" / n).write_bytes(data)
        (self.local / "notes.txt").write_text("nie multimedia")

        self.takeout = self.root / "takeout"
        self.takeout.mkdir()
        base = "Takeout/Google Photos/Photos from 2009/"
        with zipfile.ZipFile(self.takeout / "takeout-001.zip", "w") as z:
            z.writestr(base + "a.jpg", a)
            z.writestr(base + "a.jpg.supplemental-metadata.json", meta("a.jpg", utc))
            z.writestr(base + "c.jpg", make_jpeg(None, b"X" * 300))
            assert len(make_jpeg(None, b"X" * 300)) == len(c)
            z.writestr(base + "c.jpg.json", meta("c.jpg", utc))
            z.writestr(base + "d.jpg", make_jpeg(self.exif, b"Z" * 100))
            z.writestr(base + "d.jpg.json", meta("d.jpg", utc))
            z.writestr(base + "e.jpg", make_jpeg(None, b"Q" * 999))
            z.writestr(base + "e.jpg.json", meta("e.jpg", utc))
        with zipfile.ZipFile(self.takeout / "takeout-002.zip", "w") as z:
            z.writestr(base + "f-edited.jpg", make_jpeg(None, b"Y" * 77))
            z.writestr(base + "f.jpg.json", meta("f.jpg", utc))

    def tearDown(self):
        self.tmp.cleanup()

    def run_all(self):
        ga.main(["--db", self.db, "index-local", str(self.local)])
        ga.main(["--db", self.db, "index-takeout", str(self.takeout)])
        con = ga.open_db(self.db)
        return {Path(p).name: lvl for p, lvl in ga.classify(con)}

    def test_exif_parser(self):
        p = self.local / "2009" / "a.jpg"
        got = ga.read_exif_taken(str(p))
        self.assertEqual(got, calendar.timegm(time.strptime(self.exif, "%Y:%m:%d %H:%M:%S")))
        self.assertIsNone(ga.read_exif_taken(str(self.local / "2009" / "c.jpg")))

    def test_classification(self):
        res = self.run_all()
        self.assertEqual(res, {
            "a.jpg": "sha256",
            "b.jpg": "missing",
            "c.jpg": "name+size",
            "d.jpg": "name+time",
            "e.jpg": "name-only",
            "f.jpg": "name+time",
        })

    def test_resume_skips_done_archives(self):
        self.run_all()
        con = ga.open_db(self.db)
        n1 = con.execute("SELECT COUNT(*) FROM takeout").fetchone()[0]
        ga.main(["--db", self.db, "index-takeout", str(self.takeout)])
        n2 = con.execute("SELECT COUNT(*) FROM takeout").fetchone()[0]
        self.assertEqual(n1, n2)

    def test_report_files(self):
        self.run_all()
        out = self.root / "raport"
        ga.main(["--db", self.db, "report", "--source", "local", "--out", str(out)])
        with open(out / "missing.csv", newline="") as f:
            rows = list(csv.reader(f))[1:]
        self.assertEqual([Path(r[0]).name for r in rows], ["b.jpg"])

    def test_drive_flow(self):
        """index-drive na atrapie klienta: ścieżki, filtr po folderze, dopasowanie po md5 i czasie."""
        import hashlib
        a = (self.local / "2009" / "a.jpg").read_bytes()
        b = (self.local / "2009" / "b.jpg").read_bytes()
        d = (self.local / "2009" / "d.jpg").read_bytes()
        md5 = lambda x: hashlib.md5(x).hexdigest()

        class FakeDrive:
            def __init__(self, *_a, **_k):
                pass

            def list_all(self, q, fields, on_page=None):
                if "name='Zdjęcia'" in q:  # segment folderu głównego
                    yield {"id": "F1", "name": "Zdjęcia"}
                elif q.startswith("mimeType='application/vnd.google-apps.folder'"):
                    yield {"id": "F1", "name": "Zdjęcia", "parents": ["root"]}
                    yield {"id": "F2", "name": "2009", "parents": ["F1"]}
                    yield {"id": "F3", "name": "inne", "parents": ["root"]}
                else:
                    yield {"id": "1", "name": "a.jpg", "size": str(len(a)), "md5Checksum": md5(a), "parents": ["F2"]}
                    yield {"id": "2", "name": "b.jpg", "size": str(len(b)), "md5Checksum": md5(b), "parents": ["F2"]}
                    # d.jpg: inna treść niż w Takeoucie, ale ten sam EXIF-owy czas -> name+time
                    yield {"id": "3", "name": "d.jpg", "size": str(len(d)), "md5Checksum": md5(d), "parents": ["F2"],
                           "imageMediaMetadata": {"time": self.exif, "width": 3264, "height": 2448,
                                                  "cameraModel": "Canon PowerShot A580"}}
                    yield {"id": "4", "name": "poza.jpg", "size": "1", "md5Checksum": "x", "parents": ["F3"]}

        FakeDrive.exif = self.exif
        original = ga.DriveClient
        ga.DriveClient = FakeDrive
        try:
            ga.main(["--db", self.db, "index-drive", "--use-api", "Zdjęcia"])
        finally:
            ga.DriveClient = original
        ga.main(["--db", self.db, "index-takeout", str(self.takeout)])
        con = ga.open_db(self.db)
        paths = [r[0] for r in con.execute("SELECT path FROM drive ORDER BY path")]
        self.assertEqual(paths, ["Zdjęcia/2009/a.jpg", "Zdjęcia/2009/b.jpg", "Zdjęcia/2009/d.jpg"])
        res = {Path(p).name: lvl for p, lvl in ga.classify(con, "drive")}
        self.assertEqual(res, {"a.jpg": "md5", "b.jpg": "missing", "d.jpg": "name+time"})
        self.assertEqual(con.execute("SELECT camera, width FROM drive WHERE name='d.jpg'").fetchone(),
                         ("Canon PowerShot A580", 3264))

    def test_json_media_name(self):
        f = ga.json_media_name
        self.assertEqual(f("IMG_1.jpg.json"), "IMG_1.jpg")
        self.assertEqual(f("IMG_1.jpg.supplemental-metadata.json"), "IMG_1.jpg")
        self.assertEqual(f("IMG_1.jpg.supplemental-metad.json"), "IMG_1.jpg")
        self.assertEqual(f("IMG_1.jpg(1).json"), "IMG_1(1).jpg")
        self.assertEqual(f("IMG_1.jpg.supplemental-metadata(1).json"), "IMG_1(1).jpg")

    def test_time_matches(self):
        self.assertTrue(ga.time_matches(1000 + 3600, 1000))     # CET
        self.assertTrue(ga.time_matches(1000 - 5 * 3600, 1000))  # strefa ujemna
        self.assertFalse(ga.time_matches(1000 + 1234, 1000))     # nie pełna ćwiartka godziny
        self.assertFalse(ga.time_matches(1000 + 20 * 3600, 1000))  # >14h


if __name__ == "__main__":
    unittest.main()
