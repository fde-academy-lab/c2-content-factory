# Chapter 1 set: what the ERP actually sent

6 items, about 18 minutes, after chapter 1. Every number here is invented unless it says it is from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask for the best-fit approach, a sizing or the fact that would change it.

Post one line, 6 letters in item order, no spaces:

```
Post exactly this shape: xxxxxx
```

---

### Q1

An analyst reads three amounts straight from a CSV, `["950", "18000", "4500"]`, and calls `max()` on the list to name the largest order for Anand. Which order does the note name as the largest?

a) Rs 18,000, since max compares the numbers the text holds
b) Rs 4,500, since max takes the middle value of three strings
c) Rs 950, since text compares one character at a time
d) None of them, since max raises an error on text

### Q2 (Design)

Two exports of the same quarter arrive, profiled the same way.

| Export | Rows | Distinct order ids | Amounts that convert |
|---|---|---|---|
| North | 240 | 240 | 238 |
| South | 240 | 221 | 240 |

Which export would you total first for Anand?

a) North, whose two failed amounts can be logged and read
b) South, since every one of its amounts converts cleanly
c) Neither, since both carry at least one field that fails
d) Both at once, since the two profiles have equal row counts

### Q3

Anand asks about this invented profile of an export.

| Field | Present | Convertible | Distinct |
|---|---|---|---|
| order_id | 180 | text | 171 |
| amount | 180 | 180 | 164 |
| channel | 180 | text | 3 |
| discount | 122 | 122 | 5 |

Which field could move his revenue figure?

a) discount, since a third of its values are missing
b) channel, since three values cannot describe 180 orders
c) amount, since 164 distinct values means some repeat
d) order_id, since 180 rows hold 171 orders

### Q4

`json.load` on the app's feed stops with `JSONDecodeError: Unterminated string starting at: line 812 column 9`. What do you do first?

a) Wrap the load in try and skip the whole feed
b) Open the file at line 812 and read what is there
c) Ask the ERP team to resend the feed as a CSV file
d) Re-run the load, since the error is often transient

### Q5 (Design)

A new export has 2 crore rows and Anand wants the reconciliation tomorrow. Which way of learning what arrived is the best fit?

a) Scroll the first thousand rows of it in a spreadsheet
b) Total the amounts and compare with the books
c) Sample 1,000 rows and tie each to the books
d) Profile every field, then read the rows it flags

### Q6 (Design)

A sample of 20 rows is drawn from a 200-row export that holds one unreadable amount. About how likely is the sample to contain it?

a) About 90 percent
b) About 50 percent
c) About 10 percent
d) Certain, since 20 rows is enough
