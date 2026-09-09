# Pre-read and setup: after Day 4

Ships tonight. Read it tonight, do the setup line tonight, leave the rest for the weekend.

---

## What happens next, in order

```
Fri 02 Oct   Gandhi Jayanti. Institute closed. No session.
Sat 03 Oct   Recap block. Pen and paper, then the solution discussion.
Mon 05 Oct   Week 2 opens on the question today refused to answer.
```

Four teaching days done. The week ends Thursday because Friday is a gazetted national holiday.

---

## Setup you must do tonight

Nothing to install. One thing to run.

**Restart your kernel and run both of today's notebooks top to bottom, in a fresh Codespace if you can.**

```
Kernel > Restart Kernel and Run All Cells
```

Notebook 2 stops on a `KeyError` on purpose and keeps going, so a red block in that cell is the notebook working correctly. Anything else that stops is real, and finding it tonight beats finding it on Monday.

While you are there, confirm three numbers on screen:

```
orders loaded: 44
mean amount over 44 orders: Rs 12,753.30
Business 9, Retail-Core 14, Retail-Plus 11, Student 10   ->   total 44
```

If those three agree, your environment is fine for the weekend.

---

## Saturday, the recap block

Four hours, no new content. A pen-and-paper recap in short-answer form, a break, then the solution discussion led by the Academic TA with papers swapped for peer cross-evaluation and random call-outs throughout.

**Ungraded.** It carries no weight of any kind and the programme reads it as a performance indicator.

**AI-free by format**, since it is on paper.

The paper is built from the week's interview question set. The questions are already published on the Saturday row and none of them is a surprise:

- A list against a dictionary: when do you reach for each?
- `b = a`, then `b.append(9)`: what happens to `a`, and how do you copy on purpose?
- How do you read a Python traceback, and what do you look at first?
- Why is a bare `except` worse than letting the code crash?
- Everything read from a CSV is a string: what breaks, and where do you convert?
- CSV or JSON for nested records, and what does flattening cost?
- Mean or median for a money field, and why?
- Your cleaning run reported zero rejects on a file you know is dirty: what do you check?

**How to prepare.** Answer all eight out loud, to nobody, in under a minute each. Two of the eight came from today, and you should be able to answer those with the file's own numbers rather than in the abstract.

Answers that cite your own week beat answers that recite a definition. "The median, because our own file's mean was Rs 12,753 and only one order out of forty-four reached it" is a better answer than "the median, because outliers do not pull it", and it takes the same breath to say.

---

## Monday's vocabulary, as a gap sheet

Monday takes today's segment gap and asks whether it is real. Fill these in from what you can infer; you are not expected to know them yet, and having guessed wrong is the fastest way to learn the right one.

| Term | What you think it means, in your own words |
|---|---|
| Sampling variation | ____________________________________________ |
| Chance reference | ____________________________________________ |
| The null model | ____________________________________________ |
| Label shuffling | ____________________________________________ |
| The p-value | ____________________________________________ |
| Statistical against practical significance | ____________________________________________ |
| Confidence interval | ____________________________________________ |
| Confounder | ____________________________________________ |
| Correlation against causation | ____________________________________________ |
| Simpson's paradox | ____________________________________________ |

Bring the sheet on Monday with something written in every row. The session opens by correcting them, and a wrong guess you wrote down sticks better than a right answer you were handed.

---

## The one idea to arrive with

You ended today with this written in your own notebook:

> Open question: Business 11.1 percent on 9 orders against Retail-Plus 36.4 percent on 11 orders. Is that gap real?

Monday's whole session is the method for answering it, and it starts with an idea you can hold before any of the vocabulary above lands:

**If you took the same 44 orders and shuffled which segment each one belonged to, at random, you would still see gaps between the groups.** Some of those gaps would be large. So the real question is not "is there a gap", since there is always a gap. It is "is this gap bigger than the ones chance produces on its own".

Sit with that for a minute over the weekend. It is the whole session.

---

## Optional exploration

Your take-home already sends you to CPython's own `statistics` module source, which is worth reading twice (verified 09 Sep 2026): https://raw.githubusercontent.com/python/cpython/v3.12.0/Lib/statistics.py

The Week 1 row also names an interactive chapter on frequentist inference that makes the shuffle idea visual before any formula arrives: Seeing Theory, frequentist inference: https://seeing-theory.brown.edu/frequentist-inference/index.html (verified 09 September 2026)

If it has not appeared by the time you sit down, skip it. An unverified link is worth less than an honest blank, and Monday does not depend on it.

---

## Optional, for the restless

Rerun the whole week's pipeline in a fresh Codespace, Monday's orders through to today's segment summary, top to bottom, cold. Note anything that fails when nothing is in memory.

It is the single best use of the holiday, it takes about half an hour, and every learner who does it starts Week 2 without an environment problem.
