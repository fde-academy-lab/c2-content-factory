# Can you clean the export alone and send Anand a reconciliation his analyst can audit?

> "Send the reconciliation and the log before the day closes. My analyst checks it tonight, and she ties out to
> the rupee."
>
> Anand Iyer, finance controller, Kalpa Retail

**Who needs the answer.** Anand Iyer, the finance controller, decides tonight whether Finance accepts the
team's Q1 figure. His analyst ties out every line of the reconciliation: she matches each figure to the
books, Finance's own record of Q1 at Rs 1,90,00,000 to the rupee, so a rupee's difference is a finding.
Marketing's rescue campaign for Retail-Plus, Kalpa's paid membership tier, waits on the recomputed
numbers. A reconciliation she cannot follow becomes a finding against the team, and a number nobody
recomputes leaves Marketing planning on Tuesday's reading.

**The questions on the way.**

- What can you tell Anand from the profile and the feed?
- How does the identity rule treat repeated orders, today and next month?
- How do you decide on an unusual order and on amounts in new formats?
- Where did every row go, and what proves a re-sent export?
- What does the clean file change in Monday's tree, and what does Anand read first?

Fifty minutes, alone. The export is `data/C2_W01_D03_orders_STUDENT.csv`, Kalpa Retail's Q1 and Q2
orders from the ERP, the enterprise resource planning system Finance books orders in, and you clean it
with the day's pass in the notebook `notebooks/C2_W01_D03_ex1_escalated_case_STUDENT.ipynb`. A profile
counts, for every field, the values present, the values that convert and the distinct values. This time
you write the identity rule yourself, the rule that decides when two rows are one order and which copy
stays, and you recompute Monday's revenue tree on the clean file. The tree is revenue = customers x
orders per customer x revenue per order, with each branch read as Q2's multiple of Q1, and on Tuesday
the team read it on the export as delivered: customers x1.000, orders per customer x0.754, revenue per
order x1.180 and revenue x0.890, down 11.0 percent. Revenue in every figure is booked value, every order
at the price charged, whatever its status. The app's JSON feed is a second file cut from the same
extract as the CSV, an extract being one pull of rows out of the ERP.

The ten items below are the questions Anand, his analyst and Marketing send once your numbers land, and
a number an item calls the day's comes from your own run. Then write the note to Finance.

**What you post.** Three things, in this order: the notebook's nine letters; this brief's ten
letters; the note to Finance in under 120 words, numbers first.

```
Post exactly this shape: notebook xxxxxxxxx · brief xxxxxxxxxx · then the note
```

---

## Part 1. What can you tell Anand from the profile and the feed?

Used at work whenever a new file lands and a stakeholder asks what is in it.

### Q1. Which one line goes to Anand after the profile?

Your profile of the day's export shows order_id distinct on 186 of 201 rows, amount convertible on
200 and status present on 200. Anand asks for one line before you go further. Which line can you
defend at this point?

a) Your 1.9 crore is right; the export carries fifteen extra rows.
b) The export is clean apart from one amount and one missing status.
c) The gap is fifteen orders at about Rs 1.3 lakh each, Rs 20 lakh.
d) The export counts some orders twice; the rupees follow the rule.

### Q2. Which sentence about the JSON feed can the note carry?

The JSON feed yields 119 complete records and agrees with the CSV on 118 of their amounts; the 119th
is unreadable in both. Which sentence about the feed can the note carry?

a) The feed confirms the export's amounts for 118 of its orders.
b) The feed shows what the extract held; it cannot say a value is right.
c) The feed covers 59 percent of the export, so it can stand in for it.
d) The feed and the CSV disagree on one amount, so one of them is corrupt.

## Part 2. How does the identity rule treat repeated orders, today and next month?

Used at work wherever two extracts or two systems can send the same order twice.

### Q3. Which identity rule fits once two systems number their own orders? (Design)

From next month the export stitches the app's orders and the stores' orders, and each system numbers
its orders from KR-00001. In a test month, 312 order ids appear in both systems. Which identity rule
goes in the log, and what would today's rule cost?

a) order_id alone, as today, since the log records every row it sets aside
b) The whole record less the line, as real orders never fully match
c) The system and order_id together; today's rule drops 312 real orders
d) customer_id, amount and date, since a customer rarely repeats an order

### Q4. How many repeated orders go to the ERP team as a question?

The identity rule on the day's export keeps the copy whose amount converts, then the first. Chapter 3
found that of the 15 repeated orders, 13 have identical copies and 2 have copies that differ. How many
of the 15 does the log send to the ERP team as a question?

a) 15, one for every repeated order
b) 2, one for each pair whose copies differ
c) 1, for the pair whose valid copies disagree
d) 0, since the rule settles every pair itself

## Part 3. How do you decide on an unusual order and on amounts in new formats?

Used at work in every month-end close, when one order or one format does not fit last month's rules.

### Q5. What goes in the note about a large order the business says will not recur? (Design)

The head of Kalpa's Business segment, its sales to companies, says the largest Q2 order, the day's
Rs 29,45,460, was a one-off event order that will not recur. Anand wants Q2 as booked, and Marketing
wants a base for planning Q3. What goes in the note?

a) Q2 as booked, with the order; the Q3 plan built from Q2 without it
b) Q2 without the order, since it will not recur and would mislead
c) Q2 with it, and the Q3 plan built from Q2 as booked, order and all
d) Q2 with the order capped at the next largest, for both readers

### Q6. Which change to convert() fits amounts with paise and separators? (Design)

Next month about 40 percent of amounts will carry paise, `2310.50`, and a few a thousands separator,
`1,150`. The day's `convert()` accepts whole numbers only. Which change fits, judged by what each
leaves out of revenue?

a) Keep int(), and send every amount it refuses to the rejects log
b) Wrap int() in try, and return 0 for anything it refuses
c) Cut every amount at the dot before int(), and log the rest
d) Read commas and paise by one rule; log whatever still fails

## Part 4. Where did every row go, and what proves a re-sent export?

Used at work whenever a source system re-sends a file or a count differs from the one reported before.

### Q7. Where did the one amount that fails to convert go?

After the identity rule, converting the day's 186 kept amounts logs nothing, yet chapter 1's profile
counted one amount that fails. A colleague says the pass lost a reject. Where did that amount go?

a) To the set-aside log, as a copy, with its readable twin named
b) Into the clean file as text, since conversion skips kept rows
c) Nowhere, since the rule converted it while it compared copies
d) Out of the pass, since profile() drops a row once it fails

### Q8. What do you run on a Q1 export re-sent with the copies removed? (Design)

The ERP team offers to re-send the Q1 export tomorrow with the copies removed at source. What do you
run on it, and what should it show?

a) Nothing new, since today's bridge already explains the whole gap
b) Only a row count, expecting 100 rows, since the rupees follow
c) The whole pass: 100 orders, nothing set aside, Q1 on the books
d) Only the bridge, since copies were the one cause found today

## Part 5. What does the clean file change in Monday's tree, and what does Anand read first?

Used at work at the end of every reconciliation, when corrected numbers reach the people who acted on
the old ones.

### Q9. Which branch of Monday's tree moves furthest from Tuesday's reading?

Recomputed on the clean file, which branch of Monday's tree moves furthest from Tuesday's reading of
the Q1 to Q2 change?

a) Revenue per order: x1.144 on the clean file against x1.180
b) Orders per customer: x0.860 on the clean file against x0.754
c) Customers: the copies counted some of the 69 buyers twice
d) Orders per customer: x0.763 on the clean file against x0.754

### Q10. In what order does the note to Finance run?

The note to Finance has 120 words. Which order of content fits Anand's question?

a) Which figure is right; both reconciliations; what was flagged; what changed downstream
b) What changed downstream; which figure is right; both reconciliations; what was flagged
c) Both reconciliations; what was flagged; which figure is right; what changed downstream
d) What was flagged; both reconciliations; what changed downstream; which figure is right
