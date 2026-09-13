# Day sheet: Week 1 Day 2, Tuesday

**TRAINER ONLY.** Nothing on this page reaches a learner.

---

## The two-minute orientation

| | |
|---|---|
| **Start from** | Monday's tree and leaf counts. The ladder is new; the arithmetic is not. |
| **Go as far as** | Everyone names the branch and the segment with numbers, and states the reorder-feature cause as a hypothesis with its test. |
| **Stop before** | Files, which are Wednesday. Any test of whether the difference is real, which is Thursday. Comprehensions and modules. |
| **Comes later** | Tomorrow's cleaning changes tonight's answer. Promise that out loud at the close; it is what makes Wednesday land as a discovery rather than as a correction. |
| **Cut first** | Percentage-change formalities. **Never cut the ladder or the segment decomposition.** |

---

## The running order

| Block | Duration | What happens |
|---|---|---|
| 1 | 10 min | Meera's reply and the Retail-Plus complaint. The room lists what could make a drop look real when it is not. |
| 2 | 30 min | The investigation ladder, five rungs, and what each needs from the data |
| 3 | 45 min | Grouping by key: orders and customers by quarter, then by segment. The dictionary accumulator. |
| 4 | 35 min | Describing a segment: typical value, spread, shape from sorted values |
| 5 | 45 min | Functions: the same numbers for every segment written once. Return against print. The conversion that must not crash the loop. |
| 6 | 55 min | Guided then unguided: Q1 against Q2 along the tree, segment by segment |
| 7 | 20 min | Kahoot and close |

---

## What is planted, and what the room should find

**This section never reaches a learner.**

| Planted | What the room should do | If nobody finds it |
|---|---|---|
| Customers flat at 69 across both quarters while orders per customer falls | Compute distinct customers per quarter and disprove marketing's claim themselves | Ask "what would have to be true for marketing to be right, and can you check it?" |
| The fall concentrated in Retail-Plus, down 49 percent against Retail-Core's 5 | Reach it by calling `describe` once per segment | Ask for the same table one level down. Do not name the segment. |
| The `discount` field absent on 58 of 200 records | Meet `KeyError` when they total discounts, then count the absent records before choosing a default | It fires whether they look for it or not. It is the block-5 failure. |

**The 14 duplicated rows are also in this file and are not today's lesson.** If a sharp learner
spots that `KR-` ids repeat, that is excellent: tell them to write it in their notes and that
Wednesday is about exactly that. Do not explore it today; it is Wednesday's whole arc.

---

## The deliberate failures, with their exact text

**Block 5, the absent key.** Have the room total the discounts without `.get()`:

```
KeyError: 'discount'
```

The move to teach is **not** reaching for `.get()`. It is asking how many records and whether the
absence is concentrated. Only then choose a default, and make somebody write the reason in a
comment. Wednesday will ask for that reason by name.

**Block 5, the function that prints.** Change `return` to `print` in `describe` and call
`describe(q1)["orders"]`:

```
TypeError: 'NoneType' object is not subscriptable
```

One demonstration is enough. The sentence to leave them with: a function that prints cannot be
built on.

---

## The numbers, so you are never caught out

| | Q1 | Q2 |
|---|---|---|
| Rows | 114 | 86 |
| Revenue | Rs 2,10,00,000 | Rs 1,87,00,000 |
| Distinct customers | 69 | 69 |
| Orders per customer | 1.65 | 1.25 |
| Revenue per order | Rs 1,84,211 | Rs 2,17,442 |

Decomposition: `1.000 × 0.754 × 1.180 = 0.890`, against an actual revenue change of 0.890.

| Segment | Q1 per customer | Q2 per customer | Change |
|---|---|---|---|
| Retail-Core | 1.12 | 1.06 | down 5.3 percent |
| Retail-Plus | 2.32 | 1.18 | down 49.0 percent |
| Business | 1.82 | 1.55 | down 15.0 percent |
| Student | 2.50 | 3.50 | up 40.0 percent |

By channel, for the take-home: web down 22.4 percent, store down 8.1, app flat.

Records with no `discount` field: 58 of 200.

---

## Per-block facilitation

**Block 1.** Get five ways a drop can look real when it is not, out of the room, before the ladder
goes up. The ladder lands much harder as the answer to a confusion they just felt.

**Block 2.** Draw the rungs bottom to top. When somebody offers the reorder button as the answer,
write it on the board at rung five and leave it there, visibly four rungs above where the room is.
That single move teaches the day.

**Block 3.** Type the `.get()` line slowly and say the shape aloud: look up what is there or
nothing, then add and put it back.

**Block 4.** Put the four segment description rows on screen together. Business is the row that is
unlike the others, and somebody will say so. That is Monday's lesson returning one level up.

**Block 5.** The two failures both live here. Run them in the order given; the `KeyError` first,
because the discussion about defaults is what Wednesday needs.

**Block 6.** This is the longest block and the one where circulating matters. The most common stall
is a learner computing orders per segment rather than orders per customer per segment.

---

## Checkpoint questions

1. After block 2: which rung is "the reorder button broke", and what is below it?
2. After block 3: what does `.get(key, 0)` do that `[key]` does not, and what does that cost?
3. After block 5: your function prints the right numbers and the next line fails. Why?
4. After block 6: revenue per order went up. Does that help or hide?

---

## What the room leaves with

The ladder in order, the decomposition closing to the revenue change, Retail-Plus named with its
number, and the reorder button written down with the word "hypothesis" in front of it and a test
beside it. The last one is what rooms skip, so make somebody read theirs aloud.
