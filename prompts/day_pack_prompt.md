# The day pack prompt

One session per day pack. Start fresh: a session that already built yesterday's pack carries yesterday's
decisions and will drift into today's without anybody choosing that.

---

Build the full day pack for Cohort 2, Week {W}, Day {D}, {date}.

Source of truth, in order: this prompt, the day's row in `docs/curriculum/W{W}_*.md`,
`docs/curriculum/Structure.md`, `docs/07_Client_Zero.md` (LOCKED v2.2) and `docs/06_Day_Pack_Method.md`.
Stop and name the gap rather than building around it if the row is missing, if the business scenario
column is empty, if the dataset version the row names is not described in the locked client zero file, or
if a link on the row carries no verified date.

**Read the row in the order it is written.** Fifteen columns, opening on the business scenario in the
stakeholders' words, then the thinking trained before any tool, and only then the technique. Build the
pack in that same order. `docs/05_Curriculum_Map_Schema.md` says what each column carries.

Run the gates in order and stop after gate 2 for my approval.

0. **Source lock.** One written reference and one video per new topic, the product's own documentation for
   any tool used for the first time, and every movable fact verified with the date it was checked. Links I
   supply are the lock rather than a starting point. Where a fact cannot be verified in the session, write
   "not verified" rather than a guess. List the locked sources with their dates before gate 1.
1. **Envelope and continuity.** The day's business scenario in one line, which of the three threads it
   advances (Growth, Trust, Cost and risk), what the room already knows, what today must not repeat, what
   comes later. All from the row, in one short block.
2. **The spine, one screen.** The scenario and the thinking it trains; the deck decision (one deck, or half
   one and half two); the section list per artifact; the day's mental-model arc in one sentence; the
   deliberate failures with their exact error text; the activity choice and its toggle; the take-home shape
   with its resistance patterns named; the interview questions the day equips, with their tags. Wait for my
   approval. Build nothing past this without an explicit yes.
3. **Build passes**, one artifact family per message: (a) deck or deck halves, (b) notebooks, (c) activity,
   (d) exercises with solutions, (e) take-home with its self-check spine, (f) Kahoot pack, (g) study notes,
   cheat sheet and pre-read.
4. **Verification.** The skill checklist, then `python3 scripts/verify.py content/W{W}/D{D}`, then the file
   list with audience tags. Report what failed and what you fixed.
5. **Commit** on branch `w{ww}-d{d}`. In a cloud session, stop after committing and let the reviewer open
   the pull request.

Binding rules: the business scenario is slide one and the notebook's first markdown cell, and it is never
cut; the thinking is drawn before any tool opens; mental model first and spiral always; at most four new
ideas per two-hour block; application before theory; one deliberate failure per block with exact error
text; notebooks rich, progressive and shipped executed; the activity toggle-driven with minimal typing;
exercises few and think-heavy with selection or repair answers; the take-home shortcut-resistant with
verified exploration links and a self-check spine.

Two rules about what never reaches a learner. **Nothing planted in the dataset is named in a student
file**, because the room is meant to find it. And no trainer name, mark, weight or clock time appears
anywhere in a student file; Kalpa's fictional stakeholders are named on purpose and are the one exception
to the names rule. Durations only, Rs never the glyph, no em-dashes, banned-word scan before shipping.
