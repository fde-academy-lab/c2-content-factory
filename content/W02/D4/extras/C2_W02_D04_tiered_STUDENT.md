# Thursday's extras

## Recovery: if groupby still feels like magic

Take twenty order rows, no more, and do it by hand on paper. Write the customer ids down the left,
then tally each order under its customer, then total each tally.

That is split, apply, combine, and you have just done all three yourself. Now write the `groupby`
that does it and point at which part of your paper each piece of the call replaced.

Then do the same for `agg` with two measures, and notice that only the applying changed.

If the merge is the part that blurs, run today's demo page and change the feed between "as
delivered" and "aggregated" with `validate="one_to_one"` set. Watch the same call succeed and
fail on the same claim.

## Stretch: three that go past today

**One.** The customer table is built from `orders` alone, so a customer who never ordered is
absent entirely. Rebuild it starting from `customers` instead, so all 340 appear and the ones who
never ordered carry zeros or NaNs. Then write two sentences on which version Marketing should get
and what the difference does to any average computed from it. This is a denominator question
wearing a pandas costume.

**Two.** Today's merges all used `validate=`. Find a pair of tables in the warehouse where
`one_to_one` is genuinely correct and prove it, then find a pair where `many_to_one` is the
honest claim and say what would have to change in the data for it to start failing.

**Three.** The reshape round trip is not the identity: pivot then melt gives you more rows than
you started with, because every gap became a cell and every cell became a row. Demonstrate it with
numbers, then write one sentence on when those extra rows are a bug and when they are the point.

## If you want tomorrow's advantage

Tomorrow the chief of staff wants three things that open on a laptop with no login.

Tonight, open any spreadsheet you have and try to break a lookup on purpose: search for a value
that is not there and see what comes back. Write down what happened. Tomorrow you will find out
whether what happened was the safe behaviour or the dangerous one.
