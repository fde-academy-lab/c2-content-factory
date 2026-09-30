# Practice lab set: real, how big, how many, and who got it

About an hour in the TA-led practice lab. Four problems climbing in difficulty; the last combines the
day. Work alone for problems 1 and 2, in pairs for 3 and 4. Everything invented is labelled so.

Post the letters for problems 1 and 2 as one line, seven letters in order (problem 1 gives four and
problem 2 gives three). Problem 3's notebook gives five letters of its own, posted on a second line:

```
Post exactly this shape: xxxxxxx
```

---

## Problem 1. Four p-value sentences, 10 minutes

Four sentences from other teams' drafts. For each, choose Kavya's verdict.

### Q1

"Our loyalty test came back at p = 0.20, so the programme has no effect on repeat orders." Which
verdict?

a) Defensible: 0.20 is well above 0.05, so the effect is zero
b) Wrong: chance makes a gap that size often, which never shows the effect is zero
c) Defensible, as long as the loyalty test used more than thirty customers in each group
d) Wrong: the programme's effect is 20 percent, which is the number the share reports for anyone who reads it

### Q2

"The app redesign lifted conversion; p = 0.01, so we are 99 percent sure the redesign works." Which
verdict?

a) Wrong: the share was counted in worlds with no lift, so it is not how sure we are
b) Defensible, since 1 minus the share is how sure the analyst can be
c) Defensible if the shuffle used ten thousand shuffles or more
d) Wrong: p = 0.01 means the redesign lifted conversion by exactly 1 percent on the day it shipped

### Q3

"If basket size had not changed after the bundle launch, a rise this large would appear in about 8 of
every 100 shuffles, so we cannot yet tell it from the usual wobble." Which verdict?

a) Wrong: 8 in 100 is below 10, so the rise is real
b) Wrong: a share should never be written in shuffles
c) Defensible: the share, its world and a careful conclusion
d) Defensible only if the bundle launch also cleared its cost, which the sentence would have to state as well

### Q4

"p = 0.001 on 3 lakh orders, so the Rs 2 rise in average order is a big win for the pricing team."
Which verdict?

a) Defensible: 0.001 is about as strong as evidence gets, so the win is big
b) Defensible, because a sample of 3 lakh orders removes any doubt about both the size and the value of the rise
c) Wrong: the p-value should be multiplied by the orders to find the rupee size
d) Wrong: the rise beats chance and its size, Rs 2 on each order, still has to be judged against cost

---

## Problem 2. The confounder in three vignettes, 15 minutes

Three invented Kalpa stories. For each, choose what most likely explains the gap.

### Q5

Stores that stock the premium range report baskets 25 percent bigger. The premium range went only to
stores in the six largest malls. What most likely explains most of the gap?

a) The premium range, since it is the only thing that differs between the stores
b) Nothing, since a 25 percent gap is too small to explain
c) Where the stores are: large-mall shoppers spent more before the range arrived
d) The season, since premium ranges usually launch before festivals when every store's baskets grow

### Q6

Members who opened the monthly newsletter bought twice as often as members who did not. Marketing
wants to send it weekly. What would a fair comparison need?

a) Members who opened it against members who did not, over a longer window of six months or more
b) The newsletter sent to a random half of similar members, and both halves compared after
c) Only members who opened it, before and after each issue
d) A bigger shuffle test on the same openers and non-openers

### Q7

Delivery times fell after the new warehouse opened, and the warehouse opened in the month the
company also moved half its orders to a faster courier. What should the note say?

a) The fall is explained by the courier change and not by the warehouse
b) The warehouse cut delivery times, since it opened first
c) Nothing at all, since two changes at once can never be separated by anyone looking at the data
d) Both changed together, so split the orders by courier before crediting either

---

## Problem 3. The shuffle on Monday's sample, 20 minutes

Open `notebooks/C2_W01_D04_ex3_practice_lab_STUDENT.ipynb`. It runs today's shuffle on the 24-order
sample from Monday's take-home and asks whether Retail-Plus baskets are bigger than Retail-Core's,
first on every booked order and then on delivered orders only. Five lettered choices, posted on their
own line.

---

## Problem 4. The whole day in one note, 15 minutes, in pairs

An invented case. The app team reports: "Push notifications lifted weekly orders 9 percent. Users who
got notifications ordered more than users who did not. The lift is significant, p = 0.02." You learn
three more facts by asking:

- Notifications went only to users who had opted in, and opted-in users were already the most active.
- The comparison covers 18 opted-in users and 4,000 users who never opted in.
- Sending notifications costs almost nothing.

Write the note to the head of the app team, under 120 words, in four parts: claim, evidence, caveat,
action. The note must use all three facts. There are no letters for this problem; the TA reads your
note aloud with you and checks it against the four parts.
