# Brief 3: Invoices and collections disagree

**For:** the group allocated sub-problem 3
**Client:** Dr Priya Menon, COO, Kalpa Health, and the finance head
**Read first:** `C2_W03_D01_briefing_note_STUDENT.md`

Kalpa Health and everyone in it are fictional.

---

## The question, as it was put

> "The invoices say one thing and the collections say another. Which invoices are unpaid, how much money is that, and can I trust the figure I report?"
> The finance head, Kalpa Health

## The decision it feeds

The collections figure the finance head reports at the quarter's close, which accounts the team
chases, and whether anything is written off. A figure that is wrong in either direction reaches the board
under the finance head's name.

## The symptom, as the business sees it

The billing export and the payment feed give different totals for the same two quarters, and the
finance head cannot say which invoices make up the difference.

## The files that bear on it

- `C2_W03_D01_invoices_STUDENT.csv`
- `C2_W03_D01_payments_STUDENT.csv`
- `C2_W03_D01_bookings_legacy_STUDENT.csv`
- `C2_W03_D01_bookings_newsys_STUDENT.csv`
- `C2_W03_D01_patients_STUDENT.csv`

Every group holds all ten files, and you may use any of them. The ones above are where this question
starts.

## What the panel will ask

The panel reads your one-slide answer and then asks questions like these. Every member should be able
to answer each one from your own work.

1. How many invoices are fully paid, part paid and unpaid, and what is each group worth in rupees?
2. How did you match a payment to its invoice, and how many payments matched?
3. Where did every payment row go? Show rows in against rows matched, set aside and unexplained.
4. Which collections figure should the finance head report, and which caveat travels with it?
5. What would you ask the data team to change at the source, so the next close is easier?

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
