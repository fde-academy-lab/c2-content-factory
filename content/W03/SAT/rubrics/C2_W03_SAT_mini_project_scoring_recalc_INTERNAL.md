# Recalc manifest: the Build 1 mini project scoring sheet

`scripts/xlsx_recalc.py` recalculates the sheet through LibreOffice, asserts the empty template,
then flips entries and asserts that the totals and checks move. Written by
`internal/C2_W03_SAT_build_mini_project_scoring_INTERNAL.py`; rebuild both together.

```yaml
workbook: C2_W03_SAT_mini_project_scoring_TRAINER.xlsx
verdicts:
  - {sheet: Rubric, cell: B8, expect: "40"}
  - {sheet: Rubric, cell: B9, expect: "34"}
  - {sheet: Summary, cell: B9, expect: "36 learners still to score"}
  - {sheet: Learners, cell: F3, expect: "incomplete"}
flips:
  - name: G1 scored as a group, one member scored alone
    set: [{sheet: Groups, cell: E3, value: 6}, {sheet: Groups, cell: F3, value: 8}, {sheet: Groups, cell: G3, value: 7}, {sheet: Groups, cell: H3, value: 5}, {sheet: Learners, cell: D3, value: 4}]
    verdicts:
      - {sheet: Groups, cell: I3, expect: "26"}
      - {sheet: Learners, cell: F3, expect: "30"}
      - {sheet: Learners, cell: F4, expect: "incomplete"}
  - name: a group criterion above its maximum
    set: [{sheet: Groups, cell: F3, value: 11}]
    verdicts:
      - {sheet: Groups, cell: J3, expect: "above a maximum or below zero"}
      - {sheet: Summary, cell: B9, expect: "1 score(s) outside the rubric"}
  - name: the group of three marks its fourth seat unused
    set: [{sheet: Learners, cell: C38, value: "N"}]
    verdicts:
      - {sheet: Learners, cell: F38, expect: "absent"}
      - {sheet: Summary, cell: B3, expect: "35"}
  - name: every group and every learner scored
    set: [{sheet: Groups, cell: E3, value: 6}, {sheet: Groups, cell: F3, value: 8}, {sheet: Groups, cell: G3, value: 7}, {sheet: Groups, cell: H3, value: 5}, {sheet: Groups, cell: E4, value: 6}, {sheet: Groups, cell: F4, value: 8}, {sheet: Groups, cell: G4, value: 7}, {sheet: Groups, cell: H4, value: 5}, {sheet: Groups, cell: E5, value: 6}, {sheet: Groups, cell: F5, value: 8}, {sheet: Groups, cell: G5, value: 7}, {sheet: Groups, cell: H5, value: 5}, {sheet: Groups, cell: E6, value: 6}, {sheet: Groups, cell: F6, value: 8}, {sheet: Groups, cell: G6, value: 7}, {sheet: Groups, cell: H6, value: 5}, {sheet: Groups, cell: E7, value: 6}, {sheet: Groups, cell: F7, value: 8}, {sheet: Groups, cell: G7, value: 7}, {sheet: Groups, cell: H7, value: 5}, {sheet: Groups, cell: E8, value: 6}, {sheet: Groups, cell: F8, value: 8}, {sheet: Groups, cell: G8, value: 7}, {sheet: Groups, cell: H8, value: 5}, {sheet: Groups, cell: E9, value: 6}, {sheet: Groups, cell: F9, value: 8}, {sheet: Groups, cell: G9, value: 7}, {sheet: Groups, cell: H9, value: 5}, {sheet: Groups, cell: E10, value: 6}, {sheet: Groups, cell: F10, value: 8}, {sheet: Groups, cell: G10, value: 7}, {sheet: Groups, cell: H10, value: 5}, {sheet: Groups, cell: E11, value: 6}, {sheet: Groups, cell: F11, value: 8}, {sheet: Groups, cell: G11, value: 7}, {sheet: Groups, cell: H11, value: 5}, {sheet: Learners, cell: D3, value: 4}, {sheet: Learners, cell: D4, value: 4}, {sheet: Learners, cell: D5, value: 4}, {sheet: Learners, cell: D6, value: 4}, {sheet: Learners, cell: D7, value: 4}, {sheet: Learners, cell: D8, value: 4}, {sheet: Learners, cell: D9, value: 4}, {sheet: Learners, cell: D10, value: 4}, {sheet: Learners, cell: D11, value: 4}, {sheet: Learners, cell: D12, value: 4}, {sheet: Learners, cell: D13, value: 4}, {sheet: Learners, cell: D14, value: 4}, {sheet: Learners, cell: D15, value: 4}, {sheet: Learners, cell: D16, value: 4}, {sheet: Learners, cell: D17, value: 4}, {sheet: Learners, cell: D18, value: 4}, {sheet: Learners, cell: D19, value: 4}, {sheet: Learners, cell: D20, value: 4}, {sheet: Learners, cell: D21, value: 4}, {sheet: Learners, cell: D22, value: 4}, {sheet: Learners, cell: D23, value: 4}, {sheet: Learners, cell: D24, value: 4}, {sheet: Learners, cell: D25, value: 4}, {sheet: Learners, cell: D26, value: 4}, {sheet: Learners, cell: D27, value: 4}, {sheet: Learners, cell: D28, value: 4}, {sheet: Learners, cell: D29, value: 4}, {sheet: Learners, cell: D30, value: 4}, {sheet: Learners, cell: D31, value: 4}, {sheet: Learners, cell: D32, value: 4}, {sheet: Learners, cell: D33, value: 4}, {sheet: Learners, cell: D34, value: 4}, {sheet: Learners, cell: D35, value: 4}, {sheet: Learners, cell: D36, value: 4}, {sheet: Learners, cell: D37, value: 4}, {sheet: Learners, cell: D38, value: 4}]
    verdicts:
      - {sheet: Summary, cell: B9, expect: "every learner in use is scored"}
      - {sheet: Learners, cell: F38, expect: "30"}
```
