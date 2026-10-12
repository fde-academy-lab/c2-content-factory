# How does a strong candidate answer "how do you evaluate a forecast?", and the dispute that follows it?

Written for this programme in the style of product-company and GCC screens; the facts inside are
from the case file. A screen is an interview round, and a GCC, a global capability centre, is a
multinational company's own technology and analytics centre in India. The numbers are Friday's
Flipkart case at the Lucknow fulfilment centre. Illustrative case: the company is real, the
situation and the data are synthetic, built for this class.

**Who needs the answer.** You, before any analytics, data-science or AI-startup screen that asks
about forecasts, capacity or planning. The interviewer is deciding whether you test a forecast on
weeks it never saw before you trust its story.

**The questions on the way.**

- What does the interviewer say, and which clarifying questions come first?
- What structure carries the answer, and which trap is being fished for?
- How do a weak and a hire-grade answer compare?
- What follows up, and which line answers each?
- How does the same question come up at an AI company?
- What does the second transcript, the dispute, ask?
- What does the scorer listen for?

## Transcript 1: "How do you evaluate a forecast?"

Tagged [S], a staple asked everywhere.

### What does the interviewer say?

> "A fulfilment centre has two years of weekly shipments and three forecasts for the coming festive
> season. How do you evaluate a forecast?"

### Which clarifying questions does a strong candidate ask first?

1. "What decision does the forecast feed, and how far ahead is it booked?" The answer sets the test's
   length: eight weeks of packer shifts.
2. "What does a miss cost in each direction?" The answer sets the price: Rs 25 for a late shipment,
   Rs 650 for an idle shift of 120 shipments.
3. "Does the festival fall on the same week every year?" It does not: Diwali moved one week earlier in
   2025 and moves two weeks later in 2026.
4. "Has any of the three been scored on weeks it never saw?" The answer says whether the evidence is a
   fit or a forecast.

### What structure carries the answer?

1. Fix the error measure before scoring anything: the average miss in the business's unit.
2. Hide the latest weeks, at least as many as the plan books, and forecast them from one week.
3. Score every forecast against the simplest copies: the last week, and the same week last year.
4. Price the misses by direction, and set the plan's level from the two costs.
5. Name what the test cannot see, and test that another way.

### Which trap is the interviewer fishing for?

The candidate judges by fit ("the model matches two years within 2 percent"), or splits the
difference between two forecasts. Either answer sends an untested number to the plan.

### How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| The test | "I would check how well each model fits the history." | "I hide the latest thirteen weeks, 29 June to 21 September 2026, which is longer than the eight-week plan, and forecast them from 22 June." |
| The measure | "R-squared, or maybe MAPE." | "The average miss in shipments, MAE, fixed before anyone scores, because shifts are booked in shipments." |
| The bar to beat | Not reached. | "A copy of the same week last year, the house bot: 9,831 a week. Festival-aligned and finance's rule beat it at 6,615; the vendor's curve misses by 16,400, too high in 12 of 13 weeks, though it fits its 91 past weeks within 1.4 percent." |
| The price | Not reached. | "Priced, the vendor's misses cost least, Rs 11.9 lakh against Rs 13.5 lakh, because spare capacity costs Rs 5.42 a shipment and a late one Rs 25. So I lean high on purpose: the plan covers demand in 0.82 of weeks, festival-aligned plus 2.6 percent." |
| What the test cannot see | Not reached. | "The hidden weeks hold no festive week, so I back-test the 2025 festival from data to 22 September 2025: the house bot missed by 58,250 a week, festival-aligned by 4,034." |
| What would change it | Not reached. | "A third year of data, or a sale that opens a different distance before Diwali; either would move the plan's peak." |

### What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "MAE in shipments or MAPE in percent, and when?" | "MAE in shipments when the cost is per shipment and the plan books shipments. MAPE when I compare series of different sizes, say Lucknow with a centre twice its size, and never where an actual can sit near zero, since a percent of almost nothing explodes (Forecasting: Principles and Practice, section 5.8, checked 12 October 2026)." |
| "The festival moves by three weeks this year. What breaks?" | "Every calendar copy, the house bot and finance's rule, puts the peak three weeks off. A copy by distance from the festival moves with it. I would also check that the sale still opens the same distance before the festival, since the peak follows the sale; if it moves, I copy by distance from the sale." |
| "What did forecast error cost Zillow, and which guardrail failed?" | "Zillow priced homes on forecasts three to six months ahead inside public targets of plus or minus 200 basis points of breakeven. In 2021 its unit economics swung about 1,200 basis points toward minus 500 to minus 700, it wrote down about USD 304 million and cut about 25 percent of its workforce (Zillow's Q3 2021 shareholder letter, checked 12 October 2026). The guardrail bounded the forecast, and the forecast was what failed." |

### How does the same question come up at an AI company?

> "We launch a new assistant feature in six weeks. How do you forecast inference demand for launch
> week, and how do you know the forecast is any good?"

The strong candidate clarifies first: "Demand in what unit, requests a minute at the peak? How long
does it take to add capacity? What does a timeout cost us against an idle machine for an hour?"

The launch is the festival. Line the last launch up by days from launch day, never by calendar date,
because a weekday launch and a weekend launch peak on different dates. The copy to beat is the last
launch's shape, scaled by how the user base has grown since. Hide the last launch's own days as the
test, as many days as the plan books, and score every forecast in requests a minute. Then plan above
the forecast, since a timeout loses a user and an idle machine loses an hour of rent; the share of
minutes to cover is the cost of a timeout over the two costs added, the same arithmetic as the
packer shifts. A model that cannot beat the last launch's shape on those hidden days does not size
the launch. This variant is written for this programme and quotes no company's figures.

### Which pain points hide inside the question, each with a real case?

| Pain point | The case | The check |
|---|---|---|
| A close fit taken for a good forecast | A 2018 PLOS ONE paper by Makridakis and colleagues: on 1,045 monthly series, statistical methods beat machine-learning ones at every horizon, and the best fits to the past did not forecast best (checked 12 October 2026) | Score on weeks the model never saw |
| A forecast with no history | Target Canada: its replenishment system could not forecast new stores, so buyers used optimistic projections, and Target closed all 133 stores, with about 17,600 employees (Target's release of 15 January 2015, checked 12 October 2026) | Score the model on a festival it did not see before it books a shift |
| A guardrail breached by the forecast it bounded | Zillow, 2021, above | Watch every week's miss against the band, and stop when it is breached |
| A calendar week taken for a festival | FADA counts its festive window from the festival each year, 42 days from the first day of Navratri (FADA's release of 7 November 2025, checked 12 October 2026) | Line years up by distance from the festival |
| A model never compared with the simplest copy | Amazon Science's history of its recommendation algorithm records a Prime Video test in which a plain bestseller list beat a deep-learning recommender (checked 12 October 2026) | Put a copy of last year on every scoreboard |

## Transcript 2: "Finance and the vendor's sponsor each want theirs in front of the plan"

Tagged [D], a differentiator. The fallback hour runs this one.

### What does the interviewer say?

> "Finance wants last year plus 4 percent; the vendor's sponsor wants the curve at plus 22. Both are
> senior to you, and the plan is due Friday. What do you put in front of the regional operations
> head, and how do you present the error?"

### Which clarifying questions does a strong candidate ask first?

1. "Plus 4 and plus 22 against which weeks of last year?" Both are measured against the same calendar
   weeks, which hold only the tail of last year's festival.
2. "Has either been scored on weeks it never saw?" Finance's rule has, by the hold-out; the vendor's
   promise for the festive window has not.
3. "Who carries the cost of a short week, and who of a spare shift?" The answer says which way to
   lean.

### What structure carries the answer?

The four moves from Tuesday (restate, answer from the evidence, concede what is true, say what would
change your mind), then the plan, its error bar in each direction, and the next check.

### Which trap is the interviewer fishing for?

Splitting the difference, 13 percent between 4 and 22, or siding with the more senior person. Both
skip the evidence, and the midpoint keeps the calendar copy's peak on the wrong week.

### How do a weak answer and a hire-grade answer compare?

| | Weak answer | Hire-grade answer |
|---|---|---|
| Restate | "Both numbers have problems." | "Finance wants a rule it can explain, and the sponsor wants a model that fits history closely; both want the plan to hold in the festival." |
| Answer | "I would average them: 13 percent." | "Neither goes to the plan as it stands. Scored on thirteen hidden weeks, finance's rule ties festival-aligned at 6,615 a week and the vendor misses by 16,400. On 2025's festival, a calendar copy missed by 58,250 a week and festival-aligned by 4,034. So the plan is festival-aligned plus 2.6 percent: 20,275 packer shifts, peaking at 3,719 in the week of 19 October." |
| Concede | Nothing conceded. | "To finance: your 4 percent is the growth two years show, and your rule ties ours on the hidden weeks. To the sponsor: your curve fits history within 1.4 percent, and its misses on the hidden weeks are the cheap kind." |
| What would change it | Not said. | "A third year of data, a sale that opens at a different distance from Diwali, or the curve beating the house bot on a festival it never saw." |
| The error | One number. | "6,615 shipments a week: Rs 35,832 of idle shifts if a week lands high, Rs 1.7 lakh of late shipments if it lands low." |

### What follows up, and which line answers each?

| Follow-up | The hire-grade line |
|---|---|
| "Why not average the two and keep both happy?" | "Both are copies of the calendar, so their average books the peak on 5 October too, two weeks before the rush. Averaging two forecasts with the same error keeps the error." |
| "Finance says its rule tied yours. Why not use finance's?" | "On the hidden weeks it did tie, because those weeks hold no festival. On 2025's festival, forecast from 22 September 2025, finance's rule missed by 60,488 a week against festival-aligned's 4,034." |
| "The sponsor says the vendor's misses cost least. Answer that." | "True on the hidden weeks: Rs 11.9 lakh against Rs 13.5 lakh, because it leans high. But nobody chose how high, and it climbs with the weeks ahead, 3.6 percent too high in the first six to 11.5 in the last six. Raised by 2.6 percent on purpose, festival-aligned's misses on the same weeks price at Rs 8.8 lakh, a figure flattered a little because the 2.6 was read from those weeks." |

## What does the scorer listen for?

When you practise in pairs, the asker scores each of these from 0 to 2: clarified the scope; named
the hidden weeks and the unit; saw the paradox (a close fit, or cheap misses, that do not earn the
plan); sized it with a unit (shipments, shifts or rupees); said what would change their mind; tied
it to a decision and its cost; gave the structure before the number.
