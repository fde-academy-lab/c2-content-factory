# Which cohort is weakest when read at the same age, and what does a flat blend hide?

Zomato Gold, Chennai. The membership dashboard reports month-two retention, the share of members two
or more months past their signup month who ordered in the month, as flat at 38 percent from June to
September 2026. Chapter 2 built the cohort table on all 53,089 members. Illustrative case: the
company is real, the situation and the data are synthetic, built for this class.

This is a drill at the close of chapter 2, on paper, with no code.

**Who needs the answer.** The membership lead, about to report "nothing changed" because the number
is flat. A cohort ranked on the wrong comparison sends the follow-up to the wrong group of members.

**The questions on the way.**

- What does one cohort's row say about how members leave?
- Which comparison ranks three cohorts fairly?
- Why does a plain average of cohort rates miss the true reading?
- Which second route proves the dashboard's own number?

Three rows of the cohort table. Each cell is the percent of the cohort that ordered at that age;
month one is the first full calendar month after joining.

| Cohort | Members | Month one | Month two | Month three | Month four | Month five | Month six | Month seven | Month eight |
|---|---|---|---|---|---|---|---|---|---|
| January | 4,854 | 58 | 38.7 | 38.4 | 38.1 | 37.8 | 37.5 | 37.2 | 36.9 |
| April | 4,859 | 53 | 38.6 | 38.3 | 38.0 | 37.7 | | | |
| July | 5,057 | 49 | 38.5 | | | | | | |

In September the dashboard counts the seven cohorts from January to July: 13,218 of 35,000 members
ordered, 37.8 percent. The August cohort, 13,000 members, is in its month one at 31 percent and
outside that count.

**What you post.** Four letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

## What do the rows say, read by age?

This comes up at work whenever a retention table lands on a desk: the rows are read for how members
leave, and the cohorts are compared at the same age.

### Q1. Which sentence describes January's row?

*Level L2 · asked in every analytics screen.*

a) A steady fall of about 3 points a month, from 58 to 36.9 over seven months
b) About 19 points lost after month one, then about 0.3 points a month
c) A fall after month one that grows larger as the cohort ages
d) Flat from month two on, which is why the dashboard reads flat

### Q2. Which comparison says fairly which of January, April and July is the weakest cohort?

*Level L2, a design call · asked in product-company screens.*

a) Each cohort in September, 36.9, 37.7 and 38.5, so July is the strongest
b) Each cohort's average over every month it has had, so the oldest looks weakest
c) Each cohort at the same age, month one, 58, 53 and 49, so July is the weakest
d) Each cohort's size, since the largest cohort carries the most weight in the blend

---

## What is September's number made of?

This comes up at work when a flat number has to be taken apart before anyone believes it.

### Q3. Counting August at its month-one rate, the eight cohorts' September rates average 36.9 percent with no weights, while everyone counted reads 35.9: why do the two differ?

*Level L3 · asked in every analytics screen.*

a) The plain average gives August one vote in eight, though it holds 13,000 of 48,000 members
b) The plain average leaves out the members who placed no order in September
c) The true reading also counts the members who joined in September itself
d) Each cohort's rate was rounded before averaging, and eight roundings add up to a full point

### Q4. Which second route confirms the dashboard's 37.8 percent for September?

*Level L3, a design call · asked in GCC analytics screens.*

a) The mean of the four monthly readings from June to September, 38.2, 38.0, 37.9 and 37.8
b) September's orders divided by September's members, taken from the orders table
c) January's month-eight rate, since the oldest cohort shows where the others are heading
d) The seven cohorts' September rates weighted by size, which must give 13,218 of 35,000

**In code.** Notebook 02's empty your-turn cell builds the route in Q4 on all seven cohorts.
