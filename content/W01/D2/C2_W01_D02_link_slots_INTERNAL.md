# Link register: Week 1, Day 2

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

The take-home's reading section no longer waits on anything. It now sends learners to two files in
the CPython source, pinned to the v3.12.0 tag so the line numbers stay put, and asks for an answer
that quotes a line number:

- `Lib/csv.py` lines 118 to 132, which is what `DictReader` does with a row that has too many or too
  few fields. Neither case raises, which is the point.
- `Lib/json/decoder.py` line 34, which is where the `line 48 column 1 (char 1027)` message this pack
  quotes is actually built.

That restores the fifth shortcut-resistance pattern, so the take-home now rests on five of five:
process evidence, the learner's own artifact, a named verified source with a specific thing cited
from it, a defended threshold, and the self-check spine.

## Still to be found

Every reference below comes from the curriculum row and sits on a blocked domain, so none of them
could be verified and none of them was written into an artifact. The row carries its own check dates
from early September 2026; those dates belong to the row and never to this pack.

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Corey Schafer, Functions | youtube.com watch 9Os0o3wzS_I | 03 Sep 2026 |
| Corey Schafer, try/except blocks | youtube.com watch NIWwJbo-9_8 | 03 Sep 2026 |
| Real Python, LBYL against EAFP | realpython.com/python-lbyl-vs-eafp/ | 03 Sep 2026 |
| Corey Schafer, CSV module | youtube.com watch q5uM4VKywbA | 03 Sep 2026 |
| Real Python, Reading and Writing CSV Files | realpython.com/python-csv/ | 03 Sep 2026 |
| Official json docs | docs.python.org/3/library/json.html | 03 Sep 2026 |
| Corey Schafer, Working with JSON data | youtube.com watch 9N6a-VLBa2I | 05 Sep 2026 |
| Automate the Boring Stuff 3e, Ch 4 and Ch 10 | automatetheboringstuff.com/3e/ | 03 Sep 2026 |
| Official Python tutorial, Errors and Exceptions | docs.python.org/3/tutorial/errors.html | 03 Sep 2026 |

## What to do with them

Open a session on an environment with the trusted network access level, check each URL, and paste it
into its slot with the date it was checked, **on the same line as the URL**. The verification script
warns about any URL on a line without a date, so keep them together.

These are the trainer's own background reading and the optional extras. No student artifact in this
pack is now blocked on any of them, so this is a nice-to-have rather than a release blocker.
