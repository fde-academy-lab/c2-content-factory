# Which answers hold in the practice lab on the day's moves in new questions, and why?

Answers: 1c 2a 3d 4b 5a 6c 7b 8d 9a

The practice lab ran the day's moves on questions the chapters did not ask: four shapes to predict on
Kalpa's warehouse, 1,000 orders and 340 customers in six cities; five asks to give an owner among
plain Python, SQL and pandas; a most-used channel per customer; and the head of Retail-Plus's own
table. The growth team's table counts recency to 28 September 2026, the data's last date, and the
campaign platform's feed counts a customer it names twice once, on the first date. Kavya Nair, the
senior analyst, reviews every table and tool choice. Problems 3 and 4 have no letters; their numbers
are below.

**Who needs the answer.** You and the TA, at the end of the lab. A shape you could not predict is a
table you would have trusted without reading, and a column that guesses without saying so sends an
offer down a channel nobody chose.

**The questions on the way.**

- Which idea does the lab test?
- Why does each of the nine keys hold, from customers per city to the 40 emailed ids?
- Which numbers should problem 3 reach, and what rule goes to the growth team?
- Which numbers should problem 4 reach, and what line goes to the head of Retail-Plus?
- Why is option d in item 9, a permanent table for 40 ids, the wrong answer worth arguing about?

## Which idea does the lab test?

The day's moves transfer: the rows of a result come from its keys, a reshape's cells hold what its
`aggfunc` says, a number belongs to the tool its rerunner can run, and a column that picks one value
per row has to say what it does when no single value wins.

## Why does each of the nine keys hold, from customers per city to the 40 emailed ids?

### Q1. How many rows does a count of customers per city return?

The key is c, "6 rows, one per city". `groupby` makes one group per distinct key, and Kalpa's
customers live in six cities.

- a, "340 rows, one per customer": `size` collapses each group to one row.
- b, "4 rows, one per segment": the segment is a different column.
- d, "301 rows, one per customer who ordered": the customer list holds everyone, buyers or not.

### Q2. How many rows does a count per customer and quarter return?

The key is a, "471 rows, one per customer and quarter that has orders". A group exists only for a
pair that appears in the rows, so a customer who ordered in one quarter has one row.

- b, "602 rows, the 301 customers who ordered times 2 quarters": assumes every customer ordered in
  both quarters.
- c, "680 rows, every customer on the list times 2 quarters": a group needs a row to exist.
- d, "1,000 rows, one per order, each in its quarter": `size` collapses each pair's orders to one row.

### Q3. What shape is revenue by channel with the two quarters side by side?

The key is d, "3 by 2, a channel per row and a quarter per column". The index decides the rows and
the columns argument the columns.

- a, "2 by 3, a quarter per row and a channel per column": the transpose.
- b, "6 by 1, one row per channel and quarter": the long shape a `groupby` on both keys gives.
- c, "1,000 by 2, the quarters written onto each order": a pivot folds the orders into its cells.

### Q4. What shape is each customer's first and last order date?

The key is b, "301 by 2, one row per customer who ordered". Built from the orders, the result knows
only the customers who placed one.

- a, "340 by 2, one row per customer on the list": the 39 who never ordered have no group.
- c, "2 by 301, one row per measure": each named aggregate becomes a column.
- d, "1,000 by 2, the dates written onto each order": that is a `transform`, which this is not.

### Q5. Which tool should compute the head of Retail-Plus's protect list, refreshed weekly and read by three teams?

The key is a, "SQL, a query in the warehouse that every team reads". Three teams reading one list
need one definition where all three can run it.

- b, "pandas, a notebook the analyst reruns and emails each week": three copies of an email, each
  ageing from the moment it is sent.
- c, "Plain Python, a script with the ranking written out as a loop": a weekly ranking read by three
  teams is not a line-by-line explanation.
- d, "pandas, a CSV the analyst writes to a shared folder weekly": a copy that ages, and a list that
  depends on one analyst's machine.

### Q6. Which tool should answer how many customers a 45-day win-back line would hold, asked once in a meeting?

The key is c, "pandas, the customer table in memory and one changed number". The question is asked
once, the table is already built, and the answer is one changed threshold away: 144 at 45 days
against 111 at 60.

- a, "SQL, a new view in the warehouse for the 45-day list": a permanent object for a question asked
  once.
- b, "Plain Python, a loop over the customer table's rows": works, and is slower to write than one
  comparison on a column.
- d, "SQL, the win-back query mailed to the platform lead to rerun": moves a one-minute question to
  someone else's queue.

### Q7. Which tool should explain to a reviewer, step by step, why the win-back list holds 111 and not 166?

The key is b, "Plain Python, both recency counts side by side, dates printed". The reviewer
needs to see one customer's last order, the two dates it was counted to, and the two results.

- a, "SQL, two queries whose counts differ by 55, run one after the other": shows the two totals and
  hides the step that differs.
- c, "pandas, two chained calls on the table with both counts shown": the counts are there, and the
  chain hides the dates each was counted to.
- d, "SQL, one query with the two counts in two columns": the same totals in one place.

### Q8. Which tool should hold the monthly revenue by segment that Finance reconciles against its books?

The key is d, "SQL, a view defined in the warehouse". Finance reconciles from the warehouse, and a
view holds the definition where Finance's analyst can rerun it.

- a, "pandas, a notebook with its outputs saved for Finance to read": a copy, on one machine, that
  Finance cannot rerun.
- b, "Plain Python, a script that prints the table to the terminal": nothing for Finance to rerun
  against its books.
- c, "pandas, a CSV sent to Finance on the first of each month": a copy that ages from the moment it
  is written.

### Q9. Which tool should match a one-off list of 40 customer ids, emailed by the head of Retail-Plus, to the customer table this afternoon?

The key is a, "pandas, the 40 ids as a frame merged with `validate`". The table
lives in pandas, the list is small and arrives once, and `validate` stops the merge if the email
repeats an id.

- b, "SQL, once the platform lead loads the list into a warehouse table": a one-afternoon question
  waits in another team's queue.
- c, "Plain Python, a loop that searches the table for each id in turn": works, and checks nothing
  about repeated ids.
- d, "SQL, a new permanent table of the 40 ids in the warehouse": a permanent object in a shared
  warehouse for one afternoon's list, which is the platform lead's to create.

## Which numbers should problem 3 reach, and what rule goes to the growth team?

| Measure | Number | What it means |
|---|---|---|
| Rows | 340 | One per customer on the list |
| Orders in the cells | 1,000 | The pivot counted every order once |
| Customers who ordered | 301 | The rest have 0 in every channel |
| Customers who ordered with a tie for most-used channel | 98 | `idxmax` returns the first column in the tie, `app` |
| Customers with no orders | 39 | `idxmax` on a row of zeros returns `app` as well |
| Rows where the column is a guess | 137 | 98 ties and 39 empty rows |

Among the 301 who ordered, `idxmax` names the app for 149, the store for 92 and the web for 60, and
the app's lead is mostly ties broken by column order: with ties set aside, the counts are 77, 66 and
60. A rule the growth team can use: name a channel only when it leads outright, write "mixed" for a
tie and "none" for a customer with no orders, and send those offers by the growth team's default
channel. Any rule works if it is written down; a tie broken by the columns' alphabetical order, with nobody told, does not.

## Which numbers should problem 4 reach, and what line goes to the head of Retail-Plus?

| Measure | Number |
|---|---|
| Rows | 120, every Retail-Plus member on the list |
| Spend | Rs 9,99,150: Q1 Rs 5,85,770 and Q2 Rs 4,13,380, matching the warehouse |
| Reached by the sale | 60, once each under the growth team's rule |
| Reached members who spent less in Q2 than in Q1 | 33 of 60 |
| Members the sale did not reach who spent less in Q2 | 34 of 60 |
| Smallest recency | 0 days, counted to 28 September 2026 |
| Members lapsed on the 60-day line | 47 |

A line that holds: "Of the 60 members the monsoon sale reached, 33 spent less in Q2 than in Q1; of
the 60 it did not reach, 34 did. The table records whom the sale reached, and whether it changed
what they spent needs a fair comparison, which a group held out of the next sale would give." The
line names both groups, keeps the counts beside each other, and makes no claim about cause.

## Why is option d in item 9, a permanent table for 40 ids, the wrong answer worth arguing about?

Item 9, option d sounds like the warehouse-first habit the day built: SQL for anything that should
be rerun. A one-off list is not rerun, and a permanent table in the shared warehouse is the data
platform lead's to create. The habit is to put a number where its rerunner can run it, and a list
nobody reruns belongs on the analyst's bench.
