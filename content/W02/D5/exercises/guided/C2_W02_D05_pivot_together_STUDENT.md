# What does the pivot say on each export, and which one ties to the warehouse?

Guided, built with the trainer across chapters 1 and 2, about twenty-five minutes in all, in your own
Excel. The trainer's screen and yours should show the same number at every step; say so when they do
not. Keep this sheet: the blanks you fill in are the evidence for the tree on page two.

> "Monday's growth review deck needs three things I can open on my laptop without a login: the
> revenue tree by segment for both quarters, ..."
>
> Meera's chief of staff, Kalpa Retail

Kalpa Retail sells to four segments: Retail-Core, its everyday shoppers; Retail-Plus, its paid
membership tier; Business, corporate buyers invoiced in large amounts; and Student. Revenue is booked
order value in rupees. Q1 runs from April to June 2026 and Q2 from July to September 2026, and the
warehouse, the database that holds one row per order and that every sheet ties back to, books
Rs 10,00,00,000 in Q1 and Rs 9,84,00,000 in Q2. The data team sent two exports: the customer table,
`data/C2_W02_D05_customer_table_STUDENT.csv`, and the raw export,
`data/C2_W02_D05_raw_export_STUDENT.csv`. The revenue tree splits revenue into customers, orders per
customer and revenue per order. A PivotTable adds a column's values for each group and re-slices when
another column is dragged in.

The PivotTable steps follow Microsoft's page, Create a PivotTable (verified 29 September 2026). The
other menu names, and Excel reading the export's ISO dates as dates, were not verified in Excel for
this build; labels move between versions, so look for what the screen asks for.

**Who needs the answer.** The chief of staff puts the tree on page two of Monday's deck, and Meera
decides from it which segment the growth plan funds. A tree built on the wrong rows puts a number in
front of the directors that Finance's books do not show.

**The questions on the way.**

- What does one row of the customer table stand for?
- Which segment carries the revenue in the pivot on the customer table?
- What do the leaves beside the pivot say, and do they multiply back?
- What does the same pivot say on the raw export, by quarter?
- How many rows and how many orders does the raw export hold, and what does that say about the pivot?
- What does the pivot say when each order counts once, and does it tie?

## Step 1. What does one row of the customer table stand for?

Open the customer table in Excel. Freeze the top row (View, Freeze Panes, Freeze Top Row) and turn on
the filter (Data, Filter). Before anything else, say the grain aloud: what one row stands for, how many
rows there are, and over which months each row's revenue is added up.

**What you should see.** 300 data rows and six columns, with `last_order_date` the only date.

## Step 2. Which segment carries the revenue in the pivot on the customer table?

Select any cell in the table, then Insert, PivotTable, New Worksheet. Drag `segment` to Rows,
`revenue` to Values (Sum), `customer_id` to Values (Count) and `orders` to Values (Sum).

**What you should see.** Business Rs 19,65,99,040 from 39 customers; Retail-Plus Rs 9,77,410 from
106; Retail-Core Rs 7,39,320 from 131; Student Rs 62,490 from 24.

## Step 3. What do the leaves beside the pivot say, and do they multiply back?

In the two columns to the right of the pivot, type `=orders/customers` and `=revenue/orders` as
cell formulas pointing at the pivot's own cells, and fill them down. Then multiply one segment's three
leaves back.

**What you should see.** Retail-Plus at 3.29 orders per customer and Rs 2,801 per order; Retail-Core
at 2.99 and Rs 1,886. Multiplied back, 106 times 3.29 times Rs 2,801 is about Rs 9.77 lakh, the
segment's revenue.

## Step 4. What does the same pivot say on the raw export, by quarter?

Open the raw export. Read its column names and say what you think one row stands for. Add a column
`quarter` with `=IF(MONTH(E2)<=6,"Q1","Q2")`, where column E holds `order_date`, and fill it down.
Insert a PivotTable with `segment` in Rows, `quarter` in Columns and `order_amount` in Values (Sum).

**Write down what you see.** The grand total: ______________. Q2's total: ______________.
Retail-Core, Q1 to Q2, up or down: ______________. Leave the pivot on screen and fix nothing yet.

## Step 5. How many rows and how many orders does the raw export hold, and what does that say about the pivot?

In an empty cell, count the rows: `=COUNTA(A2:A1451)`. Then add a helper column beside the order ids,
`=IF(COUNTIF($A$2:A2,A2)=1,1,0)`, fill it down, and add it up: the helper is 1 on the first row of
each order id and 0 on any repeat, so its sum counts the orders.

**Write down what you see.** Rows: ______________. Orders: ______________. Set the pivot's grand total
from step 4 beside the warehouse's two quarters, Rs 19,84,00,000, and write one sentence on why they
differ: ______________________________________________.

## Step 6. What does the pivot say when each order counts once, and does it tie?

Point the pivot's source at the range that includes the helper column, refresh it (right-click,
Refresh), drag the helper into Filters and keep only 1. Read the grand total and each quarter again.

**What you should see.** Rs 10,00,00,000 in Q1 and Rs 9,84,00,000 in Q2, the warehouse to the rupee.
Write Retail-Core's two quarters and its change: ______________.

**The line for the tree.** One sentence on what one row of the raw export stands for, and how the
tree on page two counts each order once.

---

The chapter 1 and chapter 2 sets, `unguided/C2_W02_D05_ch1_segment_tree_STUDENT.md` and
`unguided/C2_W02_D05_ch2_both_quarters_STUDENT.md`, follow this sheet.
