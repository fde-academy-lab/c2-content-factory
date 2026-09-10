# Recalc manifest: Day 2 decision tool

Internal. Three tabs, one planted defect on each, so all three verdicts start blocking and the export tab holds the release. The last flip proves the interior optimum: clearing the stance alone leaves two decisions blocking.

```yaml
workbook: C2_W01_D02_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Stance, cell: B14, expect: "stop: the total is right and the sentence beside it is false"}
  - {sheet: Ownership, cell: B12, expect: "stop: one function cannot be right for callers that need different things"}
  - {sheet: Format, cell: B13, expect: "stop: a CSV gives every value back as text"}
  - {sheet: Stance, cell: B11, expect: "2"}
  - {sheet: Export, cell: B11, expect: "hold: 3 of 3 decisions are still blocking"}
  - {sheet: Export, cell: B14, contains: "Kalpa Retail, Week 1 Day 2"}
flips:
  - name: the stance becomes catch by name, counted, with reasons
    set:
      - {sheet: Stance, cell: B5, value: "except ValueError, counted"}
      - {sheet: Stance, cell: B8, value: "yes"}
    verdicts:
      - {sheet: Stance, cell: B14, expect: "ship it: caught by name, counted, and every rejection carries its reason"}
      - {sheet: Export, cell: B11, expect: "hold: 2 of 3 decisions are still blocking"}
  - name: the decision moves out to the caller
    set:
      - {sheet: Ownership, cell: B5, value: "in the caller"}
    verdicts:
      - {sheet: Ownership, cell: B12, expect: "ship it: the function converts or refuses and the caller decides"}
      - {sheet: Ownership, cell: B10, expect: "0"}
  - name: the format moves to JSON and the partial-file requirement is dropped
    set:
      - {sheet: Format, cell: B5, value: "JSON"}
      - {sheet: Format, cell: B8, value: "no"}
    verdicts:
      - {sheet: Format, cell: B13, expect: "ship it: the agreement matches what the reader needs"}
  - name: JSON is chosen while a partial file must still be usable
    set:
      - {sheet: Format, cell: B5, value: "JSON"}
    verdicts:
      - {sheet: Format, cell: B13, expect: "stop: a truncated JSON file yields no records at all"}
```
