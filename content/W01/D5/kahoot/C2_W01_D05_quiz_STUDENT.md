# Which of the week's calls can you make in twenty seconds?

The Kahoot for Week 1, Friday, has eight items. It is ungraded and scores correctness and speed
together, and every number in an item is invented for it.

---

## Q1. Your tree is built and the reconciliation is not done. What happens before the note goes out?
*Tests: the order of the pipeline, and why the reconciliation sits before the tree.*

- Send the tree now, and reconcile later if Finance asks for it
- Reconcile, then rebuild the tree on the reconciled rows  <- correct
- Reconcile only the one segment that the note will lead with
- Run the shuffle test first, since it uses every order

---

## Q2. 12,400 rows, 12,380 distinct order ids, and Finance counts 12,380 orders. What do you do?
*Tests: which check catches a repeat, sized: the gap is 20 rows, and Finance's count says which side is wrong.*

- Ask Finance to add the 20 orders their count is missing
- Keep all 12,400 rows, since they are under 1 percent apart
- Check the 20 match field for field, then drop them, logged  <- correct
- Drop any 20 rows at random so the count matches Finance

---

## Q3. Finance: Q1 Rs 50 lakh, Q2 Rs 45 lakh. Your zero-reject pass: Q1 Rs 47 lakh, Q2 Rs 45 lakh. What did your note say?
*Tests: what has to reconcile, computed: the headline a lost value sends, and the only check that shows it.*

- Q2 down 10.0 percent, since every order count lands
- Q2 down 4.3 percent, and the count check shows it
- Q2 up 4.3 percent, and only the rupee check shows it
- Q2 down 4.3 percent; only the rupee check shows it  <- correct

---

## Q4. Anand asks for "a typical order" from a file with a handful of corporate orders in it. Which number?
*Tests: the median for a typical order in a skewed file, the mean for anything that must reconcile.*

- The mean, because it uses every order in the file
- The mean without the corporate orders, which are outliers
- The median, with the corporate orders named beside it  <- correct
- The largest consumer order, as a safe upper figure

---

## Q5. A shuffle test gives p = 0.04. What is 0.04 a share of?
*Tests: that the p-value is a share of chance-only worlds, a different number from the chance the finding is wrong.*

- Chance-only worlds with a gap at least this large  <- correct
- Findings like this one that later turn out to be wrong
- Tests like this one that come out under 0.05 by luck
- Worlds with a real difference that show a gap this small

---

## Q6. The same 20 members in Q1 and Q2, and the gap was picked after looking. Which test, and which p?
*Tests: two calls at once: keep each member's own two quarters together, and report both directions when the direction was chosen after the data was seen.*

- Flip each member's two quarters; report one direction
- Pool their Q1 and Q2 figures, deal the labels; report both
- Shuffle segment labels across customers; report one direction
- Flip each member's two quarters; report both directions  <- correct

---

## Q7. Four moves on the clean tree. Which one leads Meera's note?
*Tests: count before rate and size together: a lead needs enough orders and a move worth acting on.*

- Business revenue -35%, 7 orders then 5
- Retail-Plus basket -12%, 140 orders then 138  <- correct
- Student revenue +50%, 6 orders then 9
- Retail-Core frequency -2%, 90 orders then 88

---

## Q8. Return from Thursday. Revenue rose after a discount. Which question comes before calling it a success?
*Tests: a fair comparison needs a like-for-like group that did not get the discount.*

- Compared with whom: a similar group that did not get it?  <- correct
- How large was the discount, as a share of the price?
- How much did revenue rise, in rupees rather than percent?
- Did the p-value on the rise come in under 0.05?
