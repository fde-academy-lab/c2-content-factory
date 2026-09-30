# Did Q1's discounted orders really make bigger baskets, and what can Meera be told on one page?

Tonight, about ninety minutes, alone. Due before Friday's lab opens. The self-check beside this brief
lists the numbers you should reach; open it only after your own notebook runs top to bottom.

> **The client asks.** "Forget the monsoon sale for a moment. Across Q1, orders that carried a
> discount were bigger baskets. Discounts grow baskets. That is why we want more of them."
>
> The marketing lead, Kalpa Retail, in a message to Meera after the growth-review draft went round

Meera forwards it with one line: "Is that true? Same rules as today: one page, and 'not yet' is
allowed."

Meera Raghavan is Kalpa Retail's CEO. A basket is one order's amount, and the claim compares the
average basket of orders that carried a discount with the average basket of orders whose discount was
zero. Today built three habits for a claim like this. A gap between two groups needs a chance
reference: because discounted and undiscounted orders are different orders, the label shuffle pools
every basket, deals the baskets at random into two piles of the groups' sizes, many times, and counts
how often chance alone makes a gap as large as the real one. That count as a fraction is the share,
reported in the claim's direction and in either direction. Every average carries its count, in
orders and in customers, and the day's rule of thumb is to distrust a comparison with fewer than
thirty customers behind it. And a gap between two groups can belong to who is in each group, so the
comparison runs inside each segment as well as over all of them: Retail-Core and Retail-Plus are
Kalpa's two consumer tiers, and Retail-Plus is the paid membership. The note has four parts: claim,
evidence, caveat and action.

**Who needs the answer.** Meera, who will read the marketing lead's claim as a reason to give more
discounts. If the claim is repeated without its counts or its chance, Kalpa spends margin on
discounts to grow baskets that a fair comparison may show never grew.

**The questions on the way.**

- Which file do you work on, and where do you start?
- What do you hand in, section by section?
- Which rules does tonight's work follow?
- What comes after the note?

## Which file do you work on, and where do you start?

`data/C2_W01_D04_takehome_STUDENT.csv` is Wednesday's take-home export again: the same second Q1
extract from the migration, copied into today's folder so your notebook finds it. You profiled and
cleaned it last night, so start from your decisions log. Apply each line of the log in code, check
that you reach the rows you kept on Wednesday, and add the one decision tonight's question needs:
what to do with an order whose discount is missing. If your Wednesday pass is unfinished, finish it
first; the self-check lists the counts a finished pass reaches.

## What do you hand in, section by section?

A new notebook, `C2_W01_D04_takehome_<your name>.ipynb`, in your own folder, that runs cold top to
bottom and carries five sections.

| Section | The question it answers | What it must show |
|---|---|---|
| 1. Clean, from your log | Which rows are orders you can use? | Your Wednesday decisions applied in code, rows read and rows kept, and one new log line for orders whose discount is missing |
| 2. The blended claim | Do discounted delivered orders have bigger baskets than orders with a discount of zero? | Both averages with the orders and customers behind each, for Retail-Core and Retail-Plus together |
| 3. Inside each segment | Does the claim hold inside Retail-Core and inside Retail-Plus separately? | The same comparison per segment, with counts, and a chart from the data |
| 4. Chance | Could chance alone make each gap? | 5,000 shuffles of the discount labels with seed 2026 per comparison; the share in the claim's direction and the share either way, in the sentence that survives Kavya |
| 5. The note | What does Meera read? | Claim, evidence, caveat, action, under 200 words |

The sentence that survives Kavya Nair, the senior analyst who reviews every line before it reaches
Meera, names the world the share was counted in: "If discounts made no difference, a gap this large
would turn up in about ___ of every 100 shuffles, and a gap that large either way in about ___."

## Which rules does tonight's work follow?

- Delivered orders are the money kept. A discount of zero and a missing discount are different facts;
  decide what you do with the missing ones and say so in the log.
- Every average carries its count, in orders and in customers. Apply today's rule of thumb, which
  counts customers, to every comparison.
- The chart in section 3 comes from your data, drawn with `kit.columns` or `kit.strip`.
- Before Friday, read the note aloud to someone outside the programme and write one line in your
  notebook about what they asked you. A question you could not answer belongs in your caveat.

## What comes after the note?

- **Watch.** Seeing Theory, frequentist inference, the interactive chapter on testing:
  https://seeing-theory.brown.edu/frequentist-inference/index.html (verified 29 Sep 2026)
- **Redo.** Run today's shuffle on your Monday take-home data too, if the practice lab did not get to
  it.
- **Recap.** Write the note's four parts and the p-value sentence from memory on a card. Both are on
  Saturday's paper.
