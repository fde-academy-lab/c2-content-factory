# Link register: Week 1, Day 1

Internal working file. Never given to a learner and never merged into a student artifact.

## What is settled, and what is not

The data in this pack is settled. Client zero locked at v1.0 on 09 September 2026 and the thirty
orders here are generated from `data/generate_client_zero.py` at the `w1d1` version, so nothing about
the dataset is pending any more. See the provenance file in this folder.

The links are still open, for the reason below.

## Why every link in this pack says "to be found"

The build session had no outbound network access. The egress proxy answered 403 to CONNECT for every reference domain on the curriculum row, tested and confirmed in this session:

| Domain | Result |
|---|---|
| `docs.github.com` | blocked by the egress proxy |
| `code.visualstudio.com` | blocked by the egress proxy |
| `www.youtube.com` | blocked by the egress proxy |
| `automatetheboringstuff.com` | blocked by the egress proxy |
| `www.geeksforgeeks.org` | blocked by the egress proxy |
| `docs.python.org` | blocked by the egress proxy |

The standing rule is that a URL enters an artifact only if it was verified on the day it entered, and a link from memory never ships. No link could be verified, so no link was written. Every reference in this pack is a named slot instead.

## What to do

Open a session on an environment with the trusted network access level, check each URL below, and paste it into the named slot with the date it was checked, on the same line as the URL. The verification script warns about any URL on a line without a date, so keep them together.

Sources below are copied from the Week 1 Day 1 curriculum row, which dates every one of its resources 03 September 2026. That date belongs to the row, never to this pack.

## Trainer resources to verify

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| GitHub Docs, Codespaces with Jupyter quickstart | docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning | 03 Sep 2026 |
| VS Code docs, notebooks on the web and in Codespaces | code.visualstudio.com/docs/datascience/notebooks-web | 03 Sep 2026 |
| Corey Schafer, Python beginner playlist, videos 1 to 7 | youtube.com playlist PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7 | 03 Sep 2026 |
| Automate the Boring Stuff 3e, Ch 1 to 3 | automatetheboringstuff.com/3e/ | 03 Sep 2026 |
| GeeksforGeeks, Python interview questions | geeksforgeeks.org/python/python-interview-questions/ | 03 Sep 2026 |

The same pass should also read the VS Code notebooks page listed above to confirm where the Restart control sits on the screen, because no file in this pack may name its position until that has been checked.

## Student references to verify

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Corey Schafer, Lists, Tuples and Sets | youtube.com watch W8KRzm-HUcc | 03 Sep 2026 |
| Corey Schafer, Dictionaries | youtube.com watch daefaLgNkw0 | 03 Sep 2026 |
| Automate the Boring Stuff 3e, Ch 2 and Ch 3 | automatetheboringstuff.com/3e/ | 03 Sep 2026 |

## The slots waiting for them

| File | Where |
|---|---|
| `C2_W01_D01_takehome_STUDENT.md` | The watch task, Corey Schafer's dictionaries video |
| `C2_W01_D01_preread_STUDENT.md` | The watch task, the same video |
| `C2_W01_D01_deck_00_intro_STUDENT.md` | Slide S24, "Before tomorrow", the same video |
| `C2_W01_D01_day_sheet_TRAINER.md` | The "What ships tonight" section, where the trainer names the watch item at the close |

One source is named inside a student artifact today, which is the dictionaries video the row sets as tomorrow's watch task, so it holds all four slots. The other seven references are trainer preparation and optional student reading, and they are listed above so that one verification pass covers the whole day.

The take-home currently rests on four shortcut-resistance patterns out of five. The fifth pattern, requiring a learner to read a named verified source and cite one specific thing found there, is the one waiting on these links. Adding it is a short edit to the take-home once a URL is verified.
