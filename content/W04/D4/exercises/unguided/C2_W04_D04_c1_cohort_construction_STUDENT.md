# How is a cohort's row counted by age, and which table says which month's joiners are weakest?

One branch of a neighbourhood gym: thirty members joined in January, February and March 2026, ten a
month, and the register records whether each visited in each month to June. SECTION 1 counted it by
hand on the slides and notebook 01 counted it in code. The gym and every number on this page are
invented for practice.

This is a drill inside SECTION 1, on paper, with no code, in about four minutes.

**How to read an item.** Its level runs from L1, a count by hand, to L6, the call an interviewer asks for; "a design call" asks you to choose a way and say why. "Screens" are interviews, and a GCC is a global capability centre, a multinational company's own technology and analytics centre in India.

**Who needs the answer.** The gym's owner, who will send one retention offer to one month's joiners.
A row counted over the wrong members, or batches compared at different ages, sends the offer to the
wrong batch.

**The questions on the way.**

- What does January's batch keep at each age?
- What does February's batch keep, once its age one is counted?
- Which first table answers "which month's joiners are weakest?"

The register, counted by calendar month. Each cell is how many of the batch's ten members visited
that month; the joining month is month zero and is left out.

| Joined, 10 each | Feb | Mar | Apr | May | Jun |
|---|---|---|---|---|---|
| January | 8 | 6 | 5 | 5 | 5 |
| February | joined | 7 | 5 | 3 | 3 |
| March | | joined | 6 | 4 | 3 |

**What you post.** Three letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## What does each batch keep at each age?

This comes up at work the first time anyone builds a retention table: each row is counted by age,
over everyone who joined in that month, before any code runs.

### Q1. Which line gives January's row at ages one to five?

*Level L1 · asked in every analytics screen.* Worked: January's age one is February, the first full
month after joining, and 8 of the 10 visited, 80 percent. Age two is March, 6 of 10; ages three to
five are April to June, 5 of 10 each. Every share keeps all ten January joiners underneath it. Which
line matches the working?

a) 50, 50, 50, 60 and 80 percent
b) 80, 60, 50, 50 and 50 percent
c) 80, 75, 83, 100 and 100 percent
d) 100, 80, 60, 50 and 50 percent

### Q2. February's age one is March, and 7 of its 10 joiners visited: which line finishes the row at ages two to four?

*Level L1 · asked in every analytics screen.* Half worked: age one is 7 of 10, 70 percent. Count ages
two to four over the same ten members.

a) 70, 50 and 30 percent
b) 71, 60 and 100 percent
c) 50, 30 and 30 percent
d) 60, 40 and 30 percent

---

## Which table answers the owner's question?

This comes up at work when a manager asks which month's customers are the weakest: the table is
chosen before any number is read.

### Q3. The owner asks which month's joiners are weakest. Which first table answers it?

*Level L2, a design call · asked in every analytics screen.*

a) Joining month down, age across, each cell over the whole batch, compared at age one
b) Joining month down, calendar month across, read along April, where March leads at 6 of 10
c) One row per member with her total visits since joining, ranked from most to fewest
d) One number a month, everyone's visits over everyone counted, as the dashboard shows it
