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
- Which route reaches the reached customers' spend without sharing the merge's code?

Every customer, feed and number in items 1 and 3 is invented.

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

a) Rs 19,500
b) Rs 25,000
c) Rs 26,000
d) Rs 31,500

### Q2. How many rows does each of four merges of the table and the first-touch feed return?

The growth team's table holds 340 customers, one row each. The feed, after the growth team's rule,
holds 130 customers, one row each, and every one of them is on the customer list. In order, how many
rows do `table.merge(first_touch, on="customer_id")`, then the same merge with `how="left"`,
`how="outer"` and `how="right"`, return?

a) 340, 340, 470 and 130
b) 130, 340, 340 and 130
c) 130, 340, 470 and 130
d) 340, 340, 340 and 340

### Q3. Which way should attach the app team's push feed, sized on what a repeat would cost?

Kalpa's app team sends a feed of the customers its October push notification reached: 2,000 rows
naming 1,900 customers, because 100 were sent twice. The stores team wants one answer from it today:
how many of its 12,000 loyalty customers the push reached, city by city. A typical reached
customer's spend is Rs 5,100. Which way fits the ask, and what does it cost?

a) A plain left merge: 12,100 rows, Rs 5.1 lakh counted twice in any spend sum
b) A merge counted before and after: 12,100 rows, the excess found afterwards
c) The first-touch rule and a validated merge: 12,000 rows and a date rule unused
d) The `isin` flag: 12,000 rows, nothing counted twice, and no rule to choose

### Q4. In which order does Monday's attach step run, so a repeat never reaches the table?

Four steps, numbered:

1. Merge the feed onto the table with `how="left"` and `validate="one_to_one"`.
2. Keep each customer's first row with `drop_duplicates("customer_id", keep="first")`.
3. Sort the feed by `exposed_date`.
4. Check that the table still holds 340 rows and Rs 19,84,00,000.

Which order runs them?

a) 3, 2, 1, 4
b) 2, 3, 1, 4
c) 1, 3, 2, 4
d) 3, 1, 2, 4

### Q5. Which route reaches the reached customers' spend without sharing the merge's code?

Kavya wants the marketing lead's Rs 8,78,980 confirmed by a route that would disagree if the rule or
the merge had gone wrong. Which route qualifies?

a) Sum `spend` over `merged["reached"]` again, after rerunning the merge
b) A plain inner merge of the table and the raw feed, with spend summed
c) A SQL sum of the orders of customers `IN` the feed's warehouse table
d) Total spend less the unreached customers' spend, from the merged table
