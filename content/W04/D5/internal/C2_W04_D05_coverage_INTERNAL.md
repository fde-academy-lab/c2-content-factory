# Coverage matrix, Week 4 Friday

Row: docs/curriculum/W4_Analyst_craft.md, "Fri 30 Oct 2026 · Forecasting basics"
Subtopics in the row: 5

## The row's subtopics and where each is taught

| # | Subtopic (verbatim from the row) | Name in the chapter title and the notebook | Chapter | Slides | Notebook | Exercise items | Kahoot items | Minutes |
|---|---|---|---|---|---|---|---|---|
| 1 | Trend and seasonality, read before modelling | Trend and seasonality, read before modelling | SECTION 1: Trend and seasonality, read before modelling: what does a series tell? | half1 S6 to S13 | notebooks/C2_W04_D05_01_trend_and_seasonality_STUDENT.ipynb | c1_trend_seasonality Q1 to Q3; staffing_note Q4; lab_set Q1 | Q8 | 22 |
| 2 | Naive, seasonal naive and drift baselines | Naive, seasonal naive and drift baselines | SECTION 2: Naive, seasonal naive and drift baselines: when does a copy fail? | half1 S14 to S21 | notebooks/C2_W04_D05_02_naive_seasonal_naive_drift_STUDENT.ipynb | c2_baselines Q1 to Q3; same_week_rule Q1, Q3; lab_set Q2, Q5 | Q1 | 23 |
| 3 | Holding out; MAE and MAPE in the business's units | Holding out; MAE and MAPE in the business's units | SECTION 3: Holding out; MAE and MAPE in the business's units: how is a forecast scored? | half1 S22 to S29 | notebooks/C2_W04_D05_03_holdout_mae_mape_STUDENT.ipynb | c3_holdout_mae_mape Q1 to Q4; same_week_rule Q2; ch2_scoreboard Q1, Q2; kalpa_board Q1; lab_set Q3, Q6 | Q2, Q5, Q7 | 30 |
| 4 | Beating the baseline; the vendor curve tested | Beating the baseline; the vendor curve tested | SECTION 4: Beating the baseline; the vendor curve tested; the good-enough call and the forecast note: when does it earn trust? | half1 S30 to S33 | notebooks/C2_W04_D05_04_beating_the_baseline_good_enough_STUDENT.ipynb | c4_beat_baseline_good_enough Q1, Q2; ch2_scoreboard Q3; kalpa_board Q2; lab_set Q4 | Q3 | 10 |
| 5 | The good-enough call and the forecast note | The good-enough call and the forecast note | SECTION 4: Beating the baseline; the vendor curve tested; the good-enough call and the forecast note: when does it earn trust? | half1 S34 to S37 | notebooks/C2_W04_D05_04_beating_the_baseline_good_enough_STUDENT.ipynb | c4_beat_baseline_good_enough Q2, Q3; staffing_note Q1 to Q3; kalpa_board Q3 | Q4 | 10 |

Subtopics 4 and 5 share SECTION 4 and its notebook, each with half of the chapter's 20 minutes: both
rest on one decision, that a forecast earns trust by beating the baseline on hidden periods and is
good enough when a better one would change no order. The concept block runs 95 minutes.

## The case chapters and the subtopics each applies

| Chapter | Applies (the # of each subtopic) | Slides | Notebook |
|---|---|---|---|
| SECTION 5: Trend, seasonality and baselines on Flipkart's weeks: where is the peak? | 1, 2 | half1 S38 to S48 | notebooks/C2_W04_D05_05_case_shape_and_baselines_STUDENT.ipynb |
| SECTION 6: Holding out and the vendor curve tested, on thirteen hidden weeks: which rule wins? | 2, 3, 4 | half1 S49 to S59 | notebooks/C2_W04_D05_06_case_holdout_scoreboard_STUDENT.ipynb |
| SECTION 7: The good-enough call and the staffing note, for the festive window: how many shifts? | 1, 2, 3, 5 | half2 S2 to S15 | notebooks/C2_W04_D05_07_case_good_enough_forecast_note_STUDENT.ipynb |

The TA lab applies all five on Kalpa Retail in `notebooks/C2_W04_D05_08_kalpa_lab_forecast_note_STUDENT.ipynb`.
The plan quantile, the spine's addition beyond the row, runs in the fallback deck's part 3 (fallback
S10 to S13) and notebook 07's depth section, labelled beyond the row in both.
