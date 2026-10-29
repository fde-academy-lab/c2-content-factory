"""Inline the shared companion library into a page, so every page stays one file.

A companion page opens from disk with no install and no network, so it cannot load a shared
script. It carries marked blocks instead, and this fills them from scripts/companion/:

    <style data-c2kit></style>      the Week 1 to 4 look, from c2kit.css
    <script data-c2kit></script>    the Week 1 to 4 diagram builders, from c2kit.js

    <style data-w5kit></style>      the Week 5 kit's look, from w5kit.css
    <script data-w5kit></script>    the Week 5 kit's components, from w5kit.js
    <script type="application/json" data-w5data="../../4_trainer_only/C2_W05_D01_explorer_data_INTERNAL.json"></script>
                                    the day's numbers, from the JSON file the attribute names,
                                    read relative to the page's own folder

Run it after editing a library file, after the day's data script rewrites its JSON, or after
starting a new page; a page whose blocks already match is left alone. --check reports a page whose
inlined copy has fallen behind the library or behind its JSON, and a data block whose file is
missing or does not parse.

Usage:
    python3 scripts/build_companion.py content/W01/D1/demos/C2_W01_D01_revenue_tree_STUDENT.html
    python3 scripts/build_companion.py content/W01/D1 --check
    python3 scripts/build_companion.py scripts/companion/demo/w5kit_demo_INTERNAL.html
"""
import json
import pathlib
import re
import sys

LIB = pathlib.Path(__file__).resolve().parent / "companion"
BLOCKS = [
    (re.compile(r"(<style data-c2kit>)(.*?)(</style>)", re.S), "c2kit.css"),
    (re.compile(r"(<script data-c2kit>)(.*?)(</script>)", re.S), "c2kit.js"),
    (re.compile(r"(<style data-w5kit>)(.*?)(</style>)", re.S), "w5kit.css"),
    (re.compile(r"(<script data-w5kit>)(.*?)(</script>)", re.S), "w5kit.js"),
]
DATA = re.compile(r"(<script\b[^>]*\bdata-w5data=\"([^\"]+)\"[^>]*>)(.*?)(</script>)", re.S)


class DataError(Exception):
    pass


def library(name):
    body = (LIB / name).read_text(encoding="utf-8").strip()
    if name.endswith(".js") and "</script" in body.lower():
        raise DataError(f"{name} contains a closing script tag, which would end the inlined block early")
    return body


def data_body(page, rel):
    """The JSON the data block names, compacted and made safe to sit inside a script tag."""
    path = (page.parent / rel).resolve()
    if not path.exists():
        raise DataError(f"the data block names {rel}, which does not exist beside the page")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise DataError(f"{rel} is not valid JSON ({e})")
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return text.replace("</", "<\\/")


def inline(text, page=None):
    """The page with every marked block refreshed, and how many blocks were found."""
    found = 0
    for pattern, name in BLOCKS:
        if not pattern.search(text):
            continue
        body = library(name)
        text, n = pattern.subn(lambda m: m.group(1) + "\n" + body + "\n" + m.group(3), text)
        found += n
    if page is not None:
        def fill(m):
            return m.group(1) + data_body(page, m.group(2)) + m.group(4)
        text, n = DATA.subn(fill, text)
        found += n
    return text, found


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(2)
    target = pathlib.Path(args[0])
    pages = [target] if target.is_file() else sorted(target.rglob("*.html"))
    stale = 0
    for page in pages:
        text = page.read_text(encoding="utf-8")
        try:
            new, found = inline(text, page)
        except DataError as e:
            print(f"FAIL  {page.name}: {e}")
            stale += 1
            continue
        if not found:
            continue
        if new == text:
            print(f"      {page.name}: library already current")
        elif check:
            print(f"FAIL  {page.name}: the inlined library or data is older than its source")
            stale += 1
        else:
            page.write_text(new, encoding="utf-8")
            print(f"      {page.name}: library inlined")
    sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# python3 scripts/build_companion.py content/W01/D1/demos/C2_W01_D01_revenue_tree_STUDENT.html
#     Fills the page's <style data-c2kit> and <script data-c2kit> blocks from scripts/companion/
#     and prints "library inlined"; run again, it prints "library already current".
# python3 scripts/build_companion.py content/W01/D1 --check
#     Exit 0 when every page's inlined copy matches the library, exit 1 naming each stale page.
# A page with neither marked block
#     Is skipped silently, so older pages that inline nothing are left exactly as they are.
# python3 scripts/build_companion.py scripts/companion/demo/w5kit_demo_INTERNAL.html
#     Fills the w5kit style and script blocks and the data block from
#     w5kit_demo_data_INTERNAL.json beside it; a second run prints "library already current".
# A page whose data-w5data names a missing file, or a file that does not parse
#     One FAIL line naming the file and the reason, the page left unwritten, and exit 1.
# The day's JSON changed after the page was built, then --check
#     FAIL naming the page, because the inlined data block no longer matches the file.
