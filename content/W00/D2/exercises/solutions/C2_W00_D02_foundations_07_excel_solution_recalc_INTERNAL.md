# Recalculation manifest: the Chapter 7 solution workbook

INTERNAL. This drives `scripts/xlsx_recalc.py`, which makes LibreOffice recompute the solution workbook
and then changes amounts on the Orders sheet, to prove the verdicts on the Checks sheet compute and move.

As shipped, every agreement check reads matches, the formula over rows 2 to 10 names its gap of Rs 950,
and the sentence for Meera is ready. The first flip changes the tenth order, K-110, from Rs 950 to
Rs 1,050: the Plus SUMIFS names a gap of Rs 100, the short range does not move because it never saw that
row, the typed pivot readings keep agreeing until the pivot is read again, and the hand trace differs on
that one row, so the sentence falls back to not ready. The second changes K-101, inside rows 2 to 10,
from Rs 1,200 to Rs 1,100, and the short range moves with it.

```yaml
workbook: C2_W00_D02_foundations_07_excel_solution_STUDENT.xlsx
verdicts:
  - {sheet: Checks, cell: D10, expect: "matches"}
  - {sheet: Checks, cell: D11, expect: "matches"}
  - {sheet: Checks, cell: D12, expect: "matches"}
  - {sheet: Checks, cell: D13, expect: "matches"}
  - {sheet: Checks, cell: D14, expect: "matches"}
  - {sheet: Checks, cell: D15, expect: "matches"}
  - {sheet: Checks, cell: D16, expect: "matches"}
  - {sheet: Checks, cell: D17, expect: "Rs 950 short of the notebook's Rs 3350"}
  - {sheet: Checks, cell: B19, contains: "Plus paid revenue is Rs 3350"}
flips:
  - name: the tenth order's amount changes, outside the short range
    set: [{sheet: Orders, cell: C11, value: 1050}]
    verdicts:
      - {sheet: Checks, cell: D12, expect: "Rs 100 above the notebook's Rs 3350"}
      - {sheet: Checks, cell: D10, expect: "Rs 100 above the notebook's Rs 5500"}
      - {sheet: Checks, cell: D13, expect: "matches"}
      - {sheet: Checks, cell: D17, expect: "Rs 950 short of the notebook's Rs 3350"}
      - {sheet: Checks, cell: D16, expect: "1 of 10 rows differ; the rows marked no below show where"}
      - {sheet: Checks, cell: B19, contains: "Not ready to say to Meera: 3 of the six"}
  - name: an amount inside rows 2 to 10 changes
    set: [{sheet: Orders, cell: C2, value: 1100}]
    verdicts:
      - {sheet: Checks, cell: D12, expect: "Rs 100 short of the notebook's Rs 3350"}
      - {sheet: Checks, cell: D17, expect: "Rs 1050 short of the notebook's Rs 3350"}
      - {sheet: Checks, cell: D16, expect: "1 of 10 rows differ; the rows marked no below show where"}
```
