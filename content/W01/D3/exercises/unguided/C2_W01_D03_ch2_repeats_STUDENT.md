# The file holds 201 rows for 186 orders: which rows did the export count twice, and what makes two rows one order?

Chapter 2 set, 4 items, about 12 minutes, after chapter 2. The file is Kalpa Retail's export of Q1 and Q2 orders from the ERP, the enterprise resource planning system Finance books orders in, and an order is one sale, which the export may carry on more than one row.

> "Which rows did the export count twice, and how do you know they are copies?"
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand Iyer, the finance controller, needs to know whether his books, Finance's own record of Q1 at Rs 1,90,00,000, are short or the export is high. A wrong answer either keeps Rs 20 lakh that was never earned or deletes real orders from his books, and every per-customer rate the team reported on Tuesday, such as orders per customer, moves with the same rows.

**The questions on the way.**

- Why does a dedupe find 0 copies when 300 rows hold 284 order ids?
- Which match builds one customer table from two systems inside 2 hours?
- What does a reviewer still owe Anand when two keys agree on 22 rows?
- Where does the fuzzy match leave revenue against the order_id key?

Chapter 1 profiled the export, counting for every field the values present, the values that convert and the distinct values. It found 201 rows for 186 distinct values of order_id, the field that carries each order's number, and Q1 over the amounts that convert comes to Rs 2,09,98,210, Rs 19,98,210 above the books. The ERP team's note says the CSV was stitched from two extracts, two separate pulls of rows out of the ERP, during the migration, the Q1 move of the order data from one system to another. A dedupe is a step that removes the rows it judges to be copies of another row.

Every number in the items is invented unless the item says it comes from today's file, and the reasoning is the one you ran on Kalpa's export. An item marked Design asks you to combine two of the day's ideas, or to size the options yourself, before you choose.

**What you post.** One line of 4 letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

### Q1. Why does a dedupe find 0 copies when 300 rows hold 284 order ids?

A colleague's dedupe of a 300-row export reports 0 duplicates, and a count of distinct order ids returns 284. The pipeline stamps every row with the time it was loaded. What happened?

a) The load stamp differs on every row, so no two rows matched
b) 16 orders were lost in the load, and the ERP team must resend
c) The dedupe is right, and the id count is off by 16 somewhere
d) 16 rows carry a blank order_id, so the id count falls short

### Q2. Which match builds one customer table from two systems inside 2 hours? (Design)

Meera Raghavan, Kalpa Retail's CEO, wants one customer table from the app's 30,000 records and the stores' 30,000, each system numbering customers from C-1, spread evenly over 6 cities. The team's machine compares about 50 lakh pairs a minute, and the job must finish inside 2 hours. Which match fits?

a) Each system's own customer id, one lookup a record
b) Cleaned phone and email, every record against every other
c) Cleaned phone and email, compared within each city
d) Every field matching exactly, name and address too

### Q3. What does a reviewer still owe Anand when two keys agree on 22 rows?

On an invented export the order_id key flags 22 rows as copies, and a fuzzy match on customer and amount within 60 days also flags 22. The reviewer is about to sign off because the counts agree. Which check does the reviewer still owe Anand?

a) Compare the two keys' counts again, quarter by quarter
b) Compare the two lists of flagged rows, line against line
c) Rerun the fuzzy match with a 30-day window to confirm 22
d) Check that both keys flag at least one Business order

### Q4. Where does the fuzzy match leave revenue against the order_id key? (Design)

On an invented export the fuzzy match flags 40 rows and the order_id key flags 38; they share 36. The 4 rows only the fuzzy match flags are real orders averaging Rs 2,50,000, and the 2 rows only the order_id key flags are copies of Rs 3,000 each. Against the order_id key, where does the fuzzy match leave the quarter's revenue?

a) Rs 10,06,000 below the order_id key's figure
b) Rs 6,000 above the order_id key's figure
c) Rs 10,00,000 below the order_id key's figure
d) Rs 9,94,000 below the order_id key's figure
