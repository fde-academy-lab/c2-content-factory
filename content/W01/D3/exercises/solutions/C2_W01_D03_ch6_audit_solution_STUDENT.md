# Solution: chapter 6 set: the log the analyst audits

Answers: 1c 2a 3b 4d 5c

3 of 5 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | c | read | A row reconciliation proves no row vanished, not that the right rows stayed; the missing rupees sit in a set-aside row whose kept twin lacks them. | a: rounding is where the gap hides. b: an adjustment line hides the cause. d: the books are the reference until a row proves otherwise. |
| 2 | a | read | 50,00,000 less 4,20,000 is 45,80,000, which equals the books, so the rupees reconcile. | b: the size of a move is not a test. c: that is what the row reconciliation proves. d: the rupee check stands on its own. |
| 3 | b | design | Test the amounts first so the rule can see which copy validates, then the rule, then rows, then rupees to the books. | a and c: running the rule before converting keeps the first copy even when it is unreadable. d: reconciling rows before the rule has nothing to reconcile. |
| 4 | d | design | About 24 lines tie both totals and let her replay the pass; the other hand-overs either take hours or prove only the rows. | a: no reasons and hours of comparison. b: shows what went, never why. c: ties the rows and nothing else. |
| 5 | c | design | The replay is independent of the pass: if the raw export less the logged lines equals the clean file, nothing went unlogged. | a: counts can match while the rows differ. b: proves reasons exist, not that every removal is listed. d: the same code reproduces the same mistakes. |
