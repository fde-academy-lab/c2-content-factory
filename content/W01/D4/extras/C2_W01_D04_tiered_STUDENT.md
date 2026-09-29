# Extras: one to stretch, one to recover

Both are optional and neither is graded. Pick the one that matches where you actually are.

---

## Stretch: a shuffle that respects the members

You finished the take-home and the shuffle felt easy. Then this one is for you.

**The situation.** Kavya reads your Retail-Plus test and asks one more question.

> "You pooled all 44 member-quarters and dealt them out at random. But the same 22 members are in both
> quarters. A member who spends a lot in Q1 usually spends a lot in Q2. Does your shuffle know that?"

**What to build.** A second shuffle that keeps each member's pair together. For each member, compute
the Q1 less Q2 difference; in each shuffle, flip the sign of each member's difference at random (if
the quarter made no difference, either order was as likely); the gap in that world is the mean of the
flipped differences. Run it 5,000 times with seed 2026.

| Column | What goes in it |
|---|---|
| The pooled shuffle's share | From notebook 1 |
| The paired shuffle's share | Your new number |
| Which is smaller, and why | One sentence in business terms |
| Which you would report | One sentence, and the reason |

**The hard part, and the point.** Both shuffles are legitimate; they answer slightly different
questions about the same members. The skill is saying which question Meera asked, and choosing the
test that answers it.

---

## Recover: the three sentences, until they are automatic

Today felt fast, and the p-value sentence still comes out wrong under pressure. Then do this, and
nothing else, tonight.

**Step 1.** Write the three sentences on a card, from the cheat sheet:

- "If nothing had changed, a gap this large turns up in about ___ of every 100 shuffles."
- "It is worth Rs ___ a quarter, ___ percent of the company."
- "The rate stands on ___ orders; under thirty, it is a lead."

**Step 2.** Open notebook 1 and rerun sections 3 and 4 only. Fill the first sentence twice, once for
Retail-Core and once for Retail-Plus, and read both aloud.

**Step 3.** Open the round 1 set in `exercises/unguided/` and redo items 2 to 5 without looking at the
solution. If any answer changes from your first attempt, read that item's row in the solution file and
say the reason aloud.

**Step 4.** Say the note's four parts aloud from memory: claim, evidence, caveat, action. Saturday's
paper asks for them.
