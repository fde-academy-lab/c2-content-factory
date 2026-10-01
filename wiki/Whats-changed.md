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
| 13 Sep 2026 | Client zero moved to v2.2. Kalpa's stakeholders are named and fixed, three threads run the length of the programme, the business-question ladder is fixed to the day for Weeks 1 to 9, domain rotation is scheduled (Retail only for Weeks 1 to 4, then Health, Financial Services and Connect in the build weeks), and the dataset ladder runs v0 to v6 plus the text and corpus sets. | [`docs/07_Client_Zero.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/07_Client_Zero.md) | `locked` |
| 13 Sep 2026 | The curriculum week tab moved from twelve columns to fifteen. The three new ones lead: the business scenario in the stakeholders' words, the thinking trained before any tool, and the interview angle. A day pack is now built in that order, so a deck opening on a topic title was not built from the row. | [`docs/05_Curriculum_Map_Schema.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/05_Curriculum_Map_Schema.md) | `method` |
| 13 Sep 2026 | What is planted in a dataset is never named to a learner. The row's client-zero column is TRAINER ONLY, and the room is meant to find the bulk order by sorting and the duplicates by reconciling. | `02_Content_Doctrine.md` section 12 | `method` |
| 13 Sep 2026 | The build-week group discussion runs on the expert's Friday and Saturday at about 30 minutes per group, unprepared and expert-led. It previously read as a Monday hour with 30 to 45 minutes of preparation, which the Structure tab and the Week 3, 6 and 9 tabs both contradict. | [Running a Situation Room](Running-a-Situation-Room) | `ruling` |
| 13 Sep 2026 | The exam anchors were corrected to ME1 in Week 5, ME2 in Week 10 and ME3 in Week 15. The programme facts file had Weeks 9, 15 and 20, which contradicted the Structure tab, the modules file and the Week 5 tab. | `01_Programme_Facts_C2.md` | `ruling` |
| 13 Sep 2026 | The daily check is Kahoot alone. The Neo daily MCQ pool is gone and the pen-and-paper test sits on Saturday, not Friday. | `01_Programme_Facts_C2.md` | `ruling` |
| 19 Sep 2026 | The Saturday recap paper became objective: fill in the blank, true or false, one or more correct options, scenario sets, applied maths and ordering, graded easy to hard, tagged by role, swapped and marked against a key. | [`docs/curriculum/Saturday_papers.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/curriculum/Saturday_papers.md) | `method` |
| 21 Sep 2026 | The calendar moved a week: Week 0 runs 28 September to 3 October, teaching starts on Monday 5 October and Week 20 closes on 20 February 2027. The re-cut gave Week 1 a Friday lab, Week 4 a communication Tuesday and Week 7 the tokenization Friday. | [`docs/programme/calendar.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/programme/calendar.md) | `locked` |
| 21 Sep 2026 | ME1, ME2 and ME3 carry 70, 100 and 130 proposed marks, and ME3 moved to the first half of Week 16 Monday. | `01_Programme_Facts_C2.md` | `ruling` |
| 21 Sep 2026 | About 60 hours of IITGN faculty sessions were planned as 30 tentative blocks in Weeks 2, 4, 5, 7, 8, 10 and 11, each after the day's applied core. | [`docs/programme/faculty-plan.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/programme/faculty-plan.md) | `content` |
| 27 Sep 2026 | Every movable fact now lives in `data/programme/facts.yaml` with a status, and `python3 scripts/sync_programme.py` regenerates everything that follows from it, from the exports to the board's calendar; a workflow runs it on every branch and checks it on every pull request. | `CLAUDE.md`, `scripts/sync_programme.py` | `tooling` |
| 27 Sep 2026 | The board follows the new calendar: Week 0 and Weeks 10 to 20 joined it, and seven cards moved in place where a holiday and a working day swapped weekdays. | [The content board](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/agents/content-board.md) | `tooling` |
| 27 Sep 2026 | Nine skills were imported from five upstream repositories for visual direction, the analytical lens of study notes, brainstorming before the spine, verification before done, and public pages. | [`docs/skills-imported.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/skills-imported.md) | `method` |
| 30 Sep 2026 | The Saturday recap paper prints in parts named for what each shows, with each item's format and level beside it and up to six recall items on an untimed stretch page, and the room sits a Word paper in the Week 0 diagnostic's format with its answer sheet at the back. | `CLAUDE.md`, `.claude/skills/exercise-builder/SKILL.md` | `method` |
| 30 Sep 2026 | Anand Iyer is Kalpa Retail's finance controller in every pack and paper, where the tracker's Week 1 and Week 2 rows called him the CFO. | `data/programme/facts.yaml`, decision `anand-finance-controller` | `ruling` |
| 30 Sep 2026 | All thirty option edits and relabellings laid on the Week 1 and Week 2 Saturday papers were accepted, and each applies until the tracker's Saturday papers tab carries it. | `data/programme/paper_edits.yaml` | `content` |
| 30 Sep 2026 | The week's Saturday recap paper, and no other learner file, may name a plant the room has already found in class, so the Week 1 Saturday paper keeps the two tracker items that name Week 1 Monday's plants. | `CLAUDE.md`, decision `plants-once-found` | `ruling` |
| 30 Sep 2026 | The Week 2 Tuesday interview line asks what you do when the validation fails at the end of reporting day, where tracker v7 named a clock time. | `docs/curriculum/source.xlsx`, decision `reporting-day-line` | `content` |
| 30 Sep 2026 | The Saturday recap papers became interview grade: the tracker's bank sets what is tested, any bank item may be reworded, folded into a deeper item or moved to the stretch page with its reason, about 60 percent of the timed items are hard, every part opens on a Kalpa scenario with a visual, and blanks, pairs and statements are answered from word banks, match tables and reasons. | `CLAUDE.md`, decision `saturday-interview-grade`, `.claude/skills/exercise-builder/SKILL.md` | `method` |
| 30 Sep 2026 | The Saturday recap papers may set items at named, real companies and in public case studies alongside Kalpa, with every real figure checked against a dated source and anything unchecked written as a labelled hypothetical. | decision `saturday-real-cases`, `CLAUDE.md` | `ruling` |
| 30 Sep 2026 | A teaching day runs in about six chapters, each one deck chapter paired with one notebook that builds on the one before it; every chapter states the problem, lays out two to four answers sized in rows, minutes, rupees and error, makes the best-fit call and reaches its number a second way before the code is called done; and every pack runs a five-pass depth loop whose last two passes are fresh reviewers. | [`the-standard.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/.claude/skills/day-pack-builder/references/the-standard.md), `CLAUDE.md` | `method` |
| 30 Sep 2026 | The programme prepares learners for four domains, retail and e-commerce, US healthcare, financial services, and SaaS and enterprise AI, and each opens on its story from a domain dossier the first day it appears, with Kalpa's unit set beside the real companies it resembles. | [`domain-dossier.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/.claude/skills/day-pack-builder/references/domain-dossier.md), decision `four-domains` | `method` |
| 30 Sep 2026 | Kalpa Health became a US-facing diagnostics and revenue-cycle business run from Kalpa's GCC, so Build 1 teaches US healthcare in dollars with payers, claims and denials; the Build 1 generator and the Week 3 packs follow. | [`docs/07_Client_Zero.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/07_Client_Zero.md) section 1c | `locked` |
| 1 Oct 2026 | Build 1's visit register is drawn from the bookings, so every register row names its booking and a rebooked patient's missed slot sits beside the kept one; the no-show sub-problem is re-planted on it. | [`docs/detailing/W03_build1_spine.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/detailing/W03_build1_spine.md), decision `build1-register-from-bookings` | `content` |
| 1 Oct 2026 | Week 1 Tuesday's files after chapter 3 may state the frequency fall the room finds there, each on its own page, since every file stands alone. | `CLAUDE.md`, decision `tuesday-finding-once-found` | `ruling` |
| 1 Oct 2026 | Week 1 Thursday's exposure table is the campaign platform's August list under its own customer ids, a separate population from Finance's order file. | [`docs/07_Client_Zero.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/07_Client_Zero.md) section 1d | `locked` |

---

## Open decisions, waiting on somebody

These are not gaps in the writing. They are questions only the Programme Head can settle, and
nothing should be built on a guess about them.

| Question | Why it is blocked | What is blocked by it |
|---|---|---|
| Should Kalpa cover United States healthcare, travel and airlines, or professional services? | All three are outside the locked file. Adding a sixth unit changes the shape of every build week, since each draws one sub-problem per unit. | Situation cards in those domains, and any build-week brief that would use them |
| All marks and weights | The scheme proposed to the AOC on 25 September awaits its lock | Any artifact that states a weight, a mark total or a percentage. Nothing may reconstruct a total from partial figures. |
| The IITGN faculty members and dates | Every session is tentative until IIT Gandhinagar confirms it | The timing lines of the 30 days that carry a block |

The full register, with who closes each decision and the working rule for every conflict between
sources, is [`docs/programme/decisions.md`](https://github.com/fde-academy-lab/c2-content-factory/blob/main/docs/programme/decisions.md).

The first one is the one this wiki most wants an answer to. See
[The Kalpa world](The-Kalpa-world#what-is-not-in-kalpa-and-is-an-open-decision) for what each option
would cost.
