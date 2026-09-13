# Self-check: know you are right before anybody marks it

Six checkpoints. Every one is something you can verify alone. If a checkpoint fails, the fix is
named beside it.

---

## Part 1, the notebook

| # | Checkpoint | What you should see | If it fails |
|---|---|---|---|
| 1 | The file loaded | `24 orders loaded` | The data folder is not beside your notebook. Run the generator command named in the error. |
| 2 | Revenue is a whole number | The check prints PASS | You added `order["amount"]` without `int()`, so one text amount is either crashing you or being skipped |
| 3 | Revenue is above Rs 5 lakh | The check prints PASS | You are summing only delivered orders, or you dropped the corporate orders |
| 4 | Customers fewer than orders | The check prints PASS | You counted rows rather than distinct ids. A `set` is what refuses duplicates. |
| 5 | The median sits between Rs 500 and Rs 6,000 | The check prints PASS | You took `amounts[len(amounts) // 2]` on an even-length list without averaging the middle pair |
| 6 | The summary line | `8 checks passed and 0 failed` | Any FAIL line names the checkpoint above |

---

## Part 1, the two numbers worth staring at

Once every check passes, look at these two side by side.

- The **mean** on this sample is far above the **median**.
- Take the single largest order out, and the mean drops by more than half.

If those two things are not true in your run, you have a different file. Say so tomorrow.

---

## Part 2, the tree you built

Read your own page back and answer each of these with yes or no. Three noes means rewrite it.

1. Does every branch carry a **denominator**, in words, not in symbols?
2. Could somebody who has never seen that business tell what it sells from your five rows?
3. Is the cost of moving each branch written in the **owner's** terms rather than in business-school
   terms?
4. Is the branch you picked the one your own numbers point at, rather than the one that is easiest
   to write about?
5. Is the number you asked for something the owner would actually know?

---

## Part 3, the paragraph

One test, and it is brutal.

> Cover the second half of your paragraph. Does the first half name a **check that a person could
> perform on Tuesday morning**, with something they already have?

If the check needs data nobody collects, it is not a check, it is a wish. Rewrite it.

---

## The honest signal

If you finished Part 1 in twenty minutes and Part 2 took you an hour, that is the right ratio. Part
1 is arithmetic you already saw. Part 2 is the skill.
