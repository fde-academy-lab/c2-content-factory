# Recalculation manifest: Friday's deck pack

INTERNAL. This drives `scripts/xlsx_recalc.py`, which recalculates the deck pack through LibreOffice
and then makes the changes a director or a hurried analyst makes in the room, to prove the sheet
answers each one. The build script `C2_W02_D05_build_deck_pack_TRAINER.py` writes this file together
with the workbook.

As shipped, the tree and the front page tie to the warehouse and the release holds the protect list,
because the customer table is one member short: C-0170, a Retail-Plus member with 6 orders and
Rs 21,740, rank 5 if present, named here and in the day sheet only. The Checks tab says the table does
not match and prints neither the gap nor the id, which the room computes in chapter 3. The flips reproduce the day's
traps in the workbook: a count per payment row, a restated control total, an approximate lookup on a
missing id (C-0195, and the plant itself, which hands back C-0169 at rank 50), a SUM at the foot, a
figure typed over a formula, and the scope and voucher changes a director asks for.

The XLOOKUP cell (Protect!F8) is never asserted, because LibreOffice 24.2 returns #NAME? for it.

```yaml
workbook: C2_W02_D05_deck_pack_STUDENT.xlsx
verdicts:
  - {sheet: Tree, cell: C20, expect: "Send: Q2 revenue Rs 9.84 crore, down 1.6 percent on Q1; Retail-Plus orders per customer 2.36 to 1.84, customers 91 to 76."}
  - {sheet: Tree, cell: C18, expect: "The tree ties to the warehouse to the rupee and to the order in both quarters, and every row's leaves multiply back to its revenue."}
  - {sheet: Protect, cell: F10, expect: "C-0152: Rs 25,840 across both quarters, rank 1 of 50 on the Retail-Plus protect list."}
  - {sheet: Protect, cell: F9, expect: "COUNTIF finds 1 row holding C-0152 and SUMIFS adds Rs 25,840."}
  - {sheet: Protect, cell: B69, expect: "The 50 Retail-Plus members on the list spent Rs 7.15 lakh across both quarters, and a Rs 500 voucher for each costs Rs 25,000."}
  - {sheet: Protect, cell: E64, expect: "714890"}
  - {sheet: FrontPage, cell: B21, expect: "All segments, Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore); 100.0 percent of company revenue in Q2."}
  - {sheet: FrontPage, cell: B18, expect: "In rupees the largest fall is Business's Rs 14.30 lakh, out of a net fall of Rs 16.00 lakh, and the steepest fall is Retail-Plus, down 29.4 percent."}
  - {sheet: Checks, cell: B5, expect: "PASS"}
  - {sheet: Checks, cell: B6, expect: "HOLD"}
  - {sheet: Checks, cell: C6, expect: "The customer table's orders and revenue do not match the warehouse's two quarters, so the protect list waits until the table reconciles."}
  - {sheet: Checks, cell: B7, expect: "PASS"}
  - {sheet: Checks, cell: C7, expect: "The lookup says C-0195, an id the table does not hold, is not in the table."}
  - {sheet: Checks, cell: B8, expect: "PASS"}
  - {sheet: Checks, cell: B9, expect: "PASS"}
  - {sheet: Checks, cell: C11, expect: "Send the tree and the front page. Hold the protect list until the customer table reconciles to the warehouse."}
flips:
  - name: the pivot counts every payment row
    set: [{sheet: Tree, cell: C4, value: "once per row"}]
    verdicts:
      - {sheet: Tree, cell: C18, contains: "Rs 19.57 crore over the warehouse in the two quarters and counts 1,450 orders against the warehouse's 1,000: the export's 1,450 rows carry 1,000 orders"}
      - {sheet: Tree, cell: C20, expect: "Do not send: the tree counts an order once per payment row. Count each order once."}
      - {sheet: FrontPage, cell: B19, expect: "The card does not tie: its quarters read Rs 19.94 crore and Rs 19.47 crore against the warehouse's Rs 10.00 crore and Rs 9.84 crore."}
      - {sheet: FrontPage, cell: B21, expect: "Hold the card: it is built on a count that does not tie to the warehouse."}
      - {sheet: Checks, cell: B5, expect: "HOLD"}
      - {sheet: Checks, cell: C11, expect: "Do not send the tree or the front page: the tree does not tie to the warehouse, and the card inherits it. Hold the protect list too, until the customer table reconciles to the warehouse."}
  - name: Finance restates Q2 one lakh higher
    set: [{sheet: Tree, cell: D6, value: 98500000}]
    verdicts:
      - {sheet: Tree, cell: C20, expect: "Do not send: the tree does not tie to the warehouse's control totals. Find what differs before anyone slices it."}
      - {sheet: Checks, cell: B5, expect: "HOLD"}
  - name: the chief of staff looks up C-0195 with an approximate match
    set: [{sheet: Protect, cell: C4, value: "C-0195"}, {sheet: Protect, cell: C5, value: "approximate"}]
    verdicts:
      - {sheet: Protect, cell: F4, expect: "C-0194"}
      - {sheet: Protect, cell: F6, expect: "rank 15 of 50 on the Retail-Plus protect list"}
      - {sheet: Protect, cell: F10, expect: "Do not answer: the lookup returned C-0194's row for C-0195. Switch the match to exact."}
      - {sheet: Protect, cell: F9, expect: "COUNTIF finds 0 rows holding C-0195."}
      - {sheet: Checks, cell: B7, expect: "HOLD"}
      - {sheet: Checks, cell: C11, expect: "Send the tree and the front page. Hold the protect list until the customer table reconciles to the warehouse and the lookup matches exactly."}
  - name: the same id with an exact match
    set: [{sheet: Protect, cell: C4, value: "C-0195"}]
    verdicts:
      - {sheet: Protect, cell: F10, expect: "C-0195 is not in the customer table: say so, and check the export before anyone answers."}
  - name: the missing member itself, looked up approximately
    set: [{sheet: Protect, cell: C4, value: "C-0170"}, {sheet: Protect, cell: C5, value: "approximate"}]
    verdicts:
      - {sheet: Protect, cell: F4, expect: "C-0169"}
      - {sheet: Protect, cell: F6, expect: "rank 50 of 50 on the Retail-Plus protect list"}
      - {sheet: Protect, cell: F10, expect: "Do not answer: the lookup returned C-0169's row for C-0170. Switch the match to exact."}
  - name: a SUM at the foot of the list
    set: [{sheet: Protect, cell: E64, value: "=SUM(E13:E62)"}]
    verdicts:
      - {sheet: Checks, cell: B8, expect: "HOLD"}
      - {sheet: Checks, cell: C11, expect: "Send the tree and the front page. Hold the protect list until the customer table reconciles to the warehouse and the foot follows the filter."}
  - name: a director pastes Retail-Plus's Q2 back as a typed number
    set: [{sheet: Tree, cell: K11, value: 413380}]
    verdicts:
      - {sheet: Checks, cell: B5, expect: "PASS"}
      - {sheet: Checks, cell: B9, expect: "HOLD"}
      - {sheet: Checks, cell: C9, expect: "1 computed cell holds a typed figure: trace each one and restore its formula."}
      - {sheet: Checks, cell: C11, expect: "Hold the whole workbook until the typed figure is traced and its formula restored."}
  - name: a director types five lakh over Retail-Plus's Q2
    set: [{sheet: Tree, cell: K11, value: 500000}]
    verdicts:
      - {sheet: Checks, cell: B5, expect: "HOLD"}
      - {sheet: Checks, cell: B9, expect: "HOLD"}
  - name: a director takes Business off the card
    set: [{sheet: FrontPage, cell: B4, value: "All except Business"}]
    verdicts:
      - {sheet: FrontPage, cell: B21, expect: "All except Business, Q2, July to September 2026: Rs 8.15 lakh, down 17.3 percent on Q1, April to June 2026 (Rs 9.86 lakh); 0.8 percent of company revenue in Q2."}
      - {sheet: FrontPage, cell: B18, expect: "In rupees the largest fall is Retail-Plus's Rs 1.72 lakh, more than the net fall of Rs 1.70 lakh because Student rose, and the steepest fall is Retail-Plus, down 29.4 percent."}
  - name: the card shows Retail-Plus alone
    set: [{sheet: FrontPage, cell: B4, value: "Retail-Plus"}]
    verdicts:
      - {sheet: FrontPage, cell: B21, expect: "Retail-Plus, Q2, July to September 2026: Rs 4.13 lakh, down 29.4 percent on Q1, April to June 2026 (Rs 5.86 lakh); 0.4 percent of company revenue in Q2."}
      - {sheet: FrontPage, cell: B18, expect: "Customers who ordered went from 91 to 76, orders each from 2.36 to 1.84, and the basket from Rs 2,725 to Rs 2,953."}
  - name: a director tries a Rs 750 voucher
    set: [{sheet: Protect, cell: C6, value: 750}]
    verdicts:
      - {sheet: Protect, cell: B69, expect: "The 50 Retail-Plus members on the list spent Rs 7.15 lakh across both quarters, and a Rs 750 voucher for each costs Rs 37,500."}
  - name: the lookup check is given an id that is present
    set: [{sheet: Checks, cell: B13, value: "C-0152"}]
    verdicts:
      - {sheet: Checks, cell: B7, expect: "HOLD"}
      - {sheet: Checks, cell: C7, expect: "The test id C-0152 is in the table, so the check proves nothing: pick an id you know is missing."}
```
