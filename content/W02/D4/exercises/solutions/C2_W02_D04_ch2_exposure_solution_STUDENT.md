# Which answers hold in the chapter 2 set on attaching the monsoon sale to the table, and why?

Answers: 1c 2b 3d 4a 5c

The marketing lead asks for November's budget on two numbers: how many customers the monsoon sale
reached, and what those customers spent. The campaign platform's feed lists the customers the sale
reached in August 2026, and the growth team's table holds one row for each of Kalpa's 340 customers.
A merge in pandas is a join with SQL's four shapes, and `validate` raises a `MergeError` when the
keys break the promise it states. Chapter 2 found 130 customers reached, who spent Rs 8,78,980 over
April to September 2026, with the table still 340 rows and Rs 19,84,00,000; the growth team's rule
keeps a customer the feed names twice once, on the first date. Two of the five items are design
items: 3 and 5.

**Who needs the answer.** You, checking your five letters after the lab or tonight. The merge that
attaches a feed decides how many rows the table has, and every spend summed over those rows goes
into a budget request.

**The questions on the way.**

- Which idea does the chapter 2 set test?
- Why does each of the five keys hold, from the Diwali slide to the second route?
- Why is option c in item 3, the chapter's own method, the wrong answer worth arguing about?
- Where does one event arriving twice come up at work?

## Which idea does the chapter 2 set test?

A merge copies a row once for every match, so the shape of the feed decides the shape of the table.
The set asks what a re-sent row does to a sum, how many rows each `how` returns on the day's
tables, which way of attaching a feed fits an ask, in which order the safe steps run, and which
route confirms the spend without sharing the merge.

## Why does each of the five keys hold, from the Diwali slide to the second route?

### Q1. What does the Diwali email's slide say the reached customers spent?

Five invented customers, and a feed that names C-8102 twice.

The key is c, "Rs 26,000". The left merge gives C-8102 two rows, both with a feed date, so the sum
over filled dates is Rs 4,000, Rs 6,500 twice and Rs 9,000. The customers the email reached spent
Rs 19,500, and the slide overstates them by C-8102's whole Rs 6,500.

- a, "Rs 19,500": what the reached customers truly spent, which is the number the slide should have
  said and does not.
- b, "Rs 25,000": all five customers' spend, as if the sum ignored the feed dates.
- d, "Rs 31,500": every row of the merged table, five customers and C-8102's second copy.

### Q2. How many rows does each of four merges of the table and the first-touch feed return?

340 customers on the left, 130 on the right, every one of the 130 on the list.

The key is b, "130, 340, 340 and 130". With `how` left out the merge is inner, so only the 130 found
on both sides survive. Left keeps all 340. Outer keeps every key from either side, and the 130 are
already among the 340, so it adds nothing. Right keeps the 130.

- a, "340, 340, 470 and 130": reads the default as left, and outer as the two sides stacked.
- c, "130, 340, 470 and 130": gets the default right and still stacks the sides for outer.
- d, "340, 340, 340 and 340": treats every merge as keeping the table whole.

### Q3. Which way should attach the app team's push feed, sized on what a repeat would cost?

A design item. 2,000 rows name 1,900 customers, and the stores team wants a count of reached
customers by city, today.

The key is d, "The `isin` flag: 12,000 rows, nothing counted twice, and no rule to choose". The ask
is yes or no per customer, and a flag is set once however often the feed repeats a customer, so the
table stays at 12,000 rows and no spend is counted twice.

- a, "A plain left merge: 12,100 rows, Rs 5.1 lakh counted twice in any spend sum": 100 repeated
  customers add 100 rows, and at Rs 5,100 each any sum of spend grows by Rs 5,10,000.
- b, "A merge counted before and after: 12,100 rows, the excess found afterwards": the count finds
  the 100 extra rows once the wrong table exists, and the ask never needed a merge.
- c, "The first-touch rule and a validated merge: 12,000 rows and a date rule unused": it is safe,
  and it costs a rule about dates for an ask that never reads a date. When the ask needs the date,
  as Monday's table does, this is the way.

### Q4. In which order does Monday's attach step run, so a repeat never reaches the table?

Four steps: merge with `validate`, keep each customer's first row, sort by date, check the table.

The key is a, "3, 2, 1, 4". The feed is sorted first, so that "first" means the earliest date; the
repeats are dropped next, so the merge's promise holds; the merge runs with the promise stated; the
check confirms 340 rows and Rs 19,84,00,000 after it.

- b, "2, 3, 1, 4": drops repeats before sorting, so "first" means whichever row the platform happened
  to send first.
- c, "1, 3, 2, 4": merges the raw feed first, and `validate="one_to_one"` stops the run on the first
  repeated customer.
- d, "3, 1, 2, 4": sorts, then merges before the repeats are dropped, and the run stops the same way.

### Q5. Which route reaches the reached customers' spend without sharing the merge's code?

A design item. Kavya wants Rs 8,78,980 confirmed by a route that would disagree if the rule or the
merge had gone wrong.

The key is c, "A SQL sum of the orders of customers `IN` the feed's warehouse table". `IN`
only asks whether a customer is in the feed, however often, so repeats cannot multiply anything, and
the query shares no code with the sort, the rule or the merge.

- a, "Sum `spend` over `merged[\"reached\"]` again, after rerunning the merge": the same code gives
  the same number, right or wrong.
- b, "A plain inner merge of the table and the raw feed, with spend summed": it shares nothing, and it
  multiplies any customer the feed sends twice, so it can agree only when the feed has no repeats.
- d, "Total spend less the unreached customers' spend, from the merged table": it re-derives the
  reached spend from the same merged table, so it moves whenever the merge moves.

## Why is option c in item 3, the chapter's own method, the wrong answer worth arguing about?

Chapter 2 chose the first-touch rule and a validated merge for Monday's table, so a learner who
remembers the call picks it again. The call rested on a fact: Monday's table needs the date the sale
reached each customer. The stores team's ask needs only yes or no, and the flag answers it with no
rule to defend. A method is chosen for an ask, and the ask decides when to switch.

## Where does one event arriving twice come up at work?

Meta's advertisers can send one purchase twice, once from the Meta Pixel in the shopper's browser
and once from their own server through the Conversions API, and Meta's documentation says they "must
set up a deduplication method". Under the method Meta recommends, when the same event ID and event
name reach the same Pixel within 48 hours, Meta keeps the first copy and discards the rest (Meta for
Developers, Handling Duplicate Pixel and Conversions API Events, checked 1 Oct 2026).
