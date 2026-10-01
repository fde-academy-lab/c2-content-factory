# How does Mock R1's roster prove it computes, and that its verdicts move?

Read by `scripts/xlsx_recalc.py`. It recalculates the roster through LibreOffice, asserts the day's
verdicts as shipped, then changes one input at a time and asserts that the verdicts move. The
workbook is written by `content/W03/D4/internal/C2_W03_D04_build_workbooks_INTERNAL.py`. Five flips
put every group on one sub-problem in turn and assert that no seat is asked two questions from one
family and no two group-mates share a question; two more edit a set and assert that both checks
catch it.

```yaml
workbook: C2_W03_D04_roster_TRAINER.xlsx
verdicts:
  - {sheet: Settings, cell: B16, expect: "fits: 36 slots for 35 learners"}
  - {sheet: Settings, cell: B17, expect: "block 2, minute 145"}
  - {sheet: Settings, cell: B19, expect: "0"}
  - {sheet: Settings, cell: B21, expect: "0"}
  - {sheet: Settings, cell: B22, expect: "0"}
  - {sheet: Settings, cell: C29, expect: "35"}
  - {sheet: Settings, cell: E28, expect: "block 2, minute 120"}
  - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T04-L2, T07-L3"}
  - {sheet: Grid, cell: G13, expect: "spare"}
  - {sheet: Seat list, cell: B2, expect: "1"}
  - {sheet: Seat list, cell: F2, expect: "Programme Head"}
  - {sheet: Seat list, cell: G10, expect: "online, from your own laptop in the quiet room"}
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
      - {sheet: Settings, cell: C29, expect: "34"}
      - {sheet: Seat list, cell: B2, expect: "not placed: see the trainer"}
  - name: the changeover shrinks to 2 minutes
    set: [{sheet: Settings, cell: B4, value: 2}]
    verdicts:
      - {sheet: Settings, cell: B16, expect: "fits: 42 slots for 35 learners"}
  - name: G1 takes the no-show question, so its set A seat is asked set E's L2
    set: [{sheet: Groups, cell: B2, value: "4 no-shows"}]
    verdicts:
      - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T08-L2, T07-L3"}
  - name: G6 takes the offer question, so its set H seat is asked set D's L3
    set: [{sheet: Groups, cell: B7, value: "5 campaign"}]
    verdicts:
      - {sheet: Grid, cell: G9, expect: "G6-S3, set H, P3: T08-L1, T01-L2, T10-L3"}
  - name: every group takes the revenue question
    set: [{sheet: Groups, cell: B2, value: "1 revenue"}, {sheet: Groups, cell: B3, value: "1 revenue"}, {sheet: Groups, cell: B4, value: "1 revenue"}, {sheet: Groups, cell: B5, value: "1 revenue"}, {sheet: Groups, cell: B6, value: "1 revenue"}, {sheet: Groups, cell: B7, value: "1 revenue"}, {sheet: Groups, cell: B8, value: "1 revenue"}, {sheet: Groups, cell: B9, value: "1 revenue"}, {sheet: Groups, cell: B10, value: "1 revenue"}]
    verdicts:
      - {sheet: Settings, cell: B21, expect: "0"}
      - {sheet: Settings, cell: B22, expect: "0"}
      - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T10-L1, T04-L2, T07-L3"}
  - name: every group takes the bookings question
    set: [{sheet: Groups, cell: B2, value: "2 bookings"}, {sheet: Groups, cell: B3, value: "2 bookings"}, {sheet: Groups, cell: B4, value: "2 bookings"}, {sheet: Groups, cell: B5, value: "2 bookings"}, {sheet: Groups, cell: B6, value: "2 bookings"}, {sheet: Groups, cell: B7, value: "2 bookings"}, {sheet: Groups, cell: B8, value: "2 bookings"}, {sheet: Groups, cell: B9, value: "2 bookings"}, {sheet: Groups, cell: B10, value: "2 bookings"}]
    verdicts:
      - {sheet: Settings, cell: B21, expect: "0"}
      - {sheet: Settings, cell: B22, expect: "0"}
  - name: every group takes the billing question
    set: [{sheet: Groups, cell: B2, value: "3 billing"}, {sheet: Groups, cell: B3, value: "3 billing"}, {sheet: Groups, cell: B4, value: "3 billing"}, {sheet: Groups, cell: B5, value: "3 billing"}, {sheet: Groups, cell: B6, value: "3 billing"}, {sheet: Groups, cell: B7, value: "3 billing"}, {sheet: Groups, cell: B8, value: "3 billing"}, {sheet: Groups, cell: B9, value: "3 billing"}, {sheet: Groups, cell: B10, value: "3 billing"}]
    verdicts:
      - {sheet: Settings, cell: B21, expect: "0"}
      - {sheet: Settings, cell: B22, expect: "0"}
      - {sheet: Grid, cell: E2, expect: "G1-S1, set A, P1: T01-L1, T04-L2, T05-L3"}
  - name: every group takes the no-show question
    set: [{sheet: Groups, cell: B2, value: "4 no-shows"}, {sheet: Groups, cell: B3, value: "4 no-shows"}, {sheet: Groups, cell: B4, value: "4 no-shows"}, {sheet: Groups, cell: B5, value: "4 no-shows"}, {sheet: Groups, cell: B6, value: "4 no-shows"}, {sheet: Groups, cell: B7, value: "4 no-shows"}, {sheet: Groups, cell: B8, value: "4 no-shows"}, {sheet: Groups, cell: B9, value: "4 no-shows"}, {sheet: Groups, cell: B10, value: "4 no-shows"}]
    verdicts:
      - {sheet: Settings, cell: B21, expect: "0"}
      - {sheet: Settings, cell: B22, expect: "0"}
  - name: every group takes the offer question
    set: [{sheet: Groups, cell: B2, value: "5 campaign"}, {sheet: Groups, cell: B3, value: "5 campaign"}, {sheet: Groups, cell: B4, value: "5 campaign"}, {sheet: Groups, cell: B5, value: "5 campaign"}, {sheet: Groups, cell: B6, value: "5 campaign"}, {sheet: Groups, cell: B7, value: "5 campaign"}, {sheet: Groups, cell: B8, value: "5 campaign"}, {sheet: Groups, cell: B9, value: "5 campaign"}, {sheet: Groups, cell: B10, value: "5 campaign"}]
    verdicts:
      - {sheet: Settings, cell: B21, expect: "0"}
      - {sheet: Settings, cell: B22, expect: "0"}
  - name: set A is edited to hold two questions from one family
    set: [{sheet: Sets, cell: B2, value: "T07-L1"}]
    verdicts:
      - {sheet: Settings, cell: B21, expect: "5"}
  - name: set B is edited to share its L1 with set A
    set: [{sheet: Sets, cell: B3, value: "T01-L1"}]
    verdicts:
      - {sheet: Settings, cell: B22, expect: "8"}
```
