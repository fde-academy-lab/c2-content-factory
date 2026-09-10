# Recalc manifest: Day 4 decision tool

Internal. Three tabs, one planted defect on each, so all three start blocking and the export tab holds the release. The last flip proves the interior optimum.

```yaml
workbook: C2_W01_D04_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Typical, cell: B16, contains: "stop: the mean describes"}
  - {sheet: Typical, cell: B14, expect: "a long right tail"}
  - {sheet: Denominator, cell: B15, contains: "stop: you cannot rank on 9 records"}
  - {sheet: Sentence, cell: B14, expect: "stop: 3 of the four parts are missing"}
  - {sheet: Export, cell: B11, expect: "hold: 3 of 3 decisions are still blocking"}
  - {sheet: Export, cell: B14, contains: "Kalpa Retail, Week 1 Day 4"}
flips:
  - name: the statistic becomes the median
    set:
      - {sheet: Typical, cell: B5, value: "the median"}
    verdicts:
      - {sheet: Typical, cell: B16, expect: "ship it: the median, with the mean and its owner named"}
      - {sheet: Export, cell: B11, expect: "hold: 2 of 3 decisions are still blocking"}
  - name: the same tab, pointed at a symmetric column
    set:
      - {sheet: Typical, cell: B5, value: "the mean"}
      - {sheet: Typical, cell: B6, value: 1880}
      - {sheet: Typical, cell: B7, value: 1850}
      - {sheet: Typical, cell: B8, value: 240}
      - {sheet: Typical, cell: B9, value: 500}
    verdicts:
      - {sheet: Typical, cell: B14, expect: "roughly symmetric"}
      - {sheet: Typical, cell: B16, expect: "ship it: the shape is symmetric, so say which one you used"}
  - name: the ranking is dropped and the count is stated
    set:
      - {sheet: Denominator, cell: B8, value: "no"}
    verdicts:
      - {sheet: Denominator, cell: B15, expect: "hold: quote it with the count and say the base is small"}
      - {sheet: Denominator, cell: B13, expect: "11.1"}
  - name: the sentence gains all four parts
    set:
      - {sheet: Sentence, cell: B5, value: "yes"}
      - {sheet: Sentence, cell: B6, value: "yes"}
      - {sheet: Sentence, cell: B8, value: "yes"}
    verdicts:
      - {sheet: Sentence, cell: B14, expect: "ship it: nothing is left for the reader to guess"}
```
