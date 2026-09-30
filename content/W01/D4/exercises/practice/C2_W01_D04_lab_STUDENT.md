# Can you run the day's checks on cases you have not seen, in an hour: four teams' draft sentences, three unexplained gaps, Monday's sample and one note?

The TA-led practice lab, after the afternoon block. Four problems, climbing in difficulty, are the
core and take about 60 minutes: problem 1 ten minutes, problem 2 fifteen, problem 3 twenty and
problem 4 fifteen, the last combining the day. Work alone for problems 1 and 2, in pairs for 3 and 4.
The chapter sets' remaining 26 items, items 3 onward of each set in `exercises/unguided/`, are the
lab's stretch: if you finish the four problems early, work them, chapters 4 to 6's items first, and
whatever is left is tonight's work. Everything invented is labelled so.

Kavya Nair is the senior analyst on Kalpa Retail's data team, and she reviews every line before it
reaches Meera Raghavan, the CEO. A p-value, which the day also calls a share, is the fraction of
chance-only worlds, built by shuffling or flipping where nothing changed, that make a gap at least
as large as the real one. It can count one direction, or a gap that large in either direction. The
usual wobble is the movement chance alone makes in a number from one period or group to the next. A
label shuffle pools the values of two groups of different customers and deals them into two piles at
random, many times. Kalpa Retail's four segments are Retail-Core and Retail-Plus, its two consumer
tiers, of which Retail-Plus is the paid membership; Student; and Business, its sales to companies. A
basket is one order's amount, and a booked order is any order placed, whatever happened to it
afterwards. Which orders count as the money Kalpa kept is Monday's definition, and recalling it is
part of problem 3, so it is not repeated here. The note to a stakeholder has four parts: claim,
evidence, caveat and action.

**Who needs the answer.** Kavya sends back any draft that reads a share as a certainty, credits a
change without asking what else changed, or quotes a rate without its count, and a draft she sends
back is a Monday lost before the growth review. The same four checks come up in analyst interviews,
on cases nobody has seen before.

**The questions on the way.**

- Which of four p-value sentences from other teams' drafts would Kavya pass?
- What most likely explains the gap in each of three invented Kalpa stories?
- Do Retail-Plus baskets beat Retail-Core's on Monday's sample, or is the lead the wobble chance makes?
- What does the note to the head of the app team say about push notifications?

**What you post.** The letters for problems 1 and 2 as one line, seven letters in order, problem 1
giving four and problem 2 giving three. Problem 3's notebook gives five letters of its own, posted on
a second line. Stretch letters, if you reach them, go on one line per chapter set.

```
Post exactly this shape: xxxxxxx
```

---

## Problem 1. Which of four p-value sentences from other teams' drafts would Kavya pass?

Used at work every time a draft with a p-value reaches a senior reviewer.

Ten minutes, alone. Four sentences from other teams' drafts; for each, choose Kavya's verdict.

### Q1. Which verdict does Kavya give the loyalty test's "no effect" line?

"Our loyalty test came back at p = 0.20, so the programme has no effect on repeat orders." Which
verdict?

a) Defensible: 0.20 sits far above 0.05, so the programme's effect is zero
b) Wrong: chance makes a gap that size often, which cannot show a zero effect
c) Defensible, provided the test had more than thirty customers in each group
d) Wrong: the programme's effect is 20 percent, the number the share reports

### Q2. Which verdict does Kavya give the app redesign's "99 percent sure" line?

"The app redesign lifted conversion; p = 0.01, so we are 99 percent sure the redesign works." Which
verdict?

a) Wrong: the share was counted in worlds with no lift at all
b) Defensible, since one minus the share is how sure the analyst can be
c) Defensible, provided the test ran ten thousand shuffles or more
d) Wrong: it means the redesign lifted conversion by exactly 1 percent

### Q3. Which verdict does Kavya give the bundle launch's line about 8 in 100 shuffles?

"If basket size had not changed after the bundle launch, a rise this large would appear in about 8 of
every 100 shuffles, so we cannot yet tell it from the usual wobble." Which verdict?

a) Wrong: 8 in 100 is below 10, so the rise is real
b) Wrong: it should say a 92 percent chance the rise is real
c) Defensible: the share, its world and a careful conclusion
d) Defensible only once the bundle has also cleared its cost

### Q4. Which verdict does Kavya give the pricing team's Rs 2 "big win"?

"p = 0.001 on 3 lakh orders, so the Rs 2 rise in average order is a big win for the pricing team."
Which verdict?

a) Defensible: 0.001 is about as strong as evidence gets, so the win is big
b) Defensible, since 3 lakh orders remove any doubt about the rise's size
c) Wrong: on 3 lakh orders any gap turns significant, so this rise is only noise
d) Wrong: it beats chance, and Rs 2 an order must still be judged against cost

---

## Problem 2. What most likely explains the gap in each of three invented Kalpa stories?

Used at work whenever a gap between two groups reaches a meeting with a cause already attached to it.

Fifteen minutes, alone. Three invented Kalpa stories; for each, choose what most likely explains the
gap, or what a fair comparison would need.

### Q5. What most likely explains the premium-range stores' 25 percent bigger baskets?

Stores that stock the premium range report baskets 25 percent bigger. The premium range went only to
stores in the six largest malls. What most likely explains most of the gap?

a) The premium range, since it is the only thing that differs between the stores
b) Chance: a 25 percent gap across a few stores is the usual wobble
c) Where the stores are: large-mall shoppers spent more before the range arrived
d) The season, since premium ranges launch before festivals, when baskets grow

### Q6. What would a fair comparison of newsletter openers need?

Members who opened the monthly newsletter bought twice as often as members who did not. Marketing
wants to send it weekly. What would a fair comparison need?

a) Members who opened it against those who did not, over six months or more
b) A random half of similar members sent it, and the two halves compared
c) Only members who opened it, before and after each issue, over a year
d) A bigger shuffle test on the same openers and non-openers

### Q7. What should the note say about delivery times after the warehouse and the courier changed together?

Delivery times fell after the new warehouse opened, and the warehouse opened in the month the
company also moved half its orders to a faster courier. What should the note say?

a) The courier change explains the fall, and the warehouse explains none of it
b) The warehouse cut delivery times, since it opened first
c) Nothing, since two changes at once can never be separated in the data
d) Both changed at once, so split orders by courier before crediting either

---

## Problem 3. Do Retail-Plus baskets beat Retail-Core's on Monday's sample, or is the lead the wobble chance makes?

Used at work whenever a team compares two customer groups on a small file and a definition decides
which orders count.

Twenty minutes, in pairs. Open `notebooks/C2_W01_D04_ex3_practice_lab_STUDENT.ipynb`. It asks
whether Retail-Plus baskets are bigger than Retail-Core's on the 24-order sample from Monday's
take-home, first on every booked order and then on the money Kalpa kept. The two tiers' baskets are
different customers' orders, so the chance reference is the label shuffle: every basket goes into one
pool and is dealt at random into two piles of the tiers' sizes, 5,000 times. Five lettered choices,
posted on their own line.

---

## Problem 4. What does the note to the head of the app team say about push notifications?

Used at work whenever a team reports a lift and asks for more of what produced it.

Fifteen minutes, in pairs. An invented case. The app team reports: "Push notifications lifted weekly
orders 9 percent. Users who got notifications ordered more than users who did not. The lift is
significant, p = 0.02." You learn three more facts by asking:

- Notifications went only to users who had opted in, and opted-in users were already the most active.
- The comparison covers 18 opted-in users and 4,000 users who never opted in.
- Sending notifications costs almost nothing.

Write the note to the head of the app team, under 120 words, in four parts: claim, evidence, caveat,
action. The note must use all three facts. There are no letters for this problem; the TA reads your
note aloud with you and checks it against the four parts.
