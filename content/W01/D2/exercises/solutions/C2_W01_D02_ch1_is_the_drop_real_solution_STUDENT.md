# Solution: chapter 1 scenario set: is the drop real

Answers: 1c 2b 3a 4d 5b 6c

3 of the 6 items are design items.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | scenario | c | The change is measured against the starting quarter: Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent, on two closed quarters. | a: Measuring against Q2 inflates the fall to 12.3 percent. b: The rounded crore figures lose Rs 3,00,000 of the gap. d: The tile stops on 15 September, so its fall is partly a window artefact. |
| 2 | scenario | b | The tile runs 1 July to 15 September, about 11 weeks, against Q1's 13, so two weeks are missing from one side only and Rs 12 crore would move on a gap that is mostly the calendar. | a: Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is Q1. c: Both sides count booked orders, which is consistent. d: The totals are exact to the rupee. |
| 3 | design | a | Rs 16,15,385 a week against Rs 14,14,541 is minus 12.4 percent. A rate fixes the length and not the position: Q2's first eleven weeks stand against all of Q1, so while Q2 is open the same 11 weeks of each quarter are the better fit, and the two disagree here (minus 17.0) because a few lakh-sized orders make weeks lumpy. | b: Dividing by 13 and by 11 changes the ratio by 13 over 11. c: 11.0 is the closed quarters, which needs Q2 closed. d: The same weeks give minus 17.0 because Kalpa's weeks are lumpy, so the two methods disagree on this file. |
| 4 | design | d | Only a comparison with the same season a year earlier takes the season out, and the file holds April to September of one year, so it needs a data request. | a: Closed quarters fix the length, and the two quarters are still different seasons. b: A rate per day fixes a day, not a season. c: Matched weeks fix the position inside a quarter; Q1 and Q2 are still different seasons. |
| 5 | scenario | b | Read the windows, choose a fair pair, compute, then say the definition and the window in the sentence. | a: Chooses a pair before anyone has read the dates. c: Computes before choosing the fair pair, which is how the tile's number reached a slide. d: Writes the sentence before the number it states exists. |
| 6 | design | c | The first route trusted the `quarter` field and the second only the dates, and both give each quarter the same total, which is agreement in aggregate; two mislabelled orders of equal value could still cancel out, so an order-by-order check is the stronger proof. | a: The quarter key stays the headline; months are for questions inside a quarter. b: Both routes read the same amounts, so a wrong amount would fool both. d: The season is still in the comparison; only last year's Q2 removes it. |
