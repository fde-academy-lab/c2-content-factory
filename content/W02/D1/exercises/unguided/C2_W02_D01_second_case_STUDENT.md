# Which channel is losing Kalpa's consumers, once the Business orders are read apart?

The second case, in the take-home, in pairs or alone. You work in
`notebooks/C2_W02_D01_ex2_second_case_STUDENT.ipynb`, and this brief carries everything the case
needs, so it can be read with nothing else open. Items 1 to 7 are the notebook's seven lettered
markers, with the same numbers and the same letters. Items 8 to 10 are this brief's own design items,
answered here.

> "The same numbers for every channel: app, web and store. Marketing says the store is booming and the
> web is collapsing, and wants the budget moved. Is that what the book says?"
>
> Anand Iyer, finance controller, Kalpa Retail

Kalpa Retail sells through three channels: its app, its website and its stores. Booked revenue, every
order at its amount whatever its status, was Rs 10,00,00,000 in Q1 (April to June 2026) and
Rs 9,84,00,000 in Q2 (July to September 2026). Business, the corporate segment, books about 99 percent
of those rupees in orders worth lakhs each. The other three segments, Retail-Core, Retail-Plus and
Student, are Kalpa's consumers, whose orders are worth hundreds or a few thousand rupees. Marketing read
the channel totals and wants budget moved from the web to the stores.

The book is Kalpa's Postgres warehouse: `orders` (1,000 rows: order_id, customer_id, order_date,
quarter, channel, amount, status) and `customers` (340 rows, one per member: customer_id, segment,
city, country, joined_date). The channel is a column of the orders table; the segment is looked up with
`JOIN customers c USING (customer_id)`, which finds each order's one customer and changes no row count.
Customers who bought are counted once in a group, however many orders they placed, and orders per
customer is a group's orders divided by those customers. A channel's consumer tree splits its consumer
revenue into consumers who bought, orders per consumer and revenue per order, which multiply back to
it. A tie-out adds a set of parts and sets the sum beside the whole it should make. A change is Q2 over
Q1, less one, in percent.

| Channel | Q1 orders | Q1 booked revenue | Q2 orders | Q2 booked revenue |
|---|---|---|---|---|
| app | 192 | Rs 4,21,38,840 | 153 | Rs 4,25,90,270 |
| store | 165 | Rs 1,99,59,110 | 159 | Rs 3,21,48,730 |
| web | 181 | Rs 3,79,02,050 | 150 | Rs 2,36,61,000 |

**Who needs the answer.** Anand decides whether to back Marketing's request, and the channel heads
will live with the budget it moves. A budget moved on totals that a few corporate orders dominate goes
to a channel whose own consumers may be the ones leaving.

**The questions on the way.**

- What do the channel totals say from Q1 to Q2?
- How much of each channel is Business, and how much is consumers?
- How did each channel's consumers move, branch by branch?
- Which line goes on Anand's channel sheet?

**What you post.** One line of ten letters in item order, no spaces, items 1 to 7 from the notebook's
markers and items 8 to 10 from this brief, in this shape:

```
Post exactly this shape: xxxxxxxxxx
```

Beside the letters, post one line for Anand that names the channel losing its consumers fastest, with
its number.

---

## Step 1. What do the channel totals say from Q1 to Q2?

Used at work whenever a channel manager's budget follows the channel's total, since the total is the
first number anyone reads.

Marker 1 in the notebook, then item 8 here.

### Q1. Which grouping gives Anand one line per channel and quarter?

Anand wants one line per channel and quarter, six lines in all. Which grouping gives the analyst
exactly those lines?

a) `GROUP BY channel, quarter`
b) `GROUP BY channel`
c) `GROUP BY quarter`
d) `GROUP BY customer_id, channel`

### Q8. Which analysis answers Marketing's question, sized in rows?

Marketing's question is whether a channel is losing its consumers. Kalpa has three channels, and every
order is either a Business order or a consumer order. Which analysis answers the question, sized in
rows?

a) The six channel totals, since the budget follows a channel's revenue
b) Twelve rows, each channel's Business and consumer orders apart per quarter, read as changes
c) Three rows, each channel's half-year revenue, since two quarters of movement cancel out
d) All 1,000 order rows exported, so Marketing can check the split for itself in its own spreadsheet

## Step 2. How much of each channel is Business, and how much is consumers?

Used at work whenever a total is made of a few very large orders and many small ones, since each part
is read on its own before the total is.

Marker 2 in the notebook.

### Q2. Which label splits each channel's orders into Business and consumer the way Anand's segments do?

The notebook labels every order as Business or consumer and groups by the label. Which label splits the
orders the way Anand's segments do?

a) The customer's own segment name, four labels in each channel
b) Business where the customer's segment is Business, consumer for the other three
c) Business where the order is worth more than Rs 5,00,000, and consumer where it is not
d) A filter that drops the Business customers' orders before anything is grouped

## Step 3. How did each channel's consumers move, branch by branch?

Used at work whenever a channel's consumer health is read as its tree, consumers times orders each
times revenue per order, each as a change.

Markers 3 and 4 in the notebook, then item 9 here.

### Q3. Which expression counts each channel's consumers, each once?

The consumer tree needs each channel's consumers who bought in a quarter, each counted once. Which
expression counts them?

a) `count(*)`, since each consumer order row belongs to a consumer
b) `sum(1)`, since adding one per order reaches everyone who bought
c) `count(DISTINCT o.customer_id)`, one per consumer however many rows
d) `count(o.customer_id)`, since it counts the customer column rather than rows

### Q4. Which orders-per-consumer figure multiplies back to the orders?

The analyst multiplies every orders-per-consumer figure back to its orders. Which expression gives a
figure that survives her check?

a) `count(*) / count(DISTINCT o.customer_id)`
b) `round(count(*) / count(DISTINCT o.customer_id), 2)`
c) `round(count(DISTINCT o.customer_id)::numeric / count(*), 2)`
d) `round(count(*)::numeric / count(DISTINCT o.customer_id), 2)`

### Q9. What does the app's consumer revenue come to by a route that uses no consumer filter?

Kavya Nair, the team's senior analyst, wants the app's consumer revenue confirmed by a route that
shares no code with the consumer query: the app's booked total less the app's Business revenue. The
app's Business revenue was Rs 4,17,78,440 in Q1 and Rs 4,23,16,600 in Q2, and its totals are in the
table at the top of this brief. What does the route give?

a) Rs 3,60,400 then Rs 2,73,670, down 24.1 percent
b) Rs 3,60,400 then Rs 2,73,670, down 31.7 percent
c) Rs 4,21,38,840 then Rs 4,25,90,270, up 1.1 percent
d) Rs 4,17,78,440 then Rs 4,23,16,600, up 1.3 percent

## Step 4. Which line goes on Anand's channel sheet?

Used at work whenever a budget is about to move on one line of a report.

Markers 5 to 7 in the notebook, then item 10 here.

### Q5. Which channel lost the largest share of its consumer revenue?

Reading each channel's consumer revenue as a change from Q1 to Q2, which channel lost the largest
share of it?

a) web
b) store
c) none, since every channel held its consumers
d) app

### Q6. Which line goes on Anand's sheet for the store?

Which line goes on Anand's sheet for the store?

a) Store revenue rose 61.1 percent from Q1 to Q2, so the budget should move to the stores.
b) Store consumer revenue fell 18.8 percent; the store total rose on Business orders.
c) The store is flat once the Business orders are removed.
d) Store revenue cannot be reported until Business is removed from the book.

### Q7. Which fact would move the budget question back to the channel totals?

Which fact, if it held, would make the channel totals, Business orders included, the right basis for
the budget?

a) If the web's consumer orders fell further next quarter
b) If Anand asked for the channels in rupees rather than orders
c) If Business placed its orders through whichever channel its buyer chose on the day
d) If Business chose a channel for that channel's own service

### Q10. How should the consumer lines be tied out before they reach Anand, sized?

In Q1 the three consumer segments together placed 441 orders worth Rs 9,85,560, from 208 customers who
bought. The consumer lines per channel will sit on Anand's sheet beside that total. How should they be
tied out before they reach him?

a) Customers as well, the channels' 325 against the segments' 208 in Q1, since a tie-out adds every column
b) Revenue alone, since Anand signs rupees and the orders and customers follow from them
c) Orders and rupees against the segments' 441 orders and Rs 9,85,560 in Q1, customers left out
d) No tie-out, since the channel totals already added back to the book in step 1

## Which rules does the case keep?

- The data is the warehouse's orders and customers tables, read where they live; nothing is exported.
- Every number in your line for Anand says which part of the business it reads: the total, Business,
  or the consumers.
- Every ratio goes on the sheet with its two counts beside it.
- Work in pairs or alone; if you pair, both names go on the post and each of you can explain every
  letter.
