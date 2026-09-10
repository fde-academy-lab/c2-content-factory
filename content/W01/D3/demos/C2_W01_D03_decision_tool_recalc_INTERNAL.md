# Recalc manifest: Day 3 decision tool

Internal. Three tabs, one planted defect on each, so all three start blocking and the export tab holds the release. The last flip proves the interior optimum.

```yaml
workbook: C2_W01_D03_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Missingness, cell: B15, expect: "stop: say what the absence means before you decide anything"}
  - {sheet: Duplicates, cell: B14, expect: "stop: your rule finds nothing while the id count says otherwise"}
  - {sheet: Extremes, cell: B17, expect: "stop: deleting a real order changes the business the file describes"}
  - {sheet: Extremes, cell: B12, expect: "87%"}
  - {sheet: Export, cell: B11, expect: "hold: 3 of 3 decisions are still blocking"}
  - {sheet: Export, cell: B14, contains: "Kalpa Retail, Week 1 Day 3"}
flips:
  - name: the absence of a discount is named as meaning something
    set:
      - {sheet: Missingness, cell: B8, value: "yes"}
    verdicts:
      - {sheet: Missingness, cell: B15, expect: "keep absent as absent, flag it, and write down what the absence means"}
      - {sheet: Export, cell: B11, expect: "hold: 2 of 3 decisions are still blocking"}
  - name: the same tab, pointed at a required field
    set:
      - {sheet: Missingness, cell: B5, value: "amount"}
      - {sheet: Missingness, cell: B6, value: 48}
      - {sheet: Missingness, cell: B9, value: "yes"}
    verdicts:
      - {sheet: Missingness, cell: B15, expect: "reject the incomplete rows, with the reason on each"}
  - name: the identity rule becomes order_id alone, and the pair is escalated
    set:
      - {sheet: Duplicates, cell: B5, value: "order_id"}
    verdicts:
      - {sheet: Duplicates, cell: B14, expect: "escalate to the order book owner, keep both rows and flag the pair"}
      - {sheet: Duplicates, cell: B12, expect: "1"}
  - name: the outlier is kept and flagged
    set:
      - {sheet: Extremes, cell: B5, value: "keep it and flag it"}
    verdicts:
      - {sheet: Extremes, cell: B17, expect: "ship it: kept, flagged, and its share of the total stated"}
      - {sheet: Extremes, cell: B14, expect: "12591"}
```
