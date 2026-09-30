# Chapter 1 set: what the ERP actually sent

4 items, about 12 minutes, after chapter 1. The ERP is the enterprise resource planning system Finance books orders in, and its export is the file chapter 1 profiled. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask you to combine two of the day's ideas or to size the options yourself before you choose.

Post one line, 4 letters in item order, no spaces:

```
Post exactly this shape: xxxx
```

---

### Q1

A colleague's note to Anand names Rs 980 as the largest Q2 order in a new export, found by calling `max()` on the amounts as the CSV gave them. The same export's profile shows 21 Business orders, the smallest of them Rs 2,10,000. What do you tell the colleague before the note goes?

a) Send it, since max() looked at every Q2 amount the file holds
b) Send it, adding that Business orders are counted apart
c) Hold it: no largest order sits below every Business order
d) Hold it until the ERP team confirms Rs 980 is the true value

### Q2 (Design)

A new export of 1.2 crore rows and 12 fields lands, and Anand's analyst starts work in 45 minutes. The team's profile reads about 20 lakh values a minute. Which plan fits the 45 minutes?

a) Profile all 12 fields, then read the rows the profile flags
b) Profile order_id and amount, then read the rows they flag
c) Tie out a random sample of 10,000 rows against the books
d) Total every amount, then set the total beside the books

### Q3

An invented export holds 250 rows, 238 distinct order ids and 247 amounts that convert. How many rows could inflate revenue as copies, and how many amounts sit outside every total until someone reads them?

a) 12 copies and 3 unreadable amounts
b) 3 copies and 12 unreadable amounts
c) 15 copies and no unreadable amounts
d) 9 copies and 3 unreadable amounts

### Q4 (Design)

Next quarter's export will hold 4 crore rows. A Python set of order ids takes about 100 bytes an id, and the laptop the team leaves running overnight has 2 GB free. Which route counts the distinct order ids?

a) A set of every id, then its length, as chapter 1 did
b) A Counter over every id, which also keeps how often each appears
c) A set of the first crore ids, with the answer times four
d) Sort the ids on disk, then count each change from the last
