# Solution: chapter 6 set: the log the analyst audits

Answers: 1c 2a 3d 4b

3 of 4 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | c | read | Rows prove no row vanished and say nothing about which rows stayed; the missing rupees sit in a set-aside row whose kept twin cannot be summed. | a: a gap of any size is an order missing from a file called reconciled. b: an adjustment closes the gap without a cause. d: the books are the reference until a row proves otherwise. |
| 2 | a | design | The rule has to see which copy converts, so it runs first and keeps a readable copy; conversion then runs on what was kept, the rows equation needs the rejects count, and the rupee tie comes last, against the books. | b: step 3 converts the kept amounts, and nothing is kept before the rule runs. c: the rows equation counts the rejected rows, which exist only after conversion. d: converts and reconciles before anything is kept. |
| 3 | d | design | 24 + 4 + 5 + 2 is 35 lines, about 17 and a half minutes, and it ties both totals and lets her replay the pass. The clean file against the raw is 1,776 lines, about 15 hours, and a full diff 900 lines, 7 and a half hours, and neither says why. | a: about 15 hours, with no reasons. b: 7 and a half hours, showing what went and never why. c: one line, which ties the rows and nothing else. |
| 4 | b | design | The replay shares no code with the pass: if the raw export less the logged lines equals the clean file, nothing left without a line. | a: counts can match while the rows differ. c: proves each line has a reason, never that every removal has a line. d: the same code repeats the same mistakes. |
