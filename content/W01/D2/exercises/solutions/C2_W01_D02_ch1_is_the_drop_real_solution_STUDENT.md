# Solution: Did revenue really fall from Q1 to Q2, and by how much, once both sides cover the same weeks?

Answers: 1c 2b 3a 4d 5b 6c

Meera Raghavan, Kalpa Retail's CEO, asked whether revenue really fell from Q1, April to June, to Q2, July to September, before she answers Marketing's request for Rs 12 crore to win new customers. The request rests on a slide showing a fall of 25.9 percent. Revenue is booked revenue, every order placed at the price charged before any cancellation or return: Rs 2,10,00,000 in Q1 and Rs 1,87,00,000 in Q2, both quarters closed, against Rs 1,55,59,950 on a dashboard tile read on 15 September.

Three of the six items are design items: 3, 4 and 6.

### Q1. How far did revenue fall between the two closed quarters?

Meera asks how far revenue fell between the two closed quarters, Rs 2,10,00,000 in Q1 and Rs 1,87,00,000 in Q2.

The key is c, "11.0 percent, the Rs 23,00,000 gap measured against Q1's total". A change is measured against the quarter it starts from. Rs 23,00,000 over Rs 2,10,00,000 is 11.0 percent, on two closed quarters of 13 weeks each.

- a, "12.3 percent, the Rs 23,00,000 gap measured against Q2's total": measuring the gap against Q2's total inflates the fall to 12.3 percent.
- b, "9.5 percent, from the rounded Rs 1.9 crore against Rs 2.1 crore": the rounded crore figures lose Rs 3,00,000 of the gap.
- d, "25.9 percent, the figure on the dashboard tile Marketing quotes": the tile stops on 15 September, so part of its fall comes from the shorter window.

### Q2. Why does Marketing's slide say revenue fell 25.9 percent?

Marketing's slide sets the Q2 dashboard tile, Rs 1,55,59,950 read on 15 September, against all of Q1, Rs 2,10,00,000, and reports a fall of 25.9 percent.

The key is b, "It sets about 11 weeks of Q2 against all 13 weeks of the closed Q1". The tile runs from 1 July to 15 September, about 11 weeks, against Q1's 13, so two weeks are missing from one side only, and Rs 12 crore would move on a gap that is mostly the calendar.

- a, "The percentage is computed on Q2's total, which overstates the fall": Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is already Q1.
- c, "It counts booked orders, where a count of delivered orders would be lower": both sides count booked orders, so the definition is the same on each.
- d, "It rounds both totals to the nearest lakh before dividing them": both totals are exact to the rupee.

### Q3. What does revenue per week give on 15 September, and what does it miss? (Design)

On 15 September, with Q2 still open, a colleague divides each side of Marketing's slide by the weeks its dates cover.

The key is a, "Minus 12.4 percent, and it still compares Q2's early weeks with the whole of Q1". Rs 16,15,385 a week against Rs 14,14,541 is minus 12.4 percent. A rate evens out the length of the two windows and leaves their position as it was, so Q2's first eleven weeks still stand against all of Q1. While Q2 is open the same 11 weeks of each quarter fit better, and the two disagree here (minus 17.0) because a few lakh-sized orders make weeks lumpy.

- b, "Minus 25.9 percent, since dividing both sides by weeks leaves their ratio alone": dividing one side by 13 and the other by 11 changes the ratio by 13 over 11.
- c, "Minus 11.0 percent, since a rate per week removes every difference in the windows": 11.0 percent is the closed quarters' figure, which needs Q2 to have closed.
- d, "Minus 17.0 percent, the answer that matched weeks of each quarter would give": the same weeks give minus 17.0 because Kalpa's weeks are lumpy, so the two methods disagree on this file.

### Q4. Which comparison answers Meera's question about the monsoon? (Design)

With both quarters closed, Meera asks whether Q2 is always weaker than Q1 because of the monsoon.

The key is d, "The same quarter last year, which needs last year's export to run". Only a comparison with the same season a year earlier takes the season out. The file holds April to September of one year, so the answer needs a data request.

- a, "Closed quarters again, since both are complete and compare like with like": closed quarters fix the length, and the two quarters are still different seasons.
- b, "A rate per day, since it removes the one-day gap between 91 and 92 days": a rate per day evens out the length of the quarters and leaves the season in.
- c, "The same 11 weeks of each quarter, since it also matches position": matched weeks fix the position inside a quarter, and Q1 and Q2 are still different seasons.

### Q5. In which order do the four moves that test the drop run?

Four moves test whether the drop is real: compute the change (p), find each window's first and last order date (q), state the definition and the window to Meera (r), and choose closed quarters or matched weeks (s).

The key is b, "q, s, p, r". Read the windows, choose a fair pair, compute the change, then state the definition and the window in the sentence to Meera.

- a, "s, q, p, r": it chooses a pair before anyone has read the dates.
- c, "q, p, s, r": it computes before choosing the fair pair, which is how the tile's number reached a slide.
- d, "q, s, r, p": it writes the sentence before the number it states exists.

### Q6. What does adding revenue by month prove when it matches the closed quarters? (Design)

The second route added revenue by the month in `order_date` and reached the same fall as the first route, which added it by the `quarter` field.

The key is c, "That the quarter field and the dates give each quarter the same total". The first route trusted the `quarter` field and the second read only the dates, and both give each quarter the same total. That is agreement in aggregate: two mislabelled orders of equal value could still cancel out, so an order-by-order check is the stronger proof.

- a, "That monthly totals are a better headline for Meera than the quarters": the quarter stays the headline, and months are for questions inside a quarter.
- b, "That no order in the file carries a wrong amount or a missing field": both routes read the same amounts, so a wrong amount would fool both.
- d, "That the fall is real and needs no comparison with last year": the season is still in the comparison, and only last year's Q2 takes it out.
