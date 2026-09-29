# Solution: which branch does Meera open first?

Answers: 3b 4d 6a 7c 8b 9d 10a

The three numbers: item 1 is 16 customers, item 2 is 1.24 orders per customer, item 5 is Rs 5,448.

The executed notebook beside this file,
`exercises/solutions/C2_W01_D01_ex1_escalated_case_solution_STUDENT.ipynb`, computes every number
here from the 30 orders.

## The idea being tested

The morning answered three questions with three checks. This case puts them together and adds the
one that decides the budget: branches multiply. Marketing adds a 10 percent lift in customers to a
10 percent lift in frequency and calls it 20 percent; the tree multiplies them, 1.10 times 1.10 is
1.21, so the right figure is 21 percent, Rs 6,59,220 on Rs 5,44,810 against Rs 6,53,772 at 20
percent, Rs 5,448 apart. The same arithmetic turns a 15 percent discount that lifts quantity 10
percent into a 6.5 percent fall, because 0.85 times 1.10 is 0.935. The branch to open first is
frequency, since 16 of 23 customers bought once in the quarter. One window shows the shape of
revenue, and only two windows show which branch moved, so the Rs 12 crore is held until Tuesday's
Q1 against Q2.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | 16 | 23 customers less the 7 who bought twice leaves 16 who bought once. | 7 is the repeat count; 23 is every customer; 30 counts rows. |
| 2 | 1.24 | 26 not-cancelled orders over the 21 distinct customers on them. | 1.30 is the booked rate; 1.11 is delivered; 26 over 23 is 1.13, which mixes two definitions. |
| 3 | b | The median, Rs 2,205, is what a typical order is worth, and the sentence says why the mean is set aside. | a is the trap from round 3. c gives the delivered median a booked label. d hands Meera two numbers and no answer. |
| 4 | d | Branches multiply: 1.10 times 1.10 is 1.21, and 1.21 times Rs 5,44,810 is Rs 6,59,220. | a is marketing's addition. b drops one lift for no reason. c is arithmetic with no basis. |
| 5 | Rs 5,448 | Rs 6,59,220 less Rs 6,53,772 is Rs 5,448. | Rs 54,481 is a full 10 percent; any figure above it has added a lift twice. |
| 6 | a | Price at 0.85 and quantity at 1.10 multiply to 0.935; 0.935 times Rs 5,44,810 is about Rs 5,09,400, a 6.5 percent fall. | b adds percentages that multiply. c ignores the lower price. d counts the discount as a lift. |
| 7 | c | 16 of 23 customers bought once in the quarter, so repeat buying is the branch with the most room and the cheapest to test. | a names the branch with a budget attached, which is the reason it needs checking. b: price was never measured today and risks volume. d: the typical order is a level, and with one window there is nothing to say it is short. |
| 8 | b | The answer names what one window cannot show and when the evidence arrives, which makes it a hold rather than a refusal. | a refuses with no evidence against acquisition. c: the file is enough to show the shape, so waiting a year gives up what is known. d turns a question of evidence into a contest between teams. |
| 9 | d | A change needs two windows; one quarter shows the shape of revenue and cannot show which branch moved. | a, b and c are all answered inside this window, and the morning answered each. |
| 10 | a | The definition first, then the leaves, then the typical order, then the branch, then the limit: each part rests on the one before it. | b leads with the recommendation before the numbers that support it. c puts the typical order before the leaves and the limit before the branch. d gives leaves before saying which "sales" they are on. |

## The sentence to Meera

A sentence that meets the brief reads close to this: "On the 30 orders from 1 July to 26
September, 23 customers placed 1.30 orders each at a typical order of Rs 2,205, and 16 of them
bought only once, so I would open frequency before acquisition; this one window cannot show which
branch moved, so hold the Rs 12 crore until Tuesday's two quarters."

Read yours against four tests: it names the window, it carries the median rather than the mean, it
names a branch, and it says what it cannot yet show.

## The part worth arguing about

Item 8, option a. Some learners will want to kill the budget outright, and the numbers do make
acquisition look like the weaker bet. One window cannot prove that the customer count did not fall;
it can only show that frequency has room. The honest move is to hold, name the test, and name the
day it runs. A "no" with a date on it survives the marketing lead's reply; a "no" without one
starts an argument.

**Kavya's review.** "Two lifts of 10 percent are 21 percent, and the Rs 5,448 is small here. At
Kalpa's scale, the same slip in a plan is a crore. Recompute through the tree every time."

## Where the pattern lives in production

Driver-tree planning is how finance and growth teams set targets: a plan for revenue is written as
a plan for each driver, and the drivers are multiplied back. The additive slip is common in planning
decks, and the discount arithmetic is the first question in most pricing reviews. Consulting case
interviews test the same move as the profitability framework.

## Hands-on

The twelve TODO picks in `notebooks/C2_W01_D01_ex1_escalated_case_STUDENT.ipynb`, in order, are
c b d d c d a c b b a d. The executed solution notebook named above carries the filled line for each,
and its checks all print PASS.

## The afternoon in one line

For the debrief, both cases together:

Answer key: 3b 4d 6a 7c 8b 9d 10a 11c 12a 13d 14b 15a 16b
