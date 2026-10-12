# TA lab note: the pairs method on Kalpa's baskets, then the practice set

**TRAINER ONLY.** For the TA who runs the practice lab after the faculty block (tentative). The lab
re-runs levels L1 to L3 on Kalpa Retail's baskets in notebook 04, then works the practice set. The
programme's facts set no length for the lab, so the parts below run in this order and the practice
set is cut from its end when time runs short. Never cut the twelve baskets or the two your-turn
cells.

## What does the lab ask, and what is the order of work?

Kalpa's merchandising team wants to pair every product with the Rs 199 phone charger "because it is
in 80 percent of baskets" (the row). The head of merchandising asks which pairs to promote and what
each promotion is worth before any money is spent.

| Order | Part | File |
|---|---|---|
| 1 | The twelve baskets counted by hand on paper | The table below, printed one per group |
| 2 | The same twelve confirmed in code | Notebook 04, cell 4 |
| 3 | Your turn: the charger's share and its lift with every product | Notebook 04, cell 6, empty |
| 4 | Your turn: the strongest pair above a 5 percent floor, and the thin pair | Notebook 04, cell 8, empty |
| 5 | The data checks and the three lines for merchandising | Notebook 04, cells 9 to 11 |
| 6 | Items 2 and 3 of the Kalpa unguided set, sat after the lab | `exercises/unguided/C2_W04_D03_kalpa_charger_STUDENT.md` |
| 7 | The practice set | `exercises/practice/C2_W04_D03_lab_set_STUDENT.md` |

## What do the twelve baskets hold, and what should the hand count give?

Print this table for each group. A basket is one consumer order; Business orders hold one product in
bulk and are left out.

| Basket | Segment | Products |
|---|---|---|
| KR-00001 | Student | USB-C cable, notebook A5, phone charger 20W |
| KR-00002 | Student | cable organiser, earphone jack adapter, notebook A5, pen set, phone charger 20W, phone grip |
| KR-00004 | Student | LED desk lamp, extension cord, phone charger 20W |
| KR-00005 | Student | phone charger 20W, power bank 10000mAh, screen protector |
| KR-00006 | Student | earphone jack adapter, extension cord, pen set, phone charger 20W, phone grip |
| KR-00008 | Student | LED desk lamp, notebook A5, pen set, phone charger 20W |
| KR-00009 | Student | LED desk lamp, notebook A5, pen set, phone grip |
| KR-00011 | Student | USB-C cable, cable organiser, earphone jack adapter, extension cord, screen protector |
| KR-00157 | Retail-Plus | LED desk lamp, extension cord, pen set, phone charger 20W, phone grip, wireless earphones |
| KR-00190 | Retail-Plus | earphone case, extension cord, notebook A5, phone charger 20W, power bank 10000mAh, wireless earphones |
| KR-00340 | Retail-Core | USB-C cable, cable organiser, earphone case, earphone jack adapter, notebook A5, power bank 10000mAh |
| KR-00938 | Retail-Core | cable organiser, earphone case, phone charger 20W, phone grip, screen protector, wireless earphones |

The hand count: the charger in 9 of 12 baskets, 0.75; screen protector to charger, 2 of 3, 0.67, and
lift 0.89; wireless earphones with their case, 2 baskets where chance gives 0.75, lift 2.67. Every
value sits at least 0.05 from the full-data plants below, so the hand count spends none of them.

## Which plants should the your-turn cells find, and what do you do if nobody finds one?

The plants stay on this page until a learner's own cell prints them. After that, the room may say
them (decision `w4-finding-once-found`).

| Plant | What the full data says | If nobody finds it |
|---|---|---|
| The charger is everywhere | In 686 of the 812 consumer baskets, 84.5 percent, above merchandising's 80 | Ask "which orders are baskets?" A learner who keeps the 188 Business orders gets 69.6 percent, the wrong base |
| The charger pairs with nothing | Screen protector to charger: confidence 0.82, lift 0.97; every product in at least 2 percent of baskets reads confidence 0.82 to 0.85 and lift 0.97 to 1.00 | Ask "what is the charger's own share?", then "divide the confidence by it" |
| A real pair above the floor | Wireless earphones with their case: lift 3.1, support 6 percent, 49 baskets, 76 percent of them Retail-Plus | Ask "sort the pairs at or above 5 percent by lift; whose baskets are they?", and point at the join with `orders` |
| A thin pair below the floor | Car phone mount with car charger: lift 4.0 on 2 baskets, support 0.25 percent | Ask "below the floor, which pair has the highest lift, and on how many baskets?" |

69 pairs clear the 5 percent floor. The three lines a group brings back: the charger's share and its
lift with the products it would be bundled with; the earphones and case to promote for Retail-Plus,
with support and lift; the car pair to watch, with its two baskets.

## Where do learners stall in the practice set, and which hint unlocks each item?

The practice set's keys are 1c, 2a, 3b, 4b, 5a and 6c.

| Item | Where learners stall | The one hint |
|---|---|---|
| Q1, the lift of tea and rusk | Dividing 30 by 40 and calling 0.75 the lift | "What would chance put in the tea-and-rusk cell?" |
| Q2, a lift of exactly one | Reading sugar to tea, 0.60, as a strong bundle | "Tea is in 60 percent of all bills anyway." |
| Q3, the four pairs and the rule | Which support the floor refers to: it is the pair's, over all bills | "How many carts would the slot touch?" |
| Q4, a slot after the discount | Leaving the Rs 3 in, or pricing at Rs 30 | "Which number does the business keep from each add, after the bundle?" |
| Q5, the scrambled counting cell | Starting from the lift line, or counting before the baskets exist | "Which line uses a name no earlier line has made?" |
| Q6, three bundles | Choosing Z for its lift of 5.0 | "How many bills would Z's slot touch in a week?" |

## What do you send the trainer after the lab?

One line per group, sent to the trainer before Thursday's session: the charger share it found, the
pair it would promote and the pair it would watch. A group that found no plant is named, so
Saturday's recap can start there.
