# Chapter 4 set: what is missing or malformed

5 items, about 15 minutes, after chapter 4. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask for the best-fit approach, a sizing or the fact that would change it.

Post one line, 5 letters in item order, no spaces:

```
Post exactly this shape: xxxxx
```

---

### Q1 (Design)

An order in Q2 has no status and a valid amount. Revenue is booked value, and Operations also reads the delivered share. Which decision keeps both numbers honest?

a) Drop the order, since its fate is unknown
b) Default the status to delivered, the usual case
c) Keep the order and flag the status as unknown
d) Default the status to cancelled, the safe case

### Q2

A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted amounts start `0, 0, 0, 410, 460`. What most likely happened?

a) Three amounts failed and a helper turned each into 0
b) Three customers placed free orders in a promotion
c) Three orders were cancelled, and cancelled orders carry 0
d) The profile is right, and zero is a valid Kalpa order

### Q3

A colleague converts amounts with `int(v) if v.isdigit() else 0`. On an invented export, an amount written `1,150` with a thousands separator comes out as Rs 0. Which change fixes the logic?

a) Keep the isdigit test and footnote the order
b) Replace the 0 with the segment's median amount
c) Wrap int() in try and return 0 on any failure
d) Try int(); log the value and its reason

### Q4 (Design)

An amount in the CSV reads `fourteen`. The JSON feed, cut from the same extract, reads `fourteen` for that order too. Which is the best fit for the log?

a) Repair it from the feed, since a second source agrees
b) Reject it to the log and ask the ERP team
c) Read the word as Rs 14, since the text says fourteen
d) Coerce it to zero so the pass can finish tonight

### Q5

Forty of 100 orders carry no discount, and the 60 that carry one average Rs 90. What does the average read if the blanks are taken as zero?

a) Rs 90
b) Rs 72
c) Rs 36
d) Rs 54
