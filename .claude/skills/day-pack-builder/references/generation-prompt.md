# The Day Pack Generation Prompt

Paste this into a new session, filling the three braces. One session per day pack: a session that already
built yesterday's pack carries yesterday's decisions and will drift.

---

Build the full day pack for Cohort 2, Week {W}, Day {D}, {date}.

Source of truth, in order: this prompt, the day's row in `docs/curriculum/W{W}_*.md`, `docs/curriculum/Structure.md`,
`docs/07_Client_Zero.md` (LOCKED v2.2), and `docs/06_Day_Pack_Method.md`. Stop and name the gap rather
than building around it if the row is missing, if the business scenario column is empty, if the dataset
version the row names is not in the locked client zero file, or if a link on the row carries no verified date.

**Read the row in the order it is written.** It opens on the business scenario in the stakeholders' words,
then the thinking trained before any tool, and only then the technique. Build the pack in that same order.

Run the gates in order and stop after gate 2 for my approval:

1. Envelope and continuity: the day's business scenario in one line, which of the three threads it advances
   (Growth, Trust, Cost and risk), what the room already knows, what today must not repeat, what comes
   later. All from the row, in one short block.
2. The spine, one screen: the scenario and the thinking it trains; the deck decision (one deck, or half one
   and half two); section list per artifact; the day's mental-model arc in one sentence; the deliberate
   failures with exact error text; the activity choice and its toggle; the take-home shape with its
   resistance patterns named; the interview questions the day equips, with their tags. Wait for my approval.
3. Build passes after approval, one artifact family per message: (a) deck or deck halves, (b) notebooks,
   (c) activity, (d) exercises with solutions, (e) take-home with its self-check spine, (f) Kahoot pack,
   (g) study notes, cheat sheet and pre-read.
4. Verification report against the skill checklist, then `python3 scripts/verify.py content/W{W}/D{D}`, then
   the file list with audience tags.

Binding rules: the business scenario is slide one and the notebook's first markdown cell, and it is never
cut; the thinking is drawn before any tool opens; mental model first and spiral always; at most four new
ideas per two-hour block; application before theory; one deliberate failure per block with exact error text;
notebooks rich and progressive (idea, diagram, demo, output, failure, fix, industry example and interview
question at milestones, one new element per section); activity toggle-driven with minimal typing; exercises
few and think-heavy with selection or repair answers; take-home shortcut-resistant with verified exploration
links and a self-check spine.

Two rules about what never reaches a learner: **nothing planted in the dataset is named in a student file**,
because the room is meant to find it; and no trainer name, mark, weight or clock time appears anywhere in a
student file. Kalpa's fictional stakeholders are named on purpose and are the exception to the names rule.
Durations only, Rs never the glyph, no em-dashes, banned-word scan before shipping.
