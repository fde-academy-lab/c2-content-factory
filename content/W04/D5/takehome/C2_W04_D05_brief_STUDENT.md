# Does the scoreboard change when only the last four weeks are hidden?

Flipkart, the Lucknow fulfilment centre. In class, the thirteen weeks from 29 June to 21 September
2026 were hidden and every rule forecast them from the week of 22 June 2026. On those weeks
festival-aligned and finance's rule missed by 6,615 shipments a week, the house bot (a copy of the
same week last year) by 9,831, drift by 14,842, naive by 14,923 and the vendor's curve by 16,400.
Illustrative case: the company is real, the situation and the data are synthetic, built for this
class.

Tonight you hide only the last four weeks instead, 31 August to 21 September 2026, forecast them from
the week of 24 August, and say what changed. It is about 60 minutes of work.

**Who needs the answer.** The regional operations head, who will hear the vendor's sponsor say "test
it on the latest four weeks, they are the most recent". Before the shift plan is signed, the head
needs to know whether a shorter test would have told a different story, and whether that story can
be trusted.

**The questions on the way.**

- What does each rule forecast for the four weeks, made from 24 August?
- How does each rule score in shipments, and priced in rupees?
- Which numbers moved from the thirteen-week test, and why?
- Does the pick for the staffing plan change?

## What do you build, and what do you hand in?

Start from a copy of notebook 02, which reads `content/W04/D5/data/C2_W04_D05_weekly_shipments_STUDENT.csv`
and the vendor's file beside it. Move the split: the last week every rule may see is 24 August 2026,
the 100th row (position 99), and the four rows after it are hidden.

Hand in one notebook that runs top to bottom, with these five things, each under a heading that is a
question:

1. The split: the origin week and its shipments, and the four hidden weeks with theirs.
2. Every rule rebuilt from the new origin. Naive repeats the week of 24 August. Drift extends the line
   from the first week to 24 August, so its step is the change over those weeks divided by 99. The
   house bot, finance's rule and festival-aligned copy 2025's weeks exactly as before. The vendor's
   rows for these four weeks are its old forecast, made from 22 June; score them, and say in one
   sentence why that is a different test from the other five.
3. The scoreboard: MAE in shipments, the weeks each rule sat too high, and the four misses priced at
   Rs 5.42 for each shipment planned and not shipped and Rs 25 for each shipment late.
4. One check by a second route: one rule's MAE worked by hand from its four printed misses, asserted
   equal to the code's.
5. A paragraph of four to six sentences for the regional operations head, plain words first: which
   numbers moved and why, which rule you would still send to the plan, and why a four-week test is
   too short to settle it.

## What makes the paragraph strong?

It names the origin week's shipments and says what that did to naive. It says which rules never
looked at the origin, and so barely moved. It says how far ahead of its own forecast the vendor's
four weeks sit. It ends on one call the regional operations head can repeat, with the length of test
the plan needs.

The self-check (`takehome/C2_W04_D05_selfcheck_STUDENT.md`) gives the numbers each rule should reach.
Open it after your notebook runs, never before.
