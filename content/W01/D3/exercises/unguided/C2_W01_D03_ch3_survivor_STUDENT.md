# Chapter 3 set: the copy that stays

4 items, about 12 minutes, after chapter 3. An extract is one pull of rows out of the ERP, the enterprise resource planning system Finance books orders in. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask you to combine two of the day's ideas or to size the options yourself before you choose.

Post one line, 4 letters in item order, no spaces:

```
Post exactly this shape: xxxx
```

---

### Q1

Two rows share order_id KR-90012. The first reads amount `--` and the second reads `1900`, and every other field matches. Which row stays in the clean file, and what does the log say?

a) The second, whose amount converts; the first logged unreadable
b) The first, as the original, with the second logged as its copy
c) Both, flagged, until Finance says which amount it booked
d) The first, with its amount set to 0 so that the sum runs

### Q2 (Design)

An invented export holds 40 repeated orders. In 38 pairs the copies are identical. In one pair the first copy's amount is unreadable and its twin reads Rs 2,600. In one pair the copies differ only on the date, both at Rs 1,450. What does keeping the first copy of every pair cost against the books?

a) Rs 0, since every order still keeps one of its rows
b) Rs 4,050, the unreadable pair and the pair with two dates
c) Rs 2,600, the twin's value, which the first copy lacks
d) Rs 5,200, since the lost twin's value counts twice in Q1

### Q3 (Design)

The ERP team replies that the second extract re-ran May's orders after a pricing fix, and copied April's and June's unchanged. Which survivor rule goes in the log?

a) Last copy for every pair, since the second extract is the fix
b) First copy for every pair, as the first extract is the original
c) The copy that converts, then the first, everywhere: it tied Q1
d) Last copy for May; elsewhere the copy that converts, then first

### Q4

Twenty rows are set aside as copies. Two are Business orders carrying Rs 9,00,000 of the Rs 9,30,000 set aside, and eighteen are Retail-Plus orders. Which conversation do the two Business rows belong to first?

a) Marketing's, since Retail-Plus carries most of the rows set aside
b) Anand's, since two rows carry nearly all of the rupees set aside
c) The auditor's, since every row set aside needs its reason first
d) Operations', since Business orders move the count of deliveries
