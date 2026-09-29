# Kahoot, Week 1 Wednesday

Eight items, ungraded, scored on correctness and speed together. The first item returns to Tuesday;
the rest climb the day's five rungs. Every number is invented unless the item says it is the day's.

Each item names what it tests, so an item dropped for time says what was lost.

---

## Q1. Return to Tuesday: which data reason could fake a segment's fall?
*Tests: Tuesday's finding was measured on an unchecked export, which is today's premise.*

- A price rise in that segment during the second quarter
- Rows copied twice in the first quarter of that segment  <- correct
- A new customer segment launched in the second quarter
- A discount field missing on a subset of the orders

---

## Q2. What three counts does a profile report for every field?
*Tests: the profile before any total.*

- Mean, median and maximum of the field
- Rows, columns and the file's size on disk
- Present, convertible and distinct  <- correct
- Missing, duplicated and outlying values

---

## Q3. A dedupe says 0 duplicates; distinct ids say 186 of 200. What happened?
*Tests: the whole-record key that makes every row unique.*

- 14 orders are missing from the export and need a resend
- The id count is wrong, since the dedupe checked every field
- Fourteen rows have a blank order_id the count skipped
- The dedupe compared a field that differs on every row  <- correct

---

## Q4. Failures are turned into 0 so the loop runs. What got lost?
*Tests: coercion hides failures and invents values.*

- Nothing, since zero adds nothing to the total
- The evidence that an order's amount was unreadable  <- correct
- Only the speed of the loop, since it now does more
- The rows, since a zero row is dropped from the file

---

## Q5. Input 200, clean 183, rejected 14. Does it reconcile?
*Tests: input equals clean plus rejected, as arithmetic.*

- No, since 183 plus 14 is 197, 3 short  <- correct
- Yes, since 183 is more than nine tenths of the input
- Yes, since the rejected rows are all listed in the log
- No, since a clean file must hold all 200 rows

---

## Q6. The rows reconcile, and Q1 is Rs 3,000 short of the books. Next step?
*Tests: reconcile twice, in rows and in rupees.*

- Ship it, since Rs 3,000 rounds away in a crore
- Add a Rs 3,000 adjustment line to close the gap
- Find the set-aside row that holds it  <- correct
- Ask Finance to lower their books by Rs 3,000

---

## Q7. A Rs 18 lakh Business order survives cleaning. Why?
*Tests: large is not wrong; the record decides.*

- Its record and its buyer both check out  <- correct
- Removing it would make the quarter look too small
- Bulk orders are never checked by a cleaning pass
- It sits below three times the quarter's mean order

---

## Q8. Dashboard 2.1 crore, Finance 1.9. Which is right, and how do you prove it?
*Tests: the bridge, one move per cause, backed by rows.*

- The dashboard, since it reads every row the ERP exported
- The average of the two, since both carry some error
- Neither, until Finance re-enters every order by hand
- The books, once the bridge closes to them in rupees  <- correct
