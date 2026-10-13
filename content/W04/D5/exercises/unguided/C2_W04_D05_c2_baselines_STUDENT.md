# Naive, seasonal naive and drift baselines: which copy does the hostel mess trust, and when does it fail?

This set practises chapter 2, naive, seasonal naive and drift baselines, at the hostel mess
(invented), where every number is invented. Item 1 is the chapter's live check; items 2 and 3 are sat
in the lab's opening twenty minutes. Three words, each defined once: **naive** repeats the last value,
the **seasonal naive** copies the value one season back, and **drift** extends the line from the first
value to the last.

**Who needs the answer.** The mess manager (invented), who needs a rule a person can run on paper
before the rice is ordered, and who pays for every kilogram cooked and thrown away.

**The questions on the way.**

- Which rule, and what does it say for next Sunday?
- Which baseline do you trust after the mess has been closed?
- Which forecast fits a series that repeats and climbs?

**What you post,** in this set's thread in the cohort channel: three letters in item order, with no
spaces, in this shape:

```
Post exactly this shape: xxx
```

---

## Which copy fits the beat?

When a beat is strong, the plainest copy that respects it wins; the hard part is naming the beat.

### Q1. The mess's last four days used 25, 26, 25 and 27 kg of rice and last Sunday 42 kg: which rule fits, and what does it say for next Sunday?

*Level L1 · the chapter's live check.*

a) Naive, 27 kg: the last value repeated
b) Drift, about 27.7 kg: the line extended one day
c) Seasonal naive, 42 kg: last Sunday copied
d) The four days' mean, 25.75 kg: a smoothed day

## Which copy survives a closure and a climb?

### Q2. The mess closes for Diwali week and reopens the week after: which baseline do you trust for that week, and why?

*Level L4, a design call · asked in retail analytics screens.*

a) Naive, which copies the closed week's last day, since that is the latest value the mess has
b) The seasonal naive with a beat of 7 days, which copies the same days of the closed week
c) The same calendar week last year, 364 days back, since a year back holds the same season
d) The week after last year's closure, the same distance from the festival, since Diwali moves

### Q3. Sixteen weeks of rice ran 190, 186, 194, 238 kg, and then each cycle of four weeks 2 kg higher, ending at 196, 192, 200 and 244 kg: which forecast fits week 17, the first week of the next cycle?

*Level L4, a design call · asked in product-company screens.*

a) Naive, 244 kg: the last week, a guest week, copied forward
b) The seasonal naive with a season of four weeks, plus the 2 kg each cycle climbs: 198 kg
c) The seasonal naive with a season of four weeks, copying week 13 exactly as it stands: 196 kg
d) Drift from week 1 to week 16, the line extended one week: above 244 kg
