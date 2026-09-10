# Day 3, E3. Mid-session: classify the gaps

Drop point: the close of the second block, after duplicates and outliers. About 15 minutes, working alone.

Four missingness cases, then eleven items on duplicates, extremes and what ships. Every answer is a letter.

Post one line at the end, in this shape, using your own letters:

```
1c 2a 3d 4b 5c 6a 7d 8b 9c 10a 11d 12b 13c 14a 15d
```

---

## Item 1

`discount` is absent on 39 of 50 orders, and absence means no discount ran. What do you do?

a) Keep absent as absent, and flag it
b) Fill it with zero
c) Drop those 39 orders
d) Fill it with the mean of the eleven present values

## Item 2

`amount` is absent on 2 of 50 orders, and an order with no amount cannot be summed. What do you do?

a) Fill it with the segment mean
b) Reject the row, with a reason
c) Fill it with zero
d) Keep it and flag it

## Item 3

`order_date` is present on all 50 and one of them reads `2026-09-14` where the rest of that customer's orders are in August. What do you do?

a) Delete the row and note why you did
b) Correct it to August, like its neighbours
c) Nothing yet, a later date is no defect
d) Reject it as unparseable

## Item 4

`customer_id` has 47 distinct values across 50 rows. What do you do?

a) Reject the repeated customer rows
b) Fill the repeated ones with fresh ids
c) Escalate it as a duplicate
d) Nothing, customers place many orders

## Item 5

Match each case above to the treatment it earned. One treatment is left over.

Cases
1. discount, absent on 39
2. amount, absent on 2
3. customer_id, 47 across 50

Treatments
a) reject the row with a reason
b) keep absent as absent, and flag it
c) escalate to the order book owner
d) nothing, this is expected

Which matching is right?

a) 1 to b, 2 to a, 3 to d
b) 1 to a, 2 to b, 3 to c
c) 1 to d, 2 to c, 3 to a
d) 1 to b, 2 to c, 3 to a

## Item 6

A whole-record dedupe reports zero and the distinct order_id count reports 49 across 50 rows. What happened?

a) The dedupe crashed and returned an empty result
b) Two rows share an id and differ somewhere
c) One order_id is empty, so it did not count as distinct
d) The file holds a repeated header row

## Item 7

You look at the pair. Same id, same customer, same amount, same status, six weeks apart on `order_date`. Which identity rule finds it?

a) every field
b) order_id plus order_date
c) order_id alone
d) order_id plus amount plus order_date

## Item 8

Four defensible identity rules give three different answers. What does that tell you?

a) The data is corrupt
b) The dedupe function is wrong somewhere
c) You should use every field, since it is the strictest
d) The rule is the decision

## Item 9

Who decides which rule applies?

a) Whoever owns the order book
b) You, on the day, since you are cleaning it
c) Nobody, since the strictest rule is always right
d) The person who wrote the file

## Item 10

The largest amount in the file is Rs 480,000 against a next-largest of about Rs 2,900. What do you do first?

a) Delete it, since it is plainly an outlier
b) Investigate it, since it looks real
c) Cap it at the fence
d) Split it into smaller orders

## Item 11

That one order is 86 percent of the money in the file. What does that do to the mean?

a) Nothing, since the mean uses every value
b) It pulls the median far above every ordinary order
c) It pulls the mean far above every ordinary order
d) It has no effect until you sort the column

## Item 12

What goes in the decisions log about it?

a) Outlier removed from the cleaned file
b) The row number it sits on in the file
c) Nothing, since nothing was changed
d) The amount, its share, and it stays

## Item 13

The companion file reads 21 rows and the first one holds `order_id` in the order_id column. What happened?

a) The header row was written twice
b) The file is sorted alphabetically
c) The reader failed and returned a placeholder
d) A row was corrupted somewhere in transit

## Item 14

Which check would have caught that without anybody reading the file?

a) A row count
b) A check for a value equal to its field
c) A check that the file parses without error
d) A check that the file is not empty

## Item 15

At the close of the day, what ships?

a) The clean file
b) The clean file and the rejects file only
c) The clean file, the rejects and the log
d) The notebook

---

Post your fifteen letters on one line in the shape shown at the top. The solution is released at the close of the session.

## Hands-on

The running half is `notebooks/C2_W01_D03_ex1_hands_on_STUDENT.ipynb`, which profiles the file, records the decisions, runs the pass and reconciles the counts. Post its five letters on the same line as these fifteen.
