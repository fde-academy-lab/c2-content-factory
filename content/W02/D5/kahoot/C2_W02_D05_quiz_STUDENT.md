# Kahoot, Week 2 Friday

Eight items, ungraded, scored on correctness and speed together. Item 8 is the return question from
Thursday, one level up.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. The pivot's grand total is higher than the warehouse's. What do you suspect first?

*Tests: the grain under a pivot, checked before anything else.*

- The warehouse has not loaded the latest week of orders yet
- The export repeats rows, so Sum counts orders twice  <- correct
- The pivot is averaging where it should be adding
- Somebody typed over the grand total cell by hand

---

## Q2. A lookup returned a member for an id that does not exist. Which argument was wrong?

*Tests: an approximate match hands back a neighbour, silently.*

- The return column, which pointed at the wrong field
- The lookup value, which was typed in lower case letters
- The table range, which stopped one row too early
- The match type: approximate where it had to be exact  <- correct

---

## Q3. A front-page number without which three things will be misread?

*Tests: the card carries its period, its comparison and its base.*

- Its period, its comparison and its base  <- correct
- Its colour, its font size and its icon
- Its source, its owner and its refresh date
- Its trend, its forecast and its target

---

## Q4. A director changes an assumption in the room. What must be true for the recalculation to be honest?

*Tests: inputs are marked, and every other cell computes from the source.*

- The sheet was saved before the meeting started
- The director types the new figure over the old one
- It is an input, and every other cell is a formula  <- correct
- The pivot is refreshed by hand after every change

---

## Q5. Anand's audited revenue, a one-off hypothesis, a director's what-if. Which tools, in order?

*Tests: the operating rule, called fast.*

- Excel, pandas, the warehouse
- The warehouse, pandas, Excel  <- correct
- pandas, the warehouse, Excel
- The warehouse, Excel, pandas

---

## Q6. Which of the week's steps must never be done in Excel?

*Tests: Excel presents and explores; it never cleans the source.*

- Removing the double-paid rows from the export  <- correct
- Slicing the tree by segment in the room
- Looking up a member by id before a call
- Drawing the front-page number's monthly trend

---

## Q7. A list is filtered to Mumbai and the foot still reads the whole list's total. What is at the foot?

*Tests: SUM adds rows a filter hid; SUBTOTAL(109) does not.*

- SUBTOTAL(109) over the revenue column
- AVERAGE over the revenue column
- COUNT over the member ids
- SUM over the revenue column  <- correct

---

## Q8. Thursday's merge turned 1,000 customers into 1,120 rows. What happened, and which argument would have caught it?

*Tests: the return question: a fan-out, made loud by validate.*

- Some customers were dropped; how="outer" would keep them
- The exposure feed repeats keys; validate="one_to_one" raises  <- correct
- The segments were misspelt; on="segment" would repair the join
- The index was reset; sort=True would restore the order
