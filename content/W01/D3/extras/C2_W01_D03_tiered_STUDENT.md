# Tiered extras: Day 3

Two optional tasks. Take the one that matches where you are.

---

## Recovery: if the full pass did not come together

Work through these in order and stop when you are moving again.

**Step 1. Prove you can profile one field.**

Print `present` for `amount` only. You should see 48 out of 50. If this fails, the problem is the path or the field name, and the error message names which.

**Step 2. Prove you can profile every field.**

Wrap step 1 in a loop over `orders[0].keys()`. You should get seven lines. Do not add the other two counts yet.

**Step 3. Add convertibility.**

For `amount` only, count how many values survive `normalise_amount`. You should see 44. The gap of four against step 1 is the whole point of the day, so stop and look at it before moving on.

**Step 4. Add distinct.**

`len({r[field] for r in orders})`. One line. For `amount` you should see 46.

**Step 5. Now clean.**

Call `clean_records(orders)` from Tuesday, unchanged. You should see 44 clean and 6 rejected, and those two should sum to 50.

If step 5 gives a different number from step 3, one of them is counting something you did not intend, and finding which is worth more than finishing.

---

## Stretch: if you finished with time to spare

Do not reach for pandas. Go further into what you already have.

**Make the profiler tell you what it found.**

Right now your profiler prints numbers and leaves the reading to you. Write `describe_field(rows, field)` that returns one sentence per field, choosing from these shapes:

- present equals converts equals the row count, and distinct is small: a complete category
- present equals the row count and converts is zero: a complete text field
- present is below the row count: a field with gaps, and say how many
- converts is below present: a field with unusable values, and say how many
- distinct is below the row count on a field whose name ends in `_id`: an id that repeats, and say how many times

Run it on today's file. It should surface the `order_id` finding on its own, without anybody knowing to look for it. That is the difference between a profiler and a profile.

**The harder question.**

Your `describe_field` now flags a repeating id automatically. Would it have flagged the Rs 480,000 order? Should it?

Write four lines on where you would draw the line between a check that fires on its own and a judgement that needs a person. There is no correct answer and the reasoning is the whole exercise.

**The one that changes tomorrow.**

You kept the Rs 480,000 order because it is real. Compute two averages of the amount column, one with it and one without, and write both down with one sentence saying which you would give a manager who asked for the average order value.

Bring that sentence tomorrow. It is the first thing tomorrow argues about.
