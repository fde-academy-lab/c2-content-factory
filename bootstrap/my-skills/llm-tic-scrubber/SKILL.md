---
name: llm-tic-scrubber
description: Scrub machine-written phrasing out of any deliverable before it ships. Use whenever writing or reviewing slides, documents, exercises, briefs, emails or training content, and especially when a draft has been rejected as reading generic, boring, robotic, or "not how a professional writes". Catches antithesis constructions, fragment stacking, repeated labels, hedge openers, triads, and the other tells that mark text as generated. Runs a scanner and gives the rewrite for each pattern.
---

# LLM tic scrubber

Content is rejected for *sounding* generated far more often than for being
wrong. These are the tells, ranked by how often they have actually caused a
rejection.

## Run the scanner first

    python3 scripts/tic_scan.py <file.md|file.pptx|file.docx>

It reports each hit with a line or slide number and the class of tic. Fix
every hit before showing the work.

## The tics, and what to write instead

### 1. Antithesis: "not X, but Y"

The single most recognisable tell. Also appears as "it is not A. It is B",
"less A, more B", "X is not about A, it is about B".

- Rejected: "This is not a framework, but a way of thinking."
- Write: "This is a way of thinking." Say the thing. The contrast adds nothing.

### 2. Fragment stacking

Two or three clipped sentences in a row, used for emphasis. Reads as ad copy.

- Rejected: "Two questions. Four builds. The same four from yesterday."
- Write: "Two questions place any piece of work into one of the four builds."

### 3. The repeated label

Any bolded lead-in used more than twice in a document. "In plain words:",
"Key insight:", "The takeaway:", "Bottom line:", "Note:".

- Fix: delete the label and write the sentence. If the point needs signposting
  more than twice, the structure is wrong, not the labelling.

### 4. Triads everywhere

Three parallel items where two or four would be truer. Generated text
defaults to three.

- Fix: count the real items. Ship two, or five, when that is the honest number.

### 5. Hedge openers and empty scaffolding

"It is worth noting that", "It is important to understand", "Let us explore",
"When it comes to", "In today's fast-paced".

- Fix: delete the opener. The sentence after it is the sentence.

### 6. Closing inspirational lines

"That is the whole point.", "And that changes everything.", "Carry this out of
the room." A mid-senior audience does not read them.

- Fix: end on the last factual sentence.

### 7. Elegant-variation churn

Renaming the same thing three ways in one page (the framework, the model, the
approach, the lens) so nothing is nameable.

- Fix: pick one noun and repeat it. Repetition reads as rigour.

### 8. Symmetry that is not real

Tables where every row has the same shape because the shape was filled in,
not because the content matched. Watch for a column of near-identical
sentence lengths.

- Fix: let rows be uneven. Delete any cell that exists only to complete a grid.

### 9. Over-signposting the structure

"First we will look at X, then Y, and finally Z", followed by X, Y and Z.

- Fix: keep the map if the audience genuinely needs it, and cut every later
  repetition of it.

### 10. Words that mark the register

Delve, tapestry, testament, landscape, realm, navigate the complexities,
leverage as a verb, robust, seamless, holistic, unlock, harness, elevate,
crucial, pivotal, vital, myriad, plethora.

- Fix: use the plain word. Most of the time the plain word is shorter.

## Two checks the scanner cannot do

**Read it aloud.** Anything you would not say to a colleague standing in front
of you comes out.

**Check that every sentence carries a fact.** Sentences that only manage the
reader's expectations ("this is important because", "as we will see") are the
residue of generated prose. Delete them and the paragraph gets better.
