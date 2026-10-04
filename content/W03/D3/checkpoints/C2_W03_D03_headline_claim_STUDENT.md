# What one sentence can your group give Dr Menon tonight, with its number, its denominator, its period and its caveat?

- **For:** every group, at the close of Wednesday 21 October
- **Client:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health
- **Data:** the ten files in `content/W03/D1/data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic. Kalpa
Health is a US diagnostics business in six US metro areas. It bills its patients' payers in dollars,
and a payer is whoever pays for a patient's tests: a commercial health plan, Medicare (the federal
programme for people aged 65 and over), Medicaid (each state's programme for people on low incomes)
or the patient. Its analytics work runs from Kalpa's Global Capability Centre (GCC) in Bengaluru,
where you work as trainee engineers. Q2 is April to June 2026 and Q3 is July to September 2026.

Today the word claim means two things, so this sheet keeps them apart. A claim is the bill Kalpa
Health sends a payer for one completed booking, at its list prices. Your group's headline claim is
the one sentence it states at today's close.

> "I want one answer per question: a sentence I can carry into the board meeting, the evidence
> behind it, what would change it, and what you would have me do."
> Dr Priya Menon, COO, Kalpa Health, in her briefing note of Monday 19 October

Each group took one of her heads' five questions on Monday, and each states its headline claim at
today's close, in about a minute. It is stated today, before it is fully tested, because Thursday's
mock interview and the panel on Friday and Saturday test it; a headline claim first stated on
Thursday meets its first test in the mock itself.

**Who needs the answer.** Dr Menon, who repeats the sentence to her board with nobody there to
explain it, so a number without its base or its period becomes the board's number. Then every member
of your group: tomorrow's viva, the spoken defence of your group's work that closes each member's
mock interview, and the weekend's panel start from the sentence you pin tonight.

**The questions on the way.**
1. What must one sentence carry for Dr Menon to repeat it safely?
2. What does a finished headline claim look like, on New York's billed revenue?
3. Which six tests does a sentence pass before you pin it?
4. Which wrong versions of New York's headline claim would a hurried analyst send, and which test does each fail?
5. What does your group say at the close if its headline claim is not ready?
6. How is the headline claim scored, and when?
7. What do you take home tonight, and what reaches you for Thursday's mock?

---

## What must one sentence carry for Dr Menon to repeat it safely?

**Who needs the answer.** The member who says your headline claim aloud at the close, who has about
a minute, and Dr Menon, who has two minutes and no chart. A sentence that leaves out its base or its
period reaches the board without them, and the board acts on a number nobody can check.

**The questions on the way.** Which parts go in the sentence? Which go on the lines below it? In
what order?

The sentence carries three parts and the reason the evidence gives for them, and a fourth part goes
on the line below it:

| Part | What it is | Why Dr Menon needs it |
|---|---|---|
| **The number** | The change or the level you found, in its unit: dollars, bookings, claims, visits, patients or a rate | It is what she will repeat |
| **The denominator** | What every rate or average is out of, both sides of any comparison, in counts someone can check | A rate with no base cannot be checked or compared |
| **The period** | Which weeks or quarters, and whether the windows are the same length | "Up 8 percent" over unequal windows is a different number from the pace |
| **The caveat** | The one thing that would change the headline claim, on its own line below the sentence | The panel will ask what would change the claim, and a group that wrote it down answers in a sentence |

The shape is Week 1 Thursday's note, claim first, because a COO reads the first line and may stop:

```
CLAIM      one sentence: the number, what it counts, its denominators, its period,
           and the reason, stated no more strongly than the evidence allows
EVIDENCE   what you computed, from which files, on how many rows after which identity rule
CAVEAT     the one thing that would change the claim, on its own line
ACTION     what Dr Menon should do, and what it costs or what it needs next
```

The sentence you say at the close is the CLAIM line, your headline claim. The CAVEAT goes on the
line below it and is never folded into the claim.

## What does a finished headline claim look like, on New York's billed revenue?

**Who needs the answer.** Every group, before it writes its own. A sentence written without a model
usually drops its base or its period, and the finance head throws it out with one question. The New
York build takes brief 1's method to one metro of six, so its moves serve every brief, and a revenue
group still builds its own tree across all six metros and every branch.

**The questions on the way.** What did the trainer's parallel build find? How do the four parts sit
on the page?

This morning's parallel build took one metro's billed revenue, New York's, from Q2 to Q3. Billed
revenue is the dollars on the claims at Kalpa Health's list prices, what it asked the payers for.
The payers pay a contracted share of it weeks later, and section 3 of the domain dossier,
`content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, follows one claim from its
list price to the cash. The build counted New York's rows in the old booking export, the file from
the booking system Kalpa Health has used since before Q2. It kept one row per booking under an
identity rule, one written rule for what makes two rows one record (here, one booking id is one
booking), converted every amount, matched the claims one to one to the completed bookings and split
billed revenue into claims times the mean claim, the average dollars on one claim.

| Part | New York, Q2 against Q3 |
|---|---|
| **Headline claim** | Over Q2's 91 days and Q3's 92, New York's billed revenue rose 5.5 percent, from $174,910 on 977 claims to $184,485 on 1,055 claims, carried by 78 more claims at a mean claim $4.16 lower. |
| **Evidence** | The old booking export's 2,128 New York rows are 2,095 bookings under one identity rule; the 2,032 completed bookings match the 2,032 claims one to one; every amount converts; the same totals come out of SQL run on the raw files; the change splits into $13,964 from more claims and minus $4,389 from the lower mean; per day, billed revenue rose 4.3 percent. |
| **Caveat** | Billed revenue is list price, and the payers pay a contracted share of it weeks later, so the money collected may have grown by more or less than 5.5 percent. |
| **Action** | Report New York as growing on claim volume, and open the branch below the mean claim to learn why it fell before anyone calls the lower mean a price or a mix change. |

The headline claim names its unit (billed revenue, counted in claims), carries both denominators
(977 and 1,055 claims), its period (Q2's 91 days against Q3's 92) and the branch that carried the
change (more claims at a lower mean), which says where the change sits and claims no cause. "New
York up 5.5 percent" alone would not survive one question from the finance head.

## Which six tests does a sentence pass before you pin it?

**Who needs the answer.** Your group, before the close. A headline claim that fails one test is not
ready, and the panel finds the failure with its first question; the fix is almost always a smaller
claim.

**The questions on the way.** Does it reproduce? Does it say what it counts? Does it carry its
bases? Do its windows match? Does it say what it cannot? Does it end on an action the evidence
carries?

| Test | The question to put to your sentence |
|---|---|
| **1. It reproduces** | Does one notebook or SQL file, run cold from the raw files, print every number in the sentence? |
| **2. It names what it counts** | For every number: bookings, claims, tests, patients, visits, postings or dollars, and counted after which identity rule? |
| **3. It carries its denominators** | Does every rate show its base, both sides of any comparison, in counts someone can check? |
| **4. The windows match** | Are the two periods the same length and the same kind? If not, does the sentence say so, or give the rate per day? |
| **5. It says what it cannot** | Is there one caveat, on its own line, that names what would change the claim, and would Kavya Nair, the senior analyst on your team, accept it as the real risk? |
| **6. It ends on an action the evidence carries** | Does an action Dr Menon can take follow on its own line, and does it stop where the evidence stops? |

**Kavya's review.** A headline claim that passes all six has the count you started from, every row
you set aside with its reason, and a second way to reach the same total. If one of the three is
missing, say so in the caveat, so the panel hears it from your group first.

## Which wrong versions of New York's headline claim would a hurried analyst send, and which test does each fail?

**Who needs the answer.** Every group, before it reads its own sentence. Each wrong version below is
a plausible number the New York build met this morning, and a group that can name the slip in
another group's sentence catches it in its own before the panel does.

**The questions on the way.** What does each sentence count? Over which period? Could anyone rebuild
it from the raw files? Which of the six tests does it fail?

Read the five sentences, and name the test each one fails before you read the table under them.

1. "New York grew 5.5 percent."
2. "New York's bookings grew 4.8 percent from Q2 to Q3."
3. "New York's billed revenue grew 3.3 percent, from $179,499 to $185,354."
4. "New York collected $184,485 in Q3, up 5.5 percent."
5. "New York is growing at 8.0 percent a quarter on claims."

**What is wrong with each.**

| Sentence | What is wrong with it | The test it fails |
|---|---|---|
| 1 | It gives no unit, no base and no period, so nobody can say 5.5 percent of what, out of what, or from when. | 2, 3 and 4 |
| 2 | It counted the export's rows as bookings; 33 bookings appear on two rows, and counted once each the bookings grew 6.8 percent. | 2 |
| 3 | Its totals come from a join that matched some claims twice, so they count export rows, $5,458 more than the claims themselves hold. | 2 |
| 4 | It calls billed revenue money collected, when the payers pay a contracted share of it, and later. | 2 |
| 5 | Q3 has a day more than Q2, and per day the claims grew 6.8 percent. | 4 |

## What does your group say at the close if its headline claim is not ready?

**Who needs the answer.** A group whose build is behind, which still owes Dr Menon a sentence and
owes the trainer its blocker. A group that says nothing tonight sends its members into tomorrow's
viva with nothing to defend.

**The questions on the way.** Is a smaller claim acceptable? When is "not yet" the answer? What does
a blocker sound like?

A smaller headline claim that keeps its denominators and its caveat is a finished claim: one metro
instead of six, one quarter's count instead of a full tree. Week 1 Thursday's "not yet" is also an
answer, if it says what would turn it, the way the New York build left its own open question: "Not
yet: New York's mean claim fell $4.16, and we will know whether that is price or mix once the branch
below the claim is opened." If your group has neither, name the blocker in one sentence: which of
this morning's three checkpoint questions you still cannot answer, and what is in the way. The
Academic TA starts the open build time at the tables that named one.

## How is the headline claim scored, and when?

**Who needs the answer.** Every member. The headline claim is scored once for the group at its
presentation, on Friday 23 or Saturday 24 October, and each member then defends its caveat alone, for
the 6 marks of presentation and defence that each learner earns for themselves.

**The questions on the way.** Which criterion scores it? What do full marks look like?

The mini project is scored on the rubric below, and your headline claim is its fourth criterion, the
claim, worth 6 of the 40 marks. Its full-marks line asks for one sentence with its number,
denominator, period and caveat, plus an action Dr Menon can take, which is what the six tests check.

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

## What do you take home tonight, and what reaches you for Thursday's mock?

**Who needs the answer.** Your group, before Thursday's mock, where each member's viva starts from
tonight's sentence. A skeleton drafted tonight leaves Thursday's build time for the evidence; one
left until Thursday takes that time.

**The questions on the way.** What is tonight's task? What reaches you at the close for Thursday's
mock? What does every group ship by the end of the week?

Tonight you draft the presentation skeleton on the note's four parts, claim, evidence, caveat and
action, with one line under each, and close whatever gap in the evidence today's headline claim
exposed. The trainer hands out the presentation format at the close.

At the close the trainer also sends you Thursday's mock brief, which says how Mock R1's 20 minutes
run and how to prepare, and the seat list, which gives your slot, its minutes and your assessor.
Mock R1 is a mock interview, one assessor with one learner, in two halves: a technical half on the
Weeks 1 and 2 method, and the viva on your group's work. The first mocks start ten minutes into
Thursday, so read the brief tonight and find your slot before you leave, whenever it falls.

By the end of the week every group ships:

| What | What it holds |
|---|---|
| The presentation | A slot of 25 to 30 minutes, with a live demo run cold on your own copy of the Kalpa Health files, and the panel's questions to every member |
| The one-slide answer | The slide Dr Menon carries into her board meeting: claim, evidence, caveat and action |
| The reproduction | The notebook or SQL that rebuilds every number from the raw files, top to bottom |
| The decisions log | One row for every cleaning and matching call in `content/W03/D1/briefs/C2_W03_D01_decisions_log_STUDENT.xlsx`: the field, the issue, the rows it moved, the decision and the reason, which is Week 1 Wednesday's rule, rows and reason with the field and the issue added, and at least one row records a value kept as it was |
| The challenges log | Every obstacle and open question, dated as it happened, in `content/W03/D1/briefs/C2_W03_D01_challenges_log_STUDENT.xlsx` |
