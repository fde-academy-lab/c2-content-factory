# Issue tracker: local markdown

Issues and specs for this repository live as markdown files in `.scratch/`. There is a GitHub remote, and GitHub Issues are deliberately not the tracker here, so a skill that wants to file or read work goes to `.scratch/` and never to `gh issue`.

Files under `.scratch/` are committed rather than ignored. Cloud sessions run on managed VMs whose containers are reclaimed after the session ends, so an uncommitted tracker would not survive the session that wrote it.

## Conventions

- One feature per directory: `.scratch/<feature-slug>/`
- The spec is `.scratch/<feature-slug>/spec.md`
- Implementation issues are one file per ticket at `.scratch/<feature-slug>/issues/<NN>-<slug>.md`, numbered from `01`, never a single combined tickets file
- Triage state is recorded as a `Status:` line near the top of each issue file, using the role strings in `triage-labels.md`
- Comments and conversation history append to the bottom of the file under a `## Comments` heading

## When a skill says "publish to the issue tracker"

Create a new file under `.scratch/<feature-slug>/`, creating the directory if it does not exist.

## When a skill says "fetch the relevant ticket"

Read the file at the referenced path. The requester will normally pass the path or the issue number directly.

## Wayfinding operations

Used by `/wayfinder`. The map is a file with one child file per ticket.

- Map: `.scratch/<effort>/map.md`, carrying the Notes, Decisions-so-far and Fog body.
- Child ticket: `.scratch/<effort>/issues/NN-<slug>.md`, numbered from `01`, with the question in the body. A `Type:` line records the ticket type, which is one of `research`, `prototype`, `grilling` or `task`, and a `Status:` line records `claimed` or `resolved`.
- Blocking: a `Blocked by: NN, NN` line near the top. A ticket is unblocked when every file it lists is `resolved`.
- Frontier: scan `.scratch/<effort>/issues/` for files that are open, unblocked and unclaimed, and the first by number wins.
- Claim: set `Status: claimed` and save before any work.
- Resolve: append the answer under an `## Answer` heading, set `Status: resolved`, then append a context pointer, meaning the gist and the link, to the Decisions-so-far section of `map.md`.

## What this does not cover

Day packs are not tracked here. They follow the build workflow in `CLAUDE.md`, one session per pack, on a `w{ww}-d{d}` branch.
