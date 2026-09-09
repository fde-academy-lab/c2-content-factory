# Link register: Week 1, Day 3

Internal working file. Never given to a learner.

## What is verified, and what is not

Tested on 09 September 2026. The egress proxy is selective rather than closed, which was not known
when this pack was first built.

| Domain | Result |
|---|---|
| `raw.githubusercontent.com` | Reachable. Source files can be fetched and pinned to a tag |
| `api.github.com` | Reachable |
| `pypi.org` | Reachable |
| `docs.python.org` | Blocked |
| `realpython.com` | Blocked |
| `automatetheboringstuff.com` | Blocked |
| `learnpython.com` | Blocked |
| `geeksforgeeks.org` | Blocked |
| `www.youtube.com` | Blocked |
| `www.khanacademy.org` | Blocked |
| `seeing-theory.brown.edu` | Blocked |

So a reference can ship verified today if it lives in a public git repository, and cannot otherwise.

## What that changed in this pack

The take-home's reading section no longer waits on anything. It now sends learners to
`Lib/csv.py` in the CPython source, pinned to the v3.12.0 tag, to read `Sniffer.has_header` starting
at line 390 and the vote that ends it at line 451.

That reading was chosen because it is the day's own lesson from the other side: the standard library
guesses whether row one is a header, and Wednesday's companion file is the case where guessing loses.
The last of its four questions asks when guessing is right and when stating a rule is, which is what
Thursday opens on.

That restores the fifth shortcut-resistance pattern, so the take-home now rests on five of five:
process evidence, the learner's own artifact, a named verified source with a specific thing cited
from it, a defended threshold, and the self-check spine.

## Still to be found

Every reference below comes from the curriculum row and sits on a blocked domain, so none of them
could be verified and none of them was written into an artifact. The row carries its own check dates
from early September 2026; those dates belong to the row and never to this pack.

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Real Python, csv module reference | realpython.com/ref/stdlib/csv | 03 Sep 2026 |
| GeeksforGeeks, Data Analyst interview questions | geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/ | 03 Sep 2026 |
| LearnPython, 15 Python questions for data analysts | learnpython.com/blog/python-interview-questions-for-data-analyst/ | 03 Sep 2026 |
| Automate the Boring Stuff 3e, Ch 18 | automatetheboringstuff.com/3e/ | 03 Sep 2026 |
| Khan Academy, mean, median and mode | on the Thursday row's student references | 03 Sep 2026 |

## What to do with them

Open a session on an environment with the trusted network access level, check each URL, and paste it
into its slot with the date it was checked, **on the same line as the URL**. The verification script
warns about any URL on a line without a date, so keep them together.

One student-facing slot is still open: the optional Khan Academy watch in
`C2_W01_D03_preread_STUDENT.md`. It is optional by design and the pre-read's gap sheet carries the
vocabulary without it, so this is not a release blocker. Everything else is the trainer's background
reading.
