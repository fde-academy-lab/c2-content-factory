# Day 3 exercises

Four pieces of work. Two are short thinking exercises on paper, one is built with the trainer, and one you run alone.

Today's answers are judgements with reasons attached. A number without its reason scores nothing, because a number without its reason is what this whole day is against.

---

## E1. Guided: grow the counter into a profiler

Drop point: the profiler section, first half. About 45 minutes, trainer-led with the room mirroring.

Monday you wrote a counter that said how many orders had a value in a field. Today it grows two more questions.

Step 1. Start from the counter you already have, and get it printing `present` for every field rather than for one.

Step 2. Add `converts`. For each field, how many values become an integer? Most fields will report zero, and that is information rather than a bug. A field where nothing converts is a text field.

Step 3. Add `distinct`. How many different values does the field hold?

Step 4. Print all three per field and read the shape aloud with the room. You are looking for exactly these lines:

```
  field          present  converts  distinct
  order_id            50         0        49
  amount              48        44        46
  discount            11        11         9
```

Step 5. One field has a `distinct` that does not match its row count, and nothing else on the printout explains it. Name that field. Do not solve it. It is the second half of the day.

Then, together, take one missingness decision end to end: pick `discount`, state the choice, and write the one-line reason underneath it.

---

## E2. Mid-session: which dataset would you trust

Drop point: the break in the first half. About 15 minutes. No computer.

Two profiles of the same order book arrive from two colleagues.

```
              A                                    B
amount    present 48/50  converts 44/50        present 50/50  converts 50/50
          distinct 46                          distinct 42
discount  present 11/50  distinct 9            present 50/50  distinct 9
status    present 50/50  distinct 3            present 50/50  distinct 3
```

1. Which of these two datasets would you compute on, and why?
2. Three counts moved between A and B. For each one, say what a colleague would have had to do to move it that way.
3. One count went down. Explain in one sentence how a cleaning step can reduce the number of distinct values in a column.
4. B's author says the data is now clean because nothing fails to convert. What is the strongest one-sentence reply?
5. If you were handed only B, with no A to compare against, name the one check that would still have caught it.

Question 5 is the one to write carefully. It is the difference between spotting this and living with it.

---

## E3. Mid-session: classify four gaps

Drop point: the break in the second half. About 15 minutes. No computer.

Four fields are missing values in a Kalpa Retail extract. For each, choose **drop the record**, **use a stated default**, **keep and flag**, or **escalate before deciding**, and write the one-line reason a reviewer would read.

| # | The gap |
|---|---|
| 1 | `amount` is empty on 2 orders out of 50. The order book has no other copy of the value. |
| 2 | `discount` is empty on 39 orders out of 50. Absence means no discount was applied. |
| 3 | `segment` is empty on 6 orders. Segment is assigned by a nightly job that failed once last month. |
| 4 | `status` is empty on 1 order, which is also the largest order in the file at Rs 480,000. |

Then answer this: two of your four choices could be argued the other way. Say which two, and what fact you would need to settle each.

---

## E4. Unguided: the full pass

Drop point: the last block. About 40 minutes, alone, no hints. Solution released at the close.

Take the order book from zero to something you would put your name on.

Produce three things:

1. `output/profiled_orders.csv`, the orders you would compute on.
2. `output/rejects.csv`, everything you set aside, each with the reason the interpreter gave.
3. `output/decisions_log.csv`, one line per decision, with the field, what you found, what you chose and why.

Rules that make this the real job rather than an exercise:

- Profile before you change anything, and keep the profile.
- Call `clean_record` and `clean_records` from yesterday. If you are writing a fresh conversion loop, stop and go back for the function.
- Every decision goes in the log, including the ones where you chose to change nothing.
- Reconcile at the end: input equals profiled plus rejected. Print it even when it holds.

Two things in this file need a decision rather than a cleaning step. One is a row, one is a value. Your log should show both, and neither should be deleted.

Before you look at anything, write down two numbers: how many orders you profiled, and how many you rejected. If they do not sum to 50, you have found the most valuable thing in this exercise.
