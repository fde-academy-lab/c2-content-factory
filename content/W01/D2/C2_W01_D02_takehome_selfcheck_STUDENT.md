# Take-home self-check

Open this after your run, before you hand anything in.

These are checkpoints, not answers. Each one is something you can verify on your own screen in under a minute. If a checkpoint fails, the fix is yours to find, and finding it is the exercise.

---

## Checkpoint 1: the input

Your reader should see **30 records** in the file, not counting the header row.

If you got 31, you are counting the header. If you got 29, your reader is skipping the first record.

## Checkpoint 2: the conversion failures

Exactly **3 records** will not convert with `int()`.

Their ids are `3008`, `3011` and `3019`. If you found fewer than three, one of them slipped past you, and the one people miss is not the one they expect.

Their reasons, in the interpreter's own wording:

```
invalid literal for int() with base 10: 'forty two'
invalid literal for int() with base 10: ''
invalid literal for int() with base 10: '24 500'
```

If your reasons read differently from these, you invented wording instead of carrying `str(e)`.

## Checkpoint 3: the one that converts and is still wrong

There is exactly **one** such record. It is not in the list above, because `int()` accepts it without complaint.

Sort your clean amounts and look at the smallest one. If nothing looks wrong, you have not sorted them.

## Checkpoint 4: your total, whichever rule you chose

Two totals are defensible, and which one you land on depends entirely on the rule you wrote.

| If your rule is | Clean records | Total |
|---|---|---|
| Reject only what `int()` refuses | 27 | 219050 |
| Also reject the record from checkpoint 3 | 26 | 223550 |

If your total is neither of these, work backwards: check your reconciliation before you check your arithmetic.

Notice the second total is **larger** while holding **fewer** records. If that surprises you, you have found the reason checkpoint 3 matters.

## Checkpoint 5: the reconciliation

Whichever rule you chose:

```
30 in = clean + rejected
```

If this does not hold, a record went somewhere you did not intend. The usual cause is a `continue` in the wrong place, or an append inside a branch that does not always run.

## Checkpoint 6: reopened, not just written

Your reconciliation must count rows read back **from the files on disk**, never the lists still sitting in memory.

Quick test: restart your kernel, run only the reconciliation cell, and see whether it still works. If it fails, you were counting memory.

---

## What no checkpoint can tell you

Whether your threshold rule is any good. A rule that passes every number here can still be one a reviewer would reject.

Read your own rule back and ask: could a colleague apply this tomorrow, on a file I have never seen, without asking me a single question? If they would have to guess at anything, the rule is not finished.

Bring the rule tomorrow. That is the part we discuss.
