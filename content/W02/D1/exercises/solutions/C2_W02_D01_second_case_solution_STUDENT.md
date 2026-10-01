# Which answers hold in the second case on whether the store is booming and the web collapsing, and why?

Answers: 1d 2a 3c 4b 5b 6d 7c 8c 9a 10b

Marketing read Kalpa Retail's channel totals, the store up 61.1 percent and the web down 37.6 percent,
and asked Anand Iyer, the finance controller, to move budget from the web to the stores. Business
places a few orders worth lakhs each, so the totals mostly show where corporate buyers placed their
orders. The case asks each learner to read the consumers apart: items 1 to 7 are the seven markers of
`notebooks/C2_W02_D01_ex2_second_case_STUDENT.ipynb`, and items 8 to 10 are the brief's design items.
The executed solution, `C2_W02_D01_ex2_second_case_solution_STUDENT.ipynb` in this folder, runs every
marker. Four of the ten items are design items: 7, 8, 9 and 10.

**Who needs the answer.** You and your partner do, when you check your ten letters and your line after
the take-home. The line you send Anand decides where a channel budget goes, and a line that reads the
totals sends it to the channel whose own consumers are leaving.

**The questions on the way.**

- Which idea does the second case test: a total that is two businesses, read apart before it is read whole?
- Which numbers should you have reached, from the channel totals to the app's consumers?
- Why does each of the ten keys hold, from the six channel lines to the consumer tie-out?
- Why is option c in item 2, the Rs 5,00,000 size line, worth arguing about?
- Where does a listed company report its business buyers apart from its consumers?

## Which idea does the second case test: a total that is two businesses, read apart before it is read whole?

A total made of a few very large orders and many small ones is two businesses, and each is read on its
own before the total is. The case asks for the split by the customer's segment, a count of consumers
that counts people, a ratio divided in numeric, and a line that reads the part of the business the
budget is for. The design items size the analysis, choose the route that could disagree with a
consumer number, tie the consumer lines out on the columns that add, and name the fact that would put
the totals back in charge.

## Which numbers should you have reached, from the channel totals to the app's consumers?

| Step | Number | What it means |
|---|---|---|
| 1 | Booked totals, Q1 to Q2: app Rs 4,21,38,840 to Rs 4,25,90,270, up 1.1 percent; store Rs 1,99,59,110 to Rs 3,21,48,730, up 61.1 percent; web Rs 3,79,02,050 to Rs 2,36,61,000, down 37.6 percent | This is the reading Marketing brought to Anand. |
| 2 | Business per channel: app Rs 4,17,78,440 to Rs 4,23,16,600; store Rs 1,96,33,000 to Rs 3,18,84,000; web Rs 3,76,03,000 to Rs 2,33,84,000 | The store's rise and the web's fall are corporate orders moving between channels. |
| 3 | Consumers, Q1 then Q2 (orders, consumers, orders per consumer, revenue): app 161, 111, 1.45, Rs 3,60,400 then 124, 101, 1.23, Rs 2,73,670; store 141, 108, 1.31, Rs 3,26,110 then 127, 99, 1.28, Rs 2,64,730; web 139, 106, 1.31, Rs 2,99,050 then 120, 94, 1.28, Rs 2,77,000 | Every channel's consumers fell. |
| 4 | Consumer revenue, Q1 to Q2: app down 24.1 percent, store down 18.8 percent, web down 7.4 percent | The app is losing its consumers fastest, and the web, the channel Marketing would cut, is losing them slowest. |

A line for Anand that holds: "Consumer revenue fell in every channel, fastest in the app, down 24.1
percent from Rs 3,60,400 to Rs 2,73,670; the store's rise and the web's fall are Business orders moving
between channels."

## Why does each of the ten keys hold, from the six channel lines to the consumer tie-out?

### Q1. Which grouping gives Anand one line per channel and quarter?

Kind: choose the grouping. The key is d, `GROUP BY channel, quarter`: six groups, one per channel and
quarter, whose revenue adds back to the book in each quarter.

- a, `GROUP BY channel`: merges the two quarters, so no change can be read.
- b, `GROUP BY quarter`: merges the channels, which is the book's two lines.
- c, `GROUP BY channel, quarter, status`: splits every line three ways by status, 18 lines where
  Anand asked for six.

### Q8. Which analysis answers Marketing's question, sized in rows?

Kind: a design item, the best-fit analysis with its size. The key is c, "Twelve rows, each channel's
Business and consumer orders apart per quarter, read as changes". Business's orders are worth lakhs and
the consumers' hundreds, so a channel's total moves wherever a few corporate orders land; reading the
two kinds apart is what tells Anand whether the channel's own customers grew. Three channels, two kinds
of order and two quarters make twelve rows, and reading each as a change shows which part of each
channel moved.

- a, "The six channel totals, since the budget follows a channel's revenue": the totals are what
  Marketing already read, and a few corporate orders dominate them.
- b, "Three rows, each channel's half-year revenue, since two quarters of movement cancel out": a
  half-year hides the change the question is about.
- d, "All 1,000 order rows exported, so Marketing can rebuild any total it likes in its own
  spreadsheet": moves the whole book out to answer a question twelve rows answer, which Anand ruled
  out.

### Q2. Which label keeps every Business order on the Business side, next quarter as well as this one?

Kind: choose the definition. The key is a, "Business where the customer's segment is Business,
consumer for the other three". A Business order is an order a corporate buyer places, whatever its
size, and the segment lives on the customer, so a label that follows the customer's segment files
every such order on the Business side this quarter and next; 188 orders carry the Business label, the
Business segment's own.

- b, "The customer's own segment name, four labels in each channel": keeps the four segments apart, so
  each channel has four kinds where the question asks for two.
- c, "Business where the order is worth more than Rs 5,00,000, and consumer where it is not": labels by
  order size, and on this book it files the 50 Business orders worth Rs 2,09,000 to Rs 4,94,000 as
  consumer orders, so only 138 orders carry the Business label against the segment's 188.
- d, "Business where the customer is in Business or Retail-Plus, the segments with larger orders":
  Retail-Plus's orders are larger than Retail-Core's and Student's, and they are still household
  orders; the label puts its 355 orders under Business, 543 in all.

### Q3. Which expression counts each channel's consumers, each once?

Kind: choose the count. The key is c, "`count(DISTINCT o.customer_id)`, since an id stands for one
consumer". It counts each consumer once however many orders they placed, and gives the app 111
consumers in Q1 behind 161 orders.

- a, "`count(*)`, since each consumer order row belongs to a consumer": counts orders, 161.
- b, "`sum(1)`, since adding one per order reaches everyone who bought": adds one per row, 161 again.
- d, "`count(o.customer_id)`, since it counts the customer column rather than rows": counts rows with
  a customer id, which is every row.

### Q4. Which orders-per-consumer figure multiplies back to the orders?

Kind: fix the logic. The key is b, `round(count(*)::numeric / count(DISTINCT o.customer_id), 2)`. The
app's consumers ordered 1.45 times each in Q1 and 1.23 in Q2, and 1.23 times 101 is 124.2, within half
an order of 124.

- a, `count(*) / count(DISTINCT o.customer_id)`: two whole numbers divide as a whole number, so every
  channel reads 1.
- c, `round(count(*) / count(DISTINCT o.customer_id), 2)`: rounds after the whole-number division has
  already dropped the fraction, so every channel reads 1.00.
- d, `round(count(DISTINCT o.customer_id)::numeric / count(*), 2)`: consumers per order, the branch
  upside down.

### Q9. Which route could disagree with the app's consumer revenue if the consumer query were wrong?

Kind: a design item, the independent second route, checked from the amounts on the page. The key is a,
"The app's booked total less the app's Business revenue: Rs 3,60,400 then Rs 2,73,670". Rs 4,21,38,840
less Rs 4,17,78,440 is Rs 3,60,400, and Rs 4,25,90,270 less Rs 4,23,16,600 is Rs 2,73,670. The route
starts from the app's total and the Business label and never reads the consumer query, so a consumer
filter that dropped or doubled orders would leave the two routes apart.

- b, "The consumer query rerun in a fresh session": the same code gives the same numbers, right or
  wrong, so it can only show that the query repeats.
- c, "The app's consumer orders times their revenue per order": revenue per order is the consumer
  query's revenue over its own orders, so the product hands its revenue back.
- d, "The app's consumers times their spend per consumer": spend per consumer is the same revenue over
  the same consumers, so it hands the revenue back too.

### Q5. Which channel lost the largest share of its consumer revenue?

Kind: read the output. The key is b, app: its consumer revenue fell 24.1 percent, against 18.8 for the
store and 7.4 for the web.

- a, web: the web's total fell furthest, 37.6 percent, on Business orders; its consumers fell least.
- c, store: its consumers fell 18.8 percent, less than the app's.
- d, "none, since every channel held its consumers": every channel's consumer revenue fell.

### Q6. Which line goes on Anand's sheet for the store?

Kind: choose the line for the stakeholder. The key is d, "Store consumer revenue fell; the store total
rose on Business orders". It reads the store's consumers, the part a channel budget serves, down 18.8
percent from Rs 3,26,110 to Rs 2,64,730, and names why the total rose: the store's Business revenue
went from Rs 1,96,33,000 to Rs 3,18,84,000.

- a, "Store revenue rose 61.1 percent from Q1 to Q2, so the budget should move to the stores":
  Marketing's reading of the total, which corporate orders carry.
- b, "The store is flat once the Business orders are removed": the store's consumers fell 18.8
  percent, which is no flat line.
- c, "Store consumer revenue rose with its Business orders, so both parts of the store grew": the two
  parts moved in opposite directions, and the total hid the fall.

### Q7. Which fact would move the budget question back to the channel totals?

Kind: a design item, the fact that would switch the reading. The key is c, "If Business chose a
channel for that channel's own service". Then a corporate buyer's move into the stores would say
something about the stores themselves, and the totals, Business included, would be a fair basis for
the budget.

- a, "If the web's consumer orders fell further next quarter": a fact about consumers, which the
  consumer lines already read.
- b, "If Anand asked for the channels in rupees rather than orders": changes the unit, and the totals
  are already in rupees.
- d, "If Business placed its orders through whichever channel its buyer chose on the day": this is the
  reason the totals mislead, since a channel chosen on the day says nothing about the channel.

### Q10. How should the consumer lines be tied out before they reach Anand, sized?

Kind: a design item, the tie-out that fits the columns. The key is b, "Orders and rupees against the
segments' 441 orders and Rs 9,85,560 in Q1, customers left out". The channels' consumer orders, 161,
141 and 139, add to 441, and their revenue, Rs 3,60,400, Rs 3,26,110 and Rs 2,99,050, adds to
Rs 9,85,560. Customers stay out of the addition with a note, because a consumer who bought through two
channels sits in both rows.

- a, "Customers as well, the channels' 325 against the segments' 208 in Q1, since a tie-out adds every
  column": 325 is 111, 108 and 106 added, and it can never reach 208 while consumers use more than one
  channel.
- c, "Revenue alone, since Anand signs rupees and the orders and customers follow from them": orders
  add as well, and tying them out costs one more addition.
- d, "No tie-out, since the channel totals already added back to the book in step 1": the consumer
  lines are new numbers, built with a new label, and need their own check.

## Why is option c in item 2, the Rs 5,00,000 size line, worth arguing about?

A size line sounds like the same split in other words, since every Business order is worth lakhs and
no consumer order reaches Rs 5,000. The line drawn at Rs 5,00,000 is not the segment line, though: it
files 50 Business orders worth Rs 2,09,000 to Rs 4,94,000 as consumer orders. The app's consumer
revenue would then read Rs 18,91,400 in Q1 and Rs 36,76,670 in Q2, up 94.4 percent, and the store's
would read Rs 35,53,110 then Rs 17,28,730, down 51.3 percent: the app would look like the channel
winning consumers, when its consumers fell fastest. The notebook's check catches it, 138 orders under
the Business label against the segment's 188. A label that follows the customer's segment means the
same thing whatever the orders look like next quarter.

## Where does a listed company report its business buyers apart from its consumers?

Eternal, the company behind Zomato and Blinkit, defines its headline B2C net order value over its
consumer-facing businesses, food delivery, quick commerce and going-out, and reports Hyperpure, its
supplies business for restaurants and other businesses, as a segment of its own, B2B (shareholders'
letter for Q1 FY27, 22 July 2026, pages 3 and 26). Kalpa's channel sheet makes the same cut on a smaller book: the
Business segment's orders on one line, the consumers' on another.
