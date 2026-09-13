# Extras: one to stretch, one to recover

---

## Stretch: the pass that runs itself

You finished early and the cleaning felt mechanical. Then this.

**The situation.** Anand's analyst likes your reconciliation and asks the obvious follow-up:

> "Fine. Now do it every Monday, on whatever they send us, and tell me when it looks wrong."

**What to build.** One function, `audit(rows)`, that takes any export of this shape and returns a
dictionary with:

| Key | What it holds |
|---|---|
| `input`, `clean`, `rejected` | The three counts, and they must reconcile |
| `reasons` | A count per rejection reason |
| `bridge` | A list of `(step, amount)` pairs from the raw total to the clean one |
| `flags` | Anything kept but worth a human look, each with a sentence |

Then run it on **both** exports, the class file and the take-home file, and print the two side by
side.

**The hard part, and the point.** The two files have different defects. A function that only handles
the ones it has seen will report a clean file when it meets the negative amount, because that one
converts without error. Write one test per defect kind first, then write the function.

**The question to answer in writing:** what would `audit` have to return for you to say "this export
is too broken to use", and where is that line? Name a number.

---

## Recovery: one row, one decision, at a time

The cleaning pass ran past you and you would rather rebuild it slowly. Tonight, alone.

**Work in a fresh cell. One step at a time, printing after each.**

1. Load the CSV and print `len(rows)`. That is your `input`. Write it on paper.
2. Print `rows[0]`. Look at the seven fields until they are familiar.
3. Print `rows[0]["amount"]` and then `type(rows[0]["amount"])`. It is text. Sit with that.
4. Make two empty lists, `clean` and `rejected`. Loop over the rows and append every row to `clean`.
   Print both lengths. `input = clean + rejected` already holds, trivially.
5. Now add one rule: if the row's `status` is empty, append to `rejected` instead. Print the two
   lengths again. The equation still holds, and one row moved.
6. Add the second rule for an amount that will not convert. Print again.
7. Add the third rule for a repeated `order_id`. Print again.

**What you should end up believing.** The pass is one loop with one branch per rule, and every
branch moves a row from one list to the other and never loses it. If the two numbers ever stop
adding up to the input, a branch is falling through without appending anywhere, and that is the only
bug this shape of code has.

**Then do one more thing.** Go back to step 5 and, instead of rejecting the row, append a reason
beside it: `rejected.append((row, "no status"))`. Run it. That two-line change is the difference
between a pass and an auditable pass, and it is the whole of today.
