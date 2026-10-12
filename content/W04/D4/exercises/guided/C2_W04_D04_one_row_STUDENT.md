# How is one cohort's row counted, and how do a funnel's first two steps divide?

Zomato Gold, Chennai. The membership dashboard reports month-two retention as flat at 38 percent
from June to September 2026, while every signup cohort's own curve falls with age, and since a new
Android checkout shipped on 14 September, members' add-to-cart to order on Android has fallen from
58 to 44 percent. The membership lead must say on Friday whether Gold has a cohort problem or an
everyone problem, and which step of the order flow owns the loss. Illustrative case: the company is
real, the situation and the data are synthetic, built for this class.

The trainer builds this set with the room. Items 1 and 2 run in chapter 1 on the twelve-member card:
the first is fully worked, the second half worked. Items 3 and 4 open chapter 3 on a toy funnel, and
both are yours.

**Who needs the answer.** The membership lead, who will read every cohort row the room builds today.
A row counted over the wrong members makes a weak group look strong.

**The questions on the way.**

- What does the May group keep at each month since joining?
- What does the June group keep, once its first month is counted?
- What does each of a funnel's first two steps read, over the step before?
- Which checkout rate belongs on the membership lead's chart?

Five terms, defined once. A **cohort** is the members who joined in the same calendar month. **Month
one** is the first full calendar month after joining; the joining month is month zero and is never
counted. A member is **active** in a month when she placed at least one order in it. A **session** is
one visit to the app, from opening it to leaving it. A funnel **step's rate** divides those who
reached the step by those who reached the step before, in one unit: sessions or people.

These are seven of the twelve members on the chapter 1 card, rows of the case data, which is
synthetic like all of it. A 1 means she placed at least one order that calendar month.

**How to read an item.** Its level runs from L1, a count by hand, to L6, the call an interviewer asks for; "a design call" asks you to choose a way and say why. "Screens" are interviews, and a GCC is a global capability centre, a multinational company's own technology and analytics centre in India.

| Member | Joined | Jun | Jul | Aug | Sep |
|---|---|---|---|---|---|
| ZG20844 | May | 1 | 1 | 1 | 1 |
| ZG21052 | May | 1 | 1 | 0 | 0 |
| ZG22010 | May | 1 | 0 | 0 | 0 |
| ZG22634 | May | 0 | 0 | 0 | 0 |
| ZG25312 | Jun | joined | 1 | 1 | 1 |
| ZG27475 | Jun | joined | 1 | 0 | 0 |
| ZG28603 | Jun | joined | 0 | 0 | 0 |

**What you post.** Four letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

## What does each group keep at each month since joining?

This comes up at work the first time anyone builds a retention table: the row is counted by age, over
everyone who joined, before any code runs.

### Q1. Which line gives the May group's share at months one, two, three and four?

*Level L1 · asked in every analytics screen.* Worked: May's month one is June, and ZG20844, ZG21052
and ZG22010 ordered, so 3 of 4. Month two is July: 2 of 4. Month three is August: 1 of 4. Month four
is September: 1 of 4. Every share keeps all four May members underneath it. Which line matches the
working?

a) 75, 67, 50 and 100 percent
b) 100, 67, 33 and 33 percent
c) 75, 50, 25 and 25 percent
d) 25, 50, 75 and 75 percent

### Q2. The June group's month one is July, and two of its three members ordered: which line finishes the row?

*Level L1 · asked in every analytics screen.* Half worked: month one is 2 of 3. Count months two and
three over the same three members.

a) 67, 33 and 33 percent
b) 67, 50 and 100 percent
c) 100, 50 and 50 percent
d) 33, 67 and 67 percent

---

## How does a funnel's first step read, and in which unit?

This comes up at work when a product team brings a funnel: each rate divides by the step just before
it, and the chart names whether it counts sessions or people.

A toy funnel, invented for chapter 3, counted in sessions: 100 sessions, 40 with a search, 20 with an
add-to-cart and 10 with a checkout. The 100 sessions came from 20 people, and the 10 checkouts from
10 of them.

### Q3. What do the first two steps read, each over the step before?

*Level L3 · asked in every analytics screen.*

a) 40 and 20 percent, both over the 100 sessions
b) 40 and 50 percent, each over the step before
c) 60 and 50 percent, the share lost at each step
d) 40 and 200 percent, searches over add-to-carts

### Q4. A chart reads "checkout: 10 percent", and the membership lead says one member in ten checks out: what does the chart need?

*Level L3, a design call · asked in product-company screens.*

a) Nothing, since 10 percent is the funnel's rate from the top
b) Its numbers redone per person, since people are what the lead pays for
c) Its denominator moved to the 40 sessions that had a search
d) Its unit named: 10 of 100 sessions is 10 of 20 people, half of them
