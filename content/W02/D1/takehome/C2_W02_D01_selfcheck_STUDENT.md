# Self-check before you hand in Monday's take-home

Nine checks. Run them against your own file, honestly. Six or fewer passing means the work is not
finished, and the fix is usually in the comment block rather than the SQL.

## The questions themselves

1. Read your two questions aloud with the word SQL removed. Do they still sound like something a
   finance controller would ask? A question phrased as "group orders by channel" fails; "which
   channel lost us the most in Q2" passes.

2. Is either question answerable by adding a `WHERE` to a suite query? If so, it does not count
   and you need a different one.

3. Could you defend spending ten minutes of Anand's time on the answer? If the honest answer is
   no, the question is technically fine and professionally pointless.

## The denominator line

4. Does your denominator line name what is **excluded**, not just what is divided? "Per customer"
   is incomplete. "Per customer who ordered in that quarter, so dormant customers are out" is
   complete.

5. For your denominator-focused question: how many observations sit under the smallest group in
   your result? If you do not know, you have not checked, and last week's Student segment is what
   happens next.

## The caveat line

6. Would your caveat survive somebody saying "so what"? "The data could be incomplete" does not.
   A caveat names a specific way the number misleads a specific reader.

7. Does your caveat point at something inside the query rather than outside it? A caveat about the
   business climate is not a caveat about your number.

## The SQL

8. Does every query have an `ORDER BY` if it has a `LIMIT`? Check, do not assume.

9. Run each query twice and compare the output row for row. If anything moved, an ordering is
   missing somewhere.

## The note

Read your four-or-five-sentence note and cross out every sentence that only says what you did. The
note should be about which question matters more and why, and if crossing out leaves you with one
sentence, write the note again.
