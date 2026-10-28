# W05 Tuesday: the financial services domain story (dossier, card, talk track)

You build one part of Week 5 Tuesday (3 November 2026) of the IITGN Cohort 2 PG Diploma in AI-ML
and Agentic AI Engineering, in /home/user/c2-content-factory: the financial services domain, which
enters the programme on this day (decision `four-domains` in `data/programme/facts.yaml`). Another
session builds the rest of Tuesday in the same folder at the same time; touch only your files.
Work in one long turn: nobody will answer questions, so decide within the rules and record each
decision in your sources file. Branch `w05-d2-domain`, cut from `origin/main`
(`git fetch origin main && git checkout -B w05-d2-domain origin/main`), pushed with
`git push -u origin w05-d2-domain`; small commits; never open, merge or close a pull request.

## Read first

1. `CLAUDE.md`, above all "From Week 5 on", and `docs/11_Artifact_Set_W05.md`.
2. `.claude/skills/day-pack-builder/references/domain-dossier.md` (the twelve sections) and the
   model dossier for retail, `content/W01/D1/study-notes/C2_W01_D01_domain_retail_STUDENT.md`.
3. `docs/07_Client_Zero.md` for Kalpa Financial Services and Rohan Desai, head of risk, and the
   Week 5 rows in `docs/curriculum/W5_ML_core_ME1.md` (Tuesday's transfer and Friday's) and Week 6
   (`docs/curriculum/W6_Build_2.md`, Build 2 in Kalpa Financial).
4. `docs/detailing/W05_ml_core_plan.md` and `docs/detailing/W05_research/W05_cases.md`.

## What you ship

- `content/W05/D2/3_study_material_for_students/C2_W05_D02_domain_financial_services_STUDENT.md`
  and its PDF: the dossier in the twelve sections, lean (about 3,500 words, far below the older
  6,000 to 8,000, because the requester wants less verbosity), visual first (a money-flow diagram
  of how a lender earns, a metric tree, who decides what as a table), each section opening on a
  relatable scene. It covers how Indian lending and payments make money, who asks for which number,
  the metrics as formulas (for example approval rate, default rate, gross NPA, cost of risk, net
  interest margin, collection efficiency), the language, the compliance that binds data (RBI's fair
  practices and digital lending rules, credit bureaus, KYC, India's Digital Personal Data
  Protection Act 2023), which real Indian companies Kalpa Financial is like, and where analytics, ML
  and agents pay. Every real fact comes from a source you fetch and date today; anything you cannot
  verify is left out or written as "not verified".
- `content/W05/D2/3_study_material_for_students/C2_W05_D02_financial_services_card_STUDENT.md` and
  its PDF: one printed page, the metric tree, ten metrics with formulas, twenty terms, the
  compliance lines, and the one picture.
- `content/W05/D2/4_trainer_only/C2_W05_D02_domain_story_TRAINER.md`: the talk track for a
  15-minute story told just before Tuesday's transfer chapter: what to say in what order, the
  question to ask the room at each turn, the one board drawing; bullets and a table.
- `content/W05/D2/4_trainer_only/C2_W05_D02_domain_sources_INTERNAL.md`: every source with its URL
  and the date checked, and a line per fact.

Print the two STUDENT files with `python3 scripts/build_doc.py <file.md>`. Formulas in plain text
or code spans, never LaTeX.

## Rules

Durations only, never clock times; role labels only in STUDENT files, Kalpa's fictional people the
one exception; Rs, never the rupee glyph; no em-dashes or en-dashes; none of Additionally,
Moreover, However, Hence, Thus, Nonetheless, Furthermore, Accordingly, Indeed, Dynamic,
comprehensive, robust, holistic, seamless, leverage as a verb; no "not X, but Y"; no logo; every
URL fetched today and dated. Run the humanizer skill's read on your prose.

## Finish

`python3 scripts/verify.py content/W05/D2` may report files the other session has not pushed yet;
make sure no failure names one of your four files. Push the branch. Report in under 250 words:
the files, the sources you relied on, and anything you could not verify.
