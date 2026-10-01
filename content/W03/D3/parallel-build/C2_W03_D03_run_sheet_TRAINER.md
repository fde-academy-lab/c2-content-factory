# How does the trainer build New York's revenue tree in the open in sixty minutes, without spending any group's find?

**TRAINER ONLY.** Nothing on this page reaches a learner, since it names the plants the slice runs
beside, with their witness numbers. The notebook is
`parallel-build/C2_W03_D03_new_york_revenue_tree_STUDENT.ipynb`; it ships executed, and every number
on this page is one of its saved outputs or, in the plant table, a witness figure, each recomputed
from the raw files by `internal/C2_W03_D03_numbers_INTERNAL.py`.

The parallel build runs straight after the checkpoint, in the morning block. The row asks it to set
the pace and show the method without handing over answers, so the trainer works a question no group
holds, New York's billed revenue from Q2 to Q3, through the same moves every group's build needs:
one row per record, every amount converted, one file reconciled against another, the tree, a second
route and the claim.

## What is the slice, and where does it start and stop?

**The slice.** Sub-problem 1's revenue tree for one metro, New York, Q2 (April to June 2026)
against Q3 (July to September 2026), read from the old booking export and the claims in
`content/W03/D1/data/`, and stopped at the two leaves a claim carries: how many claims were billed,
and the mean claim. Billed revenue is the dollars on the claims at list prices, what Kalpa Health
asked the payers for, which is more than they will pay.

| Start from | Go as far as | Stop before |
|---|---|---|
| The checkpoint's last answer, and the files every group opened on Monday | One claim with its denominators, period and caveat; a four-row decisions log; the same totals reached in SQL | Anything below the mean claim: what a claim holds, channels, tests, payers, payments, and any other metro |

## What does the trainer set up before the room arrives?

1. Open the Codespace, open the notebook and run it once from the top; it needs under a minute. If a
   cell fails, the executed copy on GitHub carries every output, so teach from that.
2. Clear the board, and draw nothing until minute one: the empty tree goes up live.
3. Keep a blank decisions log open beside the notebook, in the Week 1 Wednesday columns: Field,
   Issue, Rows, Decision, Reason. The groups have the same shape in
   `content/W03/D1/briefs/C2_W03_D01_decisions_log_STUDENT.xlsx`.
4. Zoom the editor until the back row can read a table cell.

## How do the sixty minutes run, step by step?

Ask each predict question before its cell runs, take a show of hands or letters in the chat, and
only then run the cell. The answer letters are in the last column.

| Step | Min | Say | Run | Draw | Ask before it shows, and its answer |
|---|---|---|---|---|---|
| 0. The ask | 4 | "Each group holds one of Dr Menon's five questions. I am taking a smaller one that no brief asks: New York's billed revenue, Q2 against Q3. Watch the moves; New York's numbers answer none of your briefs." | The title cell, read aloud: Dr Menon's words, the finance head as the person who needs it | The empty tree: billed revenue, then claims times the mean claim | "Before I open a file, what would I need to trust each box?" Take two answers; one should be "the count is real". |
| 1. The options | 6 | "Four ways to answer the finance head. The cheap two disagree, so the hour goes on the reconciliation." | Section 1, the sizing cell | Beside the tree: B 8.0 and D 4.8 | Which two options report different volume growth? **b**, B and D. Then: "Which would you trust, and why neither yet?" |
| 2. One row per booking | 10 | "Rows first, then distinct ids, then blanks. I clean nothing I have not counted." Then: "Counted as rows, New York grew 4.8 percent; counted as bookings, 6.8. Which would you send?" | Section 2, the profile cell, then the identity rule | 2,128 rows, 2,095 bookings, 33 set aside; first log row written live, reason included | How many bookings does the export hold? **b**, fewer than 2,128. Then: "Where are the extra rows, Q2 or Q3?" 26 in Q2, 7 in Q3. |
| 3. Every amount converts | 8 | "The amount column is text. There is a quick fix that never complains." Then: "Coerce blanked six amounts, and revenue is $903 short with no error on the screen." | Section 3, coerce, then the fix | Second log row | What does the coerced sum do? **d**, it comes out short. Then: "What check would have caught it before any total?" Count the blanks after converting. |
| 4. Claims against bookings | 10 | "Two files describe the same visits. I prove that in both directions and on its grain." Then: "The raw join says $364,853; the claims say $359,395. That is Week 2's fan-out, and it makes New York's growth read 3.3 percent." | Section 4, the raw join, `validate`, then the outer join and its bridge | On the board: 2,128 = 2,095 + 33, then 2,095 = 2,032 + 63, then 2,032 claims = 2,032 completed | How many rows does the raw join return? **c**, between 2,032 and 2,128 (2,065). |
| 5. The tree, and per day | 9 | "Now, and only now, the tree." Then: "78 more claims at Q2's mean add $13,964; a lower mean takes $4,389 away. Q3 is a day longer, so per day the claims grew 6.8, not 8.0." | Section 5, the tree, the driver tree and the bridge, then the per-day cell | Fill the drawn tree; an arrow up on claims, one down on the mean; 91 and 92 written beside the quarters | Which leaf moved the revenue? **a**, more claims at a lower mean. Per day, how much did claims grow? **c**, about 6.8 percent. |
| 6. Where, and where to stop | 3 | "Site is on every booking, so I split by site, and that is where I stop. What a claim holds is the next branch, and I do not open it." | Section 6 | A dashed box under the mean claim | Which site billed most of the extra claims? **b**, KH-NYC-02. |
| 7. A second route | 4 | "The same build again in SQL: ROW_NUMBER keeps one row per booking, the join, the GROUP BY. If my pandas were wrong, this would disagree." | Section 7 | A tick beside each total on the tree | "What would it mean if the two routes disagreed by $903?" The amounts were coerced on one side. |
| 8. The claim | 6 | Read the claim table aloud: claim first, then the caveat on its own line, then the action. | Section 8, the decisions log and the interview answers | Circle the two denominators in the claim on the board | "What is my caveat, in your words?" Take one answer, then hand over. |

The steps run 4, 6, 10, 8, 10, 9, 3, 4 and 6 minutes, which is 60.

## What does the trainer say to hand the room back to its own build?

Word for word: "That is one metro and one branch, stopped at the claim. Your question is bigger and
messier. Run the same moves on it: say what one row is, convert every amount, reconcile one file
against another, then split, then reach the number a second way. Bring me your claim at the close,
with its denominators, its period and its caveat."

## Which plants does the slice run beside, and how does the trainer hold each?

The plant table is in `docs/detailing/W03_build1_spine.md`. Never name a plant, never quote a
whole-file count, and never compare New York with another metro. Each figure below is the witness
from `python3 data/generate_kalpa_health.py --witness` or the numbers script.

| Plant | Where the slice touches it | What you do | What you never say |
|---|---|---|---|
| The old export repeats rows (sub-problem 2, and everyone's profile) | New York holds 33 of the 180 repeated ids, 26 of its extra rows in Q2 and 7 in Q3; the repeats are booked from 1 June to 26 September | Show the identity rule and log the cause as a question for the data team, which is the habit the room should copy: a count that does not reconcile becomes a dated question in the challenges log | "Re-export", "mid-quarter", 180, or any link to the two metros whose bookings fell |
| Text amounts (sub-problem 1) | 6 of the 60 dollar-text amounts are New York's, $668 in Q2 and $235 in Q3 | Show coerce failing in silence and the strict conversion | 60, or the whole file's $10,559 that coerce hides |
| A panel is one claim line, and the dashboard counts tests (the headline, for every group) | The mean-claim leaf | Stop the tree at the dashed box and never open `line_items` or `booking_tests`. If asked what a claim holds: "That is the next branch. Which file would tell you?" | Tests per claim, panel names, or anything about how the dashboard counts |
| The employer contract (sub-problem 1) | Absent from New York: its largest claim is $410 | Profile New York's rows only, as the notebook does, and never profile the claims file whole | "Is New York typical?" gets "That is what your tree across metros will tell you." |
| The at-home offer (sub-problem 5) | New York's patients were offered it too, a fifth of them at random (316). Its home-collection claims rise from 97 to 160, and 42 of the Q3 ones carry no $20 collection fee, every one an offered patient's. The home claims' mean falls from $194.23 to $175.36 and the other claims' from $177.35 to $174.78, which together pull the mean claim down. New York's offered patients also out-book the rest by 23.5 percent, a chance draw (permutation p of about 0.03) | Never split by channel. If asked why the mean fell: "The claims cannot tell us yet. It is logged as a question for the next branch." If someone proposes a channel split live: "A good next cut, and it is yours to make in your own build." | Channel, the offer, the waived fee, or New York's gap between offered and other patients |
| The system switch (sub-problem 2) | None: New York has no booking in the new system's export, and every New York claim finds its booking in the old one | If asked why the notebook reads only the old export: "Every New York claim finds its booking in this export, and for billed revenue that is the test that matters. Which files hold your own metro's bookings is a profile question for your group." | That two metros moved systems, the date, or the date format |
| Dr Menon's 5 percent (the headline) | New York's billed revenue happens to rise 5.5 percent | If anyone links the two: "A different count. Hers is her dashboard's; ask what it counts." | That the dashboard counts the old system's bookings or a panel as its tests |

The claim keys and double posts (sub-problem 3) and the walk-ins (sub-problem 4) are untouched by
the slice.

## What does the trainer do when the build goes wrong?

| What happens | What you do |
|---|---|
| The Codespace will not start, or a cell errors | Switch to the executed notebook on GitHub. Every output is saved, so teach from the page and let the room read the checks. |
| `FileNotFoundError` on the data | The notebook must run from `parallel-build/`, reading `../../D1/data/`. Pull the branch that carries Monday's data folder, or run from GitHub as above. Give it two minutes and its last line, no more. |
| Minute 45 arrives with step 5 not started | Cut step 7 to its result table, then step 6 to its prediction. Never cut the reconciliation, the claim or the caveat. |
| A group says it has already done all this | Ask for its reconciliation in one line of arithmetic, rows in equal rows kept plus rows set aside. If it has one, the group goes back to its build and skips the rest of the demo. |
| A learner wants to clean the 43 blank channels | Point at the log's kept row: the tree does not use channel, so leaving the blanks is a decision with a reason. |
| A learner asks for the cells to copy | The notebook is in the repository. The cells answer New York's question and the briefs ask others, so what carries over is the order of the moves. |
| Someone asks a question that would open a plant | Write it on the board as a question, say "That is your group's to answer", and go on, since an answer from the front would spend another group's find. |

## Where does every number on this sheet come from?

Every value is a saved output of the notebook, computed from `content/W03/D1/data/`, and every one
is recomputed by `python3 content/W03/D3/internal/C2_W03_D03_numbers_INTERNAL.py`.

| Number | Value |
|---|---|
| New York rows in the old export, distinct booking ids | 2,128 and 2,095: 33 ids on two rows, 26 pairs identical and 7 differing only in `updated_at` |
| Rows against bookings per quarter | 1,039 to 1,089 rows, up 4.8 percent, against 1,013 to 1,082 bookings, up 6.8 percent |
| The four options' volume readings | B, the claims: up 8.0 percent; D, the export's rows: up 4.8 percent; C reads 4,160 rows against B's 2,032 |
| Dollar-text amounts, and what coerce hides | 6 amounts, $668 in Q2 and $235 in Q3, $903 in all |
| The fanned join | 2,065 rows and $364,853 against 2,032 claims and $359,395, $5,458 too much ($4,589 in Q2), so growth reads 3.3 percent |
| Kept, cancelled, completed, claims | 2,095, 63, 2,032 and 2,032 |
| Billed revenue, Q2 to Q3 | $174,910 to $184,485, up 5.5 percent, $9,575 |
| Claims, mean claim, median claim | 977 to 1,055 (up 8.0 percent); $179.03 to $174.87 (down 2.3 percent, $4.16); $150 in both quarters |
| The bridge, in tree order | Plus $13,964 for the extra claims, minus $4,389 for the lower mean; reversed, $13,640 and minus $4,065; the joint part $324 |
| Per day, over 91 and 92 days | Claims up 6.8 percent, billed revenue up 4.3 percent |
| By site, claims Q2 to Q3 | KH-NYC-01, the laboratory, 328 to 319; KH-NYC-02 296 to 365; KH-NYC-03 353 to 371 |
| The SQL route | 977 and 1,055 claims, $174,910 and $184,485, to the cent |
| Quest Diagnostics, Form 10-K for 2025 | Net revenues $11,035 million against $9,872 million, up 11.8 percent; revenue estimated including contractual allowances and patient price concessions (source and check date in the provenance) |
