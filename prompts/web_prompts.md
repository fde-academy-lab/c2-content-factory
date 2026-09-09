# Copy-paste prompts for Claude Code on the web

One task per prompt. Start each from claude.ai/code with `c2-content-factory` selected.

---

## Prompt 1. Install the skill and finish the scaffold

```
Set up this repository so future sessions load the day-pack skill automatically.

1. Create the directory .claude/skills and move bootstrap/day-pack-builder into it, so the result is .claude/skills/day-pack-builder/SKILL.md plus its references folder. Remove the now-empty bootstrap directory.
2. Create a .gitignore containing: .DS_Store, __pycache__/, *.pyc, .ipynb_checkpoints/
3. Create the directories content/W01 through content/W09, each with subdirectories D1 to D6, and put an empty .gitkeep file in each so git tracks them.
4. Read CLAUDE.md and .claude/skills/day-pack-builder/SKILL.md, then reply with: the ground-truth order, the six build-workflow steps, and the name of the file you must read before building any day pack. Do not build any content.
5. Commit on a branch named setup-skill and stop.
```

After it finishes: open the diff, create the pull request, merge it on GitHub.

---

## Prompt 2. Verify the context landed (read-only, no commit)

```
Read CLAUDE.md, docs/curriculum/W1_Curriculum.md and docs/curriculum/Structure.md. Do not write or commit anything.

Answer in under 200 words:
1. What does Week 1 Tuesday teach, and what must the trainer stop before?
2. What is the deliberate failure for Week 1 Wednesday, with its exact error behaviour?
3. What is the status of the client-zero scenario, and what does that block?
4. Which day of Week 1 has no session, and why?
```

The answers must come from the files. If anything is vague or invented, stop and tell me before we build.

---

## Prompt 3. Build one teaching day (use for D2, D3, D4)

Replace the three values in the first line.

```
Build the full day pack for Cohort 2, Week 1, Day 2, Tuesday 29 September 2026.

Source of truth, in order: this prompt, the day's row in docs/curriculum/W1_Curriculum.md, docs/curriculum/Structure.md, and docs/06_Day_Pack_Method.md. Follow .claude/skills/day-pack-builder/SKILL.md. If the row is missing, the client-zero lock is needed and absent, or a link on the row is unverified, stop and name the gap instead of building around it.

Run the gates in order and stop after gate 2 for my approval:
1. Envelope and continuity: what the room already knows, what today must not repeat, what comes later, all from the row, in one short block.
2. The spine, one screen: the deck decision (one deck, or half one and half two), section list per artifact, the day's mental-model arc in one sentence, the deliberate failures with exact error text, the activity choice and its toggle, the take-home shape with its resistance patterns named. Wait for my approval.
3. Build passes after approval, one artifact family per message: (a) deck or deck halves, (b) notebooks, (c) activity, (d) exercises with solutions, (e) take-home with its self-check spine, (f) Kahoot pack, (g) study notes, cheat sheet and pre-read.
4. Run python3 scripts/verify.py content/W01/D2 and fix every failure, then report the results including what failed and was fixed.

Write every file under content/W01/D2/ using C2_W01_D02_{artifact}_{AUDIENCE}.{ext}. Commit on branch w01-d2.

Binding rules: mental model first and spiral always; at most four new ideas per two-hour block; application before theory; one deliberate failure per block with exact error text; notebooks rich and progressive (idea, diagram, demo, output, failure, fix, industry example and interview question at milestones, one new element per section); activity toggle-driven with minimal typing; exercises few and think-heavy with selection or repair answers; take-home shortcut-resistant with verified exploration links and a self-check spine; durations only, role labels only, Rs never the glyph, no em-dashes.
```

Then: approve the spine in the same session, let the passes run, read the verification report, open the diff, create the pull request, merge.

---

## Prompt 4. Build the Saturday recap pack (D6)

```
Build the Saturday pack for Cohort 2, Week 1, Day 6, Saturday 3 October 2026.

Source of truth: the Saturday row in docs/curriculum/W1_Curriculum.md, docs/curriculum/Structure.md, and docs/06_Day_Pack_Method.md. Saturday is not a teaching day, so build only these:

1. The recap paper: pen and paper, AI-free, about two hours, built from the question set on the Saturday row, short-answer format so papers can be swapped for peer cross-evaluation. Questions carry no answers on the student paper.
2. The answer key and marking guide for the peer cross-evaluation, with the mark split per question and what a full-credit answer contains.
3. The discussion guide for the Academic TA: the order to walk the answers, the two follow-ups per question, and the random call-out list.

Stop after a one-screen spine for my approval before writing anything. Then write to content/W01/D6/ as C2_W01_D06_recap_paper_STUDENT.md, C2_W01_D06_answer_key_TRAINER.md and C2_W01_D06_discussion_guide_TRAINER.md. Run python3 scripts/verify.py content/W01/D6 and report. Commit on branch w01-d6.

The paper is ungraded and is a performance indicator, so state no marks total anywhere in the student file.
```

---

## Prompt 5. Build Day 1, after client zero is locked

```
Build the Day 1 pack for Cohort 2, Week 1, Day 1, Monday 28 September 2026.

Day 1 is the exception: it ships the introduction pack plus the teaching day. Read .claude/skills/day-pack-builder/references/day1-intro-pack.md first, then the Monday row in docs/curriculum/W1_Curriculum.md and docs/curriculum/Structure.md.

Confirm before starting that docs/07_Client_Zero.md exists and is marked locked. If it does not exist, stop and say so rather than inventing a company.

Stop after the spine for my approval. The spine must cover both halves: the introduction pack (client-zero narrative deck with the mental-map and entity diagrams, the journey map, the session-mechanics section) and the standard teaching pack for the day. Then build in passes, verify, and commit on branch w01-d1.
```

---

## Prompt 6. Refresh the curriculum exports after a workbook change

```
The workbook docs/curriculum/source.xlsx has been updated. Run python3 scripts/export_curriculum.py, then show me a summary of which markdown files changed and what changed in each. Commit on branch curriculum-refresh. If openpyxl is missing, install it first with pip install openpyxl.
```
