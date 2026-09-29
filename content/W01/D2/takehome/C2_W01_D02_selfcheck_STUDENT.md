# Self-check: know you are right before anybody reads it

Every checkpoint is something you can verify alone, in the order the ladder runs. If one fails, the
fix is named beside it. Read this after your notebook runs, never before, because the order in which
you meet these numbers is the investigation.

---

## Part 1, the numbers

| # | Rung | Checkpoint | What you should see | If it does not match |
|---|---|---|---|---|
| 1 | Load | The file loaded | 169 orders | The loader still names the class file; change the file name in the setup cell |
| 2 | 1 | Q1's window | First order 1 April, last order 28 June | Sort the dates as text in the form the file gives them; they sort correctly as written |
| 3 | 1 | Q2's window | First order 4 July; your last date is the final entry when every Q2 date is sorted, and it is the date checkpoint 5 counts to | Same fix as checkpoint 2 |
| 4 | 1 | The headline change on totals | Rs 2,05,00,000 to Rs 1,94,00,000, down 5.4 percent | 5.7 percent means you measured against Q2 |
| 5 | 1 | Weeks covered | 13 in Q1; in Q2, the weeks from 1 July to the last date you printed at checkpoint 3 | Count to the last date the file reaches, never to a date it does not |
| 6 | 1 | Revenue per week | Rs 15,76,923 in Q1; your Q2 rate times your checkpoint 5 weeks gives back Rs 1,94,00,000 | A rate that gives back Rs 1,94,00,000 only when multiplied by a different count of weeks was divided by the wrong weeks |
| 7 | 2 | Orders and customers | 90 orders and 62 customers in Q1; 79 orders and 54 customers in Q2 | 90 and 79 customers means you counted rows; count each id once |
| 8 | 2 | Orders per customer | 1.45 in Q1 and 1.46 in Q2 | 0.69 is the rate upside down |
| 9 | 2 | Revenue per order | Rs 2,27,778 in Q1 and Rs 2,45,570 in Q2 | Check that the revenue and the orders come from the same quarter |
| 10 | 3 | Segments in and rows out | 4 segments in each quarter, 4 rows out | Fewer rows means a function returned None for a segment |
| 11 | 3 | Retail-Core | 37 orders, 34 customers, Rs 60,700 in Q1; 26 orders, 26 customers, Rs 47,900 in Q2 | Filter on the exact segment name as the file writes it |
| 12 | 3 | Retail-Plus | 30 orders, 15 customers, Rs 89,750 in Q1; 30 orders, 15 customers, Rs 87,210 in Q2 | As checkpoint 11 |
| 13 | 3 | Business | 17 orders, 11 customers, Rs 2,03,44,010 in Q1; 17 orders, 11 customers, Rs 1,92,59,000 in Q2 | As checkpoint 11 |
| 14 | 3 | Student | 6 orders, 2 customers, Rs 5,540 in Q1; 6 orders, 2 customers, Rs 5,890 in Q2 | As checkpoint 11 |
| 15 | 3 | Retail-Core's customer ids | Q1's 34 ids, less those missing from Q2, plus those new in Q2, give Q2's 26 | A sum that misses 26 means you compared ids across segments; keep both sets inside Retail-Core |
| 16 | 3 | Retail-Core per week | 2.85 orders a week in Q1, 37 over 13; in Q2, 26 orders over your checkpoint 5 weeks | Divide Q2 by the weeks the export covers |
| 17 | Missing | Orders without a discount field | Your blanks plus the orders that carry the field give 90 in Q1 and 79 in Q2 | Test whether the key is in the record; a zero in the field is a recorded value |

When all seventeen match, read your memo's first line again with checkpoints 5 and 6 beside it.

---

## Part 2, the memo

Read your page back and answer each question yes or no. Two noes means rewrite it.

1. Does the first line carry the window and the definition, and does it rest on a matched
   comparison rather than the two totals as they stand?
2. Does the branch line give both quarters' numbers, and could Anand find each one in a cell?
3. Does the segment line say what happened to the customers themselves, from the ids, and not only
   to the counts?
4. Is each cause written as a hypothesis, with a named piece of data that would settle it?
5. Does the final line pick one of the three answers and point at the number that decides it?
6. Would the memo still read correctly if the export covered a different stretch of each quarter? If
   not, does it say which number would change?

---

## Part 3, the reading and the video

Brit Institute, data analyst case study questions, including "Sales dropped last month. How would you investigate?": https://britinstitute.uk/blog/data-analyst-case-study-interview-questions (verified 29 Sep 2026)

Corey Schafer, "Python Tutorial for Beginners 8: Functions": https://www.youtube.com/watch?v=9Os0o3wzS_I (verified 29 Sep 2026)

Your line on the walkthrough names one specific step, in the walkthrough's own words, and says
whether your ladder took it. If the line could have been written without opening the page, it is not
yet the line. After the video, every function in your notebook ends in `return`; search the notebook
for `def` and check each one.
