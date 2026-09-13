# Kahoot, Week 1 Day 3

Six items plus one return question from Tuesday, one level up.

---

## Q1. What three counts does a profiler report for a field?
*Tests: profiling is a fixed move, not an improvised look around.*

a) Minimum, maximum and the average value across all of the records
b) Present, convertible and distinct  <- correct
c) Nulls, blanks and whitespace-only strings counted separately
d) Rows, columns and the number of bytes the field occupies on disk

---

## Q2. A dedupe finds nothing and 201 rows hold 186 ids. What happened?
*Tests: the identity rule, and why "looks the same" is not "is the same order".*

a) The dedupe ran on the whole record and the repeats differ somewhere  <- correct
b) The ids were read as text, so the comparison never matched anything
c) There are no duplicates and the id column simply allows repeats
d) The file was read twice and the second read replaced the first one

---

## Q3. You default every failed conversion to zero. The data looks clean. What was lost?
*Tests: a silent default is a decision nobody can audit.*

a) Nothing is lost, since zero is the correct value for an unknown amount
b) The row count, because defaulted rows are dropped from the output
c) The knowledge of how many rows failed, and why  <- correct
d) The data types, because every column becomes an integer after this

---

## Q4. Input 200, clean 183, rejected 14. Does it reconcile?
*Tests: the only equation of the day, and the arithmetic of noticing.*

a) Yes, because 183 clean rows plus 14 rejected is close enough to 200
b) Yes, if the three remaining rows were empty lines at the end of the file
c) It cannot be told without knowing what the rejection reasons were
d) No, three rows are unaccounted for  <- correct

---

## Q5. The Rs 4,80,000 order survives the clean pass. Why?
*Tests: cleaning is not making the data agree with you.*

a) Because it is the largest order and the largest is always kept on purpose
b) Because it is real  <- correct
c) Because removing it would change the revenue total that Finance already has
d) Because outliers are only removed once a statistical test has flagged them

---

## Q6. Dashboard says 2.1 crore, Finance says 1.9. Which, and how?
*Tests: the reconciliation, and the fact that both figures are computable.*

a) Finance, because the books are the system of record in every company
b) The dashboard, because it is computed from the source export directly
c) Finance, and a bridge from 2.1 to 1.9 that names every step proves it  <- correct
d) Neither until a third system is brought in to break the tie between them

---

## Return question from Tuesday, one level up

## Q7. Name a data reason that could fake the Retail-Plus finding.
*Tests: Tuesday's conclusion, now under the doubt Wednesday teaches.*

a) Retail-Plus members are simply ordering less often than they used to be
b) The two quarters cover the same number of weeks as each other
c) Duplicated Q1 rows concentrated in one segment  <- correct
d) The discount field is absent on some of the Retail-Plus records entirely

---

## Trainer note on the set

Q4 is the one to slow down on: 183 plus 14 is 197, and the missing three are the whole point of
writing the equation down. Q7 is the return question and it lands hardest if it is asked before the
reveal in block five rather than after it.
