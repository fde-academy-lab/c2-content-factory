# The metric trap: cheat sheet

Week 5, Tuesday. Two humps, one line, four boxes, two prices.

<img src="../1_in_class_training_content/slides/img/C2_W05_D02_timeline_tuesday_STUDENT.png" alt="Two humps, the line and the four boxes" width="48%" style="width:48%">

## Which terms carry the day?

| Term | Plain meaning | Rule or formula | Trap |
|---|---|---|---|
| Confusion matrix | counts of (what the model said, what happened) | TP, FP, FN, TN | scikit-learn prints `[[TN, FP], [FN, TP]]` |
| Precision | of those flagged, the share right | `TP / (TP + FP)` | dividing by everyone |
| Recall | of those real, the share flagged | `TP / (TP + FN)` | high precision hiding a recall of 0.19 |
| F1 | one grade, low if either is low | `2PR / (P + R)` | weighs both mistakes equally |
| Accuracy on imbalance | share right, mostly the easy majority | say-no scores `1 - base rate` | 88.74 percent for calling nobody |
| 1-in-N test | act when at least 1 in N would come good | `wrong action / (wrong action + missed action)`, each in Rs | needs honest probabilities |
| Threshold | the score at or above which we act | from the prices, or from the budget if stricter | 0.5 is the line for equal costs only |
| Precision at k | share of positives in the top k | `positives in top k / k` | comparing lists of different k |

## Where is today on the machine learning map?

```mermaid
flowchart LR
    A["Frame"] --> B["Split,<br/>baseline"] --> C["Fit"] --> D["Metric,<br/>line"] --> E["Features"] --> F["Generalise"] --> G["Justify"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C
    classDef next fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class A,B,C known
    class D lit
    class E,F,G next
```


## Which real numbers make it stick?

- Stripe: on a 26 dollar sale at 8 percent margin, one fraud costs the profit of 18.71 good sales, so blocking pays once about 1 in 20 blocks is fraud, a break-even precision of 5.07 percent (Radar technical guide, verified 28 October 2026).
- Flipkart with CMU: of the 250 accounts a ratings-fraud model ranked most suspicious, Flipkart's team found 211 to be fraud, a precision at 250 of over 84 percent (arXiv 1511.06030, verified 28 October 2026).
- Razorpay: fraud detection is compared "at the same alert volume", since catching more by reviewing more "is a threshold change, not proof that the model improved" (engineering blog, 10 September 2026, verified 28 October 2026).

## What has the programme covered so far, one line each?

| Day | One line |
|---|---|
| W1 Mon | The revenue tree: a business ask split into measurable branches with honest first numbers in Python. |
| W1 Tue | The sales-drop ladder: like-with-like windows, denominators and descriptive statistics by segment. |
| W1 Wed | Profile, clean and reconcile before any analysis, so input equals clean plus rejected. |
| W1 Thu | Real or noise with a permutation test, correlation against cause, and the one-page note. |
| W1 Fri | The week rebuilt alone, with no AI, and the note defended aloud. |
| W2 Mon | SQL from selection to CTEs: the revenue tree as warehouse queries. |
| W2 Tue | Joins without lying: fan-out, the anti-join, booked against collected. |
| W2 Wed | Window functions: ranks, running totals and spend against plan. |
| W2 Thu | pandas groupby, merge and reshape for the Monday customer table. |
| W2 Fri | Excel for analysts: pivots, lookups, one number on the leadership slide. |
| W3 | Build 1: a named-customer brief on raw messy data, defended live. |
| W4 Mon | Metric design: a north star with guardrails, and the proxy test. |
| W4 Tue | Stakeholder communication: one slide, five minutes, and the first guesstimate. |
| W4 Wed | Market basket: support, confidence, lift, and cross-sell value in rupees. |
| W4 Thu | Cohort and funnel: where the frequency loss actually happens. |
| W4 Fri | Forecasting against a naive baseline that is hard to beat. |
| W5 Mon | Framing a prediction: input, target, prediction time, the split, the baseline, two model families. |
| W5 Tue | The metric trap: the matrix, the ratios, accuracy on imbalance, prices to a line, the transfer to lending. |

## When does each rule apply, and what flips it?

| Situation | Report or do | Flips when |
|---|---|---|
| Miss dearer than a false action (Rs 1,200 against Rs 40) | recall leads, line low: 0.032 | the ratio tightens: at 8 to 1 the line is 0.11 |
| False action dearer (Rs 60,000 against Rs 3,000) | precision leads, line high: P(repay) 0.952 | the loss after recoveries falls |
| A fixed budget (1,000 calls) | rank, take the top k, report precision at k | the cost line is stricter than the budget |
| A stakeholder asks for one number | the leading metric, with the count and the bill beside it | never accuracy alone on an imbalanced outcome |
