# Round 1 set: read the profile before any total

Seven items, about fifteen minutes, after round 1. Every item is a question Anand's analyst or Kavya
would put to you about an export, and every number in it is invented unless it says it is from
today's file. Work alone, then compare with a partner before posting.

Post one line, seven letters in item order, no spaces:

```
Post exactly this shape: xxxxxxx
```

The hands-on part of the day is the escalated case notebook, `notebooks/C2_W01_D03_hands_on_STUDENT.ipynb`,
after lunch.

---

### Q1

An analyst reads three amounts straight from a CSV, `["950", "18000", "4500"]`, and calls
`max()` on the list to name the largest order for Anand. Which order does the note name as the largest?

a) Rs 18,000, since max compares the numbers the text holds
b) Rs 4,500, since max takes the middle value of three strings
c) Rs 950, since text compares one character at a time
d) None of them, since max raises an error on a list of text

### Q2

Two exports of the same quarter arrive, profiled the same way.

| Export | Rows | Distinct order ids | Amounts that convert | Status present |
|---|---|---|---|---|
| North | 240 | 240 | 238 | 240 |
| South | 240 | 221 | 240 | 240 |

Which export would you total first for Anand?

a) South, since every one of its amounts converts cleanly
b) Neither, since both carry at least one field that fails
c) North, whose two failed amounts can be logged and read
d) Both at once, since the two profiles have equal row counts

### Q3

A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted
amounts start `0, 0, 0, 410, 460`. What most likely happened?

a) Three customers placed free orders during a promotion
b) Three orders were cancelled, and cancelled orders carry 0
c) The profile is right, and zero is a valid Kalpa order value
d) Three amounts failed and a helper turned each into 0

### Q4

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
d) order_id, since 180 rows hold only 171 distinct orders

### Q5

`json.load` on the app's feed stops with `JSONDecodeError: Unterminated string starting at: line 812
column 9`. What do you do first?

a) Open the file at line 812 and read what is there
b) Wrap the load in try and skip the whole feed
c) Ask the ERP team to resend the feed in CSV
d) Re-run the load, since the error is often transient

### Q6

The same order reads `"status": ""` in the CSV and has no `status` key in the JSON feed. A loop
running `r["status"]` over both files for the delivered count does what?

a) Counts both records as delivered by default
b) Raises a KeyError on the JSON record only
c) Returns an empty string for both records
d) Raises a KeyError on the CSV record only

### Q7

An invented export holds 150 rows and 141 distinct order ids, and 148 of its amounts convert.
How many rows sit beyond one per order?

a) 2
b) 7
c) 9
d) 11
