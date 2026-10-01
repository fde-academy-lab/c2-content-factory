# Where does your group stand this morning: what did the files hold, what have you matched, and what will your claim be counted on?

- **For:** every group, at the first 30 minutes of Wednesday 21 October
- **From:** Dr Priya Menon, chief operating officer (COO) of Kalpa Health, and the trainer
- **Data:** the ten files in `content/W03/D1/data/`, exported on Friday 16 October 2026

Kalpa Health, Kalpa Group and everyone in them are fictional, and every record in the files is
synthetic. Kalpa Health is a US diagnostics business: a laboratory and two patient service centres,
where a phlebotomist draws patients' blood, in each of six US metro areas, billing its patients'
payers in dollars (commercial health plans, Medicare, Medicaid and patients who pay for themselves).
Its revenue-cycle and analytics work runs from Kalpa's Global Capability Centre (GCC) in Bengaluru,
where you work as trainee engineers in the data and AI team. Q2 is April to June 2026 and Q3 is July
to September 2026. The domain dossier,
`content/W03/D1/study-notes/C2_W03_D01_domain_us_healthcare_STUDENT.md`, tells the whole business,
with its words in section 6 and its numbers and their formulas in section 5.

> "My dashboard says test volumes grew 5 percent from Q2 to Q3. The plan the board approved asks for
> 18. Which branch of my business is short, and what do I do next?"
> Dr Priya Menon, COO, Kalpa Health

Five of Dr Menon's heads asked her a question, and on Monday each group took one. Today each group
builds on the files: the checkpoint first, then the trainer's parallel build on a question no group
holds, then build time, and at the day's close each group states its headline claim, one sentence
Dr Menon can carry into her board meeting.

**Who needs the answer.** Your group first, then the Academic TA and the trainer. Tomorrow every
member sits Mock R1 alone, with a viva on the group's own work, so a group that cannot answer its
three questions this morning is stuck, and a blocker named today gets help a day before the viva.

**The questions on the way.** How does the checkpoint run, and what counts as an answer? What do
all fifteen questions ask, whichever brief your group holds? What are the three questions for each
of the five briefs? What does a group do when it cannot answer one?

---

## How does the checkpoint run, and what counts as an answer?

**Who needs the answer.** Every member: a different member answers each question, so everyone
needs the group's numbers in front of them.

**The questions on the way.** In what order do groups answer? How long does each group have? What
does an answer have to contain?

| Rule | What it means |
|---|---|
| The order | Groups answer by brief, 1 to 5, so the groups that share a brief answer back to back. |
| The time | Two minutes per group, three questions. The trainer stops a group at two minutes, mid-sentence if need be. |
| Who speaks | One member per question, and a different member for each of the three. |
| An answer | A number, the file it came from, and what you counted as one row or one record when you counted it. |
| Not yet | "Not yet, because..." with what is in the way is an answer. A guess is not. |
| What it costs | Nothing: the checkpoint is not scored. This week's scored events are the mini project, Mock R1 on Thursday 22 October and the group discussion on Friday 23 and Saturday 24 October. |

Each group answers from its own notebook or SQL, run today. Nobody at the checkpoint says whether
a number is right; the trainer may ask one question back, and the next group starts.

## What do all fifteen questions ask, whichever brief your group holds?

**Who needs the answer.** Every group, before it reads its own three: the same three moves sit
under every question, so a group can prepare for its set by checking these three in its own work.

**The questions on the way.** What did the files hold? What did you match against what? What will
each number in your claim be counted over?

| | What it asks | The Week 1 or 2 move behind it |
|---|---|---|
| The first | What did your files hold when you profiled them, before you changed anything? | Week 1 Wednesday: profile every field before touching it, and count rows against distinct ids |
| The second | What did you match against what, and what was left over on each side? | Week 1 Wednesday: rows in equal rows kept plus rows set aside; Week 2 Tuesday: a join is counted before anything is summed |
| The third | What will each number in your claim be counted over, and compared with what? | Week 1 Monday: every branch a count over a denominator; Week 1 Thursday: the count beside every rate, and the comparison that is fair |

## Brief 1, for the revenue groups: what do the claims hold, what did you match them to, and what is each branch of your tree counted over?

> "The board will ask me where the plan's growth went. Where does our lab revenue actually come
> from, and which branch of it is short?"
> The finance head, Kalpa Health

A claim is the bill for one completed booking, sent to the patient's payer at Kalpa Health's list
prices, plus any collection fee for a home draw, and billed revenue is the dollars on the claims. A
branch is one part of the revenue tree: a count or a ratio whose change shows how much of the growth
it carries.

**Who needs the answer.** The finance head, who writes the board's page on where the plan's growth
went; a branch named on a number nobody can rebuild sends the recovery effort to the wrong place.

**The questions on the way.**

1. **What did the claims file hold when you profiled it?** How many rows and how many distinct
   claim ids, how many values in each column you use converted to the type the data dictionary
   gives, and what are the smallest and the largest billed amounts? *The move: Week 1 Wednesday,
   profile every field before touching it.*
2. **What did you match the claims against, and what was left on each side?** Which count from the
   booking side did you put beside the claims, how many matched, and what is every claim or
   booking left over? *The move: Week 1 Wednesday, rows in equal rows kept plus rows set aside, and
   Week 2 Tuesday, a join counted before anything is summed.*
3. **What is each branch of your tree counted over?** Name every count and every average on your
   tree with its denominator and its Q2 and Q3 values, and put the median beside every average.
   *The move: Week 1 Monday, the revenue tree with every branch a count over a denominator, and a
   typical value that one large order cannot move.*

## Brief 2, for the bookings groups: what do the booking files hold, what did you check the fall against, and what is one booking in your count?

> "Bookings fell in two of our metros in Q3. Before I send a field team or cut staff there, I need
> to know how far they fell, and why."
> The patient service centres' operations head, Kalpa Health

A booking is one patient's visit to have one or more tests done, and it ends completed or cancelled.
A field team is operations staff sent to a metro to see on the ground what is happening.

**Who needs the answer.** The operations head, who decides this month whether to send a field team
or cut staff; a fall read too large cuts staff that patients still need.

**The questions on the way.**

1. **What did each booking file hold when you profiled it?** For each booking file you opened: how
   many rows, how many distinct booking ids, and which metros and which dates it covers. *The move:
   Week 1 Wednesday, profile every field before touching it, and count rows against distinct ids.*
2. **Before you explained the fall, what did you check it against?** Metro by metro and quarter by
   quarter, which second count did you put beside the bookings, and where did the two disagree?
   *The move: Week 1 Tuesday, rung 1 of the investigation ladder, confirm the drop before anyone
   explains it.*
3. **What is one booking in your count?** State the fall in each of the two metros as a Q2 count
   and a Q3 count, name the file or files each count comes from, and say what you counted as one
   booking. *The move: Week 1 Tuesday, rung 2, like with like: the same definition in both
   quarters.*

## Brief 3, for the billing groups: what does each file's row stand for, what did your join match, and which postings count as money received?

> "The claims we billed say one thing and the posting system says another. Which claims are unpaid,
> how much money is that, and can I trust the figure I report?"
> The finance head, Kalpa Health

A remittance is a payer's answer to a claim, and the posting system records it as postings, one row
each: money received (a payment), a refusal (a denial) or money taken back (a reversal). A payer's
filing deadline is the time after the service within which it must receive the claim.

**Who needs the answer.** The finance head, who reports the collections figure at the quarter's
close under their own name; a claim chased late can pass its payer's filing deadline and never be
paid.

**The questions on the way.**

1. **What did the claims and the remittances hold when you profiled them?** What is one row of
   each file, how many rows does each hold, and what values do the columns you use take? *The move:
   Week 1 Wednesday, profile every field before touching it.*
2. **When you joined the postings to the claims, what matched and what was left?** How many
   postings matched a claim, how many postings and how many claims were left unmatched, and what is
   each leftover? *The move: Week 2 Tuesday, a join counted before anything is summed, and Week 1
   Wednesday, rows in equal rows kept plus rows set aside.*
3. **Which postings count as money received, and which claims as unpaid?** Give the rule for each
   class you defined (paid, part paid, denied, unpaid) and the count of claims and the dollars in
   each. *The move: Week 2 Tuesday, booked against collected: which total is which, and what each
   one counts.*

## Brief 4, for the no-show groups: what does the visit register hold, what did you check it against, and what is each centre's rate out of?

> "KH-ATL-03, one of our two Atlanta patient service centres, has the worst no-show rate on my Q3
> report. I am being asked to add a receptionist there or close it. Is the centre really worse?"
> The patient service centres' operations head, Kalpa Health

The visit register records each Q3 visit a booking brought to a patient service centre. A no-show is
a visit the register records as not attended, and the report's no-show rate is the share of a centre's
Q3 visits recorded that way.

**Who needs the answer.** The operations head, who chooses between a receptionist, reminder calls
and a closure notice; a centre closed on a rate read wrongly takes a neighbourhood's nearest blood
draw away.

**The questions on the way.**

1. **What did the visit register hold when you profiled it?** How many rows does each centre have,
   and what values does each column take? *The move: Week 1 Wednesday, profile every field before
   touching it.*
2. **What did you check the register against, and did it agree?** Did every visit find its
   booking, at the same centre, and does every Q3 booking at a centre find its visit? *The move:
   Week 1 Wednesday, reconcile one file against another, both ways.*
3. **What is each rate out of?** Give KH-ATL-03's no-show rate and the other centres' as a count
   over a count, say which visits sit in each denominator, and say how often chance alone would
   make a gap that size on that many visits. *The move: Week 1 Thursday, the count beside every
   rate, and real or noise: how often chance alone makes the gap.*

## Brief 5, for the campaign groups: who got the offer, did every offered patient match the register, and what is the 9 percent counted over?

> "Our free at-home collection offer lifted bookings 9 percent. I want to offer it to every patient
> in all six metros. Can you confirm it worked?"
> The marketing head, Kalpa Health

The offer was a free collection at home, where a phlebotomist draws the sample in the patient's home
with the visit's fee waived. Offered means on marketing's list, and the report's lift is the offered
patients' bookings per patient over the weeks the offer ran, divided by every other registered
patient's over the same weeks, minus one.

**Who needs the answer.** The marketing head, who wants the offer for every patient, and Dr Menon,
who signs its cost; every free collection sends a phlebotomist to a patient's home, so an offer
extended on a lift it did not cause spends that money every week.

**The questions on the way.**

1. **Who got the offer, and when?** How many patients were offered, in which metros, between which
   dates, and how many accepted? *The move: Week 1 Thursday, who got the sale, asked before whether
   it worked.*
2. **Did every offered patient match the patient register and the bookings?** Did each one appear
   in the register in the same metro, and how many had a booking in the weeks the offer ran? *The
   move: Week 1 Wednesday, reconcile one file against another, and Week 2 Tuesday, a join counted
   before anything is summed.*
3. **What is the 9 percent counted over, and compared with whom?** Bookings per patient over which
   weeks, for which patients, against which other patients, and how did the two groups compare
   before the offer was sent? *The move: Week 1 Thursday, cause or coincidence: were the two groups
   alike before the thing tested?*

## What does a group do when it cannot answer one of its three?

**Who needs the answer.** The group, and the Academic TA, who runs the open build time after the
second block and takes the stuck groups first.

**The questions on the way.** What does the group say? Who comes to its table, and when?

Say which question you cannot answer and what is in the way, in one sentence: "We cannot answer
the second question yet, because our join leaves rows we cannot explain." That sentence is a
blocker, and the trainer writes it beside your group's name. The trainer comes to your table first
in the morning's build time and the Academic TA first in the open build time, and the blocker goes
into your challenges log, `content/W03/D1/briefs/C2_W03_D01_challenges_log_STUDENT.xlsx`, with
today's date. A blocker named in your two minutes reaches the trainer before the parallel build; one
kept quiet waits until the close, when the day's build time has gone.
