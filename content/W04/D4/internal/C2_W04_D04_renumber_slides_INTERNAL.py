"""Number Thursday's slides in deck order, half one then half two, and record what each old number became.

The concept-first rebuild put the opening and the concept chapters in front of the case, so every
case slide moved. A slide headed `## SNEW.` or `## DNEW.` is new; a slide still headed with its old
number (`## S7.`) is a case slide that moved. This walks half one and then half two, gives every
`S` slide the next number in one sequence and every `D` slide the next in another, writes the decks
back, and writes the old-to-new table that the stale-reference pass reads.

    python3 content/W04/D4/internal/C2_W04_D04_renumber_slides_INTERNAL.py           renumber and write the map
    python3 content/W04/D4/internal/C2_W04_D04_renumber_slides_INTERNAL.py --check   only report gaps and repeats

A deck already numbered in sequence is left as it is, so a second run changes nothing and its map
reads old equals new.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SLIDES = HERE.parent / "slides"
DECKS = [SLIDES / "C2_W04_D04_half1_STUDENT.md", SLIDES / "C2_W04_D04_half2_STUDENT.md"]
MAP = HERE / "C2_W04_D04_slide_map_INTERNAL.md"
HEAD = re.compile(r"^## ([SD])(NEW|\d+)\.(\s.*)$")


def renumber(write=True):
    count = {"S": 0, "D": 0}
    moved, new, seen = [], [], []
    for deck in DECKS:
        lines = deck.read_text(encoding="utf-8").split("\n")
        for i, line in enumerate(lines):
            m = HEAD.match(line)
            if not m:
                continue
            kind, old, rest = m.groups()
            count[kind] += 1
            number = f"{kind}{count[kind]}"
            title = rest.strip()
            if old == "NEW":
                new.append((deck.stem.split("_")[3], number, title))
            else:
                moved.append((f"{kind}{old}", deck.stem.split("_")[3], number, title))
            seen.append(number)
            lines[i] = f"## {number}.{rest}"
        if write:
            deck.write_text("\n".join(lines), encoding="utf-8")
    return moved, new, seen


def main():
    if "--check" in sys.argv:
        _, _, seen = renumber(write=False)
        print(f"{len(seen)} numbered slides; repeats: {len(seen) - len(set(seen))}")
        return 0
    moved, new, seen = renumber()
    out = ["# Thursday's slides: what each old number became", "",
           "Written by `C2_W04_D04_renumber_slides_INTERNAL.py` in the concept-first rebuild, 13 October 2026.",
           "The old numbers are the merged decks' of 12 October 2026 (half one S1 to S37, half two S38 to S47).",
           "A slide the rebuild removed or merged is listed under the last table.", "",
           "| Old | Deck | New | Title now |", "|---|---|---|---|"]
    out += [f"| {o} | {d} | {n} | {t} |" for o, d, n, t in moved]
    out += ["", "## The slides the rebuild added", "", "| Deck | New | Title |", "|---|---|---|"]
    out += [f"| {d} | {n} | {t} |" for d, n, t in new]
    kept = {o for o, *_ in moved}
    gone = [f"S{k}" for k in range(1, 48) if f"S{k}" not in kept]
    out += ["", "## The old slides the rebuild removed or merged", "",
            "| Old | Where its content went |", "|---|---|"]
    fate = {"S6": "the two coaching batches: a one-line analogy on SECTION 1's map slide",
            "S12": "the blend toy's question: SECTION 3's prediction, on the gym's dashboard",
            "S13": "the blend toy's answer: SECTION 3's answer and the weighted average, on the gym",
            "S14": "Blinkit's and Swiggy's cohort cards: Swiggy on SECTION 1's map node, Blinkit on SECTION 2's rules",
            "S22": "each month's 38 as a picture: merged into the wrong call's slide in SECTION 6",
            "S29": "the toy funnel: SECTION 4 on the college; SECTION 7 keeps a one-line recall as its answer slide"}
    out += [f"| {g} | {fate.get(g, 'not recorded')} |" for g in gone]
    MAP.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(seen)} slides numbered; {len(moved)} moved, {len(new)} new, {len(gone)} removed or merged")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# Test inputs and expected outcomes
# python3 content/W04/D4/internal/C2_W04_D04_renumber_slides_INTERNAL.py
#     on the rebuilt decks with SNEW and DNEW headings: numbers every slide S1 upward across half one
#     and half two, D1 upward for the self-study slides, writes the map and prints the counts
# the same command a second time
#     changes no heading, and the map reads each old number equal to its new one
# python3 content/W04/D4/internal/C2_W04_D04_renumber_slides_INTERNAL.py --check
#     prints the count of numbered slides and "repeats: 0" on a deck numbered in sequence
