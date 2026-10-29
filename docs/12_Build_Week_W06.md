# The build pack, from Week 6 on

The requester's direction of 29 October 2026, recorded as decision `w6-build-pack` in
`data/programme/facts.yaml`. Build 1 failed for a reason a template could not fix: about 10,000 words
of briefs, a dictionary and worksheets went unread, ChatGPT read them instead, groups could not
explain their own numbers, and seven of ten presentation minutes went on re-explaining the problem.
From Build 2 on a build week ships one pack, handed out in one shot on its launch day, and a learner
opens four things all week. This file wins over the build-day folders of `content/README.md` and the
day-pack-builder skill for build weeks from Week 6 on; the teaching rules of CLAUDE.md and
`docs/11_Artifact_Set_W05.md` still hold. Week 3 keeps the shape it was built in.

## The folder

```
content/W06/D2/                         the launch day holds the whole build
  README.md                             the week's run table first, then every file in the order used
  1_project/                            STUDENT, printed: the ticket and the workbook, each .md and .pdf
  2_starter_repo/                       the template repo each group copies into its own repository
  3_explorer/                           the week's explorer, on the Week 5 kit
  4_trainer_only/                       run sheets, scripts, cards, the reference build, rubrics, sources
```

Files in `1_project/`, `3_explorer/` and `4_trainer_only/` carry the stem `C2_W06_D02_` and an
audience tag. Files in `2_starter_repo/` keep the names a real repository uses (`README.md`,
`src/score.py`, `requirements.txt`), because the learners copy the folder as it stands; they still
pass every writing rule. `scripts/verify.py content/W06/D2` checks this shape.

## The four things a learner opens

| What | Holds | Length |
|---|---|---|
| The ticket | Rohan's ask, the discovery-call guide, the group's constraint card space, the AI rules | Two printed sides |
| The workbook | One page per ladder stage, then the numbers passport, the twelve-minute run sheet, the challenges log and the AI log | About twelve printed pages |
| The starter repo | The breadcrumb notebook (the only notebook, from Tuesday), `src/`, a small demo app, README and model card templates, the seven-slide presentation template | A repository |
| The explorer | The story of an ML project from ask to production, the concept map, how-it-works pages, the leak exhibit, field scenes, an interview room that solves the ML system design walk step by step, check yourself | One HTML file |

## The ladder every artefact shares

| Stage | Name | The question it answers |
|---|---|---|
| 0 | The business, black box | Who pays, who decides, and what does a wrong call cost? |
| 1 | The frame | What is decided, from what is known when, about what outcome? |
| 2 | Requirements | What must the system do (FR), how well (NFR), within which limits, and under which security, privacy and governance rules? |
| 3 | Options | What are two ways to make the decision, what does each cost, which do we choose and what fact would flip it? |
| 4 | The POC | Does the chosen way beat doing nothing on the error bill, honestly measured? |
| 5 | The architecture | Black box to white box: the high-level design, then one box zoomed into its low-level design |
| 6 | The MVP slice | What is the smallest thing the client could use tomorrow, and what does production add? |
| 7 | Present and defend | Which one sentence would the client act on, and can every member defend every number? |

The workbook gives each stage one page, the breadcrumb notebook gives stages 1 to 6 their code with
sealed hints, the explorer teaches each stage on invented numbers and a worked parallel, and the run
sheet maps slides to stages.

## Rules a build pack keeps

- Data is public and downloaded in code, never generated; the client stays a Kalpa stakeholder.
- Notebooks ship executed; the breadcrumb notebook is executed through its first audit and carries
  `__TODO__` cells after that, measured as a TODO twin, with the reference build in `4_trainer_only/`
  as its executed solution twin.
- What the room is meant to find by sorting or reconciling is never named in a STUDENT file.
- The writing rules of CLAUDE.md, durations only, role labels in STUDENT files apart from Kalpa's
  people, every URL dated.
- Images: our own code draws data pictures and mermaid draws mechanisms; an openly licensed image
  (Creative Commons or public domain, from Wikimedia Commons or the like) may be used with its
  attribution line printed beside it (decision `w6-open-images`). Anything of unclear licence is
  redrawn.
- AI runs in two lanes: no AI for the frame on paper, the gate, the viva and the defence; AI allowed
  for code, logged in the AI log, and every AI-written line explained by the group before it is
  committed.

## Review

The builder's `python3 scripts/verify.py content/W06/D2` run, `scripts/html_sweep.py` and
`scripts/explorer_shots.py` on the explorer, and one read by the orchestrating session against the
approved plan in `docs/detailing/W06_build2_plan.md`.
