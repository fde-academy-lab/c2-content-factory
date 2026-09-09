# Day sheet: Week 1, Day 3

Trainer file. Never given to learners, never pasted into a student artifact.

---

## The two minute continuity block, read before you open the deck

**Start from.** They read files, clean single orders with functions, and keep a rejects log from Tuesday. Put Monday's presence counter on screen inside the first ten minutes and say that today's profiler is that counter grown up. That sentence does more work than any slide.

**Do not repeat.** Reading files, try and except, the mechanics of the rejects log, and Tuesday's argument about the bare except. Tuesday's `clean_record`, `clean_records` and `normalise_amount` are called unchanged today rather than rebuilt, and saying so out loud is the payoff Tuesday promised.

**Go as far as.** Every learner ships the profiled dataset, the decisions log and a reconciled count, and defends one decision aloud.

**Stop before.** Imputation beyond a stated default, statistical outlier theory, standard deviation arithmetic, anything pandas.

**Comes later.** Tomorrow's descriptive statistics run on today's cleaned output, so the decisions made today set tomorrow's numbers. Week 2 re-expresses this whole pass in pandas with `isna`, `duplicated` and `to_numeric`. Say that spiral aloud.

---

## Shape of the day

| Block | Agenda items | Duration | Where |
|---|---|---|---|
| One, columns | Two profiles, the profiler, missingness, coercion at scale | 125 minutes | Deck S1 to S21, notebook 1 |
| Two, rows | Duplicates, outliers, the full pass, Kahoot and close | 115 minutes | Deck S22 to S52, notebook 2 |

Fixed content totals 240 minutes.

One deck, not two halves. The mental model does not reset today: it is profile, decide, record, applied to columns and then to rows, which is the spiral rather than a second arc. The column-to-row shift is marked at deck S22 and is worth naming as you cross it.

---

## The four ideas per block, counted as decision sentences

Block one: profile before you change anything, three counts per field; a missing value is a three-way decision with a written reason; conversion failures must be counted separately because a coerce-everything pass destroys the evidence; every cleaning act is a line in the decisions log.

Block two: "same record" is an identity rule you state, since the data cannot tell you; an outlier is a finding to investigate before it is a row to delete; the profiled dataset is shippable only with its decisions log.

Tuesday's reconciliation returns one level up, now holding across drops, defaults and dedupe. That is a revisit rather than a fifth idea, and saying "you already know this one" is what keeps it from counting.

---

## The breaks to run, and why today is harder than yesterday

Neither of today's failures raises. There is no error text to read out, and no traceback to point at. Both print a number that looks fine. Say that to the room before the first one, because a room trained on yesterday is waiting for red text that never comes.

| Where | What you do | Exact wrong output |
|---|---|---|
| Block one, coercion | Run the coerce-everything pass and re-profile | `amount` goes from present 48 converts 44 distinct 46 to present 50 converts 50 distinct 42, and `discount` from present 11 to present 50 |
| Block two, duplicates | Run the whole-record dedupe, then the id count | `duplicate rows by whole-record comparison: 0` followed by `distinct order_ids: 49 across 50 rows` |

The tell in the first one is `distinct` falling from 46 to 42. Do not point at it. Ask which number moved the wrong way and wait. Somebody will find it, and the room remembers what it found.

The tell in the second is that two numbers on two lines disagree and nothing connects them. Leave both on screen and say nothing for ten seconds.

Verified against Python 3.11.15 in the build session. Re-run both on the Codespace image before delivery.

---

## Per slide labels

| Slide | Label | Note |
|---|---|---|
| S2 | ASK | "Which of these two would you trust?" Take a show of hands before any explanation. Most rooms pick B. |
| S3 | THEN | Reveal A. Let the discomfort sit. |
| S5 | DRAW | Circle `distinct` on the board. It is the only count that can fall, and that is the sentence they should leave with. |
| S9 | SAY | "Present minus converts is your work list." |
| S13 | DRAW | Three columns on the board, drop, default, keep and flag, and fill them from the room rather than the slide. |
| S15 | TRAP | Filling discount with zero is defensible. Say so, then make them name what it costs. |
| S17 | THEN | HGNC. Give the number of renamed genes before the story. |
| S19 | BRIDGE | Columns are done. Now the records themselves. Mark the crossing. |
| S20 | THEN | Put both numbers on screen together and stop talking. |
| S22 | ASK | "Same order twice, or two orders?" Do not resolve it. It is not resolvable from the file. |
| S24 | SAY | "Not you, on your own, on a Wednesday." |
| S27 | THEN | Rs 480,000 of a Rs 561,145 total. Say the percentage last. |
| S28 | TRAP | Ask who would delete it. Several hands. Then ask what they would have deleted if it turned out to be the largest genuine customer. |
| S32 | DRAW | Write the four log lines on the board as the room dictates them. |

---

## The activity, and where it drops

`C2_W01_D03_activity_identity_rule_STUDENT.html` runs inside the duplicates section, after slide S23 and before S24. Budget about 15 minutes.

Open it on the projector with `order_id` alone selected, then switch on `order_date` and let them watch one duplicate become zero duplicates without any data changing. That single toggle is the lesson.

Then let them find a setting they would sign, and take three answers. Press the learner who selected the whole row, because their rule finds nothing and is still a rule somebody has to live with.

It doubles as a takeaway. Tell them to keep the file.

If block two has overrun, shorten it rather than dropping it, since notebook 2 section 3 carries the same comparison without the interaction.

---

## Checkpoint questions, ask by name

1. After the profiler: "Which of the three counts can go down, and why does that matter?"
2. After coercion: "Every count improved. What got worse?"
3. After duplicates: "Give me an identity rule for this file that somebody else could apply."
4. After outliers: "The whale survived cleaning. Why?"
5. At the close: "40 records dropped. Where does that fact live?"

---

## Ranked cut list

1. The outlier fence arithmetic, so the tail is flagged by sorting alone. From the row.
2. The companion file with the duplicated header, in notebook 2 section 6. This pack's addition, not the row's, so drop it only after the fence.

Never cut: the decisions log, the count reconciliation, or the two profiles on screen at the opening.

If the day is running long, the guided profiler build shortens and the unguided full pass still runs. The unguided pass is the artifact the row asks every learner to ship.

---

## The unguided pass, how to run it

They have 40 minutes and three files to produce. Walk the room.

Two things in the file need a decision rather than a cleaning step: the repeated `order_id` and the Rs 480,000 order. Do not name either. When somebody finds one, ask what they are going to do about it and let the room hear the answer.

The most common wrong turn is deleting the whale to make the numbers look sensible. When you see it, ask what they would tell the customer who placed it.

---

## What ships tonight

The pre-read for tomorrow, without exception. Tomorrow opens on the average order value of the file they cleaned today, so their decisions set tomorrow's numbers, and that connection is worth stating at the close.

## Known gaps in this pack

Every reference link is a "to be found" slot. The build session had no network access and an unverified link never ships. See the internal link register in this folder.

The data is generated rather than hand-written. See the provenance file for the one command that rebuilds it.

---

## The two tracks in the deck

The deck carries two kinds of slide and it tells you which is which.

Slides numbered `S` are the spine. They are the delivered path, in delivery order, and the block
timings above are built from them alone. Walk them.

Slides numbered `D` carry a DEPTH mark in the top right corner and sit immediately after the slide
they deepen. Skip them live. They exist so the deck is worth reading alone afterwards, so a learner
who asks a harder question has somewhere to be sent, and so you have somewhere to go when the room
is ahead of you.

If the room is running fast, add the depth slides that carry a diagram of a mechanism first, because
they save you drawing it on the board. If the room is running slow, every depth slide goes and
nothing in the spine changes.

| Depth slide | What it adds |
|---|---|
| `D1` | Why distinct is the count that catches a silent fix |
| `D2` | The three counts as rates, so columns can be compared |
| `D3` | The whole file, profiled |
| `D4` | The six failures, named, and who fixes each |
| `D5` | What distinct tells you about a field's job |
| `D6` | The same two columns, and what each choice would cost in numbers |
| `D7` | The coerce-everything pass, and what it hides |
| `D8` | The gene name case, the mechanism |
| `D9` | The gene name case, what it cost and how it was fixed |
| `D10` | Why that case belongs in a Python session |
| `D11` | The two readings, and what each one costs if you are wrong |
| `D12` | Writing the two checks so they disagree in public |
| `D13` | What you actually send, and why it fits in six lines |
| `D14` | What it does to every number you might report |
| `D15` | Where the 1.5 comes from, and why you should say so out loud |
| `D16` | Three ways to flag an extreme, and when each is honest |
| `D17` | What investigating it actually means |
| `D18` | The fields a decisions log line needs |
| `D19` | The reconciliation as an identity, with today's numbers |
| `D20` | The whole day, as one runnable check |
| `D21` | Question 1, the version that separates you from the room |
| `D22` | Question 2, the numbers that make it land |
