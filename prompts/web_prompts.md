# Copy-paste prompts for Claude Code on the web

One task per prompt. Start each from claude.ai/code with `c2-content-factory` selected.

## Filling in the day prompts

Prompts 3 and 4 are templates. Every value that changes per day is a placeholder, and the same
placeholder appears everywhere it is needed, so substituting once gets the whole prompt right.

| Placeholder | Means | Wednesday of Week 1 |
|---|---|---|
| `{WW}` | Week number, always two digits | `01` |
| `{D}` | Day number as the **folder** is named, one digit | `3` |
| `{DD}` | Day number as **filenames and the branch** are written, two digits | `03` |
| `{WEEKDAY}` | Weekday name | `Wednesday` |
| `{DATE}` | Full date, read from `docs/programme/calendar.md` | `7 October 2026` |
| `{WEEK_FILE}` | The week tab export in `docs/curriculum/`, which uses a single-digit week | `W1_Data_analysis_found.md` |

Saturday is the exception: its folder is `content/W{WW}/SAT/`, its filenames use the stem
`C2_W{WW}_SAT_`, and its branch is `w{WW}-sat`. Prompt 4 has this already filled in. Take every
date from the calendar page, which the sync writes from the curriculum workbook: the calendar moved
by a week on 21 September 2026, and a date typed from memory is the old one.

Three of these bite if you skim them.

The folder is `D{D}` with one digit and the filename stem is `D{DD}` with two, so Wednesday
lives in `content/W01/D3/` as `C2_W01_D03_...`. They do not match by design and the verifier
now fails when they disagree.

Inside the day folder every file sits in a subfolder by artifact type, and the verifier fails a
file left loose at the root or filed in a folder that day shape does not have. `content/README.md`
is the layout.

The week tab file uses a single-digit week, so Week 1 is `W1_Data_analysis_found.md` while the
content folder is `W01`. Build weeks use a different name again, such as `W3_Build_1.md`.

Before pasting, search the filled prompt for any of the six placeholders above still in braces.
One unreplaced `{D}` is how a Day 3 build ends up writing over a merged Day 2 pack.

`{artifact}`, `{AUDIENCE}` and `{ext}` are different. They are part of the naming rule itself and
stay in braces, because the session fills them per file.

---

## Prompt 1. Install the skill and finish the scaffold

```
Set up this repository so future sessions load the day-pack skill automatically.

1. Create the directory .claude/skills and move bootstrap/day-pack-builder into it, so the result is .claude/skills/day-pack-builder/SKILL.md plus its references folder. Remove the now-empty bootstrap directory.
2. Create a .gitignore containing: .DS_Store, __pycache__/, *.pyc, .ipynb_checkpoints/
3. Create the directories content/W01 through content/W09. Each gets a D{n} subdirectory for every weekday that has a session, numbered Monday to Friday as D1 to D5 with holidays left out, plus a SAT subdirectory. Read content/README.md for which days each week has. Put an empty .gitkeep file in each so git tracks them.
4. Read CLAUDE.md and .claude/skills/day-pack-builder/SKILL.md, then reply with: the ground-truth order, the six build-workflow steps, and the name of the file you must read before building any day pack. Do not build any content.
5. Commit on a branch named setup-skill and stop.
```

After it finishes: open the diff, create the pull request, merge it on GitHub.

---

## Prompt 2. Verify the context landed (read-only, no commit)

```
Read CLAUDE.md, docs/curriculum/W1_Data_analysis_found.md and docs/curriculum/Structure.md. Do not write or commit anything.

Answer in under 200 words:
1. What does Week 1 Tuesday teach, and what must the trainer stop before?
2. What is the deliberate failure for Week 1 Wednesday, with its exact error behaviour?
3. What is the status of the client-zero scenario, and what does that block?
4. What does the Week 1 Friday carry, and which client-zero version does it need?
```

The answers must come from the files. If anything is vague or invented, stop and tell me before we build.

---

## Prompt 3. Build one teaching day (use for any regular teaching day)

Substitute the six placeholders from the table above, then read the filled prompt back looking for any of them still in braces.

```
Build the full day pack for Cohort 2, Week {WW}, Day {DD}, {WEEKDAY} {DATE}.

Source of truth, in order: this prompt, data/programme/facts.yaml for any movable fact, the day's row in docs/curriculum/{WEEK_FILE} (with the violet IITGN faculty column where the week has one), the day's line in docs/programme/calendar.md, docs/curriculum/Structure.md, and docs/06_Day_Pack_Method.md. Follow .claude/skills/day-pack-builder/SKILL.md. If the row is missing, the client-zero lock is needed and absent, or a link on the row is unverified, stop and name the gap instead of building around it.

Run the gates in order and stop after gate 2 for my approval:
0. Source lock: one written reference and one video per new topic, the product's own documentation for any tool used for the first time, and every movable fact verified with the date it was checked. Links I supply are the lock rather than a starting point. Where a fact cannot be verified in the session, write "not verified" rather than a guess. List the locked sources with their dates before gate 1.
1. Envelope and continuity: what the room already knows, what today must not repeat, what comes later, all from the row, in one short block.
2. The spine, one screen: the deck decision (one deck, or half one and half two), section list per artifact, the day's mental-model arc in one sentence, the deliberate failures with their exact error text or exact wrong output, the activity choice and its toggle, the take-home shape with its resistance patterns named. Wait for my approval.
3. Build passes after approval, one artifact family per message: (a) deck or deck halves, (b) notebooks, (c) activity, (d) exercises with solutions, (e) take-home with its self-check spine, (f) Kahoot pack, (g) study notes, cheat sheet and pre-read.
4. Run python3 scripts/verify.py content/W{WW}/D{D} --execute and fix every failure, then report the results including what failed and was fixed. That one command carries every proof: nb_check for saved outputs, rendered diagrams and passing checks; distractor_audit for the option sets; xlsx_recalc for the workbook's verdicts under a flipped decision; html_sweep for every control on every demo page; deck_md_check for the slide source's numbering, title guard, question pairing and diagram share; and deck_check for a .pptx only once one has been freshly built from that markdown. A proof that reports it could not run in this session is not a pass, so say which ones ran.

Write every file under content/W{WW}/D{D}/ inside the subfolder its artifact type belongs in, named C2_W{WW}_D{DD}_{topic}_{AUDIENCE}.{ext}. Read content/README.md for the folder set before pass 1, and leave no file loose at the day folder root. Commit on branch w{WW}-d{DD}.

Binding rules: mental model first and spiral always; at most four new ideas per two-hour block; application before theory; one deliberate failure per block, carrying its exact error text where the break is a crash and its exact wrong output where the break is not; notebooks rich and progressive (idea, diagram, demo, output, failure, fix, industry example and interview question at milestones, one new element per section); activity toggle-driven with minimal typing; exercises few and think-heavy with selection or repair answers; take-home shortcut-resistant with verified exploration links and a self-check spine; durations only, role labels only, Rs never the glyph, no em-dashes.
```

Then: approve the spine in the same session, let the passes run, read the verification report, open the diff, create the pull request, merge.

One session per day pack. Start a new task for the next day rather than continuing this one.

---

## Prompt 4. Build the Saturday recap pack (the SAT folder of any regular week)

Substitute `{WW}`, `{WEEKDAY}`, `{DATE}` and `{WEEK_FILE}` from the table above. Saturday uses `SAT` everywhere a numbered day would appear, so there is no `{D}` or `{DD}` to fill.

```
Build the Saturday pack for Cohort 2, Week {WW}, Saturday {DATE}.

Source of truth: the week's paper in docs/curriculum/Saturday_papers.md (the tracker's item bank), the Saturday row in docs/curriculum/{WEEK_FILE}, docs/curriculum/Structure.md, and docs/06_Day_Pack_Method.md. Follow the Saturday section of .claude/skills/exercise-builder/SKILL.md. Saturday is not a teaching day, so build only these:

1. The recap paper: pen and paper, AI-free and objective, the bank's items in the bank's order, printing the Item column only. It is swapped and marked against the key.
2. The key: per item, the key, level, tag, roles, day and the interview anchor it descends from, so a peer can mark in seconds.
3. The discussion guide for the Academic TA: marking against the key, the most-missed items first as an interview-answer discussion with random call-outs, and the scores by tag that feed Monday's remediation read.

Stop after a one-screen spine for my approval before writing anything. Then write content/W{WW}/SAT/paper/C2_W{WW}_SAT_paper_STUDENT.md, content/W{WW}/SAT/answer-key/C2_W{WW}_SAT_answer_key_TRAINER.md and content/W{WW}/SAT/discussion/C2_W{WW}_SAT_discussion_TRAINER.md. Run python3 scripts/verify.py content/W{WW}/SAT and report. Commit on branch w{WW}-sat.

The paper is ungraded and is a performance indicator, so state no marks total anywhere in the student file. If the week has no paper in the bank yet (Weeks 10, 11, 13 and 14), stop and say so; authoring a paper is a separate request.
```

---

## Prompt 5. Build the Week 0 Monday introduction pack

```
Build the introduction pack for Cohort 2, Week 0, Day 1, Monday 28 September 2026.

Orientation moved to Week 0 Monday on the 21 September calendar. Read .claude/skills/day-pack-builder/references/day1-intro-pack.md first, then docs/journey/Week_0.md (what learners have been told, which sets the running order), the Monday row in docs/curriculum/W0_Baseline_week.md (which sets the content), and docs/curriculum/Structure.md.

Confirm before starting that docs/07_Client_Zero.md exists and is marked locked. If it does not, stop and say so rather than inventing a company.

Stop after the spine for my approval. The spine covers the client-zero narrative deck with the mental-map and entity diagrams, the journey map across twenty weeks, the kinds of week, the session mechanics, the setup walkthrough and the self-rating form. Then build in passes, verify with python3 scripts/verify.py content/W00/D1, and commit on branch w00-d1.
```

---

## Prompt 6. Refresh everything after a workbook change

```
One of the workbooks has been updated: docs/curriculum/source.xlsx, docs/faculty/source.xlsx or docs/journey/source.xlsx. Run python3 scripts/sync_programme.py, then show me the warnings and errors it printed and a summary of which files changed and what changed in each. If it reports an error, stop and explain it rather than editing around it. Commit on branch programme-sync. If openpyxl or pyyaml is missing, install it first with pip install openpyxl pyyaml.
```

## Prompt 7. A movable fact changed

```
{WHAT CHANGED, for example: IIT Gandhinagar confirmed the Week 4 faculty sessions, and W4-3 moves to Thursday 29 October.}

Record it in data/programme/facts.yaml (a faculty change goes under faculty.overrides until IIT Gandhinagar sends a new workbook; a holiday, a decision or a proposal goes in its own section, with its status and its source). Run python3 scripts/sync_programme.py and show me what it changed, including every day pack whose sync blocks moved. Then run python3 scripts/board_sync.py --dry-run --all and show me what the board would change. Commit on branch programme-sync and stop.
```
