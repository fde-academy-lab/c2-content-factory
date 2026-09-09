# Take-home self-check

Open this after your run, before you hand anything in.

These are checkpoints, not answers. Each is something you can verify on your own screen in under a minute. When one fails, the fix is yours to find.

---

## Checkpoint 1: the shape of the file

**41 rows**, not counting the header. **Seven fields**, the same seven as today.

If you read 42, you are counting the header row. If your profiler reports fields you did not expect, read the header again.

## Checkpoint 2: the profile before you touch anything

```
amount    present 40/41   converts 38/41   distinct 39
discount  present  5/41
```

If your `converts` for `amount` is 41, you have already coerced something. Go back and profile the raw file.

## Checkpoint 3: the three that will not convert

Exactly **three** amounts fail. Their ids are `KR7506`, `KR7519` and `KR7527`, and their reasons in the interpreter's own wording are:

```
invalid literal for int() with base 10: 'eleven hundred'
invalid literal for int() with base 10: ''
invalid literal for int() with base 10: '3,150'
```

If your reasons read differently, you invented wording instead of carrying `str(e)`.

## Checkpoint 4: the row-level finding

`order_id` holds **40 distinct values across 41 rows**.

A whole-record comparison will report **0 duplicates**, exactly as it did in class.

The repeated id is `KR7511`, and the two rows differ on **`status`**, not on the date. That is a harder call than today's pair: one row says the order was delivered and the other says it was returned, and only one of those can be true of a single order.

If your log has no line about this, you cleaned the columns and missed the record.

## Checkpoint 5: the reconciliation

```
41 in = 38 profiled + 3 rejected
```

Both rows of the repeated pair stay in the profiled file unless your written rule says otherwise, in which case your rule has to be in the log and the counts move to 37 and 3, with one row removed on purpose and recorded.

Either is defensible. Neither is defensible unsaid.

## Checkpoint 6: the extreme

Sort the amounts and read the tail. The largest is **Rs 96,000**, against a next largest of **Rs 3,000** and a middle order of **Rs 1,965**.

It is **58 percent** of the Rs 164,110 total.

It converts cleanly, so it is not a cleaning problem. It is smaller and more arguable than today's Rs 480,000, which is deliberate: today's was obviously worth raising and this one is the size where people quietly decide on their own.

## Checkpoint 7: the reusability test

The real test of `profile_dataset()` takes ten seconds. Delete a column from a copy of the file and run your function on it again.

If it raises a `KeyError`, a field name is written inside the function and it is not reusable. If it returns a profile with one fewer field, it is.

---

## What no checkpoint can tell you

Whether your identity rule is any good.

Read your two lines back and ask: could a colleague apply this tomorrow, on a file I have never seen, without asking me a single question? If they would have to guess at anything, the rule is not finished.

Bring the rule tomorrow. That is the part that gets discussed.
