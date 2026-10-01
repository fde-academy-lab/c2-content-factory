# Recalculation manifest: Monday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move.

The workbook ships with one planted formula defect per tab, so as shipped every verdict asks for
its fix and the Export release reads "not ready". Each flip below is the fix a learner makes, some
with a decision changed after the fix, and the last applies all four, which is the only state that
releases the line for Anand. The figures come from the warehouse through the builder,
`C2_W02_D01_build_decision_tool_TRAINER.py`.

| Tab | The planted defect | The fix |
|---|---|---|
| Customers | B12 divides the orders by the order rows whatever definition is chosen | `=ROUND(B9/B11,2)` |
| Division | The honest column F5:F12 still divides with INT | `=ROUND(C5/D5,2)` and down |
| Average | B11, the Q2 denominator under "spent Rs 0", is the Q1 buyers | `=IF(B9="spent Rs 0",C7,C6)` |
| Sample | E5 calls no ORDER BY repeatable, and the rerun after the reload drew 3 of Monday's five | `no` |

```yaml
workbook: C2_W02_D01_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Customers, cell: B15, contains: "fix the ratio that divides by the wrong count"}
  - {sheet: Division, cell: C20, contains: "fix the honest column"}
  - {sheet: Average, cell: B17, contains: "fix the q2 denominator"}
  - {sheet: Sample, cell: B15, contains: "fix the repeatable column"}
  - {sheet: Export, cell: B5, expect: "Not ready: 4 of the four tabs still carry a defect to fix first."}
flips:
  - name: orders per customer divides by the chosen count
    set: [{sheet: Customers, cell: B12, value: "=ROUND(B9/B11,2)"}]
    verdicts:
      - {sheet: Customers, cell: B15, expect: "Retail-Plus, Q2: 76 members bought, 1.84 orders each."}
      - {sheet: Export, cell: B5, contains: "3 of the four"}
  - name: the fixed ratio, with order rows chosen as customers
    set: [{sheet: Customers, cell: B12, value: "=ROUND(B9/B11,2)"}, {sheet: Customers, cell: B10, value: "order rows"}]
    verdicts:
      - {sheet: Customers, cell: B15, contains: "counting rows as customers erases the frequency branch"}
      - {sheet: Export, cell: B5, contains: "4 of the four"}
  - name: the fixed ratio, over the members on the customer table
    set: [{sheet: Customers, cell: B12, value: "=ROUND(B9/B11,2)"}, {sheet: Customers, cell: B10, value: "members on the customer table"}]
    verdicts:
      - {sheet: Customers, cell: B15, contains: "1.17 orders per member on the customer table"}
  - name: the honest column divides in numeric
    set:
      - {sheet: Division, cell: F5, value: "=ROUND(C5/D5,2)"}
      - {sheet: Division, cell: F6, value: "=ROUND(C6/D6,2)"}
      - {sheet: Division, cell: F7, value: "=ROUND(C7/D7,2)"}
      - {sheet: Division, cell: F8, value: "=ROUND(C8/D8,2)"}
      - {sheet: Division, cell: F9, value: "=ROUND(C9/D9,2)"}
      - {sheet: Division, cell: F10, value: "=ROUND(C10/D10,2)"}
      - {sheet: Division, cell: F11, value: "=ROUND(C11/D11,2)"}
      - {sheet: Division, cell: F12, value: "=ROUND(C12/D12,2)"}
    verdicts:
      - {sheet: Division, cell: C20, expect: "Retail-Plus frequency moved from 2.36 to 1.84, 22.0 percent down."}
  - name: the fixed column, read for Retail-Core
    set:
      - {sheet: Division, cell: F5, value: "=ROUND(C5/D5,2)"}
      - {sheet: Division, cell: F6, value: "=ROUND(C6/D6,2)"}
      - {sheet: Division, cell: F7, value: "=ROUND(C7/D7,2)"}
      - {sheet: Division, cell: F8, value: "=ROUND(C8/D8,2)"}
      - {sheet: Division, cell: F9, value: "=ROUND(C9/D9,2)"}
      - {sheet: Division, cell: F10, value: "=ROUND(C10/D10,2)"}
      - {sheet: Division, cell: F11, value: "=ROUND(C11/D11,2)"}
      - {sheet: Division, cell: F12, value: "=ROUND(C12/D12,2)"}
      - {sheet: Division, cell: C17, value: "Retail-Core"}
    verdicts:
      - {sheet: Division, cell: C20, expect: "Retail-Core frequency moved from 1.95 to 2.01, 3.0 percent up."}
  - name: the Q2 average divides by every member
    set: [{sheet: Average, cell: B11, value: '=IF(B9="spent Rs 0",C7,C6)'}]
    verdicts:
      - {sheet: Average, cell: B17, expect: "Spend per Retail-Plus member fell 29.4 percent, from Rs 5,474 to Rs 3,863, with all 107 members counted."}
  - name: the fixed average, with the lapsed members left out on purpose
    set: [{sheet: Average, cell: B11, value: '=IF(B9="spent Rs 0",C7,C6)'}, {sheet: Average, cell: B9, value: "is left out"}]
    verdicts:
      - {sheet: Average, cell: B17, expect: "Spend per buying member fell 15.5 percent; say it leaves out the 31 members with no Q2 order."}
  - name: no ORDER BY is not repeatable
    set: [{sheet: Sample, cell: E5, value: "no"}]
    verdicts:
      - {sheet: Sample, cell: B15, expect: "Order by order_id, then LIMIT 5: the analyst gets the same five orders on every run."}
  - name: the fixed table, with no ORDER BY chosen
    set: [{sheet: Sample, cell: E5, value: "no"}, {sheet: Sample, cell: B11, value: "nothing"}]
    verdicts:
      - {sheet: Sample, cell: B15, contains: "the analyst may trace a different five"}
  - name: all four tabs fixed
    set:
      - {sheet: Customers, cell: B12, value: "=ROUND(B9/B11,2)"}
      - {sheet: Division, cell: F5, value: "=ROUND(C5/D5,2)"}
      - {sheet: Division, cell: F6, value: "=ROUND(C6/D6,2)"}
      - {sheet: Division, cell: F7, value: "=ROUND(C7/D7,2)"}
      - {sheet: Division, cell: F8, value: "=ROUND(C8/D8,2)"}
      - {sheet: Division, cell: F9, value: "=ROUND(C9/D9,2)"}
      - {sheet: Division, cell: F10, value: "=ROUND(C10/D10,2)"}
      - {sheet: Division, cell: F11, value: "=ROUND(C11/D11,2)"}
      - {sheet: Division, cell: F12, value: "=ROUND(C12/D12,2)"}
      - {sheet: Average, cell: B11, value: '=IF(B9="spent Rs 0",C7,C6)'}
      - {sheet: Sample, cell: E5, value: "no"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready for Anand's sheet."}
      - {sheet: Export, cell: B7, contains: "Frequency: Retail-Plus frequency moved from 2.36 to 1.84"}
```
