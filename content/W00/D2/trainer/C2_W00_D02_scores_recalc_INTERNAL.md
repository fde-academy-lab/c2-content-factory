# Recalculation manifest: the Week 0 score workbook

INTERNAL. This drives `scripts/xlsx_recalc.py`, which makes LibreOffice recompute the workbook and
then changes its inputs to prove the results move.

The workbook holds one decision, the share of the Python ticks below which a learner joins
Wednesday's taught track, in Settings B9. Everything else is arithmetic over typed ticks. The
verdicts check the grey example row as shipped, and the flips check that the track follows the
share, that a learner who missed the paper gets no track from an empty row, and that the room
counts pick up a learner once their ticks are typed in.

```yaml
workbook: C2_W00_D02_scores_TRAINER.xlsx
verdicts:
  - {sheet: Scores, cell: AQ5, expect: "6"}
  - {sheet: Scores, cell: AU5, expect: "taught"}
  - {sheet: Scores, cell: AV5, contains: "Python 6 of 13; SQL 3 of 7"}
  - {sheet: Settings, cell: B10, expect: "6.5"}
  - {sheet: Settings, cell: B11, contains: "6 or fewer of the 13 Python ticks"}
  - {sheet: Room, cell: B4, expect: "0"}
flips:
  - name: the taught line drops to 40 percent of the Python ticks
    set: [{sheet: Settings, cell: B9, value: 0.4}]
    verdicts:
      - {sheet: Scores, cell: AU5, expect: "practice"}
      - {sheet: Settings, cell: B11, contains: "5 or fewer"}
  - name: the example learner missed the paper
    set: [{sheet: Scores, cell: B5, value: "no"}]
    verdicts:
      - {sheet: Scores, cell: AU5, expect: "no paper yet"}
  - name: one learner is marked in full on Python
    set:
      - {sheet: Scores, cell: B6, value: "yes"}
      - {sheet: Scores, cell: G6, value: 1}
      - {sheet: Scores, cell: H6, value: 1}
      - {sheet: Scores, cell: I6, value: 1}
      - {sheet: Scores, cell: J6, value: 1}
      - {sheet: Scores, cell: K6, value: 1}
      - {sheet: Scores, cell: L6, value: 1}
      - {sheet: Scores, cell: M6, value: 1}
      - {sheet: Scores, cell: N6, value: 1}
      - {sheet: Scores, cell: O6, value: 1}
      - {sheet: Scores, cell: P6, value: 1}
      - {sheet: Scores, cell: Q6, value: 1}
      - {sheet: Scores, cell: R6, value: 1}
      - {sheet: Scores, cell: S6, value: 1}
    verdicts:
      - {sheet: Scores, cell: AQ6, expect: "13"}
      - {sheet: Scores, cell: AU6, expect: "practice"}
      - {sheet: Room, cell: B4, expect: "1"}
      - {sheet: Room, cell: B7, expect: "1"}
      - {sheet: Room, cell: D16, expect: "1"}
  - name: one learner earns six Python ticks
    set:
      - {sheet: Scores, cell: B6, value: "yes"}
      - {sheet: Scores, cell: G6, value: 1}
      - {sheet: Scores, cell: H6, value: 1}
      - {sheet: Scores, cell: I6, value: 1}
      - {sheet: Scores, cell: J6, value: 1}
      - {sheet: Scores, cell: K6, value: 1}
      - {sheet: Scores, cell: L6, value: 1}
      - {sheet: Scores, cell: M6, value: 0}
    verdicts:
      - {sheet: Scores, cell: AU6, expect: "taught"}
      - {sheet: Room, cell: B6, expect: "1"}
```
