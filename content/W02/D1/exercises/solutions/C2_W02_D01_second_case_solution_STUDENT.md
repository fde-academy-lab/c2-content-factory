# Which answers hold in the second case on which channel is losing Kalpa's consumers, and why?

Answers: 1a 2b 3c 4d 5d 6b 7d 8b 9a 10c

Marketing read Kalpa Retail's channel totals, the store up 61.1 percent and the web down 37.6 percent,
and asked Anand Iyer, the finance controller, to move budget from the web to the stores. Business books
about 99 percent of the rupees in a few large orders, so the totals mostly show where corporate buyers
placed their orders. The case asks each learner to read the consumers apart: items 1 to 7 are the seven
markers of `notebooks/C2_W02_D01_ex2_second_case_STUDENT.ipynb`, and items 8 to 10 are the brief's
design items. The executed solution, `C2_W02_D01_ex2_second_case_solution_STUDENT.ipynb` in this
folder, runs every marker. Four of the ten items are design items: 7, 8, 9 and 10.

**Who needs the answer.** You and your partner, after the take-home, checking ten letters and one line.
The line you send Anand decides where a channel budget goes, and a line that reads the totals sends it
to the channel whose own consumers are leaving.

**The questions on the way.**

- Which idea does this case test?
- Which numbers should you have reached, step by step?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this case test?

A total made of a few very large orders and many small ones is two businesses, and each is read on its
own before the total is. The case asks for the split by the customer's segment, a count of consumers
that counts people, a ratio divided in numeric, and a line that reads the part of the business the
budget is for. The design items size the analysis, confirm a consumer number by a route that avoids the
consumer filter, tie the consumer lines out on the columns that add, and name the fact that would put
the totals back in charge.

## Which numbers should you have reached, step by step?

| Step | Number | What it means |
|---|---|---|
| 1 | Booked totals, Q1 to Q2: app Rs 4,21,38,840 to Rs 4,25,90,270, up 1.1 percent; store Rs 1,99,59,110 to Rs 3,21,48,730, up 61.1 percent; web Rs 3,79,02,050 to Rs 2,36,61,000, down 37.6 percent | This is the reading Marketing brought to Anand. |
| 2 | Business per channel: app Rs 4,17,78,440 to Rs 4,23,16,600; store Rs 1,96,33,000 to Rs 3,18,84,000; web Rs 3,76,03,000 to Rs 2,33,84,000 | The store's rise and the web's fall are corporate orders moving between channels. |
| 3 | Consumers, Q1 then Q2 (orders, consumers, orders per consumer, revenue): app 161, 111, 1.45, Rs 3,60,400 then 124, 101, 1.23, Rs 2,73,670; store 141, 108, 1.31, Rs 3,26,110 then 127, 99, 1.28, Rs 2,64,730; web 139, 106, 1.31, Rs 2,99,050 then 120, 94, 1.28, Rs 2,77,000 | Every channel's consumers fell. |
| 4 | Consumer revenue, Q1 to Q2: app down 24.1 percent, store down 18.8 percent, web down 7.4 percent | The app is losing its consumers fastest, and the web, the channel Marketing would cut, is losing them slowest. |

A line for Anand that holds: "Consumer revenue fell in every channel, fastest in the app, down 24.1
percent from Rs 3,60,400 to Rs 2,73,670; the store's rise and the web's fall are Business orders moving
between channels."

## Why is each key right, item by item?

### Q1. Which grouping gives Anand one line per channel and quarter?

Kind: choose the grouping. The key is a, `GROUP BY channel, quarter`: six groups, one per channel and
quarter, whose revenue adds back to the book in each quarter.

- b, `GROUP BY channel`: merges the two quarters, so no change can be read.
- c, `GROUP BY quarter`: merges the channels, which is the book's two lines.
- d, `GROUP BY customer_id, channel`: one line per customer and channel, hundreds of them.

### Q8. Which analysis answers Marketing's question, sized in rows?

Kind: a design item, the best-fit analysis with its size. The key is b, "Twelve rows, each channel's
Business and consumer orders apart per quarter, read as changes". Three channels, two kinds of order
and two quarters make twelve rows, and reading each as a change shows which part of each channel moved.

- a, "The six channel totals, since the budget follows a channel's revenue": the totals are what
  Marketing already read, and a few corporate orders dominate them.
- c, "Three rows, each channel's half-year revenue, since two quarters of movement cancel out": a
  half-year hides the change the question is about.
- d, "All 1,000 order rows exported, so Marketing can check the split for itself in its own
  spreadsheet": moves the whole book out to answer a question twelve rows answer, which Anand ruled
  out.

### Q2. Which label splits each channel's orders into Business and consumer the way Anand's segments do?

Kind: choose the definition. The key is b, "Business where the customer's segment is Business,
consumer for the other three". Anand's segments live on the customer, so the label follows the
customer's segment, with the three consumer segments under one label.

- a, "The customer's own segment name, four labels in each channel": keeps the four segments apart,
  so each channel has four kinds where the question asks for two.
- c, "Business where the order is worth more than Rs 5,00,000, and consumer where it is not": labels
  by order size, and a round threshold picked by eye. On this book it calls 50 of the 188 Business
  orders consumer ones, every Business order from Rs 2,09,000 to Rs 5,00,000, so each channel's consumer
  line swells with corporate rupees. The segment is the definition Anand's sheet already uses.
- d, "A filter that drops the Business customers' orders before anything is grouped": removes
  Business, so the split the step asks for is lost.

### Q3. Which expression counts each channel's consumers, each once?

Kind: choose the count. The key is c, "`count(DISTINCT o.customer_id)`, one per consumer however many
rows". It gives the app 111 consumers in Q1 behind 161 orders.

- a, "`count(*)`, since each consumer order row belongs to a consumer": counts orders, 161.
- b, "`sum(1)`, since adding one per order reaches everyone who bought": adds one per row, 161 again.
- d, "`count(o.customer_id)`, since it counts the customer column rather than rows": counts rows with
  a customer id, which is every row.

### Q4. Which orders-per-consumer figure multiplies back to the orders?

Kind: fix the logic. The key is d, `round(count(*)::numeric / count(DISTINCT o.customer_id), 2)`. The
app's consumers ordered 1.45 times each in Q1 and 1.23 in Q2, and 1.23 times 101 is 124.2, within half
an order of 124.

- a, `count(*) / count(DISTINCT o.customer_id)`: two whole numbers divide as a whole number, so every
  channel reads 1.
- b, `round(count(*) / count(DISTINCT o.customer_id), 2)`: rounds after the whole-number division has
  already dropped the fraction, so every channel reads 1.00.
- c, `round(count(DISTINCT o.customer_id)::numeric / count(*), 2)`: consumers per order, the branch
  upside down.

### Q9. What does the app's consumer revenue come to by a route that uses no consumer filter?

Kind: a design item, the independent second route, computed. The key is a, "Rs 3,60,400 then
Rs 2,73,670, down 24.1 percent". Rs 4,21,38,840 less Rs 4,17,78,440 is Rs 3,60,400, and Rs 4,25,90,270
less Rs 4,23,16,600 is Rs 2,73,670, the same as the consumer query; the fall of Rs 86,730 over Q1's
Rs 3,60,400 is 24.1 percent.

- b, "Rs 3,60,400 then Rs 2,73,670, down 31.7 percent": divides the fall by Q2's revenue, where a
  change is measured from Q1.
- c, "Rs 4,21,38,840 then Rs 4,25,90,270, up 1.1 percent": the app's totals, with Business still in
  them.
- d, "Rs 4,17,78,440 then Rs 4,23,16,600, up 1.3 percent": the app's Business revenue, the part the
  route subtracts.

### Q5. Which channel lost the largest share of its consumer revenue?

Kind: read the output. The key is d, app: its consumer revenue fell 24.1 percent, against 18.8 for the
store and 7.4 for the web.

- a, web: the web's total fell furthest, 37.6 percent, on Business orders; its consumers fell least.
- b, store: its consumers fell 18.8 percent, less than the app's.
- c, "none, since every channel held its consumers": every channel's consumer revenue fell.

### Q6. Which line goes on Anand's sheet for the store?

Kind: choose the line for the stakeholder. The key is b, "Store consumer revenue fell 18.8 percent;
the store total rose on Business orders". It reads the store's consumers, the part a channel budget
serves, and names why the total rose: the store's Business revenue went from Rs 1,96,33,000 to
Rs 3,18,84,000.

- a, "Store revenue rose 61.1 percent from Q1 to Q2, so the budget should move to the stores":
  Marketing's reading of the total, which corporate orders carry.
- c, "The store is flat once the Business orders are removed": the store's consumers fell 18.8
  percent, which is no flat line.
- d, "Store revenue cannot be reported until Business is removed from the book": the book can report
  both parts side by side, and should.

### Q7. Which fact would move the budget question back to the channel totals?

Kind: a design item, the fact that would switch the reading. The key is d, "If Business chose a
channel for that channel's own service". Then a corporate buyer's move into the stores would say
something about the stores themselves, and the totals, Business included, would be a fair basis for
the budget.

- a, "If the web's consumer orders fell further next quarter": a fact about consumers, which the
  consumer lines already read.
- b, "If Anand asked for the channels in rupees rather than orders": changes the unit, and the totals
  are already in rupees.
- c, "If Business placed its orders through whichever channel its buyer chose on the day": this is the
  reason the totals mislead, since a channel chosen at random says nothing about the channel.

### Q10. How should the consumer lines be tied out before they reach Anand, sized?

Kind: a design item, the tie-out that fits the columns. The key is c, "Orders and rupees against the
segments' 441 orders and Rs 9,85,560 in Q1, customers left out". The channels' consumer orders, 161,
141 and 139, add to 441, and their revenue, Rs 3,60,400, Rs 3,26,110 and Rs 2,99,050, adds to
Rs 9,85,560. Customers stay out of the addition with a note, because a consumer who bought through two
channels sits in both rows.

- a, "Customers as well, the channels' 325 against the segments' 208 in Q1, since a tie-out adds every
  column": 325 is 111, 108 and 106 added, and it can never reach 208 while consumers use more than one
  channel.
- b, "Revenue alone, since Anand signs rupees and the orders and customers follow from them": orders
  add as well, and tying them out costs one more addition.
- d, "No tie-out, since the channel totals already added back to the book in step 1": the consumer
  lines are new numbers, built with a new label, and need their own check.

## Which wrong answer is worth arguing about?

Item 2, option c. On this book the size line and the segment line split the orders identically, so a
learner who chose c got every later number right and will say so. The argument is about next quarter.
A label that follows the customer's segment keeps meaning the same thing whatever the orders look like;
a label that follows order size changes meaning the day a corporate buyer places a small order or a
household places a large one, and nothing in the suite would say it had.

## Where does this show up at work?

Any business that sells to companies and to households through the same channels meets this: a
handful of corporate orders can move a channel's total more than every household order combined.
Channel reviews that read the two apart before the total, and say which part a budget is for, are the
ones that move money to where it does some good.
