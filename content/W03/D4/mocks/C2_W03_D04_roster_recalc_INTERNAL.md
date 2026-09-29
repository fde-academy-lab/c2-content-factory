# Recalc manifest for the Mock R1 roster

Read by `scripts/xlsx_recalc.py`. It recalculates the roster through LibreOffice, asserts the day's
verdict as shipped, then changes one input at a time and asserts that the verdict moves.

```yaml
workbook: C2_W03_D04_roster_TRAINER.xlsx
verdicts:
  - {sheet: Settings, cell: B16, expect: "fits: 36 slots for 35 learners"}
  - {sheet: Settings, cell: B17, expect: "block 2, minute 145"}
  - {sheet: Settings, cell: B19, expect: "0"}
  - {sheet: Settings, cell: C27, expect: "35"}
  - {sheet: Settings, cell: E26, expect: "block 2, minute 120"}
flips:
  - name: the mock slot grows to 25 minutes
    set: [{sheet: Settings, cell: B3, value: 25}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "does not fit: 5 learners without a slot"}
      - {sheet: Settings, cell: B17, expect: "after the day"}
  - name: one learner is known to be absent before the day
    set: [{sheet: Seats, cell: G2, value: "no"}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "fits: 36 slots for 34 learners"}
      - {sheet: Settings, cell: C27, expect: "34"}
  - name: the changeover shrinks to 2 minutes
    set: [{sheet: Settings, cell: B4, value: 2}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "fits: 42 slots for 35 learners"}
```
