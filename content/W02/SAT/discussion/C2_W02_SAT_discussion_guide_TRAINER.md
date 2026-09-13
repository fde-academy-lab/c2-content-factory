# Week 2 Saturday: the discussion guide

TRAINER ONLY. For the Academic TA leading the solution walk-through.

## The shape of the session

| Block | Minutes | What happens |
|---|---|---|
| The paper | 120 | Pen and paper, AI-free, no notes |
| Break | 20 | |
| Solution discussion | 75 | Papers swapped, every answer discussed as an interview answer |
| Doubt clearing and the bridge | 25 | Build 1 opens Monday in Kalpa Health |

## Before the room opens

Papers are swapped for peer cross-evaluation. Say once, at the start of the discussion, that the
person marking is not deciding anything: they are reading somebody else's answer against the one
being discussed, which is a different and more useful exercise than being marked.

Nothing here is graded. If somebody asks, say plainly that it is a performance indicator and move
on rather than defending it.

## The three items that carry the session

Thirty-five of the seventy-five minutes go to these three. Everything else gets a minute or two.

### B3, the join where every row was correct

> "Collected revenue came back at roughly twice the true figure and every individual row in the
> result was correct. Explain how both of those can be true at once."

This is the week's central idea and most papers will have some version of "there were duplicates
in the data". There were not. Neither table holds a duplicate row.

Push on that. Ask where the duplication happened, and keep asking until somebody says "in the
join". Then ask what that means for every check they were about to run on the output, and the
answer is that all of them pass.

Call on somebody who wrote the wrong version first, not last. Getting there in public from a wrong
start is the thing the room should see.

### C3, the argument against ROW_NUMBER

> "Give the argument against `ROW_NUMBER` that has nothing to do with fairness."

Most papers will restate the fairness argument in different words, because it is the one that was
said out loud on Wednesday and it feels sufficient.

The answer is reproducibility: two analysts run the same query against the same data and hand
Marketing different names. Ask the room which of the two is wrong, and let the silence sit before
saying neither.

This is the item most likely to appear in an interview in exactly this form, and worth saying so.

### F4, the sentence to Meera

> "Last week you told Meera that Q1 was Rs 2.10 crore. This week the warehouse said Rs 10.00 crore.
> Write the sentence you send her."

Read three or four aloud, anonymously, and ask the room to sort them into ones that apologise and
ones that explain.

Nothing was done wrong. An answer that opens by apologising has misread the situation, and the
instinct is common, understandable and expensive in a client room. Say that directly and without
mockery; several people will recognise themselves.

The strong version names what survived, which is the shape, and what did not, which is the level.

## Call-outs

Random, throughout, sixty seconds each. Use them on the short items rather than the long ones: A3,
B4, C1, D2, E1, E4.

Two rules for yourself. Call on somebody whose paper you have not read, so the call is genuinely
cold. And when an answer is wrong, take the next answer from somebody else before correcting it,
so the room does the work.

## Items that will split the room, and how to close them

**B6, retry against instalment.** Several will have written a rule that removes duplicate
payments. Ask how many rows their rule deletes. It is four hundred, and they are all correct.
Close it by saying the separator is a business fact, and business facts do not become rules
without somebody deciding.

**D4, the pivot round trip.** Most will have said the result is the same size. Do not spend long
on it. Say what happens and why once, clearly, and move on: this is a surprise to be met once
rather than a principle.

**E2, what the pivot did wrong.** The correct answer is "nothing", and a room that will not accept
it has the week's lesson still to land. Ask them to name one thing the pivot could have done
differently given the file it was handed.

## The bridge, and give it the full twenty-five minutes

Build 1 opens Monday in Kalpa Health with the Programme Head's online introduction. Unfamiliar
unit, unfamiliar data, unfamiliar stakeholders, and a group of four rather than a room.

Ask G1 out loud rather than reading answers back. What transfers and what does not.

The answers worth drawing out are habits rather than techniques: count before you total, name the
denominator, say what one row means, ask who owns the number. The things that do not transfer are
the entity model and the vocabulary, and the failure the item is testing for is somebody reaching
for Retail's revenue tree in a health business.

End on the sentence, and put it on the board:

```
The method transfers. The domain does not.
```

## What to record for the build team

Three things, in a short note after the session.

Which items the room got wrong in a way that suggests the teaching rather than the learner. Any
item where more than half the papers gave the same wrong answer is a content problem and belongs
in a follow-up issue rather than in a remark about the cohort.

Which two or three learners answered G1 with habits rather than techniques. They are the ones to
watch in Build 1.

Any question from the room that the answer key does not cover.
