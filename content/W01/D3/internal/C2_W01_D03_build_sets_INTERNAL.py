"""Write Wednesday's six chapter sets and their solutions from one table of items.

Run from the repository root:
    python3 content/W01/D3/internal/C2_W01_D03_build_sets_INTERNAL.py

Each item carries its stem, four options, the key, why the key holds, why each other letter fails,
and its kind. "design" is kept for items that pass the house test: the learner combines two ideas or
takes several dependent steps, such as the best-fit approach with a sizing the learner computes, the
fact that would switch it, or the second route, and nothing else in the pack answers it. "read" is
reading a result or a trap, "predict" is arithmetic on an exhibit, and "fix the logic" repairs code.

The script refuses to write a set whose key is the lone longest or the lone shortest option, so
length points neither way, and a set whose keys pile onto one position.
"""
import collections
import pathlib

DAY = pathlib.Path("content/W01/D3/exercises")

GLOSS = {
    "ch1_profile": "The ERP is the enterprise resource planning system Finance books orders in, and its "
                   "export is the file chapter 1 profiled. ",
    "ch3_survivor": "An extract is one pull of rows out of the ERP, the enterprise resource planning system "
                    "Finance books orders in. ",
}

SETS = [
    ("ch1_profile", "Chapter 1 set: what the ERP actually sent", "after chapter 1", [
        ("A colleague's note to Anand names Rs 980 as the largest Q2 order in a new export, found by calling "
         "`max()` on the amounts as the CSV gave them. The same export's profile shows 21 Business orders, the "
         "smallest of them Rs 2,10,000. What do you tell the colleague before the note goes?",
         ["Send it, since max() looked at every Q2 amount the file holds",
          "Send it, adding that Business orders are counted apart",
          "Hold it: no largest order sits below every Business order",
          "Hold it until the ERP team confirms Rs 980 is the true value"], "c",
         "A Q2 order at Rs 980 cannot be the largest when 21 Business orders start at Rs 2,10,000; `max()` compared "
         "the amounts as text, where 9 beats 2, so the note names a small order and the audit skips the money.",
         "a: max() ranked the amounts by spelling, so reading every one did not help. b: the Business orders are Q2 "
         "orders in the same file, so the note still names the wrong one. d: the ERP holds the right value, and the "
         "fault is in how the colleague compared it.", "read"),
        ("A new export of 1.2 crore rows and 12 fields lands, and Anand's analyst starts work in 45 minutes. The "
         "team's profile reads about 20 lakh values a minute. Which plan fits the 45 minutes?",
         ["Profile all 12 fields, then read the rows the profile flags",
          "Profile order_id and amount, then read the rows they flag",
          "Tie out a random sample of 10,000 rows against the books",
          "Total every amount, then set the total beside the books"], "b",
         "All 12 fields are 14.4 crore values, 72 minutes at 20 lakh a minute, past the deadline; order_id and amount "
         "are 2.4 crore values, 12 minutes, which leaves half an hour to read what they flag. The key and the money "
         "fields are where a repeat or an unreadable amount would move Anand's figure.",
         "a: 72 minutes, so the analyst starts with nothing. c: reads under a tenth of a percent of the rows and says "
         "nothing about the rest. d: a total cannot say why it differs from the books.", "design"),
        ("An invented export holds 250 rows, 238 distinct order ids and 247 amounts that convert. How many rows "
         "could inflate revenue as copies, and how many amounts sit outside every total until someone reads them?",
         ["12 copies and 3 unreadable amounts", "3 copies and 12 unreadable amounts",
          "15 copies and no unreadable amounts", "9 copies and 3 unreadable amounts"], "a",
         "250 rows less 238 ids is 12 rows beyond one per order; 250 less 247 is 3 amounts that do not convert.",
         "b: swaps the two counts. c: adds them into one. d: takes the 3 failures out of the 12, as if every "
         "failure were a copy.", "predict"),
        ("Next quarter's export will hold 4 crore rows. A Python set of order ids takes about 100 bytes an id, and "
         "the laptop the team leaves running overnight has 2 GB free. Which route counts the distinct order ids?",
         ["A set of every id, then its length, as chapter 1 did",
          "A Counter over every id, which also keeps how often each appears",
          "A set of the first crore ids, with the answer times four",
          "Sort the ids on disk, then count each change from the last"], "d",
         "4 crore ids at 100 bytes each is about 4 GB, twice the memory free, so any route that holds every id at "
         "once stops part way; a sort can run on disk and has to remember only the id before.",
         "a: needs about 4 GB. b: needs at least as much as a set, since it keeps a count beside every id. c: "
         "scales a count that does not scale, since repeated ids can sit anywhere in the file.", "design"),
    ]),
    ("ch2_repeats", "Chapter 2 set: the rows that repeat", "after chapter 2", [
        ("A colleague's dedupe of a 300-row export reports 0 duplicates, and a count of distinct order ids returns "
         "284. The pipeline stamps every row with the time it was loaded. What happened?",
         ["The load stamp differs on every row, so no two rows matched",
          "16 orders were lost in the load, and the ERP team must resend",
          "The dedupe is right, and the id count is off by 16 somewhere",
          "16 rows carry a blank order_id, so the id count falls short"], "a",
         "A load stamp differs on every row, so a whole-record key never matches; 300 rows against 284 ids says 16 "
         "rows repeat an order.",
         "b: all 300 rows are present, so nothing was lost. c: the id count is the check, and it disagrees with the "
         "dedupe. d: blank ids would show in the profile as order_id present on fewer than 300 rows, and the dedupe "
         "would still match nothing.", "read"),
        ("Meera wants one customer table from the app's 30,000 records and the stores' 30,000, each system numbering "
         "customers from C-1, spread evenly over 6 cities. The team's machine compares about 50 lakh pairs a minute, "
         "and the job must finish inside 2 hours. Which match fits?",
         ["Each system's own customer id, one lookup a record",
          "Cleaned phone and email, every record against every other",
          "Cleaned phone and email, compared within each city",
          "Every field matching exactly, name and address too"], "c",
         "Neither id names one person across both systems, so the match rests on contact fields cleaned the same way. "
         "Every record against every other is 60,000 x 59,999 / 2, about 180 crore pairs, 360 minutes at 50 lakh a "
         "minute; within 6 cities of 10,000 it is about 30 crore pairs, 60 minutes, inside the window, with doubtful "
         "pairs sent to a person.",
         "a: C-1 in the app and C-1 in a store are different people. b: the right fields, and 6 hours, three times the "
         "window. d: two systems rarely write one person's record identically, so real matches are missed.", "design"),
        ("On an invented export the order_id key flags 22 rows as copies, and a fuzzy match on customer and amount "
         "within 60 days also flags 22. The reviewer is about to sign off because the counts agree. Which check does "
         "the reviewer still owe Anand?",
         ["Compare the two keys' counts again, quarter by quarter",
          "Compare the two lists of flagged rows, line against line",
          "Rerun the fuzzy match with a 30-day window to confirm 22",
          "Check that both keys flag at least one Business order"], "b",
         "Two keys can flag the same number of rows and share fewer than all of them; only the rows themselves show "
         "which real orders one key removed and which copies it missed.",
         "a: counts by quarter can match while the rows differ. c: a narrower window changes the count and never tests "
         "whether the rows are the same. d: says nothing about which rows either key flagged.", "read"),
        ("On an invented export the fuzzy match flags 40 rows and the order_id key flags 38; they share 36. The 4 rows "
         "only the fuzzy match flags are real orders averaging Rs 2,50,000, and the 2 rows only the order_id key "
         "flags are copies of Rs 3,000 each. Against the order_id key, where does the fuzzy match leave the "
         "quarter's revenue?",
         ["Rs 10,06,000 below the order_id key's figure",
          "Rs 6,000 above the order_id key's figure",
          "Rs 10,00,000 below the order_id key's figure",
          "Rs 9,94,000 below the order_id key's figure"], "d",
         "The fuzzy match removes 4 real orders, Rs 10,00,000, and keeps 2 copies the id key removes, Rs 6,000, so "
         "its revenue sits Rs 10,00,000 less Rs 6,000 below: Rs 9,94,000.",
         "a: counts the kept copies as a second loss, when they add rupees. b: counts only the copies and forgets "
         "the four real orders. c: forgets the two copies it keeps.", "design"),
    ]),
    ("ch3_survivor", "Chapter 3 set: the copy that stays", "after chapter 3", [
        ("Two rows share order_id KR-90012. The first reads amount `--` and the second reads `1900`, and every other "
         "field matches. Which row stays in the clean file, and what does the log say?",
         ["The second, whose amount converts; the first logged unreadable",
          "The first, as the original, with the second logged as its copy",
          "Both, flagged, until Finance says which amount it booked",
          "The first, with its amount set to 0 so that the sum runs"], "a",
         "The copy whose amount converts carries the order's value, and the log names the unreadable copy and the "
         "line of the row that stayed.",
         "b: keeps a row that cannot be summed, so the quarter falls Rs 1,900 short. c: counts one order twice in the "
         "rows, and Finance booked one order. d: turns a failure into a sale for nothing.", "read"),
        ("An invented export holds 40 repeated orders. In 38 pairs the copies are identical. In one pair the first "
         "copy's amount is unreadable and its twin reads Rs 2,600. In one pair the copies differ only on the date, "
         "both at Rs 1,450. What does keeping the first copy of every pair cost against the books?",
         ["Rs 0, since every order still keeps one of its rows",
          "Rs 4,050, the unreadable pair and the pair with two dates",
          "Rs 2,600, the twin's value, which the first copy lacks",
          "Rs 5,200, since the lost twin's value counts twice in Q1"], "c",
         "Only the unreadable-first pair moves rupees: the first copy adds nothing to the sum, so its Rs 2,600 twin "
         "is lost. The date pair keeps Rs 1,450 whichever copy stays.",
         "a: misses that the kept copy cannot be summed. b: the date pair costs nothing, since both copies carry "
         "Rs 1,450. d: the twin is lost once, never twice.", "design"),
        ("The ERP team replies that the second extract re-ran May's orders after a pricing fix, and copied April's "
         "and June's unchanged. Which survivor rule goes in the log?",
         ["Last copy for every pair, since the second extract is the fix",
          "First copy for every pair, as the first extract is the original",
          "The copy that converts, then the first, everywhere: it tied Q1",
          "Last copy for May; elsewhere the copy that converts, then first"], "d",
         "May's second copies carry the corrected prices, so they win in May; April and June were copied unchanged, so "
         "the day's rule still decides there, and it keeps a readable copy wherever one exists.",
         "a: applies May's reason to months it does not cover. b: keeps May's uncorrected prices. c: a rupee tie on "
         "today's file is no reason to keep May's prices from before the fix.", "design"),
        ("Twenty rows are set aside as copies. Two are Business orders carrying Rs 9,00,000 of the Rs 9,30,000 set "
         "aside, and eighteen are Retail-Plus orders. Which conversation do the two Business rows belong to first?",
         ["Marketing's, since Retail-Plus carries most of the rows set aside",
          "Anand's, since two rows carry nearly all of the rupees set aside",
          "The auditor's, since every row set aside needs its reason first",
          "Operations', since Business orders move the count of deliveries"], "b",
         "Two rows carry about 97 percent of the rupees, which is where Anand's gap sits; the eighteen Retail-Plus rows "
         "matter to a per-customer rate, a second conversation.",
         "a: the Retail-Plus rows are Marketing's, and they carry Rs 30,000. c: the auditor wants every row, and the "
         "money decides which to show first. d: two rows move a count of orders very little.", "read"),
    ]),
    ("ch4_missing", "Chapter 4 set: what is missing or malformed", "after chapter 4", [
        ("Next month about 1,800 of 60,000 orders will arrive with no status. Operations can look an order up in the "
         "courier's system at about 2 minutes an order, and the delivered share goes out every Monday. Which plan "
         "fits the weekly report?",
         ["Look up all 1,800 by hand before the first report goes out",
          "Keep and flag them; report the share and the count unknown",
          "Default them to delivered, since most orders with a status are",
          "Drop them from the report, since 3 percent cannot move a share"], "b",
         "1,800 lookups at 2 minutes each is 60 hours, more than a working week, so the flag stays and the report says "
         "how many are unknown; a lookup is worth building as an automatic feed from the courier, never as hand work "
         "before each report.",
         "a: 60 hours of lookups before a weekly report. c: invents up to 1,800 deliveries nobody recorded. d: 3 "
         "percent of orders can move a share by up to 3 points, and dropping them hides it.", "design"),
        ("A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted amounts "
         "start `0, 0, 0, 410, 460`. What most likely happened?",
         ["Three amounts failed, and a helper turned each into 0",
          "Three customers placed free orders during a promotion",
          "Three orders were cancelled, and cancelled orders carry 0",
          "Three small orders rounded down to 0 when converted"], "a",
         "No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the fingerprint of a "
         "helper that turns failures into zero.",
         "b: a free order would still carry a line and a reason. c: Kalpa's files book a cancelled order at its "
         "value. d: amounts are whole rupees, so nothing rounds to 0.", "read"),
        ("A colleague converts amounts with `int(v) if v.isdigit() else 0`. On an invented export an amount written "
         "`1,150`, with a thousands separator, comes out as Rs 0. Which change fixes the logic?",
         ["Keep the isdigit test and footnote the order in the note",
          "Replace the 0 with the segment's median amount",
          "Wrap int() in try and return 0 on any failure",
          "Try int(); on failure, log the value and its reason"], "d",
         "isdigit rejects the comma and the else branch invents a zero; trying the conversion and logging a failure "
         "keeps the value and its reason, so the order can be repaired by a stated rule instead of sold for nothing.",
         "a: the order still reads Rs 0 in every total. b: invents an amount nobody booked. c: still turns a failure "
         "into a zero, more quietly.", "fix the logic"),
        ("An amount in the CSV reads `fourteen`. The JSON feed, cut from the same extract, reads `fourteen` for that "
         "order too, and no other source holds it. What goes in the log tonight?",
         ["Repair it from the feed, since a second source agrees with it",
          "Read the word as Rs 14, since the text is plain about the number",
          "Reject it to the log, and ask the ERP team for the booked value",
          "Coerce it to zero, so the pass finishes and the log stays short"], "c",
         "The feed witnesses what the extract held, never whether a value is right, so its agreement repairs nothing; "
         "with no independent source the order goes to the rejects log with its reason until the ERP team supplies "
         "the value.",
         "a: the feed copied the defect from the same extract. b: a word is not an amount, and Rs 14 sits far below "
         "any Kalpa order. d: a zero is a false value, and it hides the defect from every later check.", "design"),
    ]),
    ("ch5_bridge", "Chapter 5 set: the bridge to the books", "after chapter 5", [
        ("Q1 as exported is Rs 3,40,00,000. The rows set aside by the identity rule carry Rs 30,00,000, and the books "
         "say Rs 3,10,00,000. Which statement does the bridge support?",
         ["The export is right, and the books missed Rs 30 lakh of orders",
          "Neither is right until the rows are re-entered from source",
          "The books are right, and the copies explain most of the gap",
          "The books are right, and the copies account for every rupee"], "d",
         "Rs 3,40,00,000 less Rs 30,00,000 is Rs 3,10,00,000, the books exactly, so the copies explain every rupee of "
         "the gap.",
         "a: reverses the finding. b: the bridge already closes, and re-entry would only add error. c: the bridge "
         "closes, so nothing is left over.", "read"),
        ("Tuesday's report said a segment's orders per customer fell 38 percent. On clean data the fall is 23 "
         "percent. What leads the note to the leadership group?",
         ["The 38 percent, since leadership has already seen that figure",
          "The 23 percent, with why it moved from the 38 first reported",
          "Both figures side by side, with no view on which one stands",
          "The 23 percent alone, since the 38 was measured on bad data"], "b",
         "The corrected number leads, with what changed and why, so the reader can trust the next number too.",
         "a: repeats a number known to be wrong. c: leaves the reader to pick, which is the analyst's job. d: drops "
         "the change, and whoever remembers the 38 will ask.", "read"),
        ("For Q3 the export and the books differ by Rs 8,40,000, and your logged moves explain Rs 7,90,000 of it. The "
         "warehouse keeps its own record of every Q3 order, loaded by a separate system and complete for the "
         "quarter. Which proof goes to Anand?",
         ["The bridge as it stands, with Rs 50,000 in an unexplained line",
          "The warehouse record's total alone, since that source is complete",
          "Q3 rebuilt from the warehouse record, and the bridge as its check",
          "The bridge's Rs 7,90,000 now, and the Rs 50,000 at month end"], "c",
         "The bridge leaves Rs 50,000 unexplained, and a source independent of the export and complete for the "
         "quarter can prove the figure on its own; the bridge then checks it, and the two together can say what the "
         "Rs 50,000 is.",
         "a: an unexplained line is a bridge that has not closed. b: a total with no bridge says which number and "
         "never why. d: sends a proof known to be incomplete.", "design"),
        ("Marketing sized a frequency campaign on Tuesday's reading of orders per customer, 1.65 in Q1 against 1.25 in "
         "Q2. Recomputed on the clean file, the day's numbers are 1.45 against 1.25. How has the gap the campaign "
         "aims to close changed?",
         ["It has halved, from 0.40 to 0.20 orders per customer",
          "It is unchanged, since Q2's 1.25 did not move at all",
          "It has gone, since clean revenue fell only 1.6 percent",
          "It shrank by an eighth, as 1.45 sits 12 percent under 1.65"], "a",
         "The gap is Q1 less Q2: 1.65 less 1.25 is 0.40 and 1.45 less 1.25 is 0.20, so the campaign aims at half what "
         "Tuesday showed, and its sizing has to be redone on 0.20.",
         "b: Q2 held while Q1 fell, so the gap moved. c: revenue held because revenue per order rose while orders per "
         "customer still fell. d: measures the change in Q1 alone, not in the gap.", "design"),
        ("The largest Q2 order is 1.8 times the next, placed by a Business account that ordered in both quarters, "
         "with every field valid. Marketing asks for Q2 without it. What goes in the note?",
         ["Q2 without it, since one order that size distorts the quarter",
          "Q2 with the order capped at the next largest, to keep the shape",
          "Q2 with it, flagged, and the figure without it shown beside",
          "Q2 without it, and a footnote that names the account"], "c",
         "Nothing about the record is wrong, so it is revenue; the note shows both readings and says which one "
         "Finance's books hold.",
         "a: size is not a defect, and Finance's books hold the order. b: invents a smaller order nobody booked. d: "
         "a footnote does not put booked revenue back in the quarter.", "read"),
    ]),
    ("ch6_audit", "Chapter 6 set: the log the analyst audits", "after chapter 6", [
        ("A pass reports 500 rows in, 470 kept and 30 set aside, and its Q1 comes out Rs 2,100 below the books' "
         "Rs 3,20,00,000. What do you do next?",
         ["Ship it, since the rows reconcile and Rs 2,100 is a rounding error",
          "Add a Rs 2,100 adjustment line, labelled, so the rupees tie",
          "Find the set-aside row whose value its kept twin lacks",
          "Ask Finance whether its books carry Rs 2,100 too much"], "c",
         "Rows prove no row vanished and say nothing about which rows stayed; the missing rupees sit in a set-aside "
         "row whose kept twin cannot be summed.",
         "a: a gap of any size is an order missing from a file called reconciled. b: an adjustment closes the gap "
         "without a cause. d: the books are the reference until a row proves otherwise.", "read"),
        ("Put the pass in order for Anand's analyst: 1 apply the identity rule, keeping the copy whose amount "
         "converts; 2 reconcile rupees to the books; 3 convert the kept amounts and log any that fail; 4 reconcile "
         "rows, in equals kept plus set aside plus rejected. Which order holds?",
         ["1, 3, 4, 2", "3, 1, 4, 2", "1, 4, 3, 2", "3, 4, 1, 2"], "a",
         "The rule has to see which copy converts, so it runs first and keeps a readable copy; conversion then runs on "
         "what was kept, the rows equation needs the rejects count, and the rupee tie comes last, against the books.",
         "b: step 3 converts the kept amounts, and nothing is kept before the rule runs. c: the rows equation counts "
         "the rejected rows, which exist only after conversion. d: converts and reconciles before anything is kept.",
         "design"),
        ("Anand's analyst has 20 minutes tonight and reads a line in about 30 seconds. Your pass set aside 24 rows, "
         "flagged 4, made 5 decisions and ties 2 control totals, on a raw file of 900 rows and a clean file of 876. "
         "Which hand-over fits her 20 minutes?",
         ["The clean file, to read against the raw one, line by line",
          "A full diff of the raw and clean files, a line per raw row",
          "The clean file, with one line saying 24 rows were set aside",
          "The set-aside, flags and decisions logs, with both totals"], "d",
         "24 + 4 + 5 + 2 is 35 lines, about 17 and a half minutes, and it ties both totals and lets her replay the pass. "
         "The clean file against the raw is 1,776 lines, about 15 hours, and a full diff 900 lines, 7 and a half "
         "hours, and neither says why.",
         "a: about 15 hours, with no reasons. b: 7 and a half hours, showing what went and never why. c: one line, "
         "which ties the rows and nothing else.", "design"),
        ("The analyst asks how she can know the log is complete without trusting the code that wrote it. Which test "
         "gives her that?",
         ["Count the log's lines and compare them with the rows removed",
          "Rebuild the clean file from the raw export and the log alone",
          "Read every line of the log and check that each has a reason",
          "Rerun the pass and compare the new log with the old, line by line"], "b",
         "The replay shares no code with the pass: if the raw export less the logged lines equals the clean file, "
         "nothing left without a line.",
         "a: counts can match while the rows differ. c: proves each line has a reason, never that every removal has a "
         "line. d: the same code repeats the same mistakes.", "design"),
    ]),
]


def length_ok(opts, key):
    """The key is neither the lone longest nor the lone shortest option."""
    k = "abcd".index(key)
    lengths = [len(o) for o in opts]
    lone_long = lengths[k] == max(lengths) and lengths.count(max(lengths)) == 1
    lone_short = lengths[k] == min(lengths) and lengths.count(min(lengths)) == 1
    return not (lone_long or lone_short)


def write():
    for name, title, when, items in SETS:
        design = sum(1 for it in items if it[5] == "design")
        keys = collections.Counter(it[2] for it in items)
        assert max(keys.values()) <= len(items) // 2, (name, keys)
        stu = [f"# {title}", "",
               f"{len(items)} items, about {3 * len(items)} minutes, {when}. " + GLOSS.get(name, "") +
               "Every number here is invented unless it says it is from today's file; the reasoning is the one you "
               "ran on Kalpa's export. Items marked Design ask you to combine two of the day's ideas or to size the "
               "options yourself before you choose.", "",
               f"Post one line, {len(items)} letters in item order, no spaces:", "", "```",
               "Post exactly this shape: " + "x" * len(items), "```", "", "---"]
        sol = [f"# Solution: {title[0].lower() + title[1:]}", "",
               "Answers: " + " ".join(f"{i + 1}{it[2]}" for i, it in enumerate(items)), "",
               f"{design} of {len(items)} items are design items.", "", "## Item by item", "",
               "| Item | Key | Kind | Why it holds | Why the others fail |", "|---|---|---|---|---|"]
        for i, (stem, opts, key, why, others, kind) in enumerate(items):
            assert length_ok(opts, key), (name, i + 1, [len(o) for o in opts], key)
            assert stem.rstrip().endswith("?"), (name, i + 1)
            stu += ["", f"### Q{i + 1}" + (" (Design)" if kind == "design" else ""), "", stem, ""]
            stu += [f"{l}) {o}" for l, o in zip("abcd", opts)]
            sol.append(f"| {i + 1} | {key} | {kind} | {why} | {others} |")
        (DAY / "unguided" / f"C2_W01_D03_{name}_STUDENT.md").write_text("\n".join(stu) + "\n", encoding="utf-8")
        (DAY / "solutions" / f"C2_W01_D03_{name}_solution_STUDENT.md").write_text("\n".join(sol) + "\n", encoding="utf-8")
        print("wrote", name, len(items), "items,", design, "design, keys", dict(sorted(keys.items())))


if __name__ == "__main__":
    write()
