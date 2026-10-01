# What one sentence can your group give Dr Menon tonight, with its number, its denominator, its period and its caveat?

- **For:** every group, at the close of Wednesday 21 October
- **From:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health
- **Data:** the ten files in `content/W03/D1/data/`, exported on Friday 16 October 2026

Kalpa Health and everyone in it are fictional, and every record in the files is synthetic. Kalpa
Health is a US diagnostics business in six US metro areas, billing its patients' payers in dollars,
with its analytics work run from Kalpa's Global Capability Centre (GCC) in Bengaluru, where you work
as trainee engineers. Q2 is April to June 2026 and Q3 is July to September 2026.

> "I want one answer per question: a sentence I can carry into the board meeting, the evidence
> behind it, what would change it, and what you would have me do."
> Dr Priya Menon, COO, Kalpa Health, in her briefing note of Monday 19 October

Each group took one of her heads' five questions on Monday, and each states its headline claim at
today's close, in about a minute. It is stated today, before it is fully tested, because Thursday's
mock and the panel on Friday and Saturday test it; a claim first stated on Thursday has had no
testing at all.

**Who needs the answer.** Dr Menon, who repeats the sentence to her board with nobody there to
explain it, so a number without its base or its period becomes the board's number. Then every member
of your group: tomorrow's viva and the weekend's panel start from the sentence you pin tonight.

**The questions on the way.**
1. What must one sentence carry for Dr Menon to repeat it safely?
2. What does a finished claim look like, on a question no group holds?
3. Which wrong versions of that claim would a hurried analyst send, and what is wrong with each?
4. Which six tests does your sentence pass before you pin it?
5. What does your group say at the close if its claim is not ready?
6. How is the claim scored, and when?
7. What do you take home tonight?

---

## What must one sentence carry for Dr Menon to repeat it safely?

**Who needs the answer.** The member who says your claim aloud at the close, and Dr Menon, who has
two minutes and no chart.

**The questions on the way.** Which parts go in the sentence? Which go on the lines below it? In
what order?

The sentence carries four things, and the reason that connects them:

| Part | What it is | Why Dr Menon needs it |
|---|---|---|
| **The number** | The change or the level you found, in its unit: dollars, bookings, claims, visits, patients or a rate | It is what she will repeat |
| **The denominator** | What every rate or average is out of, both sides of any comparison, in counts someone can check | A rate with no base cannot be checked or compared |
| **The period** | Which weeks or quarters, and whether the windows are the same length | "Up 8 percent" over unequal windows is a different number from the pace |
| **The caveat** | The one thing that would change the claim, on its own line below the sentence | The panel will ask what would change the claim, and a group that wrote it down answers in a sentence |

The shape is Week 1 Thursday's note, claim first, because a COO reads the first line and may stop:

```
CLAIM      one sentence: the number, what it counts, its denominators, the period, and the reason
EVIDENCE   what you computed, from which files, on how many rows after which identity rule
CAVEAT     the one thing that would change the claim, on its own line
ACTION     what Dr Menon should do, and what it costs or what it needs next
```

The sentence you say at the close is the CLAIM line. The CAVEAT goes on the line below it and is
never folded into the claim.

## What does a finished claim look like, on a question no group holds?

**Who needs the answer.** Every group, as a model of the claim's shape: it answers a question none
of the five briefs asks, so its numbers belong to no group.

**The questions on the way.** What did the trainer's parallel build find? How do the four parts sit
on the page?

This morning's parallel build took one metro's billed revenue, New York's, from Q2 to Q3. Billed
revenue is the dollars on the claims at Kalpa Health's list prices, what it asked the payers for;
the payers pay a contracted share of it weeks later, a road the domain dossier,
`content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, follows from list price
to cash in its section 3. The build kept one row per booking under an identity rule, one written
rule for what makes two rows one record (here, one booking id is one booking), converted every
amount, matched the claims one to one to the completed bookings and split billed revenue into
claims times the mean claim, the average dollars on one claim.

| Part | New York, Q2 against Q3 |
|---|---|
| **Claim** | New York's billed revenue rose 5.5 percent, from $174,910 on 977 claims in Q2 to $184,485 on 1,055 claims in Q3, because it billed 78 more claims at a mean claim $4.16 lower. |
| **Evidence** | The old booking export's 2,128 New York rows are 2,095 bookings under one identity rule; the 2,032 completed bookings match the 2,032 claims one to one; every amount converts; the same totals come out of SQL run on the raw files; the change splits into $13,964 from more claims and minus $4,389 from the lower mean. |
| **Caveat** | Billed revenue is list price, which the payers do not pay in full, so this is not money collected; and Q3 has 92 days to Q2's 91, so per day billed revenue rose 4.3 percent. Why the mean claim fell is not yet known. |
| **Action** | Report New York as growing on claim volume, and open the branch below the mean claim before calling the lower mean a price or a mix change. |

The claim names its unit (billed revenue, claims), carries both denominators (977 and 1,055
claims), its period (Q2 against Q3) and its reason (more claims at a lower mean). "New York up 5.5
percent" alone would not survive one question from the finance head.

## Which wrong versions of that claim would a hurried analyst send, and what is wrong with each?

**Who needs the answer.** Every group, before it reads its own sentence the same way: each wrong
version below is a plausible number the New York build met this morning.

**The questions on the way.** What does each sentence count? Over which period? Could anyone rebuild
it from the raw files?

| The sentence | What is wrong with it | The test it fails, from the next section |
|---|---|---|
| "New York grew 5.5 percent." | No unit, no base and no period: 5.5 percent of what, out of what, from when? | 2, 3 and 4 |
| "New York's bookings grew 4.8 percent from Q2 to Q3." | It counted the export's rows as bookings; 33 bookings appear on two rows, and counted once each the bookings grew 6.8 percent | 2 |
| "New York's billed revenue grew 3.3 percent, from $179,499 to $185,354." | The totals come from a join that matched some claims twice, so they count export rows, $5,458 more than the claims themselves hold | 2 |
| "New York collected $184,485 in Q3, up 5.5 percent." | It calls billed revenue money collected; the payers pay a contracted share, and later | 2 |
| "New York is growing at 8.0 percent a quarter on claims." | Q3 has a day more than Q2; per day the claims grew 6.8 percent | 4 |

## Which six tests does your sentence pass before you pin it?

**Who needs the answer.** Your group, before the close: a claim that fails one test is not ready, and
the fix is almost always a smaller claim.

**The questions on the way.** Does it reproduce? Does it say what it counts? Does it carry its
bases? Do its windows match? Does it say what it cannot? Is it a claim and not a plan?

| Test | The question to put to your sentence |
|---|---|
| **1. It reproduces** | Does one notebook or SQL file, run cold from the raw files, print every number in the sentence? |
| **2. It names what it counts** | For every number: bookings, claims, tests, patients, visits, postings or dollars, and counted after which identity rule? |
| **3. It carries its denominators** | Does every rate show its base, both sides of any comparison, in counts someone can check? |
| **4. The windows match** | Are the two periods the same length and the same kind? If not, does the sentence say so, or give the rate per day? |
| **5. It says what it cannot** | Is there one caveat, on its own line, that names what would change the claim, and would Kavya Nair, the senior analyst on your team, accept it as the real risk? |
| **6. It is a claim and not a plan** | Can Dr Menon repeat it without a chart, and does it stop before recommending more than the evidence carries? |

**Kavya's review.** A claim that passes all six has the count you started from, every row you set
aside with its reason, and a second way to reach the same total. If one of the three is missing,
say so in the caveat, so the panel hears it from your group first.

## What does your group say at the close if its claim is not ready?

**Who needs the answer.** A group whose build is behind, which still owes Dr Menon a sentence and
owes the trainer its blocker.

**The questions on the way.** Is a smaller claim acceptable? When is "not yet" the answer? What does
a blocker sound like?

A smaller claim that keeps its denominators and its caveat is a finished claim: one metro instead of
six, one quarter's count instead of a full tree. Week 1 Thursday's "not yet" is also an answer, if it
says what would turn it, the way the New York build left its own open question: "Not yet: New York's
mean claim fell $4.16, and we will know whether that is price or mix once the branch below the claim
is opened." If your group has neither, name the blocker in one sentence: which of this morning's
three checkpoint questions you still cannot answer, and what is in the way. The Academic TA starts
the open build time at the tables that named one.

## How is the claim scored, and when?

**Who needs the answer.** Every member: the claim is scored once for the group at its
presentation, on Friday 23 or Saturday 24 October, and every member defends its caveat alone.

**The questions on the way.** Which criterion scores it? What do full marks look like?

The mini project's rubric, which the requester approved on 29 September 2026 for learners to see.
The sentence you pin tonight is the one its fourth criterion, the claim, scores, and the six tests
above are what its full-marks line asks for.

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

## What do you take home tonight?

**Who needs the answer.** Your group, before Thursday's mock, where each member's viva starts from
tonight's sentence.

**The questions on the way.** What is tonight's task? What does every group ship by the end of the
week?

Tonight's task is the presentation skeleton on the same four parts, claim, evidence, caveat and
action, with one line under each, and closing whatever gap in the evidence today's claim exposed.
The trainer hands out the presentation format at the close. By the end of the week every group
ships:

| What | What it holds |
|---|---|
| The presentation | A slot of 25 to 30 minutes, with a live demo run cold on your own copy of the Kalpa Health files, and the panel's questions to every member |
| The one-slide answer | The slide Dr Menon carries into her board meeting: claim, evidence, caveat and action |
| The reproduction | The notebook or SQL that rebuilds every number from the raw files, top to bottom |
| The decisions log | Every cleaning and matching call in the Week 1 Wednesday shape (field, issue, rows, decision, reason), with at least one row kept as it was, in `content/W03/D1/briefs/C2_W03_D01_decisions_log_STUDENT.xlsx` |
| The challenges log | Every obstacle and open question, dated as it happened, in `content/W03/D1/briefs/C2_W03_D01_challenges_log_STUDENT.xlsx` |
