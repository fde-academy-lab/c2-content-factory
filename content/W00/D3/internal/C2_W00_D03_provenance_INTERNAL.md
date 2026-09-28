# Provenance: Week 0, Wednesday

INTERNAL.

## What the pack was built from

The Wednesday row of `docs/curriculum/W0_Baseline_week.md` (tracker v7, 21 September 2026) for the
brush-up's content: two tracks set from Tuesday's diagnostic, the taught track's list (types, lists and
dictionaries, loops and accumulators, functions that return, reading a traceback), the practice
track, and the one-to-ones on the baseline card. The student Week 0 sheet, `docs/journey/Week_0.md`
(version 2, 27 September 2026), for the running order: the brush-up's part one in the first half
and the introductions, four minutes each, in the second. The tracker's Saturday row supplied the
project talks' interview questions and the one-to-one guide it lists as still to build, since the
talks moved to Wednesday with the student sheet. The spine was approved in session on 28 September
2026, with one decision from the requester: the make-up runs first thing.

## Checked on 28 September 2026

| Source | What it settled |
|---|---|
| The Python tutorial, chapters 3, 4, 5 and 8, at docs.python.org (documentation version 3.14.7) | The written reference for each idea, and the sentence the deck quotes: "The last line of the error message indicates what happened." |
| Corey Schafer's Python beginner playlist, the row's own video reference | Live, with videos 2 and 3 on types, 4 and 5 on lists and dictionaries, 7 on loops and 8 on functions |
| Python 3.11.15, run in session | The deck's and the exercise's printed outputs, and the failure text `TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'` |
| `jupyter nbconvert`, from each notebook's own folder | The demo and the solution twin execute cold with every check passing; the TODO twin stops at `__TODO1__` with a `NameError` |
| mermaid-cli 11.17.0, through the deck and cheat sheet builders | Every diagram renders; `-s` is its scale option and defaults to 1 |

No video on reading a traceback is locked. Real Python's traceback guide refused the session's
requests, so it was not verified and is not cited.

## Conflicts, and what the pack did

- **The running order.** The tracker runs the warden's framing class and a practice lab in the second
  half; the student sheet gives the second half to the introductions and puts a one-hour class on
  stating a problem on Thursday. The pack follows the student sheet, and the warden's class, its
  Kahoot and its three interview questions move to Thursday's pack.
- **The one-to-ones.** The tracker says fifteen minutes each; the student sheet, which learners have
  read, says ten. The guide runs ten.
- **The practice platform.** The row's after-class task names CodeChef, which `data/programme/facts.yaml`
  holds as an open decision, so no file names a platform.
- **Files for learners.** The course's own repository is not open to learners yet, so the room codes
  along in a blank notebook and the printed exercise and hands-on pages carry the tasks.

## Protected for Week 1

Week 1 plants four moments the brush-up must not spend: the amount stored as text and the bulk order
that splits the mean from the median (Monday), the missing field fixed with `.get()` and a default
(Tuesday), and the file errors (Wednesday). The brush-up's two logs carry none of them, its
dictionary totals start with `if key not in`, and its deliberate failures are a helper that prints
and a loop that reaches one position too far.

## Own constructions

The librarian's scenario and both logs (the class log is the table the pack's retired SQL paper
used); the section timings
of the taught track; the exercise's twelve items and the hands-on notebook's twelve markers; the
one-to-one guide's ten-minute split and its three rules; the introductions' opening, clock, break and
capture sheet; the models of a weak and a strong project story; and the cheat sheet.

## Changed in the Tuesday pack

The baseline card gained a "by when" line under each action, since the tracker's Saturday row asks for
actions with dates. The Tuesday day sheet, pre-read and provenance now say the make-up runs first
thing on Wednesday.

## Changed when the requester's diagnostic replaced the pack's

On 28 September 2026 the requester's diagnostic replaced the pack's four papers. The tracks now come
from the key workbook's Python brush-up call, with a full call joining the taught track and a light
call the practice track. The make-up is the diagnostic itself, about 90 minutes. The one-to-one reads
the learner's report email and Profile line, and the day sheet maps the diagnostic's Python items to
the taught track's sections. The deck, the notebook, the exercise and the data file no longer point
to a Tuesday paper.

## Found outside the pack

`scripts/build_deck.py` rendered each diagram with `mmdc -w 2600` and no `-s`, so every slide picture
in every deck was drawn at one pixel per CSS pixel and then stretched to fill the slide, at 27 to 127
pixels to the inch and 56 at the median. The shared builder now renders each picture for the width
it is drawn at, at 288 pixels to the inch, and the Wednesday decks were rebuilt with every other
deck on 28 September 2026.
