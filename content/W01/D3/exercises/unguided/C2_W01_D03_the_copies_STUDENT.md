# Round 2 set: the copies and the identity rule

Seven items, about fifteen minutes, after round 2. Every number here is invented; the reasoning is
the one you ran on Kalpa's export this morning.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

---

### Q1

A colleague's dedupe of a 300-row export reports 0 duplicates, and a count of distinct order ids
returns 284. Each row carries a load timestamp added by the pipeline. What happened?

a) The timestamp made every row unique, so no row matched
b) Sixteen orders were lost in the load and need a resend
c) The dedupe is right, and the id count is off by 16
d) Sixteen rows carry blank order ids that the count skips

### Q2

Kalpa's ERP issues one order_id per order and never reuses it. What key do you deduplicate orders on?

a) customer_id and order_date together
b) Every field, the load timestamp included
c) Every field except the load timestamp
d) order_id, the key the ERP issues

### Q3

Two rows share order_id KR-90012. The first reads amount `--` and the second reads `1900`, and every
other field matches. Which row stays in the clean file?

a) The first, since the first extract is the original
b) The second, since its amount converts
c) Both, until Finance chooses between them
d) Neither, since the pair contradicts itself

### Q4

Two rows share order_id KR-90047. Both amounts convert to Rs 3,100; one is dated 21 August and the
other 30 July. Which decision goes in the log?

a) Drop both rows, since the order cannot be dated
b) Keep both rows, since the dates make them two orders
c) Keep the first extract's row and ask the ERP team
d) Keep the later date, since later loads are corrections

### Q5

Put the pass in order for Anand's analyst: 1 apply the identity rule, 2 reconcile rupees to the
books, 3 convert amounts and log failures, 4 reconcile rows. Which order holds?

a) 1, 3, 4, 2
b) 1, 4, 3, 2
c) 3, 4, 1, 2
d) 3, 1, 4, 2

### Q6

Twenty rows are set aside as copies. Two of them are Business orders carrying Rs 9,00,000 of the
Rs 9,30,000 set aside, and eighteen are Retail-Plus orders. Which conversation needs the two
Business rows first?

a) Anand's, since those two rows carry most of the rupees
b) Marketing's, since Retail-Plus is the segment they own
c) The auditor's, since most of the rows are Retail-Plus
d) Nobody's, since rows are rows and all twenty go together

### Q7

An analyst dedupes Kalpa orders on customer_id and order_date. A loyal member places two real orders
on the same day. What happens to revenue?

a) It stays right, since the key still finds true copies
b) It falls, since one real order is set aside as a copy
c) It rises, since the key keeps both orders and a copy
d) It stays right, since two orders a day never happen
