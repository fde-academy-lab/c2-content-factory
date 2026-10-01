# Solution: How do you total any group of Kalpa's orders, describe it, and write the total once for every segment and quarter?

Answers: 1d 2b 3a 4c 5b

The guided exercise builds, with the trainer, the grouping that every later number of the day rests
on. Kalpa Retail's class file holds 200 orders from Q1 and Q2, each a record with its quarter, its
amount in rupees, its customer id and its segment, the kind of customer who placed it, and revenue
is booked revenue, every order placed at the price charged before any cancellation or return. Anand
Iyer, the finance controller, wants orders and revenue for every segment in every quarter, and Meera
Raghavan, the CEO, reads the day's answer off that table.

## What does the guided exercise test?

Grouping is one move repeated: a dictionary keyed by the thing you want to compare, updated once per
record. Describing a group needs its typical value and its spread, read off a sorted list. The moment
the same total is needed twice, it belongs in a function that returns it, because a function that
only prints cannot feed a table.

## Which answer holds at each checkpoint, and why?

### Checkpoint 1. What does `orders_by_quarter` hold after the loop?

Anand asks how many orders each quarter booked, and the loop adds one to its quarter's count for
every order.

The key is d, "`{"Q1": 114, "Q2": 86}`, one count for each order booked". One count per order,
grouped by quarter, gives 114 in Q1 and 86 in Q2.

- a, "`{"Q1": 1, "Q2": 1}`, one count the first time each quarter appears": it reads the two
  additions as part of the `if` block, which runs only the first time a quarter appears. They sit
  level with the `if`, so they run for every order.
- b, "`{"Q2": 1}`, since the dictionary is reset on every order": that is what a dictionary created
  inside the loop would leave, and this one is created above it.
- c, "`{"Q1": 200, "Q2": 200}`, since every order is counted twice": each order passes through the
  loop once, and no quarter holds the whole file.

### Checkpoint 2. What does `revenue_by_quarter` hold after the loop?

The same loop adds each order's amount into its quarter's revenue.

The key is b, "Rs 2,10,00,000 in Q1 and Rs 1,87,00,000 in Q2, the booked revenue". Summing the
amounts per quarter gives Rs 2,10,00,000 and Rs 1,87,00,000.

- a, "Rs 1,84,211 in Q1 and Rs 2,17,442 in Q2, the revenue per order": that is revenue per order, a
  rate, which divides the totals by the orders.
- c, "Rs 3,97,00,000 in Q1 and Rs 3,97,00,000 in Q2, the file's revenue": that is the whole file,
  which no single quarter holds.
- d, "Rs 2,10,00,000 in Q1 and Rs 2,10,00,000 in Q2, the first quarter's": it gives Q2 the first
  quarter's total, which happens only when the key is ignored.

### Checkpoint 3. How many keys should `orders_by_key` hold before you read a single count?

Step 2 keys the same loop by quarter and segment together, and the keys are counted before any
count is read.

The key is a, "Eight, four segments in each of two quarters; fewer means a group is lost". Four
segments times two quarters is eight keys, and counting the keys before reading the values catches
a segment missing from one quarter.

- b, "Four, one per segment; the quarter is a column that the key leaves out": a key without the
  quarter mixes two quarters into one count.
- c, "Two hundred, one key per order; a dictionary keeps every row it is given": a dictionary holds
  one entry per key, however many rows share it.
- d, "Sixty-nine, one per customer; a customer is the unit Meera is asking about": that keys by
  customer, which is a different split.

### Checkpoint 4. What are the median, minimum, maximum and range of Retail-Core's Q1 orders?

Retail-Core's 38 Q1 amounts, sorted, are described by their median, minimum, maximum and range.

The key is c, "Median Rs 2,325, min Rs 860, max Rs 3,000, range Rs 2,140". Sorted, the 38 amounts
run from Rs 860 to Rs 3,000, the middle two average Rs 2,325, and the range is Rs 3,000 less Rs 860,
which is Rs 2,140.

- a, "Median Rs 2,117, min Rs 860, max Rs 3,000, range Rs 2,140": it puts the mean, Rs 2,117, in the
  median's place.
- b, "Median Rs 2,080, min Rs 890, max Rs 2,950, range Rs 2,060": those are Retail-Core's figures
  for Q2.
- d, "Median Rs 2,325, min Rs 860, max Rs 3,000, range Rs 3,860": it adds the minimum to the maximum
  where the range subtracts it.

### Checkpoint 5. Which last line lets `revenue_for` feed Anand's table?

Anand wants a table of revenue for every segment and quarter, built by calling `revenue_for` once
for each group.

The key is b, "`return total`, so each call hands its number to the table". `return total` hands the
value to whatever called the function, so a loop can store it in a table.

- a, "`print(total)`, so the total shows on screen for each call": it prints the total and returns
  None, so the table fills with blanks.
- c, "`return print(total)`, so it shows the total and returns it": it returns what `print` returns,
  which is None.
- d, "`total`, as the last line, so the notebook displays the value": a bare expression inside a
  function displays nothing and leaves the function returning None.

## Which checkpoint is worth arguing about?

Checkpoint 3. Counting the keys feels like a formality, and it is the cheapest check in the day. A
segment that bought nothing in one quarter produces no key at all, and a table built from the
dictionary then has seven rows while nobody notices the missing one. The same count, groups in
against groups out, comes back later in the day.

## Where does this pattern live in production?

Every `GROUP BY` in SQL and every `groupby` in pandas is this accumulator with the loop hidden, and
the programme meets both later. The habit of counting groups before reading them is what catches a
step that lost a segment without a word, whatever the tool.
