# Week 4: the build workflow (revised 12 October 2026, afternoon)

Today is Monday 12 October 2026. Week 4 opens on Monday 26 October 2026 (`docs/programme/calendar.md`)
and the freeze is Friday 23 October. Building starts today; there is no pilot gate. Fourteen sessions
build the week, in waves of at most three at a time, and every session is a cloud session on its own
branch that pushes and stops; the orchestrating session reviews, opens the pull request, merges and
moves the board card (`python3 scripts/board_sync.py --status W04/D3 review-1` and onward,
`docs/agents/content-board.md`). No day session opens, merges or closes a pull request.

## 0. The calendar

| Wave | Dates | Sessions (model) | Depends on |
|---|---|---|---|
| S0 | Mon 12 Oct | S0 the method session (the orchestrator, Opus 5.5) | The requester's approval of `W04_analyst_craft_spine.md`, `W04_case_file.md` and the decisions in `ONE_SCREEN.md` |
| 1 | Tue 13 to Wed 14 Oct | D1-draft, D3-draft, D4-draft (claude-opus-4-7) | S0 merged |
| 2 | Thu 15 to Fri 16 Oct | D5-draft, D2-draft (claude-opus-4-7); D1-finish (claude-opus-5-5) | D2-draft needs D1-draft's facts file (merged Wed 14); D1-finish needs D1-draft |
| 3 | Sat 17 to Sun 18 Oct | D3-finish, D4-finish, EXP the explorer (claude-opus-5-5) | EXP needs all five facts files (D5 and D2 land Fri 16) |
| 4 | Mon 19 to Tue 20 Oct | D5-finish, D2-finish, SAT the Saturday session (claude-opus-5-5) | SAT reads the finished packs as they merge |
| 5 | Wed 21 to Thu 22 Oct | WR the week read and print run (claude-opus-5-5); the slack for a slipped session | Every pack merged |
| Freeze | Fri 23 Oct | | WR merged; every card Done |

Branches: `w04-method`, `w04-d1` to `w04-d5` (the draft and the finish of a day share its branch; the
finish checks out the pushed draft), `w04-explorer`, `w04-sat`, `w04-week-read`. The orchestrator
merges each wave's branches before the next wave starts, D1-draft's on Wednesday evening so D2-draft
and D1-finish can read it. A session that finds its model id unavailable in the environment's model
list uses the other Opus model and says so in its report; no model id is guessed.

If a draft slips a day, its finish moves a day and the week read absorbs it; the explorer can start
with four facts files and add the fifth day's scenes on Monday 19 October. If the weekly usage limit
hits mid-build, the Saturday paper and the week read move first, since the bank and the builder already
exist, and the explorer moves last, since the decks reference its scenes by id and can ship without it
for one day.

## 1. Rules every session follows

**Read first, in this order.** `docs/detailing/W04_analyst_craft_spine.md` (the approved spine; this
plan's `W04_analyst_craft_spine.md` until S0 lands it), `docs/detailing/W04_case_file.md` (the day's section in
full), `.claude/skills/day-pack-builder/references/teaching-styles.md`, the day's row in `docs/curriculum/W4_Analyst_craft.md`,
the day's line in `docs/programme/calendar.md`, `docs/detailing/W04_research_cases.md` for the allowed
facts (as `docs/detailing/W04_research_ledger.md` once S0 copies it), `docs/07_Client_Zero.md`
sections 1, 1a, 1b, 6 and 7 for the Kalpa transfer, CLAUDE.md, and `the-standard.md` for the form of
each family only. Then the skills the task needs: `day-pack-builder` (the artefact manifest and file
naming), `training-deck-builder`, `notebook-builder`, `exercise-builder`, `study-notes-builder`,
`fde-cheat-sheets`, `concept-packaging`, `companion-builder` and `design-taste-frontend` in EXP,
`ponytail` for every line of code, `humanizer` and `llm-tic-scrubber` for every line of prose,
`research` for any fresh fact. Run `bash setup.sh` before anything else and say in the report what
the setup could not install.

**Models and effort.** Every session runs at max effort; `.claude/settings.json` pins it. A drafting
session runs on `claude-opus-4-7`; a finishing session, EXP, SAT and WR run on `claude-opus-5-5`; the
two cold reads inside a finishing session are agents on the Opus 5.5 model.

**The rules that stop invention.**

1. No number outside the facts file. Every number in any learner file comes from the day's facts
   file under its id, or from the data through code in an executed cell whose value the facts file
   also carries. A number the notebook computes that disagrees with the facts file is a stop: the
   session reports both values and builds nothing on either until the generator is fixed.
2. No company fact outside R2 or a fresh dated check. Every public fact about a company comes from
   the case file's table for the day with its R2 id and check date, or from a primary source the
   session fetched and dated the same way and recorded in its sources list; otherwise the sentence
   labels it a hypothetical. No company outside the case file's tables appears in any file. No URL is
   written from memory. A URL that fails on the day reads "not verified on <date>" and leaves the
   learner files.
3. Every case is labelled illustrative. The line "Illustrative case: the company is real, the
   situation and the data are synthetic, built for this class" opens the ticket in every learner file
   that carries it, and no sentence anywhere says the company did or suffered the situation.
4. A toy (the canteen token, the tea stall, the coaching batches, the cups) is labelled invented in
   every learner file where it appears. An assumption (an add rate, a margin, a unit cost, an uptake)
   is labelled with its range, and the fact that would change it is named beside it.
5. The Kalpa transfer stays in second position and its plant stays hidden: the Kalpa twelve rows and
   every planted value sit in TRAINER files until the lab; the lab step that finds a plant runs in an
   empty your-turn cell; a STUDENT file names a plant only as decision `w4-finding-once-found` allows.
   Kalpa's people are those in client zero section 1a and no one else.
6. The faculty block's content appears only through `sync:faculty-day:W04/D{d}`, and a STUDENT file
   says tentative beside any mention of it. No trainer name anywhere. No clock time in lesson material;
   the peak windows are named by length, never by hour.
7. The style: no em-dashes or en-dashes; Rs and never the glyph; none of CLAUDE.md's banned words and
   none of the antithesis constructions it bans; full sentences; durations only. Every prose file passes
   the humanizer in file mode and the tic scanner (`python3 .claude/skills/llm-tic-scrubber/scripts/tic_scan.py <file>`),
   and the notebooks' markdown is edited through the script that writes them.
8. The explorer never carries a Kalpa plant: EXP greps the five facts files' `plants` blocks against
   its constants block and the report pastes the empty result.
9. Nothing is called done without `python3 scripts/verify.py content/W04/D{d}` (or `/SAT`) and
   `python3 scripts/sync_programme.py --check` passing, with both outputs in the report, and the
   spine's acceptance test (section 12) ticked line by line with evidence.

**What every day leaves behind in `internal/`.** The generator `C2_W04_D0{d}_generate_INTERNAL.py`
and its contract output `C2_W04_D0{d}_contract_INTERNAL.md` (every line PASS), the facts file
`C2_W04_D0{d}_facts_INTERNAL.yaml`, the drafting brief, the sources list `C2_W04_D0{d}_sources_INTERNAL.md`
of at most one page (each URL with its check date and where it is used, the data command, the toys and
assumptions, the two cold reads' findings and what each fix changed, in a line each), the cold reads
`C2_W04_D0{d}_cold_reads_INTERNAL.md`, and the figure script `C2_W04_D0{d}_figures_INTERNAL.py` that
draws every PNG and GIF under `whiteboards/`. No narrative provenance, no proof script beyond these.

## 2. S0, the method session (Monday 12 October)

**Model.** The orchestrator, Opus 5.5, max effort, one session; no drafting agent.

**Inputs.** `W04_analyst_craft_spine.md`, `W04_case_file.md`, `ONE_SCREEN.md` with the requester's answers,
`docs/detailing/W04_research_cases.md`, `.claude/skills/day-pack-builder/references/teaching-styles.md` when it lands, CLAUDE.md,
`the-standard.md`, `data/programme/facts.yaml`, `data/programme/paper_edits.yaml`, `scripts/build_deck.py`,
`scripts/deck_md_check.py`, `scripts/build_cheatsheet.py`, `scripts/sync_programme.py`'s docstring.

**Outputs.**

1. `docs/detailing/W04_analyst_craft_spine.md`: `W04_analyst_craft_spine.md` as approved, with the requester's
   edits if any, its status line reading approved with the date.
2. `docs/detailing/W04_case_file.md`: `W04_case_file.md` as approved.
3. `.claude/skills/day-pack-builder/references/teaching-styles.md`: `.claude/skills/day-pack-builder/references/teaching-styles.md` copied as it stands, or a
   one-paragraph placeholder naming the twelve styles of spine section 2.4 if R3 has not landed, to be
   replaced by the week read.
4. `docs/detailing/W04_research_ledger.md`: R2 copied as it stands, marked INTERNAL in its header, so
   day sessions read the facts from the repository.
5. CLAUDE.md with the four bullets replaced exactly as spine section 13 words them; the-standard.md's
   opening paragraph amended exactly as section 13 words it.
6. `data/programme/facts.yaml`: the six decisions added under `decisions` with status closed and the
   requester as closer on 12 October 2026; `saturday_papers.paper_minutes` gains `W04: 120`; the
   `papers-to-build` text gains its Week 4 Tuesday line.
7. `data/programme/paper_edits.yaml`: a `W4:` block with item 41's `stem` edit, status proposed, the
   text and reason from spine section 10.
8. The three script changes: an image line in `build_deck.py`; `deck_md_check.py` counting an image
   line toward the diagram share; `build_cheatsheet.py` placing an image line in a panel. A one-slide
   test deck and a one-panel test sheet under the session's scratch folder, each carrying a PNG and
   the deck a GIF, built and rendered through LibreOffice and looked at; the result recorded in the
   pull request's description.
9. `python3 scripts/sync_programme.py` run, so the decisions register, the calendar and every sync
   block re-render.
10. The six drafting briefs, one per day plus the explorer's, written into
    `content/W04/D{d}/internal/C2_W04_D0{d}_drafting_brief_INTERNAL.md` (and
    `content/W04/D1/internal/C2_W04_D01_explorer_brief_INTERNAL.md`), each carrying: the spine's day
    section verbatim; the case file's day section verbatim; the styles table for the day; the allowed
    R2 ids; the deck shape (the ticket as the cover, the week map lit as section 1 draws it, "where
    today ends" as slide three, the concept board built region by region, chapter openers as
    `## SECTION n:` each opening on a question with lettered options, a predict slide always followed
    by its reveal slide, every body slide with a notes fence opening LIVE and its minutes and naming
    any explorer scene it uses, the trap pair, the real-company slide with the decision and its cost,
    the chapter close that adds today's node to the map and gives the crux line); the notebook shape
    (first cell the ticket and the chapter's question, plain pandas and matplotlib, a three-line
    `check`, one line of narration per cell, predict-before-you-run with lettered options, the second
    route asserted equal, `check_summary` or five printed PASS lines at the end, the lab notebook with
    its empty your-turn cell); the generator's contract lines from the case file; the size limits; and
    the nine rules of section 1.

**Completion criteria, all of them.** The spine, case file, styles note and ledger exist under
`docs/detailing/`; CLAUDE.md's four bullets match section 13 character for character; the six decisions
read back from `facts.yaml`; `sync_programme.py --check` exits 0; the test deck and sheet build without
error and `deck_md_check.py` counts their image lines; `python3 scripts/verify.py content/W02/D3` still
passes as the spot check; the six briefs exist and each quotes its spine and case-file sections in full;
no other file changed. Branch pushed; the orchestrator merges the same day, since wave 1 loads CLAUDE.md.

## 3. The drafting session of a day (D1 to D5, claude-opus-4-7)

One session per day on `w04-d{d}`, from its drafting brief. It writes the case data, the decks and the
notebooks, and nothing else.

**Inputs.** The drafting brief, the spine and case file sections it quotes, the styles note, the
ledger, `data/generate_client_zero.py` (v4 is frozen: its 340 customers, 1,000 orders, payments,
refunds, exposure and plan line regenerate byte for byte, and the Kalpa transfer tables import its
frames), `content/W01/D1` as the model pack for form, the skills named in section 1.

**Stage A, the generator and the facts file.** `internal/C2_W04_D0{d}_generate_INTERNAL.py`: one
seed family, the standard library and pandas only, a `--contract` flag that prints PASS or FAIL with
both numbers for every target in the case file's tables and every Kalpa plant line, a `--list` flag.
It writes the case tables to `data/` as CSV (and the Kalpa transfer tables beside them, with
`content/W04/D1/data/C2_W04_D01_warehouse_v5_STUDENT.sql` on Monday adding `app_reorders` beside the
Week 2 warehouse without touching its tables; Wednesday, Thursday and Friday add their Kalpa tables to
the same loadable file through `.devcontainer/load_warehouse.sh`), the twelve rows as their own CSV,
and the facts file with `day`, `written_by` (the session, the date, the commit), `source_tables`,
`numbers` (a list of `id`, `value`, `unit`, `how` in one line, `used_by` as the level or chapter),
`twelve_rows`, `kalpa` (the transfer's numbers), `plants` (each with `value` and `found_in`, the lab
notebook's your-turn cell) and `shared_constants` (Monday and Thursday: the two Kalpa windows,
asserted equal). The regenerated v4 is diffed against the committed Week 2 warehouse and the diff is
empty. If a plant cannot be shaped with v4 frozen, the session takes the fallback the case file names
and records it in the facts file; it never changes a case target.

**Stage B, the decks.** `half1`, `half2` and (on a faculty day) `fallback` as markdown to the deck
shape in the brief, built with `scripts/build_deck.py`, rendered through LibreOffice and looked at
slide by slide; `deck_md_check.py` passing. The ticket is the cover, word for word from the case file.

**Stage C, the notebooks.** The notebooks of the spine's artefact table as `nb_make`-style build
scripts in `internal/`, executed cold in their own folders, each with at least three rendered pictures
and five passing checks, the lab notebook with its empty your-turn cell, every cell narrated in one
line, the predict cell before every trap.

**Stage D, the figure script and the pictures.** Every PNG and the GIF the spine names, with the
GIF's first and last frames as PNGs, under `whiteboards/`, drawn from the facts file.

**Completion criteria, all of them.** The generator's contract output is pasted in the report with
every line PASS; the v4 diff is empty; every table has exactly the columns the case file lists; the
facts file carries every number the spine and the case file mark "target" for the day (the session
lists them against the case file's lines in the report) and every Kalpa plant with its `found_in`; the
twelve rows match the case file's shape row by row; every deck builds, renders and passes
`deck_md_check.py`, opens on the ticket with the label line, carries the week map on slide two and
"where today ends" on slide three, and names its explorer scenes in notes fences; every notebook ran
cold and ships executed within its cell limit; `python3 scripts/verify.py content/W04/D{d}` passes on
what exists (data, internal, slides, notebooks, whiteboards); `sync_programme.py --check` passes; the
branch is pushed with the report naming every value chosen and which case-file line it answers. The
session writes no exercise, note, sheet, pre-read or trainer file.

## 4. The finishing session of a day (D1 to D5, claude-opus-5-5)

One session per day, checking out `w04-d{d}` as the draft left it.

**Stage A, the read.** Reads the draft against the spine's day section, the case file and the facts
file before building on it, and fixes the draft where it drifts (a number with no home, a slide that
opens on a topic, a trap without its predict slide, a cell without its one line).

**Stage B, the rest of the pack.** Exercises with solutions (the devices from `exercise-builder`;
every stem a question; items ordered by level and tagged with the company that asks them; at least a
third design items; the distractor audit), the take-home with its self-check (plain words first), the
Kahoot pack (eight items, the return question, a `*Tests:*` line each), the study notes (each level
linked to its explorer scene, the "say it to a hostel warden" line under each), the cheat sheet
(markdown, then `build_cheatsheet.py`, panel one the concept board and panel two the twelve rows), the
pre-read, the transcript and the AI-company variant from the case file's L6 notes, the guesstimate
sheet with its anchor and catch, the pain points, the trainer files (the day sheet with its sync blocks
and the ladder, the run sheet, the role cards with their ledger facts, the scorecard, the fallback note,
the lab note with the Kalpa twelve rows and the plant table), the board work.

**Stage C, the house reads.** Humanizer in file mode and the tic scanner on every prose file and on
the notebooks' markdown through their build scripts; the headings-only read of every learner file.

**Stage D, the two cold reads (two agents on Opus 5.5, findings only, never edits).** The fresh
graduate: "You are 23, you have never worked inside a company, and you open only the STUDENT files of
this pack, in the order a learner meets them, with the explorer's scenes for this day open beside
them. List every word, step, number and output you could not picture, could not predict or could not
have produced yourself, with the file and the place, and say what one sentence would have let you."
The hiring interviewer: "You run analyst screens at a product company's Bengaluru centre. Score every
transcript's hire-grade answer and the AI-company variant on the TRAINER scorecard, name anything a
strong interviewer would reject in the interview material, the exercises' design items and the
guesstimate, name any sentence that claims a real company did something the case file does not
support, and name any real fact you would want a source for." Both write to
`internal/C2_W04_D0{d}_cold_reads_INTERNAL.md`.

**Stage E, the fix pass.** Every finding is fixed or carries a one-line reason in the sources list. A
fix that changes a number other files repeat is checked in those files and nowhere else. No second
round.

**Stage F, the gates.** `python3 scripts/verify.py content/W04/D{d}`, every failure fixed, the final
output pasted; `python3 scripts/sync_programme.py --check`; the facts-file listing: every number in a
STUDENT file with its facts id, produced by reading and pasted in the report; the company-fact
listing: every named company with its R2 id or "hypothetical"; the spine's acceptance test, all
seventeen lines, each ticked with the evidence in one line.

**Stage G.** Commit on `w04-d{d}`, push, report, stop.

**Completion criteria, all of them.** Every row of the spine's artefact table for the day exists
under its folder with its audience tag and within its size; the twelve-row hand count opens chapter 1;
the ticket opens every learner file that carries it, with the label line; the week map is slide two
with the right nodes lit and the earlier days' numbers on them; the concept board is built region by
region and is the sheet's panel one; the GIF exists with its two stills, or the cut is recorded; the
run sheet names roles, minutes, materials, lines and stall fixes, and every material exists; the
handoff line continues the ticket and is in the day sheet and `half2`; the fallback deck and note
exist and teach nothing the block owns; the transcript, the AI-company variant and the scorecard, the
guesstimate with its anchor or "to be found", and the pain points with their anchors are in the pack;
the role cards carry a ledger fact each; the Kahoot chains to the day before; the pre-read opens on
tomorrow's ticket; the Kalpa twelve rows and the plant sit only in TRAINER files and the lab
notebook's your-turn cell is empty; the two cold reads are in `internal/` with every finding resolved;
the sources list fits one page; verify.py and `sync_programme.py --check` pass with their outputs in
the report; the facts-file and company-fact listings are in the report; the acceptance test's
seventeen lines are ticked with evidence. A session that cannot meet a line stops at that line and
names it.

**Day-specific notes.**

- **D1.** Fixes the two Kalpa windows (10 to 30 September and 20 August to 9 September 2026) in
  `shared_constants`; its finish writes the war game and the role cards the Tuesday studio reuses.
- **D2.** Draft starts after D1-draft merges; its facts file copies Monday's numbers by id and adds
  the three denominators and the twelve-week series; it carries the three cluttered slides in `half1`
  and the one-slide template in `exercises/guided/`; its guesstimate sheet marks the drivers-at-peak
  anchor "to be found" unless the session fetches and dates a primary source; its Kahoot's return
  question is Monday's.
- **D3.** Writes `products` and `order_items` for the Kalpa transfer with the case file's contract
  lines; its trainer sheet carries the IBM Apriori audit item.
- **D4.** Reads Monday's `shared_constants` and asserts them; takes the app-activity fallback for
  Kalpa retention only if the orders-based version cannot be shaped, and says so.
- **D5.** Writes the Kalpa 24 months and the vendor curve with the case file's contract lines; the
  festival calendar card carries the three Diwali dates with F5 and `facts.yaml` beside it; its deck
  reopens the week map with Monday's, Wednesday's and Thursday's numbers.

## 5. EXP, the explorer session (Saturday 17 to Sunday 18 October, claude-opus-5-5)

**Inputs.** Spine section 11 (every scene), the five facts files, the five decks' notes fences
(which scene each slide calls), the styles note, `scripts/html_sweep.py`, `companion-builder`,
`design-taste-frontend` and `minimalist-ui` for the page's direction, `content/W01/D1/demos/` for the
house page conventions.

**Outputs.** `content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html` (one file, inline SVG and
script, no network, no storage, under 400 KB, a constants block at the top with every number and its
facts id) and `content/W04/D1/internal/C2_W04_D01_explorer_notes_INTERNAL.md` (the scene list with
the slide that calls each, the sweep output, the plant grep, the fresh-graduate walk's findings and
fixes).

**Completion criteria, all of them.** The home map lights day by day and opens each day's section;
all 21 scenes exist with their six parts (the question, the prediction, the drawing, the controls,
the reveal, the formula); every control changes a text readout; every slider's step moves a printed
digit; `python3 scripts/html_sweep.py content/W04/D1/demos/C2_W04_D01_week_explorer_STUDENT.html`
passes with every control clicked, none inert and no console error, output pasted; the plant grep is
empty and pasted; every number on the page is in a facts file or labelled a toy; the page opens from
disk with no network; a fresh-graduate agent walked every scene and every finding is fixed or
reasoned; `python3 scripts/verify.py content/W04/D1` still passes; the branch `w04-explorer` is pushed.

## 6. SAT, the Saturday session (Monday 19 to Tuesday 20 October, claude-opus-5-5)

**Model and skills.** Opus 5.5, max effort; `exercise-builder` for the blueprint and the key;
`day-pack-builder` for the Saturday shape; the W1 and W2 source files
(`content/W0{1,2}/SAT/internal/*_paper_source_INTERNAL.yaml`) and `scripts/build_saturday_paper.py`'s
docstring for the format.

**Inputs.** The bank's 43 Week 4 items (`docs/curriculum/Saturday_papers.md`), spine section 10, the
case file's Saturday section, the five facts files and the five lab notes (which plants the room
found), the transcripts and AI-company variants of the finished packs as they merge,
`paper_edits.yaml` with item 41's stem edit, `facts.yaml` with `paper_minutes W04: 120`.

**Outputs.** `content/W04/SAT/internal/C2_W04_SAT_paper_source_INTERNAL.yaml` (parts, banks,
additions, folded, stretch_bank, exhibits, notes, purpose, company, stretch), the paper and the key as
markdown and Word through `python3 scripts/build_saturday_paper.py W04 --docx`, the item-analysis
workbook with its recalc manifest, `discussion/C2_W04_SAT_discussion_guide_TRAINER.md` (the 300
minutes as spine section 10 runs them; the most-missed procedure; the anchors answered aloud; the
eight briefs with their answer grids; the spoken transfer round; the mock-interview round sheet
drawing its questions and follow-ups from the transcripts and variants with the scorecard; the Week 5
bridge), and `internal/C2_W04_SAT_sources_INTERNAL.md`.

**Completion criteria, all of them.** The paper's timed minutes land between 119 and 121 at the
builder's pace; about 60 percent of timed items are hard, each raised level carrying its reason in
`notes`; every one of the 43 bank items sits in a part, in `stretch_bank` or in `folded` with its
reason; every scenario set stays whole and in order; Part 2 carries the Tuesday items and the key lists
them as waiting for the tracker; the blanks answer from word banks and the pairs from match tables,
each bank with two unused options and no option keying two items; every part opens on a scenario and
an exhibit drawn only from its situation's numbers, set in Kalpa or at the week's named company with
the label line; every real-case item carries its R2 id in the source file's notes; item 41 prints the
reworded stem; the calendar trap is its own hard item with the festival dates on the page;
`scripts/distractor_audit.py` passes; the `--docx` build succeeds and `xlsx_recalc.py` passes on the
workbook; the eight briefs name the metric, the constraint and the error cost that change, and the
company briefs carry only R2 facts or labelled hypotheticals; the mock round sheet uses only the
transcripts' and variants' questions; `verify.py content/W04/SAT` and `sync_programme.py --check` pass
with outputs in the report; no plant is named in the paper that a lab note does not record as found.

## 7. WR, the week read and the print run (Wednesday 21 to Thursday 22 October, claude-opus-5-5)

**What it does.** Reads the six packs and the explorer in the order the room meets them, Monday
morning to Saturday close, as the trainer who did not write them. Checks: the week map's node texts on
each day equal the earlier days' facts; the crux lines each deck closes on are the ones the next day's
pre-read and the Saturday discussion repeat; every deck slide that names an explorer scene matches a
scene that exists; the Kahoot return questions chain Monday to Friday; the transcripts' follow-ups
appear on the Saturday round sheet; every URL carries a date and the ones used on each day were
re-fetched by that day's finishing session; every case carries its label line; no sentence claims a
company did the situation; Monday's and Thursday's `shared_constants` agree; the humanizer's read
across files reads as one house voice; the styles note is the real R3 and not the placeholder. Fixes
small things directly and records each in one line in
`content/W04/D1/internal/C2_W04_D01_week_read_INTERNAL.md`; anything larger goes back to the
orchestrator as a named finding. Builds the print pack: the twelve-row tables, Wednesday's cart packs,
the role cards, the scorecards, the festival calendar card, the paper and the key, as PDFs in each
file's own folder, and lists the print counts for 35 learners in nine groups (`facts.yaml`, `cohort`).

**Completion criteria.** Every check above is reported with its result; every fix is listed;
verify.py passes on all six folders and `sync_programme.py --check` passes; the print list exists; the
branch is pushed by Thursday 22 October.

## 8. What the orchestrating session does

Merges in order: S0 the same day it lands; wave 1's three drafts on Wednesday evening; wave 2's on
Friday evening; wave 3's on Sunday evening; wave 4's on Tuesday evening; WR on Thursday. Reviews each
pack against the spine's acceptance test in one read, fixes findings in one pass through the session's
branch or its own, opens the pull request, merges, and moves the board card (`board_sync.py --status
W04/D{d} review-1`, then onward to Done at the freeze). Sends the requester the Monday pack on
Friday 16 October evening as the first finished pack to read, and carries any change into the spine
and the remaining briefs before wave 3 starts, without gating wave 3 on it.

## 9. Risks, and the cut that answers each

| Risk | The cut |
|---|---|
| A case target cannot be shaped by a generator in a day | The case file's targets are ranges where they can be (the Kalpa contract lines already are); a session that cannot hit a point value within a day reports the nearest value it reached and the orchestrator re-keys the case file and the explorer's constants in one commit, never the session alone |
| A Kalpa plant cannot be shaped with v4 frozen | The case file names the fallback for each: Monday may re-date Retail-Plus orders inside the quarter under the full v4 contract; Thursday may define retention on app activity; both are recorded in the facts file, never silently |
| A drafting agent reloads the six-chapter habit or writes a stakeholder drama | The brief carries the ticket register, the ladder and the size limits; the finishing session reads every draft against them before building on it; acceptance lines 1, 3 and 16 cut what drifts |
| A session invents a number or a company fact | The facts-file and company-fact listings in every report, the ledger as the only source, the label line, the interviewer read's "claims a real company did something" check; a report without the listings is sent back |
| The drivers-at-peak guesstimate has no anchor | It ships with "to be found" and the case's synthetic check, as the house rule allows; the week read tries one more dated fetch |
| The explorer fails the sweep on a canvas scene or a rounding readout | The rules in spine section 11: inline SVG, a text readout per control, a step that moves a printed digit; the sweep runs after every scene is added, never only at the end |
| Two days disagree on a shared number (the Kalpa windows, Monday's numbers reused on Tuesday) | `shared_constants` asserted in both facts files; Tuesday copies by id; the week read checks both |
| mermaid-cli, LibreOffice, playwright or a Python package is missing in a session | `bash setup.sh` first; `html_sweep.py --install` for the browser; verify.py reports what it could not run and the report says so; S0 proves the picture path once |
| An IITGN block confirms, moves or is withdrawn | One edit to `facts.yaml` or the faculty workbook and one `sync_programme.py` reach every day sheet; the fallback deck already exists |
| The weekly usage limit runs out mid-build | At most three sessions run at once; the Saturday paper and the week read move first; the explorer moves last |
| R3 lands late | S0 writes the placeholder styles note; day sessions use spine section 2.4; the week read swaps in R3 |
| The paper runs long or short | The builder's minute table sizes it; folds and stretch moves adjust it before the docx is built |
