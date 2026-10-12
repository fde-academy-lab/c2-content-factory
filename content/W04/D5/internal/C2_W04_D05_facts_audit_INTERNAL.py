"""Trace every number in every Friday STUDENT file to an id in the day's facts file.

    python3 content/W04/D5/internal/C2_W04_D05_facts_audit_INTERNAL.py

Reads every STUDENT markdown file (speaker notes and code included, since a learner who opens the
deck file sees them) and every notebook's markdown, code and printed output. A number matches a fact
when the fact's printed form holds it, or when it equals the fact's value, its percent, its lakh or
its crore at the precision it is printed with. Numbers that only count the material itself (a slide,
a chapter, a level, an item, minutes, a date, a year, a file name) are structural and left out.
Writes C2_W04_D05_facts_audit_INTERNAL.md and exits 1 when any number has no home.
"""
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DAY = HERE.parent
FACTS = HERE / "C2_W04_D05_facts_INTERNAL.yaml"
OUT = HERE / "C2_W04_D05_facts_audit_INTERNAL.md"

NUMBER = re.compile(r"(?<![\w.,/-])-?(\d{1,3}(?:,\d{2,3})+|\d+(?:\.\d+)?)(?![\w/])(\s*(?:percent|%|lakh|crore))?")
MONTHS = ("Jan|January|Feb|February|Mar|March|Apr|April|May|Jun|June|Jul|July|Aug|August|Sep|Sept|"
          "September|Oct|October|Nov|November|Dec|December")
BEFORE = re.compile(r"(?:\b(?:Week|week|Day|day|chapter|Chapter|level|Level|Part|part|Item|item|Q|S|D|L|W|F|T|M|Th|R|"
                    r"Panel|panel|round|Round|rung|Rung|step|Step|cell|Cells?|notebook|Notebook|Follow-up|follow-up|"
                    r"Question|question|scene|Scene|Vote|vote|Section|SECTION|Set|set|Task|task|row|rows|seed|"
                    r"Module|module|Build|build|version|v|FY|figure|Figure|section|sections|top|Top)\s?)$")
AFTER = re.compile(r"^\s*(?:minutes?\b|min\b|" + MONTHS + r"\b|slides?\b|items?\b|steps?\b|chapters?\b|"
                   r"sentences?\b|lines?\b|words?\b|levels?\b|groups?\b|parts?\b|cards?\b|columns?\b|letters?\b|"
                   r"seconds?\b|tables?\b|cells?\b|questions?\b|rules?\b|answers?\b|options?\b|follow-ups?\b|"
                   r"moves?\b|checks?\b|pairs?\b|people\b|roles?\b|stakeholders?\b|years?\b)")
YEAR = re.compile(r"^(19|20)\d{2}$")
DATE_NEAR = re.compile(r"(?:\b\d{1,2}\s+(?:" + MONTHS + r")\b|\b(?:" + MONTHS + r")\s+\d{1,2}\b|\d{4}-\d{2}(?:-\d{2})?)")


def facts():
    data = yaml.safe_load(FACTS.read_text(encoding="utf-8"))
    rows = []
    for section, items in data.items():
        for r in items:
            vals = r["value"] if isinstance(r["value"], list) else [r["value"]]
            for v in vals:
                rows.append((r["id"], v, str(r.get("shown", ""))))
    return rows


def matches(token, unit, value, shown):
    if re.search(r"(?<![\d,.])" + re.escape(token) + r"(?![\d,]|\.\d)", shown):
        return True
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    num = float(token.replace(",", ""))
    places = len(token.split(".")[1]) if "." in token else 0
    unit = (unit or "").strip()
    if unit in ("percent", "%"):
        forms = [value * 100, value]
    elif unit == "lakh":
        forms = [value / 1e5, value]
    elif unit == "crore":
        forms = [value / 1e7, value]
    else:
        forms = [value, abs(value), value * 100, abs(value) * 100, value / 1e5, abs(value) / 1e5, value / 1e7]
    for f in forms:
        if abs(round(f, places) - abs(num)) < 1e-9:
            return True
    return False


def learner_lines():
    """(file, where, line, the next line) for every line a learner can see."""
    for p in sorted(DAY.rglob("*_STUDENT.*")):
        if p.parent.name in ("data", "whiteboards"):
            continue
        if p.suffix == ".md":
            text = p.read_text(encoding="utf-8").splitlines()
            for i, line in enumerate(text, start=1):
                yield p, str(i), line, text[i] if i < len(text) else ""
        elif p.suffix == ".ipynb":
            nb = json.loads(p.read_text(encoding="utf-8"))
            for c, cell in enumerate(nb["cells"], start=1):
                src = "".join(cell["source"]).splitlines()
                for j, line in enumerate(src, start=1):
                    yield p, f"cell {c}.{j}", line, src[j] if j < len(src) else ""
                for o in cell.get("outputs", []):
                    t = o.get("text") or (o.get("data") or {}).get("text/plain")
                    if not t:
                        continue
                    t = "".join(t) if isinstance(t, list) else t
                    if t.startswith("<Figure"):
                        continue
                    out = t.splitlines()
                    for j, line in enumerate(out, start=1):
                        yield p, f"cell {c} out {j}", line, out[j] if j < len(out) else ""


def structural(line, m, nxt=""):
    token = m.group(1)
    before, after = line[:m.start()], line[m.end():]
    if not after.strip() and re.match(r"^\s*(?:" + MONTHS + r")\b", nxt):
        return True                                  # a date broken across two lines
    if re.search(r"(?:<=?|>=?)\s*$", before):
        return True                                  # a tolerance or threshold inside a check
    if YEAR.match(token):
        return True
    if BEFORE.search(before) or AFTER.match(after):
        return True
    if re.search(r"(https?://\S*|[\w/.-]*C2_W\d\d_D\d\d_\w*|\.\./\S*|#\S*)$", before):
        return True
    window = line[max(0, m.start() - 12):m.end() + 12]
    for d in DATE_NEAR.finditer(window):
        start = max(0, m.start() - 12)
        if d.start() + start <= m.start() and m.end() <= d.end() + start:
            return True
    if re.match(r"^\s*(?:\)|\.)\s", after) and re.search(r"^\s*$", before):
        return True                                  # a numbered list or option label
    if re.search(r"(?:\bfigsize=\(|\bfontsize=|\brange\(|\bdpi=|\biloc\[|\bshift\(|\bhead\(|\bperiods=|"
                 r"\brotation=|\bwidth=|\bweeks=|\bquantile\(|\bround\(|\bastype|\bcolor|lw=|\bloc=|ncol=|"
                 r"\bsize\b|\bplt\.|\bax\.|\bfig\.|:\.\d|\{\d|\[\d+:|\d+\]|\bprint\(|\bmax\(|\bmin\()", before + token + after[:3]):
        if not re.search(r"\b(?:1\.04|1\.026|650|120|25|0\.82)\b", token):
            return True
    return False


def main():
    F = facts()
    traced, misses = [], []
    for p, where, line, nxt in learner_lines():
        for m in NUMBER.finditer(line):
            token, unit = m.group(1), m.group(2)
            if structural(line, m, nxt):
                continue
            first = [fid for fid, v, shown in F if shown and re.search(
                r"(?<![\d,.])" + re.escape(token) + r"(?![\d,]|\.\d)", shown)]
            ids = first + [fid for fid, v, shown in F if fid not in first and matches(token, unit, v, shown)]
            shown = (token + (unit or "")).strip()
            if ids:
                traced.append((shown, p.name, where, ", ".join(list(dict.fromkeys(ids))[:3])))
            else:
                misses.append((shown, p.name, where, line.strip()[:100]))
    lines = ["# W04 D5 facts audit: every number in a STUDENT file, traced to its facts id", "",
             "Written by C2_W04_D05_facts_audit_INTERNAL.py from the STUDENT files and "
             "C2_W04_D05_facts_INTERNAL.yaml. A number matches when a fact's printed form holds it or "
             "it equals the fact's value, percent, lakh or crore at the precision printed. Structural "
             "numbers (slide, chapter, level, item, minutes, dates, years, code parameters) are left out.", "",
             f"Numbers traced: {len(traced)}. Numbers with no home: {len(misses)}.", "",
             "| Number | File | Line | Facts id |", "|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in traced]
    if misses:
        lines += ["", "## Numbers with no home", "", "| Number | File | Line | Text |", "|---|---|---|---|"]
        lines += [f"| {a} | {b} | {c} | {d.replace('|', '/')} |" for a, b, c, d in misses]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(traced)} numbers traced, {len(misses)} with no home; table at {OUT.name}")
    for a, b, c, d in misses:
        print(f"  MISS {a:>12}  {b}  {c}: {d}")
    sys.exit(1 if misses else 0)


if __name__ == "__main__":
    main()
