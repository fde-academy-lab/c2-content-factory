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

1. The topic cover, carrying the row's Day focus, then the week map with today lit.
2. The topics slide and the concept map. The topics slide lists the row's subtopics verbatim, each with
   its chapter, its minutes and its notebook. The concept map shows how today's ideas connect to each
   other, to Weeks 1 to 3 and to the rest of the week. Then the case ticket in one slide, as the
   destination the topics will be used on.
3. The concept chapters, at the front of `slides/C2_W04_D0{d}_half1_STUDENT.md`, right after the topics slide, the map and the ticket slide.
   Each chapter's opener is headed `## SECTION n: <Name>: <short question>?`. The Name is the row's subtopic verbatim (Wednesday's spanning
   Name excepted), which the coverage gate reads; the short question starts lower-case, ends in a
   question mark and runs to about 24 characters, since the deck prints the Name over the question on the
   opener and the short question alone in the chapter pills, whose room is about 22 characters; the
   italic promise beneath says what the chapter delivers. Where a plan titles a chapter as a question,
   that question becomes the promise. The chapter is taught from zero and runs the misconception and a
   prediction, one invented everyday example (labelled) carried through the chapter, the idea derived
   from tiny numbers, a worked example and a check question, and it hands over to the case chapter that
   applies it. A concept chapter that the four-ideas-per-two-hours rule moves to the afternoon opens `half2`,
   still before the case chapter that applies it.
4. The case chapters, after the concept block in the same decks, each opener headed the same way with the
   case step and the subtopics it applies as its topic. The full ticket read opens them where the plan
   moves it there.
5. The Kalpa lab last.

SECTION numbers run in deck order, `half1` then `half2`, and each notebook is numbered as its chapter, so
the morning's concept notebooks come first: `C2_W04_D0{d}_0n_<topic>_STUDENT.ipynb`, the file name
carrying at least two of the Name's idea-words, so Monday's `04_definition_lines` becomes
`04_numerator_denominator_window_exclusions` and Tuesday's guesstimate notebook carries
`guesstimate_clarify_map_calculate_validate`. Each case notebook is renamed with the topic it applies,
and the Kalpa lab comes last.
`internal/C2_W04_D0{d}_coverage_INTERNAL.md`, in the shape
`.claude/skills/day-pack-builder/references/coverage-matrix.md` sets, maps each row subtopic to its chapter, slides, notebook,
exercise items, Kahoot items and minutes, and each case chapter to the subtopics it applies;
`scripts/coverage_check.py`, which `scripts/verify.py` runs, fails the day when a subtopic has no chapter
or no notebook carrying its name. Where a plan names a separate concepts deck, its concept slides go to
the front of `half1` instead and the plan is otherwise unchanged.

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
- Tuesday's two spoken and written chapters (defending under challenge, the written business case) each
  get a notebook that holds the chapter's example as data, so every chapter has its notebook.
- The concept block takes the sizes the plans give it. On a day with a faculty block, a case chapter's
  deeper slides are marked `D` for self-study; the twelve-row count, the trap, the unguided round, the
  interview room and the Kalpa lab are never cut.
- Thursday's fifth concept chapter, the fix-first decision, opens the afternoon, as Wednesday's seventh
  does, so the morning keeps to four new ideas per two hours.
- The explorer's home map gains each day's subtopics on its day nodes once the five days merge.
- Weeks 1 to 3: Week 2 Wednesday to Friday name their topics in their decks before each day runs; Week 1
  and Week 2 Monday and Tuesday, already taught, get revision notes headed by their row subtopics before
  ME1, the first major exam, in Week 5; Week 3 Monday gets a topics slide.
- Tuesday's guesstimate and written-business-case chapters open the afternoon after studio round two,
  each before the case chapter that applies it, as its plan keeps each example beside the case step that
  uses it; the morning carries the first three.
- Wednesday's 73-minute case chapter splits in two, the twelve carts and the three measures, then the
  pairs table and the confidence trap on 40,000 carts, so each chapter has one notebook; cross-sell
  becomes SECTION 9 and the afternoon's case chapter SECTION 10. The afternoon runs the cross-sell
  chapter, the priced strip, the unguided round, a short interview beat and the close in 60 minutes,
  and the interview room's reading moves to the lab.
- The invented example tables are written to `data/` by the day's seeded generator and recorded under
  `toy_` ids; each concept notebook loads its table and prints it in full, labelled invented.
