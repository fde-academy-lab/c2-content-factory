"""Trace every number in every Tuesday STUDENT file to an id in Tuesday's facts file.

Run from the repository root, after the generator:
    python3 content/W04/D2/internal/C2_W04_D02_facts_audit_INTERNAL.py

Reads the prose of every STUDENT markdown file (outside code and notes fences) and the markdown cells
and printed outputs of the notebook. A number has a home when it equals a value anywhere in the facts
file (a number, a Monday id, a public fact, an assumption or its range, a toy, a twelve-row or weekly
value) at the precision it is printed, read as itself, a percent, a lakh, a crore, a million or a
billion. Numbers that only count the material (slides, levels, items, chapters, minutes, dates, years,
steps) are structural and are left out. Writes C2_W04_D02_facts_audit_INTERNAL.md and exits 1 when a
number has no home.
"""
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DAY = HERE.parent
FACTS = HERE / "C2_W04_D02_facts_INTERNAL.yaml"
OUT = HERE / "C2_W04_D02_facts_audit_INTERNAL.md"

NUMBER = re.compile(r"(?<![\w./-])(\d{1,3}(?:,\d{2,3})+|\d+(?:\.\d+)?)(?![\w/])"
                    r"(\s*(?:percent|%|lakh|crore|million|billion))?")
MONTH = (r"(?:January|February|March|April|May|June|July|August|September|October|November|December|"
         r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)")
BEFORE_STRUCT = re.compile(r"(?:\b(?:Week|week|Day|day|chapter|Chapter|chapters|level|Level|Levels|levels|"
                           r"part|Part|Item|item|items|Step|step|Panel|panel|Move|move|round|Round|"
                           r"Card|card|Appendix|appendix|cell|cells|SECTION|Section|section|Questions|"
                           r"questions|Question|question|transcript|Transcript|Slide|slide|slides|"
                           r"Version|version|scene|scenes|Scene|Scenes|top|Top)\s|"
                           r"\b(?:S|D|L|Q|P|T|M|W|F|R|Th|v)|\bFY|\bQ)$")
AFTER_STRUCT = re.compile(r"^\s*(?:minutes?\b|min\b|" + MONTH + r"\b|slides?\b|questions?\b|items?\b|"
                          r"steps?\b|chapters?\b|sentences?\b|lines\b|words\b|levels\b|parts\b|moves\b|"
                          r"seconds\b|weeks?\b|days?\b|hours?\b|columns\b|letters\b|rounds\b|seats\b|"
                          r"panels\b|figures?\b|blocks\b|dots\b|pages?\b|roles\b|cards\b|groups?\b|"
                          r"rows\b|tables\b|reads\b|numbers\b|elements\b|denominators\b|devices\b|"
                          r"criteria\b|follow-ups\b|transcripts\b|estimates\b|answers\b|options\b|"
                          r"to \d|of \d|x\b|years?\b|months?\b|minute\b)")
DATE = re.compile(r"\b\d{1,2}\s+" + MONTH + r"\b|\b" + MONTH + r"\s+\d{4}\b|\b(?:19|20)\d{2}\b")
SKIP_LINE = re.compile(r"https?://|^\s*\|?\s*-{3}")
LISTNUM = re.compile(r"^\s*\d+[.)]\s")


def walk(node, path, out):
    if isinstance(node, bool) or node is None:
        return
    if isinstance(node, (int, float)):
        out.append((path, float(node)))
    elif isinstance(node, dict):
        for k, v in node.items():
            walk(v, f"{path}.{k}" if path else str(k), out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            label = v.get("id") if isinstance(v, dict) and "id" in v else str(i)
            walk({kk: vv for kk, vv in v.items() if kk != "id"} if isinstance(v, dict) else v,
                 f"{path}.{label}", out)


def facts():
    data = yaml.safe_load(FACTS.read_text(encoding="utf-8"))
    out = []
    for section in ("numbers", "monday_ids_reused", "public_facts", "assumptions", "toys",
                    "twelve_rows", "weekly_series", "kalpa", "programme"):
        walk(data.get(section), section, out)
    return out


def decimals(token):
    return len(token.split(".")[1]) if "." in token else 0


def forms(unit, value):
    """The ways a stored value can be printed. A value stored in crore, lakh or million (an id that
    ends _crore, or a count kept in millions) also matches a token printed with that unit."""
    unit = (unit or "").strip()
    if unit in ("percent", "%"):
        return [value, value * 100, abs(value), abs(value) * 100]
    scale = {"lakh": 1e5, "crore": 1e7, "million": 1e6, "billion": 1e9}.get(unit)
    if scale:
        return [value / scale, value]
    out = [value, abs(value)]
    if abs(value) < 1:
        out.append(abs(value) * 100)  # a share printed as a percent whose unit wrapped to the next line
    return out


def matches(token, unit, value):
    num = float(token.replace(",", ""))
    d = decimals(token)
    for f in forms(unit, value):
        if abs(round(f, d) - num) < 1e-9:
            return True
        if d == 0 and num >= 100 and abs(f - num) <= max(0.5, 0.005 * num) and unit in (None, ""):
            return True  # a count printed rounded, such as 8,300 for 8,333 or 5,700 for 5,704
        if d == 0 and num >= 100 and round(f, -2) == num and unit in (None, ""):
            return True
    return False


def texts():
    for p in sorted(DAY.rglob("*_STUDENT.*")):
        if p.parent.name in ("data", "whiteboards") or p.suffix not in (".md", ".ipynb"):
            continue
        if p.suffix == ".md":
            fence = None
            for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), start=1):
                s = line.strip()
                if s.startswith("```"):
                    fence = None if fence else (s[3:] or "code")
                    continue
                if fence in ("notes", "python", "code", "mermaid"):
                    continue
                if fence in ("cards", "stats", "timeline", "bar"):
                    yield p, i, line
                    continue
                if fence:
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
                            yield p, f"cell {c_no} out {j}", line


def main():
    F = facts()
    rows, misses = [], []
    for p, where, line in texts():
        if SKIP_LINE.search(line):
            continue
        clean = DATE.sub(" ", line)
        clean = re.sub(r"\bC2_W\d\d_D\d\d_\w+", " ", clean)
        clean = re.sub(r"\barXiv \d+\.\d+", " ", clean)      # a citation id, never a quantity
        clean = re.sub(r"`[^`]*`", " ", clean)
        for m in NUMBER.finditer(clean):
            token, unit = m.group(1), (m.group(2) or "").strip()
            before, after = clean[:m.start()], clean[m.end():]
            if BEFORE_STRUCT.search(before) or AFTER_STRUCT.match(after):
                continue
            if LISTNUM.match(clean) and m.start() == clean.index(token):
                continue
            if re.match(r"^\s*(?:and|or|to)\s+\d", after) and not unit and float(token.replace(",", "")) < 7:
                continue
            ids = [path for path, v in F if matches(token, unit, v)]
            shown = (token + (" " + unit if unit else "")).strip()
            if ids:
                rows.append((shown, p.name, where, ids[0]))
            else:
                misses.append((shown, p.name, where, line.strip()[:100]))
    lines = ["# W04 D2 facts audit: every number in a STUDENT file, traced to its facts id", "",
             "Written by C2_W04_D02_facts_audit_INTERNAL.py from the STUDENT files and "
             "C2_W04_D02_facts_INTERNAL.yaml. A number matches when it equals a value in the facts file "
             "at the precision printed, read as itself, a percent, a lakh, a crore, a million or a "
             "billion. Structural numbers (slide, level, item, chapter, minutes, dates, years) and the "
             "speaker notes are left out.", "",
             f"Numbers traced: {len(rows)}. Numbers with no home: {len(misses)}.", "",
             "| Number | File | Line | Facts id |", "|---|---|---|---|"]
    lines += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
    if misses:
        lines += ["", "## Numbers with no home", "", "| Number | File | Line | Text |", "|---|---|---|---|"]
        lines += [f"| {a} | {b} | {c} | {d.replace('|', '/')} |" for a, b, c, d in misses]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} numbers traced, {len(misses)} with no home; table at {OUT.name}")
    for a, b, c, d in misses:
        print(f"  MISS {a:>14}  {b}  {c}: {d}")
    sys.exit(1 if misses else 0)


if __name__ == "__main__":
    main()
