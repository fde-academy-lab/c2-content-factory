# Can you take a raw export to a note Anand would sign, alone, in two hours?

The AI-free lab, Week 1, Friday. Kavya Nair, senior analyst, Kalpa Retail data team: "The growth
review is on Monday, and Marketing will be in the room. Before anything goes to Meera, rebuild the
week from a raw export with no assistant and no notes."

**Who needs the answer.** Meera Raghavan, Kalpa Retail's CEO, decides on Monday where the next
quarter's effort goes, with Marketing's Rs 12 crore request to win new customers on the table. Anand
Iyer, the finance controller, reads every number before she does, and his rule has not changed since
Wednesday: "Until your numbers match ours, Finance will not act on a drop measured from an ERP
export." An ERP export is a file pulled from Kalpa's ERP, the enterprise system where its orders and
its books are recorded. A first line that does not tie to Anand's books is sent back; a misread
branch sends Monday's effort to the wrong team; a rate on too few orders loses the room at
Marketing's first question.

**The questions on the way.** The lab asks six, in the week's order, and each has its own part
below:

1. What does this file hold before you change anything?
2. Which rows count, and why?
3. Is the clean data still the data Finance booked?
4. Which branch of the revenue tree moved, in which segment, and on how many orders?
5. Could chance alone produce the gap you will lead with?
6. What should Meera do on Monday, and how sure is the note?

## What is Kavya's question for the lab?

"From Q1 to Q2 in this export: which branch of the revenue tree moved, in which segment, is it
something chance produces, and do your numbers match Finance's? Write it to me as you would write it
to Meera."

The metric at stake is booked revenue per quarter, the rupees of the orders recorded as sales in that
quarter, and its change from Q1 to Q2. The revenue tree splits that change into three branches:
revenue is customers, times orders per customer, times revenue per order, read segment by segment.

## What do you have to work with?

| File | What it is |
|---|---|
| `data/C2_W01_D05_lab_orders_STUDENT.csv` | Two quarters of orders you have not seen, as the export arrived. Kalpa-shaped and re-keyed for the drill, so nothing in it belongs in Monday's note. |
| `data/C2_W01_D05_lab_control_STUDENT.csv` | Finance's control totals for the same export: distinct orders and booked rupees per quarter. A control total is the source system's own count and sum for a period. |
| `notebooks/C2_W01_D05_lab_STUDENT.ipynb` | Your workspace: six sections in the week's order, and a last cell that writes what you hand in. |

## What are the rules?

- No assistant of any kind: no chat model, no code completion that writes code, no search for code.
- Notes closed: no other notebook in `notebooks/` open, and no deck, cheat sheet or study note open
  on any screen. Python's own `help()` is allowed.
- 120 minutes on the clock, one pass. Save as you go. Your output folder is copied at the
  120-minute mark, and that copy is what is observed.
- A TA records, at intervals, the step each person is on. Nothing is scored, nothing is ranked and
  nothing is shown to the room.

## Which six parts does the lab run, and in what order?

The order is fixed; the minutes are a pace.

### 1. What does this file hold before you change anything?

At work, every analyst reads a new extract before quoting from it, because a number quoted from a
file nobody has read is the one that gets taken back. In about 20 minutes you produce present,
convertible and distinct counts for every field, and write down each count that is not what the
field should hold.

### 2. Which rows count, and why?

At work, an auditor asks for the reason behind every change to a finance number, months after it was
made. In about 30 minutes you produce a clean list of orders, a rejected list, and one log row per
decision with the order id, the decision (drop, default, or keep and flag) and the reason.

### 3. Is the clean data still the data Finance booked?

At work, Finance signs off a number only when the analyst can show how it ties to the books. In
about 15 minutes you produce the checks you would show Finance, and a bridge from what you read to
what you kept.

### 4. Which branch of the revenue tree moved, in which segment, and on how many orders?

At work, a CEO opens one branch first, and the analyst's tree decides which. In about 25 minutes you
produce Q1 against Q2 per segment: customers, orders per customer, revenue per order, revenue, and
the order count under each rate.

### 5. Could chance alone produce the gap you will lead with?

At work, Marketing's first question about any finding is whether it is real. In about 15 minutes you
produce one test on the one gap your decomposition says matters, 2,000 shuffles with
`random.Random(7)`, and the p-value written as one sentence that says what it is a share of.

### 6. What should Meera do on Monday, and how sure is the note?

At work, a CEO reads one page in two minutes and acts on its first line. In about 15 minutes you
produce the note in four parts, claim, evidence, caveat and action, under 150 words.

## What do you hand in, and where?

The notebook's last cell writes three files into `notebooks/output/`: `clean_orders.csv`,
`decisions_log.csv` and `note.md`. Run it before the clock stops, even if a section is unfinished;
an unfinished note with a true caveat is worth more than a finished one without it.

## What happens after the clock stops?

You get twenty minutes for a second look. Compare the two quarter totals you used against the
control totals, and write one line under your note in a new cell: what you checked, or what moved
and by how much. What you handed in stays as it was, and this line is what you bring to the debrief.
