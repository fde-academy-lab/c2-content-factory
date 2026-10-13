# Week 4, concept-first: the revised day plans

On 13 October 2026 the requester read the Week 4 decks and asked for the curriculum's topics to come
first: concept chapters named by the row's subtopics, taught from zero on simple, complete, relatable
examples, with a concept map and a list of the day's topics, one notebook per chapter named by its topic,
and the real-company cases after them as applications, which stay. The requester asked for the build to
go ahead directly. The five plans in this folder carry that rebuild day by day, and they amend the day
shapes, sizes and acceptance lines of `../W04_analyst_craft_spine.md` wherever the two differ; the case
file, the cases' data and every number the cases print stand.

| Day | Row topic | Plan | Row subtopics, each taught by a concept chapter (a plan may split one subtopic or join two) |
|---|---|---|---|
| Monday 26 October | Business metric design | `D1_plan.md` | What to measure and why; the proxy test · North-star and guardrail metrics · Leading against lagging indicators · Definitions: numerator, denominator, window, exclusions · Gaming, and definitions that resist it · The metric definition artifact |
| Tuesday 27 October | Stakeholder communication | `D2_plan.md` | The one-slide answer: claim, evidence, caveat, action · What to leave out, and the appendix · Defending under challenge: restate, answer, concede, what would change your mind · The guesstimate: clarify, map, calculate, validate · The AI-free written business case |
| Wednesday 28 October | Market basket, lift and cross-sell | `D3_plan.md` | Support, confidence and lift, derived by counting · The confidence trap; lift near one · Basket analysis on the order items · The support floor and the watch list · Cross-sell and upsell reasoning; expected value in rupees |
| Thursday 29 October | Cohort and funnel | `D4_plan.md` | Cohort construction · Funnel stages, drop-off, denominators · Retention curves: shape and floor · Blended numbers against cohort truth · The fix-first decision and its evidence |
| Friday 30 October | Forecasting basics | `D5_plan.md` | Trend and seasonality, read before modelling · Naive, seasonal naive and drift baselines · Holding out; MAE and MAPE in the business's units · Beating the baseline; the vendor curve tested · The good-enough call and the forecast note |

## The shape every day takes

1. The ticket, as a short hook: the question the day answers, in two to ten minutes.
2. The topics slide and the concept map. The topics slide lists the row's subtopics verbatim, each with
   its chapter, its minutes and its notebook. The concept map shows how today's ideas connect to each
   other, to Weeks 1 to 3 and to the rest of the week.
3. The concept chapters, in the separate deck `slides/C2_W04_D0{d}_concepts_STUDENT.md`. Each chapter is
   headed `## SECTION n: <Topic>: <question>?` and taught from zero. It runs the misconception and a
   prediction, one invented everyday example (labelled) carried through the chapter, the idea derived from
   tiny numbers, a worked example and a check question, and it hands over to the case chapter that
   applies it.
4. The case chapters, in the half decks, each retitled `<Topic>: <question>?` with the concept it applies.
5. The Kalpa lab last.

The day's notebooks follow the same order: the concept notebooks first, one per concept chapter and named
by its topic (`C2_W04_D0{d}_01_<topic>_STUDENT.ipynb`), then the case notebooks renamed with the topic they
apply, then the Kalpa lab. `internal/C2_W04_D0{d}_coverage_INTERNAL.yaml` maps each row subtopic to its
chapter, deck, notebook, exercise items and Kahoot items, and `scripts/coverage_check.py`, which
`scripts/verify.py` runs, fails the day when a subtopic has none.

## Settled where a plan left a choice

- Wednesday's toy reads a lift of exactly 1.00, the value that means no association; it stands, since the
  0.05 margin from a Kalpa plant guards the cases' data and the twelve rows, and the toy is labelled
  invented. Wednesday's seventh chapter, cross-sell and expected value, opens the afternoon, so the morning
  carries at most four new ideas per two hours. The tea-stall toy retires there; Friday's chai stall
  carries forecasting.
- Tuesday's households trap stays at eight million, as the deck, the Kahoot and the Saturday paper already
  print it. The written business case follows the row's Kalpa brief, and the Uber page stays the worked
  example.
- Each day's invented examples are self-contained; where two days use a similar everyday setting, the
  second names it differently.
