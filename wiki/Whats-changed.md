# What's changed

A dated log of decisions, so nobody re-litigates a settled one and nobody teaches last month's
shape.

**One line per decision.** What was decided, when, and where it is written down. If a decision needs
a paragraph, the paragraph belongs in the file it affects, and this page links to it.

---

## How to add a line

Add it in the same pull request as the change it describes. A decision that lands here a week later
has already been re-argued once.

| Column | What goes in it |
|---|---|
| **Date** | The day it was decided, not the day it was written up |
| **What changed** | One sentence, in full, saying the decision rather than the topic |
| **Where it lives** | The file or page that is now the binding version |
| **Kind** | `locked`, `ruling`, `method`, `tooling` or `content` |

`locked` means a file has been frozen and now changes only by a versioned edit. `ruling` means two
sources disagreed and somebody chose. `method` changes how packs are built. `tooling` changes a
script or a gate. `content` changes what is taught.

---

## The log

| Date | What changed | Where it lives | Kind |
|---|---|---|---|
| 09 Sep 2026 | Client zero was locked at v1.0: Kalpa Group, five business units, Kalpa Retail as the teaching spine for Weeks 1 to 15. | [`docs/07_Client_Zero.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/07_Client_Zero.md) | `locked` |
| 09 Sep 2026 | Four conflicts found while building Week 1 were ruled on and the locked file moved to v1.1: the `v1` dataset arrives on Wednesday rather than Tuesday, the near-duplicate pair differs on `order_date`, `discount` sits on the order, and the typical order band describes the population rather than the planted whale. | Section 9 of `docs/07_Client_Zero.md` | `ruling` |
| 10 Sep 2026 | Cheat sheets are printed by a builder rather than hand-made: `scripts/build_cheatsheet.py` renders the markdown to a landscape PDF, and the gate now fails a sheet with no PDF or a PDF older than its markdown. | `scripts/build_cheatsheet.py`, `scripts/verify.py` | `tooling` |
| 10 Sep 2026 | Every diagram is measured before it ships. A label that would print under about five points on a sheet or nine on a slide means the diagram is reshaped, never that the page shrinks it. | `CLAUDE.md`, [Conventions](Conventions-and-house-style) | `method` |
| 10 Sep 2026 | The deck builder now reports blocks it could not place instead of dropping them silently, which surfaced and fixed a class of content loss that predated the change. | `scripts/build_deck.py`, `scripts/deck_layout.py` | `tooling` |
| 10 Sep 2026 | Content progress is tracked on a GitHub Project board in this repository, one card per day pack, driven by `scripts/board_sync.py`. Engineering issues stay as committed markdown under `.scratch/`. | [`docs/agents/content-board.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/agents/content-board.md) | `method` |
| 10 Sep 2026 | Week 1 was moved to `status:rework` rather than closed, because the curriculum and the content both need upgrades before the week is treated as delivered. | The board | `content` |
| 10 Sep 2026 | The wiki's source lives in `wiki/` in this repository and is published by a workflow on merge to `main`. Editing a page in the GitHub wiki UI is overwritten on the next merge. | `.github/workflows/wiki-publish.yml` | `tooling` |
| 10 Sep 2026 | Business cases are held in a Situation Bank, graded L1 to L4, and a card never carries its solution. The build-week group discussion is the bank's primary customer. | [The Situation Bank](The-Situation-Bank) | `method` |

---

## Open decisions, waiting on somebody

These are not gaps in the writing. They are questions only the Programme Head can settle, and
nothing should be built on a guess about them.

| Question | Why it is blocked | What is blocked by it |
|---|---|---|
| Should Kalpa cover United States healthcare, travel and airlines, or professional services? | All three are outside the locked file. Adding a sixth unit changes the shape of every build week, since each draws one sub-problem per unit. | Situation cards in those domains, and any build-week brief that would use them |
| All marks and weights | Two weighting models are in circulation and neither is signed off | Any artifact that states a weight, a mark total or a percentage. Nothing may reconstruct a total from partial figures. |
| The Saturday engagement shape | Up to four hours was agreed in principle and the activity needs confirmation before it can be designed | Saturday packs beyond the recap paper |
| Whether two industry leaders can be secured for a full build week | If they cannot, the build-week plan changes | Build-week design past the group discussion |

The first one is the one this wiki most wants an answer to. See
[The Kalpa world](The-Kalpa-world#what-is-not-in-kalpa-and-is-an-open-decision) for what each option
would cost.
