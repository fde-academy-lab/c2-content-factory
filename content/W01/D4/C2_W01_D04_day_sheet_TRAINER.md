# Day sheet: Week 1, Day 4

Trainer file. Never given to learners, never pasted into a student artifact.

---

## The two minute continuity block, read before you open the deck

**Start from.** They own 44 profiled orders and a decisions log they wrote themselves yesterday: 50 in, 6 rejected for failing conversion. They have watched tracebacks land and read them bottom-up. They already flagged the whale with a fence at ten times the middle order, so today's IQR fence is a better-built version of something they did on Wednesday.

**Do not repeat.** Cleaning, in any form. The row is explicit: compute on the profiled data only. Describing dirty data contradicts yesterday and the room will notice and say so. Also do not re-teach dictionaries, `.get()` or accumulators. Those are today's tools rather than today's topic, and explaining what a dictionary is costs you fifteen minutes you need in half two.

**Two inherited facts to state in the first two minutes.** `KR4201` is still in the file twice, because they chose to keep both rows and flag the pair. Student holds ten orders today and held twelve in the raw file, because two Student orders failed conversion. Both change today's denominators, and both are in their own rejects log rather than in any code.

**Go as far as.** Every learner ships the segment summary and writes one honest sentence per segment, each carrying its denominator.

**Stop before.** Standard deviation arithmetic, distribution theory, any chart library, and all hypothesis language. When somebody asks whether the segment gap is real, and somebody always does, name it as Monday's session and write it on the board. Do not answer it.

**Comes later.** Monday of Week 2 turns today's gap into a formal test using this exact segment summary as its input. Week 2's pandas `groupby` automates the accumulator built by hand today, which is the reason it is built by hand once. Say both aloud at the close.

---

## Shape of the day

| Block | Agenda items | Duration | Deck |
|---|---|---|---|
| Half one | Opening claims, typical, the whale, spread, shape | 130 minutes | `deck_half1` |
| Half two | Sample size, the accumulator, the summary, the honest sentence, Kahoot and close | 110 minutes | `deck_half2` |

Fixed content totals 240 minutes. Trainer discretion fills whatever remains.

---

## The four ideas per half, counted as decision sentences

**Half one.** Mean, median and mode answer "what is typical" three different ways and disagree once the data is skewed. One extreme value drags the mean and leaves the median standing, so picking a statistic is picking what you are willing to hide. Min, max, range and a fence turn "is this value strange" into a rule you can state out loud. Skew reads off sorted values by comparing median-to-max against median-to-min.

**Half two.** A rate is only as trustworthy as its denominator, so the denominator travels with the number. A dictionary accumulator groups by a key discovered while reading rather than declared up front. One pass produces count, median amount and rate per segment. The deliverable is the honest sentence, meaning the number, its denominator and its caveat in one line a stakeholder can repeat.

Sampling and sample size are not a fifth idea in half two. The whole content of agenda item 5 is one rate seen at two denominators, which is that half's first idea arriving before the code. If you find yourself teaching sampling theory, you have added an idea and something else will have to go.

Anscombe's quartet is not a fifth idea in half one either. It is the argument for the third idea, delivered as a case. Keep it to one slide and two minutes.

---

## The breaks to run, with exact text

Verified against Python 3.11.15 in the build session, both notebooks executed cold top to bottom. Re-run them in the Codespace image before delivery.

| Where | What you do | Exact output |
|---|---|---|
| Half one, section 2, **never cut** | Run the mean on the amount column, then the two count lines under it | `mean amount over 44 orders: Rs 12,753.30` / `orders at or above Rs 12,753.30: 1` / `orders below Rs 12,753.30: 43` |
| Half two, section 1 | Run the accumulator with Retail-Core, Retail-Plus and Business hard-coded | `KeyError: 'Student'`, and it fires on the very first order in the file |

The first is a wrong-output failure and it never raises. That is the entire point and it needs saying out loud: nothing in Tuesday's toolkit fires, because nothing went wrong in the sense Python understands. Let the silence sit before you sort the column.

The second is an ordinary crash, and it is quick. Do not dwell. Its value is the sentence that follows it: every hard-coded list of categories is a promise about data you have not read yet.

---

## Per slide labels, half one

| Slide | Label | Note |
|---|---|---|
| S2b | THEN | Put both claims on screen before any teaching. Ask for hands on which one they would send. Take no answer, move on. |
| S4 | SAY | "Pens down on the keyboard." Mean it. This section is on paper and the room will try to type. |
| S6 | DRAW | Seven values on the board, then physically walk to the fourth one. Position, not arithmetic. |
| S7 | ASK | "Predict both numbers before I change anything." Take three predictions aloud. Somebody will say the median moves a little. |
| S7 | TRAP | Let the person who said "a little" hear that it moved by zero. Do not soften it, and do not name them. |
| S8 | SAY | Mode gets ninety seconds. Its job today is to be dismissed for a reason, and the reason is that money does not repeat. |
| S10 | THEN | Run the mean alone first. Let it look fine. Say nothing. |
| S11 | THEN | Now the two count lines. Ten seconds of silence after. |
| S12 | DRAW | Point at the jump from 17,400 to 480,000 with your hand. Twenty-seven times. |
| S15 | ASK | "Do we delete it?" Somebody will say yes. That is the most useful answer of the day. |
| S15 | SAY | "Yesterday you wrote a decisions log so nobody could do this quietly." Tie it to their own artifact. |
| S19 | THEN | The fence catches exactly one record, which the room already found by eye. Say that connection aloud. |
| S23 | THEN | Anscombe. Two minutes, one slide. No detour into correlation. |
| S25 | BRIDGE | "Nothing in a traceback catches this one." Then break. |

## Per slide labels, half two

| Slide | Label | Note |
|---|---|---|
| S3 | ASK | Two identical rates on screen. "Which would you plan a quarter on?" Take a show of hands. Count it. |
| S4 | DRAW | Write 8.3 and 0.08 on the board side by side. The gap between those two numbers is the section. |
| S7 | SAY | Write the hard-coded version as though you are remembering the segments. Do not flag it. |
| S8 | TRAP | Run it. `KeyError`. Ask who spotted it before it ran, honestly. Usually two people. |
| S10 | SAY | "Monday's `.get()`, doing exactly what it did on Monday." The spiral, said aloud. |
| S13 | ASK | "What is missing from every row of this table?" Wait for someone to say the mean is missing. It is deliberate. |
| S14 | THEN | Show the ranking with no counts. Let it look clean and decisive. |
| S15 | THEN | Add the count column. Ten seconds of silence. This is half two's payoff. |
| S16 | SAY | "The two winners are the two smallest segments, and that is not a coincidence about this file." |
| S18 | DRAW | Read all four sentences aloud, slowly. Two of them refuse to make a claim. Point that out. |
| S20 | BRIDGE | Write the open question on the board and leave it up. It is Monday's opening slide. |
| Close | SAY | The paper-test note, below. |

---

## The activity, and where it drops

`activity_typical_number_bench_STUDENT.html` runs at the end of half one, in place of a second pass over the whale.

Open it on the projector and flip one switch: statistic to mean, whale kept in, scope Retail-Core. It reads Rs 36,027.14 on fourteen orders with a red verdict. Say nothing for a moment, then flip the whale out and let them watch the number collapse to Rs 1,875.38 on the thirteen remaining orders.

Then hand it over. Budget about fifteen minutes. Ask three learners which settings they would sign their name to.

**Press the one who removed the whale.** That setting is defensible and it still throws away something true, and the activity says so in its own verdict text. The answer you are looking for is that removing it is a decision that belongs in the decisions log, in writing, with a name on it.

It doubles as a takeaway. Tell them to keep the file.

If half one has overrun, shorten this rather than dropping it. The notebook carries the same demonstration, but the notebook cannot be flipped by a learner in ten seconds.

---

## Checkpoint questions, ask by name

1. After the typical section: "The median moved by how much when we swapped in the Rs 480,000 order?" (Zero. Not "a little".)
2. After the whale section: "The mean is correct. Name what is wrong with it anyway." Follow with: "What happened to the mean when we removed one order, and what does that tell you?" (It landed within Rs 22 of the median.)
3. After the fence: "The fence flagged one record. What do you do to that record?"
4. After the accumulator fix: "Why not just type the four segment names, since we now know Kalpa has four?"
5. After the ranking: "Business came top. How many orders is that resting on, and how many would have to change to lose it?" (Nine, and one.)
6. At the close: "What does Monday do with the number you wrote down today?"

---

## Ranked cut list

The row fixes the first two ranks.

1. **The fence arithmetic.** Flag the whale by sorted tail only and skip the quartile computation. The teaching point survives intact.
2. **Mode.** Ninety seconds, and it can go to zero. Say "there is a third one called the mode, it is for categories, we will meet it again" and move.
3. *This pack's own addition:* the Anscombe slide (S23). It is the argument rather than the mechanism, and the mechanism is already in their hands by then.

**Never cut** the hand computation on seven values, the sample-size contrast, or the count column added to the ranking at S15. The first is where the concept forms, and the last two are the day's reason to exist.

---

## The paper-test note, at the close

Say this once, plainly, and do not elaborate:

> The weekly recap paper cannot run tomorrow because the institute is closed for Gandhi Jayanti. Where it lands is the Programme Head's call and you will be told.

Do not name a slot, a duration for the shifted version, or any marks. The Structure tab records the recap as ungraded and a performance indicator, and its placement this week is not yours to announce. If pressed, the honest answer is that you do not know yet and they will hear directly.

---

## What every learner leaves with

- The segment summary table with counts beside every rate.
- Four sentences, at least two declining to make a claim.
- The open question about Business against Retail-Plus written in their own notebook, in their own words.

The third one is Monday's opening. If a learner has not written it, they will not have it on Monday, so walk the room during the close and check.

---

## The two tracks in each deck

Each deck carries two kinds of slide and it tells you which is which.

Slides numbered `S` are the spine. They are the delivered path, in delivery order, and the block
timings above are built from them alone. Walk them.

Slides numbered `D` carry a DEPTH mark in the top right corner and sit immediately after the slide
they deepen. Skip them live. They exist so the deck is worth reading alone afterwards, so a learner
who asks a harder question has somewhere to be sent, and so you have somewhere to go when the room
is ahead of you.

One warning specific to today. The depth slides say out loud what today deliberately does not
compute, which is the standard deviation and anything resting on it, because the row stops before it
and because a spread measured from this mean would inherit the whale. If a learner asks for the
formula, that slide is the answer and the honest close is that it arrives with the distribution
behind it.

**Half one.** 9 depth slides.

| Depth slide | What it adds |
|---|---|
| `D1` | The three, written as arithmetic |
| `D2` | Mean and median as two different machines |
| `D3` | How wrong can the data be before the statistic is wrong |
| `D4` | Which statistic survives a wrong record, on this file |
| `D5` | How the fence is built, step by step |
| `D6` | What today deliberately does not compute, and why |
| `D7` | Anscombe's quartet, what he actually built |
| `D8` | The tell, applied to columns you have not met yet |
| `D9` | Question 1, the version that separates you from the room |

**Half two.** 7 depth slides.

| Depth slide | What it adds |
|---|---|
| `D1` | A rate written properly, and the number nobody prints |
| `D2` | Why a ranking of small groups reads size as much as performance |
| `D3` | The failure that is worse than the KeyError |
| `D4` | Why the median cannot be accumulated and the count can |
| `D5` | The same argument, run on every segment |
| `D6` | Where the number thirty comes from, and why you should not lean on it |
| `D7` | The convention behind reporting a median, and where it comes from |
