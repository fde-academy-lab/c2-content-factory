# Link register: Week 1, Day 4

Internal working file. Never given to a learner and never merged into a student artifact.

## Why every link in this pack says "to be found"

The build session had no outbound network access. The egress proxy answered 403 to CONNECT on every reference domain on the curriculum row, tested and confirmed in this session:

| Domain | Result |
|---|---|
| `www.khanacademy.org` | 403 at the proxy, policy denial |
| `seeing-theory.brown.edu` | 403 at the proxy, policy denial |
| `en.wikipedia.org` | 403 at the proxy, policy denial |
| `docs.python.org` | 403 at the proxy, policy denial |

The standing rule is that a URL enters an artifact only if it was verified on the day it entered, and a link from memory never ships. No link could be verified, so no link was written.

## What to do

Open a session on an environment with the trusted network access level, check each URL below, and paste it into the named slot with the date it was checked, **on the same line as the URL**. The verification script warns about any URL on a line without a date, so keep them together.

Sources below are copied from the Week 1 Day 4 curriculum row, which carries its own verification dates from early September 2026. Those dates belong to the row and never to this pack.

## Trainer resources to verify

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Khan Academy, mean, median and mode, video | khanacademy.org, statistics-probability, mean-median-basics, video | 03 Sep 2026 |
| Khan Academy, mean, median and mode review with worked values | khanacademy.org, same unit, review article | 03 Sep 2026 |
| Khan Academy, summarizing quantitative data unit | khanacademy.org, summarizing-quantitative-data | 03 Sep 2026 |

## Student references to verify

| Reference | Row's URL | Row's stated check date |
|---|---|---|
| Khan Academy, summarizing quantitative data unit with practice items | khanacademy.org, summarizing-quantitative-data | 03 Sep 2026 |
| Seeing Theory, frequentist inference chapter, interactive preview for Monday | seeing-theory.brown.edu, frequentist-inference | 05 Sep 2026 |

## The slots waiting for them

| File | Where | What it is holding up |
|---|---|---|
| `C2_W01_D04_takehome_STUDENT.md` | The "Exploration, before Monday" section | The fifth shortcut-resistance pattern |
| `C2_W01_D04_preread_STUDENT.md` | The "Optional exploration" section | Nothing blocking; Monday does not depend on it |

## The cost, stated plainly

The take-home currently rests on **four** shortcut-resistance patterns out of five:

1. It runs on the learner's own `summarise_by` function from today, which no assistant has seen.
2. The answer is a defended threshold with a number in it rather than paddable prose.
3. The challenges log requires pasted output text, and paraphrases are explicitly refused.
4. The self-check spine plants seven exact values on a file no assistant has seen.

The missing fifth is the one that requires reading a named verified source and citing one specific thing found there. Both the take-home and the pre-read tell the learner to skip that section and say so in the challenges log if the link has not appeared, rather than substituting a source they found themselves. Adding the pattern back is a two-line edit to the take-home once the Seeing Theory URL is verified.

The Khan Academy links are the row's own trainer and student references and are not load-bearing for any artifact in this pack; the day teaches from the file's own numbers throughout.
