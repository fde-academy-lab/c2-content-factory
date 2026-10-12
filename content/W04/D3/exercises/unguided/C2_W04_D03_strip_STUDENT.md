# Which strip would you ship, priced in rupees and defended?

Swiggy Instamart, Pune. Since Monday 7 September 2026 the cart page's three-slot strip has shown the
items most often found in the same cart. Toned milk is in 71 percent of carts, so it now sits beside
nearly everything, and the strip's click-through (clicks over impressions, the times a slot was shown)
fell from 6.1 percent in the three weeks before to 3.8 percent in the three weeks after. The ask, due
Friday: rank the pairs the strip should show, explain the fall, and put a rupee value on a slot.
Illustrative case: the company is real, the situation and the data are synthetic, built for this
class.

This is the afternoon's unguided set, run on notebook 03 in the same 35 minutes as each group's
one-page strip: the page is what the group hands in, and these four items ask the same steps, so a
group posts its four letters once its page is done.

**Who needs the answer.** The growth lead, who takes one strip and one rupee figure to Friday's
review, where the category manager will argue for milk. A figure that overstates the gain spends the
growth lead's credibility the first time finance checks it.

**The questions on the way.**

- What does re-ranking recover in a month?
- What survives the heavy-buyer check?
- How do you answer the category manager?
- How would the same idea score an AI shopping assistant?

What the morning found, in one table:

| Number | Value | Where it comes from |
|---|---|---|
| Cart-page views a day, each showing all three slots | 60,000 | `strip_log`, mean since 7 September |
| Click-through on slots showing milk, after the change | 1.2 percent | `strip_log` |
| Click-through on every other suggestion, after the change | 6.4 percent | `strip_log` |
| Milk's share of slot impressions, after the change | 50 percent | `strip_log` |
| Adds per click | 0.5, range 0.4 to 0.6 | Assumption; `strip_log` reads 0.50 |
| Margin on an added item | Rs 9, range Rs 7 to Rs 11 | Assumption; a `cart_items` line earns Rs 9.0, milk aside |
| Chips and cold drink, lift per cart | 3.39 | Pairs table |
| Chips and cold drink, lift with every customer counted once | 2.56 | Each cart weighs one over its customer's cart count |

**What you post.** Four letters in item order, with no spaces, in this shape:

```
Post exactly this shape: xxxx
```

---

## What is a slot worth, and what does re-ranking recover?

This comes up at work whenever a placement is sold internally: a team asks for a slot and finance
asks what the slot earns.

### Q1. Milk holds half of the three slots' impressions: what does re-ranking recover in a month?

*Level L5, a design call · asked in global capability centre interviews.* Use the month's 30 days.

a) Rs 12.6 lakh, three slots each Rs 4.2 lakh better off
b) Rs 6.3 lakh, the gap on milk's 1.5 slots' worth
c) Rs 4.2 lakh, one slot's gap for the month
d) Rs 5.2 lakh, one slot's full margin for the month

## Which number survives the doubts, and how is it defended?

This comes up at work whenever a finding meets a check and a stakeholder in the same week.

### Q2. Counted with every customer once, chips and cold drink fall from 3.39 to 2.56: what should the growth lead do?

*Level L4 · asked in product-company interviews.*

a) Drop the pair, since heavy buyers produced the whole of its pull
b) Keep quoting 3.39 and leave the heavy buyers out of Friday's note
c) Hold every slot until each pair is recounted once per customer
d) Keep the slot and quote 2.56, the number that survives the check

### Q3. The category manager says "milk is our top seller; put it in every slot": which reply concedes what is true and answers the rest?

*Level L5 · asked in every stakeholder round.*

a) "Milk's confidence is only 0.74, which is too low to earn any slot on the strip."
b) "Milk is in most carts, so it needs no reminder: it clicks 1.2 percent against 6.4."
c) "Milk is in nearly every cart, so drop it from search and from the home screen too."
d) "Fine: milk takes every slot for the next two weeks, and we decide after that."

## How would the same idea score an AI shopping assistant?

This comes up in AI-company interviews, where a model's suggestions are judged by the same base rate.
Held-out carts are past carts the assistant never saw while it was built, and a popularity baseline
is a rule that always suggests the most popular items.

### Q4. An AI shopping assistant suggests add-ons and shoppers accept many of them: how should it be scored first?

*Level L6, a design call · asked in AI-startup interviews.*

a) By its acceptance rate on live traffic, the share of its suggestions that shoppers take
b) By the average confidence of the item pairs that sit behind each of its suggestions
c) By the lift of its accepted suggestions over a popularity baseline on held-out carts
d) By how many distinct items it manages to suggest across a whole week of carts
