# W04 D5 sources: what the pack cites, where it departs, and what it left unfixed

**INTERNAL.** One page for the reviewer. Every link was checked on 12 October 2026, either by the
research ledger (`docs/detailing/W04_research_cases.md`, R2, and `W04_research_teaching.md`, R1) or
afresh in this session where marked.

## Which sources does the pack cite?

| Source | Used for | Link, checked 12 October 2026 |
|---|---|---|
| Forecasting: Principles and Practice, 5.2, 5.8, 5.10 (fresh: section numbers, the test set "at least as large as the maximum forecast horizon", "a model which fits the training data well will not necessarily forecast well", percentage errors undefined at zero) | The four rules, the hold-out, MAE and MAPE, the rolling origin | https://otexts.com/fpp3/toolbox.html#sec-simple-methods, with the anchors #sec-accuracy and #sec-tscv (checked 12 October 2026) |
| Forecasting: Principles and Practice, 2.3 and 2.8 (fresh: "Seasonality is always of a fixed and known period", a cycle's rises and falls "are not of a fixed frequency", "autocorrelation measures the linear relationship between lagged values of a time series") | The four patterns of S7 and their picture; autocorrelation under half two's handoff line | https://otexts.com/fpp3/graphics.html#sec-tspatterns and #sec-acf (checked 12 October 2026) |
| Forecasting: Principles and Practice, chapters 8 and 9 (fresh: smoothing forecasts "are weighted averages of past observations, with the weights decaying exponentially as the observations get older"; ARIMA models "aim to describe the autocorrelations in the data") | Smoothing and ARIMA under half two's handoff line | https://otexts.com/fpp3/exponential-smoothing.html and https://otexts.com/fpp3/arima.html (checked 12 October 2026) |
| IBM Technology, "What is Time Series Analysis?" (fresh: title and channel through YouTube's oEmbed) | The notes' video | https://www.youtube.com/watch?v=GE3JOFwTWVM (checked 12 October 2026) |
| Makridakis, Spiliotis and Assimakopoulos, PLOS ONE 13(3), 2018 (F1) | 1,045 series; fit is not forecast | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0194889 (checked 12 October 2026) |
| M5 "Scores and Ranks" workbook (F2) | 0.847, 1.752, 0.977, 1.010, 0.520 | https://raw.githubusercontent.com/Mcompetitions/M5-methods/master/Scores%20and%20Ranks.xlsx (checked 12 October 2026) |
| Zillow, Q3 2021 shareholder letter (F3) | 200 and 1,200 basis points, USD 304 million, 25 percent | https://www.sec.gov/Archives/edgar/data/1617640/000161764021000085/exhibit993.htm (checked 12 October 2026) |
| Target, release of 15 January 2015, and Canadian Business, archived (F4) | 133 stores, about 17,600 employees; no history to forecast new stores | https://corporate.target.com/press/release/2015/01/target-corporation-announces-plans-to-discontinue-canadian-operations (checked 12 October 2026); https://www.gwern.net/docs/www/archive.canadianbusiness.com/edd0ae069905e7df1b073ae02516993a2bf4a1b9.html (checked 12 October 2026) |
| FADA, release of 7 November 2025 (F5) | 31,49,846 against 12,87,735; the 42-day window; GST cuts | https://fada.in/images/press-release/1690d68d7a2e6cFADA%20releases%20October%202025%20&%2042-Days%20Festive%20Vehicle%20Retail%20Data.pdf (checked 12 October 2026) |
| DoPT holiday lists, as reproduced by staffnews.in (F5) | Diwali on 31 October 2024, 20 October 2025, 8 November 2026 | The three staffnews.in URLs on the festival calendar card |
| Flipkart, announcement of 6 October 2026 (F6; fresh: "Ekart has added 14 million cubic feet of warehousing space ahead of TBBD" and "more than 2.5 lakh direct and indirect employment opportunities") | S13, the notes | https://stories.flipkart.com/announcement/flipkarts-big-billion-days-returns-for-its-13th-edition (checked 12 October 2026) |
| SIAM, FY 2025-26 release (T3) | The guesstimate's anchor, 2,17,05,974 | https://www.siam.in/news-&-updates/press-releases/x/605 (checked 12 October 2026) |
| Amazon Science, history of the recommendation algorithm (W1) | A bestseller list beat a deep-learning recommender | https://www.amazon.science/the-history-of-amazons-recommendation-algorithm (checked 12 October 2026) |

## Where does the pack depart from the spine, the row or the case file, and why?

| Departure | Why |
|---|---|
| The hold-out targets, the 2026 window and the vendor file follow the facts file's header, which lists nine corrections to the case file | The generator's data decide the numbers, and the case file's constants did not survive a real forecast |
| The rolling origin runs from five origins, not six | The twelve rows hold five one-week steps in 2025; a sixth needs a week the table does not print |
| Both transcripts sit in `extras/` as STUDENT files, the scorecards in `trainer/` | The fallback deck shows the [D] transcript to the room, so the room needs it; the scoring stays with the trainer |
| The take-home holds out four weeks, as the spine says, where the row says three months | The spine is approved after the row and wins |
| The notes run to 3,000 words, under the standard's 4,000 to 5,000 | The spine sets 2,000 to 3,000 for Friday and wins |
| The class sets carry 15 items and the practice set 6, 9 of the 21 design items | The spine's "about 14" counts the class sets; the TA lab's practice set is listed apart |
| S12 shows Diwali's 2026 week and stops; the house bot's misplacement is revealed in round three, at S28, S29 and the festival calendar card | The spine's L1 also places the 2026 copy, which would spend the tournament's round-three twist and the Veritasium vote before they run |
| The decks open on the ticket, with no quote cover | Acceptance line 1: the first minute is a ticket, with no quote |
| The plan's 2.6 percent cushion is read from the same thirteen weeks it is scored on | Said in the [D] transcript and the scorecard's push-back; the 2025 festival is the check that does not share the weeks |
| The explorer's Friday scenes, on branch `w04-explorer`, still carry the case file's old constants | Coordination: the report names every Friday number the scenes should show, by facts id |

## Which cold-read findings were left as they are, and why?

Filled after the fix pass.
