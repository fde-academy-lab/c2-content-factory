"""Trace every number in every STUDENT file to an id in the day's facts file.

Run from the repository root:
    python3 content/W04/D3/internal/C2_W04_D03_facts_audit_INTERNAL.py

Reads the markdown of every deck, exercise, note, sheet, take-home, quiz and pre-read, and the
markdown cells and printed outputs of every notebook. A number matches a fact when it equals the
fact's value, its percent, its lakh or its count at the precision the number is printed with. A
number that only counts the material itself (a slide, a week, a step, minutes, a date) is
structural and is listed as such. Writes C2_W04_D03_facts_audit_INTERNAL.md and exits 1 when any
number has no home.
"""
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DAY = HERE.parent
FACTS = HERE / "C2_W04_D03_facts_INTERNAL.yaml"
OUT = HERE / "C2_W04_D03_facts_audit_INTERNAL.md"

NUMBER = re.compile(r"(?<![\w.])(?:Rs\s?)?(\d{1,3}(?:,\d{2,3})+|\d+(?:\.\d+)?)(\s*(?:percent|%|lakh|crore))?")
MONTHS = r"(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)"
STRUCTURAL = [
    re.compile(r"\b(Week|week|Day|day|chapter|Chapter|slot|Slot|slots|level|Level|part|Part|Item|item|Items|items|Step|step|Q|S|D|L|W|M|T|Th|F|R|Panel|panel|group|Group|groups|Groups|Session|session|round|Round|line|lines|card|cards|Question|question|notebook|Notebook|cell|cells)\s?$"),
]
AFTER_STRUCT = re.compile(r"^\s*(minutes?|min\b|" + MONTHS + r"|slides?\b|questions?\b|items\b|steps?\b|chapters?\b|sentences?\b|lines\b|words\b|levels\b|groups\b|parts\b|moves\b|counts\b|doubts\b|decisions\b|fields\b|cards\b|tables\b|columns\b|letters\b|seconds\b|weeks\b|days\b|hours?\b|tickets\b|companies\b)")
YEAR = re.compile(r"^(19|20)\d{2}$")


def facts():
    data = yaml.safe_load(FACTS.read_text(encoding="utf-8"))
    out = []
    for section, rows in data.items():
        for r in rows:
            if isinstance(r["value"], (int, float)):
                out.append((r["id"], float(r["value"]), section, str(r.get("shown", ""))))
    return out


def decimals(token):
    return len(token.split(".")[1]) if "." in token else 0


def matches(token, unit, value):
    num = float(token.replace(",", ""))
    d = decimals(token)
    forms = []
    if unit and unit.strip() in ("percent", "%"):
        forms = [value * 100, value]
    elif unit and unit.strip() == "lakh":
        forms = [value / 1e5]
    elif unit and unit.strip() == "crore":
        forms = [value / 1e7]
    else:
        forms = [value, value * 100]
    for f in forms:
        if abs(round(f, d) - num) < 1e-9:
            return True
        # a rupee amount written in thousands with a comma, or a count rounded the same way
        if d == 0 and abs(f - num) < 0.5:
            return True
    return False


def texts():
    """(file, line number, text) for every learner-visible line."""
    for p in sorted(DAY.rglob("*_STUDENT.*")):
        if p.parent.name in ("data", "whiteboards") or p.suffix not in (".md", ".ipynb"):
            continue
        if p.suffix == ".md":
            inside_code = False
            for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
                if line.strip().startswith("```"):
                    fence = line.strip()[3:]
                    if not inside_code and fence in ("python", "sql", "notes"):
                        inside_code = fence
                    elif inside_code:
                        inside_code = False
                    continue
                if inside_code:
                    continue
                yield p, i, line
        else:
            nb = json.loads(p.read_text(encoding="utf-8"))
            for c_no, cell in enumerate(nb["cells"], start=1):
                if cell["cell_type"] == "markdown":
                    for j, line in enumerate("".join(cell["source"]).splitlines(), start=1):
                        yield p, f"cell {c_no}.{j}", line
                else:
                    for o in cell.get("outputs", []):
                        t = o.get("text") or o.get("data", {}).get("text/plain")
                        if not t:
                            continue
                        t = "".join(t) if isinstance(t, list) else t
                        if t.startswith("<Figure"):
                            continue
                        for j, line in enumerate(t.splitlines(), start=1):
                            yield p, f"cell {c_no} output {j}", line


def main():
    F = facts()
    rows, misses = [], []
    for p, where, line in texts():
        for m in NUMBER.finditer(line):
            token, unit = m.group(1), m.group(2) or ""
            before = line[:m.start()]
            after = line[m.end():]
            if YEAR.match(token) or STRUCTURAL[0].search(before) or AFTER_STRUCT.match(after):
                continue
            if re.search(r"(C\d{0,5}|KR-\d{0,4}|PC\d{0,4}|P0{0,2})$", before) or "http" in line:
                continue
            # A fact printed in a rounded form, such as "about 433,000", also matches the number
            # exactly as that form prints it.
            in_shown = re.compile(r"(?<![\d,.])" + re.escape(token) + r"(?![\d,]|\.\d)")
            ids = [(0 if shown_form and shown_form in line else 1, fid)
                   for fid, v, _, shown_form in F
                   if matches(token, unit, v) or (shown_form.startswith("about ") and in_shown.search(shown_form))]
            ids = [fid for _, fid in sorted(ids)]
            shown = (("Rs " if m.group(0).startswith("Rs") else "") + token + unit).strip()
            if ids:
                rows.append((shown, p.name, where, ", ".join(ids[:3])))
            else:
                misses.append((shown, p.name, where, line.strip()[:90]))
    lines = ["# W04 D3 facts audit: every number in a STUDENT file, traced to its facts id", "",
             "Written by C2_W04_D03_facts_audit_INTERNAL.py from the STUDENT files and "
             "C2_W04_D03_facts_INTERNAL.yaml. A number matches when it equals a fact's value, "
             "percent, lakh or count at the precision printed. Structural numbers (slide, week, "
             "step, minutes, dates, ids) are left out.", "",
             f"Numbers traced: {len(rows)}. Numbers with no home: {len(misses)}.", "",
             "| Number | File | Line | Facts id |", "|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
    if misses:
        lines += ["", "## Numbers with no home", "", "| Number | File | Line | Text |", "|---|---|---|---|"]
        lines += [f"| {a} | {b} | {c} | {d.replace('|', '/')} |" for a, b, c, d in misses]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} numbers traced, {len(misses)} with no home; table at {OUT.name}")
    for a, b, c, d in misses:
        print(f"  MISS {a:>12}  {b}  {c}: {d}")
    sys.exit(1 if misses else 0)


if __name__ == "__main__":
    main()
