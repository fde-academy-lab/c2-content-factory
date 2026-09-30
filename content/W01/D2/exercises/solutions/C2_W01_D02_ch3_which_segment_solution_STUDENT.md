# Solution: chapter 3 scenario set: which segment

Answers: 1d 2a 3c 4b 5a 6d

3 of the 6 items are design items.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | design | d | One place holds the definitions, so a change reaches every group, and any subset asked later is a single line. | a: Eight copies mean eight edits when the definition changes, and one gets missed. b: One pass wins on a huge file; here it is shaped for these eight groups only. c: It moves the work out of the pipeline the rest of the week builds on. |
| 2 | design | a | On a large file, reading the rows once instead of once per group is what matters; that is `groupby` in Week 2. | b: Changing definitions favour the function. c: Groups asked one at a time favour the function. d: That is today's file, where the function wins. |
| 3 | scenario | c | A function without `return` hands back `None`; the screen looked right and the caller got nothing. | a: An empty list would raise a division error. b: 1.65 is the right Q1 figure. d: Printing never changes a value. |
| 4 | scenario | b | Averaging gives a 2-customer segment the vote of a 34-customer one; total orders over total customers must give 114 over 69 and 86 over 69. | a: More decimals of a wrong roll-up stay wrong. c: Dropping groups hides the weighting problem. d: Medians of rates share the same flaw. |
| 5 | scenario | a | The median moved from Rs 9,83,780 to Rs 9,52,000, while one order of Rs 29,45,460 set the range; the fall is three fewer orders. | b: The median held. c: The range doubled, not the typical order. d: The mean is the number one order moves most. |
| 6 | design | d | Reading the rows once instead of once per group matters on a large file when every group is wanted together. | a: Groups asked one at a time favour the function. b: A changing definition favours one function holding it. c: On 200 rows the function costs nothing extra. |
