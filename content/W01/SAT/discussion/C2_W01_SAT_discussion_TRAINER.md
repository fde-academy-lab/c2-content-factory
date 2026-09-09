# Week 1 Saturday: discussion guide for the Academic TA

Trainer file. It never reaches a learner, because the follow-up questions in it only work if the room has not read them.

## The two minute continuity block, read before the room comes in

**Where they are.** Four teaching days: types, comparisons, loops and records on Monday; functions, errors and files on Tuesday; profiling, cleaning and the decisions log on Wednesday; typical, spread and the segment summary on Thursday. Friday was Gandhi Jayanti, so the room has had a full day away from the material and will be cold on Monday's content in particular.

**What today is.** No new content. The paper rehearses the week as interview answers, and the discussion is where the answers get spoken rather than written, because a screen asks out loud.

**What today is not.** It is not a test with a score attached. Say that once at the start and do not repeat it, since saying it three times reads as an apology and the room stops trying.

**Where they go next.** Monday takes Thursday's segment gap and asks whether chance alone could have produced it. From Tuesday the same Kalpa Retail records stop being a file and become tables in Postgres, and the same segment summary gets written as one query and then as one line of pandas.

## Shape of the block

| Segment | Duration | Who runs it |
|---|---|---|
| The recap paper, pen and paper, no device in sight | 120 minutes | You invigilate. |
| Break | 20 minutes | Papers stay on the desks face down. |
| Solution discussion: the marking walk, then the deep pass | 75 minutes | You lead. |
| Doubt clearing and the bridge into Week 2 | 25 minutes | You lead. |

That is the four hours the week's row allocates, with nothing left over.

## Invigilation, the parts that matter

The paper is AI-free by format rather than by policing, which only holds if the format holds. Devices go into bags at the start, not face down on the desk. The file facts the questions rely on are printed on the paper itself, so nobody has a defensible reason to open a laptop. A learner who finishes early hands the paper in and waits, since papers leaving the room during the writing window breaks the swap.

## The swap

Collect every paper before the break. Redistribute after the break across rows rather than along them, so nobody marks the person they sat beside and prepared with. Each marker writes their own identifier on the sheet and marks in a different colour from the writer. Whole points only, no halves. Disputes are noted in the margin and brought to you at the end of the block, never raised during the walk, because one argument at question three costs the room questions six, seven and eight.

## Part one, the marking walk: 40 minutes, eight questions, five minutes each

Walk in paper order. A paper written in question order cannot be marked out of question order without every marker flipping pages on every question, and any other walk costs more in confusion than it buys in teaching.

Each five minute slot runs the same shape, and holding the shape is what keeps eight questions inside forty minutes:

1. Read the point split for the question from the answer key, about thirty seconds.
2. State what a full-credit answer contains, about two minutes. Say the content, not a model paragraph, because the markers are matching content.
3. One call-out from the draw, sixty seconds on the clock, answering aloud as they would in an interview.
4. Markers award the points and you move, about ninety seconds. Do not take a second question from the floor here. Park it for the deep pass or for doubt clearing.

The one thing to say out loud in each slot, when the rest is going fast:

| Q | The line worth saying |
|---|---|
| 1 | The twelfth order is `orders[11]`, and the off-by-one is the most common single point lost on this paper. |
| 2 | Assignment copies the reference. If your answer said `a` is still `[1, 2, 3]`, that belief will cost you a real dataset one day. |
| 3 | Read the bottom of a traceback first. The top frame is where you started, and it is never the bug. |
| 4 | `561145` is a correct sum. What fails is everything the number does not say. |
| 5 | Strip formatting, never guess a value. That rule is the difference between repairing `'24 500'` and inventing a number for `'twelve'`. |
| 6 | A cost stated in the abstract earns nothing. Name the field. |
| 7 | The denominator is not decoration. Forty-four is part of the answer. |
| 8 | Zero rejects on a dirty file is evidence about your code, not about the file. |

## Part two, the deep pass: 30 minutes, three questions, ten minutes each

Choose the three live. After the walk, ask for a show of hands on each question: who lost two or more points here. Take the top three by hands. Do not choose by what you found interesting, and do not skip the show of hands to save two minutes, because the whole value of the deep pass is that the room chose it.

Each ten minute slot:

1. Three call-outs from the draw on the same question, sixty seconds each, each learner adding to the previous answer rather than restarting it, about three minutes.
2. Both follow-ups below, about five minutes. These are one level up from what the paper asked, so a room that scored well on the written question can still be moved.
3. The one line everybody writes down before you move on, about two minutes.

If the hands say the room lost Q8, take it. It is the differentiator on the week's question set, and it is the answer that separates a candidate who checks a pipeline from one who trusts its output.

## The two follow-ups per question

Sixteen in all. Each one raises the same idea by one level, so they work whether or not the question made the deep pass.

| Q | Follow-up one | Follow-up two |
|---|---|---|
| 1 | You now have five million orders and the id lookup sits inside a loop over another table. What changes, and by how much? | Your dictionary is keyed on `order_id`, and `KR4201` appears twice in the file. What does `by_id` hold after you build it, and which of the two rows survived? |
| 2 | `dict(record)` copies one level. Your record carries a nested `customer` block. Change the city on the copy and tell me what happened to the original. | Where in Tuesday's cleaning code would this bug have shown up as a wrong number rather than as a crash? |
| 3 | Same traceback, last line now reads `KeyError: 'discount'`. Is your first move the same one? | You wrap the call in `try` and `except`, rerun, and the run goes green with zero rejects. What did you get wrong? |
| 4 | You narrow to `except ValueError` and the run reports six rejects. Next month the file arrives with a `None` in the amount column. What happens, and is that the behaviour you want? | Your reviewer says the crash blocked the pipeline for two hours and asks you to catch `Exception` broadly. Answer them, out loud, the way you would answer a lead. |
| 5 | You repair `'12,400'` by stripping the comma. The next file comes from a vendor that writes `12.400` for the same value. What does your repair do to it? | Both empty amounts were rejected. Someone then notices the JSON carries `source.amount_raw` of `1975` for `KR4214` and nothing at all for `KR4237`. Does that change your decision, and does it change it for both records? |
| 6 | The feed doubles in size and the consumer now wants only `order_id`, `amount` and `status`. Does your format choice change, and where does the flattening happen? | You flattened and shipped. Six months later someone asks what the amount looked like before cleaning. Where do they look? |
| 7 | The stakeholder now asks for the Student segment. It has twelve rows, ten usable amounts and a median of Rs 1,430. What do you send, and what do you say before you send the number? | Next month there are four orders above Rs 400,000 rather than one. Is the median still your answer? |
| 8 | Your run reports six rejects and forty-four clean, and the counts reconcile to fifty. Name one way the run can still be wrong. | You hand this pipeline to someone else on Monday and go on leave. Which single file makes your run defensible without you in the room? |

The answers you are listening for, in one line each: the id lookup becomes a scan per row and the cost multiplies rather than adds; the second `KR4201` overwrites the first and the near-duplicate arrives through the back door; the shallow copy shares the nested block so the original city changes too; mutating the source record makes the rejects log point at a record that has already been altered; a `KeyError` on an optional field is answered with `.get()` and a written default rather than a repair; a green run with zero rejects means the catch is too wide or the append is unreachable; the `None` raises `TypeError` and is not caught, which is correct, because a new failure mode is a signal to read; a broad catch ships a plausible wrong total and nobody finds out, so the answer is narrow catches plus a top-level handler that fails loudly; the comma strip does nothing to `12.400` or produces the wrong magnitude, so formatting repair carries a stated assumption into the decisions log; `KR4214` is recoverable and `KR4237` is genuinely lost, so the decision differs per record and is written down either way; the flattening belongs at the consumer boundary rather than at the source; the pre-cleaning value lives in `source_amount_raw` or nowhere at all; ten records get their sample size said before their median; four whales are a segment forming and the answer is to split the population rather than to pick a statistic; the reconciliation says nothing about identity, so forty-four clean records can still contain the duplicated `KR4201`; and the file that makes it defensible is the decisions log with a reason per rejection.

## The call-out draw

Seventeen call-outs: eight in the marking walk, one per question, and nine in the deep pass, three per chosen question. Sixty seconds each, on the clock, and you stop them at sixty even mid-sentence, because an interview does.

The draw is fixed in advance so nobody can read anything into who gets called. Number the attendance list in seat order from one, then take the positions below in sequence. If a drawn position is absent, take the next number in the list. Never re-draw and never pick someone yourself, since one chosen name turns the mechanism into a judgement about that learner.

| Where | Draw order |
|---|---|
| Marking walk, Q1 to Q8 | 26, 58, 18, 53, 27, 30, 16, 42 |
| Deep pass, first question | 38, 41, 14 |
| Deep pass, second question | 5, 13, 35 |
| Deep pass, third question | 48, 57, 3 |
| Reserves, in order, for absentees | 51, 24, 12, 39, 29, 28, 23, 17, 6, 50 |

A learner who cannot answer says so and you move to the next number without comment. Sixty seconds of silence in front of sixty peers is a heavy enough lesson without an added remark.

## Doubt clearing and the bridge, 25 minutes

Doubts first, about fifteen minutes. Take them by question number rather than by hand order, so the room does not spend all of it on Q1. Anything that needs a laptop to answer gets written on the board and carried to Monday's trainer rather than improvised here.

Then the bridge, about ten minutes, and it is worth protecting the time for it because it is the payoff for the whole week:

1. Monday takes Thursday's segment gap and asks the question the week left open, which is whether chance alone could have produced it.
2. From Tuesday the same records stop being a file. They become tables in Postgres, and the counting question you answered with a loop and an accumulator becomes one query.
3. The segment summary you built by hand with dictionary accumulators becomes one `GROUP BY`, and then one line of pandas. It was built by hand once so that when the shorter form arrives, you already know what answer it should produce.
4. The eight questions on today's paper come back on Week 2's paper, one level up, on the same records.

## What you record and hand on

Per question, the count of papers that lost each part point. Nothing else, and no per-learner totals anywhere, since the Structure tab locks this paper as a performance indicator rather than an assessment component. That table goes to the Programme Head and to Monday's trainer, who uses the two worst rows to decide what gets re-anchored in the first fifteen minutes of Week 2.

Collect the margin disputes at the end, settle them yourself against the answer key, and note any question where more than a handful of markers disagreed with each other. A part point that markers cannot apply consistently is a defect in the key, and it gets fixed before the Week 2 paper reuses the format.
