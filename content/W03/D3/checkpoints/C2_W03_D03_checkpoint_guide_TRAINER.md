# The checkpoint guide: what on track sounds like, and the one nudge

**TRAINER ONLY.** It goes with `checkpoints/C2_W03_D03_checkpoint_questions_STUDENT.md`. The
checkpoint takes the first 30 minutes of the morning block. The plants and their numbers are in
`docs/detailing/W03_build1_spine.md`. Every number below was computed from the files in
`content/W03/D1/data/` the way a group would compute it (the identity rule applied to the old export
first), and matches the spine's witness wherever the spine gives one.

---

## How to run the thirty minutes

1. **Order.** Take groups by sub-problem, 1 to 5, so the three groups on one sub-problem answer back
   to back and the room hears one question answered three ways.
2. **Two minutes per group, by the clock.** One member per question, a different member each time.
   Stop the group at two minutes even mid-sentence, and write "unfinished" against the question it
   was on.
3. **Listen for three things only:** a number, the file it came from, and whether it was counted
   after an identity rule. Do not teach at the checkpoint. The nudge is one sentence, said once, and
   then the next group starts.
4. **Record** each group on one line: on track, slow, or stuck, plus the question it could not
   answer. The line feeds the catch-up plan (`checkpoints/C2_W03_D03_catchup_plan_TRAINER.md`) and
   the Academic TA's first round in the open build time.
5. **The minutes left after the last group** go to the stuck groups' blockers, one sentence each, so
   the TA knows where to sit first.

**Never, at the checkpoint:** confirm or deny a number against the spine's witness, name a plant,
or tell one group what another found. "That's a number worth checking a second way" is as close to
a verdict as you go.

**A group answering a stranger number than any listed below** has usually counted rows instead of
bookings or summed text as numbers. Ask for the row count and the distinct-id count, and move on.

---

## Sub-problem 1. Revenue

| Q | On track, the answer contains | The tell of a stuck group | The one nudge |
|---|---|---|---|
| 1. Profile | 11,356 invoice rows and 11,356 distinct numbers. `amount` fails to convert on 35 rows because of a thousands comma. Stronger groups add that `corporate_account` is filled on one row and that the largest amount is Rs 18,00,000. | A revenue total with no mention of conversion, or Rs 1,96,27,945, which is Rs 78,004 under the true Rs 1,97,05,949 because 35 amounts were coerced to blanks | "What does your code do with an amount it can't read, and how many did it do that to?" |
| 2. Reconcile | Invoices against completed bookings. The old export's 11,213 completed bookings, after the identity rule, leave 143 invoices unmatched, and those 143 carry the new system's booking ids. Across both exports, 11,356 completed bookings match 11,356 invoices one to one, and the cancelled ones carry none. | "Every invoice matched", said by a group that only read the old export, or 143 invoices written off as bad data | "Read the booking id of one invoice you couldn't match, aloud." |
| 3. Denominator | Mean invoice per invoice: 5,508 invoices in Q1 and 5,848 in Q2. The Q2 mean is Rs 1,904 against a median of Rs 1,499, and Rs 1,596 without the one corporate invoice. Stronger groups have seen that one invoice line can stand for many tests: 22,152 non-corporate invoice lines sit on bookings that carry 46,867 tests (48,235 counting cancelled bookings, the spine's figure). | "Revenue per test" computed as revenue over `line_items`, or a Q2 mean quoted alone | "Put the median beside your Q2 mean. What is pulling them a fifth apart?" |

## Sub-problem 2. Bookings

| Q | On track, the answer contains | The tell of a stuck group | The one nudge |
|---|---|---|---|
| 1. Profile | Two files. The old export has 11,729 rows and 11,549 distinct ids. The new system's export has 153 rows (Chennai 85, Pune 68), with its own ids, clinic codes and a day-first date format, starting 18/09/2026. | One file opened | "Your data team said two cities changed booking systems. Which file holds a booking made after the change?" |
| 2. Reconcile | Bookings against invoices by city and quarter. In Chennai and Pune, Q2 invoices (633 and 570) exceed the old export's completed Q2 bookings (554 and 506) by the new system's completed bookings (79 and 64). Every other city matches. | Bookings compared with nothing, or the mismatch explained as "invoices are wrong" | "Put your Q2 completed bookings beside Q2 invoices, city by city. Where do they part?" |
| 3. Denominator | Q1 1,415 bookings in the two cities. Q2 is 1,090 in the old export alone (down 23.0 percent) and 1,243 across both files (down 12.2 percent). The group says which file each count came from and that the old export was de-duplicated first. | The 23.0 percent fall stated as the finding, or 1,450 and 1,099 (rows, counted before the identity rule) | "Which bookings in those two cities would the old export not hold?" |

## Sub-problem 3. Billing

| Q | On track, the answer contains | The tell of a stuck group | The one nudge |
|---|---|---|---|
| 1. Profile | 11,289 payment rows. The reference takes three forms: 9,070 bare digits such as `000001`, 1,972 `INV-` followed by a number, and 247 full invoice numbers. 11,187 rows say success and 102 say refund. | "The references look like invoice numbers", with no counts by form | "Group the references by their first four characters and count each group." |
| 2. Reconcile | A first exact join matches 247 payments, 2.2 percent. After one rule maps every form to the invoice number, all 11,289 payments match, and 398 invoices have no payment, one of them the Rs 18,00,000 corporate invoice. | "Only 2 percent of invoices are paid", or a fuzzy match with no stated rule | "Put one invoice number beside a payment reference you believe belongs to it. What rule turns one into the other?" |
| 3. Denominator | Collected is success rows, less repeated posts, net of refunds. 229 success rows repeat a reference and an amount minutes apart (Rs 3,55,254). Refunds come to Rs 1,60,164. That leaves Rs 1,70,97,980 collected against Rs 1,97,05,949 invoiced, and the 398 unpaid invoices (Rs 24,47,805) plus the refunds account for the gap exactly. | The amount column summed as it stands (Rs 1,74,53,234), or double posts counted as money | "Group the payments by reference and amount. What does a count of two mean?" |

## Sub-problem 4. No-shows

| Q | On track, the answer contains | The tell of a stuck group | The one nudge |
|---|---|---|---|
| 1. Profile | 7,133 appointment rows over Q2, at the 12 walk-in clinics (the laboratories have none). Eleven clinics hold 614 to 681 rows each, and KH-HYD-03 holds 52. `kind` takes the values scheduled and walk-in, and `attended` takes Y and N. | A rate per clinic with no row counts beside it | "How many visits sit behind each clinic's rate?" |
| 2. Reconcile | Every clinic code in the file is a walk-in clinic in the clinics file. Clinic totals add to 7,133, which is 4,091 scheduled plus 3,042 walk-in. A group that tried to match appointments to bookings found the counts differ, and logged that as a question rather than a finding. | A mismatch against bookings treated as a defect in the data | "Which file tells you what a clinic is, and did every code in your file appear there?" |
| 3. Denominator | On all visits: 10 of 52 (19.2 percent) against 616 of 7,081 (8.7 percent). On scheduled visits only: 10 of 50 (20.0 percent) against 616 of 4,041 (15.2 percent). A group near the end adds that a base of 50 lets chance produce a gap this size about one time in five (0.22). | "Twice as bad", from 19.2 against 8.7 | "Which visits in your denominator could never have been a no-show?" |

## Sub-problem 5. The campaign

| Q | On track, the answer contains | The tell of a stuck group | The one nudge |
|---|---|---|---|
| 1. Profile | 2,381 patients offered, from 15 July to 4 August 2026. Bengaluru 619, Mumbai 607, Hyderabad 416, Delhi 316, Chennai 215, Pune 208. 948 took it up. | Take-up quoted with no city split | "Put offers per city beside patients per city." |
| 2. Reconcile | All 2,381 appear in the patients file, each in the same city. 1,716 of them have at least one booking in the old export. Patients with no booking at all are counted and set aside with a stated reason. | "We joined and it worked", with no counts | "How many offered patients have no booking at all, and did you count them in the denominator?" |
| 3. Denominator | Bookings per patient over a stated window (the spine's is 15 July to 14 September), offered against not offered. Overall, offered patients book 9.0 percent more. Within each of Bengaluru, Hyderabad and Mumbai they book less (down 10.8, 19.9 and 13.0 percent). Those three cities were already rising 6.9 percent before the offer. | 9 percent restated with no city split, or "the campaign worked" | "Run the same comparison inside one city." |

**The offer outside the three cities.** The campaign file also carries offers in Delhi, Chennai and
Pune, to a fifth of patients at random, against half in the campaign cities. In Delhi, offered
patients out-book the rest by 23.5 percent, a chance draw that a permutation test puts at p of about
0.03; Chennai shows minus 4.8 and Pune plus 0.6. A group that reads Delhi as proof the offer works has
met a false positive. Ask it whether the other two cities outside the campaign show the same gap. Do not
settle it at the checkpoint.

---

## What to write down, per group

```
Group   Sub-problem   Q1   Q2   Q3   Status (on track / slow / stuck)   Blocker, in its words
```

A group marked stuck on two or more of its three questions goes to the catch-up plan today.
