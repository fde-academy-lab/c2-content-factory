# Solution: the practice lab

Answers: 1b 2c 3b 4a 5d 6b 7c 8d 9b 10a 11d

Hands-on numbers from a correct rerun: 4 rows rejected, Q2 revenue Rs 23,39,340, Retail-Plus
orders per customer in Q2 1.50.

## The idea being tested

The practice export carries the week's four defect families in places the lab did not use, so a
learner who reran the method rather than remembering the morning's answers gets every item. The
numbers a correct run reaches: 79 rows and 75 distinct orders; 4 rows rejected as repeats of orders
already kept; one amount stored with its currency, read as Rs 2,260 and flagged; one Q2 order with
no customer_id, kept in revenue and flagged; Q1 Rs 23,21,000 and Q2 Rs 23,39,340, both landing on the
control totals with 39 and 36 orders. The total is flat, up 0.8 percent. Inside it, Retail-Plus keeps
its 8 members and their basket (Rs 2,900 to Rs 2,850) while orders per member fall from 2.00 to 1.50,
down 25 percent. Student moves from 2 orders to 3.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | 79 rows carry 75 distinct order ids, so 4 rows repeat an order already kept. | a compares neighbours, which misses repeats that sit apart. c counts a quarter, not repeats. d confuses a bad value with a repeated order. |
| 2 | c | "Rs 2,260" can be read without guessing, so it is converted, kept and flagged with the text in the log. | a hides a real order and reports no rejects. b throws away revenue that can be recovered. d invents a value and leaves no trace. |
| 3 | b | The order is real revenue; only the customer is unknown, so the count is stated both ways (11 known customers in Retail-Core in Q2, 12 if the unknown is a new one). | a loses Rs 1,740 of real revenue. c counts a blank as a person. d invents a customer. |
| 4 | a | Counts prove every row is accounted for; only a rupee check proves the values survived. | b stops at the count. c undersells a check that is necessary. d claims more than a count can show. |
| 5 | d | Rs 23,21,000 less Rs 2,260 is Rs 23,18,740: the unconvertible amount was set to zero. | a would make Q1 larger, by Rs 11,150. b sits in Q2. c would move a whole corporate order. |
| 6 | b | Retail-Plus keeps 8 members and about the same basket; orders per member fall. | a: members are flat. c: revenue per order moves 1.7 percent. d reads the total, which hides the tier. |
| 7 | c | 16 distinct Q1 orders over 8 members is 2.00; 12 over 8 is 1.50; the change is -25.0 percent. | a keeps the 4 repeated Q1 rows, 20 over 8 is 2.50, which gives -40.0. b is the basket. d divides the wrong way round. |
| 8 | d | Two orders then three cannot carry a rate; the count goes in the caveat. | a and b act on a rumour. c hides a move Meera may hear about from someone else. |
| 9 | b | A customer's orders belong together, so the label is shuffled across customers. | a splits a customer's orders across groups. c tests a different question. d breaks the link between an order and its amount. |
| 10 | a | The claim names the branch, the segment, the rate with both ends and the denominator. | b reads the total and misses the tier. c is the uncleaned -40 percent. d leads with two and three orders. |
| 11 | d | It restates the claim with its count, bounds it, and offers the test that settles chance. | a folds. b overclaims what a p-value does. c changes the subject to the total. |

## The part worth arguing about

Item 3. Whether the empty customer_id is one of the 11 known Retail-Core customers or a twelfth is
not knowable from the file. The honest note says "11 known customers, plus one order whose customer
is missing", and lets the reader see both counts. A learner who writes 12 has the right number by
luck and the wrong reason.

## Where the pattern lives in production

Every monthly close in a finance or analytics team runs this shape: the export arrives with control
totals from the source system, the analyst's pass must land on them before any analysis is trusted,
and the decisions log is what an auditor asks for when a number is questioned months later.
