# Does the strip's ranking hold for one zone or one time of day?

Swiggy Instamart, Pune. Since Monday 7 September 2026 the cart page's three-slot strip has shown the
items most often found in the same cart, and its click-through fell from 6.1 percent to 3.8 percent.
In class, the pairs table on all 40,000 September carts ranked chips and cold drink (lift 3.39),
coriander and green chillies (3.00) and bread and butter (2.21) above a floor of 1 percent of carts,
with milk's pairs at chance. Illustrative case: the company is real, the situation and the data are
synthetic, built for this class.

Tonight you rerun that ranking for one slice of the city, about 60 minutes of work.

**Who needs the answer.** The growth lead, who will be asked on Friday whether one strip suits the
whole city or whether Kothrud's evening shoppers need different suggestions from Baner's morning
ones. A strip tuned to a slice that cannot carry the weight wastes slots on luck.

**The questions on the way.**

- How many carts does your slice hold, and what does that do to the floor?
- Which four pairs top the slice above its floor, and on how many carts does each rest?
- Which pair would you refuse to trust, and why?
- Does the city's strip hold in your slice?

## Which slice do you take, and what do you hand in?

Take one of these four slices of `carts` (in `content/W04/D3/data/`, with `cart_items` beside it):

| Slice | How to select it |
|---|---|
| Kothrud, evening | `zone == "Kothrud"` and `time_band == "evening"` |
| Baner, morning | `zone == "Baner"` and `time_band == "morning"` |
| Hinjewadi, night | `zone == "Hinjewadi"` and `time_band == "night"` |
| Viman Nagar, week three | `zone == "Viman Nagar"` and `placed_date` from 15 to 21 September |

Hand in one notebook that runs top to bottom, with these five things, each under a heading that is a
question:

1. The slice's number of carts, and its floor: 1 percent of the slice's carts, as a count.
2. The pairs table on the slice, built the way notebook 02 builds it, with `Counter` over
   `combinations` of each cart's sorted items.
3. The four pairs with the highest lift at or above the slice's floor, each with its lift and the
   number of carts holding both.
4. One check by a second route: one of your four lifts recomputed as confidence over the partner's
   share within the slice, asserted equal.
5. A paragraph of four to six sentences for the growth lead, plain words first: which of the city's
   three pairs still lead, which pair you would refuse to trust and the count that makes you refuse
   it, and whether the slice needs its own strip.

## What makes the paragraph strong?

It names numbers from your slice, never from the city. It says how many carts sit under the pair it
distrusts. It says what would change its mind: a count, a week of data or a test. And it ends on one
call the growth lead can repeat.

The self-check (`takehome/C2_W04_D03_selfcheck_STUDENT.md`) lists the numbers each slice should give.
Open it after your notebook runs, never before.
