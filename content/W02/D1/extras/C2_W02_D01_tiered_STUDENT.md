# Monday's extras

Two paths. Take the one that matches where you actually are, not where you would like to be.

## Recovery: if the execution order did not land

Do this before tomorrow, because tomorrow assumes it.

Take one query you wrote today and write the seven stages down the left of a page. Beside each
stage, write how many rows exist at that moment. For the segment query on Q1 that reads 1,000 at
`FROM`, 538 after `WHERE`, 4 after `GROUP BY`, 4 after `SELECT`.

Then do the same for a query that failed today, and stop at the stage where it failed. The number
beside that stage is usually the explanation.

If that still feels thin, redo SQLBolt lessons 1 to 5 and stop after each one to say which stage
of the picture it was about.

## Stretch: three questions the suite cannot answer

Each of these is answerable with what you know today, and each one takes a turn you have to find.

**One.** Which customers ordered in Q1 and not in Q2? You have no join tools for this yet beyond
what you used today, so the honest route is two CTEs and a `NOT IN`. Write it, then write one
sentence on what `NOT IN` does when the inner list contains a NULL. Test that sentence rather than
trusting it.

**Two.** What share of Q1 revenue came from the largest ten orders? Getting the numerator is easy.
Getting numerator and denominator into the same result without running two queries is the turn.

**Three.** The suite reports orders per customer as a single average per segment. Find the segment
where that average is least honest, and prove it with one query. The word to reach for is not in
today's material, and finding that out is the point.

## If you want tomorrow's advantage

Open the `payments` table and look at five rows. Do not analyse it. Just look, and count how many
payment rows the same `order_id` can have.
