# Solution: chapter 1 scenario set: is the drop real

Answers: 1c 2b 3a 4d 5b 6c

3 of the 6 items are design items.

## Item by item

| Item | Kind | Key | Why it holds | Why the others fail |
|---|---|---|---|---|
| 1 | scenario | c | The change is measured against the starting quarter: Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent, on two closed windows of 13 weeks. | a: Measuring against Q2 inflates the fall to 12.3 percent. b: The rounded crore figures lose Rs 3,00,000 of the gap. d: The tile covers 11 weeks of Q2, so its fall is a window artefact. |
| 2 | scenario | b | The tile stopped on 15 September, so two weeks of Q2 are missing from one side only, and Rs 12 crore would move on a gap that is mostly the calendar. | a: Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is Q1. c: Both sides count booked orders, which is consistent. d: The totals are exact to the rupee. |
| 3 | design | a | The same weeks of both quarters control for length and for where in the quarter the weeks sit; the day Q2 closes, closed quarters answer the question directly. | b: That is the unmatched comparison that produced 25.9 percent. c: A projection assumes the last two weeks look like the first eleven, which Kalpa's lumpy weeks break. d: One month against one month discards most of both quarters and still mixes seasons. |
| 4 | design | d | On 200 rows each option takes well under a millisecond or two; what separates them is what each controls for: length, position in the quarter, or the season. | a: Speed and accuracy are unrelated here; the closed quarters are both fast and right. b: Every option computes a change; last year's Q2 cannot run at all. c: Option D reads no rows because the data is missing, and the sentence dodges what decides the call. |
| 5 | scenario | b | Q1 runs 1 April to 30 June, 91 days; Q2 runs 1 July to 30 September, 92 days, so per day Q2's total is divided by one more day. | a: With equal days the two agree exactly. c: The rate divides by calendar days in the window. d: Both figures are exact; they answer slightly different questions. |
| 6 | design | c | The first route trusted the `quarter` field and the second trusted only the dates; if any order's field disagreed with its date, the totals would differ. | a: The quarter key stays the headline; months are for questions inside a quarter. b: Both routes read the same amounts, so a wrong amount would fool both. d: The season is still in the comparison; only last year's Q2 removes it. |
