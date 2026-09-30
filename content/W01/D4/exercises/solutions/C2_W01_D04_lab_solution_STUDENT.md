# Which answers hold in the practice lab on the day's checks in new cases, and why?

Answers: 1b 2a 3c 4d 5c 6b 7d

Problem 3's five letters, from `notebooks/C2_W01_D04_ex3_practice_lab_STUDENT.ipynb`, are `cabdb`,
and its executed solution is `C2_W01_D04_ex3_practice_lab_solution_STUDENT.ipynb` in this folder.

The practice lab puts the day's checks on cases nobody has seen: four sentences from other teams'
drafts that each read a p-value, the share of chance-only worlds that make a gap at least as large as
the real one; three invented Kalpa stories in which a gap between two groups arrives with a cause
attached; the label shuffle, which pools two groups' values and deals them into two piles at random,
rerun on the 24-order sample from Monday's take-home; and a note in four parts, claim, evidence,
caveat and action, on an invented app case. The chapter sets' remaining items were the lab's
stretch, and their answers are in each set's own solution file.

**Who needs the answer.** You, after the lab, checking your letters and your note. Kavya Nair, the
senior analyst who reviews every line before it reaches Meera Raghavan, Kalpa Retail's CEO, sends
back any draft that makes one of these mistakes, and an interviewer counts the same mistakes against
you.

**The questions on the way.**

- Which idea does this lab test?
- Why is each key right, item by item?
- What does problem 3's notebook find, marker by marker?
- What does a model note for problem 4 say?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this lab test?

A p-value says how often chance alone makes a gap, in worlds where nothing changed, and nothing more:
it is neither the chance a finding is wrong, nor a size, nor proof of no effect. A gap between two
groups belongs to whatever else differs between them until a fair comparison rules that out. And a
definition, such as which orders count as money kept, can move a verdict as far as the data can.

## Why is each key right, item by item?

### Q1. Which verdict does Kavya give the loyalty test's "no effect" line?

"Our loyalty test came back at p = 0.20, so the programme has no effect on repeat orders."

The key is b, "Wrong: chance makes a gap that size often, which cannot show a zero effect". A large
share says chance makes the gap often, and a real effect too small for this test to see would look
the same.

- a, "Defensible: 0.20 sits far above 0.05, so the programme's effect is zero": reads absence of
  evidence as evidence of no effect.
- c, "Defensible, provided the test had more than thirty customers in each group": the count does
  not change what the share means.
- d, "Wrong: the programme's effect is 20 percent, the number the share reports": a share is never a
  size.

### Q2. Which verdict does Kavya give the app redesign's "99 percent sure" line?

"The app redesign lifted conversion; p = 0.01, so we are 99 percent sure the redesign works."

The key is a, "Wrong: the share was counted in worlds with no lift at all". The share was counted in
no-lift worlds, so one minus it is no measure of how sure anyone can be.

- b, "Defensible, since one minus the share is how sure the analyst can be": the day's first mistake
  in its most common form.
- c, "Defensible, provided the test ran ten thousand shuffles or more": more shuffles sharpen the
  share and leave its meaning where it was.
- d, "Wrong: it means the redesign lifted conversion by exactly 1 percent": a share is never a size.

### Q3. Which verdict does Kavya give the bundle launch's line about 8 in 100 shuffles?

"If basket size had not changed after the bundle launch, a rise this large would appear in about 8 of
every 100 shuffles, so we cannot yet tell it from the usual wobble."

The key is c, "Defensible: the share, its world and a careful conclusion". It states the share and
the world it was counted in, and draws the honest conclusion: not yet.

- a, "Wrong: 8 in 100 is below 10, so the rise is real": 10 is no threshold, and 8 in 100 is common
  enough to be the wobble.
- b, "Wrong: it should say a 92 percent chance the rise is real": turns the share into a certainty,
  the mistake of item 2.
- d, "Defensible only once the bundle has also cleared its cost": cost is the next question, and this
  sentence answers the first.

### Q4. Which verdict does Kavya give the pricing team's Rs 2 "big win"?

"p = 0.001 on 3 lakh orders, so the Rs 2 rise in average order is a big win for the pricing team."

The key is d, "Wrong: it beats chance, and Rs 2 an order must still be judged against cost". The
share settles chance; Rs 2 on each order is the size, and only the cost of what produced it says
whether it is a win.

- a, "Defensible: 0.001 is about as strong as evidence gets, so the win is big": reads significance
  as size.
- b, "Defensible, since 3 lakh orders remove any doubt about the rise's size": the count makes the
  rise surely more than chance, and says nothing about whether Rs 2 matters.
- c, "Wrong: on 3 lakh orders any gap turns significant, so this rise is only noise": a large count
  makes a small gap detectable, and a detectable gap is still a real one.

### Q5. What most likely explains the premium-range stores' 25 percent bigger baskets?

The stores that stock the premium range report baskets 25 percent bigger, and the range went only to
stores in the six largest malls.

The key is c, "Where the stores are: large-mall shoppers spent more before the range arrived". The
stores that got the range were already the high-spending stores, and that difference would show a
gap with no range at all.

- a, "The premium range, since it is the only thing that differs between the stores": the malls
  differ too, and the range went only to them.
- b, "Chance: a 25 percent gap across a few stores is the usual wobble": the stores were chosen by
  where they are, so the gap has a cause to check before chance is the answer.
- d, "The season, since premium ranges launch before festivals, when baskets grow": a festival grows
  every store's baskets alike.

### Q6. What would a fair comparison of newsletter openers need?

Members who opened the monthly newsletter bought twice as often as members who did not, and
Marketing wants to send it weekly.

The key is b, "A random half of similar members sent it, and the two halves compared". Chance
deciding who gets the newsletter makes the two halves alike apart from it.

- a, "Members who opened it against those who did not, over six months or more": a longer window
  keeps the choice of who opens.
- c, "Only members who opened it, before and after each issue, over a year": before and after mixes
  in everything else that changed.
- d, "A bigger shuffle test on the same openers and non-openers": a shuffle cannot undo who chose to
  open.

### Q7. What should the note say about delivery times after the warehouse and the courier changed together?

Delivery times fell after the new warehouse opened, in the month the company also moved half its
orders to a faster courier.

The key is d, "Both changed at once, so split orders by courier before crediting either". Two changes
landed together, and splitting by courier separates them in the data the team already has.

- a, "The courier change explains the fall, and the warehouse explains none of it": overclaims for
  the courier.
- b, "The warehouse cut delivery times, since it opened first": first is not the same as cause.
- c, "Nothing, since two changes at once can never be separated in the data": the split can often
  separate them.

## What does problem 3's notebook find, marker by marker?

The head of Retail-Plus asked whether members buy bigger baskets than Retail-Core. Both tiers'
baskets are different customers' orders, so the notebook shuffles the tier labels 5,000 times with
seed 2026. On every booked order Retail-Plus leads by Rs 1,326 an order, 8 orders against 11, and
shuffled labels make a lead that large only 2 times in 1,000. On delivered orders, the money kept,
Retail-Plus has three orders, the lead is Rs 671, and chance makes it about 15 times in 100, because
five of Retail-Plus's eight booked orders were cancelled or returned and they averaged about
Rs 3,800. The definition moved the verdict and the count decided how far to trust it: not yet.

- Marker 1 is c, `r["segment"] in ("Retail-Plus", "Retail-Core")`: the question is about the two
  consumer tiers. a, `r["segment"] != "Student"`, keeps Business, whose lakh-rupee orders would swamp
  any basket comparison; b, `True`, keeps everyone; d,
  `r["segment"] in ("Retail-Plus", "Retail-Core", "Business")`, names Business outright.
- Marker 2 is a, `int(r["amount"])`: every amount in the file converts cleanly with `int()`,
  including the one stored as text, which was Monday's lesson. b, `r["amount"]`, leaves text in the
  list, so the average stops with a `TypeError`; c,
  `int(r["amount"]) if r["status"] == "delivered" else 0`, zeroes every order that was not delivered,
  which answers step 2's question in step 1 and keeps the cancelled orders in the count at zero; d,
  `len(str(r["amount"]))`, measures the length of the text.
- Marker 3 is b, `sum(1 for g in gaps if g >= real) / len(gaps)`: a Retail-Plus lead at least as
  large as the real one is a shuffled gap at or above it. a, `sum(1 for g in gaps if g <= real) / len(gaps)`,
  counts every shuffled gap at or below the real lead, which is nearly every deal; c,
  `real / max(gaps)`, is a ratio with no count of worlds; d,
  `sum(1 for g in gaps if abs(g) >= abs(real) * 2) / len(gaps)`, asks for a gap twice as large.
- Marker 4 is d, `r["status"] == "delivered"`: delivered orders are the money kept. a,
  `r["status"] != "cancelled"`, keeps returns; b, `r["status"] == "returned" or r["status"] == "delivered"`,
  keeps returned and delivered orders, the same as a on this file; c, `r["amount"] != ""`, keeps
  everything.
- Marker 5 is b, `share_kept`: the head of Retail-Plus asked about the money kept, so the share is
  the one on the money kept, and with it the line says not yet. a, `share_booked`, is computed on a
  definition nobody asked about; c, `1 - share_kept`, is its complement, the share of deals with a
  smaller lead; d, `min(share_booked, share_kept)`, picks whichever share flatters the claim.

## What does a model note for problem 4 say?

A model note, 94 words.

**Claim.** We cannot yet say that notifications lift orders.

**Evidence.** The 9 percent gap compares 18 opted-in users, who were already the most active, with
4,000 users who never opted in. With 18 users, one user moves the rate by more than 5 points.

**Caveat.** The users who got notifications chose to, so the gap mixes the notification with who they
already were; p = 0.02 says the gap beats chance, and says nothing about the cause.

**Action.** Since sending costs almost nothing, send to a random half of opted-in users for four weeks
and compare the halves.

## Which wrong answer is worth arguing about?

Item 1, option a. "No effect" sounds like the careful answer, and a room that has spent the day
distrusting small shares will reach for it. A share of 0.20 says chance could have made the gap; it
cannot say the programme did nothing, because a real effect too small for this test would read the
same. The honest line is "not yet, and here is what would tell us".

## Where does this show up at work?

Experiment readouts, pricing tests and campaign reviews reach a senior's desk as sentences like the
four in problem 1, and many business questions first arrive as a store or city comparison like the
ones in problem 2. The checks are the same each time: in which world was the share counted, what else
differs between the groups, which orders count, and how many customers stand behind the number.
