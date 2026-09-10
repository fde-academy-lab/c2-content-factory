# Page anatomy

## The shape a day gets

A one-topic teaching day gets one page: a header, a left rail listing that page's sections with active tracking, and the sections themselves. A day with several distinct parts gets a grouped title bar, and the groups are named for what the learner is doing rather than for the topic: understand, build by hand, build without code, test, operate. Reference and contact sit on the right.

Most days in a teaching week are one topic. Reach for the grouped bar only when the single page has genuinely stopped scrolling sensibly.

## The guided walk

One Next button, and nothing else advancing the state. Each press fires one event and three things move together:

1. The diagram, with the current node lit.
2. The artifact, with the line or row that just changed marked.
3. The meter, where the topic has one worth counting.

A narration card sits beside them and is rewritten per event: two or three full sentences saying what just happened and what to look at. The card never says "click Next", because the button is visible and the card's job is the content.

A meter explains itself. It carries a legend and, on click, a per-item breakdown of what it is counting. A number with no breakdown behind it is a decoration.

## Experiment cards

One card, one change. Eight parts, in this order, and none is optional:

| Part | What it holds |
|---|---|
| Situation | Two sentences putting the learner in a specific moment with the running case named |
| Hypothesis | What the learner should expect before running, stated as a claim they can be wrong about |
| Watch for | The one thing on screen that will move, named precisely |
| Run | The control. One button, or one toggle with two states |
| What happened | Written after the run, from the real result rather than from a script |
| Why it matters | The consequence in the work, with a number where there is one |
| The rule | One sentence a learner could repeat in an interview |
| Sequence popup | The same run drawn as a sequence across the named lanes |

The first card on the page is the day's existing toggle idea. It is what the trainer already knows how to run, and losing it to a redesign costs more than it gains.

## The other page kinds, and when a day earns one

| Kind | Anatomy | Earned when |
|---|---|---|
| Classify exercise | Lines with lettered choices, per-line feedback, a running score | The day has a judgement applied repeatedly to similar items |
| Layer builder | A system map growing one part per layer, code with the current layer highlighted, a capability line | The topic is built up in stages and each stage unlocks something |
| Workbench | A few fields in, real output out, and a verdict that refuses bad input | The learner will generate something they paste elsewhere |
| Simulator | A stepper of choices, a run producing a sequence diagram, probes against the configuration, a readiness verdict with reasons | The topic is a configuration whose consequences are not visible until it runs |
| Ladder page | Options with verified rates and sources, a decision tree, a matrix, the same run priced on every option, a calculator for the deciding inequality | The choice is between tiers that differ on cost |
| Playbook | A pyramid with popups per level, a decision tree for the instrument, methods each opening a worked example, gates as flowcharts, a symptom lookup | The day teaches a practice rather than a mechanism |
| Framework page | Each letter defined, situations, numbered steps, where the idea came from with sources, a case, a without-it and with-it contrast, where it stops | The day introduces a named framework |
| Formula page | Each rule with a number as a calculator showing its formula and a sentence on what the number means | The day's rules are arithmetic |
| Reference page | Practices with in-place checks, mistakes with how each shows in the artifact, a filterable glossary, printable visual and text cheat sheets | The day produces something a learner will look up later |

A day gets the kinds its topic actually is. Building all ten is how a companion becomes unmaintainable.

## The rules, restated as things to check on screen

**Important text is never grey.** Grey is for captions, units and provenance. A rule, a verdict or a number is ink.

**Every control does something visible.** Click each one and watch the page. A control whose only effect is internal state needs a visible acknowledgement, even if that is one changed word.

**Nothing is preloaded.** A page that opens with the result already showing makes the Run button look broken. Open empty, with the situation and the hypothesis visible and the result area holding one line saying what will appear there.

**A popup earns its place.** It adds a breakdown, a worked example, a sequence, or a why-this-step. A popup that repeats the text behind it is a second click for nothing.

**Full sentences.** Card bodies, narration, rule lines, glossary entries and calculator captions are all sentences with verbs.

**Provenance.** Simulated numbers say they are simulated. Any rate or price carries the date it was verified. Nothing is invented, and a slot with no verified source says "to be found".
