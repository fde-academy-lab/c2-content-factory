# Run sheet: the parallel build, Week 3 Wednesday

**TRAINER ONLY.** Sixty minutes, straight after the checkpoint. The notebook is
`parallel-build/C2_W03_D03_delhi_revenue_tree_STUDENT.ipynb`. It ships executed, and every number
below is one of its saved outputs.

---

## The slice, in one line

Sub-problem 1's revenue tree for Delhi only, Q1 (April to June) against Q2 (July to September). It
reads the old booking export and the invoices from `content/W03/D1/data/` and stops at the leaves an
invoice carries: how many invoices were raised, and what each was worth on average.

| Start from | Go as far as | Stop before |
|---|---|---|
| The checkpoint's last answer, and the room's own mess from Monday | One claim with its denominators and caveat, and a four-row decisions log | Anything below the invoice: what an invoice holds, channels, tests, payments |

---

## Before the room arrives

1. Open the Codespace, open the notebook, and run it once from the top. It needs under a minute. If
   a cell fails, the executed copy on GitHub carries every output, so teach from that.
2. Clear the board, then draw the empty tree in the first minute of the session, not before.
3. Keep the decisions log open beside the notebook as a blank table with the Week 1 Wednesday
   columns: Field, Issue, Rows, Decision, Reason.
4. Zoom the editor so the back row reads a table cell.

---

## The sixty minutes

| Step | Min | Say | Type or run | Draw | Ask the room before it shows |
|---|---|---|---|---|---|
| 0. The ask | 5 | "Each group holds one of Dr Menon's five branches. I'm taking a smaller question that no brief asks on its own: Delhi's revenue, Q1 against Q2. Watch the moves, not the numbers. Delhi's numbers answer none of your briefs." | Nothing yet | The tree: Revenue, then invoices times mean invoice, then invoices as bookings minus cancelled | "Before I open a file, what would I need to trust each leaf?" Take two answers; one should be "the count is real". |
| 1. Profile and the identity rule | 12 | "Rows first, then distinct ids, then blanks. I don't clean anything I haven't counted." | Setup cell, MAP, the profile cell | Beside the tree: 2,128 rows, 2,095 ids | The predict on level 1. Take a show of hands for a to d. The answer is b. |
| | | "Count rows per quarter and call them bookings, and Delhi grew 4.8 percent. Count bookings and it grew 6.8. Which would you send?" | The trap cell and the columns chart | Two bars, 4.8 and 6.8 | "Where are the extra rows, Q1 or Q2?" (26 in Q1, 7 in Q2.) |
| | | "One booking id is one booking. Where two rows share an id I keep the later `updated_at`. Why the export repeats a booking is a question for the data team, so it goes in the challenges log and my rule doesn't wait for the answer." | The identity rule cell and its checks | Write the first decisions log row | None. Write the row live, reason included. |
| 2. Amounts | 10 | "The amount column is text. There's a quick fix that never complains." | MAP, the coerce cell | Nothing | The predict on level 2. The answer is c. |
| | | "Four amounts have a thousands comma. Coerce blanked them, and revenue is Rs 6,048 short with no error on the screen. That is the number the finance head would not be able to match." | The fix and its checks | Second log row | "What check would have caught it before any total?" (Count the blanks after converting.) |
| 3. Reconcile | 13 | "Two files describe the same bookings. I prove that in both directions and on its grain." | MAP, the fanned join | Nothing | The predict on level 3. The answer is c: 2,065 rows. |
| | | "The raw join says Rs 32,43,653. The invoices say Rs 31,96,230. Rs 47,423 came from nowhere. That is the Week 2 fan-out." | The `validate` cell, then the reconciliation table and bridge | On the board: 2,128 = 2,095 + 33, then 2,095 = 2,032 + 63, then 2,032 = 2,032 | "Which side would you check first if these did not match?" |
| 4. The tree | 12 | "Now, and only now, the tree." | MAP, the tree table and driver tree | Fill the drawn tree with the numbers | The predict on level 4. The answer is a. |
| | | "78 more invoices at Q1's mean add Rs 1,24,262. A lower mean across Q2 takes Rs 40,942 away. Together they make Rs 83,320, which is the change." | The bridge and its checks | Two arrows on the tree, one up, one down | None |
| | | "8.0 percent more invoices, but Q2 is a day longer. Per day it's 6.8 percent, and revenue per day 4.2." | The per-day cell | Write 91 and 92 beside Q1 and Q2 | "Where else in your own cut are the windows unequal?" |
| | | "Clinic is on every booking, so I split by clinic. That's where I stop. What an invoice holds is the next branch, and I don't open it." | The clinic cell | A dashed box under the mean invoice | None. The dashed box is the point. |
| 5. The claim | 8 | Read the claim table aloud, claim first, then the caveat on its own line. | The decisions log cell, the interview section | Circle the two denominators in the claim on the board | "What is my caveat, in your words?" Take one answer, then hand over. |

**The hand-over line, word for word.** "That's one city and one branch, stopped at the invoice. Your
cut is bigger and messier. Run the same moves on it: profile, identity rule, convert, reconcile both
ways, the tree, the claim. Bring me your claim at the close."

---

## The plants this slice touches, and how to hold each

The plant table is in `docs/detailing/W03_build1_spine.md`. The slice runs next to five of them.
Never name a plant, never quote a whole-file count, and never compare Delhi with another city.

| Plant | Where the slice touches it | What you do | What you never say |
|---|---|---|---|
| The old export repeats rows (sub-problem 2, and everyone's profile) | 33 repeated Delhi ids, 26 in Q1 | Show the identity rule and log the cause as a question for the data team. That is the habit: a count that does not reconcile becomes a question, not a story. | "Re-export", "mid-quarter", the file's 180, or any hint that it bears on the two cities |
| A package is one invoice line (sub-problem 1 and the headline) | The mean invoice leaf | Stop the tree at "What an invoice holds" and never open `line_items` or `booking_tests`. If asked what an invoice holds: "That's the next branch. Which file would tell you?" | Tests per invoice, the package names, anything about how the dashboard counts |
| The free home-collection offer (sub-problem 5) | Delhi's patients were offered it too (316 in the campaign file). Home-collection invoices rise from 97 to 160 and their mean falls from Rs 1,670 to Rs 1,516, which is part of why Delhi's mean falls. The rest of Delhi's invoices also fall, from Rs 1,585 to Rs 1,561. | Never split by channel. If asked why the mean fell: "The invoice can't tell us. It's logged as a question for the next branch." If someone proposes a channel split live: "Good next cut. It's yours, not mine." | Channel, the campaign, the waived fee |
| The corporate contract (sub-problem 1) | Absent from Delhi | Profile Delhi rows only, as the notebook does, and never profile the invoice file whole | "Is Delhi typical?" gets "That's what your tree across cities will tell you." |
| Dr Menon's 5 percent (the headline) | Delhi's revenue happens to rise 5.4 percent | If anyone links the two: "Different count. Hers is her dashboard's. Ask what it counts." | That the dashboard counts old-system bookings or tests |

The payment feed (sub-problem 3), the booking-system switch (sub-problem 2) and the no-show clinic
(sub-problem 4) are untouched. If someone asks why the notebook reads only the old export: "Delhi's
rows are all in it. Check which file holds your city's rows." The data team already told the room
that two cities changed systems, so this line gives nothing away.

---

## When it goes wrong

| What happens | What you do |
|---|---|
| The Codespace will not start, or a cell errors | Switch to the executed notebook on GitHub. Every output is saved, so teach from the page and let the room read the checks. |
| `FileNotFoundError` on the data | The notebook must run from `parallel-build/`, reading `../../D1/data/`. Pull the branch that carries Monday's data folder, or run from GitHub as above. Give it two minutes, no more. |
| You reach minute 45 with step 4 not started | Cut the clinic split first, then the per-day table. Never cut the reconciliation, the claim or the caveat. |
| A group says "we already did all this" | Ask for their reconciliation in one line of arithmetic, input equals kept plus set aside. If they have it, they go back to building and skip the rest of the demo. |
| A learner wants to clean the blank channels | Point at the log's kept row: the tree doesn't use channel, so leaving the blanks is a decision and it has a reason. |
| A learner asks for the cells to copy | The notebook is in the repository. Tell them the cells answer Delhi, and their brief asks something else, so what carries over is the order of the moves. |
| Someone asks a question that would open a plant | Log it on the board as a question, say "your group's to answer", and go on. Modelling the question is the lesson; answering it spends another group's. |

---

## The numbers, with their source

Every number is a saved output of the notebook, computed from the files in `content/W03/D1/data/`.

| Number | Value |
|---|---|
| Delhi rows in the old export, distinct booking ids | 2,128 and 2,095, so 33 repeated ids (26 identical, 7 differing only in `updated_at`) |
| Rows per quarter against bookings per quarter | 1,039 to 1,089 (plus 4.8 percent) against 1,013 to 1,082 (plus 6.8 percent) |
| Comma-written amounts, and what coerce hides | 4 amounts, Rs 4,098 in Q1 and Rs 1,950 in Q2, Rs 6,048 in all |
| The fanned join | 2,065 rows and Rs 32,43,653, against 2,032 invoices and Rs 31,96,230 (Rs 47,423 too much) |
| Kept, cancelled, completed, invoiced | 2,095, 63, 2,032, 2,032 |
| Revenue Q1 to Q2 | Rs 15,56,455 to Rs 16,39,775, plus 5.4 percent |
| Invoices, mean, median | 977 to 1,055 (plus 8.0 percent); Rs 1,593 to Rs 1,554 (minus 2.4); Rs 1,499 to Rs 1,400 |
| The bridge | plus Rs 1,24,262 for volume, minus Rs 40,942 for the mean, Rs 83,320 in all |
| Per day, over 91 and 92 days | invoices plus 6.8 percent, revenue plus 4.2 percent |
| By clinic, invoices Q1 to Q2 | KH-DEL-01 328 to 319, KH-DEL-02 296 to 365, KH-DEL-03 353 to 371 |
