# Week 1 recap paper: the answer key

**TRAINER ONLY** until the discussion block, when it is walked question by question.

Every answer below is what a full-credit response contains, and beside it the most common partial
answer and why it is partial. The discussion is worth more than the marking, so the second column is
the one to spend time on.

---

## Section A. The tree and the ladder

**A1.** Revenue equals customers, times orders per customer, times items per order, times price per
item, less discounts. A full answer picks one branch and gives a reason of the right kind: either
the data can settle it fastest, or the answer would change the decision.

| Common partial answer | Why it is partial |
|---|---|
| The tree drawn correctly with no branch picked | The question asked for a choice and a reason |
| "Customers, because marketing asked for the money" | That is what makes it the branch under dispute, not the branch to check first |

**A2.** Confirm the drop is real. Compare like with like. Decompose along the tree. Isolate the
branch and the segment. Hypothesise, and say what evidence would settle it.

Each rung needs: both totals on one definition; equal windows and the same segment definitions;
customers, orders and revenue by period; the same split per segment; something from outside the data.

| Common partial answer | Why it is partial |
|---|---|
| The five rungs in the wrong order | The order is the whole answer; decomposing before comparing gives a confident wrong result |
| Rungs listed with no "what it needs" | A rung without its input is a label |

**A3.** Something of this shape: the customer count is flat in both quarters, so the base is not
shrinking. Orders per customer fell and almost all of it is in one segment. Here is what would
settle why, and I have not tested it yet.

The mark is for saying the disproof **before** the finding, and for leaving the cause as a
hypothesis.

---

## Section B. Numbers that describe

**B1.** The median, because it describes a typical order. Say the mean beside it and explain the
gap: one corporate order carries most of the revenue, so the mean describes nothing in the file.

| Common partial answer | Why it is partial |
|---|---|
| "The median" with no mention of the mean | The gap between them is the finding, and hiding the mean hides it |

**B2.** Two sentences of this shape: most orders are small and sit near Rs 1,200, and at least one is
tens of thousands larger, so the spread is dominated by a few values rather than by the typical
order.

**B3.** Orders divided by distinct customers, in the same window. Things that break comparability:
different window lengths, a changed segment definition, one period still open, a different
definition of customer.

---

## Section C. Trust

**C1.** First: profile the export and reconcile, because both figures are computable and one of them
is right. Refuse: adjusting your figure so the two agree. That is the difference between reconciling
and fabricating.

**The refusal is the mark.** An answer with no refusal in it is half an answer.

**C2.** No. 183 plus 14 is 197, so three rows are unaccounted for. Find them, because a pass that
loses rows silently will lose more on a bigger file.

**C3.** Three checks, in an order like: is the file the one I think it is; does the row count match
the source; and is my rule actually firing, tested on a row I know is bad.

| Common partial answer | Why it is partial |
|---|---|
| "Check the data" | Not a check |
| Three checks with no order | The order is the answer: the file, then the counts, then the rule |

**C4.** A whole-record check leaves the pair in, because the dates differ. A check on the id removes
one and forces a choice of date. Use the id check, and record which date was kept and why.

---

## Section D. Real, and caused

**D1.** It is the share of chance-only worlds that produce a result at least this extreme.

It is **not** a 3 percent chance the finding is wrong, not a 3 percent chance that chance caused it,
and not a statement about the size of the effect.

**The second half is where the marks are.** An answer with a correct definition and no negation is
an answer that will be misused under pressure.

**D2.** `p < 0.0002`. Because five thousand shuffles can only resolve down to one in five thousand,
and writing `p = 0` claims a certainty the method cannot produce.

**D3.** The 31 percent on 400. The rule of thumb is to distrust a rate computed on fewer than about
thirty observations, and it is **a rule of thumb rather than a law**, which the answer has to say.

**D4.** Three of: the customers who took it may have been about to buy anyway; the group that took
it differs from the group that did not; something else changed in the same weeks; the comparison has
no control group; the aggregate may be a mix effect.

**D5.** Both groups fell. The exposed group holds a larger share of the higher-spending segment than
the control group does. So the blend is pulled upward by who is in it rather than by what anybody
spent.

Full credit needs all three sentences. Two of them is the most common submission.

---

## Section E. The note

**E1.** Four sentences, in order, each doing its own job.

> **Claim.** Orders per Retail-Plus member fell about a third between the quarters, against
> Retail-Core's 2.7 percent.
> **Evidence.** Sixty-six orders across 22 members, and chance produced a gap this large in none of
> 5,000 shuffles.
> **Caveat.** The cause is untested; the reorder-feature complaint is a hypothesis and nothing here
> measures the feature.
> **Action.** Pull reorder events per member either side of the six weeks, against Retail-Core,
> which is a day's work.

The added sentence for marketing's pushback should concede what is true and hold the line: the six
percent is real and it measures the mix rather than the discount.

**E2.** Something of this shape: "Not yet. On twelve orders a rise that size turns up by chance two
times in five. Give it a full quarter and I will have an answer at around fifty orders."

The mark is for naming **what would end the not-yet**. A refusal without that is evasion.

---

## Section F. The transfer

**F1.** Stays the same: the tree, the ladder, the reconciliation habit, the four-part note, and
asking for the denominator.

Changes, and two specifics are needed. Acceptable pairs include: the vocabulary, where a booking is
an order and a test is an item; the cost of an error, where a missed diagnosis is not a missed sale;
the seasonality, since diagnostics have referral patterns retail does not; the regulatory constraint
on what can be reported.

First three asks: the equivalent of the orders table with its date and unit; the definitions their
Finance uses for a completed test; and whichever branch the COO believes is short, so the first cut
tests her belief rather than yours.

| Common partial answer | Why it is partial |
|---|---|
| A method list with no "what changes" | The transfer is the question; restating Week 1 is not the answer |
| "The domain changes" | Name two things, as asked |

---

## What to do with the marking

Papers swap for peer cross-evaluation. The peer marks against this key and writes **one line per
answer** saying what was missing rather than a number. The discussion then walks D1, C1 and E1,
because those three carry the week.
