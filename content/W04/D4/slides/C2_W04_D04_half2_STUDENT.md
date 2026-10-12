# What does Zomato Gold fix first, and how do you walk an interviewer through it?

Week 4, Day 4. Half two.

Header: WEEK 4  ·  DAY 4  ·  ZOMATO GOLD, CHENNAI, AN ILLUSTRATIVE CASE

## SECTION 4: What is fixed first?
*The morning's three chapters found two problems, a dashboard that reads 38 because of who it counts and one broken step on Android; the afternoon's three sections use them and add no new idea. Which problem goes first, on what evidence, at what cost, and what does the app team's lead say?*

```notes
Sixty trainer minutes: the fix-first call unguided (30), the interview walk and the AI-company
variant (15), the Kahoot and the close (15). Then the IITGN faculty session W4-3 runs (tentative),
or the weaned-users fallback if it slips.
LIVE, 30 minutes, unguided, in the nine groups. L5. Styles: the case method (the app team's lead
argues from a role card and is partly right), Feynman (the call in one sentence a membership lead
could repeat).
Transition: the task.
```

---

## S38. The task: one call, five lines, one page
*What does a fix-first call carry, and in what order?*

```timeline
label: 1 | title: The call | body: What gets fixed first, in one sentence
label: 2 | title: The evidence | body: The stage, the segment and the date, each with its number
label: 3 | title: The cost | body: Orders a week and rupees, with every assumption named and ranged
label: 4 | title: The objection | body: The app team's lead, answered with the split that settles it
label: 5 | title: What would change it | body: The one fact that would reverse the order | tone: dark
```

Each group writes the five lines for the membership lead on one page, the fix-first set's page, and then answers its items. After the lab, the Kalpa set's second page asks for the same five lines for Kalpa's head of Retail-Plus. Every number comes from the morning's notebooks.

```notes
LIVE, 4 minutes to set up, then 18 minutes of writing. Circulate with one question per group:
which line of your evidence would the app team's lead attack first? Groups that write "fix
retention" with no stage are sent back to the chapter 3 split.
Transition: the app team's lead.
```

---

## S39. The app team's lead: "our checkout is fine"
*What does the app team's lead claim, what is true in it, and what answers it?*

![Android members: the step that changed is checkout to order](../whiteboards/C2_W04_D04_stage_split_STUDENT.png)

**The claim.** "Carts that start checkout held at 80 percent on every platform, before and after 14 September, so the new flow works." **What is true.** Starting checkout did not break. **What answers it.** Completing the order once checkout has started fell from 72.5 to 55 percent, for members on Android, from the release week. Concede the true part, restate the question, bring the split.

```notes
LIVE, 5 minutes. A learner reads the role card aloud (TRAINER role card); one group answers in
the four moves from Tuesday: restate, answer from the evidence, concede what is true, say what
would change your mind. A response that calls the app team wrong has lost; the chart is right
about the step it measures.
Transition: what each problem costs.
```

---

## S40. What each problem costs, side by side
*How big is each loss, in orders and rupees, and how sure is each number?*

```stats
value: 1,223 to 1,317 | label: orders a week | note: not placed after the release: 22,841 Android member carts in 17 days at 58 against 44 percent, less the point the comparators lost
value: Rs 3.7 to 6.6 lakh | label: of order value a week | note: at Rs 300 to Rs 500 an order, an assumption; Zomato keeps its commission and fees from it
value: 0.23 | label: orders per sale-week member | note: in month one, against 0.61 for an organic August member
value: 33 | label: percent, October | note: the dashboard once the August cohort enters, if it loses July's 10.5 points (32 to 34)
```

The release costs orders every week it stays live, and a code fix ends it. The August cohort's discount is already paid for; what can still change is whether the next sale runs, which waits on whether this one's members pay their discount back.

```notes
LIVE, 4 minutes. Read each number with its assumption. The 1,317 assumes the carts that failed
would have converted at the old rate. If members had retried and ordered later, it would overstate
the loss; they did not: after a checkout with no order, the member ordered within a day 36.5
percent of the time before the release and 35.1 after. Held to members who joined before August,
Android members also ordered less each (1.45 to 1.24 orders per ordering member) while iOS held
(1.44 and 1.45). Ask which number the membership lead can act on this week.
Transition: the wrong fix.
```

---

## S41. The wrong fix: buy more sale members
*What would "fix retention" with more acquisition do to the number, and to the business?*

```mermaid
flowchart LR
    A["<b>another sale</b><br/>a big discounted cohort"] --> B["<b>its month two</b><br/>enters the dashboard's count"]
    B --> C["<b>the dashboard falls again</b><br/>and the discount is spent"]
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class A,B,C bad
```

**What breaks.** "Retention will recover if we run another sale." The next discounted cohort enters the count at its month two and, if it behaves like this one, pulls the dashboard down again at the discount's cost.

**The rule.** Before buying another sale, work out what a sale-week member returns over her first months against the discount she was given: at 0.23 orders in month one against 0.61 for an organic member, this sale has not paid back yet. Leave search to menu view alone: its 118 percent was never a broken step.

```notes
LIVE, 4 minutes. Two traps of L5: acquiring your way out of a retention problem, and fixing the
skippable stage. If a group asks what a real company did instead: Swiggy went the other way and
weaned away more than 4 million unprofitable Instamart users (its Q1 FY27 letter, the fallback
block's first part). Then the groups finish their page.
Source:
https://nsearchives.nseindia.com/corporate/SWIGGY_30072026154100_Covering_Letter_Letter_to_Shareholders_-_signed.pdf (checked 12 October 2026)
Transition: the call, said in one breath.
```

---

## S42. The call: the Android checkout first
*What does a strong call say, in the order the membership lead needs it?*

**The call.** Fix the last step of the new Android checkout for members first: it loses about 1,223 to 1,317 orders a week, a quarter of Android members' orders, and a code fix ends the loss. **The evidence.** Checkout start to order placed fell from 72.5 to 55 percent for members on Android from the release week; starting checkout held at 80; on the same step iOS members went from 71 to 70 and non-members on Android from 65 to 64; the order records match the event log. **The cost.** Rs 3.7 to 6.6 lakh of order value a week at Rs 300 to Rs 500 an order, of which Zomato keeps its commission and fees. **The second problem.** The sale-week members kept 20 percent in month one against 49 for organic August members; before another sale, work out whether these members pay back their discount. **What would change the order.** If members who failed had come back and ordered later, the release would cost a delay rather than orders and the sale would go first; within a day, 36.5 percent did so before the release and 35.1 after.

```notes
LIVE, 3 minutes. One group reads its call; the room scores it against the five lines. This is the
model, and a group that puts the sale-week members first with a reason that holds has made a
defensible call; the room should hear why.
Transition: the interview.
```

---

## SECTION 5: What does the interviewer hear?
*"Retention dropped; walk me through your investigation." How does a hire-grade candidate, one whose answer gets the job, order it, and how does the same idea apply to an AI product?*

```notes
LIVE, 15 minutes. L6. Pairs read the transcript in the extras folder: one plays the interviewer,
one the candidate; they score the hire-grade answer on the scorecard's seven lines and swap.
Explorer scene Th4 carries the AI-company variant.
Transition: the order of the walk.
```

---

## S43. The walk: the morning's five causes, then the call
*In what order does a strong candidate investigate a retention drop?*

```mermaid
flowchart LR
    A["<b>1. Tracking</b><br/>did the count change?"] --> B["<b>2. Definition</b><br/>who is counted, from when?"]
    B --> C["<b>3. Cohorts</b><br/>each signup month<br/>at the same age"]
    C --> D["<b>4. Everyone</b><br/>platform, date, zone;<br/>fewer users or fewer orders each?"]
    D --> E["<b>5. A stage</b><br/>which step changed, for whom?"]
    E --> F["<b>6. The call</b><br/>fix, evidence, cost"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class A,B,C,D,E known
    class F lit
```

| | A weak answer | A hire-grade answer |
|---|---|---|
| First sentence | "It's probably the August cohort." | "Before a cause, I'd check the count, then what the number counts." |
| The flat 38 | Accepts it | "Who does month-two retention count, and from when?" |
| The split | Overall conversion | Cohorts at the same age, then platform and date on the same step, then fewer users against fewer orders each, cohorts held fixed |
| The close | "Retention dropped." | "One step on Android since 14 September, about 1,223 to 1,317 orders a week; then whether the sale paid back; October reads about 33." |

```notes
LIVE, 6 minutes. The steps are the morning's hypothesis board. Aced's guide to analyst interviews
says the same about a metric drop: rule out a data issue first, segment before a root cause, and
keep fewer users apart from fewer views each (checked 12 October 2026). The weak answer names a
cause in its first sentence.
Source:
https://www.aced.io/blog/top-data-analyst-interview-questions (checked 12 October 2026)
Transition: the AI-company variant.
```

---

## S44. The AI variant: judge each cohort at week four
*An AI writing assistant launched two months ago and its launch week brought its biggest cohort ever. How do you know whether it is habit or novelty?*

| | Launch-week cohort | A cohort that found the app on its own |
|---|---|---|
| Week one | Looks strong: the feature is new | Looks normal |
| Week four (invented numbers) | 24 percent still active | 36 percent still active |
| The blended weekly actives | Jump in launch week, then stay near the record | Each week's new cohort adds to the count |

```mermaid
flowchart LR
    L["<b>launch-week cohort</b><br/>week four: 24 percent"] --> B["<b>blended weekly actives</b><br/>near the record"]
    O["<b>a cohort that came on its own</b><br/>week four: 36 percent"] --> B
    N["<b>new cohorts every week</b>"] --> B
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class O,N known
    class L,B bad
```

**The call.** Count a user as active only on the core action, a draft she keeps, and read each cohort at the same age, week four or later (the programme's rule of thumb), with the share of drafts kept and the cost per retained user beside it. The blended count still sizes load and spend; it cannot say whether anyone formed a habit. The structure is Chennai's: a mix that hides a fall.

```notes
LIVE, 4 minutes. Programme-written, every number a toy (explorer scene Th4 shows the same toy).
The transfer: a launch cohort is the sale-week members of an AI product. Two months after launch,
the launch cohort and the next few weekly cohorts have all reached week four.
Transition: the handoff.
```

---

## S45. The handoff: the member who has not left yet
*What does the cohort table get wrong about its newest members, and who picks it up?*

**The handoff line.** "Your cohort table treats a member who has not left yet as if she were retained for ever, and that flatters every curve. The next 120 minutes give that member a name, censored, and show when two curves really differ by more than chance."

The next block is the IITGN faculty session W4-3 on survival curves, censoring and hazard, tentative until IIT Gandhinagar confirms it.

```notes
LIVE, 1 minute. Say the handoff line word for word and stop. If the block has slipped, open the
fallback deck (the weaned-users block). Park any "is the difference real" question for the block.
Transition: the Kahoot.
```

---

## SECTION 6: What does the room carry out?
*Which of the day's calls can the room make in seconds, and what does the day close on before Friday's ticket?*

```notes
LIVE, 15 minutes. The Kahoot (10) and the close (5).
Transition: the Kahoot.
```

---

## S46. Kahoot: eight items, one from Wednesday
*Which of the day's calls can the room make in seconds?*

```cards
icon: users | eyebrow: Items 1, 3 and 4 | title: Cohorts and the blend | body: What a cohort fixes; a blend that holds while two old cohorts fall; what a curve's level after month one says | tone: light
icon: filter | eyebrow: Items 2, 5 and 7 | title: The funnel | body: The step that owns the Android loss; a step above 100 percent; per session against per member | tone: light
icon: rotate-ccw | eyebrow: Items 6 and 8 | title: Wednesday, then the interview | body: Bread to milk, confidence 0.74 and lift 1.04, the verdict in one breath; then the first move in a retention walk | tone: dark
```

```notes
LIVE, 10 minutes. Ungraded, scored on correctness and speed. The trap item uses a blend other than
38. Read the most-missed item's answer aloud before the close.
Transition: the close.
```

---

## S47. The day in one sentence, and Friday's ticket
*What does Thursday close on, and what is Friday's question?*

**The sentence.** The dashboard was flat because of who it counts: every cohort fell after month one, each newer one started lower, and the August cohort is outside the count until October, when the dashboard reads about 33; the orders were lost in one step, on one platform, after one date.

**The crux lines.** A cohort fixes the entry moment. A blend is a size-weighted average and counts who it counts. Each funnel step divides by the step before, in one named unit. A low step is not a loss until it moves.

**Friday.** Flipkart's Lucknow fulfilment centre must book packer shifts for the festive weeks, and two forecasts sit eighteen points apart: which one goes to the plan, and how wrong could it be? The pre-read ships tonight: the ticket's first lines and five terms.

```notes
LIVE, 4 minutes. Say the sentence twice. The TA lab after the block runs the same method on Kalpa
Retail's Retail-Plus tier. The cohort axis built today is Friday's time axis.
Transition: the faculty block (tentative) or the fallback.
```
