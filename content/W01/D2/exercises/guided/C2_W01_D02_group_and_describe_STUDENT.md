# Guided: group, describe, and write it once

Built with the trainer across chapters 2 and 3, one step at a time, in your own Codespace. Nothing
here is graded. Every line on your screen is there because you typed it, which is what makes it
yours when the afternoon's case arrives and nobody types it for you.

The ask the steps answer:

> "Are we losing customers, or are the ones we have buying less? Is it across all our customers, or
> one kind of customer?" (Meera Raghavan)

Five checkpoints sit between the steps. Answer each one before you run the cell, then run it and
see whether you were right. Post one line at the end, five letters in checkpoint order, no spaces:

```
Post exactly this shape: xxxxx
```

```mermaid
flowchart LR
    A["<b>200 orders</b>"] --> B["<b>group by quarter</b><br/>a dictionary accumulator"]
    B --> C["<b>group by segment</b><br/>the same move, a new key"]
    C --> D["<b>describe one segment</b><br/>typical value and spread"]
    D --> E["<b>revenue_for</b><br/>one decision, written once"]
```

---

## Step 1. Group by quarter

Open a new cell below the setup cell of chapter 2's notebook and type the accumulator with the room:

```python
ORDERS = kit.load_records("C2_W01_D02_orders_STUDENT.py")

orders_by_quarter = {}
revenue_by_quarter = {}
for order in ORDERS:
    q = order["quarter"]
    if q not in orders_by_quarter:
        orders_by_quarter[q] = 0
        revenue_by_quarter[q] = 0
    orders_by_quarter[q] = orders_by_quarter[q] + 1
    revenue_by_quarter[q] = revenue_by_quarter[q] + order["amount"]
```

### Checkpoint 1. Anand asks how many orders each quarter booked. After the loop, what does `orders_by_quarter` hold?

a) `{"Q1": 69, "Q2": 69}`, one count for each distinct customer
b) `{"Q2": 1}`, since the dictionary is reset on every order
c) `{"Q1": 200, "Q2": 200}`, since every order is counted twice
d) `{"Q1": 114, "Q2": 86}`, one count for each order booked

### Checkpoint 2. What does `revenue_by_quarter` hold, written as Meera would read it?

a) Rs 1,84,211 in Q1 and Rs 2,17,442 in Q2, the revenue per order
b) Rs 2,10,00,000 in Q1 and Rs 1,87,00,000 in Q2, the booked revenue
c) Rs 3,97,00,000 in Q1 and Rs 3,97,00,000 in Q2, the file's revenue
d) Rs 2,10,00,000 in Q1 and Rs 2,10,00,000 in Q2, the first quarter's

---

## Step 2. Group by segment, inside each quarter

The same move with a key made of two parts. Change the key line to
`key = (order["quarter"], order["segment"])` and build `orders_by_key` and `customers_by_key`,
where the second holds a set of customer ids for each key. Run it, then print the keys in order
with `for key in sorted(orders_by_key): print(key)`. Read the counts in your own notebook; the room
reads them together in chapter 3.

### Checkpoint 3. Before you read a single count, how many keys should `orders_by_key` hold, and why check?

a) Eight, four segments in each of two quarters; fewer means a group is lost
b) Four, one per segment; the quarter is a column that the key leaves out
c) Two hundred, one key per order; a dictionary keeps every row it is given
d) Sixty-nine, one per customer; a customer is the unit Meera is asking about

---

## Step 3. Describe one segment

Pull the Retail-Core amounts for Q1 into a list, sort it, and describe it with the room:

```python
amounts = []
for order in ORDERS:
    if order["quarter"] == "Q1" and order["segment"] == "Retail-Core":
        amounts.append(order["amount"])
amounts.sort()
print(len(amounts), amounts[:5], amounts[-5:])
```

Then the median with `statistics.median(amounts)`, the minimum, the maximum and the range. Read the
sorted list aloud from both ends before you trust any single number.

### Checkpoint 4. Which description of Retail-Core in Q1 is right?

a) Median Rs 2,117, min Rs 860, max Rs 3,000, range Rs 2,140
b) Median Rs 2,080, min Rs 890, max Rs 2,950, range Rs 2,060
c) Median Rs 2,325, min Rs 860, max Rs 3,000, range Rs 2,140
d) Median Rs 2,325, min Rs 860, max Rs 3,000, range Rs 3,860

---

## Step 4. Write it once: `revenue_for(subset)`

The same total is needed for every segment in every quarter, so it moves into a function:

```python
def revenue_for(rows):
    total = 0
    for order in rows:
        total = total + order["amount"]
    ____
```

Run `revenue_for(ORDERS)` and then `revenue_for` on the Q1 rows only, and check the second against
Step 1.

### Checkpoint 5. Anand wants a table of revenue for every segment and quarter, built from `revenue_for`. Which last line makes the function usable in that table?

a) `print(total)`, so the total shows on screen for each call
b) `return total`, so each call hands its number to the table
c) `return print(total)`, so it shows the total and returns it
d) `total`, as the last line, so the notebook displays the value

---

## What you leave with

A dictionary accumulator you can point at any key, one segment described by its typical value and
its spread, and a function that returns its answer. The next step, running the tree on every
segment in both quarters, is yours alone at the end of chapter 3.
