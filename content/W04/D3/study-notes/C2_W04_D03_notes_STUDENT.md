# Which pairs beat chance on Instamart's Pune carts, and what is a strip slot worth?

Week 4, Wednesday. About 13 minutes to read, and 10 more for the self-check.

Swiggy Instamart, Pune. On Monday 7 September 2026 the cart page's strip of three suggested items
switched from a curated list to the items most often found in the same cart, and its click-through
fell from 6.1 percent to 3.8 percent. Illustrative case: the company is real, the situation and the
data are synthetic, built for this class.

---

## What can you do after Wednesday?

- You can count support, confidence and lift from four counts on paper, then for every pair of
  40,000 carts in code, and check a lift by a second route.
- You can read a blended click-through as a mix of two rates and find the part that moved.
- You can rank pairs by lift above a support floor and park a strong pair on few carts on a watch
  list.
- You can price a slot in rupees with each assumption's range, and name the cost line most people
  forget.

## Where does Wednesday sit in the week?

**What was worked, and what was only mentioned.** Wednesday counted three measures by hand on ten
tea-stall orders and twelve real carts, then on all 40,000 carts; split the click-through by what each
slot suggested; ranked pairs above a floor; priced a slot; and checked the ranking with every
customer counted once and the curd stock-out set aside. Cause was only mentioned, since a count
cannot say whether a suggestion makes a sale, and upsell was named and left for later.

```mermaid
flowchart LR
    M["<b>Mon · Uber</b><br/>trips an online hour<br/>1.9 to 1.6"] --> T["<b>Tue · Uber</b><br/>Rs 314 to Rs 260<br/>an hour, one slide"]
    T --> W["<b>Wed · Instamart</b><br/>beyond chance"]
    W --> H["<b>Thu · Zomato Gold</b><br/>beyond the blend"]
    H --> F["<b>Fri · Flipkart</b><br/>beyond the baseline"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class W lit
```

Each day of Week 4 asks what a number is compared with; Wednesday compares two items sharing a cart
with what chance alone would give. It prepares you for a growth lead asking "which items should we
show together?" and, at once, "compared with what?".

**What was left out.** The IITGN faculty session after class (tentative) reads the same three numbers
as probabilities and shows how a support floor lets an algorithm skip most combinations. Whether a
suggestion causes a sale needs a randomised test, the subject of Monday's faculty session (tentative).

## Which one picture holds the day?

![Ten invented tea-stall orders as dots in two circles, beside the 2 by 2 table of counts](../whiteboards/C2_W04_D03_ten_dots_STUDENT.png)

Call it **the ten dots**: ten invented tea-stall orders, chai in 6, biscuit in 4, both in 3. Every
measure of the day is a ratio of cells in that table.

$$\text{support} = \frac{3}{10} = 0.30 \qquad \text{confidence}(\text{chai} \to \text{biscuit}) = \frac{3}{6} = 0.50 \qquad \text{lift} = \frac{3}{10 \times 0.6 \times 0.4} = \frac{3}{2.4} = 1.25$$

Support asks how often, confidence how reliably from one side, and lift how far above chance, the
same from either side. Every later section comes back to this picture.

---

## What does "together" mean, counted on twelve carts by hand?

**Who needs the answer.** The category manager, who decides what the strip may suggest: a strip
filled on the wrong count wastes the three spaces under every cart.

**The questions on the way.**

- How often do two items share a cart?
- How reliably does one bring the other?
- Do they meet more often than chance would put them together?
- What can twelve carts not tell you?

On the ten dots, confidence from biscuit to chai is 3 of 4, 0.75, against 0.50 the other way, and
lift is 1.25 from both sides. "Chai lifts biscuit sales by 25 percent" is the tempting wrong sentence,
since lift counts and never names a cause. An invented carry bag in 9 of the 10 orders, and in 3 of
the 4 biscuit orders, reads confidence 0.75 from biscuit, yet its lift is 0.75 / 0.90 = 0.83, below
chance: the item in every bag earns high confidence toward everything.

The twelve cart cards are twelve real carts of the 40,000.

| Count | Bread and milk | Chips and cold drink | Ice cream and chocolate sauce |
|---|---|---|---|
| Carts with each item | 4 and 8 | 3 and 3 | 1 and 1 |
| Carts with both | 4 | 2 | 1 |
| Expected by chance | 12 x 4/12 x 8/12 = 2.67 | 12 x 3/12 x 3/12 = 0.75 | 0.08 |
| Lift | 1.50 | 2.67 | 12 |

**WATCH OUT.** Confidence 1.00 from bread to milk reads like a bundle. The tell is a partner in most
carts anyway, 8 of 12 here, and the check is lift.

**IN THE FIELD.** Amazon's recommendation team wrote that counting how often buyers of one item
bought another would have put a bestseller beside everything, with Harry Potter books and trash bags
as their example; the fix compared what was seen with what chance would predict (Amazon Science,
checked 12 October 2026).

**CALLBACK.** Week 1, Monday: every rate names what it divides by.

**The answer.** Support counts how often, confidence how reliably from one side, lift how far above
chance from both sides. Twelve carts cannot tell a real pull from four lucky carts.

## What do 40,000 carts say, and why did the click-through fall?

**Who needs the answer.** The growth lead, who explains the fall on Friday to a category manager
defending milk as the top seller.

**The questions on the way.**

- How often is each item in a cart?
- Which pairs sit together most often, and is that the ranking?
- What does lift say about milk?
- Why did the click-through fall?

**Two ways to count every pair.** Testing each of the 1,711 possible pairs against every cart makes
about 68 million checks; turning each cart into a set and letting `Counter` add the pairs it holds
makes about 433,000, since a cart holds 4.7 items on average. Notebook 02 runs the second way.

```python
baskets = items.groupby("cart_id").item.apply(set)                          # one set per cart
pair_count = Counter(p for b in baskets for p in combinations(sorted(b), 2))  # every pair once
```

Milk is in 71 percent of carts, bread in 34. Ranked by count, every one of the six most frequent
pairs holds milk, led by bread and milk on 10,064 carts, and that table has been the strip's ranking
since 7 September.

Bread to milk reads confidence 0.74, close to milk's own 0.71, so lift is 1.04: chance puts both in
9,656 carts, and 10,064 hold them. Twelve carts said 1.50; 40,000 say 1.04, because a few carts can
make a pull look strong. For all 50 items in at least 2 percent of carts, lift with milk runs 0.99 to
1.04, while chips and cold drink read a weak-looking confidence of 0.42 and lift 3.39.

**The second route.** Lift is also confidence over the partner's share: 0.74 / 0.71 = 1.04 from
bread's side and 0.35 / 0.34 = 1.04 from milk's.

**Why the click-through fell.** Before the change milk held 2 percent of slot impressions; after it,
50 percent. Milk's slots click at 1.2 percent and every other suggestion at 6.4, up from 6.2.

$$0.5 \times 1.2\% + 0.5 \times 6.4\% = 3.8\%$$

Slot 1 draws 8.2 percent for a suggestion other than milk and slot 3 draws 5.4, and milk took 70
percent of slot 1.

**WATCH OUT.** "Shoppers changed after the monsoon" fails the split, because the rate on everything
except milk rose. A blended rate can fall while every part of it holds.

**IN THE FIELD.** Beer and diapers, told accurately: in 1992 an analysis of about 1.2 million Osco
Drug baskets found the two together in the early evening, no shelf was moved on the strength of it,
and the vivid version is largely invented (The Register, checked 12 October 2026).

**ORIGIN.** Rules measured by support and confidence come from Agrawal, Imielinski and Swami, "Mining
association rules between sets of items in large databases", ACM SIGMOD 1993.

**The answer.** Milk tops every count because it is in 71 percent of carts, and lift divides that
popularity out to 1.04. The click-through fell because milk took half the impressions at 1.2 percent.

## Which pairs fill the strip, and what is a slot worth in rupees?

**Who needs the answer.** The growth lead, who takes a ranked strip and a rupee figure to Friday's
review, where the category manager will argue that milk anchors the cart.

**The questions on the way.**

- Which pairs beat chance by enough, on enough carts?
- What should the watch list do with a strong pair on few carts?
- What is a slot worth in rupees?
- What can the counts not tell us?

**Four ways to rank, and the call.** By count or by confidence, milk fills the strip. By lift alone,
ice cream and chocolate sauce take slot 1 at 4.60 on 100 carts. By lift above a floor of 1 percent of
carts, 400 carts, 246 pairs qualify and four beat chance clearly: chips and cold drink 3.39, coriander
and green chillies 3.00, bread and butter 2.21, onions and tomatoes 1.70. The call is the fourth way;
a cheaper slot would change it by letting a lower floor admit thinner pairs.

![Every pair with support of at least 0.1 percent: lift against support, with the 1 percent floor](../whiteboards/C2_W04_D03_action_map_STUDENT.png)

**The watch list.** Ice cream and chocolate sauce rest on 100 carts, support 0.25 percent, too thin
to repay a slot shown on every cart page; the pair is tried in two zones for two weeks first.

**The slot in rupees.**

$$60{,}000 \text{ views a day} \times 6.4\% \times 0.5 \text{ adds per click} \times \text{Rs } 9 = \text{Rs } 17{,}280 \text{ a day}$$

Showing milk at 1.2 percent, the slot earns Rs 3,240. The gap, Rs 14,040 a day, is about Rs 4.2 lakh
a month a slot, and milk holds 1.5 slots' worth, so re-ranking recovers about Rs 6.3 lakh a month:
Rs 3.9 lakh to Rs 9.3 lakh as the assumed add rate runs from 0.4 to 0.6 and the margin from Rs 7 to
Rs 11.

**WATCH OUT.** Booking sales as the gain: 1,920 adds a day at about Rs 42 each looks like Rs 80,197 of
daily strip revenue, four times the Rs 17,280 of margin. A bundle discount comes off the margin too,
for adds that might have happened anyway.

**IN THE FIELD.** Swiggy's letter for the quarter to June 2025 describes Maxxsaver, a discount
unlocked once a basket passes a threshold, as funnelling part of the larger basket's margin back to
the user; over 28 percent of MTUs used it, and Instamart's average order value rose 16 percent on the
quarter to Rs 612 (Swiggy Q1 FY26 letter, checked 12 October 2026). That discount is the cost line.

**Six doubts, each with its check.**

| Doubt | The check | What it showed |
|---|---|---|
| Together is no proof of cause | A holdout that changes the strip | Needs Monday's A/B test (tentative) |
| Heavy buyers | Count each customer once | Chips and cold drink fall from 3.39 to 2.56; bread and milk stays 1.04 |
| The curd stock-out | Set aside two zones, 15 to 21 September | Curd's share rises from 26.0 to 27.8 percent; lift with milk stays 1.01 |
| Time of day | Each time band alone | Bread with milk reads 1.03 to 1.05 in every band |
| The strip's own pull | Click-through by slot | Slot 1 draws 8.2 percent, slot 3 5.4 |
| A customer places many carts | The heavy-buyer check | The top tenth place 38 percent of carts and 73 percent of the chips and cold drink carts |

**IN THE FIELD.** Uber's 10-K for 2025 says consumers using both rides and delivery generated over
three times the gross bookings of single-product consumers (checked 12 October 2026). That is an
outcome and no proof of cause, since a heavy user is likelier to try a second product anyway.

**The answer.** Chips with cold drink, coriander with green chillies and bread with butter fill the
strip, ice cream and chocolate sauce wait, and re-ranking recovers about Rs 6.3 lakh a month.

---

## Where does this show up in the work?

| Situation | The decision | What the wrong count costs |
|---|---|---|
| A quick-commerce app's "goes well with" strip | Which items fill the slots under every cart | Slots spent on staples: Rs 14,040 a day a slot here |
| A merchandiser's bundle discount | Whether a pair earns a promotion | The discount handed back on adds that would have happened anyway |
| An LLM shopping assistant | How to score its add-on suggestions before launch | An assistant praised for suggesting milk, which shoppers were buying already |

Tonight's lab meets the same claim at Kalpa Retail: pair everything with the Rs 199 charger, "in 80
percent of baskets".

## Can you answer these without notes?

1. Which measure answers "do these two meet more often than chance?"
2. Of 40,000 carts, 6,000 hold coriander, 3,200 green chillies and 1,440 both: what is the lift?
3. Milk holds half the impressions at 1.2 percent and the rest click at 6.4: what is the blend?
4. A pair reads lift 4.60 on 100 carts in four weeks: does it get a slot?
5. Which lift does the growth lead quote for chips and cold drink, and why?
6. From Tuesday: an objection is partly right; what are the four moves of the answer?

**Key.** 1: lift (the ten dots). 2: 1,440 x 40,000 / (6,000 x 3,200) = 3.00 (the 40,000 carts). 3:
3.8 percent (the 40,000 carts). 4: no, the watch list (the strip). 5: 2.56, since heavy buyers
inflate 3.39 (the six doubts). 6: restate, answer from the evidence, concede what is true, say what
would change your mind (Tuesday's notes).

## Which interview questions does Wednesday prepare you for?

| The question as asked | The hire-grade line |
|---|---|
| Support, confidence, lift: which cannot be fooled by popularity, and why? | Lift, since it divides by what chance gives: bread to milk reads 0.74, but milk is in 71 percent of carts, so lift is 1.04 |
| Lift 4.6 on support of 0.25 percent: act? | Not yet: 100 carts cannot repay a slot shown to everyone, so it goes on the watch list |
| Heavy buyers buy everything: what does that do to lift? | It inflates the pairs they repeat; counted once per customer, chips and cold drink fall from 3.39 to 2.56 |
| Make it a rupee recommendation: which cost line do most forget? | Margin, never sales, less any discount handed back on adds that would have happened anyway |

**The AI-company variant.** An LLM shopping assistant's add-ons are scored offline by their lift over
a popularity baseline on held-out carts, then online by a holdout. The transcript is in `extras/`.

**The guesstimate: orders a dark store handles in a day.** Households in the catchment, times the
share ordering in a week, times orders a week, over seven: assuming 40,000, 15 percent and 1.5 gives
about 1,290 (about 430 to about 2,860 across the ranges). Swiggy reported 1,089 across 1,171 stores in
the quarter to June 2026 (Q1 FY27 letter, checked 12 October 2026), counted per active store-day, so a
new store counts only once it is live.

## Which words did Wednesday use?

| Term | Plain meaning | Where it appeared | Example |
|---|---|---|---|
| Support | Share of all carts holding both items | The ten dots | Chips and cold drink: 5.0 percent |
| Confidence | Share of A's carts that also hold B | The twelve carts | Bread to milk: 0.74 |
| Lift | Carts with both, over the carts chance alone gives | Every chapter | Chips and cold drink: 3.39 |
| Base rate | How common an item is across all carts | The 40,000 carts | Milk: 71 percent |
| Support floor | The fewest carts a pair needs to take a slot | The strip | 1 percent, 400 carts |
| Click-through | Clicks divided by impressions | The ticket | 6.1 percent before, 3.8 after |
| Blended rate | One rate mixing groups that have different rates | The 40,000 carts | 3.8 percent from 1.2 and 6.4 |
| Margin | What the business keeps from a sale after the item's cost | The strip | Rs 9 an added item |
| Watch list | Strong pairs on too few carts, tried before promotion | The strip | Ice cream and chocolate sauce |

## Where should you read next, and how long does each take?

| Order | Source | Time |
|---|---|---|
| 1 | Practical Business Python, "Introduction to Market Basket Analysis in Python", the lift section, https://pbpython.com/market-basket-analysis.html (checked 12 October 2026) | 20 minutes |
| 2 | StatQuest, "Conditional Probabilities, Clearly Explained!!!", https://www.youtube.com/watch?v=_IgyaD7vOOA (checked 12 October 2026) | length not verified |
| 3 | Amazon Science, "The history of Amazon's recommendation algorithm", https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 12 October 2026) | 15 minutes |
| 4 | IBM Technology, "What is an AI Recommendation Engine?", https://www.youtube.com/watch?v=gEdePRsDACc (checked 12 October 2026) | 11 minutes |
