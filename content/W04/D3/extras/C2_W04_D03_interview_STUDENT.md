# How does a strong candidate answer "which measure cannot be fooled by popularity?"

Written for this programme in the style of product-company and GCC screens; the facts inside are
from the case file. The numbers are Wednesday's Swiggy Instamart case in Pune. Illustrative case: the
company is real, the situation and the data are synthetic, built for this class.

**Who needs the answer.** You, before any analytics, product or AI-startup screen that asks about
recommendations, bundles or "frequently bought together". The interviewer is deciding whether you
see the base rate before you see the bundle.

**The questions on the way.**

- What does the interviewer say?
- Which clarifying questions come first?
- What structure carries the answer?
- Which trap is being fished for?
- How do a weak and a hire-grade answer compare?
- What follows up, and which line answers each?
- How does the same question come up at an AI company?
- Which pain points hide inside the question?
- What does the scorer listen for?

## What does the interviewer say?

> "You have a year of shopping carts. Support, confidence, lift: which one cannot be fooled by
> popularity, and why?"

## Which clarifying questions does a strong candidate ask first?

1. "Is a basket one order, or everything a customer bought in a month?" The answer decides the
   denominator.
2. "Are we choosing what to show, or measuring whether showing it worked?" The first is a ranking,
   the second needs a test.
3. "How many baskets does the rarest pair we care about sit in?" The answer decides whether a floor
   is needed.

## What structure carries the answer?

1. Keep the three questions apart: how often (support), how reliably (confidence), how far above
   chance (lift).
2. Name the base rate: how common the partner is in every basket.
3. Put one number on each side: a popular pair that looks strong, and a real pair that looks weak.
4. State the floor and the decision.
5. Name the limit: meeting more than chance is no proof of cause.

## Which trap is the interviewer fishing for?

The candidate picks confidence because "it is the probability they are bought together", or names
lift without saying what it divides by. Either answer ranks milk beside everything.

## How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| The pick | "Confidence, because it is the probability of B given A." | "Lift, because it divides by the base rate." |
| The number | "Bread to milk is 0.74, so I would show milk beside bread." | "Bread to milk reads confidence 0.74, but milk is in 71 percent of carts anyway, so lift is 0.74 over 0.71, 1.04: chance." |
| The other side | Not reached. | "Chips and cold drink read confidence 0.42, which sounds weak, and lift 3.39." |
| The floor | Not reached. | "I rank by lift above a support floor, 1 percent of carts here, because a lift on a few carts can be luck." |
| The limit | Not reached. | "Lift says the two meet more than chance. Whether a suggestion causes a sale needs a holdout." |

## What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "A pair has lift 4.6 and support 0.25 percent. Do you act?" | "Not yet: 100 carts in four weeks cannot repay a slot shown on every cart page, so it goes on a watch list and a two-zone trial." |
| "Heavy buyers buy everything. What does that do to lift, and what is the fix?" | "They inflate the pairs they repeat. Count each customer once: chips and cold drink fall from 3.39 to 2.56 and still beat chance. Amazon's team measured the base rate per purchase for the same reason (W1, Amazon Science, checked 12 October 2026)." |
| "Turn it into a rupee recommendation. Which cost line do most people forget?" | "Margin, never sales: a slot at 6.4 percent earns Rs 17,280 a day against Rs 80,197 of sales. Any discount is margin handed back on adds that might have happened anyway, which is how Swiggy's own letter describes Maxxsaver (W4, Swiggy Q1 FY26 letter, checked 12 October 2026)." |

## How does the same question come up at an AI company?

> "Our LLM shopping assistant suggests add-ons at checkout, and shoppers accept a lot of them. Is it
> working?"

The base-rate trap, restated for a model. An assistant that suggests milk is accepted often because
shoppers were buying milk anyway, so its acceptance rate flatters it the way confidence flattered
milk. A strong answer scores it in two steps. Offline, on carts held out from its training, count how
often each suggestion lands in the held-out cart, and compare it with a popularity baseline that
always suggests the most common items: the assistant earns its place only by beating that baseline,
which is lift over the base rate. Online, run a holdout, with the assistant on half the carts and the
baseline on the other half, and score incremental adds per cart times margin, less what the
suggestions cost. This variant is written for this programme and names no company's figures.

## Which pain points hide inside the question, each with a real case?

| Pain point | The case | The check |
|---|---|---|
| The popular partner looks like everyone's bundle | Amazon's team wrote that counting co-purchases would put a bestseller beside everything, with Harry Potter books and trash bags as their example (W1, Amazon Science, checked 12 October 2026) | Lift, over the partner's own share |
| Heavy buyers inflate every count | Amazon later measured the base rate per purchase (W1, the same source) | Count each customer once |
| A legend repeated as fact | Beer and diapers: in 1992, about 1.2 million Osco Drug baskets showed the pair in the early evening, and no shelf was moved (W2, The Register, checked 12 October 2026) | Ask what was decided, and what it cost |
| A cross-sell outcome read as a cause | Uber's 10-K for 2025: consumers using rides and delivery generated over three times the bookings of single-product consumers (W4, checked 12 October 2026) | Ask who chose to use both |
| A discount that hands margin back | Swiggy describes Maxxsaver as returning part of a larger basket's margin to the user; over 28 percent of MTUs used it (W4, Swiggy Q1 FY26 letter, checked 12 October 2026) | Price the discount on the adds that would have happened anyway |

## What does the scorer listen for?

When you practise in pairs, the asker scores each of these from 0 to 2: clarified the scope; named
the denominator and the window; saw the paradox (a high confidence that means nothing); sized it
with a unit; said what would change their mind; tied it to a decision and its cost; gave the
structure before the number.
