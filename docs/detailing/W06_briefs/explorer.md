# Build 2, explorer session: the story of an ML project from ask to production

INTERNAL. Read `common.md` first, then the Week 5 explorer rules in
`docs/detailing/W05_briefs/explorers/common.md` and the kit's manual `scripts/companion/W5KIT.md`.
Branch `w06-explorer`. Skills: `companion-builder` (its Rules), `design-taste-frontend`, `dataviz`,
`concept-packaging`, `humanizer`.

Build `content/W06/D2/3_explorer/C2_W06_D02_explorer_STUDENT.html` on the Week 5 kit, inlined with
`python3 scripts/build_companion.py <page>`. Screenshot the merged Week 5 explorers first with
`scripts/explorer_shots.py` and match their quality. The explorer teaches the method on invented
numbers, worked parallels and real cases, and it never hands a group its answer on the card data.

| Route | What it does |
|---|---|
| `#story` | Rohan's ask told as an animated storyline: Kalpa has no card history, a public book proves the method, the call before the due date, the two costs. The learner predicts how many in 100 default before 22 appears. |
| `#map` | The concept map of an ML project: the eight ladder stages as a path, linked back to Weeks 1 to 5 (framing, the split, the confusion matrix, the cost threshold, leakage, overfitting, the memo) and forward to deployment and monitoring in later weeks. |
| `#p1` | Stages 0 and 1, black box to frame: the money flow drawn, who decides, what is known when. |
| `#p2` | Stage 2, requirements: sort statements into FR, NFR, constraint, security, privacy and governance, and see what each one changes; the Apple Card scene as the cost of a missing explanation path. |
| `#p3` | Stage 3, options: a rule against a model on invented numbers, the A against B sheet filling in, the decision and the fact that flips it; Google's Rules of ML rule 1. |
| `#p4` | Stage 4, the POC: honest evaluation, the do-nothing bill, the threshold sweep and the error bill, the top-N list against capacity, on invented numbers. |
| `#p5` | Stage 5, the architecture: a black box opening into a white box (data, features, train, evaluate, score, serve, monitor), one box zooming into its LLD, the training and serving paths drawn apart. |
| `#p6` | Stage 6, POC against MVP against production: what each must prove, the iceberg under the model, what changes when Kalpa's own data arrives. |
| `#p7` | Stage 7, present and defend: the twelve-minute run sheet as a timeline, the passport, the answer-first sentence built word by word. |
| `#case` | The worked parallel ("I do"): the same ladder walked on Week 5's bank campaign data, with its real numbers from the Week 5 pack; then the leak exhibit on HMDA (public domain), where the interest-rate field written after the decision scores AUC 0.98, exported by `4_trainer_only/C2_W06_D02_explorer_data_INTERNAL.py`. |
| `#field` | Verified scenes from `W06_references.md`: Apple Card (NYDFS 2021 and CFPB 2024), Upstart's tested model, Ascarza on whom to target, Stripe's latency and selective labels, RBI's written reasons and digital lending rules, MuleHunter.AI; then the six seats. |
| `#interview` | The ML system design walk for a credit risk or collections system, played step by step with the whiteboard building (the ten steps in `W06_references.md` section 4), plus four to six situations from its follow-up list, each with the clarifying question, the ordered steps, the committed answer, the model answer and the room's usual wrong answers crossed out. |
| `#check` | Visual checks, the map with the ladder lit, and the week's rhythm. |

An openly licensed image from `W06_references.md` section 5 may appear with its attribution line
printed beside it (decision `w6-open-images`); prefer the kit's own drawings. Run `html_sweep.py` and
`explorer_shots.py --end --tabs` and look at every picture before you finish.
