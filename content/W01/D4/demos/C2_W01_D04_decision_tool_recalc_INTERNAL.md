# Recalculation manifest: Thursday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move.

The workbook ships with one planted formula defect per tab, so as shipped every verdict asks for
its fix and the Export release reads "not ready". Each tab has the fix a learner makes and at least
one more flip with inputs changed so the verdict moves to another branch: the Share tab runs its
three readings (rare, borderline, the usual wobble) under each direction choice, and the Count tab
shows many orders from few customers staying a lead. The last flip applies all four fixes, which is
the only state that releases the note.

```yaml
workbook: C2_W01_D04_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Share, cell: B20, contains: "fix the share formula"}
  - {sheet: Share, cell: B18, contains: "indefensible"}
  - {sheet: Size, cell: B17, contains: "fix the segment fall formula"}
  - {sheet: Count, cell: B15, contains: "fix the threshold test"}
  - {sheet: Mix, cell: B18, contains: "fix the same-mix blend"}
  - {sheet: Export, cell: B5, expect: "Not ready: 4 of the four tabs still carry a defect to fix first."}
flips:
  - name: the share divides by the flips run, with no direction decided in advance
    set: [{sheet: Share, cell: B12, value: "=B6/B5"}]
    verdicts:
      - {sheet: Share, cell: B20, expect: "No direction was decided before the test, so both go in the note: a fall this large turns up in about 4.2 of every 100 flips, and a move that large either way in about 8.0. By the reading agreed before the test, that is borderline: size it, and watch it before acting on it alone."}
      - {sheet: Export, cell: B5, contains: "3 of the four"}
  - name: the fixed share, falls only decided in advance, on a rarer fall
    set: [{sheet: Share, cell: B12, value: "=B6/B5"}, {sheet: Share, cell: B8, value: "falls only"}, {sheet: Share, cell: B6, value: 30}, {sheet: Share, cell: B7, value: 45}]
    verdicts:
      - {sheet: Share, cell: B20, expect: "Counting falls only, as decided before the test, chance makes a fall this large in about 0.6 of every 100 flips, and a move that large either way in about 0.9. By the reading agreed before the test, that is rare as pure wobble, so size it next."}
  - name: the fixed share, either way decided in advance, on a common move
    set: [{sheet: Share, cell: B12, value: "=B6/B5"}, {sheet: Share, cell: B8, value: "either way"}, {sheet: Share, cell: B6, value: 900}, {sheet: Share, cell: B7, value: 1700}]
    verdicts:
      - {sheet: Share, cell: B20, expect: "Counting either way, as decided before the test, chance makes a move this large in about 34.0 of every 100 flips, and a fall this large in about 18.0. By the reading agreed before the test, that is inside the usual wobble, so not yet."}
  - name: the defensible sentence is chosen
    set: [{sheet: Share, cell: B17, value: "X of every 100 chance-only worlds"}]
    verdicts:
      - {sheet: Share, cell: B18, contains: "Defensible: the share counts chance-only worlds"}
  - name: the segment fall multiplies the gap by the members
    set: [{sheet: Size, cell: B11, value: "=B5*B6"}]
    verdicts:
      - {sheet: Size, cell: B17, expect: "The fall is Rs 11,20,000 a quarter, 1.2 percent of company revenue, and the fix breaks even when it wins back 22.3 percent of it. At 30 percent it pays, netting Rs 86,000 a quarter."}
  - name: the fixed size with a weaker win-back
    set: [{sheet: Size, cell: B11, value: "=B5*B6"}, {sheet: Size, cell: B9, value: 15}]
    verdicts:
      - {sheet: Size, cell: B17, contains: "At 15 percent it loses Rs 82,000 a quarter, so it waits for a cheaper fix."}
  - name: the threshold reads the customers
    set: [{sheet: Count, cell: B12, value: '=IF(B7<30,"lead","worth testing")'}]
    verdicts:
      - {sheet: Count, cell: B15, expect: "A rise of 75.0 percent on 22 orders from 5 customers is a lead: watch it until more customers buy, thirty or more, since more orders from the same few customers add no new evidence. One order moves it by about 4.5 points."}
  - name: the fixed count on more customers
    set: [{sheet: Count, cell: B12, value: '=IF(B7<30,"lead","worth testing")'}, {sheet: Count, cell: B5, value: 20}, {sheet: Count, cell: B6, value: 26}, {sheet: Count, cell: B7, value: 40}]
    verdicts:
      - {sheet: Count, cell: B15, expect: "A rise of 30.0 percent on 46 orders from 40 customers is worth testing on its count."}
  - name: the fixed count on many orders from few customers
    set: [{sheet: Count, cell: B12, value: '=IF(B7<30,"lead","worth testing")'}, {sheet: Count, cell: B5, value: 20}, {sheet: Count, cell: B6, value: 26}, {sheet: Count, cell: B7, value: 6}]
    verdicts:
      - {sheet: Count, cell: B15, expect: "A rise of 30.0 percent on 46 orders from 6 customers is a lead: watch it until more customers buy, thirty or more, since more orders from the same few customers add no new evidence. One order moves it by about 2.2 points."}
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
      - {sheet: Share, cell: B12, value: "=B6/B5"}
      - {sheet: Size, cell: B11, value: "=B5*B6"}
      - {sheet: Count, cell: B12, value: '=IF(B7<30,"lead","worth testing")'}
      - {sheet: Mix, cell: B14, value: "=B8/100*C5+(1-B8/100)*C6"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the note to Meera."}
      - {sheet: Export, cell: B7, contains: "Share: No direction was decided before the test"}
      - {sheet: Export, cell: B7, contains: "Count: A rise of 75.0 percent on 22 orders from 5 customers is a lead"}
      - {sheet: Export, cell: B7, contains: "Mix: Every group spent less"}
```
