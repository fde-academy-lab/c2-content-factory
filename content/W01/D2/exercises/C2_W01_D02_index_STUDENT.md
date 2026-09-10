# Exercises: Week 1, Day 2

Every exercise runs on the Kalpa Retail files in `../data/`, the same ones the demo notebooks read.

Answers are letters. You post one line per exercise into the chat, in the shape each file shows at the top, and that shape is written in neutral letters that are not the answers.

| Exercise | Where it sits | Items | File |
|---|---|---|---|
| G1. Guided, with the trainer: carve normalise_amount | `guided/` | Built live | `C2_W01_D02_carve_normalise_STUDENT.md` |
| E2. Mid-session, about fifteen minutes: trace the calls | `unguided/` | 15 | `C2_W01_D02_trace_calls_STUDENT.md` |
| E3. Mid-session, about fifteen minutes: the truncated feed | `unguided/` | 15 | `C2_W01_D02_truncated_feed_STUDENT.md` |
| E4. Unguided, AI-free lab: read, clean, write | `unguided/` | A real run | `C2_W01_D02_ai_free_lab_STUDENT.md` |

The AI-free lab is deliberately not a set of lettered items. Its whole value is that you meet a defective file cold, with nobody and nothing helping, and produce two real output files from it. Do not paste it into an assistant; the file it names has never been seen by one.

## The running half

| Notebook | Belongs to | Markers |
|---|---|---|
| `C2_W01_D02_ex1_hands_on_STUDENT.ipynb` | E2, trace the calls | 4 |
| `C2_W01_D02_ex2_hands_on_STUDENT.ipynb` | E3, the truncated feed | 4 |

Run either notebook as it stands and it stops at the first placeholder with a `NameError` naming `__TODO1__`. That is the file working correctly.

## Where the files are

Your notebook sits in `notebooks/`, so the day's data is one folder up in `../data/` and anything you write goes into `output/` beside your notebook. That folder is not committed, since everything in it is reproducible from the input and the notebook.

## What to have on screen at close of session

- `clean.csv` and `rejects.csv` from the AI-free lab, both reopened and both parsing.
- The reconciliation line: input equals clean plus rejected, asserted rather than eyeballed.
- Your fifteen letters for each of E2 and E3, with the notebook letters beside them.

## Solutions

Released at the close of the session. Every solution carries the idea being tested, the answers, an item-by-item table with a why-the-others-fail column, the part worth arguing about, the hands-on picks, and where the pattern lives in production.
