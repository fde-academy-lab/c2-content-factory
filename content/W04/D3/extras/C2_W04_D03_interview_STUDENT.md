# How does a strong candidate answer "which measure cannot be fooled by popularity?"

Written for this programme in the style of product-company and GCC screens; the facts inside are
from the case file. A screen is an interview round, and a GCC, a global capability centre, is a
multinational company's own technology and analytics centre in India. The numbers are Wednesday's
Swiggy Instamart case in Pune. Illustrative case: the company is real, the situation and the data are
synthetic, built for this class.

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
2. "Which window? A year mixes seasons, so I would rank on the last four weeks and refresh weekly."
   The answer decides what the base rate is measured on.
3. "Are we choosing what to show, or measuring whether showing it worked?" The first is a ranking,
   the second needs a test.
4. "How many baskets does the rarest pair we care about sit in?" The answer decides whether a floor
   is needed.

## What structure carries the answer?

1. Keep the three questions apart: how often (support), how reliably (confidence), how far above
   chance (lift).
2. Name the base rate and the window it is measured on.
3. Put one number on each side: a popular pair that looks strong, and a real pair that looks weak.
4. State the floor, the decision and the result that would change it.
5. Name the limits: direction, the strip's own feedback, and cause.

## Which trap is the interviewer fishing for?

The candidate picks confidence because "it is the probability they are bought together", or names
lift without saying what it divides by. Either answer ranks milk beside everything.

## How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| The pick | "Confidence, because it is the probability of B given A." | "Lift, because it divides by the base rate. Support and confidence both crown milk: bread and milk share 25.2 percent of carts, and bread to milk reads confidence 0.74, because milk is everywhere." |
| The window and the number | "Bread to milk is 0.74, so I would show milk beside bread." | "In September's sample of 40,000 Pune carts, every cart of 12,000 customers, milk is in 71 percent, so bread to milk's lift is 0.74 over 0.71, 1.04: bread buyers take milk 4 percent more often than shoppers in general. At this size that may be real, and it is far too small to spend a slot on." |
| The other side | Not reached. | "Chips and cold drink read confidence 0.42, which sounds weak, and lift 3.39." |
| The floor | Not reached. | "I rank by lift above a floor of 1 percent of carts, 400 carts, and give a slot only at a lift of 1.5 or more, because a lift on a handful of carts moves by luck: one shared cart in twelve gave a lift of 12." |
| What would change the call | Not reached. | "If chips and cold drink fell near one with each customer counted once, or if chips buyers shown cold drink in the strip bought it no more often than chips buyers in a holdout who never see the strip, I would drop it." |
| The limits | Not reached. | "Lift says nothing about direction: ice cream to sauce reads 0.06 and sauce to ice cream 0.18. And after 7 September it partly counts carts the strip itself filled, so I would check it on a holdout's carts, which never saw the strip." |

## What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "A pair has lift 4.6 and support 0.25 percent. Do you act?" | "The pair is real: 100 carts against the 22 chance gives. The strip suggests it only beside ice cream, which is in 4 percent of carts, so about 2,400 of the strip's 60,000 views a day if views follow carts. Sauce earns Rs 37.40 of margin an add against milk's Rs 2, so clicking like the other suggestions in place of milk it would earn about Rs 85,000 a month: worth a test, though 100 carts cannot say how shoppers will click it. It goes on a watch list: in two zones a random half of shoppers see it beside ice cream, and it takes the slot only if their ice-cream carts buy sauce more often than the other half's, by a gap set before the trial, with margin per shopper as the guardrail. A whole cart's margin swings too much to show a gain this size, and the trial's length is fixed from the count it needs before day one." |
| "Heavy buyers buy everything. What does that do to lift, and what is the fix?" | "Two effects. Heavy buyers repeat the party pair, with 73 percent of its carts from the top tenth of customers, so counting each customer once takes 3.39 to 2.56. And bigger baskets hold any pair by chance, so the expected count should come from each cart's size, the cart-level version of the per-purchase baseline Amazon's team adopted (Amazon Science, checked 12 October 2026). Sized that way, chips and cold drink reads 2.48, and onions and tomatoes falls from 1.70 to 1.38, below the 1.5 I set for a slot. Corrected for both, chips and cold drink still reads 1.95 and keeps its slot, and onions and tomatoes no longer earns one." |
| "Turn it into a rupee recommendation. Which cost line do most people forget?" | "Incrementality: some strip adds would have come through search or habit anyway. Assuming 0.5 adds per click and Rs 9 margin, moving milk's half of the slots to pairs that click like the rest recovers about Rs 6.3 lakh a month, Rs 3.9 lakh to Rs 9.3 lakh across the ranges, before that share comes off, and only a holdout measures it. Priced at milk's own Rs 2 a pouch it is about Rs 7.5 lakh, so Rs 6.3 lakh is the cautious figure. Any bundle discount is also paid on carts that would have bought anyway, and the gain is margin: a slot's adds ring up Rs 80,197 of sales a day, of which only the Rs 17,280 margin counts." |

## How does the same question come up at an AI company?

> "Our LLM shopping assistant suggests add-ons at checkout, and shoppers accept a lot of them. Is it
> working?"

The strong candidate clarifies first: "Accepted how: tapped, added or paid for? How many of those
carts held the item anyway? And compared with what: no suggestions, or the best strip we could ship
without it?"

Acceptance flatters an assistant the way confidence flattered milk: shoppers accept milk because
they were buying milk anyway. Offline scoring is only a gate. On carts placed after a cutoff date,
hide one item in each cart and check that the assistant recovers it more often than a popularity
list and the strip re-ranked by lift do, counting each customer once and leaving out the staples
each shopper buys every week. Amazon's Prime Video team learned why the cutoff matters: its first
autoencoder trailed a list of the past two weeks' most popular rentals until it was trained on
viewing before a cutoff and scored on the two weeks after it (Amazon Science, checked
12 October 2026).

The online test decides. Customers, never carts, are randomised into three arms (no suggestions, the
strip re-ranked by lift, and the assistant) for at least two full weeks, so every weekday appears
twice, and for as long as the count the test needs, fixed before launch. The re-ranked strip is the
bar because re-ranking is free: against today's count-ranked strip, the assistant would take credit
for the gain a re-rank gives anyway. The number is incremental margin per customer on items kept at
payment, less what the suggestions cost to serve, with checkout conversion, response time and
out-of-stock suggestions as guardrails. At the strip's 60,000 views a day, every 10 paise of serving
cost a view is Rs 1.8 lakh a month, so at 35 paise a view the assistant costs the whole Rs 6.3 lakh
a month that re-ranking the strip could recover. It ships only if its margin over the re-ranked
strip's arm clears its serving cost and no guardrail moves. This variant is written for this
programme.

## Which pain points hide inside the question, each with a real case?

| Pain point | The case | The check |
|---|---|---|
| The popular partner looks like everyone's bundle | Amazon Science's history of the algorithm says counting co-purchases would make a few bestsellers, such as Harry Potter books and trash bags, the top recommendations for every customer (Amazon Science, checked 12 October 2026) | Lift, over the partner's own share |
| Heavy buyers inflate every count | The same history says the team measured the increased likelihood of buying an item with any given purchase, scaling heavy buyers down (the same source) | Count each customer once, or size the expected count by cart |
| A legend repeated as fact | Beer and diapers: in 1992, about 1.2 million baskets from Osco Drug stores showed the pair in the early evening, and the chain does not appear to have moved any shelf (The Register, checked 12 October 2026) | Ask what was decided, and what it cost |
| A cross-sell outcome read as a cause | Uber's annual report (10-K) for 2025: in the last quarter of 2025, in countries offering both, consumers using rides and delivery generated over three times the bookings of single-product consumers (checked 12 October 2026) | Ask who chose to use both, and compare the same consumers before and after they added a second product |
| A discount that hands margin back | Swiggy's shareholder letter for April to June 2025 describes Maxxsaver, a discount unlocked once a basket passes a set size, as returning part of the larger basket's margin to the user, and says it sometimes consolidates carts into fewer orders; over 28 percent of its monthly transacting users used it (checked 12 October 2026) | Price the discount on the purchases that would have happened anyway |

## What does the scorer listen for?

When you practise in pairs, the asker scores each of these from 0 to 2: clarified the scope; named
the denominator and the window; saw the paradox (a high confidence that means nothing); sized it
with a unit (a number with carts, minutes or rupees on it); said what would change their mind; tied
it to a decision and its cost; gave the structure before the number.
