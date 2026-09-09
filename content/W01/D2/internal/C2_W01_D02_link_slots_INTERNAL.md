# Link register: Week 1, Day 2

Internal working file. Never given to a learner and never merged into a student artifact.

## What is settled, and what is not

The data in this pack is settled. Client zero locked at v1.0 on 09 September 2026 and every data
file here is regenerated from `data/generate_client_zero.py`, so nothing about the dataset is
pending any more. See the provenance file in this folder.

The links are still open, for the reason below.

## Why every link in this pack says "to be found"

The build session had no outbound network access. The egress proxy refused every reference domain on the curriculum row, tested and confirmed:

| Domain | Result |
|---|---|
| `realpython.com` | blocked by the egress proxy |
| `docs.python.org` | blocked by the egress proxy |
| `automatetheboringstuff.com` | blocked by the egress proxy |
| `www.youtube.com` | blocked by the egress proxy |

The standing rule is that a URL enters an artifact only if it was verified on the day it entered, and a link from memory never ships. No link could be verified, so no link was written. Every reference in this pack is a named slot instead.

## What to do

Open a session on an environment with the trusted network access level, check each URL below, and paste it into the named slot with the date it was checked, on the same line as the URL. The verification script warns about any URL on a line without a date, so keep them together.

Sources below are copied from the Week 1 Day 2 curriculum row, which carries its own verification dates from early September 2026. Those dates belong to the row, never to this pack.

## Trainer resources to verify

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Corey Schafer, Functions | youtube.com watch 9Os0o3wzS_I | 03 Sep 2026 |
| Corey Schafer, try/except blocks | youtube.com watch NIWwJbo-9_8 | 03 Sep 2026 |
| Real Python, LBYL against EAFP | realpython.com/python-lbyl-vs-eafp/ | 03 Sep 2026 |
| Corey Schafer, CSV module | youtube.com watch q5uM4VKywbA | 03 Sep 2026 |
| Real Python, Reading and Writing CSV Files | realpython.com/python-csv/ | 03 Sep 2026 |
| Official json docs | docs.python.org/3/library/json.html | 03 Sep 2026 |

## Student references to verify

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Corey Schafer, Working with JSON data | youtube.com watch 9N6a-VLBa2I | 05 Sep 2026 |
| Automate the Boring Stuff 3e, Ch 4 and Ch 10 | automatetheboringstuff.com/3e/ | 03 Sep 2026 |
| Official Python tutorial, Errors and Exceptions | docs.python.org/3/tutorial/errors.html | 03 Sep 2026 |

## The slots waiting for them

| File | Where |
|---|---|
| `takehome/C2_W01_D02_brief_STUDENT.md` | The reading section, Automate the Boring Stuff chapter 10 |
| `preread/C2_W01_D02_preread_STUDENT.md` | Optional reading, same chapter |

The take-home currently rests on four shortcut-resistance patterns out of five. The fifth pattern, requiring a learner to read a named verified source and cite one specific thing found there, is the one waiting on these links. Adding it is a two-line edit to the take-home once the URLs are verified.
