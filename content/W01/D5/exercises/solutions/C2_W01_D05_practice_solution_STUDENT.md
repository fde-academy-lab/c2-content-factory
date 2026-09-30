# Solution: the practice lab

Answers: 1b 2c 3b 4d 5a 6d 7a 8b 9c 10c 11b 12c 13a 14d 15a 16d

Hands-on numbers from a correct rerun: 4 rows rejected, Q2 revenue Rs 23,39,340, Retail-Plus's
distinct orders in Q2 12.

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

Items 4, 7, 10, 11, 12, 15 and 16 are design items, seven of sixteen. Item 16 is also the set's ordering item.

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Rows less distinct order ids counts every repeat wherever it sits; here 79 rows carry 75 distinct ids, so 4 rows repeat an order already kept. | a compares neighbours, which misses repeats that sit apart. c counts a quarter twice, which is no test of repeats. d confuses a bad value with a repeated order. |
| 2 | c | "Rs 2,260" can be read without guessing, so it is converted, kept and flagged with the text in the log. | a hides a real order and reports no rejects. b throws away revenue that can be recovered. d invents a value and leaves no trace. |
| 3 | b | The order is real revenue; only the customer is unknown, so it is kept, flagged and the customer count is stated both ways (in this file, 11 known customers in Retail-Core in Q2, 12 if the unknown is a new one). | a loses real revenue (Rs 1,740 here). c counts a blank as a person. d invents a customer. |
| 4 | d | Distinct ids against rows is one cell and costs the same at 79 rows or 5 lakh; it found the 4 repeats here. This is a design item: the approach that scales. | a works at 79 rows and fails at 5 lakh. b grows with the square of the rows: about 3,000 pairs here and over 10^11 at 5 lakh. c hands your check to someone else and leaves no trace of it in your log. |
| 5 | a | Counts prove every row is accounted for (here 75 orders, 39 and 36); only a rupee check proves the values survived. | b stops at the count. c undersells a check that is necessary. d claims more than a count can show. |
| 6 | d | A value set to zero keeps its row, so the count lands, the rupees fall short and nothing is rejected; here Rs 23,21,000 less the Rs 2,260 amount read as zero is Rs 23,18,740. | a would make the quarter larger and the count too high. b would make the count short and show in the log. c would move the count as well. |
| 7 | a | With no outside total, the value accounting (present equals convertible plus logged) still runs, and the note says the quarter is unreconciled. Design item: the check you still have. | b gives up a check that needs nothing outside the file. c compares a typical order, which cannot show a lost or doubled one. d reconciles Q2 to a number that is not about Q2. |
| 8 | b | Retail-Plus keeps 8 members and about the same basket; orders per member fall. | a: members are flat. c: revenue per order moves 1.7 percent. d reads the total, which hides the tier. |
| 9 | c | 16 distinct Q1 orders over 8 members is 2.00; 12 over 8 is 1.50; the change is -25.0 percent. | a keeps the 4 repeated Q1 rows, 20 over 8 is 2.50, which gives -40.0. b is the basket. d divides the wrong way round. |
| 10 | c | Two orders then three cannot carry a rate, and no test on five orders can say more than the count; the count goes in the caveat, with the size at which it comes back to Meera. Design item: the approach, and the fact that switches it. | a acts on a rumour. b spends fifteen minutes on a test that cannot settle five orders. d hides a move Meera may hear about from someone else. |
| 11 | b | A customer's orders belong together, so the label is shuffled across customers. | a splits a customer's orders across groups. c tests a different question. d breaks the link between an order and its amount. |
| 12 | c | The one gap the tree says matters, on enough customers to test, shuffled at the customer. Design item: where to spend the one test. | a is two orders then three, which no test can read. b is not a finding. d runs four tests at 0.05, which gives about a one-in-five chance that one looks real by luck. |
| 13 | a | The claim names the branch, the segment, the rate with both ends and the denominator: here Retail-Plus orders per member 2.00 to 1.50, down 25 percent, members flat. | b reads the total and misses the tier. c is the uncleaned -40 percent. d leads with two and three orders. |
| 14 | d | It restates the claim with its count (8 members here, all still ordering), bounds it, and offers the test that settles chance. | a folds. b overclaims what a p-value does. c changes the subject to the total. |
| 15 | a | The claim rests on the gap being larger than chance produces, so a rerun that puts it inside the chance spread moves it to the caveat. Design item: the fact that would switch the call. | b is about the total, which never carried the claim. c is about a different segment. d is disagreement, which the evidence answers rather than obeys. |
| 16 | d | The profile first, then the check that needs nothing outside the file, then the request for a control total, which runs while the decomposition does. Design item: the order under a clock with no reference. | a reads the tree before anyone knows the file is sound. b quotes a number before the profile. c spends the two hours waiting. |

## The part worth arguing about

Item 3. Whether the empty customer_id is one of the 11 known Retail-Core customers or a twelfth is
not knowable from the file. The honest note says "11 known customers, plus one order whose customer
is missing", and lets the reader see both counts. A learner who writes 12 may have the right number,
and still has no reason for it.

The same decision moves the test behind the note's lead. Shuffling the segment label across customers,
2,000 times on `random.Random(7)`, Retail-Plus's fall in orders per member against Retail-Core's comes
out at p = 0.047 with the unknown order kept as a customer of its own (0.046 to 0.058 on seeds 1 to
3), and at p = 0.011 with it left out of the customer count. The first sits on the edge of 0.05, so
the honest note leads with the fall, says the test is borderline, and names the unknown order in the
caveat as the decision the verdict turns on. That is item 15's fact in practice: a rerun that puts the
gap inside chance moves the claim to the caveat.

## Where the pattern lives in production

Every monthly close in a finance or analytics team runs this shape: the export arrives with control
totals from the source system, the analyst's pass must land on them before any analysis is trusted,
and the decisions log is what an auditor asks for when a number is questioned months later.
