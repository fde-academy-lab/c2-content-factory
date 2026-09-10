# Exercises: Week 1, Day 1

Every exercise runs on the same thirty Kalpa Retail orders in `../data/`, the ones the demo notebooks read.

Answers are letters. You post one line per exercise into the chat, in the shape each file shows at the top, and the shape is written in neutral letters that are not the answers. The thinking is the work and the writing takes a moment.

| Exercise | Where it sits | Items | File |
|---|---|---|---|
| G1. Guided, with the trainer: the threshold count | `guided/` | Built live | `C2_W01_D01_threshold_count_STUDENT.md` |
| E2. Mid-session, about fifteen minutes: predict the output | `unguided/` | 15 | `C2_W01_D01_predict_output_STUDENT.md` |
| E3. Mid-session, about fifteen minutes: find the mistake | `unguided/` | 15 | `C2_W01_D01_find_the_mistake_STUDENT.md` |
| E4. Unguided, no hints: the three questions | `unguided/` | 15 plus the build | `C2_W01_D01_three_questions_STUDENT.md` |

## The running half

Two of these have a hands-on notebook beside them in `notebooks/`, where every decision is a lettered choice above a `__TODOn__` placeholder and a check after each step tells you whether it landed.

| Notebook | Belongs to | Markers |
|---|---|---|
| `C2_W01_D01_ex1_hands_on_STUDENT.ipynb` | E4, the three questions | 5 |
| `C2_W01_D01_ex2_hands_on_STUDENT.ipynb` | E3, find the mistake | 4 |

Run either notebook as it stands and it stops at the first placeholder with a `NameError` naming `__TODO1__`. That is the file working correctly, so do not report it as a bug.

## Where the files are

Your notebook sits in `notebooks/`, so the day's data is one folder up in `../data/` and anything you write goes into `output/` beside your notebook.

## What to have on screen at close of session

- Your three answers from E4, each a count and a total, each said in a sentence that names its group.
- The repaired loop from E3, printing Rs 25,720.
- Your fifteen letters for each of E2, E3 and E4, and the notebook letters beside them.

## Solutions

Released at the close of the session. Every solution carries the idea being tested, the answers, an item-by-item table with a why-the-others-fail column, the part worth arguing about, the hands-on picks, and where the pattern lives in production. The executed hands-on twins sit in `solutions/` with every placeholder filled and every check passing.
