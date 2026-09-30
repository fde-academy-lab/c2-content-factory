# Which segment carried the fall from Q1 to Q2, and how often did its customers order?

Chapter 3 set, five items. Items 1 and 2 run live in chapter 3's last minutes if the chapter ran to
time; items 3 to 5 are the practice lab's stretch or tonight's work.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself."
>
> Anand Iyer, finance controller, Kalpa Retail

Kalpa Retail's booked revenue fell 1.6 percent from Q1 (April to June 2026) to Q2 (July to September
2026), from Rs 10,00,00,000 to Rs 9,84,00,000, and Anand Iyer, the finance controller, wants one line
per segment on the Monday sheet. Kalpa has four segments: Business, its corporate buyers, whose orders
are worth lakhs; Retail-Core, its everyday shoppers; Retail-Plus, its paid membership tier; and
Student. The segment is a column of the customers table, and each order looks it up with one line,
`JOIN customers c USING (customer_id)`, which finds the order's one customer and changes no row count.
Customers who bought are counted once per group, and orders per customer is a group's orders divided
by its customers who bought. WHERE keeps or drops single rows before the groups form; HAVING keeps or
drops whole groups after they form. Kavya Nair, the team's senior analyst, flags on the sheet any
rate that stands on fewer than 30 customers.

| Segment | Quarter | Orders | Customers who bought | Booked revenue |
|---|---|---|---|---|
| Business | Q1 | 97 | 36 | Rs 9,90,14,440 |
| Business | Q2 | 91 | 35 | Rs 9,75,84,600 |
| Retail-Core | Q1 | 199 | 102 | Rs 3,73,070 |
| Retail-Core | Q2 | 193 | 96 | Rs 3,66,250 |
| Retail-Plus | Q1 | 215 | 91 | Rs 5,85,770 |
| Retail-Plus | Q2 | 140 | 76 | Rs 4,13,380 |
| Student | Q1 | 27 | 15 | Rs 26,720 |
| Student | Q2 | 38 | 20 | Rs 35,770 |

**Who needs the answer.** The head of Retail-Plus reads the segment lines on Anand's sheet to decide
which members to work to keep. A wrong line on how often a segment's customers order sends the
retention budget to the wrong segment for a quarter.

**The questions on the way.**

- Which way produces every channel and status line each quarter, and how many rows does it return?
- Which segment-quarters come back when the flag's bar rises to 40 customers?
- What should the sheet show for Surat's orders per customer, and how does Surat compare with Pune?
- Which route confirms Retail-Core's 2.01 orders per customer in a way that could catch a wrong count?
- Which line tells Anand which segment carried the fall?

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

## How should one query answer every group at once?

Used at work whenever a stakeholder asks for the same measures cut by every value of a column.

### Q1. Which way produces every channel and status line each quarter, and how many rows does it return?

Anand's controller team wants orders, customers who bought and booked revenue for every channel and
every status in each quarter. Kalpa has three channels (app, web and store) and three statuses
(delivered, returned and cancelled), and every pairing has orders in both quarters. Which way fits,
and how many rows does it return?

a) One query per channel and status, nine queries returning 18 rows between them
b) One query grouped by channel, status and quarter, returning 18 rows
c) One query grouped by channel and status, returning 9 rows
d) The 1,000 order rows pulled into pandas and grouped there, returning 18 rows

### Q2. Which segment-quarters come back when the flag's bar rises to 40 customers?

For a board pack, Kavya raises the bar for a flagged rate from 30 customers to 40. The query keeps its
groups by segment and quarter and ends on `HAVING count(DISTINCT o.customer_id) < 40`. Which
segment-quarters come back to be flagged?

a) Student in both quarters, the two groups with fewer than 40 orders
b) Student in both quarters, the two groups with fewer than 30 customers
c) Business in both quarters, since its 99 percent of the rupees rests on few orders
d) Business and Student in both quarters, four groups

## How often did each group's customers order?

Used at work whenever a frequency goes on a sheet and a reader multiplies it back to the orders.

### Q3. What should the sheet show for Surat's orders per customer, and how does Surat compare with Pune?

Every number in this item is invented. A hurried sheet computed orders per customer for four cities
with `count(*) / count(DISTINCT customer_id)`.

| City | Orders | Customers who bought | orders_per_customer as printed |
|---|---|---|---|
| Pune | 45 | 20 | 2 |
| Surat | 38 | 21 | 1 |
| Indore | 30 | 16 | 1 |
| Kochi | 52 | 25 | 2 |

Anand's analyst multiplies every ratio back to its orders before reading it. What should the sheet
show for Surat, and what does the corrected column say about Surat against Pune?

a) 1.81, so Pune's 2.25 is about 24 percent higher, where the sheet said double
b) 1, as printed, so Surat's customers order half as often as Pune's customers do
c) 2, rounded up from 1.81, so Surat and Pune order equally often
d) 0.55, customers per order, which states the same fact the other way round

### Q4. Which route confirms Retail-Core's 2.01 orders per customer in a way that could catch a wrong count?

The corrected sheet says Retail-Core's customers ordered 2.01 times each in Q2: 193 orders from 96
customers. Kavya wants the 2.01 confirmed by a route that could catch a wrong count behind it. Which
route does that, and how many rows does it move?

a) Multiply 2.01 by the 96 customers and set the product beside the 193 orders, moving no rows
b) Rerun the grouped query with the division rounded to three places instead of two, one row
c) One row per Retail-Core customer in Q2 with their order count, 96 rows averaged in Python
d) Divide Retail-Core's Q2 revenue by its revenue per order, one row

## Which segment carried the fall?

Used at work whenever one line has to say where a company-wide change came from.

### Q5. Which line tells Anand which segment carried the fall?

Anand's sheet has room for one line on which segment carried the fall of Rs 16,00,000 from Q1 to Q2.
Which line holds on the table at the top of this set?

a) Retail-Plus carried the fall, since its revenue fell 29.4 percent, the most of any segment
b) Business carried most of the rupees of the fall, and Retail-Plus 75 of the 76 fewer orders
c) Student offset the fall, since its revenue rose 33.9 percent while the book's revenue fell 1.6 percent
d) No segment carried it, since the book's revenue fell only 1.6 percent overall
