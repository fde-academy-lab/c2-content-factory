# When an order appears twice, which copy stays, and does Q1 then land on the books?

Chapter 3 set, 4 items, about 12 minutes, after chapter 3. The books are Finance's own record of Q1, Rs 1,90,00,000 to the rupee, and an order appears twice when Kalpa Retail's export of orders from the ERP, the enterprise resource planning system Finance books orders in, carries it on two rows.

> "When two copies disagree, which one did you keep, and why that one?"
>
> Anand Iyer, finance controller, Kalpa Retail

The export was stitched from two extracts, two separate pulls of rows out of the ERP. Chapter 2 found that the order_id, the number the ERP issues once per order, decides when two rows are one order: 15 orders appear twice, 14 in Q1 and 1 in Q2, none three times. For 13 of those pairs the two copies are identical, and for 2 they disagree. A survivor rule picks which copy of a pair stays in the clean file, and every copy it does not keep is set aside to a log with its reason; a copy's twin is the other row of the same order. An amount converts when it reads as a whole number of rupees. As exported, Q1 comes to Rs 2,09,98,210 against the books' Rs 1,90,00,000, Rs 19,98,210 apart. Kalpa's Business segment is its sales to companies, every order in lakhs, and Retail-Plus is its paid membership tier.

**Who needs the answer.** Anand Iyer is the finance controller, and his analyst ties out to the rupee: she matches every figure to the books line by line, and a rupee's difference is a finding. If the copy kept for any order moves Q1 away from the books, the reconciliation she checks becomes a finding against the team, and on today's file keeping the wrong copy moved Q1 by Rs 1,790.

**The questions on the way.**

- Which row of order KR-90012 stays, and what does the log say?
- What does keeping the first copy of every pair cost against the books?
- Which survivor rule goes in the log once the ERP team explains the second extract?
- Who hears first about the two Business rows set aside?

Every number in the items is invented unless the item says it comes from today's file, and the reasoning is the one you ran on Kalpa's export. An item marked Design asks you to combine two of the day's ideas, or to size the options yourself, before you choose.

**What you post.** One line of 4 letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

### Q1. Which row of order KR-90012 stays, and what does the log say?

On an invented export, two rows share order_id KR-90012. The first reads amount `--` and the second reads `1900`, and every other field matches. Which row stays in the clean file, and what does the log say?

a) The second, whose amount converts; the first logged unreadable
b) The first, as the original, with the second logged as its copy
c) Both, flagged, until Finance says which amount it booked
d) The first, with its amount set to 0 so that the sum runs

### Q2 (Design). What does keeping the first copy of every pair cost against the books?

An invented export holds 40 repeated orders. In 38 pairs the copies are identical. In one pair the first copy's amount is unreadable and its twin reads Rs 2,600. In one pair the copies differ only on the date, both at Rs 1,450. What does keeping the first copy of every pair cost against the books?

a) Rs 0, since every order still keeps one of its rows
b) Rs 4,050, the unreadable pair and the pair with two dates
c) Rs 2,600, the twin's value, which the first copy lacks
d) Rs 5,200, since the lost twin's value counts twice in Q1

### Q3 (Design). Which survivor rule goes in the log once the ERP team explains the second extract?

The ERP team replies that the second extract re-ran May's orders after a pricing fix, and copied April's and June's unchanged. Which survivor rule goes in the log?

a) Last copy for every pair, since the second extract is the fix
b) First copy for every pair, as the first extract is the original
c) The copy that converts, then the first, everywhere, as it tied Q1 today
d) Last copy for May; elsewhere the copy that converts, then first

### Q4. Who hears first about the two Business rows set aside?

Twenty rows are set aside as copies. Two are Business orders carrying Rs 9,00,000 of the Rs 9,30,000 set aside, and eighteen are Retail-Plus orders. Anand needs the gap to his books explained in rupees, Marketing reads the per-customer rates behind Tuesday's finding, the auditor asks why each row went, and Operations counts deliveries. Which conversation do the two Business rows belong to first?

a) Marketing's, since Retail-Plus carries most of the rows set aside
b) Anand's, since nearly all of the gap in rupees sits in those two
c) The auditor's, since every row set aside needs its reason first
d) Operations', since Business orders move the count of deliveries
