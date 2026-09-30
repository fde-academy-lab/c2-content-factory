# Recalculation manifest: Monday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move. The build script
`C2_W01_D01_build_decision_tool_TRAINER.py` writes this file together with the workbook.

The workbook ships with one planted formula defect per tab, so as shipped every verdict asks for
its fix and the Export release reads "not ready". Each flip below is the fix a learner makes, some
with a decision changed after the fix, and the last applies all seven, which is the only state that
releases the brief.

```yaml
workbook: C2_W01_D01_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Sales, cell: B19, expect: "Fix the not-cancelled total before any number leaves the team."}
  - {sheet: Customers, cell: B17, expect: "Fix the customer count before you say anything about frequency."}
  - {sheet: Typical, cell: B14, expect: "Fix the typical order before it values anything."}
  - {sheet: Lifts, cell: B18, expect: "Fix the new revenue before you quote any growth."}
  - {sheet: Channel, cell: B18, expect: "Fix the delivered column before you rank any channel."}
  - {sheet: Sales, cell: B15, contains: "still carries the cancelled orders"}
  - {sheet: Lifts, cell: B16, contains: "disagree by Rs 648"}
  - {sheet: Fraction, cell: B15, expect: "Fix the AOV before it values any order."}
  - {sheet: Fraction, cell: B13, contains: "Rs 5,44,803, which lands on no revenue"}
  - {sheet: Edge, cell: B15, expect: "Fix the lost count before the sentence calls anyone lost."}
  - {sheet: Export, cell: B5, expect: "Not ready: tabs still carrying a defect, 7 of seven."}
flips:
  - name: the not-cancelled total leaves the cancelled orders out
    set: [{sheet: Sales, cell: C11, value: "=C5+C6"}]
    verdicts:
      - {sheet: Sales, cell: B19, expect: "Sales, not cancelled, 1 July to 26 September: Rs 5,35,760 on 26 orders, with Rs 9,050 and 4 orders of the booked total left out by the definition."}
      - {sheet: Export, cell: B5, expect: "Not ready: tabs still carrying a defect, 6 of seven."}
  - name: the fixed sales tab, read as delivered
    set: [{sheet: Sales, cell: C11, value: "=C5+C6"}, {sheet: Sales, cell: B14, value: "delivered"}]
    verdicts:
      - {sheet: Sales, cell: B19, contains: "Rs 5,20,790 on 21 orders, with Rs 24,020 and 9 orders"}
  - name: the AOV divides the chosen definition by itself
    set: [{sheet: Fraction, cell: B11, value: "=ROUND(B10/B9,0)"}]
    verdicts:
      - {sheet: Fraction, cell: B15, expect: "AOV on the delivered definition is Rs 24,800 on 21 orders, and it multiplies back to Rs 5,20,790."}
  - name: the fixed fraction, read as booked
    set: [{sheet: Fraction, cell: B11, value: "=ROUND(B10/B9,0)"}, {sheet: Fraction, cell: B8, value: "booked"}]
    verdicts:
      - {sheet: Fraction, cell: B15, contains: "Rs 18,160 on 30 orders"}
  - name: the edge holds back the recent buyers
    set: [{sheet: Edge, cell: B11, value: "=B7-B9"}]
    verdicts:
      - {sheet: Edge, cell: B15, expect: "7 came back, 7 are past the usual gap, and 9 bought too recently to judge, so at most 30 percent of customers look lost."}
  - name: customers counted by id
    set: [{sheet: Customers, cell: B11, value: "=SUM(B5:B8)"}]
    verdicts:
      - {sheet: Customers, cell: B17, expect: "23 customers placed 1.30 orders each; 7 of them (30 percent) came back and 16 bought once, so frequency is a live branch before acquisition."}
  - name: the fixed count on a file where nobody came back
    set: [{sheet: Customers, cell: B11, value: "=SUM(B5:B8)"}, {sheet: Customers, cell: B5, value: 30}, {sheet: Customers, cell: B6, value: 0}]
    verdicts:
      - {sheet: Customers, cell: B17, contains: "Every one of the 30 customers bought once"}
  - name: the typical order reads the median
    set: [{sheet: Typical, cell: B9, value: "=B7"}]
    verdicts:
      - {sheet: Typical, cell: B14, expect: "Report the median, Rs 2,205, as the typical order: the mean of Rs 18,160 is 8.2 times it, so a first order is worth about Rs 2,205 to the acquisition case."}
  - name: the fixed typical order, asked for a total that must add up
    set: [{sheet: Typical, cell: B9, value: "=B7"}, {sheet: Typical, cell: B11, value: "a total that must add up"}]
    verdicts:
      - {sheet: Typical, cell: B14, contains: "Use the mean, Rs 18,160, on the tree"}
  - name: new revenue multiplies the branches
    set: [{sheet: Lifts, cell: B13, value: "=ROUND(B4*C6*C7*C8,0)"}]
    verdicts:
      - {sheet: Lifts, cell: B18, expect: "Through the tree, revenue moves from Rs 64,810 to Rs 78,420, up 21.0 percent, which reaches the 15 percent plan; adding the lifts would have said Rs 77,772."}
  - name: the fixed tree, running the 15 percent discount
    set: [{sheet: Lifts, cell: B13, value: "=ROUND(B4*C6*C7*C8,0)"}, {sheet: Lifts, cell: B6, value: 0}, {sheet: Lifts, cell: B8, value: -15}]
    verdicts:
      - {sheet: Lifts, cell: B18, contains: "down 6.5 percent, which misses the 15 percent plan"}
  - name: delivered takes the returns out
    set: [{sheet: Channel, cell: F8, value: "=C8-D8-E8"}, {sheet: Channel, cell: F9, value: "=C9-D9-E9"}, {sheet: Channel, cell: F10, value: "=C10-D10-E10"}]
    verdicts:
      - {sheet: Channel, cell: B18, expect: "On consumer orders delivered, app leads with Rs 18,600 of Rs 40,790; returns took Rs 14,970 and cancellations Rs 9,050, so the channel view adds two leaks to name and leaves frequency first standing."}
  - name: the fixed channel tab, read as booked
    set: [{sheet: Channel, cell: F8, value: "=C8-D8-E8"}, {sheet: Channel, cell: F9, value: "=C9-D9-E9"}, {sheet: Channel, cell: F10, value: "=C10-D10-E10"}, {sheet: Channel, cell: B4, value: "booked"}]
    verdicts:
      - {sheet: Channel, cell: B18, contains: "On consumer orders booked, web leads with Rs 27,290 of Rs 64,810"}
  - name: six of seven fixed still holds the release
    set:
      - {sheet: Sales, cell: C11, value: "=C5+C6"}
      - {sheet: Customers, cell: B11, value: "=SUM(B5:B8)"}
      - {sheet: Typical, cell: B9, value: "=B7"}
      - {sheet: Lifts, cell: B13, value: "=ROUND(B4*C6*C7*C8,0)"}
      - {sheet: Fraction, cell: B11, value: "=ROUND(B10/B9,0)"}
      - {sheet: Edge, cell: B11, value: "=B7-B9"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Not ready: tabs still carrying a defect, 1 of seven."}
  - name: all seven tabs fixed
    set:
      - {sheet: Sales, cell: C11, value: "=C5+C6"}
      - {sheet: Customers, cell: B11, value: "=SUM(B5:B8)"}
      - {sheet: Typical, cell: B9, value: "=B7"}
      - {sheet: Lifts, cell: B13, value: "=ROUND(B4*C6*C7*C8,0)"}
      - {sheet: Channel, cell: F8, value: "=C8-D8-E8"}
      - {sheet: Channel, cell: F9, value: "=C9-D9-E9"}
      - {sheet: Channel, cell: F10, value: "=C10-D10-E10"}
      - {sheet: Fraction, cell: B11, value: "=ROUND(B10/B9,0)"}
      - {sheet: Edge, cell: B11, value: "=B7-B9"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the note to Meera."}
      - {sheet: Export, cell: B7, contains: "Order value: AOV on the delivered definition is Rs 24,800"}
      - {sheet: Export, cell: B7, contains: "Rs 5,35,760 on 26 orders"}
      - {sheet: Export, cell: B7, contains: "Customers: 23 customers placed 1.30 orders each"}
      - {sheet: Export, cell: B7, contains: "hold the Rs 12 crore until Tuesday's two quarters"}
```
