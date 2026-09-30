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

## The foundations guide, as chapters (30 September 2026)

On 30 September 2026 the requester supplied Cohort 2's foundations guide, "From the Diagnostic to
Week 1: the foundations guide", a 93-page PDF that is also the full model explanation of the
diagnostic, and asked for it to join the Week 0 pre-requisite reads chapter by chapter. The guide's
words are kept; conversion changed only what a markdown chapter needs.

| File in `study-notes/` | Guide pages | What it holds |
|---|---|---|
| `C2_W00_D02_foundations_00_map_STUDENT.md` | 1 to 6 | How to read the guide, the chapter table, the forty questions with links to Chapter 9 and to the discussion threads, and Figures 0 and 1 |
| `C2_W00_D02_foundations_01_python_STUDENT.md` | 7 to 14 | Chapter 1, Python, with mini project 1 |
| `C2_W00_D02_foundations_02_sql_STUDENT.md` | 15 to 21 | Chapter 2, SQL, with mini project 2 |
| `C2_W00_D02_foundations_03_numbers_STUDENT.md` | 22 to 28 | Chapter 3, Numbers, with mini project 3 |
| `C2_W00_D02_foundations_04_language_models_STUDENT.md` | 29 to 34 | Chapter 4, Language models, with mini project 4 |
| `C2_W00_D02_foundations_05_business_problems_STUDENT.md` | 35 to 40 | Chapter 5, Business problems and judgment, with mini project 5 |
| `C2_W00_D02_foundations_06_pandas_STUDENT.md` | 41 to 45 | Chapter 6, pandas, with mini project 6 |
| `C2_W00_D02_foundations_07_excel_STUDENT.md` | 46 to 48 | Chapter 7, Excel, with its hands-on |
| `C2_W00_D02_foundations_08_github_STUDENT.md` | 49 to 56 | Chapter 8, GitHub |
| `C2_W00_D02_foundations_09_diagnostic_worked_STUDENT.md` | 57 to 90 | Chapter 9, the forty questions worked, anchored `#q1` to `#q40` |
| `C2_W00_D02_foundations_10_path_STUDENT.md` | 91 to 93 | The path: videos, reading and the six mini projects as a week |

### How the conversion was checked

- Every figure became a mermaid fence, a table or a code block, and every mermaid fence rendered with
  mermaid-cli 11.17.0.
- Chapter 9's forty answers were compared with `answer-key/C2_W00_D02_diagnostic_key_INTERNAL.xlsx`
  (Key for Q1 to Q34, Best and Worst for Q35 to Q40), and all forty match. Its twenty code blocks were
  compared with the guide's code panels and its 160 options with the Word paper.
- Every link in the guide was opened on 30 September 2026; each chapter dates a source once, at its
  first mention, and points at the page the link now resolves to.

| Link as the guide gives it | On 30 September 2026 | Where it resolves |
|---|---|---|
| https://developers.google.com/machine-learning/crash-course | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://docs.github.com | Opens (HTTP 200), checked 30 September 2026 | https://docs.github.com/en |
| https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://docs.github.com/en/codespaces/getting-started/quickstart | Opens (HTTP 200), checked 30 September 2026 | https://docs.github.com/en/codespaces/quickstart |
| https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github | Opens (HTTP 200), checked 30 September 2026 | https://docs.github.com/en/account-and-profile/how-tos/account-management/creating-an-account-on-github |
| https://docs.python.org | Opens (HTTP 200), checked 30 September 2026 | https://docs.python.org/3/ |
| https://docs.python.org/3/tutorial/errors.html | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://freecodecamp.org/news/introduction-to-git-and-github | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://github.com | Opens through a direct fetch, checked 30 September 2026 | The page loads |
| https://github.com/skills/code-with-codespaces | Opens through a direct fetch, checked 30 September 2026 | Code with GitHub Codespaces and Visual Studio Code |
| https://learnsql.com | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://learnsql.com/blog/window-functions | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://nedbatchelder.com | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://nedbatchelder.com/text/names.html | Opens (HTTP 200), checked 30 September 2026 | https://nedbatchelder.com/text/names |
| https://pandas.pydata.org | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://pandas.pydata.org/docs/user_guide/10min.html | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://platform.claude.com/docs/en/build-with-claude/prompt-engineering | Opens (HTTP 200), checked 30 September 2026 | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview |
| https://platform.openai.com/docs/guides/prompt-engineering | Opens (HTTP 200), checked 30 September 2026 | https://developers.openai.com/api/docs/guides/prompt-engineering |
| https://plato.stanford.edu/entries/paradox-simpson | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://postgresql.org | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://postgresql.org/docs/current/tutorial-sql.html | Opens (HTTP 200), checked 30 September 2026 | The same page |
| https://support.microsoft.com | Opens (HTTP 200), checked 30 September 2026 | https://support.microsoft.com/en-us/ |
| https://support.microsoft.com/office/18fb0032-b01a-4c99-9a5f-7ab09edde05a | Opens (HTTP 200), checked 30 September 2026 | https://support.microsoft.com/en-us/excel/get-started/create-a-pivottable-to-analyze-worksheet-data |
| https://youtube.com/playlist?list=PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "Pandas Tutorials", Corey Schafer |
| https://youtube.com/watch?v=HXV3zeQKqGY | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "SQL Tutorial - Full Database Course for Beginners", freeCodeCamp.org |
| https://youtube.com/watch?v=HZGCoVF3YvM | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "Bayes theorem, the geometry of changing beliefs", 3Blue1Brown |
| https://youtube.com/watch?v=RGOj5yH7evk | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "Git and GitHub for Beginners - Crash Course", freeCodeCamp.org |
| https://youtube.com/watch?v=ZyhVh-qRZPA | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "Python Pandas Tutorial (Part 1): Getting Started with Data Analysis - Installation and Loading Data", Corey Schafer |
| https://youtube.com/watch?v=_AEJHKGk9ns | Confirmed by the author's own page, checked 30 September 2026 | https://nedbatchelder.com/text/names1.html, which names it "Python Names and Values", PyCon 2015, Montreal, 29 March 2015 |
| https://youtube.com/watch?v=wjZofJX0v4M | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "Transformers, the tech behind LLMs \| Deep Learning Chapter 5", 3Blue1Brown |
| https://youtube.com/watch?v=zjkBMFhNj_g | Opens (YouTube oEmbed, HTTP 200), checked 30 September 2026 | "[1hr Talk] Intro to Large Language Models", Andrej Karpathy |

### Where the chapters depart from the guide's text

- **Capitals restored.** The guide's layout lowercased the first letter after a colon in three
  places, printing "cOUNT(*)", "wHERE" and "nULL" in the map's question list and in the headings of
  Q13, Q15 and Q16. The chapters print "COUNT(*)", "WHERE" and "NULL", as the key's Concept tested
  column spells them.
- **Clipped text completed.** Figure 12's column header is cut off in the PDF at "ROW_NUMBER() OVER
  (PARTITION BY ticket_i" and is restored from the paragraph above it as `ROW_NUMBER() OVER
  (PARTITION BY ticket_id ORDER BY call_id DESC)`. Three clipped words are completed: "percent" in
  Figure 14, "city" in Figure 16 and "places" in Figure 28's lead-in.
- **One video title updated.** The guide calls 3Blue1Brown's video wjZofJX0v4M "But what is a GPT?
  Visual intro to transformers"; the chapters use its current title, as the link check above
  records it.
- **Links point where the pages now live.** Each link keeps the guide's anchor text and points at the
  address the check above resolved it to, and each chapter dates a source on every line it appears.
- **The map.** The exact word count is dropped, since conversion changes it; the reading times and the
  figure count are the guide's. A column links each question to its discussion thread in this folder.
- **The path.** The Build column names each mini project as its own chapter names it (projects 1, 4, 5
  and 6 were worded differently in the two places).
- **Figures.** Every figure is a mermaid fence, a table or a code block. Figure 14 draws its three bars
  as three boxes and Figure 19 its scores as one box, with every label and value kept; Figure 6's
  small highlight inside the JSON panel is not carried by the code block; Figure 25's ringed column is
  bold; the screen illustrations in Chapter 8 are mermaid windows. The rings, notes and title bars use
  the guide's own bronze and ink throughout.
- **Chapter 9's code.** Q11's call, which the PDF wraps inside a string, is one line, as the paper sets
  it, since a line break there would not be valid Python.

### Found in the guide and left as written

- **pandas in Week 1.** Chapter 6 says pandas replaces most of the loops "from Week 1 onward", places
  pandas in every Module 1 notebook, ties the chapter to "the Week 1 notebook where the room computes
  revenue by tier for Kalpa in six lines of pandas", and says time series, pivoting and plotting
  arrive in Week 1. The tracker's Week 1 rows stop before pandas, the built Week 1 keeps it closed,
  and Week 2 Thursday opens it. The Saturday readiness page says pandas and Excel arrive in Week 2.
- **Git in Week 1.** Chapter 8 says branches, pull requests and the Git command line arrive in Week 1,
  and that merge conflicts and pull request review are Week 1. No Week 1 row teaches them.
- **Marks.** Chapter 3 says "Marks were lost" of the diagnostic, while the diagnostic's own first page
  says the paper carries no marks; `scripts/verify.py` warns on the word.
