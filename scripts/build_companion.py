"""Inline the shared companion library into a page, so every page stays one file.

A companion page opens from disk with no install and no network, so it cannot load a shared
script. It carries two marked blocks instead, and this fills them from scripts/companion/:

    <style data-c2kit></style>      the look, from c2kit.css
    <script data-c2kit></script>    the diagram builders, from c2kit.js

Run it after editing either library file or starting a new page; a page whose blocks already match
is left alone. --check reports a page whose inlined copy has fallen behind the library.

Usage:
    python3 scripts/build_companion.py content/W01/D1/demos/C2_W01_D01_revenue_tree_STUDENT.html
    python3 scripts/build_companion.py content/W01/D1 --check
"""
import pathlib
import re
import sys

LIB = pathlib.Path(__file__).resolve().parent / "companion"
BLOCKS = [
    (re.compile(r"(<style data-c2kit>)(.*?)(</style>)", re.S), "c2kit.css"),
    (re.compile(r"(<script data-c2kit>)(.*?)(</script>)", re.S), "c2kit.js"),
]


def inline(text):
    """The page with both marked blocks refreshed from the library, and how many were found."""
    found = 0
    for pattern, name in BLOCKS:
        body = (LIB / name).read_text(encoding="utf-8").strip()
        text, n = pattern.subn(lambda m: m.group(1) + "\n" + body + "\n" + m.group(3), text)
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
        new, found = inline(text)
        if not found:
            continue
        if new == text:
            print(f"      {page.name}: library already current")
        elif check:
            print(f"FAIL  {page.name}: the inlined library is older than scripts/companion/")
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
