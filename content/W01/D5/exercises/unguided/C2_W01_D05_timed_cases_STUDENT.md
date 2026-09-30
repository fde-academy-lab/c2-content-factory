# Three timed design cases

Each case is a question an analytics screen asks, set at Kalpa: a situation, a few ways a team could
answer it, and a clock. Read it once, think for three minutes on paper, then answer aloud to your
partner in two minutes. Two answers go to the room before the model answer is read.

Every case asks the same three things, because every design question in an interview does: **which
approach fits, sized how, and what would make you switch.** The numbers marked illustrative are set
for the case and are not Kalpa's records.

## Case 1: Meera's first read, two hours after the export lands

*[F] You have two hours and a raw export; what do you do first, and what do you skip?*

Meera Raghavan wants a first read on Q3 booked revenue by segment before Monday's review. The raw
export from the ERP lands on your screen with two hours to go, about 2,000 orders (illustrative),
and nobody has checked it. Finance will close the quarter's books after the review.

**The real company it is like.** DMart (Avenue Supermarts) published its July to September 2025
standalone revenue, Rs 16,218.79 crore across 432 stores, as a business update on 3 October 2025,
with the figures stated as provisional and subject to limited review, and reported the quarter's
results in a regulatory filing on 11 October 2025 (Business Today, 11 October 2025). A first read
that goes out before the books close is normal. What matters is what it has been checked against.

Every plan below fits inside the two hours and leaves out one step. Size each from the lab's pace:
profile 20 minutes, clean with a log 30, reconcile to the ERP's own control totals 15, decompose 25,
one shuffle test 15, the four-part note 15.

```mermaid
flowchart TB
    Q["<b>two hours, a raw export</b><br/>which step do you leave out?"] --> A["<b>A.</b> no reconciliation"]
    Q --> B["<b>B.</b> no test"]
    Q --> C["<b>C.</b> the tree for one segment only"]
    Q --> D["<b>D.</b> no profile"]
```

| Option | What it does |
|---|---|
| A | Profile, clean with a log, decompose, one shuffle test on the biggest segment gap, and the note |
| B | Profile, clean with a log, reconcile, decompose, and the note marked provisional, with no test |
| C | Profile, clean with a log, reconcile, one shuffle test on one segment's gap, and the note on that segment |
| D | Clean with a log, reconcile, decompose, one shuffle test, and the note, with no profile first |

Your paper: the option you choose and the minutes each plan costs; the one step you will not drop at
any point on the clock, and why; the fact about the export that would make you switch, and to what.

## Case 2: zero rejects and a Rs 20 lakh gap, after the migration

*[S] Walk me through how you clean and check a dataset you have never seen.*

The first full quarter out of the migrated ERP is about 50,000 rows (illustrative). Your cleaning
pass reports zero rejects. The dashboard built on it shows the quarter Rs 20 lakh above Anand
Iyer's books, and Anand wants to know by tomorrow which number Meera should see.

**The real company it is like, loosely.** TSB, the UK bank, moved its customers' records from Lloyds
Banking Group's platform to its owner Sabadell's Proteo4UK platform in April 2018. The Register,
reporting the independent review in November 2019, said the move left 1.9 million customers unable
to view their accounts, and in December 2022 the FCA and the PRA fined TSB a total of £48.65 million.
The likeness is loose: TSB's customers were locked out of a new platform, where this case is a
quarter's total trusted before it was reconciled. What carries over is that a new system's output is
the first thing to check.

| Check | What it catches | Cost on 50,000 rows |
|---|---|---|
| A. Rows against distinct order ids | A batch posted twice | One cell, seconds |
| B. What the code did with values it could not read | Values set to zero or skipped without a log line | One cell, a few minutes to read |
| C. A rupee bridge by month against Finance | How big the gap is, and in which month | About 30 minutes |
| D. Every order matched against Finance's ledger | Which orders differ, by name | Most of a day, and the ledger from Finance |

Your paper: the order you run them in and why that order; the point at which you stop; what you tell
Anand tonight, before the gap is explained.

## Case 3: 42 percent on twelve visits

*[D] A stakeholder attacks your caveat in front of the room; how do you hold it without
overclaiming?*

Kalpa's app team tried a redesigned checkout for a week: 5 of 12 visits converted, 42 percent. The
current checkout converted 31 percent of 1,200 visits in the same week (illustrative). Your note says
"promising, still to be proven". In the review, the product head says: "Forty-two beats thirty-one. Your
caveat is costing us a week. Ship it to everyone."

**The real company it is like.** At Microsoft's Bing, an idea for showing ad headlines sat unbuilt
for more than six months. When it was finally tested, revenue jumped so far that an alert for "too
good to be true" results fired; the analysis showed a real 12 percent lift, worth more than $100
million a year in the US (Kohavi and Thomke, Harvard Business Review, September to October 2017). A
big number was checked before it was believed, and it was checked on the traffic of a test.

| Option | What it does | What it costs |
|---|---|---|
| A. Ship to everyone now | Replace the checkout on the 42 percent | Nothing today; a loss nobody measures if the 42 is luck |
| B. Keep the caveat, keep the pilot small | Wait for more weeks at about 12 visits a week, with the current checkout's visits beside them | About 14 weeks |
| C. Split the traffic in half | Each checkout gets half the visits until each has about 300 | About half a week at 1,200 visits a week |
| D. Give the new checkout one visit in ten for a fortnight | A cautious rollout | About 240 new-checkout visits beside about 2,160 on the current one, over two weeks |

Your paper: your first sentence back to the product head; the option you offer, with its size and
its time; what would make you agree to ship without it.
