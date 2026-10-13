"""Trace every number in the day's STUDENT prose to a home in the facts file.

Reads the facts file and every STUDENT .md file and the markdown cells of every STUDENT notebook
under content/W04/D4 (code fences and code cells are skipped, since code prints computed values).
Writes the audit table to internal/ and prints the misses. With --notes it also reads the decks'
speaker notes and prints the numbers there with no home, without writing the table.

    python3 content/W04/D4/internal/C2_W04_D04_facts_audit_INTERNAL.py           write the table
    python3 content/W04/D4/internal/C2_W04_D04_facts_audit_INTERNAL.py --notes   check the notes too
"""
import json
import pathlib
import re
import sys

import yaml

DAY = pathlib.Path(__file__).resolve().parent.parent
NOTES = "--notes" in sys.argv
FACTS = yaml.safe_load((DAY / "internal/C2_W04_D04_facts_INTERNAL.yaml").read_text())
OUT = DAY / "internal/C2_W04_D04_facts_audit_INTERNAL.md"

homes = {}          # canonical number string -> list of ids


def add(key, fid):
    homes.setdefault(key, [])
    if fid not in homes[key]:
        homes[key].append(fid)


def norm(tok):
    """A number as text, commas dropped, trailing zeros after a point dropped."""
    t = tok.replace(",", "")
    if "." in t:
        t = t.rstrip("0").rstrip(".")
    return t


def add_value(v, fid, unit=""):
    if isinstance(v, bool):
        return
    if isinstance(v, (int, float)):
        add(norm(f"{v}"), fid)
        if isinstance(v, float) or unit in ("share", "ratio"):
            if abs(v) < 5:                      # a share: its percent forms
                add(norm(f"{round(100 * v)}"), fid)
                add(norm(f"{100 * v:.1f}"), fid)
                add(norm(f"{v:.2f}"), fid)
            add(norm(f"{round(v)}"), fid)
            add(norm(f"{v:.1f}"), fid)
        if unit == "Rs" and v >= 1e5:
            add(norm(f"{v / 1e5:.1f}"), fid)
    elif isinstance(v, str):
        for t in re.findall(r"\d[\d,]*\.?\d*", v):
            add(norm(t), fid)
    elif isinstance(v, dict):
        for k, x in v.items():
            add_value(x, fid)
    elif isinstance(v, list):
        for x in v:
            add_value(x, fid)


for n in FACTS["numbers"]:
    add_value(n["value"], n["id"], n.get("unit", ""))
    if n.get("printed"):
        add_value(n["printed"], n["id"])
for t in FACTS["toys"]:
    add_value(t["values"], t["id"])
for p in FACTS["public_facts"]:
    add_value(p["facts"], p["id"])
for o in FACTS["from_other_days"]:
    add_value(o["value"], o["id"])
    add_value(o["printed"], o["id"])
for d in FACTS.get("derived", []):
    add_value(d["value"], d["id"])
for k, v in FACTS.get("kalpa", {}).items():           # read only by files used after the lab
    add_value(v, f"kalpa.{k}")
for pl in FACTS.get("plants", []):
    add_value(pl["value"], pl["id"], "share")
    add_value(pl["how"], pl["id"])
tw = FACTS["twelve_rows"]
for k, v in {**tw["hand_counts"], **tw["dashboard_way"], **tw["everyone_way"], **tw["hand_count_percent"],
             **tw["ways_percent"]}.items():
    if isinstance(v, float):
        add(norm(f"{round(v)}"), f"twelve_rows.{k}")
    add_value(v, f"twelve_rows.{k}")
for r in tw["rows"]:
    add_value(r["member_id"][2:], "twelve_rows.member_id")
add_value(FACTS["definitions"], "definitions")
add_value(FACTS["label_line"], "label")
# calendar and case terms the ticket fixes: dates, the release, the sale week, the windows
for k, v in {"release_day": "14", "release_year": "2026", "sale_week": "17 23", "aug_first": "1",
             "sep_last": "30", "sep_13": "13", "sep_28": "28", "sep_7": "7", "sep_21": "21", "zomato_letter": "19 2023",
             "eternal_letter": "22", "swiggy_letter": "30", "kalpa_windows": "20 9 10 30 19"}.items():
    add_value(v, f"calendar.{k}")
# the case's quarters and fixed terms in public-fact sentences
for k, v in {"Q4": "4", "Q8": "8", "Q12": "12", "FY": "23 24 26 27"}.items():
    add_value(v, f"public.{k}")

SKIP_LINE = re.compile(r"^(Week 4, Day 4|Kicker:|```|# |\s*label: \d)")
STRUCTURAL = re.compile(r"\b(S\d+|D\d+|L[1-6]|W4-3|Th[1-6]|T[1-3]|M[1-9]|F[1-6]|R[12])\b|\b(week|chapter|section|part|item|Q|month|day)\s+\d+\b|\b\d+\s+(minutes|minute|cells?)\b|"
                        r"\bC2_W04_D04\w*|\b\d{2}[a-z]?\.(?!\d)|https?://\S+|\[[A-Z]+\]|\bnotebooks? \d+\b|\b0[1-9]\b(?!\.\d)", re.I)
NUM = re.compile(r"(?<![\w.])(\d[\d,]*\.?\d*)(?![\w])")


def texts():
    for p in sorted(DAY.rglob("*_STUDENT.*")):
        if p.suffix == ".md":
            inside = None
            for i, line in enumerate(p.read_text().splitlines(), 1):
                if line.startswith("```"):
                    inside = None if inside else line[3:].strip() or "plain"
                    continue
                if inside and not (NOTES and inside == "notes"):
                    continue
                if NOTES and inside != "notes":
                    continue
                yield p, i, line
        elif p.suffix == ".ipynb" and not NOTES:
            nb = json.loads(p.read_text())
            for ci, c in enumerate(nb["cells"]):
                if c["cell_type"] != "markdown":
                    continue
                inside = False
                for i, line in enumerate("".join(c["source"]).splitlines(), 1):
                    if line.strip().startswith("```"):
                        inside = not inside
                        continue
                    if inside:
                        continue
                    yield p, f"cell {ci} line {i}", line


rows, misses = [], []
for p, where, line in texts():
    if SKIP_LINE.match(line):
        continue
    clean = STRUCTURAL.sub(" ", line)
    for m in NUM.finditer(clean):
        tok = m.group(1).rstrip(".,")
        if not tok or tok in ("0", "1") and len(line) < 3:
            continue
        key = norm(tok)
        ids = homes.get(key)
        rel = p.relative_to(DAY)
        if ids:
            rows.append((tok, str(rel), where, ", ".join(ids[:3]) + (" and more" if len(ids) > 3 else "")))
        else:
            misses.append((tok, str(rel), where, line.strip()[:110]))

out = ["# Week 4 Thursday: the facts audit", "",
       "Every number in the day's STUDENT prose (deck slides, notebook markdown, exercise, note, sheet and "
       "pre-read files), traced to its home in `C2_W04_D04_facts_INTERNAL.yaml`: a `numbers` id, a toy, a "
       "twelve-row count, a public fact with its R2 id, a number copied from another day, or a calendar date "
       "the ticket fixes. Speaker notes, code and code output are left out: notes are the trainer's words and "
       "code prints what it computes from the data. Written by C2_W04_D04_facts_audit_INTERNAL.py.", "",
       f"Numbers traced: {len(rows)}. Numbers with no home: {len(misses)}.", "",
       "| Number | File | Line | Facts id |", "|---|---|---|---|"]
out += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in rows]
if misses:
    out += ["", "## Numbers with no home", "", "| Number | File | Line | Text |", "|---|---|---|---|"]
    out += [f"| {a} | {b} | {c} | {d} |" for a, b, c, d in misses]
if not NOTES:
    OUT.write_text("\n".join(out) + "\n")
print(f"traced {len(rows)}, misses {len(misses)}" + (" (speaker notes)" if NOTES else ""))
for m in misses:
    print(m)

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_facts_audit_INTERNAL.py
#     writes internal/C2_W04_D04_facts_audit_INTERNAL.md and prints "traced N, misses 0" on a clean pack
# a STUDENT slide that says "39 percent" where the facts file holds no 39
#     prints the miss with its file, line and text, and the table gains a "Numbers with no home" section
# python3 content/W04/D4/internal/C2_W04_D04_facts_audit_INTERNAL.py --notes
#     reads only the decks' speaker notes, prints their misses, and leaves the table as it was
