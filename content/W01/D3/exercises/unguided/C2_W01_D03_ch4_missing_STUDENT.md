# Chapter 4 set: what is missing or malformed

4 items, about 12 minutes, after chapter 4. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask you to combine two of the day's ideas or to size the options yourself before you choose.

Post one line, 4 letters in item order, no spaces:

```
Post exactly this shape: xxxx
```

---

### Q1 (Design)

Next month about 1,800 of 60,000 orders will arrive with no status. Operations can look an order up in the courier's system at about 2 minutes an order, and the delivered share goes out every Monday. Which plan fits the weekly report?

a) Look up all 1,800 by hand before the first report goes out
b) Keep and flag them; report the share and the count unknown
c) Default them to delivered, since most orders with a status are
d) Drop them from the report, since 3 percent cannot move a share

### Q2

A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted amounts start `0, 0, 0, 410, 460`. What most likely happened?

a) Three amounts failed, and a helper turned each into 0
b) Three customers placed free orders during a promotion
c) Three orders were cancelled, and cancelled orders carry 0
d) Three small orders rounded down to 0 when converted

### Q3

A colleague converts amounts with `int(v) if v.isdigit() else 0`. On an invented export an amount written `1,150`, with a thousands separator, comes out as Rs 0. Which change fixes the logic?

a) Keep the isdigit test and footnote the order in the note
b) Replace the 0 with the segment's median amount
c) Wrap int() in try and return 0 on any failure
d) Try int(); on failure, log the value and its reason

### Q4 (Design)

An amount in the CSV reads `fourteen`. The JSON feed, cut from the same extract, reads `fourteen` for that order too, and no other source holds it. What goes in the log tonight?

a) Repair it from the feed, since a second source agrees with it
b) Read the word as Rs 14, since the text is plain about the number
c) Reject it to the log, and ask the ERP team for the booked value
d) Coerce it to zero, so the pass finishes and the log stays short
