# Recalculation manifest: the Chapter 7 guided workbook

INTERNAL. This drives `scripts/xlsx_recalc.py`, which makes LibreOffice recompute the guided workbook
and then enters what a learner enters, to prove the verdicts on the Checks sheet compute and move.

As shipped, the two worked examples on the SUMIFS sheet already agree with the notebook's totals typed on
the Checks sheet, every verdict that waits on the learner says what to fill first, and the sentence for
Meera reads not ready. The first flip changes one Basic amount, K-102 from Rs 950 to Rs 1,050, and the
Basic and all-tier verdicts name a gap of Rs 100. The next two enter the learner's Plus SUMIFS and the
formula over rows 2 to 10, which misses the tenth order, K-110, and falls Rs 950 short. The last writes
the Plus SUMIFS and then changes K-110 from Rs 950 to Rs 1,050.

```yaml
workbook: C2_W00_D02_foundations_07_excel_guided_STUDENT.xlsx
verdicts:
  - {sheet: Checks, cell: D10, expect: "matches"}
  - {sheet: Checks, cell: D11, expect: "matches"}
  - {sheet: Checks, cell: D12, expect: "write the Plus SUMIFS in B7 on the SUMIFS sheet first"}
  - {sheet: Checks, cell: D13, expect: "type the pivot's Plus total on the Pivot sheet first"}
  - {sheet: Checks, cell: D16, expect: "fill the trace on the SUMIFS sheet first"}
  - {sheet: Checks, cell: D17, expect: "type the formula from the break-it block on the SUMIFS sheet first"}
  - {sheet: Checks, cell: B19, contains: "Not ready to say to Meera: 4 of the six"}
flips:
  - name: one Basic amount changes
    set: [{sheet: Orders, cell: C3, value: 1050}]
    verdicts:
      - {sheet: Checks, cell: D11, expect: "Rs 100 above the notebook's Rs 2150"}
      - {sheet: Checks, cell: D10, expect: "Rs 100 above the notebook's Rs 5500"}
  - name: the learner writes the Plus SUMIFS over whole columns
    set: [{sheet: SUMIFS, cell: B7, value: '=SUMIFS(Orders!C:C,Orders!B:B,"Plus",Orders!D:D,"paid")'}]
    verdicts:
      - {sheet: Checks, cell: D12, expect: "matches"}
      - {sheet: Checks, cell: B19, contains: "Not ready to say to Meera: 3 of the six"}
  - name: the learner types the range that stops one row short
    set: [{sheet: SUMIFS, cell: B27, value: '=SUMIFS(Orders!C2:C10,Orders!B2:B10,"Plus",Orders!D2:D10,"paid")'}]
    verdicts:
      - {sheet: Checks, cell: D17, expect: "Rs 950 short of the notebook's Rs 3350"}
  - name: the Plus SUMIFS written, then one Plus amount changes
    set:
      - {sheet: SUMIFS, cell: B7, value: '=SUMIFS(Orders!C:C,Orders!B:B,"Plus",Orders!D:D,"paid")'}
      - {sheet: Orders, cell: C11, value: 1050}
    verdicts:
      - {sheet: Checks, cell: D12, expect: "Rs 100 above the notebook's Rs 3350"}
```
