# Take-home: rebuild it from a fresh export, and write the rule

## The situation

Monday's deck goes to Meera's office. Between now and then, the warehouse will have been
refreshed at least once.

Tonight you find out whether your three deliverables survive that.

## Part one: rebuild

Regenerate both exports and rebuild your three deliverables from scratch.

```bash
python3 data/generate_client_zero.py --version v4 --out content/W02/D1/data --stem C2_W02_D01
bash .devcontainer/load_warehouse.sh
```

Then rebuild. For each of the three, record one line:

```
Deliverable:   the pivot / the protect list / the front-page number
Before:        the figure it showed this afternoon
After:         the figure it shows now
Same or not:   and if not, why not
```

If a number moved, find out why before you write the line. "The data changed" is not a reason; it
is a restatement.

If nothing moved at all, say how you know your rebuild actually used the new export rather than a
cached file. Somebody in the room will have rebuilt nothing and reported no change.

## Part two: the operating rule

One page. Four lines and nothing else.

Three lines saying what the warehouse, pandas and Excel each own, in your words rather than in the
deck's.

Then the fourth line, which is the condition, and one sentence underneath it naming what breaks it
first in real teams.

## Part three: one honest paragraph

Somewhere in this week you produced a number you would not have caught if the room had not been
looking. Write four sentences: which one, how it would have reached somebody, what caught it, and
what you will do differently in Build 1 next week.

This is not a confession exercise. Build 1 opens Monday in Kalpa Health with unfamiliar data and
no trainer at your shoulder, and the habit you name here is the one you will need on Tuesday.

## The self-check

`C2_W02_D05_selfcheck_STUDENT.md`.

## Why the rebuild

The whole week has been about whether a number can be produced again by somebody else. A sheet
that cannot be rebuilt has become a source of truth and nobody decided that.
