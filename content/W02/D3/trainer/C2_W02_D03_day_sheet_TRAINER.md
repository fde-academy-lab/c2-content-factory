# Trainer day sheet: Week 2, Wednesday. SQL window functions

TRAINER ONLY.

Posts to <!-- sync:module:W02/D3 -->Module 1: Foundations of AI and Data<!-- /sync:module:W02/D3 -->, on <!-- sync:day-date:W02/D3 -->Wed 14 Oct 2026<!-- /sync:day-date:W02/D3 -->.

## The IITGN faculty block (tentative)

<!-- sync:faculty-day:W02/D3 -->
**IITGN faculty block W2-3 (tentative), 120 minutes, after this row's applied core.** Faculty: to be confirmed by IIT Gandhinagar.

TOPIC: Errors, power and sample size: Type I and Type II errors, power, the sample size a comparison needs, multiple comparisons, and statistical against practical significance.
PICKS UP WHERE THE ROW STOPS: Week 1 Thursday gave a rule of thumb of thirty observations and stopped before power.
CONNECTS TO KALPA: how many Student orders Meera would need before she could trust 40 percent; marketing testing ten segments and finding one that looks significant.
BY THE END: a learner can size a comparison roughly, and can explain why testing many segments manufactures findings. The block closes the statistics that ME1 draws on.
DOES NOT REPEAT: correlation against causation, which the campaigns table already taught.
<!-- /sync:faculty-day:W02/D3 -->

## The shape of the day

| Block | Minutes | What has to happen |
|---|---|---|
| Marketing's two asks | 10 | The GROUP BY attempt that cannot produce a top fifty per segment |
| Three functions on a tie | 40 | Side by side, on paper first, then on screen |
| PARTITION BY and top-N | 45 | The window refused in WHERE, fixed in a CTE |
| LAG and the running total | 45 | Falling twice, and what makes a cumulative deterministic |
| Guided then unguided | 55 | The protect list, the flag, the plan line |
| Kahoot and close | 20 | Seven questions |

Total 215 minutes, which is the shortest day of the week and the one with a single arc, so it
takes one deck rather than two halves.

## Open on the question GROUP BY cannot answer

Write Marketing's ask on the board and let somebody attempt it with Monday's tools. They will
produce a correct query that returns every customer, and then reach for `LIMIT 50` and find it
takes fifty from the whole result.

The new tool then arrives as the missing piece rather than as the next topic.

## What is planted in v4

**Never name any of this.**

| Planted | Found by | Value |
|---|---|---|
| An exact Q2 revenue tie at the fiftieth Retail-Plus position | Looking at rows 46 to 54 of the ranking | Two members at Rs 3,350 |
| A second tie higher up, at forty-eight and forty-nine | The same query | Two members at Rs 3,480 |
| Three Retail-Plus members whose spend falls in each Q2 month | Two LAGs and a comparison | C-0161, C-0171, C-0175 |
| A flat thirteen-week plan line | The running total against plan | Rs 75,69,230 a week |

The second tie is the one to leave alone until somebody finds it. It is why `DENSE_RANK` ships
fifty-two rather than fifty-one, and a room that predicts fifty-one for both has not noticed it.

## The failures to stage

**One.** The tie itself. Show positions 46 to 54 and let the room read the three columns before
any function is named. Expect somebody to say the tie is a data problem. It is not; it is two
people who spent the same amount, which is a thing that happens.

**Two.**

```
ERROR:  window functions are not allowed in WHERE
```

Have somebody write the top-fifty filter directly in `WHERE`. Point at Monday's execution-order
drawing rather than explaining. If the drawing is not still on the board, put it back up before
this block.

## The moment the day turns

Reading the sentence from the head of Retail-Plus **after** the room has produced three different
answers, not before.

Three defensible answers exist, the room made all three, and then one sentence from a business
owner eliminates two of them. That sequence is the day. Reading his sentence first turns the
lesson into a lookup.

## The argument to make second, and make it properly

Run the `ROW_NUMBER` version twice. Even if the rows do not swap on your machine, say plainly why
they could: nothing in the data separates the tied pair, so nothing in the plan has to keep them
in order.

Ask: two analysts run this query and send Marketing different names. Which one is wrong? Neither,
and that is the problem.

## The judgment

Somebody will ask what to say to a flagged member who was on holiday. Take it seriously; it is the
best question of the day. A flag is a shortlist for a conversation rather than a verdict, and the
member being right does not make the flag wrong.

## Timing pressure

Cut `LEAD` first, per the row: teach `LAG`, name `LEAD`. Then cut the running-total variant. Never
cut the tie demonstration, which is the day.

## Close-out

Release both solution files and the protect-list solution. Set the take-home and say the impostor
query is the part that matters. Preview Thursday in one line: the same questions, a third time, in
pandas, and a senior analyst asks how you choose between the three tools.
