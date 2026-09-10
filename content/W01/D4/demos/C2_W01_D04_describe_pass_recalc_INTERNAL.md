# Recalc manifest: Day 4 describe-pass miniature

Internal. The run sheet ships with the observed column empty. The flips fill it with a healthy pass and then with a pass where somebody reported the mean.

```yaml
workbook: C2_W01_D04_describe_pass_STUDENT.xlsx
verdicts:
  - {sheet: RunSheet, cell: E5, expect: "not run yet"}
  - {sheet: RunSheet, cell: C13, expect: "0"}
  - {sheet: RunSheet, cell: C14, contains: "not finished"}
flips:
  - name: a healthy describe pass
    set:
      - {sheet: RunSheet, cell: D5, value: "44"}
      - {sheet: RunSheet, cell: D6, value: "12753"}
      - {sheet: RunSheet, cell: D7, value: "1910"}
      - {sheet: RunSheet, cell: D8, value: "1"}
      - {sheet: RunSheet, cell: D9, value: "one"}
      - {sheet: RunSheet, cell: D10, value: "kr4232"}
      - {sheet: RunSheet, cell: D11, value: "median"}
    verdicts:
      - {sheet: RunSheet, cell: C13, expect: "7"}
      - {sheet: RunSheet, cell: C14, expect: "ready: the number can leave your desk"}
  - name: somebody reported the mean and never named what owns it
    set:
      - {sheet: RunSheet, cell: D5, value: "44"}
      - {sheet: RunSheet, cell: D6, value: "12753"}
      - {sheet: RunSheet, cell: D7, value: "1910"}
      - {sheet: RunSheet, cell: D8, value: "1"}
      - {sheet: RunSheet, cell: D9, value: "one"}
      - {sheet: RunSheet, cell: D10, value: "not checked"}
      - {sheet: RunSheet, cell: D11, value: "mean"}
    verdicts:
      - {sheet: RunSheet, cell: E10, expect: "differs"}
      - {sheet: RunSheet, cell: E11, expect: "differs"}
      - {sheet: RunSheet, cell: C14, expect: "hold: 2 moves differ from what they should show"}
```
