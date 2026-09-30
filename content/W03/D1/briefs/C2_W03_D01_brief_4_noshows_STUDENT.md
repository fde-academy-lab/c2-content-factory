# Brief 4: The no-show rate looks worse at one patient service centre

**For:** the group allocated sub-problem 4
**Client:** Dr Priya Menon, COO, Kalpa Health, and the patient service centres' operations head
**Read first:** `C2_W03_D01_briefing_note_STUDENT.md`

Kalpa Health and everyone in it are fictional.

---

## The question, as it was put

> "KH-ATL-03 has the worst no-show rate on my monthly report. I am being asked to add a receptionist there or close it. Is the centre really worse?"
> The patient service centres' operations head, Kalpa Health

## The decision it feeds

Whether KH-ATL-03 gets a second receptionist, a change to its reminder calls, or a closure notice. A
centre closed on a rate read wrongly loses a neighbourhood its centre; a real problem left
alone keeps costing slots every day.

## The symptom, as the business sees it

The operations head's monthly report ranks the twelve patient service centres by no-show rate for Q3,
and KH-ATL-03 sits at the bottom. The centre's manager says their patients are no different from anyone
else's.

## The files that bear on it

- `C2_W03_D01_appointments_STUDENT.csv`
- `C2_W03_D01_sites_STUDENT.csv`

Every group holds all ten files, and you may use any of them. The ones above are where this question
starts.

## What the panel will ask

The panel reads your one-slide answer and then asks questions like these. Every member should be able
to answer each one from your own work.

1. What is KH-ATL-03's no-show rate, on what denominator, and against which comparison?
2. Could chance alone produce the gap you see? How did you check, and what did the check say?
3. What would a fair comparison between two centres need, and did yours have it?
4. What should the operations head do about KH-ATL-03, and what evidence would change your advice?
5. If a patient's missed test were a missed diagnosis, what would you want checked before acting?

## What your group ships

Every group ships the same five things, whatever its question.

| What | What it holds |
|---|---|
| A presentation slot of 25 to 30 minutes, on Friday 23 October where the roster allows or on Saturday 24 October | Your answer to Dr Menon, a live demo run cold on your group's own copy of the Kalpa Health files, and the panel's questions. Every member answers; the panel may question anyone. |
| The one-slide answer | The slide Dr Menon carries into her board meeting, in four parts: the claim, the evidence, the caveat and the action. |
| The notebook or SQL | The code that reproduces every number on your slides from the raw files in `data/`, run top to bottom from a fresh start. A number the code does not produce is not in the answer. |
| The decisions log | Every cleaning and matching decision in the Week 1 Wednesday shape (field, issue, rows, decision, reason), with each file's row count reconciled: rows in equals clean plus removed. Use `C2_W03_D01_decisions_log_STUDENT.xlsx`. |
| The challenges log | Every time the group was stuck, what you tried and what you decided, dated as it happened. Use `C2_W03_D01_challenges_log_STUDENT.xlsx`; entry one goes in on Monday. |

The mini project carries 40 marks, and the presentation is part of them. The panel scores it
against this rubric:

<!-- sync:rubric:W03/mini-project -->
**Mini project, 40 marks.** The first four criteria are scored once for the group, and every member receives those 34 marks; presentation and defence is scored for each learner on 6 marks, so a silent teammate cannot ride the group's score.

| Criterion | Marks | What full marks look like |
|---|---|---|
| The question translated | 8 | Dr Menon's words are mapped to the right Weeks 1 and 2 method, with the metric defined and the decision it feeds named. |
| The data made trustworthy | 10 | The data is profiled before it is touched, every cleaning call is in the decisions log with its reason, and counts and dollars reconcile across files. |
| The analysis | 10 | The tree, ladder or fair comparison reaches the branch that explains the symptom, on the right denominator, with a chance test where one is needed. |
| The claim | 6 | One sentence carries its number, denominator, period and caveat, plus an action Dr Menon can take. |
| Presentation and defence | 6 | The live demo runs cold, and every member answers a challenge on the caveat. |
<!-- /sync:rubric:W03/mini-project -->

The presentations run on Friday 23 October where the roster allows and on Saturday 24 October, when
every Build 1 grade closes. The mock interview (30) and the group discussion (30) are scored
separately: Mock R1 runs for every learner on Thursday 22 October, and the GD rounds run on Friday 23
October and close on the morning of Saturday 24 October. The briefing note carries their rubrics.

## Before you open a file

Write Dr Menon's question in your own words and map it onto the method you already own, in
`C2_W03_D01_translation_worksheet_STUDENT.md`. Nobody hands you that mapping; making it is Monday's
work. The files and every column in them are described in `C2_W03_D01_data_dictionary_STUDENT.md`.
Nothing new is taught this week: everything you need is in your Weeks 1 and 2 notes.
