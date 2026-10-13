# The teaching styles every pack blends

The requester set this blend on 12 October 2026 (decision `teaching-approach`); the standard's section
"The teaching approach" says where it applies. Each style below is a set of moves in an order, the
artefact that carries each move, and the way it fails when overused. A pack blends them: no chapter
uses one style alone, and every chapter shows at least three.

Each style's full card, with its verified links, and the blend worked through on Week 4's cases are
in `teaching-styles-playbook.md` beside this page; read the cards for the styles your artefact leads with.

Four findings set the blend for learners who are weak in maths and new to business: worked examples
first, with the steps fading as the learner improves; the wrong answer said aloud and then refuted, which
helps the weakest learners most; retrieval, since being tested aids long-term memory; and a vote, an
argument with a neighbour and a revote on any question that splits the room.

## The moves, style by style

| Style | The moves, in order | Where it lands | Where it fails if overused |
|---|---|---|---|
| Veritasium (Derek Muller) | Put the misconception on the table first, in the learner's own likely words; ask for a prediction and a vote; run the test; reveal; then explain why the intuition broke | The opening of every chapter and every trap; the explorer's predict-then-reveal scenes; Kahoot items | A surprise with no mechanism after it is a magic trick; the reveal must be followed by the why |
| 3Blue1Brown (Grant Sanderson) | Start from a picture the eye can read; let the quantity move continuously; derive the formula as a shorthand for what the picture already showed; name it last | The explorer's scenes; concept boards built region by region on slides; the visual derivation slide before any formula | Beautiful motion without a question in front of it; every animation answers a question asked first |
| StatQuest (Josh Starmer) | Tiny numbers a learner can hold in their head; one step per slide; say each step aloud; repeat the key idea in the same words | L1 hand counts on twelve rows; the micro-example of each concept; study notes | Never leaving the toy; the next step always moves to the full data |
| Krish Naik | Code along from the raw table to a working result: load, inspect, clean, compute, chart, conclude; one plain sentence on what each line is for; finish on an answer a business would act on | The notebooks; the code glimpse on slides; the TA lab | Typing without thinking; every block is preceded by the question it answers and followed by what its output means |
| ByteByteGo (Alex Xu) | One connected map: boxes for ideas, numbered arrows for the order things happen, today's box lit, earlier and later boxes in place | Slide two of every deck (the week map); each chapter's closing map slide; the explorer's home screen; cheat sheet panels | A map so dense nobody can read it at a glance; at most nine boxes on any one map |
| takeUforward (Striver) | A ladder of problems from easy to interview grade, grouped by pattern, each tagged with its level and where it is asked; solve one, then the next harder one | The exercise sets (L1 to L6, tagged); the practice lab; the take-home | A list with no teaching between rungs; each rung names the one idea it adds |
| Brilliant and explorable explanations (Bret Victor, Nicky Case) | Pose a problem before any explanation; let the learner change an input and watch the output; explain only after they have tried | The explorer; the first slide of each chapter as a question; design items in exercises | Endless fiddling; every control has a question attached and a number it moves |
| The Feynman technique | Explain the idea in plain words a newcomer could repeat; find the gap where the explanation breaks; fix that gap; simplify again | Study notes; the cheat sheet; the self-check; the interview answer's first sentence | Simplifying until it is wrong; plain words still carry the exact definition |
| Worked examples that fade | One fully worked example, one half worked, then one blank, on the same pattern | Guided then unguided exercises; notebook your-turn cells | Fading too fast for weak learners; L1 and L2 keep the full worked version |
| Peer instruction | A question that splits the room; everyone predicts and votes; neighbours argue for two minutes; everyone votes again; then the reveal | Live in class at each trap; Kahoot | Using it on questions with an obvious answer; it needs a real split |
| Retrieval and interleaving | Ask yesterday's idea before today's starts; mix earlier topics into later practice once each is learned | Kahoot return questions; take-home self-checks; Saturday papers | Reviewing before anything is learned; retrieval follows first teaching |
| Hans Rosling and Gapminder | Ask the room to guess a fact about the world; show how far the guesses sit from the data; let the data move on screen; name the instinct that misled | The opening of a chapter where intuition misleads; the explorer's moving charts | Turning every chapter into a quiz show; one per day is enough |
| fast.ai, beside Karpathy | Show the whole working result first, then open it up layer by layer; Karpathy's counterweight builds the same thing from scratch in a few lines | The notebooks' first cell (the end result) and their last cell (the from-scratch version) | A from-scratch build for its own sake; the build always answers the case's question |
| Interview rehearsal on annotated answers | Show the question as an interviewer asks it, a weak answer and a strong answer with notes on what each does, then the follow-ups; the learner rehearses aloud | The interview room of every day; the Saturday mock round | Memorised answers; the follow-ups change the question so only the reasoning transfers |
| The case method | A real situation with a decision, the data and the people with a stake; learners argue a position and defend it | The day's ticket; role cards; the stakeholder objection at L5; build-week projects | Discussion with no evidence; every position cites a number from the data |

## How a concept chapter blends them

A concept chapter teaches one row subtopic from zero on its educational example, and runs in this
order, each beat naming its style. The example is simple, complete and relatable: a canteen's
tokens, a hostel canteen's twelve lunch orders, a coaching centre, a chai stall's Sundays, with
invented numbers small enough to count on one hand and labelled invented wherever they appear. The
day's seeded generator writes its table to `data/` and the facts file records its numbers under
`toy_` ids.

1. The broken default: what goes wrong without this idea, in one line on the example (lesson-architecture's slot 3).
2. The misconception said aloud and a prediction voted, on the example's numbers (Veritasium, peer instruction).
3. The hand count on the tiny numbers, every step said aloud (StatQuest).
4. The picture that makes the mechanism visible, and the formula or rule named last as the shorthand for what the picture showed (3Blue1Brown).
5. A glimpse of three to six lines of code that reproduce the count, each line's purpose in plain words; the concept notebook does it in full (Krish Naik).
6. A second example of the same shape with one step missing, then the bare problem (worked examples that fade).
7. Three to five one-sentence rules a learner photographs (lesson-architecture's slot 9), and the interview line the idea earns.
8. The map node: the idea joined to the previous subtopic, the next one and the case chapter that applies it, with the chapter named (ByteByteGo).

## How a case chapter blends them

A chapter of the case ladder runs in this order, and each beat names its style. Where a beat uses an
idea a concept chapter taught, it recalls that chapter by name in one line and goes to the data; the
connected example lives here and the clearest example lives in the concept chapter, so every idea has
both (lesson-architecture's two-examples rule).

1. The question on screen, before any explanation (Brilliant).
2. The misconception said aloud and a prediction voted (Veritasium, peer instruction).
3. The hand count on the twelve rows (StatQuest).
4. The picture that makes the mechanism visible on the case's data, and the formula recalled by its concept chapter's name (3Blue1Brown).
5. The code-along on the full data to a working result (Krish Naik).
6. The trap: the plausible wrong number, revealed against the prediction (Veritasium).
7. The map slide linking the idea to earlier and later ones and to the concept chapters it applied (ByteByteGo).
8. The rung of practice problems at this level (takeUforward), with worked examples fading.
9. The plain one-sentence explanation the learner could repeat in an interview (Feynman).

## How each artefact family carries the blend

- **Decks** carry the concept map after the week map, then every concept chapter's beats 1 to 4, 7
  and 8 on slides with beat 5 as a code glimpse, then every case chapter's beats 1, 2, 4, 6 and 7 on
  slides, beat 3 on the board or a slide of tiny numbers, beat 5 as a short code glimpse, and beat 9
  as the chapter's closing line.
- **Notebooks** come one per chapter. A concept notebook carries its chapter's beats 3 to 7: the
  example loaded from `data/` and printed in full, labelled invented, the count by hand and by code
  asserted equal, the picture, the formula as a function, the faded second example as a your-turn
  cell, and the rules. A case notebook carries beats 3, 5 and 6: the twelve rows reproduced, the
  code-along with one sentence above each cell, the your-turn cell where the trap is found, and the
  second route that agrees.
- **The explorer** carries beats 1, 2 and 4 as scenes: a question, a prediction, a moving picture, a
  number, then the formula.
- **Exercises** carry beat 8 as a tagged ladder from L1 to L6, with fading worked examples and some
  wrong answers to debug.
- **Study notes and cheat sheets** carry beat 9 first and the picture of beat 4 beside it, then the
  map of beat 7 and what an interviewer checks.
- **Interview preparation** carries the case method and beat 9: the question as spoken, the weak and
  hire-grade answers side by side, the follow-ups, and the AI-company variant.
- **Projects** carry the case method end to end: the ticket, the data, the milestones climbing the
  levels, the demo, and a defence questioned at interview grade.
