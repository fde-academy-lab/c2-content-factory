# Solution: the case, the Monday suite

Answers: 1a 2c 3b 4d 5c 6a 7d 8b

The notebook's ten letters are `bdbccbadac`, in marker order 1 to 10, and the executed notebook is
`C2_W02_D01_hands_on_solution_STUDENT.ipynb` in this folder. The six queries, written for the
analyst, are `C2_W02_D01_monday_suite_solution_STUDENT.sql` in this folder, and every block runs
unchanged against the warehouse.

## The suite's results

| Query | What it returns |
|---|---|
| 1. The book | Q1: 538 orders, Rs 10,00,00,000. Q2: 462 orders, Rs 9,84,00,000, a change of 1.6 percent down |
| 2. Customers | Q1: 244 who bought. Q2: 227. The book holds 340 members |
| 3. The leaves | Eight rows; Retail-Plus 91 then 76 customers, 2.36 then 1.84 orders each, Rs 2,725 then Rs 2,953 an order |
| 4. The typical order | Retail-Plus median Rs 2,670 then Rs 3,095; Business median Rs 8,69,000 then Rs 8,32,000 |
| 5. Thin cells | One row: Student, Q1, 27 orders |
| 6. What moved | Retail-Plus: customers 16.5 percent down, frequency 22.0 down, order value 8.4 up, revenue 29.4 down |

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | 9,84,00,000 over 10,00,00,000 is 0.984, a change of 1.6 percent down. | b is the change in orders, 462 against 538. c confuses the fall with the Q2 index. d has the sign reversed. |
| 2 | c | Orders per customer in a quarter divides that quarter's orders by that quarter's buyers. | a counts members who bought nothing, which lowers the ratio for no reason. b uses a two-quarter denominator for one quarter. d is round 1's trap. |
| 3 | b | A ratio times its denominator gives its numerator: 1.84 times 76 is 139.8, which rounds back to 140. | a multiplies a rate by orders and compares it with rupees. c: rates over different denominators do not add. d: a frequency ratio is one branch of the revenue change, never the whole of it. |
| 4 | d | Segment and quarter together are unique in this result, so the order is fixed on every run. | a: `GROUP BY` promises no order. b and c sort on values that can tie, and a tie lets two rows swap. |
| 5 | c | The gap sits at the top of Business's Q2: one order far above the rest lifts the mean, and with it set aside the other 90 average Rs 8,63,633, within Rs 32,133 of the median of Rs 8,31,500 they leave. | a: both use the amount. b: half of Q2's Business orders sit at or below Rs 8,32,000, so the orders are not all near Rs 10 lakh; the mean sits there because of the top. d: the medians say nothing about the total. |
| 6 | a | The suite shows the cell and warns about it, so Anand sees Student and knows how far to trust its rate. | b hides a segment. c destroys the segment the sheet is about. d moves the goalposts until the warning disappears. |
| 7 | d | Identical steps give identical columns, so the final SELECT compares like with like and the analyst audits one step to trust both. | a: CTEs in one WITH can have any shapes. b: speed has nothing to do with it. c: a join needs a shared key, never shared names. |
| 8 | b | Rupees and orders are two questions with two answers. Business carries 99.1 percent of revenue, so its 1.4 percent dip is Rs 14,29,840 of the Rs 16,00,000 fall, against Rs 1,72,390 in Retail-Plus. Retail-Plus lost 75 of the book's 76 fewer orders, and its frequency fell furthest, 22.0 percent. | a quotes one segment's fall as if it were the book's, and prescribes acquisition when frequency fell furthest. c contradicts query 6, where Retail-Plus falls 29.4 percent and Student grows 33.9. d ignores a segment down 29.4 percent. |

## The sentence to Anand, as a model

Booked revenue fell 1.6 percent from Q1 to Q2, Rs 16,00,000, the same rate last week's file showed.
The rupees fell in Business, which carries 99.1 percent of revenue and lost Rs 14,29,840 on a 1.4
percent dip; Retail-Plus lost Rs 1,72,390. The orders fell in Retail-Plus: it lost 75 of the book's
76 fewer orders, its members ordered less often, 2.36 to 1.84 per quarter, and fewer bought at all,
91 to 76. This is booked revenue, Student's Q1 rate rests on 27 orders, and the warehouse counts
different customers from last week's file. Tomorrow we check collected revenue against it.

## The part worth arguing about

Item 2 against round 1's three counts. Some learners defend 340 because it is "all our customers".
It is the right denominator for a different question, how many members Kalpa holds. For orders per
customer the members who bought nothing would pull the ratio down without anyone having ordered
less, which is how a frequency problem gets misread as an acquisition problem.

## Where the pattern lives in production

A suite like this is what an analytics engineer calls a set of metric definitions: each number
lives in one query, versioned, with its definition in a comment, and every consumer reads that
query rather than a copy. Tools such as dbt formalise the same idea; the habit comes first.
