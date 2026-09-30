# Solution: chapter 1 set: what the ERP actually sent

Answers: 1c 2b 3a 4d

2 of 4 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | c | read | A Q2 order at Rs 980 cannot be the largest when 21 Business orders start at Rs 2,10,000; `max()` compared the amounts as text, where 9 beats 2, so the note names a small order and the audit skips the money. | a: max() ranked the amounts by spelling, so reading every one did not help. b: the Business orders are Q2 orders in the same file, so the note still names the wrong one. d: the ERP holds the right value, and the fault is in how the colleague compared it. |
| 2 | b | design | All 12 fields are 14.4 crore values, 72 minutes at 20 lakh a minute, past the deadline; order_id and amount are 2.4 crore values, 12 minutes, which leaves half an hour to read what they flag. The key and the money fields are where a repeat or an unreadable amount would move Anand's figure. | a: 72 minutes, so the analyst starts with nothing. c: reads under a tenth of a percent of the rows and says nothing about the rest. d: a total cannot say why it differs from the books. |
| 3 | a | predict | 250 rows less 238 ids is 12 rows beyond one per order; 250 less 247 is 3 amounts that do not convert. | b: swaps the two counts. c: adds them into one. d: takes the 3 failures out of the 12, as if every failure were a copy. |
| 4 | d | design | 4 crore ids at 100 bytes each is about 4 GB, twice the memory free, so any route that holds every id at once stops part way; a sort can run on disk and has to remember only the id before. | a: needs about 4 GB. b: needs at least as much as a set, since it keeps a count beside every id. c: scales a count that does not scale, since repeated ids can sit anywhere in the file. |
