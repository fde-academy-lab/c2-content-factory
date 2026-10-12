# How many drivers does the evening peak need, and can you say it on one page?

Week 4, Day 2. Half two.

Header: WEEK 4  ·  DAY 2  ·  UBER, HYDERABAD, AN ILLUSTRATIVE CASE

## SECTION 4: How big is the unknown?
*How many drivers must be online at the evening peak, sized from stated assumptions, and how do you know the answer is sane?*

```notes
LIVE, 65 minutes. Say once that the afternoon runs the dojo (a number sized from nothing,
then checked), the written case (the morning's slide as one page), the two transcripts and the
gallery, with no new technique. The dojo opens on the canteen's tea (10), drivers at the evening peak worked
together (30), UPI in pairs against the clock (25). Chapter 4 is L5 of the ladder on an estimate.
Styles: Brilliant (the chapter opens on which number to check against), StatQuest (round numbers
spoken aloud, the running product on the board), explorable explanations (explorer scene T3, the
guesstimate tree with a slider per factor). Mid-session drill 2, four estimates and their checks,
is in exercises/unguided for the lab if the room runs short here.
Transition: the opening question.
```

---

## S33. Predict: which number would check this estimate?
*You have sized drivers online at the weekday evening peak. Which of these numbers checks it in the same unit, period and definition?*

a) Monday's rider requests after the launch, 256,556 over six weeks

b) A published count of Uber drivers signed up in Hyderabad

c) A published count of Uber drivers online at one weekday evening peak in Hyderabad

d) The online driver-hours behind each rider request in the case's own data

```notes
LIVE, 3 minutes. Letters on paper, then a show of letters. Expect a, because it is the only number
on the list the room has seen.
Transition: the answer, and the rule behind it.
```

---

## S34. Answer: check in the same unit, period and definition
*Why does only one of the four check the estimate directly, and what do you do when it does not exist?*

**The answer is c, and nobody publishes it, so its slot reads "to be found".** a counts rider requests over six weeks in twelve zones: another unit, a longer period and a slice of the city. b counts sign-ups, another definition from drivers online at one moment. d is not wrong: it checks one link in the chain, a ratio the case's own data holds, and when the direct check does not exist that is the honest fallback the afternoon uses.

```mermaid
flowchart LR
    X["<b>an estimate</b><br/>drivers online,<br/>one evening moment"] --> U{"same unit?"}
    U -->|"yes"| P{"same period?"}
    P -->|"yes"| D{"same definition?"}
    D -->|"yes"| OK["<b>a check</b>"]
    U -->|"no: requests, not drivers"| NO["<b>not a check</b>"]
    P -->|"no: six weeks"| NO
    D -->|"no: signed up"| NO
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef bad fill:#FBE9EF,stroke:#D63A6A,color:#1A0F5C
    class X,U,P,D known
    class OK lit
    class NO bad
```

```notes
LIVE, 2 minutes. Write the three words on the board: unit, period, definition. They stay up all
afternoon.
Transition: the warm-up, with nothing at stake.
```

---

## S35. The canteen's tea, in four steps aloud
*How many cups of tea does the campus canteen sell on a weekday?*

**A toy, invented for this class.** Clarify: one canteen, one weekday, cups and not litres. Map: students on campus x the share who buy tea x cups each. Calculate: 2,000 x 0.6 x 2 = 2,400 cups. Validate: the canteen's till for one weekday; failing that, cups counted at the counter for one busy half hour.

```mermaid
flowchart LR
    C["<b>cups a weekday</b><br/>2,400"] --> S["students on campus<br/>2,000"]
    C --> B["share who buy tea<br/>0.6, so 1,200 buyers"]
    C --> K["cups each<br/>2"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class C lit
    class S,B,K known
```

```notes
LIVE, 5 minutes. Ask the room for each value and write the one it settles on; say the running
product aloud: 2,000, then 1,200 who buy, then 2,400 cups.
Transition: the four steps as a strip.
```

---

## S36. A guesstimate runs in four steps
*What does every estimate in the dojo, and in an interview, do in order?*

```mermaid
flowchart LR
    C["<b>1. Clarify</b><br/>scope, unit, window,<br/>what counts"]
    M["<b>2. Map</b><br/>the chain of factors<br/>that multiplies out"]
    L["<b>3. Calculate</b><br/>each factor said aloud,<br/>the running product shown"]
    V["<b>4. Validate</b><br/>against a number in the<br/>same unit, period and definition"]
    C --> M --> L --> V
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    class C,M,L known
    class V lit
```

**Interviewers listen to the structure and the stated assumptions.** Aced's guide to analyst interviews (an interview-preparation site) says the interviewer "isn't looking for a precise number" and is "evaluating your estimation framework", with each assumption stated so it can be challenged (checked 12 October 2026). A number that is wildly off still costs the answer, which is why step 4 exists.

```notes
LIVE, 2 minutes. Point at each step. The step first estimates skip is the fourth.
Transition: the city head's question, clarified.
```

---

## S37. Clarify: six questions pin the estimate down
*Which questions pin the estimate down before any number is written?*

| Ask | The answer to work with |
|---|---|
| Which city, which product? | The Hyderabad metro area, Uber, one product (assume cars) |
| Which window? | The weekday evening peak, one of the guarantee's two daily windows, three hours long |
| Drivers online when? | At one moment inside the window, since a count summed over three hours is another unit |
| What target? | A median rider wait under five minutes, for the city and then zone by zone |
| Requests or trips? | Trips: about nine in ten requests became trips in Monday's data |
| Drivers on two apps? | A driver online on Uber may be busy on another app, so lean the idle share low |

**The unit is drivers online at one moment.** Every factor in the chain must arrive in a unit that multiplies into it.

```notes
LIVE, 3 minutes. Ask the room for the clarifying questions before showing the table. A candidate
who skips this step is the one who lands on the trap at S42.
Transition: the map.
```

---

## S38. Map: drivers online as a chain of factors
*Which factors multiply into drivers online at the evening peak?*

```mermaid
flowchart TD
    D["<b>Drivers online at the peak</b>"]
    R["<b>Trips to serve an hour</b><br/>about 8,330"]
    P["people in the city<br/>1 crore (0.9 to 1.1)"]
    S["weekday Uber trips<br/>per 100 people<br/>1 (0.5 to 1.5)"]
    E["share of trips in the<br/>evening, over 3 hours<br/>a quarter (0.2 to 0.3)"]
    T["<b>Trips per online driver-hour</b><br/>1.68"]
    B["trips a busy driver<br/>fits in an hour<br/>2.4 (2 to 3)"]
    I["idle share at<br/>any moment<br/>0.30 (0.22 to 0.38)"]
    X["<b>Buffer</b><br/>1.15 (1.10 to 1.25)"]
    D --> R
    D --> T
    D --> X
    R --> P
    R --> S
    R --> E
    T --> B
    T --> I
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class D lit
    class R,T,X known
```

**Drivers online = (trips to serve an hour / trips per online driver-hour) x buffer.** Each leaf is a guess said aloud with its range. Counting trips per 100 people, never riders, keeps a commuter who rides both ways in the count. A peak trip takes about 25 minutes from accepting to dropping, so a busy driver fits 2.4 an hour; the buffer covers the busiest half hour.

```notes
LIVE, 6 minutes. Build the tree on the board with the room, leaf by leaf, asking for each value and
its range. Explorer scene T3 has a slider per leaf. The idle share is a guess here; the validate
step checks it like for like.
Transition: the running product.
```

---

## S39. Calculate aloud: about 5,700 drivers
*What does the chain multiply out to, step by step?*

| Step | Said aloud | Running result |
|---|---|---|
| People x weekday trips per person | 1 crore x 1 per 100 | 1 lakh trips a day |
| x share in the evening | x a quarter | 25,000 in the window |
| / three hours | / 3 | about 8,330 trips an hour |
| Trips per online driver-hour | 2.4 x (1 - 0.30) | 1.68 |
| Trips an hour / trips per driver-hour | 8,330 / 1.68 | about 4,960 drivers |
| x buffer | x 1.15 | about 5,700 drivers |

**Question.** Using the ranges on S38, which assumption moves the answer most: a) the idle share, b) weekday trips per 100 people, c) the buffer, d) the trips a busy driver fits in an hour?

```notes
LIVE, 6 minutes. Say each step aloud and write the running result before the next. Then the
question: letters on paper, two minutes with a neighbour, revote. A range that spans three times
its low end beats one that spans a fifth.
Transition: the swing chart.
```

---

## S40. Answer: how often people ride moves it most
*How wide is the honest range, and which factor sets it?*

![How far each assumption moves the answer](../whiteboards/C2_W04_D02_guesstimate_swing_STUDENT.png)

**The answer is b.** With every other factor at its central value, weekday trips of 0.5 to 1.5 per 100 people move the answer from about 2,900 to about 8,600; the idle share moves it from about 5,100 to 6,400. **Say it as:** "about 5,700 before the check, from 2,900 to 8,600 with everything else held, and mostly a question of how often people ride."

```notes
LIVE, 5 minutes. Trips per person is also the first number to replace: Uber's own dashboard holds
peak trips an hour. The idle share is the assumption Monday showed moving.
Transition: the check.
```

---

## S41. Validate: like for like, the chain runs high
*Which part of the estimate can the case's own data confirm, and does it move the answer?*

```stats
value: 0.53 | label: driver-hours per completed trip, before | note: the case's twelve zones, median wait 4.8 minutes
value: 0.63 | label: driver-hours per completed trip, after | note: the same zones, median wait 4.6 minutes
value: 0.60 | label: the chain, before its buffer | note: 1 / 1.68, about an eighth above 0.53
```

**The chain needs about an eighth more driver time per trip than the before window, the one whose wait met the target, so it errs high.** Re-run at the case's 1.90 trips an hour: 8,330 / 1.90 x 1.15 = about 5,000, so say about 5,000 to 5,700. The case pools both daily windows on all seven days (42 hours a week), so it checks the ratio's size, never the city's count, and a published count of drivers online at Hyderabad's evening peak has not been found.

```notes
LIVE, 3 minutes. Like for like means per completed trip on both sides: the chain counts trips, so
the case's hours are divided by its trips, never its requests (0.47 per request mixes in the 11
percent of requests nobody served). The idle share checks the same way: 1.90 trips x 25 minutes
leaves an idle share of about 0.21 before the launch, the window that held the wait at 4.8 minutes.
Transition: the trap a hurried estimate falls into.
```

---

## S42. The trap: a day's trips divided by an hour's
*What goes wrong when a day meets an hour?*

**The plausible wrong answer.** "1 crore people, 1 trip per 100 people, so 1 lakh trips; a driver does 2.4 trips an hour; so about 41,700 drivers." A city head who takes that to the review asks for incentives for about seven times the drivers the chain says.

**Why it is wrong.** A day's trips were divided by an hour's trips per driver, a period mismatch, and the idle share and the evening window were skipped. **The check:** write the unit beside every factor. **The fix:** bring the day's trips into the evening window's hour before dividing.

```notes
LIVE, 5 minutes. Write 41,700 and 5,700 side by side. Ask which step of the four was skipped:
clarify. This is the trap the interviewer fishes for in transcript 2.
Transition: UPI, in pairs.
```

---

## S43. UPI in pairs: seven minutes on the clock
*How many UPI payments happen in India on an average day?*

**The drill.** In pairs, seven minutes, all four steps on one sheet. Clarify volume or value (volume: the count of payments). Map active users x payments per user a day, and say how many of those go to shops and how many to people, so the payments a day are believable.

**What the scorer checks:** scope clarified first, every assumption written with a range, a range given, and a sanity check in the right unit.

```notes
LIVE, 12 minutes. Three minutes to set up, seven on the clock, two to swap sheets with the next
pair. Collect three pairs' estimates on the board before the next slide.
Transition: the published number.
```

---

## S44. The check: per day, and per payment
*Is a pair's estimate sane, and which comparison is the honest one?*

**NPCI's figure.** NPCI, the National Payments Corporation of India, which runs UPI, reported an average of 802 million UPI payments a day in September 2026: 24.07 billion in the month, worth Rs 29.37 lakh crore (Outlook Money, 2 October 2026; checked 12 October 2026).

```mermaid
flowchart LR
    U["<b>payments a day</b><br/>70 crore = 700 million<br/>(1 crore = 10 million)"] --> A["active users<br/>about 35 crore,<br/>one in four of 140 crore"]
    U --> F["payments per user a day<br/>about 2"]
    U -.->|"13 percent below"| N["<b>NPCI</b><br/>802 million a day"]
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    class U lit
    class A,F,N known
```

**Two checks.** Per day: September has 30 days, so 24.07 billion / 30 = 802 million; dividing by 31 gives 776 million, a small slip beside the estimate's range. Per payment: Rs 29.37 lakh crore / 24.07 billion = about Rs 1,220 a payment, far above a cup of tea, so the count holds large transfers between people.

```notes
LIVE, 6 minutes. Read the board's estimates against 802 million. The worked chain lands 13 percent
below, a little low, and payments a day is the factor to revisit: the Rs 1,220 a payment says the
2 a day must split shops from people. Praise structure and the second check over closeness.
Transition: three traps a sanity check catches.
```

---

## S45. Three traps a sanity check catches
*Which skipped move lets each wrong number through?*

| Trap | What a confident candidate says | What catches it | The test it fails |
|---|---|---|---|
| People as households | "A city of two million people has eight million households" (invented) | Households are people divided by about four: 20 lakh / 4 = 5 lakh; this one multiplied | Unit |
| A record day | A weekday estimate of Delhi Metro journeys, checked against 82,44,903 | DMRC's average is 64.06 lakh journeys a day; 82,44,903 was one record day, 17 September 2026 | Period |
| A muddled source | "Flipkart had 63 million concurrent users in a minute" | Flipkart's text says 6.3 million (the 63 is in its web address), and "concurrent in a minute" mixes a moment with a minute | Definition: read the source's own words |

**Sources,** checked 12 October 2026: The Tribune (9 August 2026) and Republic World (18 September 2026), citing DMRC, the Delhi Metro Rail Corporation; Flipkart Stories (9 October 2026).

```notes
LIVE, 6 minutes. Each trap fails one of the three tests on the board: unit, period, definition.
In 2018 DMRC's line-utilisation count tallied a trip across three lines three times (PTI, 30 May
2018), another definition trap.
Transition: what chapter 4 adds to Tuesday's node.
```

---

## S46. Chapter 4 adds a number sized from nothing
*What does Tuesday's node carry now, and what does it hand to Wednesday?*

```mermaid
flowchart LR
    M["<b>Mon</b><br/>pay for trips"] --> T["<b>Tue</b><br/>one slide, four moves<br/>5,000 to 5,700 drivers"]
    T -.-> W["<b>Wed</b><br/>what goes with what"]
    classDef known fill:#EEEAFB,stroke:#5B3FD6,color:#1A0F5C,stroke-width:2px
    classDef lit fill:#1A0F5C,stroke:#1A0F5C,color:#FFFFFF
    classDef unknown fill:#FFFFFF,stroke:#B8B2D6,color:#6B6690,stroke-dasharray:4 3
    class M known
    class T lit
    class W unknown
```

**Tuesday's node now carries** the slide (Rs 314 to Rs 260 per online hour, defended in four moves, one appendix page per role) and the estimate (about 5,000 to 5,700 drivers once checked; 2,900 to 8,600 by how often people ride). **In the interview** [S]: estimate a number from nothing, aloud, and check it. The structure, the stated assumptions and the check carry most of the score.

```notes
LIVE, 1 minute, taken from the traps slide's seven. Then the break.
Transition: break, 10 minutes, then the written case.
```

---

## SECTION 5: What goes on one page?
*What goes on the one page to the city head, so that the morning's slide reads in two minutes?*

```notes
LIVE, 40 minutes, individual, AI-free, handed in. The written case is the memo form of the
morning's slide: L5 in writing. Style: Feynman (plain words a driver would follow), Minto (the
answer first).
Transition: the brief.
```

---

## S47. The brief: one page, four parts, in sentences
*What must the page do in the first two minutes of reading?*

```cards
icon: target | eyebrow: First sentence | title: The claim | body: What the city head should believe, in words a driver would follow | tone: light
icon: hash | eyebrow: Second | title: One number and its denominator | body: The rupees per peak online hour, before and after | tone: light
icon: triangle-alert | eyebrow: Third | title: The caveat | body: In the body of the page, where the reader meets it before the action | tone: light
icon: circle-check | eyebrow: Last | title: The action and its cost | body: What to do, the saving in rupees over weeks, who signs | tone: light
```

**The reader** is the city head, with the three roles reading over a shoulder: finance reads rupees, driver operations reads drivers, marketing reads sign-ups. Words a non-technical reader would not know (denominator, index, guardrail) stay off the page, or are said in plain words.

```notes
LIVE, 3 minutes. The checklist handed back after the slot asks five things: the claim first, one
number with its denominator, the caveat in sight, the action with its cost and signer, no method
words. Three or more is a pass.
Transition: the forty minutes.
```

---

## S48. Forty minutes, on paper, alone
*What are the rules for the written case?*

**On one sheet, by hand.** No laptop and no phone, so the page is your own thinking. Write the page; then read it once as the finance partner would and fix the sentence they would attack.

**At the end of the slot the page is handed in.** Three pages, chosen for one strong part each, come back at the gallery.

```notes
LIVE, 37 minutes of silent writing. Walk once early to answer scope questions and once near the
end to signal the clock. No teaching inside the slot.
Transition: the transcripts.
```

---

## SECTION 6: What does it sound like?
*What does the slide sound like spoken in an interview, and what does a hire-grade answer open on?*

```notes
LIVE, 25 minutes. Chapter 6 is L6 of the ladder: two transcripts and the AI-company variant, read
in pairs and scored. The full transcripts are in extras/C2_W04_D02_interview_room_STUDENT.md.
Style: interview rehearsal on annotated answers.
Transition: transcript 1.
```

---

## S49. Transcript 1: two openings, side by side
*"Present this recommendation to a non-technical leader in two minutes." How do the first lines differ?*

| A weak opening | A hire-grade opening |
|---|---|
| "So I looked at the dashboard. Online hours are up 24 percent, trips are up 3 percent, trips per hour went from 1.90 to 1.58, acceptance fell, and bookings per driver-week is actually up, so it is mixed." | "You are deciding whether to keep, end or change the guarantee. It is paying for online hours that carry no trips: an hour online brought in Rs 314 of fares and now brings in Rs 260 at the same fare, while the median wait barely moved, 4.8 to 4.6 minutes. Part of the fall may be the monsoon. Test paying per completed trip with an acceptance floor on half the drivers, picked at random, for six weeks; city-wide it saves Rs 58 lakh to Rs 92.7 lakh. You sign the test." |

**The follow-ups:** which denominator did you choose, and what would make you choose another; test or rollout, and how do you stop drivers moving into the zones you treat; the finance partner says it is the monsoon, so answer in under a minute.

```notes
LIVE, 8 minutes. In pairs, one reads the interviewer, one the candidate; then the candidate answers
the three follow-ups without notes. The weak opening reads numbers and lets the per-driver-week rise
blur the claim. The full hire-grade answer, with the per-driver-week line checked (each driver
online four more hours a week at 17 percent less per hour; the 140 joiners pulled the read down), is
in extras/C2_W04_D02_interview_room_STUDENT.md.
Transition: transcript 2.
```

---

## S50. Transcript 2: the drivers estimate, two answers
*"How many drivers must be online at the evening peak in a city?" What does each answer do first?*

| A weak answer | A hire-grade answer |
|---|---|
| "About 1 crore people, 1 percent ride, so 1 lakh trips. A driver does 2.4 trips an hour, so about 41,700 drivers." | "One moment of the three-hour weekday evening peak, one product, the city's median wait under five minutes. Drivers online is trips an hour divided by the trips one online driver completes in an hour, times a buffer: 8,330 / 1.68 x 1.15, about 5,700; trips per person moves it most, 2,900 to 8,600. Like for like, the case's 0.53 driver-hours per trip against my 0.60 says I run an eighth high, so 5,000 to 5,700, and each thousand idle drivers costs up to Rs 9 lakh an evening at the floor." |

**The follow-ups:** your idle share is a guess, so which number in the case data would catch it; the window is three hours, so what does a four-hour window do; give a range, and say which factor drives it.

```notes
LIVE, 8 minutes. Hire-grade lines for the follow-ups: the case's hours with no trip (22 and 38
percent) are looser than idle at a moment, and like for like its trips per hour give about 0.21
before the launch, which held the wait at 4.8 minutes and gives about 5,000; a four-hour window
leaves the busiest half hour where it was, so the buffer rises to about 1.53 and the answer stays
about 5,700; about 2,900 to 8,600 with everything else held, driven by trips per person.
Transition: the AI-company variant.
```

---

## S51. The AI variant: acceptance rate in the sales deck
*How do you present a metric change to a head of product who quotes acceptance rate to customers?*

**The setup, invented for this class.** A coding assistant's sales deck quotes "acceptance rate 32 percent", the share of suggestions developers accept, even ones deleted soon after. The analyst proposes a new **north star**, the one number the team is judged on: characters of suggested code still in the file seven days after acceptance, per developer who saw a suggestion that week, with two **guardrails** that catch padding (retained characters per accepted character; edits per accepted suggestion).

**The objection, partly right.** "Acceptance rate is what customers see." True, and a 2022 study of GitHub Copilot's users found acceptance tracks how productive developers feel. **The answer** keeps acceptance in the deck as a **leading input**, a number that moves first, and judges the team on code that survives only once a holdout of users shows it tracks seat renewals.

```notes
LIVE, 6 minutes. Ask which of the morning's three objections this resembles. Expect marketing's:
both keep the visible number while the north star does the judging. The study: Ziegler and
colleagues, arXiv 2205.06537, 13 May 2022 (checked 12 October 2026). A commit is a saved change to
the code; a revert undoes one.
Transition: scoring the transcripts.
```

---

## S52. How a pair scores a transcript
*What does an interviewer listen for, and how is each part scored?*

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Clarified the scope first | skipped | partly | unit, window and target pinned |
| Named the denominator, or the unit, and the window | neither | one | both |
| Saw the trap | missed | named late | named and checked |
| Sized it with a unit | no unit | a unit, unchecked | a unit carried through |
| Said what would change their mind | no | vaguely | a named fact |
| Tied it to a decision and its cost | no | a decision | a decision and its rupees |
| Gave the structure before the number | number first | mixed | structure first |

```notes
LIVE, 3 minutes. Each pair scores both answers of one transcript on paper and compares with a
neighbouring pair. The trainer's scored copies are in the trainer pack.
Transition: the pain points.
```

---

## S53. Pain points, each with the case that shows it
*Where do first attempts at a slide and an estimate usually break?*

| Pain point | Where you saw it |
|---|---|
| The first slide carries every number | Slide A this morning: nine numbers, no claim |
| The first defence retreats or overclaims | Round one of the studio |
| A check against an unusual day | Delhi Metro's average day against one record day |
| A muddled published figure | Flipkart's 6.3 million against the 63 in its web address |
| A memo nobody can write in an hour | Amazon's letter: a great memo probably takes a week or more |

```notes
LIVE, 5 minutes. One line each; ask the room which one bit them today.
Transition: the gallery.
```

---

## S54. The makeover gallery: three dots each
*Which rebuilt titles would a city head act on?*

**Every group's final slide goes on the wall, beside three written pages.** Each learner places three dots: one on the title that most clearly states a claim a city head could act on, one on the appendix page that best answers its role's question, one on the caveat that sits most clearly in sight.

**The test for a title** is the Big Idea from Storytelling with Data, a site on presenting data: one complete sentence that carries a point of view and says what is at stake (checked 12 October 2026).

```notes
LIVE, 10 minutes. Five minutes to walk and dot, five to read the top three titles aloud and name
the part each does well. A high-scoring title that is still a topic is the example to discuss.
Transition: the Kahoot.
```

---

## S55. Kahoot: eight questions, ungraded
*Which of today's ideas can you retrieve under a timer?*

```cards
icon: list-ordered | eyebrow: Questions 1 to 3 | title: The slide | body: The four parts in order; keep or cut; the defence that never concedes | tone: light
icon: calculator | eyebrow: Questions 4 to 6 | title: The estimate | body: The four steps; the city of two million; a day against an hour | tone: light
icon: refresh-cw | eyebrow: Questions 7 and 8 | title: Back to Monday and the check | body: The guardrail for a scheme that pays per trip; a monthly total over the wrong number of days | tone: light
```

```notes
LIVE, 20 minutes. Run the eight items from the Kahoot pack, read one line after each on what it
tested, and revisit any item under 50 percent correct. Nothing is graded.
Transition: where the day ends.
```

---

## S56. Where the day ends: a slide, a page and a range
*What will the city head hear on Thursday, and what comes tomorrow?*

> "The scheme is paying for online hours that carry no trips: Rs 314 to Rs 260 per peak online hour at a flat Rs 165 fare. Part of it may be the monsoon. Test paying per completed peak trip with an acceptance floor: city-wide, it saves Rs 58 lakh to Rs 92.7 lakh over six weeks if a half to a fifth of the idle drivers' top-up is still paid. At the evening peak the city needs about 5,000 to 5,700 drivers online, and how often people ride could move that from 2,900 to 8,600."

**The lines to keep.** A slide carries one claim, one number with its denominator, the caveat in sight and the action with its cost. Name the denominator before the number. Answer an objection in four moves. Size a number in four steps, give the factor that drives the range, and check it like for like. Check in the same unit, period and definition.

**Tomorrow:** Swiggy Instamart's cart page in Pune, and a strip that suggests what goes with what.

```notes
LIVE, 5 minutes. Read the sentence once. Wednesday's pre-read ships tonight: the Instamart ticket's
first lines and three terms, terms only.
Transition: close.
```
