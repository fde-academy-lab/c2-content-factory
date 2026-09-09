# The locked note template

Every study note carries these nine sections in this order. The budgets keep the whole note inside a 25-minute read; when the draft runs over, trivia and history go first and every concept stays.

## 1. Header band, top of page one

One line gives the session title as taught. One line under it gives the promise: a full sentence naming what the reader can do after this note that they could not do before, written in the skills-unlocked language of the curriculum map. No logos, no dates, no names.

## 2. Key takeaways, about half a page

Five to seven full sentences, each carrying exactly one fact or capability from the session, ordered from the biggest idea downward. A takeaway states the insight itself ("Chunk boundaries decide retrieval quality more than embedding choice does"), never the topic label ("We covered chunking").

## 3. Where this sits, one page

Three parts, visual first. A curriculum strip shows the phase this session lives in with the phases before and after it greyed, drawn from curriculum-map.md. The landscape map shows the nine territories with everything covered so far shaded and this session's territory highlighted, so the learner sees cumulative progress at a glance. Then two or three concrete situations where an FDE meets this material on a client engagement or as an FTE, each a short paragraph anchored to a named situation type (a discovery call, a PoC sprint, a production incident, a cost review) and written to the learner as "you".

## 4. What was covered, three to five pages

One subsection per concept, four to seven concepts. Each subsection carries, in order:

- an action title, meaning a full sentence stating the point, never a topic label;
- the four beats from concept-packaging: the plain definition, the concrete contrast with real values, the action the learner takes, and the sticky handle;
- one visual wherever a diagram or chart beats the paragraph it replaces;
- one verified company use case with a number in it, attributed by company and year;
- at most one trivia or history box, included only when it makes the concept stickier, and verified like everything else.

Values inside a concrete contrast come from the transcript or from verified sources; a pair constructed for teaching is labelled a worked example.

When session materials were supplied, a concept's visual may be a harvested or redrawn asset from them, and code appears as a captioned panel trimmed to the lines that carry the point; the harvesting rules live in SKILL.md and the panel styles in assets/note-style.css.

## 5. Beyond the session, half a page to one page

Extensions the session pointed at without covering: the neighbouring technique the learner will meet next, the session's analogy carried further with the point where it breaks stated out loud, and one or two parallel use cases from a different industry than the session's own examples.

## 6. Try it yourself, half a page

One challenge requiring no writing and no code: a scenario to reason through, a design to sketch mentally, an ordering to commit to, or an estimate to defend. It should be doable in 15 to 20 minutes. Close the section with a self-check box the learner scores against: the expected reasoning in three or four sentences, plus the one misstep most people make on this challenge.

## 7. FDE interview questions, about one page

Four to six questions of the kind FDE and applied-AI interviews actually ask on this topic. Each gets a model answer of three to five sentences demonstrating the reasoning an interviewer rewards, and one line on what a weak answer sounds like.

## 8. Glossary, about one page

Every term the session used, as a table with three columns: the term, its plain meaning in one sentence, and one application or example. Alphabetical order. A term already explained in section 4 still appears here in shorter form.

## 9. Further reading, the last page

One or two YouTube videos first, each with creator, duration and one sentence on why it earns the learner's time. Then two to five blogs, docs or papers with the same one-line treatment. Every link is fetched live before inclusion, and the list is ordered by what to consume first.

## Writing rules, applied to every section

- No em dashes and no en dashes anywhere, including captions, code, tables and alt text.
- These words never appear: Additionally, Moreover, However, Hence, Thus, Nonetheless, Furthermore, Accordingly, Indeed, Dynamic.
- No "not X, but Y" constructions and none of the tic patterns the llm-tic-scrubber catches; the scanner run is mandatory before rendering.
- Every bullet and every table cell is a full connected sentence, with glossary term cells and link titles as the only exceptions.
- "You" in the note always means the learner, and the note never mentions its own construction, its instructions, or the transcript it came from.
- Plain words come before formal terms: the problem arrives first, then the term that names it, and the term then lands in the glossary.
- Every sentence carries a fact, an instruction or a decision, so anything that only manages expectations gets deleted.
- Numbers are real and verified, or the passage is labelled a worked example.
- Headings state points as full sentences wherever the format allows, because a heading that states the point teaches even a skimming reader.
