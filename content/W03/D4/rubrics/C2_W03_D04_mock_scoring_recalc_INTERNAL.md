# Recalc manifest for the Mock R1 scoring sheet

Read by `scripts/xlsx_recalc.py`. The sheet ships blank, so the checks as shipped read its empty state,
and the flips enter marks and assert that the totals, the status and the calibration check move.

```yaml
workbook: C2_W03_D04_mock_scoring_sheet_TRAINER.xlsx
verdicts:
  - {sheet: Criteria, cell: D11, expect: "30"}
  - {sheet: Criteria, cell: D12, expect: "yes"}
  - {sheet: Scores, cell: M2, expect: "not scored"}
  - {sheet: Assessors, cell: B6, expect: "0 of 35 scored"}
  - {sheet: Assessors, cell: B10, expect: "too few scores to compare"}
  - {sheet: Example, cell: L2, expect: "22"}
flips:
  - name: one learner is scored in full
    set:
      - {sheet: Scores, cell: D2, value: 6}
      - {sheet: Scores, cell: E2, value: 3}
      - {sheet: Scores, cell: F2, value: 2}
      - {sheet: Scores, cell: G2, value: 5}
      - {sheet: Scores, cell: H2, value: 4}
      - {sheet: Scores, cell: I2, value: 2}
    verdicts:
      - {sheet: Scores, cell: L2, expect: "22"}
      - {sheet: Scores, cell: M2, expect: "scored"}
      - {sheet: Assessors, cell: B6, expect: "1 of 35 scored"}
      - {sheet: Groups, cell: D2, expect: "22"}
  - name: a mark is entered above its maximum
    set: [{sheet: Scores, cell: D2, value: 9}]
    verdicts:
      - {sheet: Scores, cell: M2, expect: "check: a mark is above its maximum"}
      - {sheet: Assessors, cell: B7, expect: "1"}
  - name: two assessors score the same half three marks apart
    set:
      - {sheet: Scores, cell: D2, value: 8}
      - {sheet: Scores, cell: E2, value: 4}
      - {sheet: Scores, cell: F2, value: 3}
      - {sheet: Scores, cell: G2, value: 5}
      - {sheet: Scores, cell: H2, value: 5}
      - {sheet: Scores, cell: I2, value: 2}
      - {sheet: Scores, cell: D6, value: 5}
      - {sheet: Scores, cell: E6, value: 3}
      - {sheet: Scores, cell: F6, value: 3}
      - {sheet: Scores, cell: G6, value: 5}
      - {sheet: Scores, cell: H6, value: 5}
      - {sheet: Scores, cell: I6, value: 2}
    verdicts:
      - {sheet: Assessors, cell: B8, expect: "4"}
      - {sheet: Assessors, cell: B10, expect: "discuss at the close: a gap above two marks"}
```
