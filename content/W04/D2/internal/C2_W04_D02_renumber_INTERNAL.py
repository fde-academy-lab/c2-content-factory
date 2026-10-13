"""Number Tuesday's two decks in teaching order and rewrite every slide reference inside them.

The concept-first rebuild of 13 October 2026 spliced five concept chapters and their opening slides
around the merged pack's case slides. A case slide kept its merged number in its heading (## S13.)
and a new slide read ## S0., so this script walks half1 and then half2, gives every S and D slide
the next number in one sequence across both halves, rewrites each in-deck reference to a merged
number (S4, S21 and the like) to the slide's new number, and writes the map from merged numbers to
new ones, with where each moved beat went, to C2_W04_D02_slide_map_INTERNAL.md. A deck already
numbered maps onto itself, and the map file is then left as it is.

Run from the repository root:
    python3 content/W04/D2/internal/C2_W04_D02_renumber_INTERNAL.py
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
SLIDES = HERE.parent / "slides"
DECKS = ["C2_W04_D02_half1_STUDENT.md", "C2_W04_D02_half2_STUDENT.md"]
MAP = HERE / "C2_W04_D02_slide_map_INTERNAL.md"
HEAD = re.compile(r"^## ([SD])(\d+)\. (.*)$")

# Merged slides whose beat moved into a concept chapter or left the day, and the new slide that now
# carries it, found by the start of its title once the decks are numbered.
MOVED = {
    7: ("One slide carries four parts, in this order", "the four-part anatomy, now chapter 1's skeleton"),
    22: ("A defence fails by overclaiming or retreating", "conceding nothing or everything, now chapter 3's trap"),
    25: ("A defence fails by overclaiming or retreating",
         "retreat and overclaim, now chapter 3's trap and one line in round one's notes"),
    28: ("Answer: b; Amazon reads six-page memos in silence", "Amazon's memo, now chapter 7's answer"),
    35: ("Clarify, map, calculate: 3,000 x 0.45 x 2 = 2,700",
         "the canteen's tea, now chapter 6's hand count, with new invented numbers"),
    36: ("Answer: b, the structure and the check are scored", "the four steps, now chapter 6's strip"),
    54: (None, "the gallery, cut: the spine's first cut"),
}


def main():
    texts = [(SLIDES / d).read_text(encoding="utf-8") for d in DECKS]
    k, mapping, titles = 0, {}, {}
    numbered = []
    for deck, text in zip(DECKS, texts):
        out = []
        for line in text.splitlines():
            m = HEAD.match(line)
            if m:
                k += 1
                letter, old, title = m.group(1), int(m.group(2)), m.group(3)
                if old:
                    if old in mapping:
                        sys.exit(f"FAIL  {deck}: merged number {old} appears twice")
                    mapping[old] = (letter, k, deck)
                titles[k] = (letter, title, deck)
                line = f"## {letter}{k}. {title}"
            out.append(line)
        numbered.append("\n".join(out) + "\n")

    def ref(m):
        old = int(m.group(1))
        if old not in mapping:
            sys.exit(f"FAIL  a reference to S{old} names a merged slide that no longer exists")
        letter, new, _ = mapping[old]
        return f"{letter}{new}"

    changed = any(old != new for old, (_, new, _) in mapping.items())
    for deck, text in zip(DECKS, numbered):
        lines = [line if line.startswith("## ") else re.sub(r"\bS(\d{1,2})\b", ref, line)
                 for line in text.splitlines()] if changed else text.splitlines()
        (SLIDES / deck).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"numbered {deck}")
    if not changed:
        print("the decks were already numbered; the map is unchanged")
        return

    rows = ["# Tuesday's slides, merged pack to concept-first pack", "",
            "Written by C2_W04_D02_renumber_INTERNAL.py on the concept-first rebuild of 13 October 2026. "
            "Each merged slide number on the left is the slide's number in the pack merged before the "
            "rebuild; the right gives its number now, in one sequence across half1 and half2. A file "
            "outside this folder that cites a Tuesday slide by number reads its new number here.", "",
            "| Merged | Now | Deck | Title now, or where the beat went |", "|---|---|---|---|"]
    for old in sorted(set(mapping) | set(MOVED)):
        if old in mapping:
            letter, new, deck = mapping[old]
            rows.append(f"| S{old} | {letter}{new} | {deck.split('_')[3]} | {titles[new][1]} |")
        else:
            start, what = MOVED[old]
            hit = next((f"{l}{n}" for n, (l, t, _) in titles.items() if start and t.startswith(start)), None)
            if start and not hit:
                sys.exit(f"FAIL  the slide carrying S{old}'s beat, '{start}', is not in the decks")
            rows.append(f"| S{old} | {hit or 'none'} | {'' if not hit else 'moved'} | {what} |")
    MAP.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"wrote {MAP.name}: {len(mapping)} kept, {len(MOVED)} moved or cut")


if __name__ == "__main__":
    main()

# Test inputs and expected outcomes
# --------------------------------
# On the decks as assembled (case slides at their merged numbers, new slides at S0):
#     numbers half1 S1 to S54 and half2 S55 to S93 (D-slides keep their letter), rewrites S4, S11,
#     S12, S15, S21, S27, S38 and S42 in the bodies, and writes the map with the seven moved rows.
# Run a second time on the numbered decks:
#     "the decks were already numbered; the map is unchanged", and no file changes.
# A body line citing S22 while S22 is no slide of the assembled decks:
#     FAIL  a reference to S22 names a merged slide that no longer exists; exit 1, nothing written.
