# Provenance: Week 0, Tuesday

INTERNAL.

## What the pack is built from

On 28 September 2026 the requester replaced the pack's own diagnostic with theirs and asked for
every file to follow. The instrument is the requester's: forty questions in five sections, 46
points, about 90 minutes, a first page that takes the learner's rating of five areas from 1 to 4
before any question, and a closing grid of ten statements about how the learner works.

| File | What it is |
|---|---|
| `paper/C2_W00_D02_diagnostic_STUDENT.docx` | The requester's paper version with its answer sheet, unchanged |
| `paper/C2_W00_D02_diagnostic_form_STUDENT.md` | The learner page with the form link and the rules, taken from the form's own description |
| `answer-key/C2_W00_D02_diagnostic_key_INTERNAL.xlsx` | The requester's key and profile workbook, unchanged: the key with a misconception for every option, the Entry, Scoring and Profile tabs, and the Dashboard with its band and brush-up inputs |
| `answer-key/C2_W00_D02_diagnostic_key_recalc_INTERNAL.md` | The pack's recalculation manifest for that workbook |
| `internal/C2_W00_D02_diagnostic_form_builder_INTERNAL.gs` | The requester's Apps Script that builds the form, scores each submission, writes the Profiles row and emails the report; it holds the key, so it is INTERNAL |
| `paper/C2_W00_D02_baseline_card_STUDENT.md` | The card, cut to the diagnostic's five rated areas, its 1-to-4 scale and its section totals |

The Tuesday row of `docs/curriculum/W0_Baseline_week.md` (tracker v7) still supplies the day's
purpose and its interview angle, and the student Week 0 sheet (version 2) the running order.

## Checked on 28 September 2026

| Check | What it settled |
|---|---|
| The form's respond link, loaded in session | It is live, titled "Baseline Diagnostic \| Cohort 2 \| Week 0", and loads without a sign-in |
| The Word paper against the builder script's item bank | Every one of the forty stems appears in both |
| `scripts/xlsx_recalc.py` through LibreOffice | The workbook computes; one entered answer sheet moves the profile, the brush-up call and the dashboard, and moving the Python cut moves the call |
| The builder script, read in full | Reports are emailed on submission with every explanation; a second submission is labelled as a repeat; the Profiles tab follows the Entry tab's column order from column C |

## Conflicts, and what the pack did

- **Kalpa in Week 0.** The diagnostic sets questions inside Kalpa Retail and introduces its four
  stakeholders, while the tracker keeps Kalpa for Week 1 Monday and client zero v2.2 brings the head
  of support in at Week 8. The requester keeps the diagnostic as written.
- **Week 1 and Week 2 moments.** Eleven items teach what the client zero ladder has the room find in
  Week 1 and Week 2: Q1 and Q22 (Monday), Q4, Q7, Q29, Q30 and Q32 (Tuesday), Q9 (Wednesday), Q27
  and Q31 (Thursday) and Q20 (Week 2 Tuesday). The report email explains all forty on submission.
  The requester chose to keep the emails and to rework Weeks 1 and 2 next.
- **The self-rating.** The row puts the self-rating on Monday; the diagnostic takes it on its first
  page, so Monday's paper form is retired and the card reads the diagnostic's ratings.
- **The brush-up tracks.** The workbook's Dashboard calls a Python score below 50 percent of the
  section a full brush-up. The pack maps a full call to Wednesday's taught track and a light call to
  the practice track.
- **The make-up.** Absentees sit the same form first thing on Wednesday, as the requester decided.

## The discussion threads

The requester asked, on 28 September 2026, for the diagnostic's model solutions to live on GitHub
Discussions only, with extended and simulated explanations, diagrams, history and context for every
question, the questions learners ask with their answers, and videos and reading at the end. The
seven posts in `study-notes/` are that deliverable, written to paste as they stand; the course
repository they will be posted to does not exist yet.

| Check | What it settled |
|---|---|
| Every Python item and every option, run in Python 3.11.15 | The outputs and error lines printed in the Section A threads |
| Every SQL item and every option, run in PostgreSQL 16.13 in a fresh database | The output blocks printed in the Section B thread, including the error texts |
| The arithmetic of Sections C and D, recomputed in Python | Every worked figure, the binomial table for Q25, the toy sampler for Q33, the Wilson interval for Q34 and the volume and price split for Q29 |
| Four research passes, one per section, each quote machine-checked against the page saved that day | Every quotation and every dated link in the threads |
| GitHub's documentation on creating diagrams, loaded in session | Diagram rendering is available in GitHub Discussions |
| GitHub's GraphQL guide for Discussions, loaded in session | A `createDiscussion` mutation takes a repository id, a category id, a title and a body |

Own constructions in the threads: the trace tables; the example rows in Q7 (three Plus orders of
Rs 1,000, Rs 700 and Rs 800); the two-city example in Q27; the toy model's scores in Q33 (2.0, 1.6
and 0.2); the 27-of-30 agreement example in Q34; the second look at Q29, which splits each tier's
change into a volume part and a price part; the model messages in Section E; and every practice line.

Not verified, and said so or left out of the threads: the running times and content of the videos
outside Section A (YouTube returned HTTP 429, so titles and channels came from its oEmbed endpoint);
the text of Codd's 1979 paper and of Bar-Hillel's 1980 paper, which the publishers refused; the DoPT
holiday memoranda on the department's own site, which refused the connection, so the scans hosted by
StaffNews were read; and who coined the terms fan trap and chasm trap.

## Findings on the diagnostic itself, reported and left unchanged

- In three items the key is the longest option on its own: Q9 (137 characters against 119 for the
  next), Q22 (73 against 72) and Q33 (144 against 140). Key positions are well spread otherwise, with
  A and B nine times each and C and D eight times each.
- The diagnostic introduces Farhan Sheikh as Head of Support, while client zero v2.2 brings that role
  in at Week 8.

## Retired from the pack

The pack's own four papers, their key, the score workbook with its builder and manifest, and the
earlier card. The papers use neutral data and spend nothing of Week 1, so they return in Thursday's
self-prep pack as a practice set.

## Not verified, and left for the team

- Who invigilates: the row names no invigilator, so the day sheet gives the steps without a role.
- Whether every learner's laptop reaches the form on the day; the paper copies cover a failure.
