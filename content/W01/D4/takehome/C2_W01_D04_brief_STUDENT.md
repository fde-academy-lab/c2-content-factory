# Take-home: do discounts grow baskets?

Tonight, about ninety minutes, alone. Due before Friday's lab opens. The self-check beside this brief
lists the numbers you should reach; open it only after your own notebook runs top to bottom.

> **The client asks.** "Forget the monsoon sale for a moment. Across Q1, orders that carried a discount
> were bigger baskets. Discounts grow baskets. That is why we want more of them."
>
> The marketing lead, Kalpa Retail, in a message to Meera after the growth-review draft went round

Meera forwards it with one line: "Is that true? Same rules as today: one page, and 'not yet' is allowed."

## The file

`data/C2_W01_D04_takehome_STUDENT.csv` is a second Q1 export from the same ERP, pulled by a different
team on a different day. Nobody has cleaned it. Treat it the way Wednesday taught: profile it before
you trust a single total, and write down every decision you make about a row.

## What you hand in

A new notebook, `C2_W01_D04_takehome_<your name>.ipynb`, in your own folder, that runs cold top to
bottom and carries five sections.

| Section | The question it answers | What it must show |
|---|---|---|
| 1. Profile and clean | Which rows are orders you can use? | Rows read, rows kept, and a decisions log with one line per kind of row you set aside and why |
| 2. The blended claim | Do discounted delivered orders have bigger baskets than orders with a discount of zero? | Both averages with the count behind each, for Retail-Core and Retail-Plus together |
| 3. Inside each segment | Does the claim hold inside Retail-Core and inside Retail-Plus separately? | The same comparison per segment, with counts, and a chart from the data |
| 4. Chance | Could chance alone make each gap? | 5,000 shuffles with seed 2026 per comparison, and the share in the sentence that survives Kavya |
| 5. The note | What does Meera read? | Claim, evidence, caveat, action, under 200 words |

## Rules

- Delivered orders are the money kept. A discount of zero and a missing discount are different facts;
  decide what you do with the missing ones and say so in the log.
- Every average carries its count. Apply today's rule of thumb to every comparison.
- The chart in section 3 comes from your data, drawn with `kit.columns` or `kit.strip`.
- Before Friday, read the note aloud to someone outside the programme and write one line in your
  notebook about what they asked you. A question you could not answer belongs in your caveat.

## After it

- **Watch.** Seeing Theory, frequentist inference, the interactive chapter on testing:
  https://seeing-theory.brown.edu/frequentist-inference/index.html (verified 29 Sep 2026)
- **Redo.** Run today's shuffle on your Monday take-home data too, if the practice lab did not get to it.
- **Recap.** Write the note's four parts and the p-value sentence from memory on a card. Both are on
  Saturday's paper.
