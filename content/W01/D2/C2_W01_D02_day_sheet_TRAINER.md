# Day sheet: Week 1, Day 2

Trainer file. Never given to learners, never pasted into a student artifact.

---

## The two minute continuity block, read before you open the deck

**Start from.** They loop, branch and read records by name from yesterday. They have already watched three tracebacks land, so errors are familiar sights rather than a new frightening topic. Say that out loud in the first two minutes.

**Do not repeat.** Types, comparisons, loops, accumulators, lists, dictionaries. Yesterday's inline code is raw material to refactor today. If you find yourself explaining what a dictionary is, you have lost fifteen minutes.

**Go as far as.** Every learner ships `clean_record` and completes the AI-free lab with both output files reopening correctly.

**Stop before.** Custom exception classes, `*args` and `**kwargs`, lambdas, imports beyond `csv` and `json`, encodings beyond a single mention, anything pandas.

**Comes later.** Tomorrow's full dataset pass calls today's functions without one edit. Promise that aloud at the close, because it is the payoff that makes today feel worth it. Week 2 re-expresses all of today in pandas.

---

## Shape of the day

| Block | Agenda items | Duration | Deck |
|---|---|---|---|
| Half one | Opening demo, functions, errors, guided carve | 150 minutes | `deck_half1` |
| Half two | Files, the AI-free lab, Kahoot and close | 120 minutes | `deck_half2` |

Fixed content totals 270 minutes. Trainer discretion fills whatever remains.

---

## The four ideas per half, counted as decision sentences

Half one: a function packages one reusable decision and returns a value rather than printing it; a traceback is read bottom-up and names the failing line; catch narrowly on a named exception and never bare; every rejection is logged with its reason.

Half two: a file format is an agreement about structure and everything a CSV agrees to is text; `with open` guarantees the close even when the code fails; `DictReader` takes its keys from the header row; one pass ships two deliverables.

Scope and the list comprehension ride as single beats inside the first idea of each half. They are notation, and they are not counted. If you find yourself teaching either as its own topic, you have added a fifth idea and something else will have to go.

The deck's half-two JSON section is not a fifth idea either. It is the first idea met a second time, on a format that agrees about more, which is the spiral doing its job. Say that connection out loud at slide 19 or the room will count it as new.

---

## The breaks to run, with exact text

Verified against Python 3.11.15 in the build session. Re-run each one in the Codespace image before delivery, because the caret annotation lines under the failing expression differ between versions even where the message does not.

| Where | What you do | Exact text |
|---|---|---|
| Opening, half one | Run yesterday's cell, unchanged, against today's file | `ValueError: invalid literal for int() with base 10: 'twelve'` |
| Functions, half one | Call a print-only function and subscript the result | `TypeError: 'NoneType' object is not subscriptable` |
| Errors, half one, never cut | Bare except around the conversion, then the honest version | Both print `230380`. First claims `Processed 30 records`. Second says `Clean 28, rejected 2` |
| Files, half two | Open a mistyped path | `FileNotFoundError: [Errno 2] No such file or directory: 'data/orderz.csv'` |
| Exercise, half two | Learners load the truncated feed themselves | `json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 48 column 1 (char 841)` |

The bare except demonstration is the one that must not be cut under any time pressure. It is the argument the whole day rests on.

---

## Per slide labels, half one

| Slide | Label | Note |
|---|---|---|
| Opening | THEN | Before any slide, run the opening demo cell of notebook 1, headed "Where this is going": `clean_record` working on three records, rejected, rejected, kept, with each rejection saying why. Say "you will have written this within the hour" and move on. Application before theory, and it is the row's own opening. |
| S3 | ASK | "Three copies of this cell. One has a typo. Which one?" Wait. Do not answer it. |
| S5 | DRAW | Box the function on the board with an arrow in and an arrow out. Leave it up all half. |
| S5 | SAY | The comprehension lands in notebook 1 section 2 as one line beside the loop it replaces. One beat, then move. Teaching it as a topic adds a fifth idea. |
| S7 | SAY | "The function cannot see anything you did not hand it." That sentence is all of scope for today. |
| S9 | ASK | "What is inside result now?" Take three answers before you run it. |
| S10 | TRAP | Let the silence sit after the TypeError. Someone will say `None`. Let them say it. |
| S14 | DRAW | Point at the traceback bottom-up with your hand. Physically move upward. |
| S15 | SAY | "The third question is the one people skip." Then ask who checked the value. |
| S17 | TRAP | Read the bare except code aloud and ask whether it looks wrong. It does not. That is the point. |
| S18 | THEN | Run both. Say nothing for ten seconds. Let them notice the numbers match. |
| S19 | SAY | "A crash costs you an hour. A plausible wrong number costs you the quarter." |
| S25 | THEN | Knight Capital. Give the number before the story. |
| S28 | BRIDGE | "Everything so far lives in memory. Close the notebook and it is gone." |

## Per slide labels, half two

| Slide | Label | Note |
|---|---|---|
| S3 | THEN | Actually restart the kernel on the projected screen. Do not describe it. |
| S6 | DRAW | Three columns on the board: what the file holds, what Python receives, what you meant. |
| S7 | SAY | "The defect was not fixed. It was hidden by the format." |
| S10 | TRAP | Run the wrong path first, before any correct open. The error is the teacher. |
| S13 | ASK | "Who has run out of file handles on a laptop?" Nobody. That is why it needs saying. |
| S17 | TRAP | Change a header spelling live and watch every lookup raise KeyError. |
| S20 | DRAW | Draw the nested record. Point at the amount sitting one level down. |
| S21 | ASK | "Drop it or invent a column. Which, and who do you tell?" |
| S26 | SAY | "Writing a file is not finishing. Reopening it is finishing." |
| S27 | THEN | Public Health England. Say the 15,841 slowly. |
| S31 | BRIDGE | "The functions you carved today get called tomorrow without one edit." |

---

## The activity, and where it drops

`activity_defensive_stance_STUDENT.html` runs inside the errors section of half one, at slides S17 to S19, in place of talking through the bare except a second time. Budget about 15 minutes from that section.

Open it on the projector first and flip one switch. Then let them open it themselves and find a setting they would sign. Ask three learners to say which setting they chose and why, and press the one who chose validate-first with the awkward record included, because that setting is honest and still throws away a good record.

It doubles as a takeaway. Tell them to keep the file.

If half one has overrun, this is the first thing to shorten, since the notebook already carries the same demonstration. It is not on the row's cut list, so shorten it rather than dropping it.

## Checkpoint questions, ask by name

1. After the functions section: "Give me one reason a function beats a copied cell that is not about typing less."
2. After the errors section: "Both cells printed the same number. Which one lied, and about what?"
3. After the guided carve: "Your rejects list is empty on a file you know is dirty. First two checks?"
4. After files: "Where do DictReader's keys come from, and what breaks if the header changes?"
5. At the close: "What does tomorrow do with the function you wrote today?"

---

## Ranked cut list

The row fixes the first two ranks. The third is this pack's own addition and is marked as such.

1. The list comprehension variant, in notebook 1 section 2. It is one line of notation and nothing downstream depends on it. From the row.
2. `json.dump`, in notebook 2 section 5, so the day writes CSV only. Reading JSON stays. From the row.
3. The second mid-session exercise, if the first half has overrun badly. This pack's addition, not the row's, so drop it only after the two above.

Both of the row's cuts are built rather than pre-applied, so cutting them is a live decision on the day rather than a note about something that was never there.

Never cut: the bare except demonstration, the rejects log, the reconciliation, or the AI-free lab. If all four will not fit, the guided carve shortens and the lab still runs.

---

## The AI-free lab, how to run it

State the rule before you hand out the file, in these terms: no assistant, no accepted autocomplete, no searching for a finished answer, and the Python documentation is allowed. Then say why, in one sentence: today is the day they find out what they can do without help, and knowing that is worth more than a working file.

Walk the room. Learners who freeze in the first five minutes usually have a `FileNotFoundError` and have not read it. Point at the path in the message and walk away.

The defect that catches people is `12,400`, which is a real number wearing a thousands separator. Do not name it. When someone finds it, ask them what they are going to do about it and let the room hear the answer.

---

## What ships tonight

The pre-read for tomorrow goes out at the close, without exception. Tomorrow's session opens on one take-home notebook, so pick one during the lab while you are walking the room.

## Known gaps in this pack

Every reference link is a "to be found" slot. The build session had no network access to verify any URL, and an unverified link never ships. See the internal link register in this folder, and paste the verified links in before release.

Segment values in the data files are placeholders that survive until the client-zero scenario locks. See the internal rename map in this folder.

The row's STOP BEFORE bars imports beyond `csv` and `json`. The notebooks import `traceback` and `os` as plumbing, so a failure can print itself without halting the run and so the output folder exists. Both are labelled in the setup cell as not being today's topic, and neither is taught. If you would rather hold the line exactly, the alternative is a notebook that stops at its first deliberate failure, which costs more than it saves.
