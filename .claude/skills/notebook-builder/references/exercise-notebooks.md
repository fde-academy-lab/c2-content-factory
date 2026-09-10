# Exercise notebooks: the TODO twin and its solution

An exercise notebook is where an unguided exercise stops being a reading task and becomes a run. It exists for every unguided exercise that has a notebook to point at, and its answers are letters a learner posts into chat rather than code a learner types from scratch.

## The pair

```
notebooks/C2_W{ww}_D{dd}_ex{n}_hands_on_STUDENT.ipynb     the TODO version, placeholders unfilled
exercises/solutions/C2_W{ww}_D{dd}_ex{n}_hands_on_solution_STUDENT.ipynb   every placeholder filled, executed clean
```

Both import the same helper as the teaching notebooks. Both load from `../data/`. The solution twin is the same file with the placeholders replaced, so the two never drift in structure.

## The TODO notebook, in order

**A short prelude.** Two or three sentences naming the exercise, the data it runs on, and the fact that answers are letters. Not a restatement of the exercise brief, which the learner already has.

**Four to six steps.** Each step is a markdown cell saying what the step must achieve, then a code cell holding one or more TODO markers, then a `check()` cell.

Each marker is a lettered choice written as a comment directly above a `__TODOn__` placeholder:

```python
# TODO 1. Which condition keeps only the rows whose amount could be converted?
#   a) row["amount"] != ""
#   b) row["amount"].isdigit()
#   c) converts(row["amount"])
#   d) row["amount"] is not None
usable = [row for row in raw if __TODO1__]

# TODO 2. What does the denominator have to be for a presence rate?
#   a) len(usable)
#   b) len(raw)
#   c) len(raw) - len(rejects)
#   d) 50
presence_rate = len(usable) / __TODO2__
```

The placeholder is `__TODOn__` exactly, numbered across the whole notebook rather than restarting per cell, because the answer key is one letter string in order.

**A check after every step.** The check is what tells a learner they picked right without opening the solution:

```python
c2kit.check("usable holds 44 rows", len(usable) == 44, f"got {len(usable)}")
```

A step with no check gives a learner nothing, and a learner who has to open the solution to know whether they are right has not done an unguided exercise.

**The close.** A cell listing what to post: the letter string in order, and any number the checks asked for.

## The solution twin

Every placeholder filled, executed clean from a fresh kernel, every check passing, every output saved. It carries one addition the TODO version does not have: a short markdown line under each step saying why the other three letters fail. That line is what the answer key's why-the-others-fail column is written from, so writing it here saves writing it twice.

## Rules

- Every marker has exactly four options, lettered a to d, and exactly one is right.
- The wrong options are real things a learner would plausibly write. A near-miss that is precise about the wrong grain is the best distractor available; a nonsense option teaches nothing and gives the answer away by elimination.
- The correct letter is never the longest option, and the correct letters spread across a, b, c and d rather than clustering.
- No option quotes an error message, because the point is to predict behaviour rather than recognise text.
- The notebook runs top to bottom with the placeholders in it and fails at the first `__TODO1__` with a `NameError` naming the placeholder. That is the intended behaviour, and the prelude says so in one sentence, so nobody reports it as a bug.
- `nb_check.py` skips the TODO version for the executed-output rule and applies the rule in full to the solution twin.

## Sizing

Four to six steps, one to three markers per step, so eight to fifteen markers in a notebook. Longer than that and the exercise has stopped being a check and become a build, which belongs in the unguided exercise itself rather than here.
