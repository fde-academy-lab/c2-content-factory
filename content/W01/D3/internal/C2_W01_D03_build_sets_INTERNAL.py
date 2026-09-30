"""Write Wednesday's six chapter sets and their solutions from one table of items.

Run from the repository root:
    python3 content/W01/D3/internal/C2_W01_D03_build_sets_INTERNAL.py

Each item carries its stem, four options, the key, why the key holds, why each other letter fails,
and its kind: "design" for the best-fit approach, a sizing, the fact that would switch it or the
second route, and "read" for reading a result or a trap. The script refuses to write a set whose
key is the longest option, which is the first thing scripts/distractor_audit.py checks.
"""
import pathlib

DAY = pathlib.Path("content/W01/D3/exercises")

SETS = [
    ("ch1_profile", "Chapter 1 set: what the ERP actually sent", "after chapter 1", [
        ("An analyst reads three amounts straight from a CSV, `[\"950\", \"18000\", \"4500\"]`, and calls `max()` "
         "on the list to name the largest order for Anand. Which order does the note name as the largest?",
         ["Rs 18,000, since max compares the numbers the text holds", "Rs 4,500, since max takes the middle value of three strings",
          "Rs 950, since text compares one character at a time", "None of them, since max raises an error on text"], "c",
         "Text compares character by character, and 9 sorts above 4 and 1, so `max` returns \"950\".",
         "a: nothing converts the text. b: max takes the largest, never the middle. d: max works on text, which is why the mistake is silent.", "read"),
        ("Two exports of the same quarter arrive, profiled the same way.\n\n| Export | Rows | Distinct order ids | Amounts that convert |\n|---|---|---|---|\n"
         "| North | 240 | 240 | 238 |\n| South | 240 | 221 | 240 |\n\nWhich export would you total first for Anand?",
         ["North, whose two failed amounts can be logged and read", "South, since every one of its amounts converts cleanly",
          "Neither, since both carry at least one field that fails", "Both at once, since the two profiles have equal row counts"], "a",
         "North's two failed amounts are known and countable; South has 19 rows beyond one per order, which inflates any total.",
         "b: converting cleanly says nothing about copies. c: a failure you can count is no reason to stop. d: equal row counts hide South's 19 extra rows.", "design"),
        ("Anand asks about this invented profile of an export.\n\n| Field | Present | Convertible | Distinct |\n|---|---|---|---|\n"
         "| order_id | 180 | text | 171 |\n| amount | 180 | 180 | 164 |\n| channel | 180 | text | 3 |\n| discount | 122 | 122 | 5 |\n\nWhich field could move his revenue figure?",
         ["discount, since a third of its values are missing", "channel, since three values cannot describe 180 orders",
          "amount, since 164 distinct values means some repeat", "order_id, since 180 rows hold 171 orders"], "d",
         "180 rows hold 171 orders, so 9 rows repeat an order and add rupees that were never earned.",
         "a: an optional discount does not move booked revenue. b: three channels is right for app, web and store. c: two orders can share an amount.", "read"),
        ("Anand asks, \"How many orders did the ERP send for the two quarters?\" Which count from the profile answers him?",
         ["Rows in the file", "Distinct order ids", "Amounts that convert", "Rows with a status present"], "b",
         "An order is its order id, so distinct ids count orders; rows count lines, which include the migration's copies.",
         "a: counts every copy as an order. c: counts readable amounts, which is a different question. d: counts rows whose fate is known.", "match"),
        ("A new export has 2 crore rows and Anand wants the reconciliation tomorrow. Which way of learning what arrived is the best fit?",
         ["Scroll the first thousand rows of it in a spreadsheet", "Total the amounts and compare with the books",
          "Sample 1,000 rows and tie each to the books", "Profile every field, then read the rows it flags"], "d",
         "A profile reads every value in minutes and turns each defect into a count; reading rows only where it points keeps the work small.",
         "a: the first thousand rows say nothing about the rest. b: a total cannot say why it differs. c: a sample of 1,000 has well under a one percent chance of meeting a single bad row.", "design"),
        ("A sample of 20 rows is drawn from a 200-row export that holds one unreadable amount. About how likely is the sample to contain it?",
         ["About 90 percent", "About 50 percent", "About 10 percent", "Certain, since 20 rows is enough"], "c",
         "Each row has the same chance to be drawn, so the one bad row is in the sample 20 times in 200, 10 percent.",
         "a and b: overstate what a small sample sees. d: nothing about 20 rows guarantees one particular row.", "design"),
    ]),
    ("ch2_repeats", "Chapter 2 set: the rows that repeat", "after chapter 2", [
        ("A colleague's dedupe of a 300-row export reports 0 duplicates, and a count of distinct order ids returns 284. Each row carries a load timestamp added by the pipeline. What happened?",
         ["Sixteen orders were lost in the load and need a resend", "The timestamp made every row unique, so no row matched",
          "The dedupe is right, and the id count is off by 16", "Sixteen rows carry blank order ids that the count skips"], "b",
         "A load timestamp differs on every row, so a whole-record key never matches; 300 rows against 284 ids says 16 rows repeat an order.",
         "a: nothing is lost, the rows are all present. c: the id count is the check. d: a blank id would lower the present count, which nobody reported.", "read"),
        ("Kalpa's ERP issues one order_id per order and never reuses it. Which key is the best fit for deduplicating Kalpa's orders?",
         ["customer_id and order_date together", "Every field, the load timestamp included",
          "order_id, the key the ERP issues", "Every field except the load timestamp"], "c",
         "The ERP's own key is the identity: one order, one id.",
         "a: two real orders on one day would merge. b: the timestamp makes every row unique. d: finds only exact copies and misses a copy that differs in one field.", "design"),
        ("An analyst dedupes Kalpa orders on customer_id and order_date. A loyal member places two real orders on the same day. What happens to revenue?",
         ["It falls, since one real order is set aside as a copy", "It stays right, since the key still finds true copies",
          "It rises, since the key keeps both orders and a copy", "It stays right, since two orders a day never happen"], "a",
         "The key merges the two real orders, and one is set aside as a copy, so revenue falls by its amount.",
         "b and d: the key is wrong for this business. c: a dedupe removes rows and never adds one.", "read"),
        ("An invented export holds 150 rows and 141 distinct order ids, and 148 of its amounts convert. How many rows sit beyond one per order?",
         ["2", "7", "11", "9"], "d",
         "Rows less distinct order ids: 150 minus 141 is 9. Convertible amounts are a separate count.",
         "a: 150 less 148 is the failed amounts. b: 9 less 2 mixes the two counts. c: 9 plus 2 adds them.", "predict"),
        ("Kalpa's app and its stores each number customers from C-1 upwards, and Meera wants one customer table. Which identity rule is the best fit?",
         ["The customer id, since each system issues one per person", "Every field, since only an exact copy is safe to merge",
          "Cleaned phone and email, doubtful pairs reviewed", "The customer's name, since it appears in both systems"], "c",
         "Neither id identifies a person across both systems, so the match rests on contact fields cleaned the same way, with a person reviewing the doubtful pairs.",
         "a: C-1 in the app and C-1 in a store are different people. b: two systems never write a person identically. d: names repeat and are spelled many ways.", "design"),
        ("A fuzzy key with no blocking compares every row with every other. About how many comparisons does it make on 10,000 rows?",
         ["About 10,000", "About 1 lakh", "About 100 crore", "About 5 crore"], "d",
         "10,000 times 9,999 over 2 is 49,995,000, about 5 crore, which is why fuzzy matching is blocked by a field such as city first.",
         "a: that is one lookup per row, a key's cost. b: far too few pairs. c: 100 crore is ten times every row against every row, not half of it.", "design"),
    ]),
    ("ch3_survivor", "Chapter 3 set: the copy that stays", "after chapter 3", [
        ("Two rows share order_id KR-90012. The first reads amount `--` and the second reads `1900`, and every other field matches. Which row stays in the clean file?",
         ["The first, since the first extract is the original", "Both, until Finance chooses between them",
          "Neither, since the pair contradicts itself", "The second, since its amount converts"], "d",
         "The copy whose amount converts carries the order's value; keeping the first would keep one that cannot be summed.",
         "a: first is no reason when the first is broken. b: Finance booked one order, not a choice. c: throwing both away loses Rs 1,900 of booked revenue.", "design"),
        ("Two rows share order_id KR-90047. Both amounts convert to Rs 3,100; one is dated 21 August and the other 30 July. Which decision goes in the log?",
         ["Keep the first extract's row and ask the ERP team", "Drop both rows, since the order cannot be dated",
          "Keep both rows, since the dates make them two orders", "Keep the later date, since later loads are corrections"], "a",
         "Both copies are valid and disagree on one field; no rule inside the file can say which date is true, so keep the first extract and log the question.",
         "b: the order happened and is booked. c: one id is one order. d: later is a correction only if the ERP team says so.", "read"),
        ("Twenty rows are set aside as copies. Two of them are Business orders carrying Rs 9,00,000 of the Rs 9,30,000 set aside, and eighteen are Retail-Plus orders. Which conversation needs the two Business rows first?",
         ["Marketing's, since Retail-Plus is the segment they own", "Anand's, since those two rows carry most of the rupees",
          "The auditor's, since most of the rows are Retail-Plus", "Nobody's, since rows are rows and all twenty go together"], "b",
         "Two rows carry about 97 percent of the rupees, which is Anand's gap.",
         "a: the Retail-Plus rows matter to Tuesday's finding, a second conversation. c: the auditor wants every row, rupees first. d: counting rows hides where the money sits.", "read"),
        ("An export holds 40 repeated orders: 38 pairs are identical, one pair's first copy has an unreadable amount and a Rs 2,600 twin, and one pair differs only on the date. What does keeping the first copy cost against the books?",
         ["Rs 0", "Rs 5,200", "Rs 2,600", "40 orders"], "c",
         "Only the unreadable-first pair moves rupees: the first copy cannot be summed, so its Rs 2,600 twin is lost.",
         "a: misses the unreadable copy. b: counts the loss twice. d: the pairs are copies, so no order is lost by keeping one row.", "design"),
        ("Keeping the last copy lands Q1 on the books, and so does keeping the copy that validates. Which fact would make the last copy the right rule?",
         ["The last copy's rows sit at the end of the file", "Q1 ties to the books under the last-copy rule",
          "The ERP team says the second extract was a fix", "Most pairs in the file are identical copies"], "c",
         "A rule is right for a reason about the source; a corrected re-run is that reason.",
         "a: file position is where rows sit, not which is true. b: a tie can come from luck, as it does here. d: identical pairs give no reason to prefer either copy.", "design"),
    ]),
    ("ch4_missing", "Chapter 4 set: what is missing or malformed", "after chapter 4", [
        ("An order in Q2 has no status and a valid amount. Revenue is booked value, and Operations also reads the delivered share. Which decision keeps both numbers honest?",
         ["Drop the order, since its fate is unknown", "Default the status to delivered, the usual case",
          "Keep the order and flag the status as unknown", "Default the status to cancelled, the safe case"], "c",
         "Revenue stays whole and the order stays out of every count that needs its status.",
         "a: removes a booked order. b and d: invent a fact nobody recorded.", "design"),
        ("A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted amounts start `0, 0, 0, 410, 460`. What most likely happened?",
         ["Three amounts failed and a helper turned each into 0", "Three customers placed free orders in a promotion",
          "Three orders were cancelled, and cancelled orders carry 0", "The profile is right, and zero is a valid Kalpa order"], "a",
         "No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the fingerprint of a coercing helper.",
         "b: a free order would still carry a line and a reason. c: the files book cancelled orders at their value. d: zero is a claim the profile cannot support.", "read"),
        ("A colleague converts amounts with `int(v) if v.isdigit() else 0`. On an invented export, an amount written `1,150` with a thousands separator comes out as Rs 0. Which change fixes the logic?",
         ["Keep the isdigit test and footnote the order", "Replace the 0 with the segment's median amount",
          "Wrap int() in try and return 0 on any failure", "Try int(); log the value and its reason"], "d",
         "isdigit rejects the comma, and the else branch invents a zero; trying the conversion logs the value and its reason, so the order can be repaired by a stated rule instead of sold for nothing.",
         "a: the order is still recorded as Rs 0. b: invents an amount. c: still turns a failure into a zero, just more quietly.", "fix the logic"),
        ("An amount in the CSV reads `fourteen`. The JSON feed, cut from the same extract, reads `fourteen` for that order too. Which is the best fit for the log?",
         ["Repair it from the feed, since a second source agrees", "Reject it to the log and ask the ERP team",
          "Read the word as Rs 14, since the text says fourteen", "Coerce it to zero so the pass can finish tonight"], "b",
         "A copy of the same extract repeats the defect and is no witness, so the order is rejected with its reason until an independent source supplies the value.",
         "a: the feed copied the error. c: a word is not an amount, and Rs 14 is far below any Kalpa order. d: a zero is a false value that hides the defect.", "design"),
        ("Forty of 100 orders carry no discount, and the 60 that carry one average Rs 90. What does the average read if the blanks are taken as zero?",
         ["Rs 90", "Rs 72", "Rs 36", "Rs 54"], "d",
         "60 orders times Rs 90 is Rs 5,400, spread over 100 orders, Rs 54.",
         "a: the blanks were ignored. b: halves the gap. c: divides by the wrong count.", "predict"),
    ]),
    ("ch5_bridge", "Chapter 5 set: the bridge to the books", "after chapter 5", [
        ("The largest Q2 order is 1.8 times the next, placed by a Business account that ordered in both quarters, with every field valid. What goes in the note to Anand?",
         ["Remove it, since an order that size distorts the quarter", "Cap it at the next largest order, to keep the shape",
          "Keep it, flag it, and show Q2 with and without it", "Move it to Q1, since the account ordered there too"], "c",
         "Nothing about the record is wrong, so it is revenue; showing both readings lets the reader see how much one order carries.",
         "a: size is not a defect. b: invents a smaller order. d: moves revenue between quarters.", "design"),
        ("Q1 as exported is Rs 3,40,00,000. The rows set aside by the identity rule carry Rs 30,00,000. The books say Rs 3,10,00,000. Which statement does the bridge support?",
         ["The export is right, and the books missed Rs 30 lakh", "The books are right, and copies explain the whole gap",
          "Neither is right until every row is re-entered by hand", "The gap is too large for copies, so look for a date error"], "b",
         "3,40,00,000 less 30,00,000 is 3,10,00,000, the books exactly.",
         "a: reverses the finding. c: the bridge already closes. d: the copies close the whole gap.", "read"),
        ("Tuesday's report said a segment's orders per customer fell 40 percent. On clean data the fall is 25 percent. What leads the note?",
         ["The 40 percent, since leadership has seen it", "Both, in a footnote, since the story is the same",
          "Nothing, until Thursday proves the fall is real", "The smaller number, and why it changed"], "d",
         "A finding that shrank, reported first and with its reason, keeps the stakeholder's trust.",
         "a: repeats a number known to be wrong. b: buries the change. c: the clean number is ready today; Thursday tests whether it is real.", "read"),
        ("A fence at three times the median would remove one Q2 order, turning a 2 percent dip into a 15 percent fall. Which reading goes to Marketing?",
         ["The 2 percent dip, with the order checked and flagged", "The 15 percent fall, since the fence is a standard rule",
          "Both readings, with the 15 percent one first", "The 15 percent fall, with the order named in a footnote"], "a",
         "The order is real, so the quarter is a 2 percent dip; the flag and the check say so in writing.",
         "b, c and d: each leads with a fall invented by removing real revenue.", "read"),
        ("A second export from the app holds 60 percent of Q1's orders and was cut from the same extract as the CSV. Which proof is the best fit for Anand?",
         ["Rebuild Q1 from the app export and compare totals", "Take Finance's figure, since the books are audited",
          "A bridge to the books, move by move", "Average the two exports' totals and report that"], "c",
         "A bridge closes to the rupee and each move is backed by logged rows; a partial export cut from the same extract is neither complete nor independent.",
         "a: 60 percent coverage cannot rebuild a quarter, and it shares the CSV's defects. b: adopts a number without saying why the dashboard differs. d: averaging two wrong totals gives a third.", "design"),
    ]),
    ("ch6_audit", "Chapter 6 set: the log the analyst audits", "after chapter 6", [
        ("A pass reports 500 rows in, 470 kept and 30 set aside, and Q1 comes out Rs 2,100 below the books' Rs 3,20,00,000. What do you do next?",
         ["Ship it, since the rows reconcile and the gap rounds away", "Add Rs 2,100 as an adjustment line so the rupees tie",
          "Find the set-aside row whose rupees a kept twin lacks", "Ask Finance whether their books are Rs 2,100 too high"], "c",
         "A row reconciliation proves no row vanished, not that the right rows stayed; the missing rupees sit in a set-aside row whose kept twin lacks them.",
         "a: rounding is where the gap hides. b: an adjustment line hides the cause. d: the books are the reference until a row proves otherwise.", "read"),
        ("Q1 as exported is Rs 50,00,000, the rows set aside carry Rs 4,20,000, and the books say Rs 45,80,000. Does the rupee reconciliation hold, and what does it prove?",
         ["Yes, and the clean total equals the books", "No, since Rs 4,20,000 is more than 8 percent of Q1",
          "Yes, and it proves no row vanished from the file", "No, since the rows have not been counted yet"], "a",
         "50,00,000 less 4,20,000 is 45,80,000, which equals the books, so the rupees reconcile.",
         "b: the size of a move is not a test. c: that is what the row reconciliation proves. d: the rupee check stands on its own.", "read"),
        ("Put the pass in order for Anand's analyst: 1 apply the identity rule, 2 reconcile rupees to the books, 3 test which amounts convert and log the failures, 4 reconcile rows. Which order holds?",
         ["1, 3, 4, 2", "3, 1, 4, 2", "1, 4, 3, 2", "3, 4, 1, 2"], "b",
         "Test the amounts first so the rule can see which copy validates, then the rule, then rows, then rupees to the books.",
         "a and c: running the rule before converting keeps the first copy even when it is unreadable. d: reconciling rows before the rule has nothing to reconcile.", "design"),
        ("Anand's analyst has an evening to check the pass. Which hand-over is the best fit?",
         ["The clean file alone, 186 rows to compare by hand", "A full diff of the raw and clean files, 201 lines",
          "The clean file and a line saying 15 rows set aside", "The logs, the decisions and both totals"], "d",
         "About 23 lines tie both totals and let her replay the pass; the other hand-overs either take hours or prove only the rows.",
         "a: no reasons and hours of comparison. b: shows what went, never why. c: ties the rows and nothing else.", "design"),
        ("How do you prove a log is complete without trusting the code that wrote it?",
         ["Count the log's lines and compare with the rows removed", "Read every line of the log and check each reason",
          "Rebuild the clean file from the raw export and the log", "Rerun the pass and compare the two logs line by line"], "c",
         "The replay is independent of the pass: if the raw export less the logged lines equals the clean file, nothing went unlogged.",
         "a: counts can match while the rows differ. b: proves reasons exist, not that every removal is listed. d: the same code reproduces the same mistakes.", "design"),
    ]),
]


def longest_ok(opts, key):
    k = "abcd".index(key)
    return len(opts[k]) < max(len(o) for i, o in enumerate(opts) if i != k) or \
        sum(1 for o in opts if len(o) == len(opts[k])) > 1


def write():
    for name, title, when, items in SETS:
        design = sum(1 for it in items if it[5] == "design")
        stu = [f"# {title}", "",
               f"{len(items)} items, about {3 * len(items)} minutes, {when}. Every number here is invented unless it says it is "
               "from today's file; the reasoning is the one you ran on Kalpa's export. Items marked Design ask for the best-fit "
               "approach, a sizing or the fact that would change it.", "",
               f"Post one line, {len(items)} letters in item order, no spaces:", "", "```",
               "Post exactly this shape: " + "x" * len(items), "```", "", "---"]
        sol = [f"# Solution: {title[0].lower() + title[1:]}", "",
               "Answers: " + " ".join(f"{i + 1}{it[2]}" for i, it in enumerate(items)), "",
               f"{design} of {len(items)} items are design items.", "", "## Item by item", "",
               "| Item | Key | Kind | Why it holds | Why the others fail |", "|---|---|---|---|---|"]
        for i, (stem, opts, key, why, others, kind) in enumerate(items):
            assert longest_ok(opts, key), (name, i + 1)
            stu += ["", f"### Q{i + 1}" + (" (Design)" if kind == "design" else ""), "", stem, ""]
            stu += [f"{l}) {o}" for l, o in zip("abcd", opts)]
            sol.append(f"| {i + 1} | {key} | {kind} | {why} | {others} |")
        (DAY / "unguided" / f"C2_W01_D03_{name}_STUDENT.md").write_text("\n".join(stu) + "\n", encoding="utf-8")
        (DAY / "solutions" / f"C2_W01_D03_{name}_solution_STUDENT.md").write_text("\n".join(sol) + "\n", encoding="utf-8")
        print("wrote", name, len(items), "items,", design, "design")


if __name__ == "__main__":
    write()
