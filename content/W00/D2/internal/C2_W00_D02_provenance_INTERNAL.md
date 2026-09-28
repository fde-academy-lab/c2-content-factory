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

## Retired from the pack

The pack's own four papers, their key, the score workbook with its builder and manifest, and the
earlier card. The papers use neutral data and spend nothing of Week 1, so they return in Thursday's
self-prep pack as a practice set.

## Not verified, and left for the team

- Who invigilates: the row names no invigilator, so the day sheet gives the steps without a role.
- Whether every learner's laptop reaches the form on the day; the paper copies cover a failure.
