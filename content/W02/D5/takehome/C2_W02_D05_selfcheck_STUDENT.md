# Does your rebuilt workbook reach the numbers a careful pass on the fresh export reaches?

Check each line against your workbook before Monday. If a number differs, the difference is the
lesson: find which step produced it before you look anything else up.

The fresh exports are `data/C2_W02_D05_takehome_customer_table_STUDENT.csv`, one row per customer who
ordered between April and September 2026, and `data/C2_W02_D05_takehome_raw_export_STUDENT.csv`, one
row per payment with the order's amount on every row of that order. The warehouse books
Rs 10,00,00,000 in Q1 (April to June 2026) and Rs 9,84,00,000 in Q2 (July to September 2026).
Retail-Plus is Kalpa Retail's paid membership tier.

**Who needs the answer.** You, before you post. Each table below is one deliverable, and a line that
does not match is a number the chief of staff would have carried into Monday's growth review.

**The questions on the way.**

- What grain does the fresh raw export carry, and does your tree tie?
- What does your tree say for Retail-Plus and Retail-Core?
- What does the fresh customer table hold, and what does your protect list say?
- What do your lookup and your card show?
- Which behaviours should your workbook show when an input changes?

## What grain does the fresh raw export carry, and does your tree tie?

| Check | You should reach |
|---|---|
| Rows in the fresh raw export, and distinct order ids | 1,450 rows and 1,000 orders |
| A Sum of order_amount over every row | Rs 39,40,62,440, which is the number your tree must not show |
| Rows after Remove Duplicates on every column | 1,400, with the total still about Rs 39.40 crore |
| Your tree's totals, each order counted once | Q1 Rs 10,00,00,000 and Q2 Rs 9,84,00,000, tied to the warehouse to the rupee |

## What does your tree say for Retail-Plus and Retail-Core?

| Check | You should reach |
|---|---|
| Retail-Plus, Q1 | 94 customers, 2.29 orders per customer, Rs 6,14,080 |
| Retail-Plus, Q2 | 85 customers, 1.65 orders per customer, Rs 4,29,740, down 30.0 percent |
| Retail-Core, Q1 to Q2 | Rs 3,69,630 to Rs 3,75,750, up 1.7 percent, where Friday's files had it falling |

## What does the fresh customer table hold, and what does your protect list say?

| Check | You should reach |
|---|---|
| The fresh customer table's totals | 311 customers, 994 orders, Rs 19,83,85,260; compare them with the warehouse yourself, and let your Checks tab say what that means |
| Retail-Plus members in the table | 109 |
| The protect list | Rank 1 is C-0189 at Rs 32,090; the cut-off at rank 50 is Rs 8,350; the fifty together spent Rs 7,44,920 |
| The fifty-first member | Rs 8,180, so no tie sits across the boundary |
| The list filtered to Mumbai, with SUBTOTAL(109) at the foot | 7 members, Rs 1,17,530 |

## What do your lookup and your card show?

| Check | You should see |
|---|---|
| An id that is in the table, exact match | Its revenue and its place on the list |
| An id that is not in the table, exact match | "not in the table" |
| The same missing id, approximate match | A neighbour's row, with no warning, which is why the sheet uses the exact match |
| The card, all segments | Q2, July to September 2026: Rs 9.84 crore, down 1.6 percent on Q1 (Rs 10.00 crore) |
| The card, all except Business | Rs 8.41 lakh, down 16.5 percent on Rs 10.07 lakh; 0.9 percent of company revenue in Q2 |

## Which behaviours should your workbook show when an input changes?

- Changing the list size to 40 changes the list, its foot and nothing else.
- Changing the card's scope changes the number, the comparison, the share and the scope printed in the
  sentence, together.
- Counting each payment row instead of each order makes your Checks tab hold the tree and the card.
