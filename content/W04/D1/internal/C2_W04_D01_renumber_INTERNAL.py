"""Renumber Monday's half-deck slides in teaching order, and print where each slide of the old decks went.

    python3 content/W04/D1/internal/C2_W04_D01_renumber_INTERNAL.py            renumber, then print the map
    python3 content/W04/D1/internal/C2_W04_D01_renumber_INTERNAL.py --check    exit 1 if a number is out of order

Slide numbers run on from half one into half two, so a trainer can cite a slide without naming its
file; the fallback deck keeps its own S1 to S10. Every `## S<n>.` and `## D<n>.` heading is numbered
in the order it appears, half one first. The map reads the decks as they stood on origin/main before
the concept chapters were added (git show), matches each old slide to a new one by its title, and
prints old number, new number and title, so every reference in the day's other files can be moved
by the same table; an old slide whose title no longer appears is printed as moved or cut.
"""
import pathlib
import re
import subprocess
import sys

DAY = pathlib.Path(__file__).resolve().parent.parent
REPO = DAY.parents[2]
DECKS = ["C2_W04_D01_half1_STUDENT.md", "C2_W04_D01_half2_STUDENT.md"]
HEAD = re.compile(r"^## ([SD])(\d+)\. (.+)$", re.M)
# Old slides whose title changed on the way, and the new title they became.
RETITLED = {"Which number can rise with no rider at all?": "An hour needs only an open app, as a token did",
            "Answer: hours, since the app counts it open": "An hour needs only an open app, as a token did",
            "Ticket: Uber Hyderabad's peak-hour guarantee": "Ticket: Uber Hyderabad's peak-hour guarantee"}
# Old slides whose beat moved into a concept chapter, or was cut, and where the beat now sits.
MOVED = {"A canteen pays per token: tokens double": "moved to chapter 1, S9 and S10",
         "Wells Fargo paid for accounts nobody used": "moved to chapter 1, S13",
         "Swiggy writes each denominator down": "moved to chapter 4, S36",
         "Delhi Metro's numbers differ by unit and by day": "moved to chapter 4, S37",
         "Acceptance moved first, bookings followed": "moved to chapter 3, S28",
         "VA let the measured set the clock's start": "moved to chapter 5, S42",
         "This afternoon: three rounds become one answer": "cut; the topics slide, S3, carries the order",
         "Maxxsaver: fewer orders per user, bigger baskets": "moved to chapter 2, S20"}


def renumber():
    n, changed = 0, 0
    for name in DECKS:
        path = DAY / "slides" / name
        text = path.read_text(encoding="utf-8")

        def step(m):
            nonlocal n, changed
            n += 1
            changed += int(m.group(2)) != n
            return f"## {m.group(1)}{n}. {m.group(3)}"

        path.write_text(HEAD.sub(step, text), encoding="utf-8")
    return n, changed


def titles(text):
    return [(int(m.group(2)), m.group(3).strip()) for m in HEAD.finditer(text)]


def old_map():
    new = {}
    for name in DECKS:
        for num, title in titles((DAY / "slides" / name).read_text(encoding="utf-8")):
            new.setdefault(title, num)
    rows = []
    for name in DECKS:
        old = subprocess.run(["git", "show", f"origin/main:content/W04/D1/slides/{name}"], cwd=REPO,
                             capture_output=True, text=True, check=True).stdout
        for num, title in titles(old):
            target = new.get(RETITLED.get(title, title))
            rows.append((name.split("_")[3], num, target, title))
    return rows


if __name__ == "__main__":
    if "--check" in sys.argv:
        seen = [num for name in DECKS for num, _ in titles((DAY / "slides" / name).read_text(encoding="utf-8"))]
        ok = seen == list(range(1, len(seen) + 1))
        print(f"{len(seen)} slides, numbered 1 to {len(seen)} in order: {ok}")
        sys.exit(0 if ok else 1)
    total, changed = renumber()
    print(f"{total} slides across the two halves; {changed} headings renumbered")
    print("| Deck | Old | New | Title |")
    print("|---|---|---|---|")
    for deck, old, new, title in old_map():
        print(f"| {deck} | S{old} | {'S' + str(new) if new else MOVED.get(title, 'moved or cut')} | {title} |")

# Test inputs and expected outcomes
# python3 content/W04/D1/internal/C2_W04_D01_renumber_INTERNAL.py
#     prints "98 slides across the two halves; 0 headings renumbered" once the decks are in order,
#     then one table row per slide of the old decks, S1 to S50
# python3 content/W04/D1/internal/C2_W04_D01_renumber_INTERNAL.py --check
#     prints "98 slides, numbered 1 to 98 in order: True" and exits 0
# the same --check after a slide is inserted by hand with a duplicate number
#     prints "... in order: False" and exits 1
