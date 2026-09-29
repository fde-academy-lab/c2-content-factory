# Recalculation manifest: Friday's deck pack

INTERNAL. This drives `scripts/xlsx_recalc.py`, which recalculates the deck pack through LibreOffice
and then makes the changes a director or a hurried analyst makes in the room, to prove the sheet
answers each one.

As shipped, the tree and the front page reconcile to the warehouse and the release holds the protect
list, because the clean customer table is one member short. The flips reproduce the day's traps in
the workbook: a count per payment row, an approximate lookup on the missing member (C-0170, named
here and in the day sheet only), and the scope and list-size changes a director asks for.

The XLOOKUP cell (Protect!F8) is never asserted, because LibreOffice 24.2 returns #NAME? for it.

```yaml
workbook: C2_W02_D05_deck_pack_STUDENT.xlsx
verdicts:
  - {sheet: Tree, cell: C20, expect: "Send: Q2 revenue Rs 9.84 crore, down 1.6 percent on Q1; Retail-Plus orders per customer 2.36 to 1.84, customers 91 to 76."}
  - {sheet: Protect, cell: F9, expect: "C-0152: Rs 25,840 across both quarters, rank 1 of 50 on the Retail-Plus list."}
  - {sheet: Protect, cell: B76, expect: "The top 50 Retail-Plus members spent Rs 7.15 lakh across both quarters."}
  - {sheet: FrontPage, cell: B20, expect: "All segments, Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1, April to June 2026 (Rs 10.00 crore); 100.0 percent of company revenue in Q2."}
  - {sheet: Checks, cell: C6, contains: "Rs 21,740 and 6 orders short of the warehouse"}
  - {sheet: Checks, cell: C10, expect: "Send the tree and the front page. Hold the protect list until the customer table reconciles to the warehouse."}
flips:
  - name: the pivot counts every payment row
    set: [{sheet: Tree, cell: C4, value: "once per row"}]
    verdicts:
      - {sheet: Tree, cell: C18, contains: "Rs 19.57 crore over the warehouse: 1450 rows carry 1000 orders"}
      - {sheet: Tree, cell: C20, expect: "Do not send: the tree counts an order once per payment row. Count each order once."}
      - {sheet: FrontPage, cell: B18, expect: "The card does not reconcile: its two quarters sum to Rs 39.41 crore against the warehouse's Rs 19.84 crore."}
      - {sheet: FrontPage, cell: B20, contains: "Hold the card"}
      - {sheet: Checks, cell: B8, expect: "0"}
      - {sheet: Checks, cell: C10, contains: "Do not send anything"}
  - name: Finance restates the warehouse one lakh higher
    set: [{sheet: Tree, cell: C5, value: 198500000}]
    verdicts:
      - {sheet: Checks, cell: C6, contains: "Rs 1.22 lakh and 6 orders short of the warehouse"}
      - {sheet: FrontPage, cell: B18, expect: "The card does not reconcile: its two quarters sum to Rs 19.84 crore against the warehouse's Rs 19.85 crore."}
      - {sheet: Checks, cell: C10, contains: "Do not send anything"}
  - name: the chief of staff looks up the missing member with an approximate match
    set: [{sheet: Protect, cell: C6, value: "C-0170"}, {sheet: Protect, cell: C7, value: "approximate"}]
    verdicts:
      - {sheet: Protect, cell: F4, expect: "C-0169"}
      - {sheet: Protect, cell: F6, expect: "rank 50 of 50 on the Retail-Plus list"}
      - {sheet: Protect, cell: F9, expect: "Do not answer: the lookup returned C-0169's row for C-0170. Switch the match to exact."}
  - name: the same id with an exact match
    set: [{sheet: Protect, cell: C6, value: "C-0170"}]
    verdicts:
      - {sheet: Protect, cell: F9, expect: "C-0170 is not in the customer table: say so, and check the export before anyone answers."}
  - name: a director asks for the top forty
    set: [{sheet: Protect, cell: C5, value: 40}]
    verdicts:
      - {sheet: Protect, cell: B76, contains: "The top 40 Retail-Plus members spent"}
  - name: a director takes Business off the card
    set: [{sheet: FrontPage, cell: B4, value: "All except Business"}]
    verdicts:
      - {sheet: FrontPage, cell: B20, expect: "All except Business, Q2, July to September 2026: Rs 8.15 lakh, down 17.3 percent on Q1, April to June 2026 (Rs 9.86 lakh); 0.8 percent of company revenue in Q2."}
  - name: the card shows Retail-Plus alone
    set: [{sheet: FrontPage, cell: B4, value: "Retail-Plus"}]
    verdicts:
      - {sheet: FrontPage, cell: B20, expect: "Retail-Plus, Q2, July to September 2026: Rs 4.13 lakh, down 29.4 percent on Q1, April to June 2026 (Rs 5.86 lakh); 0.4 percent of company revenue in Q2."}
```
