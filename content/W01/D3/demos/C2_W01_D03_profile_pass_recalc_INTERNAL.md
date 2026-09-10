# Recalc manifest: Day 3 profile-pass miniature

Internal. The run sheet ships with the observed column empty. The flips fill it with a healthy profile and then with one where the dedupe and the reconciliation both disagree.

```yaml
workbook: C2_W01_D03_profile_pass_STUDENT.xlsx
verdicts:
  - {sheet: RunSheet, cell: E5, expect: "not run yet"}
  - {sheet: RunSheet, cell: C14, expect: "0"}
  - {sheet: RunSheet, cell: C15, contains: "not finished"}
flips:
  - name: a healthy profile, every move as it should be
    set:
      - {sheet: RunSheet, cell: D5, value: "50"}
      - {sheet: RunSheet, cell: D6, value: "46"}
      - {sheet: RunSheet, cell: D7, value: "11"}
      - {sheet: RunSheet, cell: D8, value: "49"}
      - {sheet: RunSheet, cell: D9, value: "0"}
      - {sheet: RunSheet, cell: D10, value: "480000"}
      - {sheet: RunSheet, cell: D11, value: "44"}
      - {sheet: RunSheet, cell: D12, value: "holds"}
    verdicts:
      - {sheet: RunSheet, cell: C14, expect: "8"}
      - {sheet: RunSheet, cell: C15, expect: "ready: the profile is defensible"}
  - name: somebody coerced the column first, so distinct is wrong and the pass keeps everything
    set:
      - {sheet: RunSheet, cell: D5, value: "50"}
      - {sheet: RunSheet, cell: D6, value: "41"}
      - {sheet: RunSheet, cell: D7, value: "50"}
      - {sheet: RunSheet, cell: D8, value: "49"}
      - {sheet: RunSheet, cell: D9, value: "0"}
      - {sheet: RunSheet, cell: D10, value: "480000"}
      - {sheet: RunSheet, cell: D11, value: "50"}
      - {sheet: RunSheet, cell: D12, value: "holds"}
    verdicts:
      - {sheet: RunSheet, cell: E6, expect: "differs"}
      - {sheet: RunSheet, cell: E7, expect: "differs"}
      - {sheet: RunSheet, cell: E11, expect: "differs"}
      - {sheet: RunSheet, cell: C15, expect: "hold: 3 moves differ from what they should show"}
```
