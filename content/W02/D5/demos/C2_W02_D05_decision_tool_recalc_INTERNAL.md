# Recalculation manifest: Friday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which recalculates the decision tool through
LibreOffice and applies each fix a learner makes, to prove the verdicts move.

The tool ships with one planted formula defect per tab, so as shipped every verdict asks for its
fix and the Export release reads "not ready". The defects: the Pivot difference compares the pivot
with itself; the Lookup uses an approximate match; the Visible total foot uses SUM over a filtered
list; the Front page change divides by the current period; the Rule tests the room before Finance.
The last flip applies all five, which is the only state that releases the rule.

```yaml
workbook: C2_W02_D05_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Pivot, cell: B14, expect: "Fix the difference formula before trusting the pivot."}
  - {sheet: Lookup, cell: E11, expect: "Fix the match type before answering the chief of staff."}
  - {sheet: Lookup, cell: E9, contains: "returned C-0404 for C-0405"}
  - {sheet: Visible total, cell: B17, contains: "adds 8 rows while 3 are visible"}
  - {sheet: Front page, cell: B16, expect: "Fix the change formula before the card is drafted."}
  - {sheet: Rule, cell: B13, expect: "Fix the order of the tests before the rule is written down."}
  - {sheet: Export, cell: B5, expect: "Not ready: 5 of the five tabs still carry a defect to fix first."}
flips:
  - name: the difference compares the pivot with the warehouse
    set: [{sheet: Pivot, cell: B11, value: "=B7-B8"}]
    verdicts:
      - {sheet: Pivot, cell: B14, expect: "Do not slice this pivot: it is Rs 19.57 crore off the warehouse and carries 1.45 rows per order. Rebuild it on one row per order."}
      - {sheet: Export, cell: B5, contains: "4 of the five"}
  - name: the fixed pivot on one row per order
    set: [{sheet: Pivot, cell: B11, value: "=B7-B8"}, {sheet: Pivot, cell: B5, value: 1000}, {sheet: Pivot, cell: B7, value: 198400000}]
    verdicts:
      - {sheet: Pivot, cell: B14, expect: "Slice it live: the pivot reconciles to the warehouse."}
  - name: the lookup matches exactly and says when an id is missing
    set: [{sheet: Lookup, cell: E7, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}]
    verdicts:
      - {sheet: Lookup, cell: E11, expect: "C-0405 is not in the table: say so, and check the export before anyone answers."}
  - name: the fixed lookup on an id that is there
    set: [{sheet: Lookup, cell: E7, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}, {sheet: Lookup, cell: E5, value: "C-0403"}]
    verdicts:
      - {sheet: Lookup, cell: E11, expect: "C-0403: Rs 9,120, on the list."}
  - name: the foot adds only what the filter shows
    set: [{sheet: Visible total, cell: C14, value: "=SUBTOTAL(109,C5:C12)"}]
    verdicts:
      - {sheet: Visible total, cell: B19, expect: "The 3 members you can see spent Rs 25,500."}
  - name: the change is measured on the earlier period
    set: [{sheet: Front page, cell: B12, value: "=(B5-B6)/B6"}]
    verdicts:
      - {sheet: Front page, cell: B16, expect: "All segments, Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore); 100.0 percent of company revenue."}
  - name: the fixed card with the period left off
    set: [{sheet: Front page, cell: B12, value: "=(B5-B6)/B6"}, {sheet: Front page, cell: B7, value: ""}]
    verdicts:
      - {sheet: Front page, cell: B16, contains: "Not ready for the front page: add the period"}
  - name: the fixed card for Retail-Plus
    set:
      - {sheet: Front page, cell: B12, value: "=(B5-B6)/B6"}
      - {sheet: Front page, cell: B5, value: 413380}
      - {sheet: Front page, cell: B6, value: 585770}
      - {sheet: Front page, cell: B10, value: "Retail-Plus"}
    verdicts:
      - {sheet: Front page, cell: B16, contains: "Rs 4.13 lakh, down 29.4 percent on Q1, April to June 2026 (Rs 5.86 lakh); 0.4 percent"}
  - name: the rule decides the source of truth first
    set: [{sheet: Rule, cell: B10, value: '=IF(OR(B5="yes",B6="yes"),"the warehouse",IF(B7="yes","pandas","Excel"))'}]
    verdicts:
      - {sheet: Rule, cell: B13, expect: "The front-page revenue number: the warehouse computes it, and Excel presents it read-only, refreshed from the export."}
  - name: the fixed rule on a number nobody audits
    set:
      - {sheet: Rule, cell: B10, value: '=IF(OR(B5="yes",B6="yes"),"the warehouse",IF(B7="yes","pandas","Excel"))'}
      - {sheet: Rule, cell: B5, value: "no"}
      - {sheet: Rule, cell: B4, value: "A director's what-if on next quarter"}
    verdicts:
      - {sheet: Rule, cell: B13, expect: "A director's what-if on next quarter: Excel may own it, because nothing downstream audits it."}
  - name: all five tabs fixed
    set:
      - {sheet: Pivot, cell: B11, value: "=B7-B8"}
      - {sheet: Lookup, cell: E7, value: '=IFERROR(INDEX(A5:A12,MATCH(E5,A5:A12,0)),"not in the table")'}
      - {sheet: Visible total, cell: C14, value: "=SUBTOTAL(109,C5:C12)"}
      - {sheet: Front page, cell: B12, value: "=(B5-B6)/B6"}
      - {sheet: Rule, cell: B10, value: '=IF(OR(B5="yes",B6="yes"),"the warehouse",IF(B7="yes","pandas","Excel"))'}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the team note."}
      - {sheet: Export, cell: B7, contains: "Pivot: Do not slice this pivot"}
```
