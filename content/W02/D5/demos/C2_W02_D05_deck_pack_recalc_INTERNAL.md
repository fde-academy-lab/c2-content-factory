# Recalculation manifest: Friday's deck pack

INTERNAL. This drives `scripts/xlsx_recalc.py`, which forces LibreOffice to recompute the workbook
and then flips the inputs to prove the verdicts move.

The three blue input cells are the whole decision surface: which quarter, which segment, and
whether the pivot is built on the clean table or the raw export. The verdicts below are what a
director should see change when they touch one.

The lookup verdicts read the INDEX and MATCH pair rather than the XLOOKUP beside it. XLOOKUP
arrived in LibreOffice 24.8 and the recalculation runs on 24.2, so it returns #NAME? here. That is
not a defect in the workbook; it is the portability point the sheet itself makes in cell B25, and
cell B24 reports which of the two a given reader managed to compute.

```yaml
workbook: C2_W02_D05_deck_pack_STUDENT.xlsx
verdicts:
  - {sheet: FrontPage, cell: B12, contains: "safe to send"}
  - {sheet: FrontPage, cell: B17, contains: "more than one row per customer"}
  - {sheet: FrontPage, cell: B22, expect: "not in the table"}
  - {sheet: FrontPage, cell: B23, contains: "says the id is missing"}
flips:
  - name: the pivot is built on the raw export instead
    set: [{sheet: FrontPage, cell: B6, value: "raw"}]
    verdicts:
      - {sheet: FrontPage, cell: B12, contains: "do not send"}
  - name: a member id that is actually in the table
    set: [{sheet: FrontPage, cell: B19, value: "C-0171"}]
    verdicts:
      - {sheet: FrontPage, cell: B23, contains: "all of them agree"}
```
