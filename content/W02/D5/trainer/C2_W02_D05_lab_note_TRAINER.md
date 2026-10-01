# Where will learners stall in Friday's practice lab, and which one hint unblocks each problem?

**TRAINER ONLY.** For the TA who runs `exercises/practice/C2_W02_D05_lab_STUDENT.md` after the
afternoon block. About an hour; the solution file, `exercises/solutions/C2_W02_D05_lab_solution_STUDENT.md`,
opens at the end.

**Who needs the answer.** The TA, who has one hint per problem to give and an hour to give it in. A
hint that names the answer turns the lab into a reading exercise; a hint that names the check keeps
the learner doing the work.

**The questions on the way.**

- Where do learners stall in each problem, and what is the one hint?
- What does a finished lab look like?
- Which wrong answers are worth a minute with the whole room?
- What do early finishers do next?

## Where do learners stall in each problem, and what is the one hint?

| Problem | Minutes | Where learners stall | The one hint to give |
|---|---|---|---|
| 1. Which tool owns each of eight asks | 15 | Q3 and Q8. Counting each order once feels like an Excel job because Friday did it with a flag; a what-if feels like it needs the warehouse because it is about the future. | "Who has to trust this number, and how often is it rebuilt?" |
| 2. What a director misreads in three cards | 12 | Q10: they reach for the period, which the card names. Q11: they read past the word "up". | "Read the card aloud to someone who has not seen the tree. What do they ask first?" |
| 3. The hurried pivot and the honest card | 15 | Q12: they add the instalment orders once. Q13: they think Remove Duplicates removes the instalments too, or that nothing is an exact copy. Q14: they divide the fall by Q2. | "Write the rows out quarter by quarter, then say which two rows are identical in every column." |
| 4. A sheet you did not build | 20 | Q15: they blame the date filter. Q16: they want to sort the ids. Q18: they accept 25 percent because Rs 80,000 is a quarter of Rs 3.20 lakh. | "Which of the day's checks would you run first, and what does it compare?" |

## What does a finished lab look like?

Eighteen letters, `acabcabcbccababadb` in item order (the solution's Answers line), and for problem 4
one sentence per item naming the check that caught it. Problem 3's numbers, for checking work on
paper: the pivot on the rows reads Rs 1,10,000 and Rs 1,03,000, down 6.4 percent; after Remove
Duplicates Rs 1,10,000 and Rs 1,00,000, down 9.1 percent; each order once, Rs 70,000 and Rs 60,000,
down 14.3 percent.

## Which wrong answers are worth a minute with the whole room?

- Q13 at option c, down 14.3 percent: the learner has confused Remove Duplicates with counting each
  order once, which is chapter 2's second trap. Walk the two instalment rows: same order, same amount,
  different dates, so they are not copies.
- Q16 at option b, sorting the ids: sorting is what makes an approximate match return a plausible
  neighbour, so it makes the defect harder to see.
- Q14 at option b, down 16.7 percent: the change divided by Q2, the same slip as Retail-Plus at 41.7
  percent in chapter 4.

## What do early finishers do next?

The chapter sets' items 3 onward, chapters 4 to 6 first, then the decision tool in `demos/`, whose tabs
each hide one formula defect that the tab's own check line exposes.
