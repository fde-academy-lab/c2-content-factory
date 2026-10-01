# Will next Monday's run give Anand's analyst the same answer from the same book?

Chapter 6 set, six items. Items 1 and 2 run live in chapter 6's last minutes if the chapter ran to
time; items 3 to 6 are the practice lab's stretch or tonight's work.

> "I want these numbers every Monday, for every segment and channel, computed from the warehouse
> itself. No notebooks, no exports, nothing a person can mistype."
>
> Anand Iyer, finance controller, Kalpa Retail

Anand Iyer's analyst reruns Kalpa Retail's Monday suite every week and traces a short list of orders
against the ERP, the system Finance books orders in. The book is the warehouse's two quarters of
orders, Q1 (April to June 2026) and Q2 (July to September 2026). A fingerprint is a block of numbers
that describes the book itself, printed beside a suite's results so a reader can tell whether the
book changed between two runs; a fingerprint of this book in seven numbers reads as below. An overnight
reload is the platform's nightly job that rewrites rows of the book, sometimes with the values they
already had. `ORDER BY` sorts a query's result, and `LIMIT 5` keeps five rows of it. A snapshot copies
each Monday's results into a table, which needs the right to write to the warehouse. Write, audit,
publish is a way of running a job: the run writes its results to a staging table first, the checks run
there, and only a run that passes is published; it needs write access and a scheduler.

| The fingerprint's seven numbers | This Monday |
|---|---|
| Rows in orders | 1,000 |
| Rupees in orders | Rs 19,84,00,000 |
| Distinct customers in orders | 301 |
| Latest order date | 2026-09-28 |
| Rows in customers | 340 |
| Distinct customers in customers | 340 |
| Latest joining date | 2025-12-25 |

**Who needs the answer.** Anand's analyst decides each Monday whether the suite can be signed. When two
runs disagree, she needs to know whether the book moved or the query did, and a sample that changes on
a rerun makes every number beside it suspect.

**The questions on the way.**

- Which way tells a changed book from a changed query on read access, sized over a quarter of Mondays?
- Which way would have stopped two bad runs before Anand read them, once the team can write and schedule?
- Which change to the book would the seven-number fingerprint miss?
- What most likely explains a traced sample that changed overnight while the fingerprint did not?
- Which route confirms the five cancelled store orders without trusting the database's ordering?
- Which line tells Anand what the Monday suite found?

**What you post.** One line of six letters in item order, no spaces, in this shape:

```
Post exactly this shape: xxxxxx
```

---

## How can a run prove it repeated?

Used at work whenever a scheduled report must show that a change in its numbers is real.

### Q1. Which way tells a changed book from a changed query on read access, sized over a quarter of Mondays?

Anand's analyst wants each Monday's run to show whether a difference from last week came from the book
or from the query. The team has read access only. The suite's outputs come to 18 rows each Monday: the
book's 2 quarter rows, 8 segment-quarter rows, 4 branch rows and 4 half-year rows, and a quarter holds
13 Mondays. Which way fits, sized in what it adds over the quarter?

a) Rerun the suite and compare it with last week's by eye: nothing stored, and a difference names neither cause
b) Snapshot the outputs into a table: 234 rows stored over 13 Mondays, naming which output moved
c) A fingerprint block: 7 numbers printed with each run and nothing stored; a changed one means the book moved
d) Write, audit, publish: 13 staging tables over the quarter, and a bad run stopped before Anand reads it

### Q2. Which way would have stopped two bad runs before Anand read them, once the team can write and schedule?

Three months on, the platform lead grants the team a schema it can write to and a scheduler. The two
bad runs in this item are invented. In one, a reload left a day's amounts empty, so the book's rupees
fell while its rows did not; in the other, an edit divided two counts as whole numbers, so a ratio
printed 1 where it was 1.84. Which way would have stopped both before Anand read the sheet?

a) The fingerprint alone, printed beside each run: it shows the empty amounts as a rupee fall after Anand has the sheet
b) Write, audit, publish with the fingerprint and the multiply-back check in its audit: both runs stop in staging
c) A snapshot table of each Monday's outputs: both problems show in the next week's history, after Anand reads them
d) Write, audit, publish with a row-count check alone: neither run changes a row count, so both are published

### Q3. Which change to the book would the seven-number fingerprint miss?

Suppose the seven-number fingerprint above prints beside every run. Which change to the book between
two Mondays would leave all seven numbers where they were?

a) A late Q2 order added to the orders table after Monday's run
b) An order's amount corrected from Rs 1,200 to Rs 2,100 overnight
c) A Retail-Core customer moved to Retail-Plus on the customers table
d) A new member added to the customers table with a joining date in October

## Will the same query draw the same sample?

Used at work whenever an auditor traces a sample of records from a report back to the source system.

### Q4. What most likely explains a traced sample that changed overnight while the fingerprint did not?

Every id and amount in this item is invented. The service head traces five cancelled Q2 store orders
each week with this query:

```sql
SELECT order_id, amount FROM orders
WHERE quarter = 'Q2' AND channel = 'store' AND status = 'cancelled'
LIMIT 5;
```

| Run | The five orders | Total |
|---|---|---|
| Your run on Monday | S-101 Rs 640, S-104 Rs 1,210, S-107 Rs 380, S-110 Rs 2,050, S-113 Rs 720 | Rs 5,000 |
| The analyst's rerun after an overnight reload | S-107 Rs 380, S-110 Rs 2,050, S-113 Rs 720, S-116 Rs 900, S-119 Rs 1,340 | Rs 5,390 |

The seven-number fingerprint, printed beside both runs, read the same both times. What most likely explains the Rs 390
difference?

a) The book changed overnight, since the rerun found two orders that Monday's run did not
b) LIMIT keeps the five most recent orders, and two newer cancellations arrived overnight
c) The analyst's query filtered on a different status, since the two samples share only three orders
d) With no ORDER BY the database returned an unspecified five, and the overnight reload moved rows

### Q5. Which route confirms the five cancelled store orders without trusting the database's ordering?

The service head's query now ends `ORDER BY order_id LIMIT 5`. On the book there are 19 cancelled Q2
store orders. Kavya Nair, the team's senior analyst, wants the five confirmed by a route that does not
rely on the database's ordering. Which route does that, sized in rows?

a) Rerun the same ordered query twice more and check that all three fives agree
b) Fetch all 19 candidates, sort them by order id in Python and take the first five
c) Fetch five rows with LIMIT 5 and sort those five by order id in Python
d) Fetch all 19 candidates and keep the first five in the order the database sends them

## What does the Monday suite tell Anand?

Used at work whenever a week's analysis ends in one line a controller can sign.

### Q6. Which line tells Anand what the Monday suite found?

The suite found, on the book: booked revenue down 1.6 percent, from Rs 10,00,00,000 to Rs 9,84,00,000;
Retail-Plus's revenue down 29.4 percent, with 91 members buying in Q1 and 76 in Q2, orders per
customer at 2.36 then 1.84 and revenue per order at Rs 2,725 then Rs 2,953; and 244 customers who
bought in Q1 against 227 in Q2. Which line holds?

a) Booked revenue fell 1.6 percent; Retail-Plus fell 29.4 percent: 16.5 percent fewer members, each ordering 22.0 percent less often, each order 8.4 percent larger
b) Booked revenue fell 1.6 percent; customers held flat across both quarters, and each of them ordered 14.0 percent less often than in Q1, a fall in frequency alone
c) Booked revenue fell 1.6 percent; Retail-Plus members halved their orders, from 2 each to 1 each, in one quarter, so the tier needs an emergency plan
d) Booked revenue fell 1.6 percent; spend per Retail-Plus member fell 15.5 percent, from Rs 6,437 to Rs 5,439, a milder fall than the tier's orders and revenue
