# Link register: Week 1, Day 1

Internal working file. Never given to a learner and never merged into a student artifact.

## What is verified, and what is not

Retested on 09 September 2026 against the merged state of main. The egress proxy is selective
rather than closed, which was not known when this pack was first built.

| Domain | Result |
|---|---|
| `raw.githubusercontent.com` | Reachable. Source files can be fetched and pinned to a tag |
| `api.github.com` | Reachable |
| `pypi.org` | Reachable |
| `docs.github.com` | Blocked |
| `code.visualstudio.com` | Blocked |
| `docs.python.org` | Blocked |
| `automatetheboringstuff.com` | Blocked |
| `www.youtube.com` | Blocked |

So a reference can ship verified today if it lives in a public git repository, and cannot otherwise.

## What that changed in this pack

The take-home's reading section no longer waits on anything. Section 6 sends learners to two files in
the CPython source, pinned to the v3.12.0 tag so the line numbers stay put, and asks for an answer
that quotes a line number:

- `Objects/object.c`, where the message `'>' not supported between instances of 'str' and 'int'` is
  built. The format string sits at line 822 of the v3.12.0 file, checked on 09 September 2026, and
  the brief does not name the line because finding it is the task.
- `Objects/dictobject.c`, where `dict.get` is implemented. The clinic block begins at line 3258 and
  `dict_get_impl` at line 3268, both checked on 09 September 2026.

That restores the fifth shortcut-resistance pattern, so the take-home now rests on five of five:
process evidence, the learner's own artifact, a named verified source with a specific thing cited
from it, a defended threshold, and the self-check spine.

## Still to be found

Every reference below comes from the Monday curriculum row and sits on a blocked domain, so none of
them could be verified and none of them was written into an artifact. The row carries its own check
dates from early September 2026; those dates belong to the row and never to this pack.

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| GitHub Docs, Codespaces with Jupyter quickstart | docs.github.com codespaces getting-started-with-github-codespaces-for-machine-learning | 03 Sep 2026 |
| VS Code docs, notebooks on the web and in Codespaces | code.visualstudio.com/docs/datascience/notebooks-web | 03 Sep 2026 |
| Corey Schafer, Python beginner playlist | youtube.com playlist PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 | 03 Sep 2026 |
| Automate the Boring Stuff 3e, Ch 1 to 3 | automatetheboringstuff.com/3e/ | 03 Sep 2026 |
| GeeksforGeeks, Python interview questions | geeksforgeeks.org/python/python-interview-questions/ | 03 Sep 2026 |
| Corey Schafer, Lists, Tuples and Sets | youtube.com watch W8KRzm-HUcc | 03 Sep 2026 |
| Corey Schafer, Dictionaries | youtube.com watch daefaLgNkw0 | 03 Sep 2026 |

## The slots waiting for them

| File | Where |
|---|---|
| `C2_W01_D01_takehome_STUDENT.md` | The watch task, Corey Schafer's dictionaries video |
| `C2_W01_D01_preread_STUDENT.md` | The watch item, the same video |
| `C2_W01_D01_deck_00_intro_STUDENT.md` | The closing slide, the same video |

## What to do with them

Open a session on an environment with the trusted network access level, check each URL, and paste it
into its slot with the date it was checked, on the same line as the URL. The verification script
warns about any URL on a line without a date, so keep them together.

These are the trainer's own background reading and one optional video. No student artifact in this
pack is now blocked on any of them, so this is a nice-to-have rather than a release blocker.
