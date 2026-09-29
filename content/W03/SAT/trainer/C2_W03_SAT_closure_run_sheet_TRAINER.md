# Run sheet: Week 3, Saturday. Dr Menon's answers, and Build 1 closes

**TRAINER ONLY.** Nothing on this page reaches a learner.

Posts to <!-- sync:module:W03/SAT -->Module 1: Foundations of AI and Data<!-- /sync:module:W03/SAT -->, on <!-- sync:day-date:W03/SAT -->Sat 24 Oct 2026<!-- /sync:day-date:W03/SAT -->.

| | |
|---|---|
| **The day** | Dr Menon's question gets its answers. The remaining GD rounds close, every group presents with a live demo before one of two panels, scores roll as each slot ends, every Build 1 grade closes, and each group names one improvement for Build 2. |
| **Length** | 300 minutes of room time (`data/programme/facts.yaml`), run here as a morning of 180 and an afternoon of 120 with lunch between them. A build week's Saturday carries no recap paper, no Kahoot and no practice set. |
| **Who** | The Programme Head runs the day and owns grade closure. The industry expert chairs one panel and the remaining GDs; the senior industry leader, who flies in for the day and returns the same day, chairs the other panel. The Principal Advisor takes GD rounds online where the roster needs it. The trainer scribes for the expert's room and runs the week close; the Academic TA scribes for the leader's room, checks demo machines and runs the separate questions for silent teammates. |
| **Nothing is taught** | The only teaching moment is the week close, which names what the week trained and hands the room to Week 4. |
| **Interview angle** | [S] Present a finding to a panel and take a challenge on your caveat. |

**What each panel member reads before the first slot:** the question bank,
`trainer/C2_W03_SAT_question_bank_TRAINER.md` (ten minutes for their own sub-problems, five for the
headline), and the presentation format the groups built on,
`slides/C2_W03_SAT_presentation_format_STUDENT.md`, so they know the 17 minutes the group holds.

---

## The slot, which is the same in both rooms

```mermaid
flowchart LR
    A["<b>group</b><br/>17 min<br/>answer, method, demo"] --> B["<b>panel questions</b><br/>8 to 10 min"] --> C["<b>changeover</b><br/>3 min<br/>scores recorded"]
    classDef core fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class B core
```

| Part | Minutes | Who keeps it |
|---|---|---|
| The group's presentation, with its live demo inside it | 17, a hard stop | The room's scribe holds up a card at 15 and stops the group at 17 |
| The panel's questions | 8 to 10 | The panel chair; at least four questions, per the question bank's rule 3 |
| Changeover, while the panel records each learner's score and the next group sets up | 3 | The scribe |
| **The slot** | **28 to 30** | |

**Words for the scribe at 17 minutes:** "Time for the group. The panel's questions now; the group keeps
its full question time."

**Silent teammates.** During questions the chair names the member who has spoken least for the
silent-teammate question in the bank, and the rest of the group stays silent while that member
answers. A member who still cannot answer is flagged by the scribe on the room's list, and the same
panel questions that learner separately, alone, for up to five minutes in the room's next reserve
(see the timelines), before that group's scores are final.

---

## Before the day opens

| Step | Who | Done when |
|---|---|---|
| Read the presentation order drawn at Friday's close, strike the groups that presented Friday, and assign the rest to the two rooms by the rule below | Programme Head | Both room orders are printed and on each panel's table |
| Copy Friday's GD totals (from `content/W03/D5/rubrics/C2_W03_D05_gd_scoring_sheet_TRAINER.xlsx`), Friday's first-tranche mini project totals and Thursday's mock scores into the grade closure workbook | Programme Head, with the Academic TA reading the sheets aloud | The workbook's Checks sheet shows no MISSING in the GD column for Friday's groups, none in the mini project column for the first tranche, and none in the mock column |
| Run the demo from the frozen commit for any group with no second cold run logged on Friday, as Friday's freeze rule requires | Academic TA | Every group has a logged cold run on its frozen hash |
| Open each group's demo machine on a fresh Codespace at its frozen commit, with the raw files in the data folder, and leave it closed and cold; check `git rev-parse HEAD` against Friday's freeze table before each slot | Academic TA | Every group has a machine on its frozen hash, and none has run the notebook |
| Put the question bank in front of each panel, marked with that room's sub-problems | Trainer | Each panel member has read their pages |

**The room rule.** Keep every sub-problem's groups together on one panel and back to back, so a
panel hears the alternate claims on one question in sequence. Balance the two rooms to within one
group, and give the leader's room the larger share, because the expert's room runs the remaining GDs
first. Where it can be done without splitting a sub-problem, put sub-problems 1 (revenue) and 5
(campaign) before the leader, whose questions are the board's, and 2 (bookings), 3 (billing) and 4
(no-shows) before the expert. The allocation that decides the clusters was made by the Programme Head
on Monday; this sheet does not assume it.

---

## Plan A: the clusters are 2, 2, 2, 2 and 1 (every sub-problem covered by nine groups)

This plan is sized for the heaviest Saturday the week could hand over: nobody presented on Friday
and three GD rounds remain. Every group Friday took off frees one slot of 30 minutes in its room.

**The likely Saturday, from Friday's pack.** Friday runs seven GD rounds and a first tranche of up to
three presentations in whole clusters (`content/W03/D5/trainer/C2_W03_D05_day_sheet_TRAINER.md`), so
Saturday holds two GD rounds (slots 8 and 9, one of them the Principal Advisor's online) and about six
presentations. Run both GD rounds in parallel in the first 30 minutes after the opening (the expert in
the room, the Principal Advisor online), start the leader's room at once, and let the expert's room
begin its slots after the GD; the two groups in Saturday's GDs present no earlier than the third slot
of their room, as Friday's draw requires. Six slots then end before lunch in both rooms, and the
afternoon runs follow-ups, closure and the week close with its reserve.

```mermaid
flowchart TB
    subgraph M["<b>Morning, 180 min</b>"]
      O["<b>Opening, both rooms</b><br/>10 min"]
      L1["<b>Leader's room</b><br/>5 slots, 150 min<br/>then reserve 20"]
      E1["<b>Expert's room</b><br/>3 GD rounds, 90 min<br/>then 2 slots, 60 min<br/>then reserve 20"]
      O --> L1
      O --> E1
    end
    subgraph A["<b>Afternoon, 120 min</b>"]
      E2["<b>Expert's room</b><br/>2 slots, 60 min"]
      G["<b>Grade closure</b><br/>30 min"]
      W["<b>Week close</b><br/>15 min"]
      R["<b>Reserve</b><br/>15 min"]
      E2 --> G --> W --> R
    end
    M --> A
```

| Minutes from the start | Leader's room | Expert's room |
|---|---|---|
| 0 to 10 | Opening, together: the order, the slot, the demo rules, and the silent-teammate rule said aloud | (together) |
| 10 to 160 | Five slots of 30: the larger two clusters and the single group, or the cluster the room rule gives | GD rounds, 10 to 100: three of 30 minutes each |
| | | Two slots of 30, 100 to 160: the first cluster of two |
| 160 to 180 | Reserve: silent-teammate follow-ups, the leader's scores finalised and signed | Reserve: silent-teammate follow-ups, the GD scores entered |
| Lunch | The leader's scoring is complete; the leader may leave for the flight from here | |
| Afternoon 0 to 60 | The leader joins the expert's room if still on campus, as a second pair of ears; the expert's scores stand | Two slots of 30: the second cluster of two |
| 60 to 90 | Grade closure, together (steps below) | |
| 90 to 105 | Week close, together | |
| 105 to 120 | Reserve for anything that ran over; unused, the day ends here | |

**The opening, in words the Programme Head can say.** "Every group presents once, for 17 minutes,
with a live demo run cold on the raw files. The panel then asks for eight to ten minutes, and the
panel chooses who answers. Where two groups took the same sub-problem, they present one after the
other, so the panel hears two honest answers to the same question. Nobody is told anything about
another group's work until the week close."

## Plan B: the clusters are 3, 3 and 3 (three sub-problems, three groups each)

Three-group clusters need 90 minutes each at 30-minute slots, and two of them do not fit one
morning. So Plan B runs the slot at 28 minutes (17, then 8 of questions, then 3) and opens in five.

| Minutes from the start | Leader's room | Expert's room |
|---|---|---|
| 0 to 5 | Opening, together | (together) |
| 5 to 173 | Two clusters, six slots of 28: cluster one, then cluster two | GD rounds, 5 to 95: three of 30 minutes each |
| | | One cluster, three slots of 28, 95 to 179 |
| to 180 | The leader's scores signed | The expert's scores recorded |
| Afternoon 0 to 30 | Silent-teammate follow-ups for both rooms, then every score entered | |
| 30 to 60 | Reserve for anything the morning pushed | |
| 60 to 90 | Grade closure, together | |
| 90 to 105 | Week close, together | |
| 105 to 120 | Reserve; unused, the day ends here | |

The morning has no slack in Plan B, so its overrun rule is strict: question time stops at eight
minutes, and anything the morning cannot hold moves to the afternoon's first reserve.

---

## Scoring as it rolls

Each slot's score is recorded in its own changeover, because a panel that
scores nine groups from memory scores the last three against the first six.

| Step | Who | Where |
|---|---|---|
| The panel scores the group's four group criteria once, out of 34, and each learner's presentation and defence out of 6, after the slot and never in front of the group | The panel chair | `rubrics/C2_W03_SAT_mini_project_scoring_TRAINER.xlsx`, sheets Groups and Learners; Friday's first tranche is already in the same sheet |
| The scribe copies each learner's total out of 40, once, into the grade closure workbook | Trainer (expert's room), Academic TA (leader's room) | `rubrics/C2_W03_SAT_grade_closure_TRAINER.xlsx`, sheet Scores, column Mini project |
| Each Saturday GD round is scored per learner in Friday's GD sheet, then each total out of 30 is copied once | The expert or the Principal Advisor scores; the trainer copies | `content/W03/D5/rubrics/C2_W03_D05_gd_scoring_sheet_TRAINER.xlsx`, then the closure workbook's GD column |
| A learner flagged silent is questioned in the reserve before that learner's presentation and defence score is entered; the group's 34 does not wait | The panel chair, with the scribe | The Learners sheet, then the closure workbook; each cell entered once, after the follow-up |

**The rubric the panels score against.** The requester approved Build 1's rubrics on 29 September
2026 (`data/programme/facts.yaml`, evaluation.rubrics.W03), and learners may see them. The group part
is where a missed plant shows (the data and the analysis); presentation and defence is where a silent
teammate shows.

<!-- sync:rubric:W03/mini-project -->
**Mini project, 40 marks.** The first four criteria are scored once for the group, and every member receives those 34 marks; presentation and defence is scored for each learner on 6 marks, so a silent teammate cannot ride the group's score.

| Criterion | Marks | What full marks look like |
|---|---|---|
| The question translated | 8 | Dr Menon's words are mapped to the right Weeks 1 and 2 method, with the metric defined and the decision it feeds named. |
| The data made trustworthy | 10 | The data is profiled before it is touched, every cleaning call is in the decisions log with its reason, and counts and rupees reconcile across files. |
| The analysis | 10 | The tree, ladder or fair comparison reaches the branch that explains the symptom, on the right denominator, with a chance test where one is needed. |
| The claim | 6 | One sentence carries its number, denominator, period and caveat, plus an action Dr Menon can take. |
| Presentation and defence | 6 | The live demo runs cold, and every member answers a challenge on the caveat. |
<!-- /sync:rubric:W03/mini-project -->

---

## Grade closure, 30 minutes, step by step

The graded components that close today are the GD score, the mini project score including the
presentation, and the mock score. Every learner holds three scores when closure ends.

| Minutes | Step | Who | The check that says it is done |
|---|---|---|---|
| 0 to 5 | Both scribes confirm every slot and every GD round is entered, and read out any seat whose status is not COMPLETE | Trainer and Academic TA | The Checks sheet lists each seat that is short, by seat |
| 5 to 15 | Every flag is cleared at its source: MISSING means find the signed sheet and enter it; OVER MAX or NOT A SCORE means re-read the signed sheet and correct the one cell | Programme Head, with the scribe who entered it | The Checks sheet's MISSING, OVER MAX and NOT A SCORE counts are all zero |
| 15 to 20 | A learner who missed an event (absent for the mock or the GD) is recorded in the Notes column with the Programme Head's decision; this pack sets no make-up rule, because none is published | Programme Head | Every seat without three scores carries a note |
| 20 to 25 | Each assessor role marks its column signed, in the Sign-off sheet: the GD assessors, both panels and the mock assessors | Each assessor present; the Programme Head signs for any who have left, from their signed paper sheets | The Checks sheet's verdict reads READY TO SIGN |
| 25 to 30 | The Programme Head signs the closure and saves the signed copy where the programme keeps its grade records | Programme Head | The Sign-off sheet shows the closure signed |

**Never commit the filled workbook to this repository.** It holds learners' scores, and the
repository is public. The committed file is the empty template with 35 seats and no names.

**Scores are not read aloud in the room.** How and when a learner sees their Build 1 scores is the
Programme Head's decision, and no source in this repository sets it.

---

## The week close, 15 minutes

The deck is `slides/C2_W03_SAT_week_close_STUDENT.md`; the trainer's notes for it, which carry what
the room found, are `trainer/C2_W03_SAT_week_close_notes_TRAINER.md`.

| Minutes | What happens |
|---|---|
| 0 to 4 | What the week trained: the same method, in a business nobody had seen |
| 4 to 12 | One improvement per group for Build 2: each group says its one change in one sentence, and the trainer writes all nine where the room can see them |
| 12 to 15 | The bridge: Monday is Week 4, back in Kalpa Retail, where Meera's growth plan needs its metric |

---

## What moves when the day goes wrong

**The order of cuts, when a room runs late.** Cut in this order, and stop as soon as the room is back
on time: the room's reserve first; then the changeover, from three minutes to one, with scores
recorded in the next reserve; then the week close, from 15 minutes to 10, keeping the nine
improvements and saying the bridge in one sentence. Never cut a group's question time below eight
minutes, never cut grade closure below 20, and never move a group out of its sub-problem's run.

| What happens | What moves |
|---|---|
| A group runs past 17 minutes | The scribe stops it at 17; the group keeps its question time, and nothing else in the room moves. |
| A room is 10 minutes behind after two slots | The changeover drops to one minute for the rest of the morning, and scores go into the reserve. |
| A room is 20 minutes behind at the end of the morning | The reserve absorbs it; in Plan A the leader's room has 20, and in Plan B the afternoon's first 30. |
| A GD round overruns | The next GD starts late and the expert's first slot slides with it; the expert's afternoon slots stay where they are, because the leader's room has the slack. |
| More than three GD rounds remain | The Principal Advisor runs the fourth and any after it online, in parallel with the expert's rounds, from minute 10. |
| The leader is not in the room when the day opens | The expert starts presentations in the expert's room at once, and the Principal Advisor takes the remaining GDs online. The leader's room starts on arrival and slides by the delay; up to 20 minutes late fits the morning's reserve, and up to 80 fits once the afternoon's first hour takes the leader's last two slots. |
| The leader cannot come at all | The expert hears every group alone at 25-minute slots (17, then 6 of questions, then 2): six in the morning after the opening and three in the afternoon, with the GDs online with the Principal Advisor. Closure and the week close keep their 30 and 15. |
| The leader has to leave before their last slot | The leader's unheard groups move to the expert's afternoon, which holds two more slots before closure; the leader signs the scores already given before leaving. |
| A demo machine fails before the demo starts (hardware or Codespace, not the group's code) | The Academic TA swaps to a spare machine; if none works, the group presents and its demo runs in the room's reserve, cold, before the same panel. |
| A group's demo code fails on its one run | The rule holds: the group says in one sentence what broke and why, and goes to questions. There is no second run. |
| A learner is absent | The group presents without them; the Programme Head records the absence in the workbook's Notes column at closure. |
| A group disputes a score in the room | Nothing is argued in the room. The Programme Head notes the dispute and handles it after closure. |
| The group count is not nine | The day holds nine groups. At the tracker's fifteen (three per sub-problem, fifteen groups) it does not fit 300 minutes, and the Programme Head decides the cut before Friday's close. |

---

## After the day

| What | Who |
|---|---|
| The nine improvements, as written on the board, go into Build 2's first-day sheet | Trainer |
| The flagged-silent list and the absences go to the Programme Head with the signed workbook | Academic TA |
| The board card for this day moves on once the pack's pull request merges: `python3 scripts/board_sync.py --status W03/SAT review-1` | Whoever merges the pack |
