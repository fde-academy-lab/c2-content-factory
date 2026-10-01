# Recalculation manifest: Friday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move. The build script
`C2_W02_D05_build_decision_tool_TRAINER.py` writes this file together with the workbook.

The workbook ships with one planted formula defect per chapter tab, so as shipped every verdict asks
for its fix and the Export release reads "not ready". Each flip below is the fix a learner makes, some
with a decision changed after the fix. Five fixes still hold the release, a sixth fix typed as a
number instead of a formula still holds it, and only all six fixed as formulas releases the note.

```yaml
workbook: C2_W02_D05_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Tree, cell: B59, expect: "Fix the revenue-per-order leaf before the tree goes on a page."}
  - {sheet: Tree, cell: B57, contains: "multiply back to Rs 21.94 crore against the segment's Rs 19,65,99,040"}
  - {sheet: Tree, cell: B8, expect: "a PivotTable with each leaf beside it as a ratio of its sums"}
  - {sheet: Quarters, cell: B26, expect: "Fix the revenue count before the tree reaches the deck."}
  - {sheet: Quarters, cell: B24, contains: "on 9 rows for 6 orders: the revenue adds every payment row"}
  - {sheet: Lookup, cell: E17, expect: "Fix the match type before answering the chief of staff."}
  - {sheet: Lookup, cell: E15, contains: "returned C-0404 for C-0405 while COUNTIF finds 0 rows"}
  - {sheet: Card, cell: B18, expect: "Fix the change formula before the card is drafted."}
  - {sheet: Card, cell: B16, contains: "reads 41.7 percent because it is divided by the number's own period; measured on the earlier period it is 29.4 percent"}
  - {sheet: Rule, cell: B27, expect: "Fix the collected column before anyone reads an outstanding figure."}
  - {sheet: Rule, cell: B25, contains: "Collected adds Rs 22,000 while the payment rows hold Rs 30,000"}
  - {sheet: Director, cell: B21, expect: "Fix the foot before reading it as the city's list."}
  - {sheet: Director, cell: B19, contains: "adds all 8 rows while 3 are on screen"}
  - {sheet: Export, cell: B5, expect: "0"}
  - {sheet: Export, cell: B6, expect: "Not ready: 6 of 6 tabs still carry a defect."}
flips:
  - name: the leaf is revenue over orders
    set: [{sheet: Tree, cell: B55, value: "=B53/B52"}]
    verdicts:
      - {sheet: Tree, cell: B59, expect: "Hand the directors a PivotTable with each leaf beside it as a ratio of its sums. Business: 39 customers placed 4.82 orders each at Rs 10,45,740 an order, Rs 19,65,99,040 in all, and the leaves multiply back to the rupee."}
      - {sheet: Export, cell: B6, expect: "Not ready: 5 of 6 tabs still carry a defect."}
  - name: the fixed tree for a director who changes an assumption
    set: [{sheet: Tree, cell: B55, value: "=B53/B52"}, {sheet: Tree, cell: B6, value: "yes"}]
    verdicts:
      - {sheet: Tree, cell: B59, contains: "Hand the directors a SUMIFS grid, which recalculates at once."}
  - name: each order counted once
    set:
      - {sheet: Quarters, cell: B22, value: '=SUMIFS(C5:C13,B5:B13,"Q1",E5:E13,1)'}
      - {sheet: Quarters, cell: C22, value: '=SUMIFS(C5:C13,B5:B13,"Q2",E5:E13,1)'}
    verdicts:
      - {sheet: Quarters, cell: B26, expect: "Ship the tree for both quarters: Q1 Rs 6,500 and Q2 Rs 6,700, up 3.1 percent, each order counted once and tied to the control totals; added on every row, the export would have said down 25.8 percent."}
  - name: the fixed count on an export that is one order short
    set:
      - {sheet: Quarters, cell: B22, value: '=SUMIFS(C5:C13,B5:B13,"Q1",E5:E13,1)'}
      - {sheet: Quarters, cell: C22, value: '=SUMIFS(C5:C13,B5:B13,"Q2",E5:E13,1)'}
      - {sheet: Quarters, cell: C16, value: 4}
      - {sheet: Quarters, cell: C17, value: 8700}
    verdicts:
      - {sheet: Quarters, cell: B26, expect: "Hold the tree: it counts each order once and still misses the control totals."}
  - name: the lookup matches exactly and says when an id is missing
    set: [{sheet: Lookup, cell: E8, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}]
    verdicts:
      - {sheet: Lookup, cell: E17, contains: "C-0405 is not in the table: say so, and check the export before anyone answers. On Microsoft 365, the file carries XLOOKUP with its fourth argument"}
  - name: an exact match with no not-found path
    set: [{sheet: Lookup, cell: E8, value: "=INDEX(A5:A12,MATCH(E5,A5:A12,0))"}]
    verdicts:
      - {sheet: Lookup, cell: E18, expect: "0"}
      - {sheet: Lookup, cell: E17, expect: "Fix the lookup's not-found path before answering the chief of staff."}
  - name: the fixed lookup on an id that is there, for a laptop on Excel 2019
    set:
      - {sheet: Lookup, cell: E8, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}
      - {sheet: Lookup, cell: E5, value: "C-0403"}
      - {sheet: Lookup, cell: E6, value: "Excel 2019"}
    verdicts:
      - {sheet: Lookup, cell: E17, contains: "C-0403: Rs 9,120, on the list. On Excel 2019, the file carries IFERROR around INDEX and MATCH"}
  - name: the change is measured on the earlier period
    set: [{sheet: Card, cell: B12, value: "=(B6-B8)/B8"}]
    verdicts:
      - {sheet: Card, cell: B18, expect: "Retail-Plus, Q2, July to September 2026: Rs 4.13 lakh, down 29.4 percent on Q1, April to June 2026 (Rs 5.86 lakh), a fall of Rs 1.72 lakh; 0.4 percent of company revenue."}
  - name: the fixed card with its period left off
    set: [{sheet: Card, cell: B12, value: "=(B6-B8)/B8"}, {sheet: Card, cell: B7, value: ""}]
    verdicts:
      - {sheet: Card, cell: B18, contains: "Not ready for the front page: add its period"}
  - name: the fixed card for the whole company
    set:
      - {sheet: Card, cell: B12, value: "=(B6-B8)/B8"}
      - {sheet: Card, cell: B5, value: "All segments"}
      - {sheet: Card, cell: B6, value: 98400000}
      - {sheet: Card, cell: B8, value: 100000000}
    verdicts:
      - {sheet: Card, cell: B18, expect: "All segments, Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore), a fall of Rs 16.00 lakh; 100.0 percent of company revenue."}
  - name: collected adds every payment
    set:
      - {sheet: Rule, cell: D13, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A13)"}
      - {sheet: Rule, cell: D14, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A14)"}
      - {sheet: Rule, cell: D15, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A15)"}
    verdicts:
      - {sheet: Rule, cell: B27, expect: "Booked against collected for the deck pack lives in the warehouse, and the workbook keeps a SUMIFS beside it only as a check. On the invented orders, collected is Rs 30,000 of Rs 36,000 booked, and Rs 6,000 is outstanding."}
  - name: the fixed rule placing a director's what-if
    set:
      - {sheet: Rule, cell: D13, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A13)"}
      - {sheet: Rule, cell: D14, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A14)"}
      - {sheet: Rule, cell: D15, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A15)"}
      - {sheet: Rule, cell: B5, value: "A director's what-if in the room"}
      - {sheet: Rule, cell: B6, value: "no"}
      - {sheet: Rule, cell: B7, value: "no"}
      - {sheet: Rule, cell: B9, value: "yes"}
    verdicts:
      - {sheet: Rule, cell: B27, contains: "A director's what-if in the room lives in the workbook. On the invented orders"}
  - name: the foot follows the filter
    set: [{sheet: Director, cell: C14, value: "=SUBTOTAL(109,C5:C12)"}]
    verdicts:
      - {sheet: Director, cell: B21, expect: "The 3 members on screen spent Rs 25,500, and a Rs 500 voucher for each of them costs Rs 1,500; the list's figures stay as they are, because the assumption sits in its own yellow cell."}
  - name: the fixed foot with a director's Rs 750 voucher
    set: [{sheet: Director, cell: C14, value: "=SUBTOTAL(109,C5:C12)"}, {sheet: Director, cell: C17, value: 750}]
    verdicts:
      - {sheet: Director, cell: B21, contains: "a Rs 750 voucher for each of them costs Rs 2,250"}
  - name: five of six fixed still holds the release
    set:
      - {sheet: Tree, cell: B55, value: "=B53/B52"}
      - {sheet: Quarters, cell: B22, value: '=SUMIFS(C5:C13,B5:B13,"Q1",E5:E13,1)'}
      - {sheet: Quarters, cell: C22, value: '=SUMIFS(C5:C13,B5:B13,"Q2",E5:E13,1)'}
      - {sheet: Lookup, cell: E8, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}
      - {sheet: Card, cell: B12, value: "=(B6-B8)/B8"}
      - {sheet: Rule, cell: D13, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A13)"}
      - {sheet: Rule, cell: D14, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A14)"}
      - {sheet: Rule, cell: D15, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A15)"}
    verdicts:
      - {sheet: Export, cell: B6, expect: "Not ready: 1 of 6 tabs still carries a defect."}
  - name: the sixth fix typed as a number holds the release
    set:
      - {sheet: Tree, cell: B55, value: "=B53/B52"}
      - {sheet: Quarters, cell: B22, value: '=SUMIFS(C5:C13,B5:B13,"Q1",E5:E13,1)'}
      - {sheet: Quarters, cell: C22, value: '=SUMIFS(C5:C13,B5:B13,"Q2",E5:E13,1)'}
      - {sheet: Lookup, cell: E8, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}
      - {sheet: Card, cell: B12, value: "=(B6-B8)/B8"}
      - {sheet: Rule, cell: D13, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A13)"}
      - {sheet: Rule, cell: D14, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A14)"}
      - {sheet: Rule, cell: D15, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A15)"}
      - {sheet: Director, cell: C14, value: 25500}
    verdicts:
      - {sheet: Export, cell: B5, expect: "1"}
      - {sheet: Export, cell: B6, expect: "Not ready: 1 of 6 tabs still carries a defect, and 1 computed cell holds a typed figure where a formula belongs."}
  - name: all six tabs fixed
    set:
      - {sheet: Tree, cell: B55, value: "=B53/B52"}
      - {sheet: Quarters, cell: B22, value: '=SUMIFS(C5:C13,B5:B13,"Q1",E5:E13,1)'}
      - {sheet: Quarters, cell: C22, value: '=SUMIFS(C5:C13,B5:B13,"Q2",E5:E13,1)'}
      - {sheet: Lookup, cell: E8, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}
      - {sheet: Card, cell: B12, value: "=(B6-B8)/B8"}
      - {sheet: Rule, cell: D13, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A13)"}
      - {sheet: Rule, cell: D14, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A14)"}
      - {sheet: Rule, cell: D15, value: "=SUMIFS($C$19:$C$22,$B$19:$B$22,A15)"}
      - {sheet: Director, cell: C14, value: "=SUBTOTAL(109,C5:C12)"}
    verdicts:
      - {sheet: Export, cell: B6, expect: "Ready to paste into the note to Kavya."}
      - {sheet: Export, cell: B8, contains: "Tree: Hand the directors a PivotTable"}
      - {sheet: Export, cell: B8, contains: "Card: Retail-Plus, Q2, July to September 2026: Rs 4.13 lakh, down 29.4 percent"}
      - {sheet: Export, cell: B8, contains: "Director: The 3 members on screen spent Rs 25,500"}
```
