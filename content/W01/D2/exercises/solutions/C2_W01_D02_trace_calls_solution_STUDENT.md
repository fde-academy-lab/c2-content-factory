# Day 2 solution, E2. Trace the calls

## The idea being tested

One question runs through all fifteen items: what is the caller holding after the call? A function that shows you something and hands back nothing is the most common shape a beginner writes, and it is invisible until the next line tries to use the answer.

The second half of the sheet moves the same question up a level. When a call raises, who decides what that means for the run? The function does not know what the run is for, so the caller decides, and the bare `except` is what happens when nobody decides at all.

## The answers

**Answers: 1a 2b 3c 4d 5a 6b 7c 8d 9a 10b 11c 12d 13a 14b 15c**

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | a | A function with no `return` hands back `None`, silently. | The order id is what appeared on screen, which the caller never received. The record confuses the argument with the return. An error assumes Python objects to a missing return, when it supplies `None` without a word. |
| 2 | b | `None` cannot be indexed, so the subscript raises and names the type. | `KR4200` assumes the printed value is still available somewhere. A `KeyError` would need an empty dictionary rather than `None`. Nothing at all assumes a silent no-op, which Python does not do here. |
| 3 | c | The last line names the exception type and the message, which is where the diagnosis starts. | The first line and the line naming your file are where you look second and third. Whichever is longest is a habit worth naming out loud so somebody can drop it. |
| 4 | d | `get_id_2` does both, so a caller gets the value and the room gets the noise. | Saying there is no difference treats printing as free. Slower measures the wrong thing. Returns nothing assumes printing consumes the return, which nothing in Python does. |
| 5 | a | `int("4500")` is 4500, which is above 2,000. | `False` inverts it. `TypeError` would need the conversion missing. `ValueError` would need an amount that is not digits. |
| 6 | b | `int(raw)` builds a new number and the record still holds its text, so they are not the same object. | `True` reads them as the same amount, which is the point being broken. `TypeError` assumes `is` compares values, when it compares identity. `None` confuses a comparison with a missing return. |
| 7 | c | `int` refuses and quotes the value it was handed, which is the most useful part of the message. | `12` assumes a word-to-number conversion Python does not do. `TypeError` names the wrong exception, since the type was fine and the value was not. `None` assumes silence, which is what a bare `except` would produce. |
| 8 | d | The function converts or refuses. Only the caller knows whether one bad amount means skip the row, stop the run, or fill a default. | Inside the function gives it a judgement it does not have. Inside `int` describes where the exception is raised rather than where it is decided about. The interpreter's configuration is invented. |
| 9 | a | Your rule and the offending value in one line, which is what a reader needs and what `int` cannot know. | Longer mistakes length for information. Stopping it reaching the caller is false, since raising propagates by definition. Converting first describes the order of operations rather than the benefit. |
| 10 | b | The loop swallows both failures, so the total is built from 28 records and the message says 30. | 28 would be true if the count came from the loop rather than from `len(orders)`. A total of zero would need every conversion to fail. Raising is what happens without the `except`. |
| 11 | c | The total is correct for what went into it. The claim around it is false. | Saying the total is wrong and saying both are wrong each misplace which number lies. Saying nothing is wrong treats provenance as irrelevant, which is the belief this whole day exists to break. |
| 12 | d | The same records still fail, so the total does not move. The count now reports what was actually read. | The total changing inverts it. Nothing changing ignores the counter. Stopping on the first bad record confuses catching a named exception with not catching one. |
| 13 | a | The reconciliation catches a record that vanished into neither list, which is the failure the other three checks all pass through. | The hard-coded 28 breaks on tomorrow's file. The sanity bound is true of most runs and proves nothing. A positive total passes on a total built from one record. |
| 14 | b | An id with no reason cannot be fixed and a reason with no id cannot be found. | The id alone and the reason alone each keep half. Neither is the position the bare `except` takes. |
| 15 | c | The clean file's count means nothing without the rejected file's count beside it. | The style guide appeals to authority. Quicker is a claim about effort rather than about correctness. A backup is a side effect, and a poor backup at that. |

## The part worth arguing about

Item 8. A room usually splits between the function and the caller, and the split is worth ten minutes. Push on the case where the same `normalise_amount` is used by a nightly batch that should skip bad rows and by a form submission that should refuse. The function cannot be right for both, so it does the one thing it can know about and raises.

Item 15 is the other one. Somebody always argues that the rejects file is defensive paperwork. The reply that lands is item 11's: the clean count is a claim, and a claim with no denominator is not a number anybody can act on.

## The hands-on picks

The running half is `notebooks/C2_W01_D02_ex1_hands_on_STUDENT.ipynb`, and its four markers are:

**Answers: 1b 2c 3a 4c**

The executed twin is `C2_W01_D02_ex1_hands_on_solution_STUDENT.ipynb` in this folder.

## Where this pattern lives in production

Knight Capital, 1 August 2012, lost about USD 440 million in 45 minutes because a deployment reused an old flag and nothing failed loudly enough to stop it. The shape of that failure is item 10's: a system that kept running while its claims stopped being true.

The interview question is item 13's, and it arrives as "how do you know your cleaning run did not lose records?" The answer is the reconciliation, and the follow-up is what you do when it does not hold. Say that you stop, because a missing record is a record nobody will ever look for again.
