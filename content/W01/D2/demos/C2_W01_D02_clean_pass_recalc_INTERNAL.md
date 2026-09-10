# Recalc manifest: Day 2 clean-pass miniature

Internal. The run sheet ships with the observed column empty. The flips fill it with a healthy pass and then with a pass whose reconciliation fails, so the status column and the verdict are both proved to compute.

```yaml
workbook: C2_W01_D02_clean_pass_STUDENT.xlsx
verdicts:
  - {sheet: RunSheet, cell: E5, expect: "not run yet"}
  - {sheet: RunSheet, cell: C14, expect: "0"}
  - {sheet: RunSheet, cell: C15, contains: "not finished"}
flips:
  - name: a healthy pass, every move as it should be
    set:
      - {sheet: RunSheet, cell: D5, value: "30"}
      - {sheet: RunSheet, cell: D6, value: "28"}
      - {sheet: RunSheet, cell: D7, value: "clean"}
      - {sheet: RunSheet, cell: D8, value: "28"}
      - {sheet: RunSheet, cell: D9, value: "2"}
      - {sheet: RunSheet, cell: D10, value: "2"}
      - {sheet: RunSheet, cell: D11, value: "holds"}
      - {sheet: RunSheet, cell: D12, value: "both"}
    verdicts:
      - {sheet: RunSheet, cell: C14, expect: "8"}
      - {sheet: RunSheet, cell: C15, expect: "ready: the pass is defensible"}
  - name: a row falls through both branches and the reconciliation breaks
    set:
      - {sheet: RunSheet, cell: D5, value: "30"}
      - {sheet: RunSheet, cell: D6, value: "28"}
      - {sheet: RunSheet, cell: D7, value: "clean"}
      - {sheet: RunSheet, cell: D8, value: "27"}
      - {sheet: RunSheet, cell: D9, value: "2"}
      - {sheet: RunSheet, cell: D10, value: "2"}
      - {sheet: RunSheet, cell: D11, value: "broken"}
      - {sheet: RunSheet, cell: D12, value: "both"}
    verdicts:
      - {sheet: RunSheet, cell: E8, expect: "differs"}
      - {sheet: RunSheet, cell: E11, expect: "differs"}
      - {sheet: RunSheet, cell: C15, expect: "hold: 2 moves differ from what they should show"}
```
