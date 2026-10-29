"""Place the openly licensed pictures in the Week 6 explorer, each with its attribution line.

Usage:
    python3 content/W06/D2/4_trainer_only/C2_W06_D02_open_images_INTERNAL.py
    python3 content/W06/D2/4_trainer_only/C2_W06_D02_open_images_INTERNAL.py --fetch
    python3 content/W06/D2/4_trainer_only/C2_W06_D02_open_images_INTERNAL.py --from DIR
    python3 content/W06/D2/4_trainer_only/C2_W06_D02_open_images_INTERNAL.py --check

Decision `w6-open-images` lets a Week 6 pack print an image from Wikimedia Commons when its
licence allows reuse and its attribution line is printed beside it. For every file in PICTURES
this script reads the licence, the author and the file page from the Commons API, refuses any
licence outside ALLOWED, downloads the original file unchanged, and writes it as a data URI into
the page's `<script type="application/json" id="ex-pictures">` block, so the explorer stays one
file that opens with no network. The page's own script prints the attribution line from the same
block. Commons answers HTTP 429 when a shared address asks too often, so every request backs off
and retries, and both the API answer and the files are cached in ~/.cache/c2_open_images.

--fetch fills the cache and leaves the page alone, for a run that has to wait out Commons.
--from DIR takes the files from a folder a person downloaded them into, for an address Commons
refuses under its robot policy; the licence still comes from the Commons API (or its cache), and
each file must match the byte count Commons records for it, wherever it came from.
--check rebuilds nothing: it reads the page's block and fails when a picture is missing, carries
a licence outside ALLOWED, or has no author, file page or checked date.
"""
import base64
import datetime
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = pathlib.Path(__file__).resolve().parent
PAGE = HERE.parent / "3_explorer" / "C2_W06_D02_explorer_STUDENT.html"
CACHE = pathlib.Path.home() / ".cache" / "c2_open_images"
API = "https://commons.wikimedia.org/w/api.php"  # the Commons API, checked 29 October 2026
UA = "c2-content-factory-open-images/1.0 (delivery@fde.academy)"
BLOCK = re.compile(r'(<script type="application/json" id="ex-pictures">)(.*?)(</script>)', re.S)

# The picture's key in the page, and its Commons file. The page decides where each one sits and
# what its caption teaches; this list only says which files are fetched.
PICTURES = {
    "workflow": "File:Machine_learning_workflow_diagram.png",
    "confusion": "File:Confusion_matrix_example.png",
    "mlops": "File:ML_Ops_Venn_Diagram.svg",
}

# Licences that allow reuse in a public repository with an attribution line, as Commons writes
# their short names. Anything else stops the script, and the picture gets redrawn instead.
ALLOWED = {"CC0", "Public domain", "CC BY 2.0", "CC BY 3.0", "CC BY 4.0",
           "CC BY-SA 2.0", "CC BY-SA 3.0", "CC BY-SA 4.0"}


def get(url, tries=6):
    """The bytes at url, backing off on HTTP 429 and 503."""
    wait = 30
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code not in (429, 503) or attempt == tries - 1:
                raise
            print(f"  {e.code} from Commons, waiting {wait} seconds")
            time.sleep(wait)
            wait *= 2


def text_of(meta, key):
    """One extmetadata field as plain text."""
    raw = (meta.get(key) or {}).get("value") or ""
    return html.unescape(re.sub(r"<[^>]+>", "", raw)).strip()


def metadata():
    """The Commons record of every picture, from the cache when it already holds them all."""
    path = CACHE / "meta.json"
    if path.exists():
        cached = json.loads(path.read_text(encoding="utf-8"))
        if all(t in cached for t in PICTURES.values()):
            return cached
    query = {"action": "query", "titles": "|".join(PICTURES.values()), "prop": "imageinfo",
             "iiprop": "url|size|mime|extmetadata", "format": "json"}
    answer = json.loads(get(API + "?" + urllib.parse.urlencode(query)))
    names = {n["to"]: n["from"] for n in answer["query"].get("normalized", [])}
    records = {}
    for page in answer["query"]["pages"].values():
        if "imageinfo" not in page:
            sys.exit(f"Commons has no file called {page['title']}")
        info = page["imageinfo"][0]
        records[names.get(page["title"], page["title"])] = {
            "title": page["title"], "url": info["url"], "page": info["descriptionurl"],
            "width": info["width"], "height": info["height"], "mime": info["mime"], "size": info["size"],
            "licence": text_of(info["extmetadata"], "LicenseShortName"),
            "licence_url": text_of(info["extmetadata"], "LicenseUrl"),
            "author": text_of(info["extmetadata"], "Artist"),
        }
    CACHE.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, indent=1), encoding="utf-8")
    return records


def original(record, folder=None):
    """The file itself, unchanged, from a given folder, the cache or Commons, checked by size."""
    name = pathlib.Path(urllib.parse.unquote(urllib.parse.urlsplit(record["url"]).path)).name
    path = CACHE / name
    if not path.exists():
        if folder:
            data = (pathlib.Path(folder) / name).read_bytes()
        else:
            time.sleep(5)
            data = get(record["url"])
        if record.get("size") and len(data) != record["size"]:
            sys.exit(f"{name} is {len(data):,} bytes, and Commons records {record['size']:,}; it is not the original")
        CACHE.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    return path.read_bytes()


def build(folder=None):
    records = metadata()
    checked = datetime.date.today().strftime("%-d %B %Y")
    block = {}
    for key, title in PICTURES.items():
        rec = records[title]
        if rec["licence"] not in ALLOWED:
            sys.exit(f"{title} is licensed {rec['licence']!r}, which is not in ALLOWED; redraw it instead")
        if not rec["author"]:
            sys.exit(f"{title} names no author, so no attribution line can be printed")
        data = original(rec, folder)
        if rec["mime"] == "image/svg+xml" and re.search(rb"<script|href=\"https?:", data):
            sys.exit(f"{title} is an SVG that runs a script or loads from the network")
        name = rec["title"].removeprefix("File:").rsplit(".", 1)[0].replace("_", " ")
        licence = rec["licence"] + (f" ({rec['licence_url']})" if rec["licence_url"] else "")
        block[key] = {
            "name": name, "author": rec["author"], "licence": rec["licence"], "page": rec["page"],
            "checked": checked, "width": rec["width"], "height": rec["height"],
            # The attribution line the page prints, title, author, source and licence, with the
            # date the licence was read on the same line, which is where verify.py looks for it.
            "credit": f'"{name}" by {rec["author"]}, Wikimedia Commons, {licence}, {rec["page"]}, checked {checked}',
            "src": f"data:{rec['mime']};base64," + base64.b64encode(data).decode("ascii"),
        }
        print(f"{key}: {block[key]['name']} by {rec['author']}, {rec['licence']}, {len(data):,} bytes")
    page = PAGE.read_text(encoding="utf-8")
    if not BLOCK.search(page):
        sys.exit(f"{PAGE.name} has no ex-pictures block")
    body = json.dumps(block, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    PAGE.write_text(BLOCK.sub(lambda m: m.group(1) + body + m.group(3), page, count=1), encoding="utf-8")
    print(f"wrote {len(block)} pictures into {PAGE.name}")


def fetch():
    records = metadata()
    for key, title in PICTURES.items():
        print(f"{key}: {len(original(records[title])):,} bytes cached")


def check():
    m = BLOCK.search(PAGE.read_text(encoding="utf-8"))
    if not m:
        sys.exit(f"FAIL {PAGE.name} has no ex-pictures block")
    block = json.loads(m.group(2) or "{}")
    fails = []
    for key in PICTURES:
        pic = block.get(key)
        if not pic:
            fails.append(f"{key} is missing")
            continue
        if pic.get("licence") not in ALLOWED:
            fails.append(f"{key} carries licence {pic.get('licence')!r}")
        for field in ("author", "page", "checked", "credit", "src"):
            if not pic.get(field):
                fails.append(f"{key} has no {field}")
    for f in fails:
        print("FAIL", f)
    print("PASS" if not fails else f"{len(fails)} failures")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--check" in args:
        check()
    elif "--fetch" in args:
        fetch()
    else:
        build(args[args.index("--from") + 1] if "--from" in args else None)

# Test inputs and expected outcomes:
# 1. No argument, Commons reachable, cache empty: prints one line per picture with its author,
#    licence and size, then "wrote 3 pictures into C2_W06_D02_explorer_STUDENT.html".
# 2. No argument, Commons answering 429: prints "429 from Commons, waiting 30 seconds", doubles the
#    wait up to five times, then either succeeds as in 1 or stops with the HTTP error.
# 3. --fetch, Commons reachable: prints "workflow: 26,499 bytes cached" and one line for each of
#    the other two, and leaves the page unchanged.
# 4. --check after 1: prints "PASS" and exits 0.
# 5. --check on a page whose block is empty ({}): prints "FAIL workflow is missing" and the other
#    two, then "3 failures", and exits 1.
# 6. --from ~/Downloads holding the three files as Commons names them: prints the three lines of
#    1 without touching Commons' file host. A file of the wrong size (a thumbnail, say) stops with
#    "... is 12,345 bytes, and Commons records 34,819; it is not the original".
# 7. A PICTURES entry whose Commons licence is, say, "Fair use": stops with "... is not in
#    ALLOWED; redraw it instead" and leaves the page unchanged.
