# The domain dossier, its card and its story

Most of the room has never worked in a business role. Before a learner can size a solution for a
retailer, a US health system or a bank, they need to know how that business makes money, who in it
asks for numbers, what those numbers mean, which rules bind the data, and where analytics, ML, NLP
and agents pay for themselves. The dossier carries that, once per domain, and every later day in the
domain builds on it rather than re-explaining it.

The requester set this on 30 September 2026 (decision `four-domains` in `data/programme/facts.yaml`,
which lists each domain, the day it enters and where its dossier lives). The retail and e-commerce
dossier in `content/W01/D1/` is the model.

## What ships on the domain's first day

| File | Folder | What it is |
|---|---|---|
| `C2_W{ww}_D{dd}_domain_{name}_STUDENT.md` | `study-notes/` | The dossier, 6,000 to 8,000 words in the twelve sections below, each opening on a relatable scene before any term or formula |
| `C2_W{ww}_D{dd}_{name}_domain_card_STUDENT.md` and its PDF | `cheatsheets/` | One printed page: the metric tree, the ten metrics with formulas, the twenty terms a learner must say fluently, the compliance list |
| `C2_W{ww}_D{dd}_domain_story_TRAINER.md` | `trainer/` | The talk track for the 45-minute story that opens the day: what to say in what order, the question to ask the room at each turn, the one board drawing per part |
| `C2_W{ww}_D{dd}_domain_sources_INTERNAL.md` | `internal/` | Every source with its URL and the date checked, and a line per fact on where it came from |

The day's morning deck opens its first chapter on the story, and the day's other chapters link to
the dossier's sections by name.

## The twelve sections

1. **A day in the life.** One working day at Kalpa's unit told as a story, through the people who run
   it and the customer or patient it serves. Every role and number that appears later is planted here.
2. **Which real company Kalpa's unit is like.** The real companies whose shape the unit shares, and
   what each teaches; the GCC's twins among the Indian technology centres of global companies in the
   domain. Stated as analogies, every fact about a named company checked against a source.
3. **How the business makes money.** The P&L from revenue to operating profit in the domain's own
   terms, the unit economics of one order, claim, loan or seat, and the working capital that ties
   cash up.
4. **Who decides what.** The org chart, and for each role what it owns, what it asks the data team
   and what a wrong number costs it. Kalpa's named people from `docs/07_Client_Zero.md` mapped onto it.
5. **The metrics, as formulas.** The domain's metric tree and each metric with its formula, a worked
   number from a relatable example, the trap it hides (an average across segments, a rate on a small
   base, a denominator that shifted) and who asks for it.
6. **The domain language.** About thirty terms a learner should say fluently in a stakeholder
   meeting, each defined in one line with its use in a sentence.
7. **Compliance and the rules the data team works under.** The laws and standards for India and for
   the US where the GCC serves a US client, each with what it forbids or requires of an analyst or an
   AI system, checked against the official source.
8. **Where analytics, ML, NLP and agents earn their keep.** For each use: the business problem first,
   why the technique is needed, how it works in outline, how its value is measured and what it costs
   when it is wrong.
9. **The common technical problems, with their options.** Six to eight problems a data team in the
   domain actually faces, each with two to four solution options, how to size them (rows, cost, time,
   accuracy), the best fit for a team like Kalpa's and the fact that would change the choice.
10. **Relatable examples, converted.** Five everyday scenes, each converted into its metrics, formulas
    and the data and AI problem hidden in it.
11. **Interview questions this domain asks.** Ten, tagged as the programme tags them, as questions
    only; the answers belong in the day packs.
12. **Go deeper.** A reading path of verified sources, each dated.

Visuals: a Mermaid diagram at least for the value chain, the org chart, the P&L and the metric tree,
through the shared theme and measured per CLAUDE.md's diagram rule. Tables where a comparison is the
point.

## Truth

Every fact about a real company, a regulation or a market figure is checked the day it enters, with
its URL and date in the sources file. A figure that cannot be checked is left out or given as a
labelled illustrative number. Kalpa's own numbers come from `docs/07_Client_Zero.md` and the unit's
data, nothing beyond the lock, and a planted value is never named.

## Proof

The llm-tic-scrubber scanner on every markdown file, `python3 scripts/build_cheatsheet.py` on the
card, and `python3 scripts/verify.py` on the day folder.
