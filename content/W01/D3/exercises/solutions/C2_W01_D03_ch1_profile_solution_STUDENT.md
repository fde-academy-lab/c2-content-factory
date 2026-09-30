# Solution: chapter 1 set: what the ERP actually sent

Answers: 1c 2a 3d 4b 5d 6c

3 of 6 items are design items.

## Item by item

| Item | Key | Kind | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | c | read | Text compares character by character, and 9 sorts above 4 and 1, so `max` returns "950". | a: nothing converts the text. b: max takes the largest, never the middle. d: max works on text, which is why the mistake is silent. |
| 2 | a | design | North's two failed amounts are known and countable; South has 19 rows beyond one per order, which inflates any total. | b: converting cleanly says nothing about copies. c: a failure you can count is no reason to stop. d: equal row counts hide South's 19 extra rows. |
| 3 | d | read | 180 rows hold 171 orders, so 9 rows repeat an order and add rupees that were never earned. | a: an optional discount does not move booked revenue. b: three channels is right for app, web and store. c: two orders can share an amount. |
| 4 | b | read | The error names the line and column; reading it tells you whether the file was cut, malformed or merged. | a: skipping the feed hides the problem. c: asking before looking wastes the ERP team's time. d: a parse error on a file is not transient. |
| 5 | d | design | A profile reads every value in minutes and turns each defect into a count; reading rows only where it points keeps the work small. | a: the first thousand rows say nothing about the rest. b: a total cannot say why it differs. c: a sample of 1,000 has well under a one percent chance of meeting a single bad row. |
| 6 | c | design | Each row has the same chance to be drawn, so the one bad row is in the sample 20 times in 200, 10 percent. | a and b: overstate what a small sample sees. d: nothing about 20 rows guarantees one particular row. |
