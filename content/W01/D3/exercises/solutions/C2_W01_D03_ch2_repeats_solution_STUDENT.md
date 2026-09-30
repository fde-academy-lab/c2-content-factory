# Which answers hold in the chapter 2 set on the rows the export counted twice, and why?

Answers: 1a 2c 3b 4d

Kalpa Retail's export from the ERP, the enterprise resource planning system Finance books orders in, holds 201 rows for 186 orders, and Anand Iyer, the finance controller, needs to know which rows it counted twice before he believes either the export or the books, Finance's own record of Q1 at Rs 1,90,00,000.

Two of the four items are design items: 2 and 4.

### Q1. Why does a dedupe find 0 copies when 300 rows hold 284 order ids?

A dedupe of a 300-row export reports 0 duplicates, a count of distinct order ids returns 284, and the pipeline stamps every row with the time it was loaded.

The key is a, "The load stamp differs on every row, so no two rows matched". A load stamp differs on every row, so a key that compares the whole record never finds a match, and 300 rows against 284 ids says 16 rows repeat an order.

- b, "16 orders were lost in the load, and the ERP team must resend": all 300 rows are present, so nothing was lost.
- c, "The dedupe is right, and the id count is off by 16 somewhere": the id count is the check, and it disagrees with the dedupe.
- d, "16 rows carry a blank order_id, so the id count falls short": blank ids would show in the profile, the count of each field's present, convertible and distinct values, as order_id present on fewer than 300 rows, and the dedupe would still match nothing.

### Q2. Which match builds one customer table from two systems inside 2 hours? (Design)

Meera Raghavan, Kalpa Retail's CEO, wants one customer table from 30,000 app records and 30,000 store records, each system numbering customers from C-1, over 6 cities, with the machine comparing about 50 lakh pairs a minute and 2 hours to finish.

The key is c, "Cleaned phone and email, compared within each city". Neither id names one person across both systems, so the match rests on contact fields cleaned the same way. Every record against every other is 60,000 x 59,999 / 2, about 180 crore pairs, 360 minutes at 50 lakh a minute; within 6 cities of 10,000 it is about 30 crore pairs, 60 minutes, inside the window, with doubtful pairs sent to a person.

- a, "Each system's own customer id, one lookup a record": C-1 in the app and C-1 in a store are different people.
- b, "Cleaned phone and email, every record against every other": the right fields, and 6 hours, three times the window.
- d, "Every field matching exactly, name and address too": two systems rarely write one person's record identically, so real matches are missed.

### Q3. What does a reviewer still owe Anand when two keys agree on 22 rows?

On an invented export the order_id key and a fuzzy match on customer and amount within 60 days each flag 22 rows, and the reviewer is about to sign off because the counts agree.

The key is b, "Compare the two lists of flagged rows, line against line". Two keys can flag the same number of rows and share fewer than all of them. Only the rows themselves show which real orders one key removed and which copies it missed.

- a, "Compare the two keys' counts again, quarter by quarter": counts by quarter can match while the rows differ.
- c, "Rerun the fuzzy match with a 30-day window to confirm 22": a narrower window changes the count and cannot test whether the rows are the same.
- d, "Check that both keys flag at least one Business order": a check on one segment, Kalpa's sales to companies, says nothing about which rows either key flagged.

### Q4. Where does the fuzzy match leave revenue against the order_id key? (Design)

The fuzzy match flags 40 rows and the order_id key 38, sharing 36; the 4 only the fuzzy match flags are real orders averaging Rs 2,50,000, and the 2 only the order_id key flags are copies of Rs 3,000 each.

The key is d, "Rs 9,94,000 below the order_id key's figure". The fuzzy match removes 4 real orders, Rs 10,00,000, and keeps 2 copies the id key removes, Rs 6,000, so its revenue sits Rs 10,00,000 less Rs 6,000 below: Rs 9,94,000.

- a, "Rs 10,06,000 below the order_id key's figure": counts the kept copies as a second loss, when they add rupees.
- b, "Rs 6,000 above the order_id key's figure": counts only the copies and forgets the four real orders.
- c, "Rs 10,00,000 below the order_id key's figure": forgets the two copies the fuzzy match keeps.
