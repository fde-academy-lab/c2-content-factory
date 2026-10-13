# What does a gym's dashboard read when a big new cohort joins, and how is the number proved?

A second gym, with three cohorts. Its dashboard counts a member from the month after she joins, and
prints one number a month: the share of everyone it counts who visited. SECTION 3 took the first
gym's dashboard apart, and notebook 03 rebuilt it from its cohorts. The gym and every number on this
page are invented for practice.

This is a drill inside SECTION 3, on paper, with no code, in about four minutes.

**How to read an item.** Its level runs from L1, a count by hand, to L6, the call an interviewer asks for; "a design call" asks you to choose a way and say why. "Screens" are interviews, and a GCC is a global capability centre, a multinational company's own technology and analytics centre in India.

**Who needs the answer.** The second gym's owner, who reads one number each month. A flat number
read as "nothing changed" leaves two falling cohorts with no action.

**The questions on the way.**

- What does the dashboard read in each month?
- Why does the plain mean of the cohorts' rates miss it?
- Which second route proves the number before anyone reports it?

| Cohort | Members | First month | Second month |
|---|---|---|---|
| X | 200 | 60 percent visited | 55 percent visited |
| Y | 300 | 40 percent visited | 36 percent visited |
| Z | 500 | joined, not yet counted | 52 percent visited |

**What you post.** Three letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## What does one number over three cohorts read?

This comes up at work every time a dashboard prints one rate over customers who joined at different
times: the number is a size-weighted average, and the sizes move.

### Q1. What does the dashboard read in the first month and in the second?

*Level L2 · asked in every analytics screen.* Worked: in the first month it counts X and Y, 200 at 60
percent and 300 at 40 percent, which is 120 + 120 = 240 visitors of 500, 48.0 percent. In the second
month it counts all three: 110 + 108 + 260 = 478 visitors of 1,000, 47.8 percent. Which line matches
the working?

a) 50.0 then 47.7 percent, each month's rates averaged
b) 48.0 then 43.6 percent, counting X and Y alone
c) 40 then 36 percent, the larger older cohort, Y
d) 48.0 then 47.8 percent, every member counted

### Q2. In the first month the two rates average 50 percent with no weights, while the dashboard reads 48.0. Why do the two differ?

*Level L3 · asked in product-company screens.* Half worked: the dashboard's 48.0 is 240 of 500. Ask
how many votes each cohort gets in the plain mean, against how many members it has.

a) The plain mean leaves out the members who did not visit
b) The plain mean gives X's 200 members the same vote as Y's 300
c) The dashboard rounds each cohort's rate before it adds them up
d) The dashboard already counts Z, which joined in the first month

---

## How is the number proved?

This comes up at work before any flat number goes into a report: it is rebuilt from its parts, and
the rebuild has to land on the count.

### Q3. Which second route proves the second month's 47.8 percent before anyone reports it?

*Level L3, a design call · asked in GCC analytics screens.*

a) The plain mean of the three rates, which should land within a point of it
b) The first month's 48.0, since a blend over many members moves slowly
c) Each cohort's rate weighted by its size, landing on 478 of 1,000
d) Cohort Z's own rate, since the newest and largest cohort sets the level
