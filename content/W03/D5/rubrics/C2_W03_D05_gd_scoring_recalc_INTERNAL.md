# Recalc manifest for the Build 1 GD scoring sheet

`scripts/xlsx_recalc.py` rebuilds the sheet through LibreOffice, asserts it as shipped (36 seats,
nobody scored yet), then flips three things: one learner scored in full, one seat marked absent, and
one score typed above its criterion's maximum.

```yaml
workbook: C2_W03_D05_gd_scoring_sheet_TRAINER.xlsx
verdicts:
  - {sheet: Rubric, cell: B7, expect: "30"}
  - {sheet: Summary, cell: B6, expect: "the rubric adds to 30"}
  - {sheet: Summary, cell: B7, expect: "36 learners still to score"}
  - {sheet: Scores, cell: L3, expect: "incomplete"}
flips:
  - name: the first learner is scored on all four criteria
    set:
      - {sheet: Scores, cell: H3, value: 7}
      - {sheet: Scores, cell: I3, value: 8}
      - {sheet: Scores, cell: J3, value: 5}
      - {sheet: Scores, cell: K3, value: 4}
    verdicts:
      - {sheet: Scores, cell: L3, expect: "24"}
      - {sheet: Summary, cell: B7, expect: "35 learners still to score"}
      - {sheet: Summary, cell: B12, expect: "24"}
  - name: the ninth group's fourth seat is empty
    set: [{sheet: Scores, cell: D38, value: "N"}]
    verdicts:
      - {sheet: Scores, cell: L38, expect: "absent"}
      - {sheet: Summary, cell: B7, expect: "35 learners still to score"}
  - name: a score of 7 is typed for Lands a conclusion, whose maximum is 6
    set: [{sheet: Scores, cell: K3, value: 7}]
    verdicts:
      - {sheet: Scores, cell: M3, expect: "above a maximum or below zero"}
      - {sheet: Summary, cell: B7, expect: "1 row(s) hold a score outside the rubric"}
```
