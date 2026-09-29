# Guided: the pivot, built together, then rebuilt on the raw export

Round 1, with the trainer, about twenty-five minutes. You mirror each step in your own Excel. The
trainer's screen and yours should show the same number at every step; say so when they do not.

The PivotTable steps follow Microsoft's page, Create a PivotTable (verified 29 September 2026). The
other menu names, and Excel reading the ISO dates in the export as dates, were not verified in Excel
for this build; labels move between versions, so look for what a screen asks for.

> "The revenue tree by segment for both quarters."
>
> Meera's chief of staff, Kalpa Retail

---

## Step 1. Open the customer table and say its grain

Open `data/C2_W02_D05_customer_table_STUDENT.csv` in Excel. Freeze the top row (View, Freeze Panes,
Freeze Top Row) and turn on the filter (Data, Filter).

Say the grain aloud before anything else: one row per customer, 300 rows, revenue summed across
April to September.

**What you should see.** 300 data rows and six columns, with `last_order_date` the only date.

## Step 2. The pivot by segment

Select any cell in the table, then Insert, PivotTable, New Worksheet. Drag `segment` to Rows,
`revenue` to Values (Sum), `customer_id` to Values (Count) and `orders` to Values (Sum).

**What you should see.** Business Rs 19,65,99,040 from 39 customers; Retail-Plus Rs 9,77,410 from
106; Retail-Core Rs 7,39,320 from 131; Student Rs 62,490 from 24.

## Step 3. The leaves beside the pivot

In the two columns to the right of the pivot, type `=orders/customers` and `=revenue/orders` as
cell formulas pointing at the pivot's cells, and fill them down.

**What you should see.** Retail-Plus at 3.29 orders per customer and Rs 2,801 per order; Retail-Core
at 2.99 and Rs 1,886. Multiply Retail-Plus back: 106 times 3.29 times 2,801 is about Rs 9.77 lakh.

## Step 4. The same pivot on the raw export

Open `data/C2_W02_D05_raw_export_STUDENT.csv`. Say its grain: one row per payment. Add a column
`quarter` with `=IF(MONTH(E2)<=6,"Q1","Q2")` and fill it down. Insert a PivotTable with `segment`
in Rows, `quarter` in Columns and `order_amount` in Values (Sum).

**What you should see.** A grand total of Rs 39,40,95,490, and Retail-Core rising from Q1 to Q2.
Leave it on screen. Do not fix anything yet.

## Step 5. Count, then tie

In an empty cell, count the rows: `=COUNTA(A2:A1451)`. Then count the distinct orders with a helper
column in the export, `=IF(COUNTIF($A$2:A2,A2)=1,1,0)`, filled down, and `=SUM(` over it `)`.

**What you should see.** 1,450 rows and 1,000 orders. The warehouse's two quarters are Rs
19,84,00,000. Say, in one sentence, why the pivot is wrong.

## Step 6. Rebuild on one row per order

Point the pivot's source at the range that includes the helper column, refresh it (right-click,
Refresh), drag the helper into Filters and keep only 1. Read the grand total again.

**What you should see.** Rs 10,00,00,000 in Q1 and Rs 9,84,00,000 in Q2, the warehouse to the rupee,
and Retail-Core falling from Rs 3,73,070 to Rs 3,66,250.

---

The unguided set for this round is `unguided/C2_W02_D05_round1_STUDENT.md`.
