# Which customers did the monsoon sale reach, and what did the reached customers spend?

Chapter 2 set, five items, after chapter 2: items 1 and 2 run live in the chapter's last three
minutes; the rest are the practice lab's stretch or tonight's work.

> "Before I ask for November's budget, I need two numbers I can stand behind: how many customers the
> monsoon sale reached, and what those customers spent."
>
> The marketing lead, Kalpa Retail

The marketing lead owns acquisition and campaigns at Kalpa Retail. The monsoon sale ran in August
2026 at 15 percent off, and the campaign platform sends a feed of the customers it reached, one row
per customer with the date the sale reached them, or so the platform says. The growth team's table
holds one row for each of Kalpa's 340 customers, with spend over the two quarters, April to
September 2026, adding up to Rs 19,84,00,000.

A merge in pandas is a join, with the four shapes SQL has: `how="inner"` keeps the keys found on
both sides, `"left"` every row of the left table, `"right"` every row of the right one and `"outer"`
every key from either side. `validate` states what the merge promises, such as `"one_to_one"`, each
key at most once on each side, and raises `pandas.errors.MergeError` the moment the data breaks the
promise. Chapter 2 attached the sale to the table: 130 customers reached, who spent Rs 8,78,980 over
the two quarters, with the table still 340 rows and Rs 19,84,00,000. The growth team's rule for a
customer the feed names twice is that they were reached once, on the first date. Kavya Nair, the
senior analyst on the team, reviews every table before it leaves.

**Who needs the answer.** The marketing lead, who asks for November's budget on these two numbers.
A reach or a spend inflated by the way a feed was joined makes the case with money nobody paid, and
the gap surfaces the day Finance ties the table back to the warehouse.

**The questions on the way.**

- What does the Diwali email's slide say the reached customers spent?
- How many rows does each of four merges of the table and the first-touch feed return?
- Which way should attach the app team's push feed, sized on what a repeat would cost?
- In which order does Monday's attach step run, so a repeat never reaches the table?
- Which route confirms the monsoon sale's reached spend once the feed carries two campaigns?

Every customer, feed and number in items 1 and 3 is invented, and so is the Navratri campaign in
item 5.

**What you post.** One line of five letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxx
```

---

### Q1. What does the Diwali email's slide say the reached customers spent?

Five invented customers and their spend over the year:

| customer_id | spend, Rs |
|---|---|
| C-8101 | 4,000 |
| C-8102 | 6,500 |
| C-8103 | 2,500 |
| C-8104 | 9,000 |
| C-8105 | 3,000 |

The Diwali email's feed arrives as four rows, in this order: C-8101, C-8102, C-8102, C-8104. An
analyst runs `small.merge(feed, on="customer_id", how="left")` and adds up `spend` over the rows
whose feed date is filled. What does the slide say the reached customers spent?

a) The slide says Rs 19,500.
b) The slide says Rs 25,000.
c) The slide says Rs 26,000.
d) The slide says Rs 31,500.

### Q2. How many rows does each of four merges of the table and the first-touch feed return?

The growth team's table holds 340 customers, one row each. The feed, after the growth team's rule,
holds 130 customers, one row each, and every one of them is on the customer list. In order, how many
rows do `table.merge(first_touch, on="customer_id")`, then the same merge with `how="left"`,
`how="outer"` and `how="right"`, return?

a) They return 340, 340, 470 and 130 rows.
b) They return 130, 340, 340 and 130 rows.
c) They return 130, 340, 470 and 130 rows.
d) They return 340, 340, 340 and 340 rows.

### Q3. Which way should attach the app team's push feed, sized on what a repeat would cost?

Kalpa's app team sends a feed of the customers its October push notification reached: 2,000 rows
naming 1,900 customers, because 100 were sent twice. The stores team wants one answer from it today:
how many of its 12,000 loyalty customers the push reached, city by city. A typical reached
customer's spend is Rs 5,100. Which way fits the ask, and what does it cost?

a) A plain left merge fits, at 12,100 rows and Rs 5.1 lakh counted twice in any spend sum.
b) A merge counted before and after fits, at 12,100 rows, with the excess found afterwards.
c) The first-touch rule and a validated merge fit, at 12,000 rows and a date rule unused.
d) The `isin` flag fits, at 12,000 rows, with nothing counted twice and no rule to choose.

### Q4. In which order does Monday's attach step run, so a repeat never reaches the table?

Four steps, numbered:

1. Merge the feed onto the table with `how="left"` and `validate="one_to_one"`.
2. Keep each customer's first row with `drop_duplicates("customer_id", keep="first")`.
3. Sort the feed by `exposed_date`.
4. Check that the table still holds 340 rows and Rs 19,84,00,000.

Which order runs them?

a) The order is 3, 2, 1, 4.
b) The order is 2, 3, 1, 4.
c) The order is 1, 3, 2, 4.
d) The order is 3, 1, 2, 4.

### Q5. Which route confirms the monsoon sale's reached spend once the feed carries two campaigns?

Invented: from its next file, the campaign platform sends every campaign Kalpa runs in one feed, the
monsoon sale's rows beside a Navratri email's, each row carrying its `campaign_id`. Some customers
appear under both campaigns, and some appear twice under one. The warehouse loads the same file as
its own copy of the feed, `campaign_exposure`. Kavya wants the monsoon sale's Rs 8,78,980 confirmed
by a route that shares no code with the rule or the merge and would disagree if either had gone
wrong. Which route qualifies?

a) Sum, in SQL, the orders of customers `IN` the warehouse's copy of the feed.
b) Join the orders to the feed's monsoon rows in SQL, and sum the amounts.
c) Sum, in SQL, the orders of customers `IN` the feed's monsoon rows.
d) Sum, in SQL, the monsoon customers' orders placed on or after the day the sale reached them.
