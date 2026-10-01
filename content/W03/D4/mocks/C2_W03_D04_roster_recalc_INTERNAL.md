# How does Mock R1's roster prove it computes, and that its verdicts move?

Read by `scripts/xlsx_recalc.py`. It recalculates the roster through LibreOffice, asserts the day's
verdicts as shipped, then changes one input at a time and asserts that the verdicts move. The
workbook is written by `content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py`.

```yaml
workbook: C2_W03_D04_roster_TRAINER.xlsx
verdicts:
  - {sheet: Settings, cell: B16, expect: "fits: 36 slots for 35 learners"}
  - {sheet: Settings, cell: B17, expect: "block 2, minute 145"}
  - {sheet: Settings, cell: B19, expect: "0"}
  - {sheet: Settings, cell: C27, expect: "35"}
  - {sheet: Settings, cell: E26, expect: "block 2, minute 120"}
  - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T04-L2, T07-L3"}
  - {sheet: Grid, cell: G13, expect: "spare"}
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
  - name: G1 takes the no-show question, so its set A seat is asked the reserve
    set: [{sheet: Groups, cell: B2, value: "4 no-shows"}]
    verdicts:
      - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T02-L2, T07-L3"}
  - name: G6 takes the offer question, so its set H seat is asked the reserve
    set: [{sheet: Groups, cell: B7, value: "5 campaign"}]
    verdicts:
      - {sheet: Grid, cell: G9, expect: "G6-S3, set H, P3: T08-L1, T01-L2, T05-L3"}
```
