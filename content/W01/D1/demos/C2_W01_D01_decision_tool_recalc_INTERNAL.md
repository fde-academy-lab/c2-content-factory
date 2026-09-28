# Recalculation manifest: Monday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move.

The workbook ships with one planted formula defect per tab, so as shipped every verdict asks for
its fix and the Export release reads "not ready". Each flip below is the fix a learner makes, and
the last applies all four, which is the only state that releases the brief.

```yaml
workbook: C2_W01_D01_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Sales, cell: B19, contains: "fix the total that leaves a row out"}
  - {sheet: Tree, cell: B16, contains: "fix the index that adds"}
  - {sheet: Average, cell: D13, contains: "fix the median formula"}
  - {sheet: Discount, cell: B12, contains: "fix the break-even formula"}
  - {sheet: Export, cell: B5, expect: "Not ready: 4 of the four tabs still carry a defect to fix first."}
flips:
  - name: the booked total counts the cancelled row too
    set: [{sheet: Sales, cell: C10, value: "=C5+C6+C7"}]
    verdicts:
      - {sheet: Sales, cell: B19, expect: "Revenue, all booked orders, 1 July to 26 September: Rs 5,44,810."}
      - {sheet: Export, cell: B5, contains: "3 of the four"}
  - name: the tree index multiplies its branches
    set: [{sheet: Tree, cell: B11, value: "=100*C5*C6*C7*C8*C9"}]
    verdicts:
      - {sheet: Tree, cell: B16, expect: "The moves reach the plan: revenue index 115.5 against 115."}
  - name: the fixed tree with a smaller customer lift
    set: [{sheet: Tree, cell: B11, value: "=100*C5*C6*C7*C8*C9"}, {sheet: Tree, cell: B5, value: 5}]
    verdicts:
      - {sheet: Tree, cell: B16, contains: "fall short: revenue index 110.3, 4.8 points"}
  - name: the median is the median
    set: [{sheet: Average, cell: D7, value: "=MEDIAN(A5:A14)"}]
    verdicts:
      - {sheet: Average, cell: D13, contains: "Report the median, Rs 2,200, as the typical order"}
  - name: the fixed median, asked for a total that must add up
    set: [{sheet: Average, cell: D7, value: "=MEDIAN(A5:A14)"}, {sheet: Average, cell: D11, value: "a total that must add up"}]
    verdicts:
      - {sheet: Average, cell: D13, contains: "Use the mean, Rs 19,720"}
  - name: the break-even lift is computed, not guessed
    set: [{sheet: Discount, cell: B9, value: "=100*(1/(1-B5/100)-1)"}]
    verdicts:
      - {sheet: Discount, cell: B12, contains: "needs 17.6 percent more volume"}
  - name: all four tabs fixed
    set:
      - {sheet: Sales, cell: C10, value: "=C5+C6+C7"}
      - {sheet: Tree, cell: B11, value: "=100*C5*C6*C7*C8*C9"}
      - {sheet: Average, cell: D7, value: "=MEDIAN(A5:A14)"}
      - {sheet: Discount, cell: B9, value: "=100*(1/(1-B5/100)-1)"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the note to Meera."}
      - {sheet: Export, cell: B7, contains: "Sales: Revenue, all booked orders"}
```
