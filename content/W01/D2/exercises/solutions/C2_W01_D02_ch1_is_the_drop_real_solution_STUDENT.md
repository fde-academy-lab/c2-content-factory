# Solution: chapter 1 scenario set: is the drop real

Answers: 1c 2b 3a 4d 5b 6c

3 of the 6 items are design items.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | scenario | c | The change is measured against the starting quarter: Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent, on two closed windows of 13 weeks. | a: Measuring against Q2 inflates the fall to 12.3 percent. b: The rounded crore figures lose Rs 3,00,000 of the gap. d: The tile covers 11 weeks of Q2, so its fall is a window artefact. |
| 2 | scenario | b | The tile stopped on 15 September, so two weeks of Q2 are missing from one side only, and Rs 12 crore would move on a gap that is mostly the calendar. | a: Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is Q1. c: Both sides count booked orders, which is consistent. d: The totals are exact to the rupee. |
| 3 | design | a | The same weeks of both quarters control for length and for where in the quarter the weeks sit; the day Q2 closes, closed quarters answer the question directly. | b: That is the unmatched comparison that produced 25.9 percent. c: A projection assumes the last two weeks look like the first eleven, which Kalpa's lumpy weeks break. d: One month against one month discards most of both quarters and still mixes seasons. |
| 4 | design | d | On 200 rows each option that can run takes a millisecond or two, and last year's Q2 cannot run at all; what separates them is what each controls for: length, position in the quarter, or the season. | a: Speed and accuracy are unrelated here; the closed quarters are both fast and right. b: Every option computes a change; last year's Q2 cannot run at all. c: Rows read and accuracy are unrelated: the closed quarters and per-day options read the same 200 rows and give different answers. |
| 5 | scenario | b | Find the windows, choose a fair pair, compute, then say the definition and the window in the sentence to Meera. | a: Computes before the windows are known, which is how the tile's number reached a slide. c: Chooses and computes before anyone has read the dates. d: Computes before choosing the fair pair. |
| 6 | design | c | The first route trusted the `quarter` field and the second only the dates, and both give each quarter the same total, which is agreement in aggregate; two mislabelled orders of equal value could still cancel out, so an order-by-order check is the stronger proof. | a: The quarter key stays the headline; months are for questions inside a quarter. b: Both routes read the same amounts, so a wrong amount would fool both. d: The season is still in the comparison; only last year's Q2 removes it. |
