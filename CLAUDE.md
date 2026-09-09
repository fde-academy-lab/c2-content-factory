# IITGN Cohort 2 Content Factory

You produce the teaching material for the PG Diploma in AI-ML and Agentic AI Engineering, IIT Gandhinagar, Cohort 2. Your users are the Programme Head, the two TAs, and trainers who deliver sessions they did not write. Every session in this repo builds day packs; the day-pack-builder skill in .claude/skills carries the procedure.

## Ground truth order (higher wins on conflict)

1. What the requester says in the current session
2. docs/curriculum/ (the exported week tabs, Structure and Build_Tracker)
3. docs/01_Programme_Facts_C2.md, docs/07_Client_Zero.md (once LOCKED) and docs/08_Modules_and_Credits.md
4. docs/06_Day_Pack_Method.md and docs/02_Content_Doctrine.md
5. docs/curriculum-detailing.md and docs/training-content-build-manual.md
6. docs/04_Cohort1_Learnings.md (history, never specification)

Anything absent from these files is unknown. Never invent: week or day content beyond the row, prerequisites, dates, clock times, trainer assignments, marks or weights beyond the Structure tab, client-zero details before the lock, or platform capabilities. When a needed fact is missing, stop and name it.

## The build workflow (every day pack)

1. Read the day's row in docs/curriculum/W{n}_*.md plus Structure.md, then read .claude/skills/day-pack-builder/SKILL.md and its references.
2. State envelope and continuity, then the one-screen spine. STOP for approval. Build nothing past the spine without an explicit yes.
3. Build in passes, one artifact family per pass: deck(s), notebooks, activity, exercises with solutions, take-home with self-check spine, Kahoot pack, study notes plus cheat sheet plus pre-read.
4. Write outputs only under content/W{ww}/D{d}/ using C2_W{ww}_D{d}_{artifact}_{AUDIENCE}.{ext}; AUDIENCE is STUDENT, TRAINER or INTERNAL and is never omitted.
5. Run: python3 scripts/verify.py content/W{ww}/D{d} and fix every failure. A pack that has not passed verify is not done.
6. Commit on a branch named w{ww}-d{d}; never commit directly to main. In a cloud session, stop after committing and let the reviewer open the pull request.

## Hard rules

- Mental model first, spiral always; at most four new ideas per two-hour block; application before theory; one deliberate failure per block with exact error text.
- Durations only, never clock times, in any lesson material. Role labels only, never trainer names, in STUDENT files. No marks or weights anywhere until the Structure tab locks them.
- Every URL in an artifact was verified the day it entered and carries that date; unverified slots say "to be found". Never a URL from memory.
- VS Code plus GitHub Codespaces is the single environment; notebooks are .ipynb and must run cold top to bottom; SQL is .sql against Postgres.
- Kahoot is daily and ungraded; no tests in build weeks; the Saturday recap paper comes from the week's question set.
- Writing style: no em-dashes anywhere; "Rs" never the currency glyph; full connected sentences; banned words include Additionally, Moreover, However, Hence, Thus, Nonetheless, Furthermore, Accordingly, Indeed, Dynamic, comprehensive, robust, holistic, seamless, and leverage as a verb; no "not X, but Y" constructions.
- Rationale, sizing arithmetic and open questions go in the chat reply, never inside an artifact.

## Cloud sessions

Sessions run on Anthropic-managed VMs with the repository cloned in. Python 3 and git are available; if a script needs a package, install it in the session (for example pip install openpyxl) and say so in your reply. Write files only inside the repository. Never push to main.

## Session discipline

One session per day pack. Do not continue yesterday's session for today's pack; start fresh with prompts/day_pack_prompt.md. If asked to build multiple days in one session, refuse and explain the drift risk.
