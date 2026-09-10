# Recalc manifest: Day 1 decision tool

Internal. `scripts/xlsx_recalc.py` reads the fenced block below, rebuilds the workbook through LibreOffice headless so every formula is evaluated rather than read from cache, asserts each verdict as shipped, then applies each flip and asserts the moved verdict.

The workbook ships with one planted defect per tab, so all three decision verdicts start blocking and the export tab holds the release. The flips below are what a learner does to clear each one, and the last flip proves the interior optimum: clearing conversion alone leaves the release held.

```yaml
workbook: C2_W01_D01_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Conversion, cell: B14, expect: "stop: the value the source sent is gone"}
  - {sheet: Accumulator, cell: B14, expect: "stop: move the starting value above the loop"}
  - {sheet: MissingKey, cell: B17, expect: "stop: write the default down beside the number it produced"}
  - {sheet: Export, cell: B10, expect: "3"}
  - {sheet: Export, cell: B11, expect: "hold: 3 of 3 decisions are still blocking"}
  - {sheet: Export, cell: B14, contains: "Kalpa Retail, Week 1 Day 1"}
flips:
  - name: the conversion moves to the point of use and the failures get counted
    set:
      - {sheet: Conversion, cell: B5, value: "at the point of use"}
      - {sheet: Conversion, cell: B6, value: "yes"}
      - {sheet: Conversion, cell: B8, value: "yes"}
    verdicts:
      - {sheet: Conversion, cell: B14, expect: "ship it: convert at the point of use and keep the record"}
      - {sheet: Export, cell: B11, expect: "hold: 2 of 3 decisions are still blocking"}
  - name: the accumulator moves above the loop and the printed total is the repaired one
    set:
      - {sheet: Accumulator, cell: B5, value: "above the loop"}
      - {sheet: Accumulator, cell: B6, value: 25720}
    verdicts:
      - {sheet: Accumulator, cell: B14, expect: "ship it: the accumulator starts once and the invariant holds"}
      - {sheet: Accumulator, cell: B12, expect: "holds"}
  - name: the default drops to zero and gets written down
    set:
      - {sheet: MissingKey, cell: B5, value: 0}
      - {sheet: MissingKey, cell: B9, value: "yes"}
    verdicts:
      - {sheet: MissingKey, cell: B17, expect: "ship it: the default is stated and it carries less than a tenth"}
      - {sheet: MissingKey, cell: B14, expect: "250"}
  - name: the conversion alone is cleared, and the release still holds
    set:
      - {sheet: Conversion, cell: B5, value: "at the point of use"}
      - {sheet: Conversion, cell: B6, value: "yes"}
      - {sheet: Conversion, cell: B8, value: "yes"}
    verdicts:
      - {sheet: Export, cell: B10, expect: "2"}
      - {sheet: Export, cell: B11, expect: "hold: 2 of 3 decisions are still blocking"}
```
