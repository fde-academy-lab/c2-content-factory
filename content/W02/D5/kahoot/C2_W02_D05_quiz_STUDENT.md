# Can you make Friday's eight calls in seconds, from a pivot that reads too high to Thursday's merge that grew?

Eight items, ungraded, scored on correctness and speed together. Seven are today's, and the last is
the return question from Thursday, one level up.

The day built the three things Meera's chief of staff opens on Monday without a login: the revenue
tree by segment for both quarters, the protect list of fifty Retail-Plus members with a lookup by id,
and one front-page number with its trend, in a workbook a director can change in the room. The
warehouse is the database that holds one row per order and is the source of truth, and the deck was
built from two exports of it. A lookup returns a value from the row that matches an id. Anand Iyer is
Kalpa Retail's finance controller. On Thursday the team built one row per customer in pandas, where
`merge` joins two tables on a key.

**Who needs the answer.** The trainer, closing the day. Each item is one of the day's calls made in
seconds, and an item most of the room misses is the check most likely to be skipped on Monday, so it
is the one to say again before the room leaves.

**The questions on the way.**

- The pivot's total is nearly twice the warehouse's; what do you suspect first?
- A lookup returned a member for an id the table does not hold; which argument was wrong?
- Which three things sit beside a front-page number so it is read right?
- A director changes an assumption in the room; what makes the recalculation honest?
- Which tool owns each of five asks, in order?
- Which of the week's steps must never be done in Excel?
- A filtered list still shows the whole list's total; what sits at its foot?
- Thursday's merge turned 1,000 customers into 1,120 rows; what happened, and what would have caught it?

---

## Q1. The pivot's total is nearly twice the warehouse's; what do you suspect first?
*Tests: the grain under a pivot, checked before anything else.*

- The warehouse has not loaded the latest week of orders yet
- The export repeats rows, so a Sum adds orders more than once  <- correct
- The pivot is averaging a column where it should be adding it
- Somebody typed a figure over the pivot's grand total by hand

---

## Q2. A lookup returned a member for an id the table does not hold; which argument was wrong?
*Tests: an approximate match hands back a neighbour, with nothing on screen turning red.*

- The return column, which pointed at the wrong field of the row
- The lookup value, which was typed in lower case
- The table range, which stopped one row too early
- The match type: approximate where it had to be exact  <- correct

---

## Q3. Which three things sit beside a front-page number so it is read right?
*Tests: the card carries its period, its comparison and its base.*

- Its period, its comparison and its base  <- correct
- Its source, its owner and its refresh date
- Its trend, its target and its forecast
- Its segment split, its chart and a footnote

---

## Q4. A director changes an assumption in the room; what makes the recalculation honest?
*Tests: assumptions sit in marked inputs, and every other cell computes from the source.*

- The pivot is refreshed by hand after every change made
- The director's figure replaces the old one in its own cell
- It sits in an input, and every other cell is a formula  <- correct
- The workbook is protected, so only the director can type

---

## Q5. Which tool owns each of five asks, in order?
*Tests: the operating rule, called fast. The asks: Anand's audited revenue; a one-off hypothesis; a
director's what-if; counting each order once for Finance; a member lookup on a laptop.*

- Warehouse, pandas, Excel, Excel, Excel
- Excel, pandas, Excel, warehouse, warehouse
- Warehouse, pandas, Excel, warehouse, Excel  <- correct
- Warehouse, warehouse, Excel, pandas, Excel

---

## Q6. Which of the week's steps must never be done in Excel?
*Tests: Excel presents and explores; the join Finance relies on stays in the warehouse.*

- Joining orders to their payments for Finance's figure  <- correct
- Slicing the reconciled tree by segment in the room
- Looking up one member by their id before a director's call
- Drawing the front-page number's monthly trend line

---

## Q7. A filtered list still shows the whole list's total; what sits at its foot?
*Tests: SUM adds the rows a filter hid; SUBTOTAL(109) adds only the rows on screen.*

- SUBTOTAL(109) over the revenue column
- SUBTOTAL(9) over the revenue column
- SUMIFS on the city over the revenue column
- SUM over the revenue column  <- correct

---

## Q8. Thursday's merge turned 1,000 customers into 1,120 rows; what happened, and what would have caught it?
*Tests: the return question from Thursday: a fan-out made loud by validate.*

- Some customers dropped out; how="outer" would have kept them
- The other table repeats keys; validate="one_to_one" raises  <- correct
- The segments were misspelt; on="segment" would mend the join
- The index was reset; sort=True would have restored the order
