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

1. Read the day's row in docs/curriculum/W{n}_*.md plus Structure.md, then read .claude/skills/day-pack-builder/SKILL.md and its references, then content/README.md for the folder layout.
2. Lock the sources before anything else: one written reference and one video per new topic, the product's own documentation for any tool used for the first time, and every movable fact verified with the date it was checked. Links the requester supplies are the lock rather than a starting point. Where a fact cannot be verified in the session, the artifact says "not verified" rather than carrying a guess. Then state envelope and continuity, then the one-screen spine. STOP for approval. Build nothing past the spine without an explicit yes.
3. Build in passes, one artifact family per pass: deck(s), notebooks, activity, exercises with solutions, take-home with self-check spine, Kahoot pack, study notes plus cheat sheet plus pre-read.
4. Write outputs only under content/W{ww}/D{d}/ for a teaching or build day and content/W{ww}/SAT/ for a Saturday, always inside the subfolder that fits the artifact (slides, notebooks, demos, whiteboards, cheatsheets, study-notes, exercises with its guided, unguided and solutions folders, takehome, kahoot, preread, extras, data, trainer, internal). Never leave a file loose at the day folder root. content/README.md carries the full layout, including the different shapes a build day and a Saturday take. Name files C2_W{ww}_D{dd}_{topic}_{AUDIENCE}.{ext}, or C2_W{ww}_SAT_{topic}_{AUDIENCE}.{ext} on a Saturday; the topic half carries only what the folder and the extension do not already say, and AUDIENCE is STUDENT, TRAINER or INTERNAL and is never omitted.
5. Run: python3 scripts/verify.py content/W{ww}/D{d} (or content/W{ww}/SAT) and fix every failure. A pack that has not passed verify is not done.
6. Commit on a branch named w{ww}-d{d}, or w{ww}-sat for a Saturday; never commit directly to main. In a cloud session, stop after committing and let the reviewer open the pull request.

## Hard rules

- Mental model first, spiral always; at most four new ideas per two-hour block; application before theory; one deliberate failure per block with exact error text.
- Durations only, never clock times, in any lesson material. Role labels only, never trainer names, in STUDENT files. No marks or weights anywhere until the Structure tab locks them.
- Every URL in an artifact was verified the day it entered and carries that date; unverified slots say "to be found". Never a URL from memory.
- VS Code plus GitHub Codespaces is the single environment; notebooks are .ipynb and must run cold top to bottom; SQL is .sql against Postgres.
- Notebooks ship executed: every code cell carries its saved output, at least three diagrams are rendered from code cells, and at least five checks report and pass. An unexecuted notebook teaches nobody reading it on GitHub.
- Every exercise, quiz and recap paper passes `scripts/distractor_audit.py`: no key is the longest option, key positions spread, and no format line contains the true answers.
- Every demo page passes `scripts/html_sweep.py`: a browser clicks every control, every control does something visible, and the console is clean.
- A deck is authored and transformed as markdown, which is what the gate reads; `scripts/build_deck.py` turns it into the .pptx as a separate step, so a .pptx older than its markdown is stale and gets rebuilt rather than shipped. The slide's visual system lives in `scripts/deck_layout.py`, so a claim, a breadcrumb, a table and a code block look the same in every deck of the programme.
- A cheat sheet is authored as markdown and `scripts/build_cheatsheet.py` prints it, so a sheet with no PDF beside it, or a PDF older than its markdown, fails the gate. Panel one is the anchor and carries the day's picture, which is the same drawing the deck and the notebook use.
- Every diagram is a mermaid fence rendered through the shared theme, never a picture pasted in, and it is measured before it ships: a label that would print under about five points on a sheet or nine on a slide means the diagram gets reshaped shorter or narrower, never that the page shrinks it.
- Kahoot is daily and ungraded; no tests in build weeks; the Saturday recap paper comes from the week's question set.
- Writing style: no em-dashes anywhere; "Rs" never the currency glyph; full connected sentences; banned words include Additionally, Moreover, However, Hence, Thus, Nonetheless, Furthermore, Accordingly, Indeed, Dynamic, comprehensive, robust, holistic, seamless, and leverage as a verb; no "not X, but Y" constructions.
- Rationale, sizing arithmetic and open questions go in the chat reply, never inside an artifact.

## Cloud sessions

Sessions run on Anthropic-managed VMs with the repository cloned in. Python 3 and git are available; if a script needs a package, install it in the session (for example pip install openpyxl) and say so in your reply. Write files only inside the repository. Never push to main.

## Session discipline

One session per day pack. Do not continue yesterday's session for today's pack; start fresh with prompts/day_pack_prompt.md. If asked to build multiple days in one session, refuse and explain the drift risk.

## Skills: finding and using the right ones

Every task starts with skill selection, and it is a step, never an afterthought.

1. Run `python3 scripts/skills_index.py` and read the list. It prints every installed skill with its source and when to use it, and refreshes `docs/skills-catalog.md`.
2. Choose from the routing table below, then read each chosen SKILL.md in full before producing anything. Take the parts that apply to this task and leave the rest; a skill is a toolbox, never a script to run end to end.
3. State in the chat reply which skills were used and which parts, in one line.
4. When two skills disagree, precedence runs: this repository's CLAUDE.md and docs, then day-pack-builder, then the author's own skills (those whose SOURCE file says author-skill), then Matt Pocock's skills, then Anthropic's document skills, then community skills. This repository's writing rules win over any skill's style.
5. Never install a catalog wholesale. `docs/skills-catalog-community.md` and `docs/skills-catalog-composio.md` are lookup lists for importing one specific skill on request.

| Task | Read these skills |
|---|---|
| Any deck | training-deck-builder for structure and the sketchbook visual system; pptx for the build and the render check; pptx-html2pptx when a slide needs HTML-precise layout; academic-pptx for action titles and one exhibit per slide; powerpoint-keynote-presentation for the Workshop scaffold and the anti-AI-tone pass; concept-packaging when a concept lands flat |
| Demo notebook or any script | notebook-builder for the helper, the MAP, DO, SEE, CHECK, SUM rhythm and the TODO twin; day-pack-builder for the notebook's place in the pack; tdd and diagnosing-bugs for the data generator and for staging deliberate failures; scaffold-exercises for the progression ladder |
| Any demo, activity, companion page or workbook | companion-builder for the guided walk, the experiment cards, the diagram builders and the two Excel forms; frontend-design when the page needs a visual direction; xlsx for the workbook build |
| Exercises, take-homes, build-week briefs | exercise-builder for the device wheel, item sizing and distractor discipline; scaffold-exercises; mini-project-designer for build weeks; day-pack-builder for the resistance patterns |
| Study notes and cheat sheets | study-notes-builder; fde-study-notes; fde-cheat-sheets; docx and pdf for the files; `scripts/build_cheatsheet.py` for the printed sheet |
| Curriculum rows and week plans | lesson-strategy first, then lesson-architecture, then curriculum-detailing |
| The spine before approval | grilling, or grill-me when the requester is in the session, to close open branches before asking for approval |
| Reference links | research for primary-source verification; every link dated per the hard rules |
| A decision only a person can make | decision-questionnaire or to-questionnaire |
| Parking work for another session | cohort-handoff or handoff |
| A delivered-session transcript | session-debrief |
| Learner concern or a risky announcement | concern-handling |
| Editing CLAUDE.md or any skill | writing-for-agents and writing-great-skills |
| Before committing any written artifact | llm-tic-scrubber, then `python3 scripts/verify.py`, which is the one command that runs every proof: nb_check, distractor_audit, xlsx_recalc, html_sweep and deck_md_check on the markdown, plus deck_check on a .pptx once one is freshly built |

One-time: run `/setup-matt-pocock-skills` in a session once, choosing local files as the issue tracker and `docs/` for generated docs, so the engineering skills know where to write.

## Agent skills

### Issue tracker

Issues and specs live as committed markdown files under `.scratch/<feature-slug>/`, not in GitHub Issues. See `docs/agents/issue-tracker.md`.

### Triage labels

The five canonical role strings are used unchanged, running from `needs-triage` to `wontfix`, and they sit on a `Status:` line inside each issue file. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context, so `CONTEXT.md` and `docs/adr/` both sit at the repository root. See `docs/agents/domain.md`.
