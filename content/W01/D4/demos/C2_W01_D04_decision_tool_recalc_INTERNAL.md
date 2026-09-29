# Recalculation manifest: Thursday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move.

The workbook ships with one planted formula defect per tab, so as shipped every verdict asks for
its fix and the Export release reads "not ready". Each tab has two flips: the fix a learner makes,
and the fix with one input changed so the verdict moves to its other branch. The last flip applies
all four fixes, which is the only state that releases the note.

```yaml
workbook: C2_W01_D04_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Share, cell: B14, contains: "fix the share formula"}
  - {sheet: Share, cell: B12, contains: "indefensible"}
  - {sheet: Size, cell: B17, contains: "fix the segment fall formula"}
  - {sheet: Count, cell: B14, contains: "fix the threshold test"}
  - {sheet: Mix, cell: B18, contains: "fix the same-mix blend"}
  - {sheet: Export, cell: B5, expect: "Not ready: 4 of the four tabs still carry a defect to fix first."}
flips:
  - name: the share divides by the shuffles run
    set: [{sheet: Share, cell: B8, value: "=B6/B5"}]
    verdicts:
      - {sheet: Share, cell: B14, expect: "Chance makes a gap this large in about 4.2 of every 100 shuffles, so treat it as real and size it next."}
      - {sheet: Export, cell: B5, contains: "3 of the four"}
  - name: the fixed share with more shuffles as large as the gap
    set: [{sheet: Share, cell: B8, value: "=B6/B5"}, {sheet: Share, cell: B6, value: 400}]
    verdicts:
      - {sheet: Share, cell: B14, expect: "Chance makes a gap this large in about 8.0 of every 100 shuffles: inside the usual wobble, so not yet."}
  - name: the defensible sentence is chosen
    set: [{sheet: Share, cell: B11, value: "X of every 100 chance-only worlds"}]
    verdicts:
      - {sheet: Share, cell: B12, contains: "Defensible: the share counts chance-only worlds"}
  - name: the segment fall multiplies the gap by the members
    set: [{sheet: Size, cell: B11, value: "=B5*B6"}]
    verdicts:
      - {sheet: Size, cell: B17, expect: "The fall is Rs 11,20,000 a quarter, 1.2 percent of company revenue, and the fix breaks even when it wins back 22.3 percent of it. At 30 percent it pays, netting Rs 86,000 a quarter."}
  - name: the fixed size with a weaker win-back
    set: [{sheet: Size, cell: B11, value: "=B5*B6"}, {sheet: Size, cell: B9, value: 15}]
    verdicts:
      - {sheet: Size, cell: B17, contains: "At 15 percent it loses Rs 82,000 a quarter, so it waits for a cheaper fix."}
  - name: the threshold reads the count
    set: [{sheet: Count, cell: B11, value: '=IF(B9<30,"lead","finding")'}]
    verdicts:
      - {sheet: Count, cell: B14, expect: "A rise of 75.0 percent on 22 orders is a lead: watch it until it carries thirty or more. One order moves it by about 4.5 points."}
  - name: the fixed count on more orders
    set: [{sheet: Count, cell: B11, value: '=IF(B9<30,"lead","finding")'}, {sheet: Count, cell: B5, value: 20}, {sheet: Count, cell: B6, value: 26}]
    verdicts:
      - {sheet: Count, cell: B14, expect: "A rise of 30.0 percent on 46 orders is a finding worth testing."}
  - name: the same-mix blend uses the not-exposed mix
    set: [{sheet: Mix, cell: B14, value: "=B8/100*C5+(1-B8/100)*C6"}]
    verdicts:
      - {sheet: Mix, cell: B18, expect: "Every group spent less with the campaign; the blend rose only because the exposed group held more big spenders. Do not repeat it as designed; test it against a held-back group."}
  - name: the fixed mix when every group spent more
    set: [{sheet: Mix, cell: B14, value: "=B8/100*C5+(1-B8/100)*C6"}, {sheet: Mix, cell: C5, value: 5400}, {sheet: Mix, cell: C6, value: 1000}]
    verdicts:
      - {sheet: Mix, cell: B18, expect: "Every group spent more with the campaign, Rs 175 a customer at the same mix: credit it and size it next."}
  - name: all four tabs fixed
    set:
      - {sheet: Share, cell: B8, value: "=B6/B5"}
      - {sheet: Size, cell: B11, value: "=B5*B6"}
      - {sheet: Count, cell: B11, value: '=IF(B9<30,"lead","finding")'}
      - {sheet: Mix, cell: B14, value: "=B8/100*C5+(1-B8/100)*C6"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the note to Meera."}
      - {sheet: Export, cell: B7, contains: "Share: Chance makes a gap this large in about 4.2"}
      - {sheet: Export, cell: B7, contains: "Mix: Every group spent less"}
```
