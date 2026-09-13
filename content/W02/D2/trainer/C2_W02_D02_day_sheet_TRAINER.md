# Trainer day sheet: Week 2, Tuesday. Joins and join semantics

TRAINER ONLY.

## The shape of the day

| Block | Minutes | What has to happen |
|---|---|---|
| Anand's ask and the gateway remark | 10 | The room predicts what double-posting does to a naive join |
| INNER and LEFT on two tiny tables | 45 | Traced row by row on the board, no database open |
| RIGHT and FULL OUTER | 30 | What each drops or duplicates |
| Imperfect keys and fan-out | 45 | The multiplication counted live |
| The validation habit | 40 | Row counts, the bridge, the anti-join |
| Guided then unguided | 50 | The booked-against-collected report |
| Kahoot and close | 20 | Seven questions |

Total 240 minutes.

## Order the day this way, not the other way

Open on the **wrong number**, then teach the machinery that explains it. Application before
theory. If you teach the four join types first and then show the fan-out, the fan-out becomes a
footnote instead of the point.

The first thing on screen should be the naive total coming back at roughly Rs 39.6 crore against
a book of Rs 19.84 crore, with no explanation offered.

## What is planted in v4

**Never name any of this.** The room finds it by counting.

| Planted | Found by | Exact value |
|---|---|---|
| 400 large invoices settled in two instalments | Counting rows before and after the join | 400 |
| 50 gateway retries, the same amount posted twice | `HAVING count(*) > 1 AND count(DISTINCT amount) = 1` | 50 |
| 30 delivered orders never paid | The anti-join from orders | 30 |
| 8 payments whose order is not in the book | The anti-join from payments | 8 |
| Two of the unpaid are Q2 corporate invoices on different channels | The gap by channel | Store and web carry lakhs, app carries Rs 500 |

The last row is why the gap-by-channel report has a shape worth reading. Do not point at it; let
somebody notice that app is clean and ask why.

## The failure to stage, and the exact numbers

Run the naive join total live. It returns booked at 1.9952 times the true figure.

Then ask the room to find something wrong with any individual row. They will not, because there is
nothing wrong with any individual row. Sit in that for a moment before taking the row count.

The row count is 1,450 against 1,000. Let the room work out where 450 came from before you say the
word fan-out.

## The moment the day turns

When somebody says some version of "nothing is duplicated in either table, the duplication
happened in the join".

Wait for it. It usually arrives during the board trace of the six small orders rather than from
the big query, which is exactly why the board trace comes first.

## The judgment that cannot be automated

An instalment and a retry look almost identical in the payments table. What separates them is a
business fact.

Ask the room directly: write a rule that removes duplicate payments. Then point out that their
rule deletes four hundred legitimate instalment rows. This is the day's one genuinely hard idea
and it is worth five minutes of silence.

## Timing pressure

Cut `FULL OUTER` first, per the row: name it, park it. Never cut the count validation or the
fan-out. If both halves run long, cut the orphan anti-join from the guided walk and set it as
stretch instead.

## Where this day goes wrong

Two ways. Rescuing the room from the doubled number before they have counted anything, which
turns the day into a syntax lesson. And treating the four join types as the content, when the
content is the count habit and the types are how you act on it.

## Close-out

Release both solution files. Set the take-home and say plainly that the reconciliation block is
the deliverable. Preview Wednesday in one line: Marketing wants the top fifty per segment, and the
head of Retail-Plus has an opinion about ties.
