# Exercises: Week 1, Day 3

Every exercise runs on `../data/C2_W01_D03_orders_STUDENT.csv`, the fifty Kalpa Retail orders at their dirtiest.

Answers are letters. You post one line per exercise into the chat, in the shape each file shows at the top, and that shape is written in neutral letters that are not the answers.

| Exercise | Where it sits | Items | File |
|---|---|---|---|
| G1. Guided, with the trainer: grow the profiler | `guided/` | Built live | `C2_W01_D03_grow_the_profiler_STUDENT.md` |
| E2. Mid-session, about fifteen minutes: which dataset would you trust | `unguided/` | 15 | `C2_W01_D03_which_dataset_STUDENT.md` |
| E3. Mid-session, about fifteen minutes: classify the gaps | `unguided/` | 15 | `C2_W01_D03_classify_gaps_STUDENT.md` |
| E4. Unguided, no hints: the full profile-then-clean pass | `unguided/` | A real run | `C2_W01_D03_full_pass_STUDENT.md` |

E4 is deliberately not a set of lettered items. It is the day's portfolio act: a file nobody prepared, taken to a defensible cleaned state with a log a reviewer could follow.

## The running half

| Notebook | Belongs to | Markers |
|---|---|---|
| `C2_W01_D03_ex1_hands_on_STUDENT.ipynb` | E4, the full pass | 5 |
| `C2_W01_D03_ex2_hands_on_STUDENT.ipynb` | E2, which dataset | 4 |

Run either notebook as it stands and it stops at the first placeholder with a `NameError` naming `__TODO1__`. That is the file working correctly.

## Where the files are

Your notebook sits in `notebooks/`, so the day's data is one folder up in `../data/` and anything you write goes into `output/` beside your notebook. That folder is not committed, since everything in it is reproducible from the input and the notebook.

## What to have on screen at close of session

- The profiled dataset, the rejects file and the decisions log, all three reopened from disk.
- The reconciliation: 50 in equals 44 clean plus 6 rejected, asserted rather than eyeballed.
- One decision you can defend aloud, and the name of the person who owns the one you escalated.

## Solutions

Released at the close of the session. Every solution carries the idea being tested, the answers, an item-by-item table with a why-the-others-fail column, the part worth arguing about, the hands-on picks, and where the pattern lives in production.
