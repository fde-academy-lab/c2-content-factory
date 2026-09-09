# W1 Curriculum

## Mon 28 Sep 2026 · From setup to a first business answer: Python runs on real records

### Trainer agenda

1. A working notebook answers a business question on screen (10 min).
2. Environment: Codespace launch, the run loop, kernel state, restart and recover (50 min).
3. Types, comparisons, loops and accumulators, demonstrated on the records (50 min).
4. Guided build: threshold count and total, room mirroring (40 min).
5. Records as a list of dictionaries; lookups and .get() with a default (40 min).
6. Unguided: three counting questions, no hints, solution at close (30 min).
7. Kahoot and close-out (20 min).
Fixed content is about four hours; trainer discretion fills the rest.

### Learner outcome

UNDERSTANDS: the kernel holds state between runs, a value's type decides what operations mean, and a dataset is a list of named records.
CAN DO: launch the Codespace, run, edit and recover the notebook, and answer counting and total questions with a loop, a condition and an accumulator.
CAN HANDLE: a NameError from out-of-order cells, a TypeError from comparing '4500' with 3000, and a missing key via .get() with a stated default.
CAN DEFEND: what a kernel restart resets, and why refusing a cross-type comparison is safer than a spreadsheet quietly guessing.

### Subtopics

• Codespace launch and the VS Code layout
• Cells, the kernel, restart and run all
• str, int, float, bool and type()
• Comparison operators
• for loops; if, elif and else
• Count and sum accumulators
• Lists: index, slice, append
• Dictionaries: lookup by name, .get() with a default
• A dataset as a list of dictionaries

### Trainer notes

START FROM: zero on the environment. The entry requirement guarantees some programming in some language, so lean on that familiarity without assuming any Python.
GO AS FAR AS: every learner answers three counting questions on the records unaided and recovers a deliberately broken kernel.
STOP BEFORE: functions, comprehensions, files and any import statement.
COMES LATER: functions, errors and files tomorrow; the same records return in pandas and SQL in Week 2, so say the one-spine spiral aloud once today.
BREAKS TO RUN: NameError: name 'records' is not defined (cells out of order); TypeError: '>' not supported between instances of 'str' and 'int' (the planted text amount); KeyError against .get() on the optional field.
CUT FIRST if time slips: slicing extras, then negative indexing. Never cut the kernel recovery drill or the type break.

### Client zero and case studies

TODAY'S DATA: about 30 flat client-zero records loaded by a setup cell (an id, a segment, an amount, an outcome, a date; one amount planted as text). Entity and field names slot in once the scenario locks.
INTEGRATION: every demo and exercise answers one operational question on these records, so the scenario is the classroom rather than a slide.
COMPETENCY BUILT: read the records and answer a counting question unaided; step one of the week's arc (read, clean, profile, describe).
CASE: Mars Climate Orbiter, 1999. A value crossed a system boundary in the wrong unit, nothing validated it, and the mission (about USD 327 million) was lost. Today's type discipline is the small version of that lesson.

### In-session exercises

GUIDED: the trainer builds the threshold count and total step by step; every learner mirrors on their own Codespace.
UNGUIDED: three counting and total questions on the same records, no hints, attempted in session, solution released at close.
MID-SESSION (15 min each): predict the output of three short cells before running them; find the mistake in a loop with a misplaced accumulator.

### After-class tasks

• BUILD: extend the unguided counter to report two buckets, above and below the threshold, plus one markdown cell explaining the planted text-amount bug in your own words.
• WATCH: Corey Schafer's dictionaries video before tomorrow (link in student references).
• SETUP: nothing to install; the Codespace opened today is the environment all programme.

### Trainer resources

• GitHub Docs, Codespaces with Jupyter quickstart (verified 03 Sep 2026):
https://docs.github.com/en/codespaces/developing-in-a-codespace/getting-started-with-github-codespaces-for-machine-learning
• VS Code docs, notebooks on the web and in Codespaces (verified 03 Sep 2026):
https://code.visualstudio.com/docs/datascience/notebooks-web
• Corey Schafer, Python beginner playlist, videos 1 to 7 for teaching order and illustrations (verified 03 Sep 2026):
https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7
• Automate the Boring Stuff, 3rd edition, Ch 1 to 3 for pacing a from-scratch room (verified 03 Sep 2026):
https://automatetheboringstuff.com/3e/
• GeeksforGeeks, Python interview questions, mine the entry items on types (verified 03 Sep 2026):
https://www.geeksforgeeks.org/python/python-interview-questions/

### Student references

• Corey Schafer, Lists, Tuples and Sets (verified 03 Sep 2026):
https://www.youtube.com/watch?v=W8KRzm-HUcc
• Corey Schafer, Dictionaries (verified 03 Sep 2026):
https://www.youtube.com/watch?v=daefaLgNkw0
• Automate the Boring Stuff, 3rd edition, Ch 2 and Ch 3 (verified 03 Sep 2026):
https://automatetheboringstuff.com/3e/

### Kahoot quiz plan

• Q1 trap: is '10' > 9 True, an error, or it depends (type before size)
• Q2: cells ran in order 3, 1, 2; which error appears and why (kernel order)
• Q3: predict the accumulator total after the three records shown
• Q4: type('4500') against type(4500)
• Q5: rec.get('discount', 0) on a record without the key returns what
• Q6: what a kernel restart erases and what stays on disk
• Q7 trap: b = a; b.append(9); what is len(a) now
• Ungraded; a performance indicator read for attention and retention. No return question on Day 1; today's traps seed tomorrow's.

## Tue 29 Sep 2026 · Package the logic, survive bad data, cross the file boundary

### Trainer agenda

1. clean_record shown working three times on defective records (10 min).
2. Functions: def, parameters, return against print; refactor yesterday's cells live (50 min).
3. Tracebacks read bottom-up; try/except on named errors; raise; the rejects log (50 min).
4. Guided: carve normalise_amount out of the inline code, then wrap it (40 min).
5. Files: with open, csv.DictReader, json.load; the everything-is-text rule; write clean and rejects files (60 min).
6. Unguided AI-free lab: read a fresh CSV, clean it, write both outputs (40 min).
7. Kahoot and close-out (20 min).
Comprehensions appear once as a one-line variant of the loop, no deeper.

### Learner outcome

UNDERSTANDS: a function packages one reusable decision with a returned output, an error is a signal to read, and a file format is an agreement about structure.
CAN DO: refactor repeated cells into functions, catch a named exception narrowly, log every rejection with a reason, and run read-clean-write across CSV and JSON.
CAN HANDLE: a print-only function that hands the caller None, a ValueError from int('twelve'), a wrong path, and a JSON file that fails to parse at a named line.
CAN DEFEND: why a bare except that produces a plausible wrong total is worse than a crash, and why the rejects file is part of the job.

### Subtopics

• def, parameters and return; return against print
• Scope in one sentence
• A list comprehension as the compact loop
• Reading a traceback bottom-up
• try/except on named exceptions; raise with a message
• Validate early, catch narrowly, log rejections
• open, read, write and the with block; paths
• csv.DictReader and the header row
• json.load and json.dump
• Converting columns on purpose
• Writing the clean file and the rejects log

### Trainer notes

START FROM: they loop, branch and read records by name (Day 1) and have already watched three tracebacks land, so errors are familiar sights rather than a new scary topic.
GO AS FAR AS: every learner ships clean_record and completes the AI-free read-clean-write lab with both output files reopening correctly.
STOP BEFORE: custom exception classes, *args and **kwargs, lambdas, imports beyond csv and json, encodings beyond one mention, anything pandas.
COMES LATER: the full-dataset cleaning pass tomorrow reuses today's functions unchanged, which is the payoff to promise aloud; pandas re-expresses all of it in Week 2.
BREAKS TO RUN: TypeError: 'NoneType' object is not subscriptable (the print-only function); ValueError: invalid literal for int() with base 10: 'twelve', then the bare except that swallows it and yields a wrong total; FileNotFoundError: [Errno 2] No such file or directory: 'data/orderz.csv'. The JSONDecodeError (line and column named) sits in the exercise.
CUT FIRST if time slips: the comprehension variant, then json.dump (write CSV only). Never cut the bare-except demonstration or the rejects log.

### Client zero and case studies

TODAY'S DATA: the same records grow two planted defects (an amount spelled 'twelve', a missing required field) and then leave the setup cell to become two real files, one CSV and one JSON with a nested sub-record and one truncated line.
INTEGRATION: the functions carved today are named for the scenario's cleaning steps and are called unchanged tomorrow.
COMPETENCY BUILT: clean one record defensibly and move data across the file boundary both ways; step two of the arc.
CASES: Knight Capital, 1 Aug 2012, about USD 440 million lost in 45 minutes to a bad deployment reusing an old flag, the argument for failing loudly and validating early. Public Health England, Oct 2020, 15,841 COVID cases dropped when a CSV-to-XLS conversion hit the old row limit, the argument for knowing a file format's contract.

### In-session exercises

GUIDED: carve normalise_amount out of yesterday's inline code together, then wrap the conversion in try/except and start the rejects list.
UNGUIDED (AI-free lab): read a fresh defective CSV cold, clean it with today's functions, write clean.csv and rejects.csv, and reopen both to prove they parse.
MID-SESSION (15 min each): trace three function calls on paper and state what each returns; given a JSONDecodeError message, open the file at the named line and mark the defect.

### After-class tasks

• BUILD: rerun the full read-clean-write on a third provided file with new defects; the rejects log must state a reason per rejection.
• READ: skim Automate the Boring Stuff 3e, Ch 10, reading and writing files.
• RECAP: one markdown cell contrasting the honest crash with the silent wrong total, in your own words.

### Trainer resources

• Corey Schafer, Functions (verified 03 Sep 2026):
https://www.youtube.com/watch?v=9Os0o3wzS_I
• Corey Schafer, try/except blocks (verified 03 Sep 2026):
https://www.youtube.com/watch?v=NIWwJbo-9_8
• Real Python, LBYL against EAFP, the two defensive stances (verified 03 Sep 2026):
https://realpython.com/python-lbyl-vs-eafp/
• Corey Schafer, CSV module (verified 03 Sep 2026):
https://www.youtube.com/watch?v=q5uM4VKywbA
• Real Python, Reading and Writing CSV Files (verified 03 Sep 2026):
https://realpython.com/python-csv/
• Official json docs, JSONDecodeError behaviour, current docs cover Python 3.14 (verified 03 Sep 2026):
https://docs.python.org/3/library/json.html

### Student references

• Corey Schafer, Working with JSON data (verified 05 Sep 2026):
https://www.youtube.com/watch?v=9N6a-VLBa2I
• Automate the Boring Stuff, 3rd edition, Ch 4 and Ch 10 (verified 03 Sep 2026):
https://automatetheboringstuff.com/3e/
• Official Python tutorial, Errors and Exceptions (verified 03 Sep 2026):
https://docs.python.org/3/tutorial/errors.html

### Kahoot quiz plan

• Q1: result = fix(record) prints and returns nothing; what does result hold
• Q2: read a four-line traceback and name the failing line
• Q3 trap: except: pass around int(value); what does the total look like
• Q4: which exception does int('twelve') raise
• Q5: with open against open and close by hand; what is guaranteed
• Q6: DictReader keys come from where
• Q7: the vendor's JSON fails at line 47 column 5; what is your first move
• Return question from Monday, one level up: a comparison fails mid-loop on record 17 of 30; name your first two checks.

## Wed 30 Sep 2026 · Profile before you touch: load, clean and defend a real dataset

### Trainer agenda

1. Two profile printouts on screen: which dataset would you trust, and why (10 min).
2. The profiler: presence, convertibility and distinct counts per field, grown from Monday's counter (45 min).
3. Missingness as a per-field decision: drop, default, or keep and flag, each with a written reason (40 min).
4. Coercion at dataset scale, reusing Tuesday's convert-or-reject functions (30 min).
5. Duplicates and the identity rule; the whole-record check that misses the planted pair (45 min).
6. Outlier detection: sorted tail, a simple fence, and the keep-or-investigate decision (30 min).
7. Unguided full pass producing the profiled dataset and decisions log; Kahoot and close (40 min).

### Learner outcome

UNDERSTANDS: profiling comes before cleaning, every cleaning act is a recorded decision, duplicates need a stated identity rule, and an outlier is a finding to investigate before it is a row to delete.
CAN DO: profile a dirty dataset field by field, run the full clean, and produce the Week 1 profiled-dataset artifact with a decisions log a reviewer could follow.
CAN HANDLE: a near-duplicate pair that a whole-record check misses, a column where several values fail conversion, and reconciling input count against clean plus rejected.
CAN DEFEND: one drop, fill or keep decision aloud, and who decides when two records share an id and disagree.

### Subtopics

• Profiling before analysing: presence, type convertibility, distinct counts per field
• Missing values and the three-way decision
• Mixed and wrong types at dataset scale
• Duplicate detection and the identity rule
• Outlier detection with sorted values and a simple fence
• The decisions log
• Reconciling counts: input equals clean plus rejected

### Trainer notes

START FROM: they read files, clean single records with functions and keep a rejects log (Tuesday). Open with Monday's presence counter on screen; today's profiler is that counter grown up.
GO AS FAR AS: every learner ships the profiled dataset, the decisions log and a reconciled count, and defends one decision aloud.
STOP BEFORE: imputation beyond a stated default, statistical outlier theory, standard deviation arithmetic, anything pandas.
COMES LATER: descriptive statistics tomorrow run on today's cleaned output; pandas re-expresses this pass in Week 2 (isna, duplicated, to_numeric). Say the spiral aloud.
BREAKS TO RUN: both are wrong-output failures rather than crashes. The whole-record dedupe reports 0 while the distinct-id count disagrees, forcing an identity rule. A coerce-everything pass hides real defects unless conversion failures are counted separately.
CUT FIRST if time slips: the outlier fence arithmetic (flag by sorted tail only). Never cut the decisions log or the count reconciliation.

### Client zero and case studies

TODAY'S DATA: the full client-zero dataset at its dirtiest: the near-duplicate pair (same id, one differing field), one extreme whale amount, text-typed values and the absent optional field. Every planted defect witnesses exactly one teaching point.
INTEGRATION: the day's single question is how many usable records the scenario actually has, and the answer becomes the input to Thursday's statistics.
COMPETENCY BUILT: take a dataset nobody prepared to a defensible cleaned state with an audit trail; step three of the arc and the first portfolio-grade act.
CASE: HGNC, 2020, formally renamed about 27 human genes because spreadsheets silently coerced names like SEPT1 to dates, after a 2016 audit found gene-name errors in roughly a fifth of genetics papers with spreadsheet supplements. Silent coercion at scale is a real, published failure mode.

### In-session exercises

GUIDED: grow Monday's presence counter into a per-field profiler together, then walk one missingness decision end to end with its written reason.
UNGUIDED: run the full profile-then-clean pass, produce the decisions log, and reconcile input against clean plus rejected, no hints, solution at close.
MID-SESSION (15 min each): given two profile printouts, choose the trustworthy dataset and say why; classify four missingness cases as drop, default, keep-and-flag or escalate.

### After-class tasks

• MINI-BUILD: wrap today's work into a reusable profile_dataset() and run it on a second provided file, shipping its profile and decisions log.
• WATCH: Khan Academy on mean, median and mode before tomorrow (link in student references).
• RECAP: two markdown lines defending your duplicate identity rule.

### Trainer resources

• Real Python csv module reference, DictWriter for the cleaned output (verified 03 Sep 2026):
https://realpython.com/ref/stdlib/csv
• GeeksforGeeks, Data Analyst interview questions, cleaning, missing values and duplicates items (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/
• LearnPython, 15 Python questions for data analysts, the try/except and cleaning items (verified 03 Sep 2026):
https://learnpython.com/blog/python-interview-questions-for-data-analyst/

### Student references

• Automate the Boring Stuff, 3rd edition, Ch 18, CSV, JSON and XML (verified 03 Sep 2026):
https://automatetheboringstuff.com/3e/
• LearnPython, 15 Python questions for data analysts, attempt before peeking (verified 03 Sep 2026):
https://learnpython.com/blog/python-interview-questions-for-data-analyst/

### Kahoot quiz plan

• Q1: profile before clean; name the three counts the profiler reports per field
• Q2: the dedupe says 0 and distinct ids say 47 of 50; what happened
• Q3 trap: coerce every failure to a default and the dataset looks clean; what got lost
• Q4: drop, default, keep-and-flag: match each to its one-line reason
• Q5: 40 records dropped; where must that fact be written
• Q6: the whale amount survives cleaning; why
• Return question from Tuesday, one level up: the loop finished with zero rejects on a file you know is dirty; name the two most likely causes.

## Thu 01 Oct 2026 · Describe without misleading: typical, spread, skew and the segment summary

### Trainer agenda

1. Two true claims from the same cleaned data disagree on screen; which is honest (10 min).
2. Mean, median and mode by hand on seven values, then in code on the full column (45 min).
3. The whale: watch the mean leave every ordinary record behind, investigate the sorted tail (35 min).
4. Spread and shape: min, max, range, the fence from yesterday, skew read off sorted values (40 min).
5. Sampling and sample size: the same rate from 12 records and from 1,200 (30 min).
6. Guided then unguided: the segment summary (count, median amount, outcome rate per segment) via dictionary accumulators (60 min).
7. Kahoot and close-out; the week's paper-test slot cannot run tomorrow, so flag its placement (20 min).

### Learner outcome

UNDERSTANDS: mean, median and mode answer what-is-typical differently, spread and shape decide which is honest, and a rate is only as trustworthy as its sample size.
CAN DO: compute typical and spread by hand and in code, read skew off sorted values, and build the segment summary artifact with dictionary accumulators.
CAN HANDLE: a correct mean that describes the data wrongly because of one whale record, and a small segment whose impressive rate rests on a dozen records.
CAN DEFEND: the number given to a stakeholder who asks for the average order value when one enormous order sits in the data, and the sentence that goes with it.

### Subtopics

• Central tendency: mean, median, mode
• The outlier's pull on the mean
• Spread: min, max, range and a simple fence
• Distribution shape and skew from sorted values
• Sampling and sample size
• When an average misleads
• The segment summary via dictionary accumulation
• Every reported rate carries its denominator

### Trainer notes

START FROM: they own a cleaned dataset with a decisions log (Wednesday). Compute on the cleaned data only; describing dirty data would contradict yesterday and the room will notice.
GO AS FAR AS: every learner ships the segment summary and writes one honest sentence per segment, each with its denominator.
STOP BEFORE: standard deviation arithmetic, distribution theory, chart libraries, hypothesis language. The question of whether a segment gap is real is named and parked for Monday.
COMES LATER: Monday of Week 2 turns today's segment gap into a formal test; Week 2's pandas groupby automates exactly the accumulator built today, which is why it is built by hand once.
BREAKS TO RUN: a wrong-output failure: the computed mean sits far above every visible record; the room disbelieves it, sorts the column, and finds the whale. The number was right and the description was wrong.
CUT FIRST if time slips: the fence arithmetic, then mode. Never cut the hand computation on seven values or the sample-size contrast.

### Client zero and case studies

TODAY'S DATA: the cleaned client-zero amounts and outcomes, including the whale that survived cleaning because it is real, and one small segment planted to make sample size bite.
INTEGRATION: the segment summary answers the scenario's first stakeholder question, and the gap between two segments becomes Monday's test case.
COMPETENCY BUILT: describe a dataset honestly, per segment, with denominators; step four of the arc.
CASES: Anscombe's quartet, 1973, four datasets sharing near-identical summary statistics while looking completely different, the standing argument that a summary can mislead. Statistical agencies report median household income rather than the mean because top incomes drag the mean; the same convention applies to any money field.

### In-session exercises

GUIDED: compute mean and median on seven hand-checkable values on paper, reproduce in code, then build the first segment's summary together.
UNGUIDED: complete the full segment summary and write one honest sentence per segment with its denominator, no hints, solution at close.
MID-SESSION (15 min each): four datasets described only by mean-and-median pairs, infer which hide an extreme; pick the honest statistic for four data shapes and justify.

### After-class tasks

• EXTEND: rebuild the segment summary over a second field and flag any segment whose rate rests on fewer than 30 records.
• WATCH: the Seeing Theory frequentist inference chapter before Monday (link in student references).
• RECAP: one markdown cell on when the mean is the honest choice.

### Trainer resources

• Khan Academy, mean, median and mode, video (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/v/mean-median-and-mode
• Khan Academy, mean, median and mode review with worked values (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/mean-median-basics/a/mean-median-and-mode-review
• Khan Academy, summarizing quantitative data unit, spread and outlier material for stretch (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data

### Student references

• Khan Academy, summarizing quantitative data unit with practice items (verified 03 Sep 2026):
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data
• Seeing Theory, frequentist inference chapter, interactive preview for Monday (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html

### Kahoot quiz plan

• Q1: seven sorted values on screen; give the median without computing
• Q2: one value becomes 100x larger; which moves, mean or median
• Q3 trap: segment A converts at 42 percent on 12 records, segment B at 31 percent on 1,200; which claim do you trust
• Q4: read the skew from a sorted tail
• Q5: the honest statistic for a money field with whales
• Q6: every rate must carry what beside it
• Return question from Wednesday, one level up: two records share an id and differ in one field; what do you do and who decides.

## Fri 02 Oct 2026 · Gandhi Jayanti: institute holiday, no session

### Trainer agenda

No session. Gandhi Jayanti is a gazetted national holiday and the institute is closed. Teaching for Week 1 ends Thursday.

### Learner outcome

No new outcomes. The optional self-paced work consolidates the four teaching days.

### Subtopics

None scheduled.

### Trainer notes

Nothing to deliver. The weekly pen-and-paper test cannot run today; whether it lands in Saturday's block or shifts is a Programme Head call, and no marks are stated either way since its graded status is pending.

### Client zero and case studies

The scenario rests. Learners who do the optional rerun touch the whole week's pipeline end to end.

### In-session exercises

None scheduled.

### After-class tasks

• OPTIONAL rerun: the whole week's pipeline top to bottom in a fresh Codespace; note anything that fails cold.
• OPTIONAL watch: the Seeing Theory frequentist inference chapter, ahead of Monday.

### Trainer resources

None needed.

### Student references

• Seeing Theory, frequentist inference chapter, interactive (verified 05 Sep 2026):
https://seeing-theory.brown.edu/frequentist-inference/index.html

### Kahoot quiz plan

None.

## Sat 03 Oct 2026 · Saturday recap: the pen-and-paper test, then the interview-answer discussion

### Trainer agenda

Four hours, no new content.
1. Weekly recap test: pen and paper, AI-free, built from the week's interview question set, short-answer format (120 min).
2. Break (20 min).
3. Solution discussion led by the Academic TA: papers swapped for peer cross-evaluation, every answer discussed as an interview answer, random call-outs throughout (75 min).
4. Doubt clearing and the bridge: the same records return in SQL and pandas next week (25 min).

### Learner outcome

CAN DO: answer the week's interview set on paper, without an assistant, in short-answer form.
CAN DEFEND: any of those answers aloud when called, and mark a peer's paper against the discussed solution.
STATUS: ungraded; the score is a performance indicator the programme reads, never a marks component.

### Subtopics

THE QUESTION SET (questions only; answers are built at the detailing phase):
• [S] A list against a dictionary: when do you reach for each?
• [S] b = a, then b.append(9): what happens to a, and how do you copy on purpose?
• [S] How do you read a Python traceback, and what do you look at first?
• [F] Why is a bare except worse than letting the code crash?
• [S] Everything read from a CSV is a string: what breaks, and where do you convert?
• [F] CSV or JSON for nested records, and what does flattening cost?
• [SV] Mean or median for a money field, and why?
• [D] Your cleaning run reported zero rejects on a file you know is dirty: what do you check?
Tags: [S] staple asked everywhere · [F] frequent in GCC and product screens · [SV] service-major screen opener · [D] differentiator. The tagging is this programme's own calibration for 0-3 year Indian-market candidates.

### Trainer notes

FORMAT: the paper is built from this row's question set, framed for short answers (selection, one-liners, small computations) so peer cross-checking works; answers themselves are written at the detailing phase, never improvised on the day.
DISCUSSION: papers swap for peer cross-evaluation; the Academic TA leads the solution walk-through as an interview-answer discussion, with random call-outs throughout.
STATUS: ungraded, a performance indicator rather than a marks component, and AI-free by format.

### Client zero and case studies

Answers must cite the scenario's own numbers and artifacts where the week produced them; the whole Week 1 pipeline is the reference.

### In-session exercises

• The two-hour recap test on paper.
• Peer cross-evaluation against the discussed solution.
• Random call-outs: the called learner answers aloud in sixty seconds.

### After-class tasks

• RECAP: rewrite any question you lost marks on, one line each, in your own words.

### Trainer resources

• This row's question set is the paper's source; the verified interview banks on the weekday rows calibrate difficulty.
• GeeksforGeeks, Data Analyst interview questions (verified 03 Sep 2026):
https://www.geeksforgeeks.org/data-analysis/data-analyst-interview-questions-and-answers/

### Student references

• Reread the week's tabs and your own rejected answers; the next paper reuses missed ground one level up.

### Kahoot quiz plan

None. The recap test and the discussion replace the quiz today.
