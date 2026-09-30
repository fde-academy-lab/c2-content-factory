# Recalculation manifest: Wednesday's decision tool

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then applies each fix to prove the verdicts move.

The workbook ships with one planted defect per tab, so as shipped every verdict asks for its fix
and the Export release reads "not ready". Each flip below is the fix a learner makes, and the last
applies all four, which is the only state that releases the note. Every record in the workbook is
invented.

```yaml
workbook: C2_W01_D03_decision_tool_STUDENT.xlsx
verdicts:
  - {sheet: Profile, cell: E11, contains: "fix the convertible count"}
  - {sheet: Identity, cell: B20, contains: "fix the key"}
  - {sheet: Tail, cell: E13, contains: "fix the revenue that drops the tail"}
  - {sheet: Reconcile, cell: B13, expect: "Reconciled: send it to Anand."}
  - {sheet: Export, cell: B5, expect: "Not ready: 4 of the four tabs still carry a defect to fix first."}
flips:
  - name: the convertible count counts numbers only
    set: [{sheet: Profile, cell: E6, value: "=COUNT(B5:B14)"}]
    verdicts:
      - {sheet: Profile, cell: E11, expect: "Log 1 failure with its line and reason; 9 of 10 amounts convert, totalling Rs 20,300."}
      - {sheet: Export, cell: B5, contains: "3 of the four"}
  - name: the key is the order_id
    set: [{sheet: Identity, cell: B16, value: "order_id"}]
    verdicts:
      - {sheet: Identity, cell: B20, expect: "Set aside 3 rows by the order_id rule, keep 5 orders, and log a reason for each row set aside."}
  - name: the fence flags and never removes
    set: [{sheet: Tail, cell: E9, value: "=SUM(A5:A12)"}]
    verdicts:
      - {sheet: Tail, cell: E13, contains: "Keep all 8 orders, Rs 56,90,000; flag 1 above the fence"}
  - name: a tighter fence flags more and still keeps them
    set: [{sheet: Tail, cell: E9, value: "=SUM(A5:A12)"}, {sheet: Tail, cell: E7, value: 1.4}]
    verdicts:
      - {sheet: Tail, cell: E13, contains: "flag 2 above the fence"}
  - name: the verdict reads the rupees too
    set: [{sheet: Reconcile, cell: B13, value: "=IF(AND(B6=B7+B8,B9=B10),\"Reconciled in rows and rupees: send it to Anand.\",\"Rows reconcile and rupees miss the books by \"&TEXT(B10-B9,\"#,##0\")&\": keep the copy that validates.\")"}]
    verdicts:
      - {sheet: Reconcile, cell: B13, expect: "Rows reconcile and rupees miss the books by 2,600: keep the copy that validates."}
  - name: the fixed verdict with the copy that validates
    set:
      - {sheet: Reconcile, cell: B13, value: "=IF(AND(B6=B7+B8,B9=B10),\"Reconciled in rows and rupees: send it to Anand.\",\"Rows reconcile and rupees miss the books by \"&TEXT(B10-B9,\"#,##0\")&\": keep the copy that validates.\")"}
      - {sheet: Reconcile, cell: B5, value: "the copy that validates"}
    verdicts:
      - {sheet: Reconcile, cell: B13, expect: "Reconciled in rows and rupees: send it to Anand."}
  - name: all four tabs fixed
    set:
      - {sheet: Profile, cell: E6, value: "=COUNT(B5:B14)"}
      - {sheet: Identity, cell: B16, value: "order_id"}
      - {sheet: Tail, cell: E9, value: "=SUM(A5:A12)"}
      - {sheet: Reconcile, cell: B13, value: "=IF(AND(B6=B7+B8,B9=B10),\"Reconciled in rows and rupees: send it to Anand.\",\"Rows reconcile and rupees miss the books by \"&TEXT(B10-B9,\"#,##0\")&\": keep the copy that validates.\")"}
    verdicts:
      - {sheet: Export, cell: B5, expect: "Ready to paste into the note to Anand."}
      - {sheet: Export, cell: B7, contains: "Identity: Set aside 3 rows"}
```
