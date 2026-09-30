# What does a correct rerun of the practice lab reach?

Answers: 1a 2c 3b 4d 5d 6c 7b 8c 9a 10a 11b 12d 13c 14b 15d 16a

In the practice lab, each learner reruns the step of Friday's lab they stalled on, using the practice
export (`data/C2_W01_D05_practice_orders_STUDENT.csv`, with Finance's control totals in
`data/C2_W01_D05_practice_control_STUDENT.csv`), and answers sixteen lettered items. This solution
reads without the set beside it.

A correct rerun reaches the three hands-on numbers: Q1 revenue of Rs 23,21,000, Q2 revenue of Rs
23,39,340, and 12 distinct Retail-Plus orders in Q2.

## What does the clean practice export say?

A correct rerun keeps 39 orders worth Rs 23,21,000 in Q1 and 36 worth Rs 23,39,340 in Q2. Both
quarters land on Finance's control totals in orders and in rupees, and revenue held, up 0.8 percent.
On the revenue tree, Retail-Plus keeps its 8 members and its basket barely moves (Rs 2,900, then
Rs 2,850, down 1.7 percent), while orders per member fall from 2.00 to 1.50, down 25.0 percent, on 16
orders then 12. That is the largest consumer move in rupees, a fall of Rs 12,200 in the tier's revenue,
and like every segment it rests on fewer than thirty orders a quarter: Retail-Core carries 18 orders then 18,
Student 2 then 3 and Business 3 then 3. The fair test flips each Retail-Plus member's own two quarters
and counts all 256 patterns, and 32 of them give a change at least as large, either way, p = 0.125.
So the practice note leads with the reconciled total and says no segment moved on enough orders to
lead, which covers Student's move from 2 orders to 3 as well, and it carries the Retail-Plus fall in
its caveat as a count to watch.

## Why is each key right, and each other letter wrong?

Items 3, 4, 6, 8, 10, 11, 12, 13 and 16 are design items, nine of sixteen: each asks which approach
fits and takes two ideas or several steps to answer, and six of them ask for a sizing you compute.
Item 15 is the find-the-defect item.

| Item | The item asks | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | Which reading names every finding in last month's profile of 1,240 rows? | a | Rows less distinct ids is 17 repeats; customer_id present 1,238 of 1,240 leaves 2 orders with no customer; convertible 1,236 of 1,240 leaves 4 amounts to decide; Kalpa has four segments, so a fifth distinct name is a variant spelling to repair. | b misses the 2 blank customers and the fifth segment name. c reads the distinct counts as facts about the business, which is what a profile exists to question. d gets the repeats right and misreads the rest: the 2 short in customer_id are blanks, a distinct count of customers says nothing about a customer appearing twice, a zero would convert, so the 4 are values that will not read as numbers, and present 1,240 means no segment is empty. |
| 2 | Which decisions fit "4.5k", "TBC" and "TEST", in that order? | c | "4.5k" can be read without a guess when the supplier's other amounts are whole rupees, so it is read as 4,500, kept and flagged; "TBC" on a shipped order is a real order whose value only its owner can give, so it is held and asked about; "TEST" on the QA team's account shows a test transaction, which is dropped with a reason. | a sets a real, shipped order to zero, which hides it. b holds a value anyone can read. d keeps in revenue, at zero, a test transaction that should be dropped with a reason. |
| 3 | What does comparing every pair of rows cost at 5 lakh rows, and which way fits both last month's 1,240 rows and next month's 5 lakh? | b | n(n - 1)/2 at n = 5,00,000 is about 1.25 x 10^11, 125 billion comparisons, while counting each id in one pass takes 5 lakh steps and also lists the ids that repeat. The one-pass count fits both sizes. | a halves the rows, and the number of pairs grows with the square of the rows. c has the right count and the wrong call: 125 billion comparisons is hours of compute to learn what one pass says in a second. d gives both ways the same cost, which is true of neither. |
| 4 | How do 6 orders with the customer_id "UNKNOWN", among 1,000, enter the note? | d | The 6 orders are real revenue; only their customer is unknown, so they stay in revenue, flagged, and the note gives 400 known customers plus 6 orders with no known buyer, which is what an auditor can check and what Meera needs to read revenue per customer honestly. A later test that shuffles whole customers between groups moves each customer with all their orders, and these 6 belong to no known customer, so before it runs the analyst logs whether each counts as a customer of its own or stays out of that test. | a counts a placeholder as a person. b throws away real revenue to make the rows look complete. c invents a customer for each order. |
| 5 | Control Rs 30 and 27 lakh, a pass that summed Rs 28.2 and 29.4 lakh: what went wrong, and what did it send? | d | Q1's count matches (410) while its rupees are Rs 1,80,000 short, so a value was lost; Q2 has 8 rows more than Finance's orders and Rs 2,40,000 more, so rows were posted twice; the pass sent Rs 29,40,000 over Rs 28,20,000, up 4.3 percent, where the books say down 10.0. | a has the moves right and quotes the books' headline, where the item asks for the pass's. b puts each error in the wrong quarter. c swaps the two rupee amounts. |
| 6 | Counts pass, Q1 is Rs 14,600 short and the log has no conversion lines: which second route finds the gap from the file alone? | c | The counts pass, so no order is missing and the set-aside rows are all repeats; an empty conversion log beside a rupee gap means a value changed with no line to say so. Every value present is either summed as it came or logged, and the one in neither is the gap. | a sums rows that are not in Finance's total, so they cannot explain a shortfall against it. b tests chance, which a missing value is not. d compares typical orders, which one lost value barely moves. |
| 7 | Q2 came with no control totals and every check inside the file passes: what does the note say? | b | With no outside total the rupee check cannot run for Q2, so the note calls Q2 unreconciled and names the checks that did run inside the file. | a claims more than checks inside the file can prove. c hides checks that ran and passed. d reconciles Q2 to a number that is not about Q2. |
| 8 | Which order gets Finance's 90-minute reply in 15 minutes before a 120-minute read? | c | The reply lands 90 minutes after the request. Asked first, it lands at 90, leaving 30 minutes to reconcile. | a asks at 30 and the reply lands at 120, with the read. b asks at 45 and it lands at 135, after the read. d asks at 20 and it lands at 110, 10 minutes before the read, which is under the 15 needed. |
| 9 | On the clean practice data, which branch moved inside Retail-Plus, and by how much? | a | 16 distinct Q1 orders over 8 members is 2.00; 12 over 8 is 1.50; orders per member fell 25.0 percent, with members flat and the basket down 1.7 percent. | b fails because the tier kept all 8 members. c is the basket, which barely moved. d names the right branch at a size the clean data does not give, since 2.00 falling to 1.50 is 25.0 percent. |
| 10 | Which tests fit Meera's two Retail-Plus questions, in order? | a | The first question is about the tier's own members across two quarters, so each member's own two quarters are flipped; the second compares different customers, so the segment label is shuffled across whole customers, each carrying all their orders. | b swaps the two tests. c pools each member's quarters and then splits customers' orders apart, the two hurried mistakes. d gets the first right and then splits each customer's orders between the groups. |
| 11 | Of the 256 ways to flip Retail-Plus's 8 members, how many give a change at least as large as the real one, either way, and what is p? | b | Four members ordered once fewer and four ordered the same, so the real change is 4 orders. A flip moves the total only through the four who changed, and the change is 4 or more, either way, only when all four flip the same way: 2 of their 16 patterns, times 16 for the others, is 32 of 256, p = 0.125. | a counts one direction only, 16 of 256. c forgets that the four unchanged members flip too. d is half of all 256 patterns, a coin's even odds, which is the guess before any tally. |
| 12 | What would change the verdict that item 11's count gives on Retail-Plus? | d | 0.125 is the exact share over every way to flip the 8 members, and it sits above 0.05, so the verdict is that chance alone could have made the fall. Only new orders can move an exact share, and only new orders showing the same fall, tested again, could carry the move into the claim. | a and b resample a share that is already exact, so they cannot move it. c brings new orders that point the other way, which leave the verdict where it is, since a fall that reverses adds no evidence of a fall. |
| 13 | Which first line fits the practice note? | c | The total is reconciled and held, up 0.8 percent; every segment rests on fewer than thirty orders a quarter (Retail-Plus 16 then 12, Retail-Core 18 then 18, Student 2 then 3, Business 3 then 3), and the biggest move tests at 0.125, so no segment leads and the note says so. | a leads with Retail-Plus's fall, a move on 28 orders that its own test cannot tell from chance. b leads with a rise on five orders. d reads the total and drops the Retail-Plus fall that the caveat must carry. |
| 14 | A lead on 62 orders then 57 from 33 customers tests at 1 time in 100: which answer holds it when Marketing says it could be chance? | b | It restates the lead with its counts, well above the thirty-order rule, and answers "could be chance" with what the test found: chance alone makes a change that large 1 time in 100, either way. | a folds a tested lead on enough orders into the caveat. c reads the share as a 99 percent chance that the fall is real, where 1 in 100 says how often chance alone makes a change that large and says nothing about the chance the finding is true. d answers the person instead of the question. |
| 15 | Which line of the cleaning cell lets the pass look clean while it is short in rupees? | d | Line 8 turns a value the code cannot read into zero, keeps its row and writes nothing to a log, so counts reconcile while rupees fall short. | a starts an accumulator correctly. b is Wednesday's identity rule and keeps one row per order. c is where the failure happens, and catching it there is right; the defect is what the except clause then does with the value. |
| 16 | At p = 0.048 on 2,000 shuffles, what is the wobble, and what do you do before calling the lead real? | a | The square root of 0.048 x 0.952 / 2,000 is about 0.005, so a share of 0.048 sits within one wobble of 0.05, and 20,000 shuffles bring the wobble to about 0.0015 before the call is made. | b gets the arithmetic wrong by a factor of fifty. c confuses the wobble with the share itself. d has the right wobble and ignores it. |

## Which test is fair for the practice lead, and why does the choice matter?

Meera's first question is whether Retail-Plus's own 8 members changed from Q1 to Q2, so the fair test
keeps each member's two quarters together and flips them. Eight members give only 256 patterns, so
the share is counted exactly: 32 of 256, p = 0.125. Her second question, whether Retail-Plus's change
differs from Retail-Core's, compares different customers, so its fair test shuffles the segment label
across whole customers, each carrying all their orders, 2,000 times on `random.Random(7)`. There a
correct rerun lands between about 0.01 and 0.06, by the cleaning decisions its log records and the
seed, so the note names those decisions beside the number. No p in that range lifts the lead past the
thirty-order rule, since the tier rests on 16 orders then 12, and a p near 0.05 gets 20,000 shuffles
before anyone calls it, because at 2,000 its own wobble is about 0.005. The honest note says which
question it tested and which decisions stand behind the number, and it leads with the reconciled
total.

## Where at work does a pass have to land on control totals?

Every monthly close in a finance or analytics team runs this way: the export arrives with control
totals from the source system, the analyst's pass must land on them before any analysis is trusted,
and an auditor asks for the decisions log when a number is questioned months later.
