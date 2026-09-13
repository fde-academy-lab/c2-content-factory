# Solutions: where does this belong

Answers: 1a 2c 3b 4d 5a 6b 7b 8c

## Q1 and Q2, which are the pair worth the most

Both are Anand's world. Both are weekly. They get different answers.

Q1 is a number Finance acts on, needed indefinitely, read by an auditor who will not have you
beside him. The warehouse, on a schedule, with the comment line naming the question and the
denominator.

Q2 is the same underlying numbers, needed for one meeting, read by a director who wants to poke
them. Excel, built on the clean customer table.

The numbers are the same. Who reads them and what they do next is different, and that is what
picks the tool.

## Q3. The warehouse

A join and its row-count check belong where the join is defined. Option c is defensible and
option a is the one to argue with properly: a lookup down a payment column in Excel is a join
with no count check and no way to see a fan-out, which is precisely the failure the week has been
about.

## Q4. pandas, from the warehouse, in one run

Thursday's answer. Marketing's analysts build features on this table in Python, so it arrives in
Python. The warehouse owns the numbers underneath it.

## Q5. Excel, with the assumption in a marked input cell

This is the one thing Excel does that nothing else does: a stakeholder changes an assumption and
the answer moves in front of them. The condition is that the assumption is an input cell and
everything downstream is a formula.

Option d is the answer people give when their sheet is full of typed-over numbers, and it is worth
naming as the consequence rather than a constraint.

## Q6. pandas or the warehouse

Either is fine, and Excel is not, because removing duplicates by hand leaves no record of which
row was kept or why. The feed arriving as a spreadsheet does not change where it should be
cleaned.

## Q7. Excel, showing a number the warehouse computed

The split matters. Excel presents it; the warehouse computes it. Option a is the day's whole
lesson in a single wrong answer: computing the number in Excel from the raw export is what
doubled it.

## Q8. Refuse, because a corrected sheet cannot be rebuilt

The moment a sheet holds a correction that exists nowhere else, it has become a source of truth
and nobody decided that. The correction belongs upstream, where it can be applied again next
Monday.

Option a is the tempting compromise. Documenting a correction in a sheet does not make the sheet
rebuildable; it makes the loss visible after the fact.
