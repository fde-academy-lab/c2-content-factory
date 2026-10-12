# How much is coming, and how wrong could the forecast be?

Flipkart, the Lucknow fulfilment centre, Week 4 Friday. The planner books packer shifts for the eight weeks beginning 12 October to 30 November 2026; a vendor promises 22 percent above last year and finance 4 percent. Illustrative case: the company is real, the situation and the data are synthetic, built for this class.

## Panel 1: Where does the peak fall, and which rule wins on hidden weeks?

![Two festive seasons by calendar date and by weeks from Diwali: both peak two weeks before Diwali's week](../whiteboards/C2_W04_D05_festival_plot_STUDENT.png)

| Rule | MAE on 13 hidden weeks | Misses priced |
|---|---|---|
| Festival-aligned | 6,615 | Rs 13.5 lakh |
| Finance's rule | 6,615 | Rs 13.5 lakh |
| House bot | 9,831 | Rs 30.5 lakh |
| Drift | 14,842 | Rs 28.0 lakh |
| Naive | 14,923 | Rs 28.8 lakh |
| Vendor's curve | 16,400 | Rs 11.9 lakh |

**Crux:** Both years peak two weeks before Diwali's week, and only a copy that counts weeks from Diwali, scored on weeks it never saw, earns the plan.

## Panel 2: What do twelve weeks say, counted by hand?

| Weeks from Diwali's week | -3 | -2 | -1 | Diwali | +1 | +2 |
|---|---|---|---|---|---|---|
| 2024 | 312,900 | 401,000 | 356,200 | 296,900 | 180,600 | 212,700 |
| 2025 | 331,200 | 418,200 | 369,000 | 308,900 | 188,600 | 227,900 |

For Diwali 2025's week, 308,900 shipped: naive said 369,000, 60,100 too high; the house bot 356,200, 47,300 too high; festival-aligned 296,900 x 1.04 = 308,776, 124 too low.

**Crux:** A copy of the calendar lands a moving festival in the wrong week; a copy by distance from Diwali lands it.

## Panel 3: What does each rule copy?

| Rule | The forecast | In words |
|---|---|---|
| Naive | y[T] | Repeat the last week seen |
| House bot | y[t - 52] | The same week last year |
| Drift | y[T] + h x weekly change | The line from week one, extended |
| Finance's rule | 1.04 x y[t - 52] | The house bot plus 4 percent |
| Festival-aligned | 1.04 x the week at the same distance from last Diwali | Moves with the festival |

**Crux:** Every rule copies something from the past, so say what it copies before trusting what it says.

## Panel 4: How is a forecast scored?

- Hide the latest weeks, at least as many as the plan books: here 13, 29 June to 21 September 2026, forecast from 22 June.
- MAE is the average of the misses with their signs dropped, in shipments.
- Price each miss by its direction: Rs 5.42 a shipment too high, Rs 25 a shipment too low.
- The vendor's curve missed its 91 fitted weeks by at most 1.4 percent, and the hidden weeks by 16,400 a week.

**Crux:** Beat the bot on hidden weeks: in shipments, then rupees, against a copy of last year, before any model earns the plan.

## Panel 5: Where does each forecast put the festival in 2026?

| Forecast | Busiest week | Against 13 Oct to 1 Dec 2025 | Against 29 Sep to 17 Nov 2025 |
|---|---|---|---|
| House bot | 5 Oct | level | 13.0 percent below |
| Finance's rule | 5 Oct | 4.0 percent above | 9.5 percent below |
| Vendor's curve | 5 Oct | 22.0 percent above | 6.1 percent above |
| Festival-aligned | 19 Oct | 19.5 percent above | 4.0 percent above |

On 2025's festival, forecast from 22 September 2025, the house bot missed by 58,250 a week and festival-aligned by 4,034.

**Crux:** Copy by distance from Diwali: a calendar copy moved 2025's peak a week late and moves 2026's two weeks early.

## Panel 6: Where should the plan sit, and how many shifts?

`share of weeks covered = late / (late + idle) = 25 / (25 + 5.42) = 0.82`

- An idle shift is Rs 650 for 120 shipments, Rs 5.42 a shipment.
- The 0.82 point of festival-aligned's 13 hidden-week misses is 2.6 percent, so the plan is festival-aligned x 1.026.
- Shifts are the plan over 120, rounded up: 20,275 in eight weeks, 3,719 in the week of 19 October.
- The error bar is 6,615 shipments a week: Rs 35,832 if a week lands high, Rs 1.7 lakh if it lands low.

**Crux:** Plan at the 0.82 share: being short costs 4.6 times being long, so the plan sits 2.6 percent above the forecast.

## Panel 7: What does the interviewer listen for?

"I hide the latest weeks, as many as the plan covers, and score the misses in shipments against a copy of last year: festival-aligned missed by 6,615 a week, the house bot by 9,831." An AI company's launch capacity is planned the same way: days from launch, the last launch as the copy to beat, the plan above the forecast because a timeout costs more than an idle server.

**Crux:** Name the hidden weeks, the unit, the copy to beat and the direction that costs more.
