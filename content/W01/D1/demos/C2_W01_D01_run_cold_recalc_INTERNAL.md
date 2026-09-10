# Recalc manifest: Day 1 run-cold miniature

Internal. The run sheet ships with the observed column empty, so its verdict starts at not finished. The flips fill the column with a healthy run, then with one move that differs, so the status column and the verdict are both proved to compute rather than to hold typed text.

```yaml
workbook: C2_W01_D01_run_cold_STUDENT.xlsx
verdicts:
  - {sheet: RunSheet, cell: E5, expect: "not run yet"}
  - {sheet: RunSheet, cell: C13, expect: "0"}
  - {sheet: RunSheet, cell: C14, contains: "not finished"}
flips:
  - name: a healthy cold run, every move as it should be
    set:
      - {sheet: RunSheet, cell: D5, value: "empty"}
      - {sheet: RunSheet, cell: D6, value: "30"}
      - {sheet: RunSheet, cell: D7, value: "13"}
      - {sheet: RunSheet, cell: D8, value: "25720"}
      - {sheet: RunSheet, cell: D9, value: "clean"}
      - {sheet: RunSheet, cell: D10, value: "in order"}
      - {sheet: RunSheet, cell: D11, value: "empty"}
    verdicts:
      - {sheet: RunSheet, cell: E5, expect: "pass"}
      - {sheet: RunSheet, cell: C13, expect: "7"}
      - {sheet: RunSheet, cell: C14, expect: "ready: the notebook runs cold"}
  - name: the totalling cell prints the broken number
    set:
      - {sheet: RunSheet, cell: D5, value: "empty"}
      - {sheet: RunSheet, cell: D6, value: "30"}
      - {sheet: RunSheet, cell: D7, value: "13"}
      - {sheet: RunSheet, cell: D8, value: "1460"}
      - {sheet: RunSheet, cell: D9, value: "clean"}
      - {sheet: RunSheet, cell: D10, value: "in order"}
      - {sheet: RunSheet, cell: D11, value: "empty"}
    verdicts:
      - {sheet: RunSheet, cell: E8, expect: "differs"}
      - {sheet: RunSheet, cell: C14, expect: "hold: 1 moves differ from what they should show"}
```
