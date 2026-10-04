# Does the Build 1 GD roster compute, and does each verdict move when the draw, the groups or the rounds change?

`scripts/xlsx_recalc.py` reads this file, rebuilds the roster through LibreOffice, asserts the
verdicts as shipped, then flips five decisions and asserts that the verdicts move: the group count
rising to the tracker's fifteen, a sub-problem 5 group drawn to the slot carrying card 05, a billing
group drawn to the slot carrying card 10, a draw position mistyped as 10, and rounds running long.
Written by `internal/C2_W03_D05_build_gd_roster_INTERNAL.py`; rebuild both together.

```yaml
workbook: C2_W03_D05_gd_roster_TRAINER.xlsx
verdicts:
  - {sheet: Check, cell: B3, expect: "270"}
  - {sheet: Check, cell: B8, expect: "standard roster: nine rounds, seven on Friday and two on Saturday morning"}
  - {sheet: Check, cell: B10, expect: "no group meets its own sub-problem"}
  - {sheet: Check, cell: B12, expect: "every round ends inside its block"}
  - {sheet: Check, cell: B13, expect: "every group sits exactly one GD"}
  - {sheet: Check, cell: B15, expect: "every slot has a group drawn"}
  - {sheet: Check, cell: B17, expect: "every draw position is between 1 and 9"}
  - {sheet: Roster, cell: H10, expect: "165"}
  - {sheet: Roster, cell: M8, expect: "3 and 5"}
  - {sheet: Roster, cell: M12, expect: "3"}
  - {sheet: "Friday block two", cell: B16, expect: "block two fits with 33 minutes of slack"}
flips:
  - name: the Programme Head runs the tracker's fifteen groups
    set: [{sheet: Inputs, cell: B6, value: 15}]
    verdicts:
      - {sheet: Check, cell: B3, expect: "450"}
      - {sheet: Check, cell: B8, contains: "both streams run up to 3 Saturday rounds"}
      - {sheet: "Friday block two", cell: B16, expect: "block two fits with 15 minutes of slack"}
  - name: a sub-problem 5 group is drawn to the slot carrying card 05
    set: [{sheet: Inputs, cell: B17, value: 5}]
    verdicts:
      - {sheet: Roster, cell: N8, contains: "swap"}
      - {sheet: Check, cell: B10, expect: "1 clash: swap within the level, use card 08, or swap two draw positions"}
  - name: a billing group is drawn to the slot carrying card 10
    set: [{sheet: Inputs, cell: C13, value: 9}, {sheet: Inputs, cell: C21, value: 1}]
    verdicts:
      - {sheet: Roster, cell: N12, contains: "swap"}
      - {sheet: Check, cell: B10, expect: "1 clash: swap within the level, use card 08, or swap two draw positions"}
  - name: G9's draw position is mistyped as 10
    set: [{sheet: Inputs, cell: C21, value: 10}]
    verdicts:
      - {sheet: Roster, cell: K12, expect: "no group drawn"}
      - {sheet: Check, cell: B15, expect: "slots with no group drawn: 1; check the draw positions on Inputs"}
      - {sheet: Check, cell: B17, expect: "draw positions outside 1 to 9: 1; retype them on Inputs"}
  - name: rounds run 35 minutes
    set: [{sheet: Inputs, cell: B3, value: 35}]
    verdicts:
      - {sheet: Roster, cell: H10, expect: "190"}
      - {sheet: Check, cell: B12, expect: "1 round runs past the block end"}
```
