# Day Pack Generation Prompt
Paste into a new chat in this project. Fill the three braces.

---

Build the full day pack for Cohort 2, Week {W}, Day {D}, {date}.

Source of truth, in order: this prompt, the W{W} tab row for this day in the curriculum workbook, the Structure tab, and 06_Day_Pack_Method.md. If the row is missing, the client-zero lock is needed and absent, or a link on the row is unverified, stop and name the gap instead of building around it.

Run the gates in order and stop after gate 2 for my approval:

0. Source lock: one written reference and one video per new topic, the product's own documentation for any tool used for the first time, and every movable fact verified with the date it was checked. Links I supply are the lock rather than a starting point. Where a fact cannot be verified in the session, write "not verified" rather than a guess. List the locked sources with their dates before gate 1.
1. Envelope and continuity: what the room already knows, what today must not repeat, what comes later, all from the row, in one short block.
2. The spine, one screen: the deck decision (one deck, or half one and half two), section list per artifact, the day's mental-model arc in one sentence, the deliberate failures with exact error text, the activity choice and its toggle, the take-home shape with its resistance patterns named. Wait for my approval.
3. Build passes after approval, one artifact family per message: (a) deck or deck halves, (b) notebooks, (c) activity, (d) exercises with solutions, (e) take-home with its self-check spine, (f) Kahoot pack, (g) study notes, cheat sheet and pre-read.
4. Verification report against the method's checklist, then the file list with audience tags.

Write every file under content/W{WW}/D{D}/ inside the subfolder its type belongs in, named C2_W{WW}_D{DD}_{topic}_{AUDIENCE}.{ext}. Read content/README.md for the folder set before pass 1. Run python3 scripts/verify.py content/W{WW}/D{D} --execute and fix every failure. That one command carries every proof: nb_check for saved outputs, rendered diagrams and passing checks; distractor_audit for the option sets; xlsx_recalc for the workbook's verdicts under a flipped decision; html_sweep for every control on every demo page; deck_md_check for the slide source; and deck_check for a .pptx only once one has been freshly built from that markdown. A proof that reports it could not run in this session is not a pass, so say which ones ran. Commit on branch w{WW}-d{DD}.

Binding rules: mental model first and spiral always (everyday anchor, whole pipeline shallow, deep stops only where the row says); at most four new ideas per two-hour block; application before theory; one deliberate failure per block with exact error text; notebooks rich and progressive (idea, diagram, demo, output, failure, fix, industry example and interview question at milestones, one new element per section); activity toggle-driven with minimal typing; exercises few and think-heavy with selection or repair answers; take-home shortcut-resistant with verified exploration links and a self-check spine; durations only, role labels only, Rs never the glyph, no em-dashes, banned-word scan before shipping.
