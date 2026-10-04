"""Prove that the GD swap rule clears every draw, under both of Monday's allocations.

    python3 content/W03/D5/internal/C2_W03_D05_swap_check_INTERNAL.py

Run it from the repository root. It reads the shipped roster workbook (gd/C2_W03_D05_gd_roster_TRAINER.xlsx):
each card's level and the sub-problems it is kept from on the Prompts sheet, and the card each slot
carries on the Roster sheet. Then it draws the nine groups into the nine slots in every one of the
362,880 possible orders, under Monday's two allocations (content/W03/D1/trainer, the allocation
section: Option A puts three groups each on questions 1, 3 and 5; Option B puts two groups on each
of questions 1, 2, 3 and 5 and the group of three on question 4), and applies the rule the day sheet
gives, clash by clash in slot order:

1. swap the card with the other card of its level, if neither group would then sit a card it is
   kept from;
2. give the group card 08, the spare, if no other group has it yet;
3. swap the group's draw position with the nearest group for which both moves are allowed.

It prints, per allocation, the share of draws with a clash, the share the first two steps leave
stuck, and the share all three leave stuck, and exits 1 if any draw ends with a clash.
"""
import itertools
import pathlib
import sys

from openpyxl import load_workbook

HERE = pathlib.Path(__file__).resolve().parent
BOOK = HERE.parent / "gd" / "C2_W03_D05_gd_roster_TRAINER.xlsx"

wb = load_workbook(BOOK, data_only=True)
prompts, roster = wb["Prompts"], wb["Roster"]
LEVEL, KEPT = {}, {}
for r in range(3, 13):
    card = int(prompts[f"A{r}"].value)
    LEVEL[card] = int(prompts[f"C{r}"].value)
    kept = str(prompts[f"D{r}"].value)
    KEPT[card] = set() if kept == "none" else {int(x) for x in kept.replace("and", " ").split()}
SLOT_CARD = [int(roster[f"J{r}"].value) for r in range(4, 13)]
SPARE = 8
assert SPARE not in SLOT_CARD and len(SLOT_CARD) == 9

ALLOCATIONS = {
    "Option A": [1, 1, 1, 3, 3, 3, 5, 5, 5],
    "Option B": [3, 3, 1, 1, 2, 5, 5, 2, 4],
}


def ok(sub, card):
    return sub not in KEPT[card]


def resolve(order, alloc, third_step):
    """Apply the rule to one draw; return True when every group ends on a card it may sit."""
    cards, groups, spare_used = list(SLOT_CARD), list(order), False
    for s in range(9):
        sub = alloc[groups[s]]
        if ok(sub, cards[s]):
            continue
        fixed = False
        for t in range(9):
            if (t != s and LEVEL[cards[t]] == LEVEL[cards[s]]
                    and ok(sub, cards[t]) and ok(alloc[groups[t]], cards[s])):
                cards[s], cards[t] = cards[t], cards[s]
                fixed = True
                break
        if not fixed and not spare_used and ok(sub, SPARE):
            cards[s], spare_used, fixed = SPARE, True, True
        if not fixed and third_step:
            for t in sorted(range(9), key=lambda t: (abs(t - s), t)):
                if t != s and ok(sub, cards[t]) and ok(alloc[groups[t]], cards[s]):
                    groups[s], groups[t] = groups[t], groups[s]
                    fixed = True
                    break
        if not fixed:
            return False
    return all(ok(alloc[groups[s]], cards[s]) for s in range(9))


stuck_total = 0
for name, alloc in ALLOCATIONS.items():
    draws = clashes = stuck_two = stuck_three = 0
    for order in itertools.permutations(range(9)):
        draws += 1
        if any(not ok(alloc[order[s]], SLOT_CARD[s]) for s in range(9)):
            clashes += 1
            stuck_two += not resolve(order, alloc, third_step=False)
            stuck_three += not resolve(order, alloc, third_step=True)
    stuck_total += stuck_three
    print(f"{name}: {draws:,} draws; {clashes / draws:.1%} put a group on a card it is kept from; "
          f"the first two steps leave {stuck_two / draws:.2%} stuck; all three leave {stuck_three:,}")
print(f"\nRESULT: {'PASS' if stuck_total == 0 else 'FAIL'} ({stuck_total} draws left with a clash)")
sys.exit(0 if stuck_total == 0 else 1)

# Test inputs and expected outcomes
# ---------------------------------
# Run as shipped, on 4 October 2026:
#   Option A: 362,880 draws; 88.1% put a group on a card it is kept from; the first two steps leave
#     27.38% stuck; all three leave 0
#   Option B: 362,880 draws; 72.9% put a group on a card it is kept from; the first two steps leave
#     7.28% stuck; all three leave 0
#   RESULT: PASS (0 draws left with a clash)
# On a copy of the workbook with "3 and 4" typed for card 01 on the Prompts sheet (D3):
#   Option A: 94.0% clash and 31.19% stuck after two steps; Option B: 84.4% and 9.58%; all three
#   steps still leave 0, and RESULT: PASS.
# With third_step=False in both calls: all three leave the two-step shares above, and RESULT: FAIL.
