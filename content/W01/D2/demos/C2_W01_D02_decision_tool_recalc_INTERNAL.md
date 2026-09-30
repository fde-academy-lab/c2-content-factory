# Recalculation manifest: Tuesday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move.

The workbook ships with one planted formula defect per tab, so as shipped every verdict asks for
its fix and the Export release reads "not ready". The defects are: Window!B10 divides the tile's
revenue by Q1's weeks; Tree!C10 divides Q2 revenue by customers; Discount!C12 divides the orders
with a discount by every order; Rollup!B10 averages the segment averages; Segments!D5:D8 return an empty cell
for any change beyond 30 percent, as the printing helper does. Each flip below is the fix a learner
makes, some with a changed choice or input to prove the verdict follows it, and the last applies
all five, which is the only state that releases the brief.

```yaml
workbook: C2_W01_D02_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Window, cell: B18, contains: "fix the weekly rate that divides by the wrong weeks"}
  - {sheet: Tree, cell: B15, contains: "fix the rate with the wrong denominator"}
  - {sheet: Discount, cell: B18, contains: "fix the where-recorded share"}
  - {sheet: Rollup, cell: B15, contains: "fix the roll-up that averages the averages"}
  - {sheet: Segments, cell: B16, contains: "fix the change formula that drops the big moves"}
  - {sheet: Segments, cell: B12, contains: "2 of 4 segments went in and came out empty"}
  - {sheet: Export, cell: B5, expect: "Not ready: 5 of the five tabs still carry a defect to fix first."}
flips:
  - name: the tile's weekly rate divides by its own weeks
    set: [{sheet: Window, cell: B10, value: "=B6/C6"}]
    verdicts:
      - {sheet: Window, cell: B18, expect: "Refuse the comparison: 11 weeks against 13 reads as 25.9 percent; close the window or use a rate per week."}
      - {sheet: Export, cell: B5, contains: "4 of the five"}
  - name: the fixed window, compared as closed quarters
    set: [{sheet: Window, cell: B10, value: "=B6/C6"}, {sheet: Window, cell: B13, value: "closed quarters"}]
    verdicts:
      - {sheet: Window, cell: B18, expect: "Revenue fell 11.0 percent between closed quarters of 13 weeks each."}
  - name: the fixed window, as a rate per week
    set: [{sheet: Window, cell: B10, value: "=B6/C6"}, {sheet: Window, cell: B13, value: "rate per week"}]
    verdicts:
      - {sheet: Window, cell: B18, expect: "Per week, revenue fell 12.4 percent on the cut window."}
  - name: revenue per order divides by orders
    set: [{sheet: Tree, cell: C10, value: "=C7/C6"}]
    verdicts:
      - {sheet: Tree, cell: B15, expect: "Customers held at 69, so acquisition is not the branch that moved; orders per customer went from 1.65 to 1.25 and fell 24.6 percent."}
  - name: the fixed tree with more customers in Q2
    set: [{sheet: Tree, cell: C10, value: "=C7/C6"}, {sheet: Tree, cell: C5, value: 80}]
    verdicts:
      - {sheet: Tree, cell: B15, contains: "Customers rose 15.9 percent, so the customer branch moved"}
  - name: the where-recorded share divides by recorded orders, default still zero
    set: [{sheet: Discount, cell: C12, value: "=C7/C6"}]
    verdicts:
      - {sheet: Discount, cell: B18, contains: "Refuse the zero default"}
  - name: the fixed discount, reported where recorded
    set: [{sheet: Discount, cell: C12, value: "=C7/C6"}, {sheet: Discount, cell: B16, value: "report where recorded"}]
    verdicts:
      - {sheet: Discount, cell: B18, expect: "Report the share where recorded, 60.0% to 66.7% of orders, with the orders that lack the field reported separately."}
  - name: the fixed discount, bounded
    set: [{sheet: Discount, cell: C12, value: "=C7/C6"}, {sheet: Discount, cell: B16, value: "bound with the largest value"}]
    verdicts:
      - {sheet: Discount, cell: B18, expect: "The discount branch is at most Rs 6,750, 0.29 percent of the fall, so it did not move revenue."}
  - name: the roll-up is weighted by customers
    set: [{sheet: Rollup, cell: B10, value: "=SUM(D5:D8)/SUM(B5:B8)"}]
    verdicts:
      - {sheet: Rollup, cell: B15, expect: "Frequency carries the fall: orders per customer 1.65 to 1.25, which fell 24.6 percent."}
  - name: the weighted roll-up if Retail-Plus had held its orders
    set: [{sheet: Rollup, cell: B10, value: "=SUM(D5:D8)/SUM(B5:B8)"}, {sheet: Rollup, cell: E6, value: 51}]
    verdicts:
      - {sheet: Rollup, cell: B15, expect: "Frequency fell 2.6 percent, 1.65 to 1.61, too little to carry the fall on its own."}
  - name: the change formula returns every change
    set:
      - {sheet: Segments, cell: D5, value: "=ROUND(100*(C5/B5-1),1)"}
      - {sheet: Segments, cell: D6, value: "=ROUND(100*(C6/B6-1),1)"}
      - {sheet: Segments, cell: D7, value: "=ROUND(100*(C7/B7-1),1)"}
      - {sheet: Segments, cell: D8, value: "=ROUND(100*(C8/B8-1),1)"}
    verdicts:
      - {sheet: Segments, cell: B16, contains: "is Retail-Plus, -49.0 percent"}
      - {sheet: Segments, cell: B12, expect: "Every segment that went in came out with a number."}
  - name: all five tabs fixed
    set:
      - {sheet: Window, cell: B10, value: "=B6/C6"}
      - {sheet: Window, cell: B13, value: "closed quarters"}
      - {sheet: Tree, cell: C10, value: "=C7/C6"}
      - {sheet: Discount, cell: C12, value: "=C7/C6"}
      - {sheet: Discount, cell: B16, value: "report where recorded"}
      - {sheet: Rollup, cell: B10, value: "=SUM(D5:D8)/SUM(B5:B8)"}
      - {sheet: Segments, cell: D5, value: "=ROUND(100*(C5/B5-1),1)"}
      - {sheet: Segments, cell: D6, value: "=ROUND(100*(C6/B6-1),1)"}
      - {sheet: Segments, cell: D7, value: "=ROUND(100*(C7/B7-1),1)"}
      - {sheet: Segments, cell: D8, value: "=ROUND(100*(C8/B8-1),1)"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the note to Meera."}
      - {sheet: Export, cell: B7, contains: "Window: Revenue fell 11.0 percent between closed quarters"}
      - {sheet: Export, cell: B7, contains: "Segments: The largest fall in orders per customer is Retail-Plus"}
```
