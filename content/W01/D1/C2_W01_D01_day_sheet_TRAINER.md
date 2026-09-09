# Day sheet: Week 1, Day 1

Trainer file. Never given to learners, never pasted into a student artifact.

---

## The two minute continuity block, read before you open the deck

**Start from.** Zero on the environment. The entry requirement guarantees that everyone in the room has written some programming in some language, so lean on that familiarity and assume no Python at all. Say out loud that a loop and an `if` are already familiar shapes and that only the spelling is new.

**Do not repeat.** Nothing. This is the first session of the programme and there is no yesterday to avoid repeating. Spend those first two minutes instead on the one sentence that sets the whole day up, which is that they are about to watch a notebook answer a question about a company nobody has introduced yet. Then run the demo. Do not spend the two minutes on introductions, on the syllabus or on your own background, because the company and the journey each get their own block later in the morning.

**Go as far as.** Every learner answers three counting questions on the records unaided and recovers a deliberately broken kernel.

**Stop before.** Functions, comprehensions, files and any import statement. `int()` is named as a converter today and is never shown failing.

**Comes later.** Functions, errors and files tomorrow, and tomorrow opens by running today's final cell unchanged against a file. The same thirty records return in pandas and in SQL in Week 2, so say the one-spine spiral aloud once today.

---

## Shape of the day

| Order | Block | Duration | Deck |
|---|---|---|---|
| 1 | Opening demo, a working notebook answers a Kalpa question | 10 minutes | No slide. Notebook 1, section headed "The answer, before anything is explained" |
| 2 | Introduction A, Kalpa, the five units, the entity picture, draw it back | 25 minutes | `deck_00_intro`, S1 to S11 |
| 3 | Introduction B, the journey, and the programme and the week and today as promises | 15 minutes | `deck_00_intro`, S12 to S17 |
| 4 | Block one, environment and the kernel for 50 minutes, then types, comparisons, loops and accumulators for 50 minutes | 100 minutes | `deck_half1` |
| 5 | Block two, guided threshold build for 40 minutes, records as dictionaries for 40 minutes, the unguided three for 30 minutes | 110 minutes | `deck_half2` |
| 6 | Introduction C, session mechanics | 10 minutes | `deck_00_intro`, S18 to S23 |
| 7 | Kahoot and close-out | 20 minutes | `deck_00_intro`, S24, with the Kahoot pack |

The four exercises drop inside that shape in this order. E2, the prediction drill, drops at the close of block one, after the accumulators, and runs about 15 minutes. E3, the find-the-mistake drill, drops immediately after E2 at that same close, on the misplaced accumulator you have just run at half one S26, and runs about 15 minutes. E1, the guided threshold build, opens block two and runs about 40 minutes with the room mirroring. E4, the unguided three, closes block two and runs about 30 minutes.

Fixed content totals 290 minutes, which is the row's own 240 minutes plus 50 minutes of introduction pack taken from Day 1's trainer discretion. Trainer discretion fills whatever remains.

The introduction is deliberately broken into three pieces rather than delivered as one long opening. Introduction A and Introduction B run while the room is fresh, and Introduction C sits after the unguided exercise, when the room needs the change of gear more than it needs another concept.

---

## The four ideas per block, counted as decision sentences

Block one. The kernel holds what you gave it until you restart it. Cells run in the order you run them, not the order they sit on screen. A value's type decides what an operator means, and Python refuses a comparison it cannot make honestly. A loop, a condition and an accumulator answer any counting or totalling question.

Block two. A record is a dictionary, so you fetch a field by its name and never by its position. A dataset is a list of records, so the same loop walks it. An optional field is absent rather than empty, so `.get()` with a stated default is a decision you own. And `b = a` gives one list a second name, so appending through either changes both.

Lists ride inside the second block as notation for the ideas above them. Indexing, slicing and `append` are counted as nothing, because they exist today only so that `b = a` and the list of dictionaries make sense. If you find yourself teaching indexing as its own topic, you have added a fifth idea and something else in the block will have to go, and the something else will be the unguided thirty minutes, which is the one part of the day the row will not let you drop.

The introduction pack carries no technical idea at all. It carries one thing to remember, which is the shape of the company, and the learner is asked to draw it rather than to learn it. Treat the entity picture as a picture and resist explaining foreign keys, because that whole idea belongs to Week 2 and it will cost you the guided build if you start it here.

---

## The breaks to run, with exact text

Verified against Python 3.11.15 in the build session. Re-run every one of these in the Codespace image before delivery, because the caret annotation lines under the failing expression differ between versions even where the message text does not.

| Where | What you do | Exact text |
|---|---|---|
| Kernel, block one | Run the counting cell before the setup cell, on the projected screen, with the room watching | `NameError: name 'records' is not defined` |
| Types, block one, never cut | Compare the text `"4500"` against 2000, first on a typed value at half one S18 and on KR4200 inside notebook 1 during block one, then live on KR4200 in the guided loop at half two S6 | `TypeError: '>' not supported between instances of 'str' and 'int'` |
| Accumulators, block one | Run the loop with `total = 0` moved inside it, after you have taken predictions from the room | It runs clean and prints `1460`, which is the amount of KR4224, the last delivered order in the file, and is a sum of nothing at all |
| Dictionaries, block two | Ask any of the twenty-eight records without the key for `r["discount"]` | `KeyError: 'discount'` |

The two the row forbids you to cut are the type break and the kernel recovery drill. Everything else on the day can shorten before either of those two moves.

The misplaced accumulator is the only one of the four that names no error and stops nothing. Run it after the two that do raise, so the room has met a loud failure before it meets a quiet one, and let somebody say out loud that the quiet one is worse.

---

## Per slide labels, introduction deck

| Slide | Label | Note |
|---|---|---|
| Opening | THEN | Before any slide at all, run the opening cell of notebook 1, headed "The answer, before anything is explained". Say the question out loud, "Of these thirty Kalpa Retail orders, how much did we actually collect?", run the cell and let 13 delivered orders and Rs 25,720 sit on the screen. Explain nothing. Application before theory, and it is the row's own opening. |
| S1 | SAY | "Nobody has told you who Kalpa is." That sentence is the reason the next 25 minutes exist. |
| S3 | DRAW | Five boxes on the board as you name the five units. Leave them up for the rest of the day. |
| S5 | SAY | Name each unit in one sentence and move. The room does not need the business detail today and it will forget any of it that you add. |
| S6 | SAY | "Teaching never leaves Kalpa Retail." Say why, which is that nobody absorbs a new idea and a new business on the same morning. |
| S7 | THEN | Project the entity picture and put your hand on ORDERS. Say that today is that one table flattened into a list, and stop there. |
| S9 | BRIDGE | "The tool changes every few weeks. The company is the one thing that does not." |
| S10 | ASK | Laptops closed, paper out, 3 minutes to draw Kalpa from memory. Walk the room while they draw and look at what people leave out. Whatever most of the room leaves out is what you repeat on Thursday. |
| S11 | SAY | The disclaimer, once, without ceremony, then move. |
| S12 | SAY | Read the five phases as promises about what they can do, and refuse every question about marks, weights and exam days. Say plainly that those are not settled and that you will not guess at them. |
| S14 | ASK | "Which of Monday to Thursday sounds hardest to you right now?" Take three answers. Come back to those three answers on Thursday. |
| S17 | BRIDGE | Read the day's crux line as written and then close the deck: "You can take thirty records nobody explained to you and come back with a number, and you can say what would break it." |
| S18 | SAY | Walk the seven steps of a teaching day once. This is the section that becomes a handout the moment the day runs long. |
| S21 | SAY | Name the four platforms and say that this cohort does not use Slack, because somebody will ask. |
| S23 | SAY | Name what runs AI-free and stop there. There is no written general policy for the early weeks and inventing one here will be quoted back at you in Week 5. |
| S24 | THEN | Hand over the take-home, the self-check and the pre-read by name, then release the solutions file. |

## Per slide labels, block one

| Slide | Label | Note |
|---|---|---|
| S3 | SAY | Repeat the demo answer and name the group it came from: 13 delivered orders, Rs 25,720. Naming the group is a habit you are starting here and enforcing all day. |
| S4 | SAY | "Four lines produced that answer. You will have written this before the day ends." Point at the screen and move on. Do not read the code aloud. |
| S5 | ASK | "Hands up who has the Codespace open already." This is the moment access failures surface, and the Support TA leaves the room with them. Read the environment contingency section below before you ask this. |
| S6 | THEN | Walk the five parts of the layout on the projected screen with your cursor. Do not describe them from a slide. |
| S8 | THEN | Wait until every hand is down before you move. This is the last point in the day where waiting is cheap. |
| S9 | DRAW | Draw the bench on the board, with the sweep across it for a restart. Leave it up all day and point back at it every time state comes up. |
| S11 | ASK | "Which of these three cells ran first?" Take three answers before you say anything. The counters are on the slide and most of the room will still read top to bottom. |
| S12 | TRAP | Run the counting cell before the setup cell live. Let the NameError sit on screen for ten seconds without commentary, then read the last line aloud with your finger on the word `records`. |
| S13 | THEN | Actually restart the kernel and run all on the projected screen. Do it, do not describe it. Then say the file on disk never changed. |
| S16 | ASK | "`type('4500')` and `type(4500)`. Same answer or different?" Take a show of hands before you run either. |
| S17 | TRAP | Put the two records up and say nothing. Somebody finds the quotes. Let them find it rather than pointing at it. |
| S18 | THEN | Run it, then read both type names in the message aloud with your finger on each one. The habit you are teaching is reading the message before touching the code. |
| S19 | THEN | Mars Climate Orbiter. Give the number before the story. Do not add a second case and do not add detail beyond the row. |
| S20 | SAY | "You lose ten seconds and you keep the truth." That is the answer they give when an interviewer asks why an error was the good outcome. |
| S22 | DRAW | Draw the three branches on the board and mark the point where Python stops testing. |
| S25 | THEN | Build the sum accumulator live and land on Rs 25,720, then say out loud that this is the number the day opened with. The room should feel the loop close. The converter is on this slide because notebook 1 has already met the text amount in KR4200, and the guardrail on `int()` sits at block two S7, so read that note before you take a question about it here. |
| S26 | TRAP | Take predictions before you run the misplaced accumulator. Somebody will predict an error. Run it, print `1460`, and let the silence sit. |
| S28 | BRIDGE | Read the crux line as written: "The kernel remembers exactly what you gave it and nothing else, and the type of a value decides what every operator means." |

## Per slide labels, block two

| Slide | Label | Note |
|---|---|---|
| S3 | ASK | "How many of these orders are above Rs 2,000, and what do they add up to?" Ask it as a person at Kalpa would ask it, then start typing. |
| S5 | THEN | Build the cell one line at a time with the room mirroring on their own Codespaces. Do not paste. Your typing speed is the room's pace and it should feel slow to you. |
| S6 | TRAP | The TypeError lands on the very first record in the file. Say that they met this error in block one, and here it is inside the cell they are typing themselves. |
| S7 | SAY | `int()` is a converter today and it is never shown failing. Do not show it failing, do not mention `int("twelve")`, and do not answer the question if it comes from the room beyond saying that tomorrow opens on exactly that. Tomorrow's opening is already built around it. |
| S8 | THEN | Print, then say the answer out loud as a sentence before anyone writes anything down. |
| S9 | TRAP | The two thirteens. See the dedicated section below. Name it here, once, deliberately. |
| S12 | SAY | Slicing lands as one beat. This is the first thing on the cut list, so say the line and move. |
| S13 | TRAP | Ask for `len(a)` before you run it. Most of the room says 2. Run it and let 3 land. |
| S16 | SAY | "Position is a promise the file never made to you." Then give the added-column story in one sentence. |
| S17 | TRAP | Run `records[0]["discount"]` live and let the KeyError print the field name it went looking for. |
| S20 | THEN | Run both defaults back to back and leave Rs 250 and Rs 3,050 on the screen together. Say that both cells ran to the end and only one of the two totals is a fact. |
| S23 | BRIDGE | This is the cell the day ends on and tomorrow reuses it verbatim. Say that aloud, because it is the promise that makes tonight's take-home worth doing. |
| S25 | THEN | Hand over the three unguided questions and then stop talking. Walk the room and answer nothing. The Academic TA and the Support TA hold the same line. |
| S27 | SAY | Read the half's crux line as written: "A dataset is a stack of named cards, and a loop with a condition and an accumulator turns that stack into one number you can defend." |
| S28 | SAY | Read the day's crux line as written: "You can take thirty records nobody explained to you and come back with a number, and you can say what would break it." |

---

## The activity, and where it drops

`activity_kernel_tracer_STUDENT.html` runs inside the kernel section of block one, at S12 to S13, in place of talking the restart through a second time. Budget about 15 minutes from that section.

Open it on the projector first and click one cell so the room sees the workbench panel change. Then let them open it themselves and run the four cells in an order of their own choosing until they can predict the panel before they click. Ask two learners to say which order they ran and what they expected, and press the one who ran the setup cell last, because that learner produced the NameError on purpose and can explain it.

It doubles as a takeaway. Tell them to keep the file, because the same picture is the answer to the Kahoot item on what a restart erases.

If block one has overrun, shorten this rather than dropping it, since the recovery drill it supports is on the row's never-cut list and the activity is the cheapest way to run that drill twice.

## Checkpoint questions, ask by name

1. After Introduction A: "Name the five Kalpa units, and say which one every teaching day lives inside."
2. After Introduction B: "What can you do by Saturday that you could not do when you walked in?"
3. After the environment and kernel section: "You restarted the kernel. Say one thing you lost and one thing that is still there."
4. After types, comparisons and accumulators: "`'10' > 9`. True, False, or something else, and why?"
5. After the guided build: "Your total on thirty orders came back as Rs 1,460. What is the first thing you look at?"
6. After records as dictionaries: "A record has no discount field. What does `.get('discount', 0)` hand you, and who decided the zero?"
7. After the unguided three: "Your three counts do not add up to thirty. Is that allowed, and why?"
8. At the close: "What arrives tomorrow that today's last cell has to survive?"

---

## Ranked cut list

The row fixes the first two ranks. The introduction pack carries its own separate order, below.

1. The slicing extras, at half two S12 and in notebook 2 section 2. Indexing and `append` stay, because `b = a` needs them. From the row.
2. Negative indexing, which lives only in notebook 2 section 2 and appears in no deck and no exercise. Nothing downstream depends on it. From the row.

Both of the row's cuts are built rather than pre-applied, so cutting them is a live decision on the day rather than a note about something that was never there.

Inside the introduction pack the order is separate and it is fixed. The mechanics section, `deck_00_intro` S18 to S23, becomes a handout before anything else in the introduction is touched, because it is the only part of the introduction that survives being read alone. The company section and the journey section both depend on you being in the room to draw and to answer, so they cannot become paper. If the introduction has to give up more than the mechanics section, take the phase table at S12 next and keep the four days at S14, since the week they are actually in matters more today than the phase map.

Never cut the kernel recovery drill or the type break. If everything else has to shorten so those two run, then everything else shortens. The unguided thirty minutes is the third thing to protect, and it comes out of the guided build's minutes rather than out of its own.

---

## The Day 1 environment contingency

This is the day Codespace access fails for somebody. Plan for it rather than reacting to it.

The moment you find a learner who cannot launch, pair them with the neighbour on their left, one screen between two, and tell the pair that the person without a machine drives and the person with the machine types. That keeps the learner inside the guided build instead of watching it, and it is the only arrangement that survives the guided build's pace.

The Support TA owns the recovery from that point and the room continues at the pace it was already going. Do not stop the room to debug one launch, and do not fold a launch failure into the teaching by explaining what went wrong, because the room reads that as the environment being fragile on the first morning. The Support TA takes the learner out, gets them running, and brings them back.

If a learner is still without a machine when the unguided thirty minutes start, they write their three answers on paper as code and run them on the neighbour's machine in the last few minutes. Written answers count as done for today.

Log every launch failure and hand the list to the Academic TA before you leave, so that by tomorrow morning there is an answer to whether this was one learner or a pattern.

## The baseline note

Week 1 is the baseline week. Two signals are being read today and no others.

The first is quiz behaviour on the Kahoot, which means who answers fast and wrong on the two trap items, who changes their answer pattern after the reason line is read out, and who stops answering partway through.

The second is unguided completion, which means how many of the three questions each learner actually finished inside the thirty minutes, and whether the answers came back as sentences naming the group or as bare numbers.

No scoring of any kind is applied to either signal, no metric is named, no number is recorded against a learner, and nothing is reported back to the room. The Kahoot is ungraded and it counts towards nothing at all, and you say so out loud before you run it.

This block exists in this file only. It is never read out, never shown, and never reaches a learner.

## The two thirteens warning

Two different thirteens live in this day. The delivered orders are 13 orders totalling Rs 25,720, which is the number the day opened with and the number the day closes on. The orders above Rs 2,000 are 13 orders totalling Rs 35,020, which is the guided build's answer.

They are unrelated groups that happen to hold the same count. The overlap between them is 6 orders, which is the third unguided question, so the room will meet the distinction again on its own within the hour.

The room will conflate them unless you name it once, out loud, at half two S9, in the moment the second thirteen lands. Say that these are two different groups of orders with the same count, and that this is why every answer today gets reported as a sentence that names its group. If you skip this, you will see it come back in the unguided answers as a learner reporting Rs 35,020 for the delivered question.

---

## What ships tonight

The solutions to the three unguided questions are released at the close of the session and not one minute earlier, including to the learner who asks nicely on the way out.

The take-home and its self-check spine go out at the close. The take-home extends the unguided counter into two buckets above and below the threshold, and it asks for a markdown cell explaining the planted text amount in the learner's own words.

The pre-read for tomorrow goes out at the close, without exception. Tomorrow opens by running today's final cell unchanged against a file, so the learner who has not opened the pre-read still lands on their feet, and the learner who has opened it lands ahead.

Say the watch item by name at the close: Corey Schafer, Dictionaries, video: link to be found.

## Known gaps in this pack

Every reference link in this pack is a "to be found" slot. The build session had no network access to verify a single URL and an unverified link never ships. See the internal link register in this folder and paste the verified links in before release.

The row's STOP BEFORE bars every import statement, so Monday's notebooks import nothing at all. A deliberate failure has to print itself without halting the run, and with no `traceback` helper available the notebooks use a small `try` and `except` wrapper around each break, labelled in the markdown above it as plumbing that keeps the notebook running. Beside each wrapped cell there is a markdown block carrying the full traceback exactly as the learner sees it when they run the bare line themselves. Say once, when the first wrapper appears, that the learner meets `try` and `except` properly tomorrow and that today they only need to read the message.

The three `.pptx` decks are generated from the markdown deck files in this folder. If you edit a slide, edit the markdown and regenerate, because the markdown is the source and the deck is the print.
