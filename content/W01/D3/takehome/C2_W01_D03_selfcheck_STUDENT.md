# Self-check: the pass, before anybody audits it

---

## Part 1, the notebook

| # | Checkpoint | What you should see | If it fails |
|---|---|---|---|
| 1 | The row count is not the id count | PASS | You counted rows twice rather than distinct ids |
| 2 | You found the repeated ids | PASS | You compared whole records rather than ids |
| 3 | You found the row that is not an order | PASS | You are testing for empty rather than for non-numeric |
| 4 | You found the negative amount | PASS | You checked `isdigit()`, which is `False` for `-2400`, so it landed in the wrong bucket |
| 5 | Input equals clean plus rejected | PASS | A branch is falling through without appending anywhere |
| 6 | Every rejection carries a reason | PASS | An empty string is not a reason |
| 7 | Summary | `7 checks passed and 0 failed` | Any FAIL names its own checkpoint |

**Checkpoint 4 is the one that catches people**, and it is worth understanding rather than fixing.
`"-2400".isdigit()` is `False`, so a test built on `isdigit` throws a perfectly good refund into the
same bucket as a header row. `int()` inside a `try` is the test that separates them.

---

## Part 2, the note

Read it back and answer yes or no. **Two noes means rewrite it.**

1. Does sentence one carry both a row count and a distinct-order count?
2. Does sentence two carry counts rather than adjectives?
3. Is there a single number in sentence three that you would put your name to?
4. Is sentence four a judgment, described as a judgment, that somebody could disagree with?
5. Is it under 120 words?

---

## Part 3, the log

| Test | How to check |
|---|---|
| Every reason says something the issue column does not | Cover the issue column and read the reasons alone. If a reason is now meaningless, rewrite it. |
| Every row has a count | A decision with no count is a decision about an unknown number of rows |
| At least one row is something you kept | A log of only rejections is a log from a pass that made no judgment |

---

## Part 4, the paragraph

One test, and it is the one that matters.

> Cover the first half. **Does the second half name something you would refuse to do?**

Full credit needs a refusal with a reason. "I would not adjust my figure to match theirs, because
reconciling and fabricating differ only in whether the steps are written down" is a refusal. "I
would be careful" is not.

---

## The honest signal

If you found three defects and stopped, go back. There are four, and the fourth raises no error at
all, which is exactly why the profile comes before the pass.
