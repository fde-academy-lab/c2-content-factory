# Brief 2: Bookings fell in two cities in Q2

**For:** the group allocated sub-problem 2
**Client:** Dr Priya Menon, COO, Kalpa Health, and the clinics' operations head
**Read first:** `C2_W03_D01_briefing_note_STUDENT.md`

Kalpa Health and everyone in it are fictional.

---

## The question, as it was put

> "Bookings fell in two of our cities in Q2. Before I send a field team or cut staff there, I need to know how far they fell, and why."
> The clinics' operations head, Kalpa Health

## The decision it feeds

Whether the operations head sends a field team to the two cities, cuts staff there, or leaves them alone.
A fall read too large cuts staff a city still needs; a fall read too small leaves a real decline running
for another quarter.

## The symptom, as the business sees it

The operations head's report shows bookings down in two of the six cities from Q1 to Q2, and the
other four holding or growing. The operations head wants to act on it this month.

## The files that bear on it

- `C2_W03_D01_bookings_legacy_STUDENT.csv`
- `C2_W03_D01_bookings_newsys_STUDENT.csv`
- `C2_W03_D01_clinics_STUDENT.csv`
- `C2_W03_D01_booking_tests_STUDENT.csv`
- `C2_W03_D01_patients_STUDENT.csv`

Every group holds all ten files, and you may use any of them. The ones above are where this question
starts.

## What the panel will ask

The panel reads your one-slide answer and then asks questions like these. Every member should be able
to answer each one from your own work.

1. Which two cities, and how far did bookings fall in each, from which files?
2. How many bookings did you count in each quarter, from which files, and how does that count reconcile to the rows you were given?
3. What did you check before you started explaining the fall?
4. Which step of your investigation changed your answer most, and what did it change it from?
5. What should the operations head do next week, and what would change your advice?

## What your group ships

Every group ships the same five things, whatever its question.

| What | What it holds |
|---|---|
| A presentation slot of 25 to 30 minutes | Your answer to Dr Menon, a live demo run cold on your group's own copy of the Kalpa Health files, and the panel's questions. Every member answers; the panel may question anyone. |
| The one-slide answer | The slide Dr Menon carries into her board meeting, in four parts: the claim, the evidence, the caveat and the action. |
| The notebook or SQL | The code that reproduces every number on your slides from the raw files in `data/`, run top to bottom from a fresh start. A number the code does not produce is not in the answer. |
| The decisions log | Every cleaning and matching decision in the Week 1 Wednesday shape (field, issue, rows, decision, reason), with each file's row count reconciled: rows in equals clean plus removed. Use `C2_W03_D01_decisions_log_STUDENT.xlsx`. |
| The challenges log | Every time the group was stuck, what you tried and what you decided, dated as it happened. Use `C2_W03_D01_challenges_log_STUDENT.xlsx`; entry one goes in on Monday. |

The mini project carries 40 marks, and the presentation is part of them. The mock interview (30) and
the group discussion (30) are scored separately. The criteria the panel scores against reach you when
they are published.

## Before you open a file

Write Dr Menon's question in your own words and map it onto the method you already own, in
`C2_W03_D01_translation_worksheet_STUDENT.md`. Nobody hands you that mapping; making it is Monday's
work. The files and every column in them are described in `C2_W03_D01_data_dictionary_STUDENT.md`.
Nothing new is taught this week: everything you need is in your Weeks 1 and 2 notes.
