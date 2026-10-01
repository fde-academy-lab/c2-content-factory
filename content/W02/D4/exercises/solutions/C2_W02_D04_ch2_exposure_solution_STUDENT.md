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
- Why does each of the five keys hold, from the Diwali slide to the feed with two campaigns?
- Why is option c in item 3, the chapter's own method, the wrong answer worth arguing about?
- Where does one event arriving twice come up at work?

## Which idea does the chapter 2 set test?

A merge copies a row once for every match, so the shape of the feed decides the shape of the table.
The set asks what a re-sent row does to a sum, how many rows each `how` returns on the day's
tables, which way of attaching a feed fits an ask, in which order the safe steps run, and which
route still confirms the reached spend when the feed changes shape under it.

## Why does each of the five keys hold, from the Diwali slide to the feed with two campaigns?

### Q1. What does the Diwali email's slide say the reached customers spent?

Five invented customers are on the table, and the feed names C-8102 twice.

The key is c, "The slide says Rs 26,000". The left merge gives C-8102 two rows, both with a feed
date, so the sum over filled dates is Rs 4,000, Rs 6,500 twice and Rs 9,000. The customers the email
reached spent Rs 19,500, and the slide overstates them by C-8102's whole Rs 6,500.

- a, "The slide says Rs 19,500": It is what the reached customers truly spent, the number the slide
  should have said and does not.
- b, "The slide says Rs 25,000": It is all five customers' spend, as if the sum ignored the feed
  dates.
- d, "The slide says Rs 31,500": It adds every row of the merged table, five customers and C-8102's
  second copy.

### Q2. How many rows does each of four merges of the table and the first-touch feed return?

There are 340 customers on the left and 130 on the right, and every one of the 130 is on the list.

The key is b, "They return 130, 340, 340 and 130 rows". With `how` left out the merge is inner, so
only the 130 found on both sides survive. Left keeps all 340. Outer keeps every key from either
side, and the 130 are already among the 340, so it adds nothing. Right keeps the 130.

- a, "They return 340, 340, 470 and 130 rows": It reads the default as left, and outer as the two
  sides stacked.
- c, "They return 130, 340, 470 and 130 rows": It gets the default right and still stacks the sides
  for outer.
- d, "They return 340, 340, 340 and 340 rows": It treats every merge as keeping the table whole.

### Q3. Which way should attach the app team's push feed, sized on what a repeat would cost?

Item 3 is a design item: 2,000 rows name 1,900 customers, and the stores team wants a count of
reached customers by city, today.

The key is d, "The `isin` flag fits, at 12,000 rows, with nothing counted twice and no rule to
choose". The ask is yes or no per customer, and a flag is set once however often the feed repeats a
customer, so the table stays at 12,000 rows and no spend is counted twice.

- a, "A plain left merge fits, at 12,100 rows and Rs 5.1 lakh counted twice in any spend sum": The
  100 repeated customers add 100 rows, and at Rs 5,100 each any sum of spend grows by Rs 5,10,000.
- b, "A merge counted before and after fits, at 12,100 rows, with the excess found afterwards": The
  count finds the 100 extra rows once the wrong table exists, and the ask never needed a merge.
- c, "The first-touch rule and a validated merge fit, at 12,000 rows and a date rule unused": It is
  safe, and it costs a rule about dates for an ask that never reads a date. When the ask needs the
  date, as Monday's table does, this is the way.

### Q4. In which order does Monday's attach step run, so a repeat never reaches the table?

The four steps are a merge with `validate`, keeping each customer's first row, sorting by date and
checking the table.

The key is a, "The order is 3, 2, 1, 4". The feed is sorted first, so that "first" means the
earliest date; the repeats are dropped next, so the merge's promise holds; the merge runs with the
promise stated; and the check confirms 340 rows and Rs 19,84,00,000 after it.

- b, "The order is 2, 3, 1, 4": It drops repeats before sorting, so "first" means whichever row the
  platform happened to send first.
- c, "The order is 1, 3, 2, 4": It merges the raw feed first, and `validate="one_to_one"` stops the
  run on the first repeated customer.
- d, "The order is 3, 1, 2, 4": It sorts, then merges before the repeats are dropped, and the run
  stops the same way.

### Q5. Which route confirms the monsoon sale's reached spend once the feed carries two campaigns?

Item 5 is a design item: the feed now mixes two campaigns and still repeats customers, so the second
route has to keep only the monsoon sale's rows, stay blind to repeats and measure the same spend the
marketing lead quotes.

The key is c, "Sum, in SQL, the orders of customers `IN` the feed's monsoon rows". Filtering on the
monsoon sale's `campaign_id` keeps the reach the marketing lead means. `IN` only asks whether a
customer is among those rows, however often they appear, so a repeat cannot multiply anything. The
query shares no code with the sort, the rule or the merge, and today, with only the monsoon sale in
the feed, it returns Rs 8,78,980.

- a, "Sum, in SQL, the orders of customers `IN` the warehouse's copy of the feed": `IN` is blind to
  repeats, and with no filter on the campaign it adds every customer the Navratri email alone
  reached, so it disagrees with a right merge.
- b, "Join the orders to the feed's monsoon rows in SQL, and sum the amounts": A join copies each
  order once for every row its customer has in the feed, the same fan-out as a plain merge, so it
  agrees with a plain merge that went wrong and disagrees with the right one.
- d, "Sum, in SQL, the monsoon customers' orders placed on or after the day the sale reached them":
  It measures spend after the sale reached each customer, a different number from the two quarters'
  spend the marketing lead quotes, so it disagrees even when the merge is right.

## Why is option c in item 3, the chapter's own method, the wrong answer worth arguing about?

Chapter 2 chose the first-touch rule and a validated merge for Monday's table, so a learner who
remembers the call picks it again. The call rested on a fact: Monday's table needs the date the sale
reached each customer. The stores team's ask needs only yes or no, and the flag answers it with no
rule to defend. When a later ask needs the date again, the rule and the validated merge come back.

## Where does one event arriving twice come up at work?

Meta's advertisers can send one purchase twice, once from the Meta Pixel in the shopper's browser
and once from their own server through the Conversions API, and Meta's documentation says they "must
set up a deduplication method". Under the method Meta recommends, when the same event ID and event
name reach the same Pixel within 48 hours, Meta keeps the first copy and discards the rest (Meta for
Developers, Handling Duplicate Pixel and Conversions API Events, checked 1 Oct 2026).
