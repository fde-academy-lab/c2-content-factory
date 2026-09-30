# Which answers hold in the second case on Marketing's pushback, and why?

Answers: 1b 2c 3d 4a 5b 6d 7a 8b

In the growth review, with Meera Raghavan, Kalpa Retail's CEO, listening, the marketing lead called
the split by segment cherry-picking: "Exposed Retail-Plus members spent Rs 4,850 in August. That is
far above the Rs 3,200 our unexposed customers averaged. The sale works." The table is the August
list of 160 Retail-Plus and Retail-Core customers, each flagged exposed if the monsoon sale, 15
percent off, reached them, with one average August spend per group. Pairs worked the answer in
`notebooks/C2_W01_D04_ex2_second_case_STUDENT.ipynb`, eight lettered choices in four parts, and the
executed solution, `C2_W01_D04_ex2_second_case_solution_STUDENT.ipynb` in this folder, runs every key.
Two of the eight items are design items: 4, the comparison that is fair to Marketing's claim, and 8,
whom the Diwali coin draws from.

**Who needs the answer.** You and your partner, checking your eight letters and your reply before the
debrief moves on. Meera signs off Diwali's sale, and a pair that cannot answer a correct number that
rests on an unfair comparison, or that calls Marketing's arithmetic wrong, hands the sale back to
Marketing.

**The questions on the way.**

- Which idea does this case test?
- Which numbers stand behind the reply, part by part?
- Why is each key right, marker by marker?
- What reply held the line?
- Where did pairs go wrong?
- Where does this show up at work?

## Which idea does this case test?

A pushback is answered from the same table as the claim: reproduce the stakeholder's numbers first,
show who sits in each group, rebuild the comparison like for like with its counts, and offer the test
that would settle it. Marketing's arithmetic is right throughout; the comparison is what fails.

## Which numbers stand behind the reply, part by part?

| Part | Number | What it shows |
|---|---|---|
| 1 | Exposed Retail-Plus Rs 4,850 (30 customers); all unexposed Rs 3,200 (100 customers) | Marketing's arithmetic is right |
| 2 | Exposed group 50 percent Retail-Plus; unexposed group 40 percent Retail-Plus, 60 percent Retail-Core | The two groups differ before any discount |
| 3 | Retail-Plus Rs 4,850 against Rs 5,000 on 30 and 40 customers, 3.0 percent less; Retail-Core Rs 1,940 against Rs 2,000, 3.0 percent less; in the unexposed group's mix the exposed spend Rs 3,104 against Rs 3,200, 3.0 percent less | Like for like, the sale went with lower spending |
| 4 | If the list's spend is at list price, the exposed paid Kalpa about Rs 2,886 per customer against Rs 3,200, 9.8 percent less; one in five of each segment held back at Diwali is 14 Retail-Plus and 18 Retail-Core customers, about Rs 6,360 forgone at Marketing's own 6 percent | The question Marketing has to answer, and the price of settling it |

## Why is each key right, marker by marker?

### Q1. Which line reproduces Marketing's Rs 4,850?

The notebook's `avg(segment, flag)` gives a segment's average August spend for the exposed or the
unexposed.

The key is b, `avg("Retail-Plus", "yes")`. Marketing quoted exposed Retail-Plus members.

- a, `avg("Retail-Plus", "no")`: the unexposed Retail-Plus average, Rs 5,000.
- c, `avg("Retail-Core", "yes")`: exposed Retail-Core.
- d, `mean([int(r["august_revenue"]) for r in EXPOSURE])`: averages the whole list.

### Q2. Which line reproduces Marketing's Rs 3,200?

Marketing's second figure is "the Rs 3,200 our unexposed customers averaged".

The key is c, `mean([int(r["august_revenue"]) for r in EXPOSURE if r["exposed"] == "no"])`. Marketing's
Rs 3,200 is every unexposed customer, both segments together.

- a, `avg("Retail-Core", "no")`: one segment only.
- b, `avg("Retail-Plus", "no")`: one segment only.
- d, `mean([int(r["august_revenue"]) for r in EXPOSURE if r["exposed"] == "no" and r["segment"] == "Retail-Plus"])`:
  keeps only unexposed Retail-Plus, which gives Rs 5,000.

### Q3. What share of Marketing's unexposed customers are Retail-Core?

The notebook shows who sits in each group and asks for the make-up of the unexposed group.

The key is d, `count("no", "Retail-Core") / count("no")`. Retail-Core customers over all unexposed
customers is the unexposed group's make-up: three in five.

- a, `count("no", "Retail-Core") / len(EXPOSURE)`: divides by the whole list.
- b, `count("yes", "Retail-Core") / count("yes")`: the exposed group's Retail-Core share.
- c, `mix_no["Retail-Plus"]`: the unexposed Retail-Plus share, the other two in five.

### Q4. What is the like-for-like comparison for exposed Retail-Plus?

A design item. The exposed Retail-Plus average, Rs 4,850, needs a comparison that is fair to it.

The key is a, `avg("Retail-Plus", "no")`. Like for like is exposed Retail-Plus against unexposed
Retail-Plus, Rs 4,850 against Rs 5,000: 3.0 percent less.

- b, `marketing_no`: Marketing's mixed group again.
- c, `avg("Retail-Core", "no")`: sets one segment against another.
- d, `avg("Retail-Plus", "yes")`: divides the group by itself.

### Q5. Which weights make the exposed group's average comparable with Marketing's Rs 3,200?

Marketing's Rs 3,200 averages the unexposed customers, 40 percent Retail-Plus and 60 percent
Retail-Core.

The key is b, `mix_no[s]`. Weighting the exposed segment averages by the unexposed group's mix puts
both sides in one mix, which removes the mix difference: Rs 3,104 against Rs 3,200, 3.0 percent less.

- a, `mix_yes[s]`: keeps the exposed mix, which rebuilds the blend.
- c, `0.5`: an even split, which on this list is the exposed mix again.
- d, `count("yes", s) / len(EXPOSURE) * 2`: divides by the whole list and doubles, which matches
  neither group.

### Q6. How many customers stand behind the like-for-like Retail-Plus comparison?

The rule for the pair is that every average carries the customers behind it.

The key is d, `(count("yes", "Retail-Plus"), count("no", "Retail-Plus"))`. The like-for-like
comparison stands on 30 exposed and 40 unexposed Retail-Plus customers.

- a, `(count("yes"), count("no"))`: the two whole groups, the blend's base.
- b, `(count("yes", "Retail-Plus"), count("no", "Retail-Core"))`: sets exposed Retail-Plus against
  unexposed Retail-Core.
- c, `(len(EXPOSURE), 0)`: counts the list with nobody against it.

### Q7. At list price, how did what the exposed paid Kalpa compare with the unexposed?

The list does not say whether its spend is before or after the 15 percent off, and the notebook
supposes list price.

The key is a, `blend_yes * (1 - off) / marketing_no - 1`. At list price an exposed customer paid 85
percent of the figure on the list, so the exposed group paid about Rs 2,886 per customer against
Rs 3,200: 9.8 percent less.

- b, `blend_yes / marketing_no - 1 - off`: subtracts a price cut from a spend gap, two different
  quantities.
- c, `blend_yes / (marketing_no * (1 - off)) - 1`: discounts the unexposed group, who paid full price.
- d, `(blend_yes - off) / marketing_no - 1`: takes 0.15 of a rupee off the average.

### Q8. How many customers does the Diwali coin keep out, inside each segment on the list?

A design item. A coin keeps one in five out of the Diwali sale inside each segment on the list.

The key is b, `{s: (count("yes", s) + count("no", s)) // 5 for s in PAIR}`. One in five of each
segment's customers on the list, exposed last time or not, is 14 Retail-Plus and 18 Retail-Core,
about Rs 6,360 forgone at Marketing's 6 percent.

- a, `{s: count("yes", s) // 5 for s in PAIR}`: samples only the customers Marketing picked last time.
- c, `{s: count("no", s) for s in PAIR}`: holds back every unexposed customer, which is the old
  unfair split.
- d, `{"Retail-Plus": (count("yes", "Retail-Plus") + count("no", "Retail-Plus")) // 5}`: leaves
  Retail-Core out, so a lift there could never be checked.

## What reply held the line?

"We split it because the sale reached more Retail-Plus members, who spend more anyway: inside
Retail-Plus, the 30 customers who got the sale spent 3 percent less than the 40 who did not, and if
your August figures are at list price, the exposed group paid Kalpa about 10 percent less per
customer. Let us hold back one in five of each segment at Diwali, which costs about Rs 6,360 even at
your 6 percent, and we will know."

## Where did pairs go wrong?

| Wrong move | Why it fails |
|---|---|
| Arguing that Marketing's numbers are wrong | They are right; the comparison is what fails, and saying so keeps the room |
| Comparing exposed Retail-Plus with exposed Retail-Core | That compares two segments, which says nothing about the discount |
| Treating 3 percent less as proof the sale caused a fall | The list gives one figure per group, so the spread is unseen; the Diwali hold-back settles it |
| Taking the 15 percent off the spend without asking | The list does not say whether its spend is before or after the discount, so the pair asks |
| Holding back only customers Marketing picked last time | A coin across each segment's whole list is what makes the held-back group like the rest |

## Where does this show up at work?

A campaign owner often defends a campaign with the comparison that flatters it, and with correct
arithmetic. The reply that holds is the one this case rehearses: the owner's number rebuilt
first, the groups shown side by side, the like-for-like figure with its counts, and a cheap test
offered that would settle it either way.
