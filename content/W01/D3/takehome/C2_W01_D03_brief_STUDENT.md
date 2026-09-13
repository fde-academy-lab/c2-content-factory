# Take-home: a second export, and the note that goes with it

Anand's analyst sends a 97-row slice with a one-line note: "this one came through a different
route." It has defects. **They are not the same defects as the class file**, so nothing from the
session can be pasted across.

---

## Part 1. The full pass

Open `notebooks/C2_W01_D03_hands_on_STUDENT.ipynb`. Profile, name every defect, decide, record,
reconcile. Fill every `__TODO__` and post the five letters.

**Four kinds of defect are in that file and one of them does not appear in the class file at all.**
One of the four converts cleanly and raises no error, which is why profiling comes before deciding.

**One row is not a defect.** It will look like one. Deciding correctly about it, and writing down
why, is worth more than the other four put together.

---

## Part 2. The note to Finance, four sentences

Write it as if Anand's analyst will read it before they read your code, because they will.

| Sentence | What it carries |
|---|---|
| 1 | What arrived: rows, distinct orders, and the one-line summary of what is wrong |
| 2 | What you rejected and why, with counts |
| 3 | The number you would sign |
| 4 | The one thing you had to use judgment on, stated as a judgment |

Under 120 words. Numbers first.

**Sentence four is the one being marked.** A note with no judgment in it is a note from somebody who
has not looked hard enough, and a note whose judgment is hidden inside sentence two is a note that
will be found out later.

---

## Part 3. The decisions log

A table, one row per decision, with these columns:

| Field | Issue | Rows | Decision | Reason |
|---|---|---|---|---|

Five rows at most. Two rules:

1. **A reason that restates the issue is not a reason.** "It was a duplicate so I removed it" says
   nothing. "Every field on the pair is identical and the export note says the migration re-ran"
   says something.
2. **The log must include a row you kept.** Anything you looked at and decided to leave in belongs
   here too, because that is the row an auditor asks about.

---

## Part 4. One paragraph, and this is the interview question

> Your dashboard and Finance disagree by Rs 20 lakh. Walk me through what you do, in order, and tell
> me what you would refuse to do.

Under 150 words. The second half is the part people fail.

---

## What makes this hard to shortcut

The four defects in the second export are not the four in the class file, and one of them produces
no error at all. An assistant handed the brief alone will write a pass for the defects it was told
about in the session.

The second tell is Part 3's kept row. A log with only rejections is a log from a pass that never
made a judgment, and a pass that never made a judgment did not look at the data.

---

## Reading, tonight

- Real Python, Reading and Writing CSV Files, the `DictReader` section (verified 03 Sep 2026):
  https://realpython.com/python-csv/
- Python's `json` docs, on `JSONDecodeError` (verified 03 Sep 2026):
  https://docs.python.org/3/library/json.html

---

## What to bring tomorrow

| | |
|---|---|
| The notebook | Filled, checks passing, five letters posted |
| The note | Four sentences, under 120 words |
| The decisions log | Five rows at most, including one you kept |
| The paragraph | Under 150 words, with the refusal in it |

Tomorrow Meera asks whether the gap you have left is real at all, or whether it is the kind of
difference that shows up between any two quarters. Arriving with clean numbers is what makes that
question answerable.
