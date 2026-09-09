# C2 Content Factory

The build repository for IITGN Cohort 2 teaching material. One day of training equals one day pack, built by Claude Code from the curriculum row, gated by a spine approval and a verification script.

## Setup

Browser only, no local install: follow `SETUP.md`, then use the copy-paste prompts in `prompts/web_prompts.md` at https://claude.ai/code.

Working from a terminal instead: install Claude Code (`npm install -g @anthropic-ai/claude-code`, docs at https://docs.claude.com/en/docs/claude-code/overview), clone the repository, run `claude` at its root, and use the same prompts.

## Building one day pack

1. Start a fresh session with this repository selected. One session per day pack, always.
2. Paste the matching prompt from `prompts/web_prompts.md`.
3. Claude stops at the spine. The reviewer approves it in the session; building continues only on an explicit yes.
4. After the passes finish, the session runs `python3 scripts/verify.py content/W{ww}/D{d}` (or `content/W{ww}/SAT`) and fixes every failure.
5. The session commits on branch `w{ww}-d{d}`, or `w{ww}-sat` for a Saturday. Open the diff, create the pull request, review, merge, then move the day's tracker row to Reviewed and then Locked.

## Updating the curriculum

The workbook `docs/curriculum/source.xlsx` is the source. Upload the new workbook, then run Prompt 6 so the markdown exports match it again.

## What lives where

- `CLAUDE.md`: the rules every session loads.
- `docs/`: ground truth (programme facts, doctrine, method, learnings, the plan).
- `docs/curriculum/`: the workbook and its per-tab markdown exports.
- `.claude/skills/day-pack-builder/`: the build procedure Claude follows, installed from `bootstrap/` by Prompt 1.
- `prompts/web_prompts.md`: the copy-paste prompts, one per task.
- `prompts/day_pack_prompt.md`: the same build prompt in generic form.
- `scripts/`: the exporter and the verification gate.
- `content/W{ww}/D{d}/` and `content/W{ww}/SAT/`: the shipped artifacts, filed by subfolder and audience-tagged. `content/README.md` carries the layout and `content/_TEMPLATE/` the empty shapes.
