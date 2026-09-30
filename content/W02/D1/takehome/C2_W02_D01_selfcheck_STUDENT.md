# Which numbers should Kalpa Retail East's Monday suite reach, and which check proves each?

The self-check for the Week 2 Monday take-home. Open it only once a part is done. Each line gives the
number your query should reach on the east book, loaded from
`content/W02/D1/data/C2_W02_D01_takehome_STUDENT.sql`, and the check that proves it without anyone
else's answer. Kalpa Retail East is invented for the take-home; Q1 is April to June 2026 and Q2 is
July to September 2026, and revenue is booked revenue, every order at its amount.

**Who needs the answer.** You do, before the analyst reruns your file: a number that matches here
and fails its own check is still wrong, and a number that passes its check and misses here means the
definition differs, so read the question again.

**The questions on the way.**
1. Did your book totals land, and do customers sit below orders?
2. Do your ratios multiply back, and which groups carry the flag?
3. Do both averages cover the same members?
4. Do the segments add back, and does the half-year fit inside the members?
5. Is your sample the same five on every run?
6. Does the second case's line read the consumers?

## 1. Did the book's totals land, and do customers sit below orders?

| Quarter | Orders | Booked revenue | Customers who bought |
|---|---|---|---|
| Q1 | 194 | Rs 1,09,51,150 | 95 |
| Q2 | 168 | Rs 1,12,32,610 | 85 |

Revenue rose 2.6 percent while customers who bought fell 10.5 percent and orders 13.4 percent. **The
check:** customers who bought are fewer than orders in each quarter, and fewer than the 126 members on
the customer table.

## 2. Do the ratios multiply back, and which groups carry the flag?

| Segment | Q1 orders, customers, orders per customer | Q2 orders, customers, orders per customer | Change |
|---|---|---|---|
| Business | 18, 9, 2.00 | 17, 8, 2.13 | +6.2% |
| Retail-Core | 80, 42, 1.90 | 79, 40, 1.98 | +3.7% |
| Retail-Plus | 80, 34, 2.35 | 53, 26, 2.04 | -13.4% |
| Student | 16, 10, 1.60 | 19, 11, 1.73 | +8.0% |

Each change is computed from the counts before rounding. Retail-Plus's frequency fell furthest.
**The check:** every ratio times its customers gives back its orders to within half an order, for
example 2.04 times 26 is 53.04 against 53 orders. The flagged segment-quarters, under 30 customers
who bought, are five: Business in both quarters (9 and 8), Student in both (10 and 11), and
Retail-Plus in Q2 (26).

## 3. Do both averages cover the same members?

38 Retail-Plus members bought in either quarter. Over those same 38, a member spent Rs 5,709 in Q1 and
Rs 3,897 in Q2, down 31.7 percent. **The check:** both averages count 38 members inside them, and the
change equals the change in Retail-Plus's revenue, Rs 2,16,940 to Rs 1,48,080, also down 31.7 percent,
since one fixed group of members divides both quarters.

## 4. Do the segments add back, and does the half-year fit inside the members?

The segments' customers add back to the book: 9 plus 42 plus 34 plus 10 is 95 in Q1, and 8 plus 40
plus 26 plus 11 is 85 in Q2.

| Segment | Half-year orders | Half-year rupees | Customers who bought | Members on the book |
|---|---|---|---|---|
| Business | 35 | Rs 2,14,73,000 | 10 | 12 |
| Retail-Core | 159 | Rs 3,08,800 | 52 | 60 |
| Retail-Plus | 133 | Rs 3,65,020 | 38 | 40 |
| Student | 35 | Rs 36,940 | 12 | 14 |

The book's half-year holds 112 customers. **The checks:** every segment's half-year customers fit
inside its members; the four add to 112, the fingerprint's distinct customers; and Retail-Plus reached
a second way is 34 plus 26 less the 22 who bought in both quarters, 38. On the design choice, adding
the quarter rows reads 8 rows and counting from the orders reads all 362; the choice turns on what
each assumes, and your note should say which measures can be added across quarters.

## 5. Is the sample the same five on every run?

Ordered on the order id, the five delivered Q2 web orders are KE-00198 (Rs 9,06,000), KE-00200
(Rs 1,610), KE-00202 (Rs 1,080), KE-00205 (Rs 1,010) and KE-00208 (Rs 1,380), Rs 9,11,080 in all; the
first is a Business order. Without the ORDER BY, a fresh load hands you a different five. East's
fingerprint: 362 order rows, Rs 2,21,83,760, 112 distinct customers, latest order 30 September 2026.
**The check:** run the ordered query twice, and reload the file and run it again; the five do not
move.

## 6. Does the second case's line read the consumers?

The channel totals move with a handful of Business orders: the store's booked revenue rose 61.1
percent and the web's fell 37.6 percent. Read apart from Business, every channel's consumer revenue
fell, and the app's fell furthest, 24.1 percent, against 18.8 for the store and 7.4 for the web. **The
check:** each channel's Business and consumer revenue add back to the channel's total in each
quarter. The line for Anand names the app and its 24.1 percent.
