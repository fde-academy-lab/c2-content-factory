# The AI-free lab: the week, rebuilt alone

## The situation

Kavya Nair, senior analyst, Kalpa Retail data team: "The growth review is on Monday, and Marketing
will be in the room. Before anything goes to Meera, rebuild the week from a raw export with no
assistant and no notes."

Meera Raghavan, Kalpa Retail's CEO, decides on Monday where the next quarter's effort goes, with
Marketing's Rs 12 crore request to win new customers on the table. Anand Iyer, the finance
controller, reads every number before she does, and his rule has not changed since Wednesday:
"Until your numbers match ours, Finance will not act on a drop measured from an ERP export."

| | |
|---|---|
| **The metric at stake** | Booked revenue per quarter, its change from Q1 to Q2, and the branch of the revenue tree (customers, orders per customer, revenue per order) that moved it, segment by segment |
| **Who asks** | Meera, who acts on the note's first line; Anand, who checks that line against his control totals first; Marketing, who will attack any rate that rests on too little |
| **What a wrong number costs** | A first line with the wrong sign sends Monday's review home with nothing to investigate. A fall at half its size gets half the attention. A rate on a handful of orders sends a team after a segment that did nothing, and the first time Marketing asks "on how many orders?", the whole note loses the room. |

## Kavya's question for the lab

"From Q1 to Q2 in this export: which branch of the revenue tree moved, in which segment, is it
something chance produces, and do your numbers match Finance's? Write it to me as you would write it
to Meera."

## What you have

| File | What it is |
|---|---|
| `data/C2_W01_D05_lab_orders_STUDENT.csv` | Two quarters of orders you have not seen, as the export arrived. Kalpa-shaped and re-keyed for the drill, so nothing in it belongs in Monday's note. |
| `data/C2_W01_D05_lab_control_STUDENT.csv` | Finance's control totals for the same export: distinct orders and booked rupees per quarter. |
| `notebooks/C2_W01_D05_lab_STUDENT.ipynb` | Your workspace: six sections in the week's order, and a last cell that writes what you hand in. |

## The rules

- No assistant of any kind: no chat model, no code completion that writes code, no search for code.
- Notes closed: no earlier notebook, deck, cheat sheet or study note open on any screen. Python's
  own `help()` is allowed.
- 120 minutes on the clock, one pass. Save as you go. Your output folder is copied at the
  120-minute mark, and that copy is what is observed.
- A TA records, at intervals, the step each person is on. Nothing is scored, nothing is ranked and
  nothing is shown to the room.

## The method, in its order

| Step | What it produces | A pace |
|---|---|---|
| Profile | Present, convertible and distinct counts per field, and every count that is not what the field should hold | 20 minutes |
| Clean, with a decisions log | A clean list of orders, a rejected list, and one log row per decision: order id, drop or default or keep and flag, and the reason | 30 minutes |
| Reconcile | The checks you would show Finance, and a bridge from what you read to what you kept | 15 minutes |
| Decompose along the tree | Q1 against Q2 per segment: customers, orders per customer, revenue per order, revenue, and the order count under each rate | 25 minutes |
| One shuffle test | The one gap your decomposition says matters, 2,000 shuffles with `random.Random(7)`, and the p-value as one sentence | 15 minutes |
| The note | Claim, evidence, caveat, action, under 150 words | 15 minutes |

## What you hand in

The notebook's last cell writes three files into `notebooks/output/`: `clean_orders.csv`,
`decisions_log.csv` and `note.md`. Run it before the clock stops, even if a section is unfinished;
an unfinished note with a true caveat is worth more than a finished one without it.

## After the clock

You get twenty minutes for a second look. Compare the two quarter totals you used against the
control totals, and write one line under your note in a new cell: what you checked, or what moved
and by how much. It does not change what you handed in; it is what you bring to the debrief.
