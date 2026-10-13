# The coverage matrix

Every teaching day built from Week 4 on ships `internal/C2_W{ww}_D{dd}_coverage_INTERNAL.md`. It is
the day's contract with the curriculum row: every bullet of the row's Subtopics column, verbatim,
against where the pack teaches it, and every case chapter against the subtopics it applies.
`scripts/coverage_check.py` reads it inside `verify.py`. The day session writes the skeleton first
(`python3 scripts/coverage_check.py content/W{ww}/D{d} --matrix`), before any slide, and fills a row as
each family lands. The trainer day sheet prints the first table as its topic table.

## The shape

    # Coverage matrix, Week 4 Monday

    Row: docs/curriculum/W4_Analyst_craft.md, "Mon 26 Oct 2026 · Business metric design"
    Subtopics in the row: 6

    ## The row's subtopics and where each is taught

    | # | Subtopic (verbatim from the row) | Name in the chapter title and the notebook | Chapter | Slides | Notebook | Exercise items | Kahoot items | Minutes |
    |---|---|---|---|---|---|---|---|---|
    | 1 | What to measure and why; the proxy test | What to measure and why; the proxy test | SECTION 1: What to measure and why; the proxy test: what is a number for? | half1 S5 to S10 | notebooks/C2_W04_D01_01_proxy_test_STUDENT.ipynb | guided Q1; lab_set Q3 | Q5 | 13 |

    ## The case chapters and the subtopics each applies

    | Chapter | Applies (the # of each subtopic) | Slides | Notebook |
    |---|---|---|---|
    | SECTION 7: Twelve driver-weeks counted by hand: what does an hour count? | 1, 4 | half1 S38 to S46 | notebooks/C2_W04_D01_07_proxy_test_on_twelve_rows_STUDENT.ipynb |

## The columns

- **Subtopic**: the row's bullet, character for character, minus its bullet mark. A subtopic the
  spine adds that the row does not carry ends with "(added by the spine)" and has a reason in the
  sources list; one is allowed per day, and a row subtopic is never left out.
- **Name**: the subtopic in the row's words, which the chapter opener's topic and the notebook carry.
  It is the whole bullet, because the opener prints its topic in full and the pills print only its
  short question. It shortens only where one subtopic spans several chapters or two subtopics share
  one, and then it keeps every word that names an idea: Wednesday's "Support, confidence and lift,
  derived by counting" spans three chapters under the Name "Support, confidence and lift", and it may
  not shorten to "Support".
- **Chapter**: the `## SECTION n:` heading of a `slides/*half*_STUDENT.md` file, verbatim after
  whitespace is collapsed, written `SECTION n: <topic>: <short question>?`. The topic carries the
  Name; the short question starts lower-case, ends in a question mark and runs to about 24
  characters, since the pills, the footers and the cover's chapter strip print it. A topic with a
  colon of its own splits at the last colon, so the script reads everything before the last colon of
  a title that ends on a question as its topic. Two subtopics may share a chapter only when its topic
  carries both Names (Friday's chapter 4, "Beating the baseline; the vendor curve tested; the
  good-enough call and the forecast note", carries two). One subtopic may span several chapters,
  listed with semicolons, each entry starting with `SECTION` (Wednesday's "Support, confidence and
  lift" as three chapters whose topics are Support, Confidence, and Chance and lift), when each listed
  topic carries at least one idea-word of the Name and the topics together carry every idea-word. An
  idea-word is any word of the Name that is not a stop word (the, a, and, of, in, on, by, against,
  its, that, it, read, before), matched by prefix as the Notebook entry says.
- **Slides**: the deck and the slide numbers the chapter spans, `half1 S5 to S10` or a list such as
  `half1 S5, S7; half2 S40`; a number may name an `S` slide or a self-study `D` slide.
- **Notebook**: the path of the concept notebook, or several with semicolons where the subtopic spans
  several chapters, paired with the chapters in order. Its first markdown cell's first `# ` line starts
  with the Name or with its chapter's topic. Its file name's topic half carries the Name's idea-words
  in snake case: at least two of them (every one when the Name has fewer than three). A file-name
  token matches a Name word when the two are equal, or when either is a prefix of the other and the
  shorter has at least four letters (`guardrails` matches `guardrail`, `resistant` matches `resist`),
  so `02_north_star_guardrails` passes for "North-star and guardrail metrics" and
  `04_definition_lines` fails for "Definitions: numerator, denominator, window, exclusions", which
  it matches on "definition" alone. Across a spanning set, each file carries at least one idea-word
  and the set carries every one.
- **Exercise items**: at least one item, as `<file stem> Q<n>`, where the stem is any part of the
  file's path under `exercises/` (`guided`, `lab_set`, `proxy_test_set`), the file sits outside
  `solutions/`, and it holds a `## Q<n>` or `### Q<n>` heading; `Q1 to Q3` and `Q1, Q4` name several.
- **Kahoot items**: at least one `Q<n>` that exists in `kahoot/` as a `## Q<n>` or `### Q<n>` heading.
- **Minutes**: the chapter's live minutes; the first table's sum is the concept block.

In the second table, **Chapter** is a case chapter's `## SECTION n:` heading, verbatim, its topic the
case step with the subtopics it applies; **Applies** gives the numbers of the subtopics it applies,
from the first table's `#` column (`1, 4`, `2 to 5` or `all`); **Slides** and **Notebook** read as in
the first table, and a case chapter with no notebook writes `none`, which draws a warning, since
every case chapter pairs with one.

## What fails

A subtopic with no matrix row; a matrix row whose Subtopic is neither a row bullet nor marked "(added
by the spine)"; a matrix row with no chapter heading whose topic carries its Name, or no notebook
whose file name and first heading carry it; a slide, file or item named that does not exist, or a
cell still reading "to be filled"; a case chapter opener (any `## SECTION` of a half deck not named
in the first table) absent from the second table or applying no subtopic; two subtopics sharing a
chapter whose topic carries only one. The script also fails when it cannot find the row, the row's
Subtopics section or the matrix itself.

## What warns

A Name that keeps fewer than half the subtopic's idea-words; an opener named in the matrix whose
short question is missing or runs past about 24 characters; more than one subtopic marked "(added by
the spine)"; a case chapter with no notebook. The warnings go to the trainer's cold read, which
judges the quality of a name: the script proves presence by name and never edits a file.

## When the gate applies

From the week that decision `concept-first-case-second` in `data/programme/facts.yaml` names in its
`applies_from_week`, on every day whose kind in `data/programme/days.json` is `teaching`. Earlier
weeks, build weeks, Saturdays, Week 0 and holidays print an INFO line and pass.
