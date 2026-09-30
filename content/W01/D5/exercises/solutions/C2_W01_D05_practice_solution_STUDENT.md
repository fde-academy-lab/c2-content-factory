# Solution: the practice lab

Answers: 1a 2c 3b 4d 5d 6c 7b 8c 9a 10a 11b 12d 13c 14b 15d 16a

Hands-on numbers from a correct rerun: 4 rows rejected, Q2 revenue Rs 23,39,340, Retail-Plus's
distinct orders in Q2 12.

## The idea being tested

The practice export carries the week's four defect families in places the lab did not use, so a
learner who reran the method rather than remembering the morning's answers gets every item. The
numbers a correct run reaches: 79 rows and 75 distinct orders; 4 rows rejected as repeats of orders
already kept; one amount stored with its currency, read as Rs 2,260 and flagged; one Q2 order with
no customer_id, kept in revenue and flagged; Q1 Rs 23,21,000 and Q2 Rs 23,39,340, both landing on the
control totals with 39 and 36 orders. The total held, up 0.8 percent. Inside it, Retail-Plus keeps
its 8 members and their basket (Rs 2,900 to Rs 2,850) while orders per member fall from 2.00 to 1.50,
down 25 percent, on 16 orders then 12. That is the biggest consumer move, and it rests on fewer than
thirty orders a quarter: the fair test, which flips each member's own two quarters, puts it at
exactly 32 of 256, p = 0.125. So the practice note leads with the reconciled total, says no segment
moved on enough orders to lead, and carries the Retail-Plus fall in its caveat as a count to watch.
Student moves from 2 orders to 3.

## Item by item

Items 3, 4, 6, 8, 10, 11, 12, 13 and 16 are design items, nine of sixteen: each asks which approach
fits and takes two ideas or several steps to answer, and six of them ask for a sizing you compute.
Item 15 is the find-the-defect item.

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | Rows less distinct ids is 14 repeats; customer_id present 1,238 of 1,240 leaves 2 orders with no customer; convertible 1,236 of 1,240 leaves 4 amounts to decide; Kalpa has four segments, so a fifth distinct name is a variant spelling to repair. | b misses the 2 blank customers and the fifth segment name. c reads the distinct counts as facts about the business, which is what a profile exists to question. d misreads each count: repeats sit in order_id, a distinct count of customers says nothing about a customer appearing twice, and present 1,240 means no segment is empty. |
| 2 | c | "4.5k" can be read without a guess when the supplier's other amounts are whole rupees, so it is read as 4,500, kept and flagged; "TBC" on a shipped order is a real order whose value only its owner can give, so it is held and asked about; "TEST" on the QA team's account marks a test transaction, which is dropped with a reason. | a sets a real, shipped order to zero, which hides it. b holds a value anyone can read. d keeps a test transaction in revenue at zero instead of dropping it. |
| 3 | b | n(n - 1)/2 at n = 5,00,000 is about 1.25 x 10^11, 125 billion comparisons, while counting each id in one pass takes 5 lakh steps and also lists the ids that repeat. The one-pass count fits both files. | a halves the rows instead of squaring them. c has the right count and the wrong call: 125 billion comparisons is hours of compute to learn what one pass says in a second. d gives both ways the same cost, which is true of neither. |
| 4 | d | The 6 orders are real revenue; only their customer is unknown, so they stay in revenue, flagged, and the note gives 400 known customers plus 6 orders with no known buyer, which is what an auditor can check and what Meera needs to read revenue per customer honestly. | a counts a placeholder as a person. b throws away real revenue to make the rows look complete. c invents a customer for each order. |
| 5 | d | Q1's count matches (410) while its rupees are Rs 1,80,000 short, so a value was lost; Q2 has 8 rows more than Finance's orders and Rs 2,40,000 more, so rows were posted twice; the pass sent Rs 29,40,000 over Rs 28,20,000, up 4.3 percent, where the books say down 10.0. | a has the moves right and quotes the books' headline, not the pass's. b puts each error in the wrong quarter. c swaps the two rupee amounts. |
| 6 | c | The counts pass, so no order is missing and the set-aside rows are all repeats; an empty conversion log with a rupee gap means a value was set aside silently. Every value present is either summed or logged, and the one in neither is the gap. | a sums rows that are not in Finance's total, so they cannot explain a shortfall against it. b tests chance, which a missing value is not. d compares typical orders, which one lost value barely moves. |
| 7 | b | With no outside total the rupee check cannot run for Q2, so the note calls Q2 unreconciled and names the checks that did run inside the file. | a claims more than checks inside the file can prove. c hides two checks that ran and passed. d reconciles Q2 to a number that is not about Q2. |
| 8 | c | The reply lands 90 minutes after the request. Asked first, it lands at 90, leaving 30 minutes to reconcile. | a asks at 30 and the reply lands at 120, with the read. b asks at 45 and it lands at 135, after the read. d asks at 20 and it lands at 110, 10 minutes before the read, which is under the 15 needed. |
| 9 | a | 16 distinct Q1 orders over 8 members is 2.00; 12 over 8 is 1.50; orders per member fell 25.0 percent, with members flat and the basket down 1.7 percent. | b: the tier kept all 8 members. c is the basket, which barely moved. d keeps the 4 repeated Q1 rows, 20 over 8 is 2.50, which gives the uncleaned -40.0. |
| 10 | a | The first question is about the same 8 members in two quarters, so each member's own two quarters are flipped; the second compares different customers, so the segment label is shuffled across whole customers. | b swaps the two tests. c pools each member's quarters and then splits customers' orders apart, the two hurried mistakes. d gets the first right and then splits each customer's orders between the groups. |
| 11 | b | Four members ordered once fewer and four ordered the same, so the real change is 4 orders. A flip moves the total only through the four who changed, and the change is 4 or more, either way, only when all four flip the same way: 2 of their 16 patterns, times 16 for the others, is 32 of 256, p = 0.125. | a counts one direction only, 16 of 256. c forgets that the four unchanged members flip too. d is half of all 256 patterns, a coin's even odds, which is the guess before any tally. |
| 12 | d | 0.125 is the exact share over every way to flip the 8 members, so only new orders move it: the same fall next quarter on the same members, tested on both quarters, is what would put it in the claim. | a and b resample a share that is already exact, so they cannot move it. c renames the number without adding evidence. |
| 13 | c | The total is reconciled and held; every segment rests on fewer than thirty orders a quarter (Retail-Plus 16 then 12, Retail-Core 18, Student 2 then 3, Business 3), and the biggest move tests at 0.125, so no segment leads and the note says so. | a leads with a rate on 28 orders that its own test cannot tell from chance. b leads with a rise on five orders. d reads the total and drops the Retail-Plus fall that the caveat must carry. |
| 14 | b | It restates the claim with its count, 16 orders then 12 from 8 members, and bounds it with what the test found, 1 time in 8, which is why it sits in the caveat for another quarter. | a folds. c overclaims the other way: a share above 0.05 means the fall is not shown, never that it did not happen. d dismisses a real move Meera may hear about from someone else. |
| 15 | d | Line 8 turns a value the code cannot read into zero, keeps its row and writes nothing to a log, so counts reconcile while rupees fall short. | a starts an accumulator correctly. b is Wednesday's identity rule and keeps one row per order. c is where the failure happens, which is right to catch; the defect is what the except does with it. |
| 16 | a | The square root of 0.048 x 0.952 / 2,000 is about 0.005, so a share of 0.048 sits within one wobble of 0.05, and 20,000 shuffles bring the wobble to about 0.0015 before the call is made. | b gets the arithmetic wrong by a factor of fifty. c confuses the wobble with the share itself. d has the right wobble and ignores it. |

## The part worth arguing about

The practice lead, and which test is fair for it. Retail-Plus's own 8 members ordered less often, so
the fair test keeps each member's own two quarters together and flips them: 32 of 256, p = 0.125,
counted exactly rather than sampled. A learner who asked a different question, whether Retail-Plus's
change differs from Retail-Core's, shuffles the segment label across whole customers, and there the
practice export's order with no customer_id decides the number: 0.047 with that order kept as a
customer of its own (0.046 to 0.058 on seeds 1 to 3), 0.011 with it left out of the file entirely,
and no customer to shuffle at all under item 4's handling. Neither number moves the lead past the
thirty-order rule, and the first sits so close to 0.05 that the analyst would run 20,000 shuffles
before calling it. The honest note says which question it tested, which handling it chose, and
leads with the reconciled total.

## Where the pattern lives in production

Every monthly close in a finance or analytics team runs this shape: the export arrives with control
totals from the source system, the analyst's pass must land on them before any analysis is trusted,
and the decisions log is what an auditor asks for when a number is questioned months later.
