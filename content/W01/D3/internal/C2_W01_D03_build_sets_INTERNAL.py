"""Write Wednesday's six chapter sets and their solutions from one table of items.

Run from the repository root:
    python3 content/W01/D3/internal/C2_W01_D03_build_sets_INTERNAL.py

A set's title is its chapter's full question from the day's question ladder, word for word. Beneath
it come the set's size and timing with the title's terms explained, the stakeholder's words, what the earlier
chapters found, with every term the items use explained and every number they build on printed, who
needs the answer, and the questions on the way (the items' own questions, in order), so the set is sat
with nothing else open. Where an earlier finding is a planted record, the set restates
the rule the room drew from it and leaves the record unnamed.

Each item carries its heading, a short question naming the decision it practises without giving away its key;
its stem; four options; the key; why the key holds; why each other letter fails; the stem in one line
for the solution; and its kind. "design" is kept for items that pass the house test: the learner
combines two ideas or takes several dependent steps, such as the best-fit approach with a sizing the
learner computes, the fact that would switch it, or the second route, and nothing else in the pack
answers it. "read" is reading a result or a trap, "predict" is arithmetic on an exhibit, and "fix the
logic" repairs code. Each solution opens on its Answers line and then gives, item by item, the same
question, the stem in one line, the key with why it holds and each other letter with why it fails, so
it reads with nothing else open.

The script refuses to write a set whose key is the lone longest or the lone shortest option, so
length points neither way; a set whose keys pile onto one position; a heading or a stem that is not a
question; and a heading that carries a word only one option uses when the stem does not carry it
too, since such a heading points at that option.
"""
import collections
import pathlib
import re

DAY = pathlib.Path("content/W01/D3/exercises")
LETTERS = "abcd"
WORDS = {1: "One", 2: "Two", 3: "Three", 4: "four", 5: "five"}
STOP = {"which", "what", "when", "where", "does", "that", "this", "with", "from", "into", "have", "they",
        "their", "them", "then", "than", "your", "each", "every", "will", "would", "should", "about",
        "after", "before", "only", "still", "since", "once", "some", "there"}

INVENTED = ("Every number in the items is invented unless the item says it comes from today's file, and "
            "the reasoning is the one you ran on Kalpa's export. An item marked Design asks you to combine "
            "two of the day's ideas, or to size the options yourself, before you choose.")


def item(heading, stem, options, key, why, others, short, kind):
    return dict(heading=heading, stem=stem, options=options, key=key, why=why, others=others,
                short=short, kind=kind)


SETS = [
    dict(
        name="ch1_profile", chapter=1,
        question="What did the ERP actually send, and does the dashboard's Rs 2.1 crore follow from it?",
        topic="what the ERP actually sent",
        terms=("The ERP is the enterprise resource planning system Finance books orders in. Kalpa Retail's "
               "dashboard reads an export of orders from it and puts Q1 revenue at Rs 2.1 crore, while the "
               "books, Finance's own record of Q1, say Rs 1,90,00,000 to the rupee."),
        quote=("How many records did you receive, and how many can you use?",
               "Anand Iyer, finance controller, Kalpa Retail"),
        who=("Anand Iyer, the finance controller, decides whether Finance acts at all on the drop the team "
             "reported on Tuesday, the fall from Q1 to Q2 measured on the export as delivered. Tonight his analyst "
             "ties out every figure: she matches each one to the books line by line, so a rupee's difference "
             "is a finding. A wrong count costs the most of the day, since every later number stands on it. "
             "A note that calls the dashboard right when it is not makes the analyst discount everything the "
             "team sends, and Marketing loses a month."),
        so_far=("Both of Anand's figures count booked value, every order at the price charged, whatever its "
                "status. Chapter 1 profiled the export before totalling anything: for every field it counted "
                "the values present, the values that convert to the type the field needs, and the distinct "
                "values. The profile found 201 rows for 186 distinct order ids and one amount that does not "
                "convert, and Q1 over the 200 amounts that do convert is Rs 2,09,98,210, so the dashboard's "
                "Rs 2.1 crore is honest arithmetic on this file. Kalpa's Business segment is its sales to "
                "companies, every order in lakhs."),
        scenario=("Anand Iyer, Kalpa Retail's finance controller, will not act on the dashboard's Rs 2.1 crore "
                  "for Q1 until the team shows what the ERP, the enterprise resource planning system Finance "
                  "books orders in, actually sent, since the books, Finance's own record of Q1, say Rs 1.9 "
                  "crore and his analyst ties out every figure, matching it to the books line by line."),
        items=[
            item("Should the note on the largest Q2 order go to Anand?",
                 "A colleague's note to Anand names Rs 980 as the largest Q2 order in a new export, found by "
                 "calling `max()` on the amounts as the CSV gave them. The same export's profile shows 21 "
                 "Business orders, the smallest of them Rs 2,10,000. What do you tell the colleague before the "
                 "note goes?",
                 ["Send it, since max() looked at every Q2 amount the file holds",
                  "Send it, adding that Business orders are counted apart",
                  "Hold it: no largest order sits below every Business order",
                  "Hold it until the ERP team confirms Rs 980 is the true value"], "c",
                 "A Q2 order at Rs 980 cannot be the largest when 21 Business orders start at Rs 2,10,000. "
                 "`max()` compared the amounts as text, where 9 beats 2, so the note names a small order and the "
                 "analyst's audit skips the money.",
                 {"a": "max() ranked the amounts by spelling, so reading every one did not help.",
                  "b": "the Business orders are Q2 orders in the same file, so the note still names the wrong one.",
                  "d": "the ERP holds the right value, and the fault is in how the colleague compared it."},
                 "A colleague's note names Rs 980 as the largest Q2 order in a new export, found by `max()` on the "
                 "amounts as the CSV gave them, while the same export holds 21 Business orders, Kalpa's sales to "
                 "companies, from Rs 2,10,000 up.",
                 "read"),
            item("Which plan fits the 45 minutes before the analyst starts?",
                 "A new export of 1.2 crore rows and 12 fields lands, and Anand's analyst starts work in 45 "
                 "minutes. The team's profile reads about 20 lakh values a minute. Which plan fits the 45 minutes?",
                 ["Profile all 12 fields, then read the rows the profile flags",
                  "Profile order_id and amount, then read the rows they flag",
                  "Tie out a random sample of 10,000 rows against the books",
                  "Total every amount, then set the total beside the books"], "b",
                 "All 12 fields are 14.4 crore values, 72 minutes at 20 lakh a minute, past the deadline. "
                 "order_id and amount are 2.4 crore values, 12 minutes, which leaves half an hour to read what "
                 "they flag, and those two fields are where a repeated order or an unreadable amount would move "
                 "Anand's figure.",
                 {"a": "72 minutes, so the analyst starts before the profile has finished.",
                  "c": "reads under a tenth of a percent of the rows and says nothing about the rest.",
                  "d": "a total cannot say why it differs from the books."},
                 "A new export of 1.2 crore rows and 12 fields lands, the analyst starts in 45 minutes, and the "
                 "team's profile, three counts for every field, reads about 20 lakh values a minute.",
                 "design"),
            item("How many rows are copies, and how many amounts cannot be read?",
                 "An invented export holds 250 rows, 238 distinct order ids and 247 amounts that convert. How "
                 "many rows could inflate revenue as copies, and how many amounts sit outside every total until "
                 "someone reads them?",
                 ["12 copies and 3 unreadable amounts", "3 copies and 12 unreadable amounts",
                  "15 copies and no unreadable amounts", "9 copies and 3 unreadable amounts"], "a",
                 "250 rows less 238 ids is 12 rows beyond one per order, and 250 less 247 is 3 amounts that do "
                 "not convert.",
                 {"b": "swaps the two counts.",
                  "c": "adds the two counts into one.",
                  "d": "takes the 3 failures out of the 12, as if every failure were a copy."},
                 "An invented export holds 250 rows, 238 distinct order ids and 247 amounts that convert.",
                 "predict"),
            item("Which route counts the distinct ids of 4 crore rows with 2 GB free?",
                 "Next quarter's export will hold 4 crore rows. A Python set of order ids takes about 100 bytes "
                 "an id, and the laptop the team leaves running overnight has 2 GB free. Which route counts the "
                 "distinct order ids?",
                 ["A set of every id, then its length, as chapter 1 did",
                  "A Counter over every id, which also keeps how often each appears",
                  "A set of the first crore ids, with the answer times four",
                  "Sort the ids on disk, then count each change from the last"], "d",
                 "4 crore ids at 100 bytes each is about 4 GB, twice the memory free, so any route that holds "
                 "every id at once stops part way. A sort can run on disk and has to remember only the id before.",
                 {"a": "needs about 4 GB.",
                  "b": "needs at least as much as a set, since it keeps a count beside every id.",
                  "c": "scales a count that does not scale, since repeated ids can sit anywhere in the file."},
                 "Next quarter's export will hold 4 crore rows, a Python set takes about 100 bytes an id, and the "
                 "laptop left running overnight has 2 GB free.",
                 "design"),
        ]),
    dict(
        name="ch2_repeats", chapter=2,
        question=("The file holds 201 rows for 186 orders: which rows did the export count twice, and what "
                  "makes two rows one order?"),
        topic="the rows the export counted twice",
        terms=("The file is Kalpa Retail's export of Q1 and Q2 orders from the ERP, the enterprise resource "
               "planning system Finance books orders in, and an order is one sale, which the export may carry "
               "on more than one row."),
        quote=("Which rows did the export count twice, and how do you know they are copies?",
               "Anand Iyer, finance controller, Kalpa Retail"),
        who=("Anand Iyer, the finance controller, needs to know whether his books are short or the export is "
             "high. A wrong answer either keeps Rs 20 lakh that was never earned or deletes real orders from his "
             "books, and every per-customer rate the team reported on Tuesday, such as orders per customer, moves "
             "with the same rows."),
        so_far=("Chapter 1 profiled the export, counting for every field the values present, the values that "
                "convert and the distinct values. It found 201 rows for 186 distinct values of order_id, the "
                "field that carries each order's number, and Q1 over the amounts that convert comes to "
                "Rs 2,09,98,210, Rs 19,98,210 above the books, Finance's own record of Q1 at Rs 1,90,00,000. The "
                "ERP team's note says the CSV was stitched "
                "from two extracts, two separate pulls of rows out of the ERP, during the migration, the Q1 "
                "move of the order data from one system to another. A dedupe is a step that removes the rows "
                "it judges to be copies of another row, and a fuzzy match calls two rows one order when the "
                "customer and the amount match within 60 days. Kalpa's Business segment is its sales to "
                "companies, every order in lakhs."),
        scenario=("Kalpa Retail's export from the ERP, the enterprise resource planning system Finance books "
                  "orders in, holds 201 rows for 186 orders, and Anand Iyer, the finance controller, needs to "
                  "know which rows it counted twice before he believes either the export or the books, Finance's "
                  "own record of Q1 at Rs 1,90,00,000."),
        items=[
            item("Why does a dedupe find 0 copies when 300 rows hold 284 order ids?",
                 "A colleague's dedupe of a 300-row export reports 0 duplicates, and a count of distinct order "
                 "ids returns 284. The pipeline stamps every row with the time it was loaded. What happened?",
                 ["The load stamp differs on every row, so no two rows matched",
                  "16 orders were lost in the load, and the ERP team must resend",
                  "The dedupe is right, and the id count is off by 16 somewhere",
                  "16 rows carry a blank order_id, so the id count falls short"], "a",
                 "A load stamp differs on every row, so a key that compares the whole record never finds a "
                 "match, and 300 rows against 284 ids says 16 rows repeat an order.",
                 {"b": "all 300 rows are present, so nothing was lost.",
                  "c": "the id count is the check, and it disagrees with the dedupe.",
                  "d": "blank ids would show in the profile, the count of each field's present, convertible and "
                       "distinct values, as order_id present on fewer than 300 rows, and the dedupe would still "
                       "match nothing."},
                 "A dedupe of a 300-row export reports 0 duplicates, a count of distinct order ids returns 284, "
                 "and the pipeline stamps every row with the time it was loaded.",
                 "read"),
            item("Which match builds one customer table from two systems inside 2 hours?",
                 "Meera Raghavan, Kalpa Retail's CEO, wants one customer table from the app's 30,000 records and "
                 "the stores' 30,000, each system numbering customers from C-1, spread evenly over 6 cities. The "
                 "team's machine compares about 50 lakh pairs a minute, and the job must finish inside 2 hours. "
                 "Which match fits?",
                 ["Each system's own customer id, one lookup a record",
                  "Cleaned phone and email, every record against every other",
                  "Cleaned phone and email, compared within each city",
                  "Every field matching exactly, name and address too"], "c",
                 "Neither id names one person across both systems, so the match rests on contact fields cleaned "
                 "the same way. Every record against every other is 60,000 x 59,999 / 2, about 180 crore pairs, "
                 "360 minutes at 50 lakh a minute; within 6 cities of 10,000 it is about 30 crore pairs, 60 "
                 "minutes, inside the window, with doubtful pairs sent to a person.",
                 {"a": "C-1 in the app and C-1 in a store are different people.",
                  "b": "the right fields, and 6 hours, three times the window.",
                  "d": "two systems rarely write one person's record identically, so real matches are missed."},
                 "Meera Raghavan, Kalpa Retail's CEO, wants one customer table from 30,000 app records and 30,000 "
                 "store records, each system numbering customers from C-1, over 6 cities, with the machine "
                 "comparing about 50 lakh pairs a minute and 2 hours to finish.",
                 "design"),
            item("What does a reviewer still owe Anand when two keys agree on 22 rows?",
                 "On an invented export the order_id key flags 22 rows as copies, and a fuzzy match on customer "
                 "and amount within 60 days also flags 22. The reviewer is about to sign off because the counts "
                 "agree. Which check does the reviewer still owe Anand?",
                 ["Compare the two keys' counts again, quarter by quarter",
                  "Compare the two lists of flagged rows, line against line",
                  "Rerun the fuzzy match with a 30-day window to confirm 22",
                  "Check that both keys flag at least one Business order"], "b",
                 "Two keys can flag the same number of rows and share fewer than all of them. Only the rows "
                 "themselves show which real orders one key removed and which copies it missed.",
                 {"a": "counts by quarter can match while the rows differ.",
                  "c": "a narrower window changes the count and cannot test whether the rows are the same.",
                  "d": "a check on one segment, Kalpa's sales to companies, says nothing about which rows either "
                       "key flagged."},
                 "On an invented export the order_id key and a fuzzy match on customer and amount within 60 days "
                 "each flag 22 rows, and the reviewer is about to sign off because the counts agree.",
                 "read"),
            item("Where does the fuzzy match leave revenue against the order_id key?",
                 "On an invented export the fuzzy match flags 40 rows and the order_id key flags 38; they share "
                 "36. The 4 rows only the fuzzy match flags are real orders averaging Rs 2,50,000, and the 2 rows "
                 "only the order_id key flags are copies of Rs 3,000 each. Against the order_id key, where does "
                 "the fuzzy match leave the quarter's revenue?",
                 ["Rs 10,06,000 below the order_id key's figure",
                  "Rs 6,000 above the order_id key's figure",
                  "Rs 10,00,000 below the order_id key's figure",
                  "Rs 9,94,000 below the order_id key's figure"], "d",
                 "The fuzzy match removes 4 real orders, Rs 10,00,000, and keeps 2 copies the id key removes, "
                 "Rs 6,000, so its revenue sits Rs 10,00,000 less Rs 6,000 below: Rs 9,94,000.",
                 {"a": "counts the kept copies as a second loss, when they add rupees.",
                  "b": "counts only the copies and forgets the four real orders.",
                  "c": "forgets the two copies the fuzzy match keeps."},
                 "The fuzzy match flags 40 rows and the order_id key 38, sharing 36; the 4 only the fuzzy match "
                 "flags are real orders averaging Rs 2,50,000, and the 2 only the order_id key flags are copies of "
                 "Rs 3,000 each.",
                 "design"),
        ]),
    dict(
        name="ch3_survivor", chapter=3,
        question="When an order appears twice, which copy stays, and does Q1 then land on the books?",
        topic="which copy stays",
        terms=("The books are Finance's own record of Q1, Rs 1,90,00,000 to the rupee, and an order appears "
               "twice when Kalpa Retail's export of orders from the ERP, the enterprise resource planning "
               "system Finance books orders in, carries it on two rows."),
        quote=("When two copies disagree, which one did you keep, and why that one?",
               "Anand Iyer, finance controller, Kalpa Retail"),
        who=("Anand Iyer is the finance controller, and his analyst ties out to the rupee: she matches every "
             "figure to the books line by line, and a rupee's difference is a finding. If the copy kept for any "
             "order moves Q1 away from the books, the reconciliation she checks becomes a finding against the "
             "team, and on today's file keeping the wrong copy moved Q1 by Rs 1,790."),
        so_far=("The export was stitched from two extracts, two separate pulls of rows out of the ERP. Chapter 2 "
                "found that the order_id, the number the ERP issues once per order, decides when two rows are "
                "one order: 15 orders appear twice, 14 in Q1 and 1 in Q2, none three times. For 13 of those "
                "pairs the two copies are identical, and for 2 they disagree. A survivor rule picks which copy "
                "of a pair stays in the clean file, and every copy it does not keep is set aside to a log with "
                "its reason; a copy's twin is the other row of the same order. Kalpa's Business segment is its sales to companies, every order in lakhs, and "
                "Retail-Plus is its paid membership tier."),
        scenario=("When an order appears twice in Kalpa Retail's export from the ERP, the enterprise resource "
                  "planning system Finance books orders in, the team has to choose which copy stays, and Anand "
                  "Iyer's analyst checks that choice against the books, Finance's own record of Q1 at "
                  "Rs 1,90,00,000, to the rupee."),
        items=[
            item("Which row of order KR-90012 stays, and what does the log say?",
                 "On an invented export, two rows share order_id KR-90012. The first reads amount `--` and the "
                 "second reads `1900`, and every other field matches. Which row stays in the clean file, and what "
                 "does the log say?",
                 ["The second, whose amount converts; the first logged unreadable",
                  "The first, as the original, with the second logged as its copy",
                  "Both, flagged, until Finance says which amount it booked",
                  "The first, with its amount set to 0 so that the sum runs"], "a",
                 "The copy whose amount converts carries the order's value, and the log names the unreadable "
                 "copy and the line of the row that stayed.",
                 {"b": "keeps a row that cannot be summed, so the quarter falls Rs 1,900 short.",
                  "c": "counts one order twice in the rows, and Finance booked one order.",
                  "d": "turns a failure into a sale for nothing."},
                 "On an invented export two rows share order_id KR-90012; the first reads amount `--`, the second "
                 "`1900`, and every other field matches.",
                 "read"),
            item("What does keeping the first copy of every pair cost against the books?",
                 "An invented export holds 40 repeated orders. In 38 pairs the copies are identical. In one pair "
                 "the first copy's amount is unreadable and its twin reads Rs 2,600. In one pair the copies "
                 "differ only on the date, both at Rs 1,450. What does keeping the first copy of every pair cost "
                 "against the books?",
                 ["Rs 0, since every order still keeps one of its rows",
                  "Rs 4,050, the unreadable pair and the pair with two dates",
                  "Rs 2,600, the twin's value, which the first copy lacks",
                  "Rs 5,200, since the lost twin's value counts twice in Q1"], "c",
                 "Only the pair whose first copy is unreadable moves rupees: that copy adds nothing to the sum, "
                 "so its Rs 2,600 twin is lost. The pair with two dates keeps Rs 1,450 whichever copy stays.",
                 {"a": "misses that the kept copy cannot be summed.",
                  "b": "the pair with two dates costs nothing, since both copies carry Rs 1,450.",
                  "d": "the twin is lost once, and its value leaves Q1 once."},
                 "An invented export holds 40 repeated orders: 38 identical pairs, one pair whose first copy is "
                 "unreadable beside a twin, the other copy of the same order, at Rs 2,600, and one pair that "
                 "differs only on the date, both copies at Rs 1,450.",
                 "design"),
            item("Which survivor rule goes in the log once the ERP team explains the second extract?",
                 "The ERP team replies that the second extract re-ran May's orders after a pricing fix, and "
                 "copied April's and June's unchanged. Which survivor rule goes in the log?",
                 ["Last copy for every pair, since the second extract is the fix",
                  "First copy for every pair, as the first extract is the original",
                  "The copy that converts, then the first, everywhere: it tied Q1",
                  "Last copy for May; elsewhere the copy that converts, then first"], "d",
                 "May's second copies carry the corrected prices, so they win in May. April and June were copied "
                 "unchanged, so the day's rule still decides there, and it keeps a readable copy wherever one "
                 "exists.",
                 {"a": "applies May's reason to months it does not cover.",
                  "b": "keeps May's prices from before the fix.",
                  "c": "a rupee tie on today's file is no reason to keep May's prices from before the fix."},
                 "The ERP team says the second extract, the second pull of rows out of the ERP, re-ran May's "
                 "orders after a pricing fix and copied April's and June's unchanged.",
                 "design"),
            item("Who hears first about the two Business rows set aside?",
                 "Twenty rows are set aside as copies. Two are Business orders carrying Rs 9,00,000 of the "
                 "Rs 9,30,000 set aside, and eighteen are Retail-Plus orders. Which conversation do the two "
                 "Business rows belong to first?",
                 ["Marketing's, since Retail-Plus carries most of the rows set aside",
                  "Anand's, since two rows carry nearly all of the rupees set aside",
                  "The auditor's, since every row set aside needs its reason first",
                  "Operations', since Business orders move the count of deliveries"], "b",
                 "Two rows carry about 97 percent of the rupees, which is where Anand's gap sits. The eighteen "
                 "Retail-Plus rows matter to a per-customer rate, which is a second conversation.",
                 {"a": "the Retail-Plus rows are Marketing's, and they carry Rs 30,000.",
                  "c": "the auditor wants every row, and the money decides which to show first.",
                  "d": "two rows move a count of orders very little."},
                 "Twenty rows are set aside as copies: two Business orders, Kalpa's sales to companies, carry "
                 "Rs 9,00,000 of the Rs 9,30,000, and eighteen are Retail-Plus orders, from Kalpa's paid "
                 "membership tier.",
                 "read"),
        ]),
    dict(
        name="ch4_missing", chapter=4,
        question=("What should the pass do with a value that is missing or cannot be read, so that no decision "
                  "invents or deletes a fact?"),
        topic="values that are missing or cannot be read",
        terms=("The pass is the day's cleaning run on Kalpa Retail's export of orders from the ERP, the "
               "enterprise resource planning system Finance books orders in. It profiles the file, counting for "
               "every field the values present, the values that convert and the distinct values; keeps one row "
               "per order; converts the amounts; decides every defect in writing; and reconciles to the books, "
               "Finance's own record of Q1."),
        quote=("Can my analyst follow every decision you made?", "Anand Iyer, finance controller, Kalpa Retail"),
        who=("Operations reads the share of orders delivered every week, and Finance reads every rupee, so a "
             "wrong call on a missing or unreadable value changes a number one of them reports. Tonight the "
             "analyst who works for Anand Iyer, the finance controller, reads every choice in the log, and a "
             "choice she cannot follow costs the team her trust."),
        so_far=("Chapter 3 kept one row for each of today's 186 orders and set 15 rows aside, and Q1 on the kept "
                "rows is Rs 1,90,00,000, the books to the rupee. Some kept orders still carry a field with no "
                "value, and the pass needs a written policy for any amount that does not convert. Revenue in "
                "every figure is booked value, every order at the price charged, whatever its status. An extract "
                "is one pull of rows out of the ERP."),
        scenario=("Kalpa Retail's export of orders from the ERP, the enterprise resource planning system Finance "
                  "books orders in, still holds values that are missing or cannot be read once one row per "
                  "order is kept, and each needs a written decision that the analyst who works for Anand Iyer, "
                  "the finance controller, can follow, since Operations reads the delivered share every week and "
                  "Finance reads every rupee."),
        items=[
            item("Which plan for 1,800 orders with no status fits the weekly report?",
                 "Next month about 1,800 of 60,000 orders will arrive with no status. Operations can look an order "
                 "up in the courier's system at about 2 minutes an order, and the delivered share goes out every "
                 "Monday. Which plan fits the weekly report?",
                 ["Look up all 1,800 by hand before the first report goes out",
                  "Keep and flag them; report the share and the count unknown",
                  "Default them to delivered, since most orders with a status are",
                  "Drop them from the report, since 3 percent cannot move a share"], "b",
                 "1,800 lookups at 2 minutes each is 60 hours, more than a working week, so the flag stays and "
                 "the report says how many are unknown. A lookup earns its place once it runs as an automatic feed "
                 "from the courier, and done by hand it costs those 60 hours before every report.",
                 {"a": "60 hours of lookups before a weekly report.",
                  "c": "invents up to 1,800 deliveries nobody recorded.",
                  "d": "3 percent of orders can move a share by up to 3 points, and dropping them hides it."},
                 "Next month about 1,800 of 60,000 orders will arrive with no status, a lookup in the courier's "
                 "system takes about 2 minutes an order, and the delivered share goes out every Monday.",
                 "design"),
            item("What do 300 convertible amounts that start 0, 0, 0 tell you?",
                 "A colleague's profile of a Kalpa export reports 300 of 300 amounts convertible, and the sorted "
                 "amounts start `0, 0, 0, 410, 460`. What most likely happened?",
                 ["Three amounts failed, and a helper turned each into 0",
                  "Three customers placed free orders during a promotion",
                  "Three orders were cancelled, and cancelled orders carry 0",
                  "Three small orders rounded down to 0 when converted"], "a",
                 "No Kalpa order is worth Rs 0, and a perfect convertible count beside three zeros is the "
                 "fingerprint of a helper that turns failures into zero.",
                 {"b": "a free order would still carry a line and a reason.",
                  "c": "Kalpa's files book a cancelled order at its value.",
                  "d": "amounts are whole rupees, so nothing rounds to 0."},
                 "A colleague's profile of a Kalpa export, its count of each field's present, convertible and "
                 "distinct values, reports 300 of 300 amounts convertible, and the sorted amounts start "
                 "`0, 0, 0, 410, 460`.",
                 "read"),
            item("Which change fixes a conversion that turns `1,150` into Rs 0?",
                 "A colleague converts amounts with `int(v) if v.isdigit() else 0`. On an invented export an "
                 "amount written `1,150`, with a thousands separator, comes out as Rs 0. Which change fixes the "
                 "logic?",
                 ["Keep the isdigit test and footnote the order in the note",
                  "Replace the 0 with the segment's median amount",
                  "Wrap int() in try and return 0 on any failure",
                  "Try int(); on failure, log the value and its reason"], "d",
                 "isdigit rejects the comma and the else branch invents a zero. Trying the conversion and logging "
                 "a failure keeps the value and its reason, so the order waits in the log until a stated rule "
                 "repairs it, and nothing is sold for Rs 0.",
                 {"a": "the order still reads Rs 0 in every total.",
                  "b": "invents an amount nobody booked.",
                  "c": "still turns a failure into a zero, more quietly."},
                 "A colleague converts amounts with `int(v) if v.isdigit() else 0`, and an invented amount "
                 "written `1,150`, with a thousands separator, comes out as Rs 0.",
                 "fix the logic"),
            item("What goes in the log for an amount that reads `fourteen`?",
                 "On an invented export, an amount in the CSV reads `fourteen`. The JSON feed, cut from the same "
                 "extract, reads `fourteen` for that order too, and no other source holds it. What goes in the "
                 "log tonight?",
                 ["Repair it from the feed, since a second source agrees with it",
                  "Read the word as Rs 14, since the text is plain about the number",
                  "Reject it to the log, and ask the ERP team for the booked value",
                  "Coerce it to zero, so the pass finishes and the log stays short"], "c",
                 "The feed witnesses what the extract held, never whether a value is right, so its agreement "
                 "repairs nothing. With no independent source the order goes to the rejects log with its reason "
                 "until the ERP team supplies the booked value.",
                 {"a": "the feed copied the defect from the same extract.",
                  "b": "reading a word as a number is a guess, and Rs 14 sits far below any Kalpa order.",
                  "d": "a zero is a false value, and it hides the defect from every later check."},
                 "On an invented export an amount reads `fourteen`, the JSON feed cut from the same extract, one "
                 "pull of rows out of the ERP, reads `fourteen` too, and no other source holds the order's booked "
                 "value, the price it was charged.",
                 "design"),
        ]),
    dict(
        name="ch5_bridge", chapter=5,
        question=("Can we prove to Anand, one cause at a time, that his Rs 1.9 crore is right, and does "
                  "Tuesday's finding survive the clean file?"),
        topic="the proof of Anand's Rs 1.9 crore",
        terms=("Anand Iyer is Kalpa Retail's finance controller, and his Rs 1.9 crore is the books, Finance's "
               "own record of Q1, at Rs 1,90,00,000 to the rupee. Tuesday's finding was the team's report that "
               "orders per customer in Retail-Plus, Kalpa's paid membership tier, fell 49 percent from Q1 to Q2, "
               "from 2.32 to 1.18, and the clean file is the export after the day's pass, one row per order with "
               "every defect decided in writing."),
        quote=("Which figure is right, and does the Retail-Plus fall still stand?",
               "Anand Iyer, finance controller, Kalpa Retail"),
        who=("Anand wants a proof his analyst can follow, and Marketing's rescue campaign for Retail-Plus waits "
             "on whether Tuesday's finding survives. A proof Finance cannot follow costs his trust, and a finding "
             "nobody recomputes sends Marketing after a fall of a size nobody checked."),
        so_far=("Chapters 1 to 4 built the clean file from the 201 rows of the export from the ERP, the "
                "enterprise resource planning system Finance books orders in: 186 orders kept, 15 rows set aside "
                "as copies by the identity rule, the rule that decides when two rows are one order, and one "
                "order kept with a flag on its missing status. Q1 on the clean file is Rs 1,90,00,000, against "
                "Rs 2,09,98,210 as exported. A bridge walks one total to another in steps, one cause to a step, "
                "each with its rupees. Orders per customer is one branch of Monday's revenue tree, revenue = "
                "customers x orders per customer x revenue per order, with each branch read as Q2's multiple of "
                "Q1, and on Tuesday the team read it as 1.65 in Q1 against 1.25 in Q2. Kalpa's Business segment "
                "is its sales to companies, every order in lakhs."),
        scenario=("Anand Iyer, Kalpa Retail's finance controller, wants proof, one cause at a time, that the "
                  "books, Finance's own record of Q1, are right at Rs 1,90,00,000, and Marketing wants to know "
                  "whether Tuesday's finding, a 49 percent fall in orders per customer for Retail-Plus, Kalpa's "
                  "paid membership tier, survives the clean file."),
        items=[
            item("What does a bridge from Rs 3,40,00,000 to the books' Rs 3,10,00,000 support?",
                 "Q1 as exported is Rs 3,40,00,000. The rows set aside by the identity rule carry Rs 30,00,000, "
                 "and the books say Rs 3,10,00,000. Which statement does the bridge support?",
                 ["The export is right, and the books missed Rs 30 lakh of orders",
                  "Neither is right until the rows are re-entered from source",
                  "The books are right, and the copies explain most of the gap",
                  "The books are right, and the copies account for every rupee"], "d",
                 "Rs 3,40,00,000 less Rs 30,00,000 is Rs 3,10,00,000, the books exactly, so the copies explain "
                 "every rupee of the gap.",
                 {"a": "reverses the finding.",
                  "b": "the bridge already closes, and re-entry would only add error.",
                  "c": "the bridge closes, so nothing is left over."},
                 "Q1 as exported is Rs 3,40,00,000, the copies set aside by the identity rule, which keeps one row "
                 "per order, carry Rs 30,00,000, and the books say Rs 3,10,00,000; the bridge walks the first "
                 "total to the second one cause at a time.",
                 "read"),
            item("What leads the note once a 38 percent fall turns out to be 23?",
                 "Tuesday's report said a segment's orders per customer fell 38 percent. On clean data the fall is "
                 "23 percent. What leads the note to the leadership group?",
                 ["The 38 percent, since leadership has already seen that figure",
                  "The 23 percent, with why it moved from the 38 first reported",
                  "Both figures side by side, with no view on which one stands",
                  "The 23 percent alone, since the 38 was measured on bad data"], "b",
                 "The corrected number leads, with what changed and why, so the reader can trust the next number "
                 "too.",
                 {"a": "repeats a number known to be wrong.",
                  "c": "leaves the reader to pick, which is the analyst's job.",
                  "d": "drops the change, and whoever remembers the 38 will ask."},
                 "Tuesday's report said a segment's orders per customer fell 38 percent, and on clean data the fall "
                 "is 23 percent.",
                 "read"),
            item("Which proof goes to Anand for the third quarter?",
                 "For Q3 the export and the books differ by Rs 8,40,000, and your logged moves explain Rs 7,90,000 "
                 "of it. The warehouse keeps its own record of every Q3 order, loaded by a separate system and "
                 "complete for the quarter. Which proof goes to Anand?",
                 ["The bridge as it stands, with Rs 50,000 in an unexplained line",
                  "The warehouse record's total alone, since that source is complete",
                  "Q3 rebuilt from the warehouse record, and the bridge as its check",
                  "The bridge's Rs 7,90,000 now, and the Rs 50,000 at month end"], "c",
                 "The bridge leaves Rs 50,000 unexplained, and a source independent of the export and complete for "
                 "the quarter can prove the figure on its own. The bridge then checks it, and the two together can "
                 "say what the Rs 50,000 is.",
                 {"a": "a bridge with an unexplained line has not closed.",
                  "b": "a total with no bridge says which number is right and gives no reason.",
                  "d": "sends a proof known to be incomplete."},
                 "For Q3 the export and the books differ by Rs 8,40,000, the logged moves explain Rs 7,90,000, and "
                 "a warehouse record of every Q3 order, loaded by a separate system, is complete for the quarter.",
                 "design"),
            item("How has the gap Marketing's campaign aims to close changed?",
                 "Marketing sized a frequency campaign on Tuesday's reading of orders per customer, 1.65 in Q1 "
                 "against 1.25 in Q2. Recomputed on the clean file, the day's numbers are 1.45 against 1.25. How "
                 "has the gap the campaign aims to close changed?",
                 ["It has halved, from 0.40 to 0.20 orders per customer",
                  "It is unchanged, since Q2's 1.25 did not move at all",
                  "It has gone, since clean revenue fell only 1.6 percent",
                  "It shrank by an eighth, as 1.45 sits 12 percent under 1.65"], "a",
                 "The gap is Q1 less Q2: 1.65 less 1.25 is 0.40 and 1.45 less 1.25 is 0.20, so the campaign aims "
                 "at half what Tuesday showed, and its sizing has to be redone on 0.20.",
                 {"b": "Q2 held while Q1 fell, so the gap moved.",
                  "c": "revenue held because revenue per order rose while orders per customer still fell.",
                  "d": "measures the change in Q1 alone, and the gap is Q1 less Q2."},
                 "Marketing sized a frequency campaign on Tuesday's 1.65 against 1.25 orders per customer, and the "
                 "clean file reads 1.45 against 1.25.",
                 "design"),
            item("What goes in the note when Marketing asks for Q2 without its largest order?",
                 "The largest Q2 order is 1.8 times the next, placed by a Business account that ordered in both "
                 "quarters, with every field valid. Marketing asks for Q2 without it. What goes in the note?",
                 ["Q2 without it, since one order that size distorts the quarter",
                  "Q2 with the order capped at the next largest, to keep the shape",
                  "Q2 with it, flagged, and the figure without it shown beside",
                  "Q2 without it, and a footnote that names the account"], "c",
                 "Nothing about the record is wrong, so it is revenue, and the note shows both readings and says "
                 "which one Finance's books hold.",
                 {"a": "an order's size says nothing against it, and Finance's books hold the order.",
                  "b": "invents a smaller order nobody booked.",
                  "d": "a footnote leaves the order's booked value, the price it was charged, out of the quarter."},
                 "The largest Q2 order is 1.8 times the next, from a Business account, one of Kalpa's sales to "
                 "companies, that ordered in both quarters with every field valid, and Marketing asks for Q2 "
                 "without it.",
                 "read"),
        ]),
    dict(
        name="ch6_audit", chapter=6,
        question=("Can Anand's analyst audit every decision tonight and rebuild the clean file from the log "
                  "alone?"),
        topic="the log Anand's analyst audits",
        terms=("Anand Iyer is Kalpa Retail's finance controller. The clean file is the export of orders from the "
               "ERP, the enterprise resource planning system Finance books orders in, after the day's pass, one "
               "row per order with every defect decided in writing, and the log is the set of files in which the "
               "pass records what it removed, flagged and decided, and why."),
        quote=("Send the reconciliation and the log before the day closes. My analyst checks it tonight.",
               "Anand Iyer, finance controller, Kalpa Retail"),
        who=("Anand's analyst checks the logs tonight, and an auditor may ask next quarter why any row went. A "
             "log she cannot follow costs a week of questions, and a log that fails her tie-out, which matches "
             "every figure to the books line by line, costs the team her trust in everything else it sends."),
        so_far=("Chapter 5 proved today's Q1 with a bridge, a walk from one total to another, one cause to a "
                "step: Rs 2,09,98,210 as exported, less Rs 19,67,560 of copies of corporate orders and Rs 30,650 "
                "of copies of consumer orders, lands on the books, Finance's own record of Q1, at Rs 1,90,00,000. "
                "The identity rule is the rule that decides when two rows are one order. The pass writes four logs. "
                "The set-aside log holds every row the pass removed, with its reason and the line of its twin, "
                "the row of the same order that stayed; the rejects log holds every value that would not "
                "convert; the flags log holds every record kept with a question on it; and the decisions log "
                "holds each rule with the rows and rupees it moved. Control totals are a count and a sum "
                "computed at both ends of a transfer and compared, here rows and rupees."),
        scenario=("Anand Iyer's analyst checks the team's logs tonight against the books, Finance's own record "
                  "of Q1, so every decision the pass made on Kalpa Retail's export has to be one she can audit, "
                  "and the clean file has to be one she can rebuild from the raw export and the log alone."),
        items=[
            item("What do you do next with a pass Rs 2,100 below the books?",
                 "A pass reports 500 rows in, 470 kept and 30 set aside, and its Q1 comes out Rs 2,100 below the "
                 "books' Rs 3,20,00,000. What do you do next?",
                 ["Ship it, since the rows reconcile and Rs 2,100 is a rounding error",
                  "Add a Rs 2,100 adjustment line, labelled, so the rupees tie",
                  "Find the set-aside row whose value its kept twin lacks",
                  "Ask Finance whether its books carry Rs 2,100 too much"], "c",
                 "Rows prove no row vanished and say nothing about which rows stayed. The missing rupees sit in a "
                 "set-aside row whose twin, the kept copy of the same order, cannot be summed.",
                 {"a": "a gap of any size is an order missing from a file called reconciled.",
                  "b": "an adjustment closes the gap without a cause.",
                  "d": "the books are the reference until a row proves otherwise."},
                 "A pass reports 500 rows in, 470 kept and 30 set aside, and its Q1 comes out Rs 2,100 below the "
                 "books' Rs 3,20,00,000.",
                 "read"),
            item("In what order does the pass run for Anand's analyst?",
                 "Put the pass in order for Anand's analyst: 1 apply the identity rule, keeping the copy whose "
                 "amount converts; 2 reconcile rupees to the books; 3 convert the kept amounts and log any that "
                 "fail; 4 reconcile rows, in equals kept plus set aside plus rejected. Which order holds?",
                 ["1, 3, 4, 2", "3, 1, 4, 2", "1, 4, 3, 2", "3, 4, 1, 2"], "a",
                 "The rule has to see which copy converts, so it runs first and keeps a readable copy. Conversion "
                 "then runs on what was kept, the rows equation needs the rejects count, and the rupee tie comes "
                 "last, against the books.",
                 {"b": "step 3 converts the kept amounts, and nothing is kept before the rule runs.",
                  "c": "the rows equation counts the rejected rows, which exist only after conversion.",
                  "d": "converts and reconciles before anything is kept."},
                 "Four steps to order: 1 apply the identity rule, which decides when two rows are one order, "
                 "keeping the copy whose amount converts; 2 "
                 "reconcile rupees to the books; 3 convert the kept amounts and log any that fail; 4 reconcile "
                 "rows, in equals kept plus set aside plus rejected.",
                 "design"),
            item("Which hand-over fits the analyst's 20 minutes?",
                 "Anand's analyst has 20 minutes tonight and reads a line in about 30 seconds. Your pass set aside "
                 "24 rows, flagged 4, made 5 decisions and ties 2 control totals, on a raw file of 900 rows and a "
                 "clean file of 876. Which hand-over fits her 20 minutes?",
                 ["The clean file, to read against the raw one, line by line",
                  "A full diff of the raw and clean files, a line per raw row",
                  "The clean file, with one line saying 24 rows were set aside",
                  "The set-aside, flags and decisions logs, with both totals"], "d",
                 "24 + 4 + 5 + 2 is 35 lines, about 17 and a half minutes, and it ties both totals and lets her "
                 "replay the pass. The clean file against the raw is 1,776 lines, about 15 hours, and a full diff "
                 "900 lines, 7 and a half hours, and neither says why.",
                 {"a": "about 15 hours, with no reasons.",
                  "b": "7 and a half hours, showing what went with no reason beside it.",
                  "c": "one line, which ties the rows and nothing else."},
                 "The analyst has 20 minutes and reads a line in about 30 seconds; the pass set aside 24 rows, "
                 "flagged 4, made 5 decisions and ties 2 control totals, a count and a sum compared at both ends, "
                 "on a raw file of 900 rows and a clean file of 876.",
                 "design"),
            item("Which test shows the log is complete without trusting the code that wrote it?",
                 "The analyst asks how she can know the log is complete without trusting the code that wrote it. "
                 "Which test gives her that?",
                 ["Count the log's lines and compare them with the rows removed",
                  "Replay the log on the raw export and compare with the clean file",
                  "Read every line of the log and check that each has a reason",
                  "Rerun the pass and compare the new log with the old, line by line"], "b",
                 "The replay shares no code with the pass: if the raw export less the logged lines equals the "
                 "clean file, nothing left without a line.",
                 {"a": "counts can match while the rows differ.",
                  "c": "proves that each line has a reason and says nothing about a removal with no line.",
                  "d": "the same code repeats the same mistakes."},
                 "The analyst asks how she can know the log is complete without trusting the code that wrote it.",
                 "design"),
        ]),
]


def words(text):
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) >= 4 and w not in STOP}


def length_ok(opts, key):
    """The key is neither the lone longest nor the lone shortest option."""
    k = LETTERS.index(key)
    lengths = [len(o) for o in opts]
    lone_long = lengths[k] == max(lengths) and lengths.count(max(lengths)) == 1
    lone_short = lengths[k] == min(lengths) and lengths.count(min(lengths)) == 1
    return not (lone_long or lone_short)


def heading_points(it):
    """Words in the heading that only one option uses and the stem does not carry."""
    head, stem = words(it["heading"]), words(it["stem"])
    found = []
    for n, opt in enumerate(it["options"]):
        own = words(opt) - set().union(*(words(o) for m, o in enumerate(it["options"]) if m != n))
        found += sorted((head & own) - stem)
    return found


def write():
    for s in SETS:
        name, n, items = s["name"], s["chapter"], s["items"]
        k = len(items)
        design = [i + 1 for i, it in enumerate(items) if it["kind"] == "design"]
        keys = collections.Counter(it["key"] for it in items)
        assert max(keys.values()) <= k // 2, (name, keys)
        assert s["question"].endswith("?"), name
        stu = [f"# {s['question']}", "",
               f"Chapter {n} set, {k} items, about {3 * k} minutes, after chapter {n}. {s['terms']}", "",
               f"> \"{s['quote'][0]}\"", ">", f"> {s['quote'][1]}", "", s["so_far"], "",
               f"**Who needs the answer.** {s['who']}", "",
               "**The questions on the way.**", ""]
        stu += [f"- {it['heading']}" for it in items]
        stu += ["", INVENTED, "",
                f"**What you post.** One line of {k} letters in item order, no spaces, in this shape:", "",
                "```", "Post exactly this shape: " + "x" * k, "```", "", "---"]
        count = WORDS[len(design)] + f" of the {WORDS[k]} items are design items: "
        count += ", ".join(str(d) for d in design[:-1]) + (" and " if len(design) > 1 else "") + f"{design[-1]}."
        sol = [f"# Which answers hold in the chapter {n} set on {s['topic']}, and why?", "",
               "Answers: " + " ".join(f"{i + 1}{it['key']}" for i, it in enumerate(items)), "",
               s["scenario"], "", count]
        for i, it in enumerate(items):
            opts, key = it["options"], it["key"]
            assert len(opts) == 4 and key in LETTERS, (name, i + 1)
            assert length_ok(opts, key), (name, i + 1, [len(o) for o in opts], key)
            assert it["stem"].rstrip().endswith("?"), (name, i + 1)
            assert it["heading"].endswith("?"), (name, i + 1)
            assert not heading_points(it), (name, i + 1, heading_points(it))
            assert set(it["others"]) == set(LETTERS) - {key}, (name, i + 1)
            # The tag sits before the question, so every heading ends on its question mark.
            head = f"### Q{i + 1}" + (" (Design)" if it["kind"] == "design" else "") + f". {it['heading']}"
            stu += ["", head, "", it["stem"], ""]
            stu += [f"{l}) {o}" for l, o in zip(LETTERS, opts)]
            sol += ["", head, "", it["short"], "",
                    f"The key is {key}, \"{opts[LETTERS.index(key)]}\". {it['why']}", ""]
            sol += [f"- {l}, \"{o}\": {it['others'][l]}" for l, o in zip(LETTERS, opts) if l != key]
        (DAY / "unguided" / f"C2_W01_D03_{name}_STUDENT.md").write_text("\n".join(stu) + "\n", encoding="utf-8")
        (DAY / "solutions" / f"C2_W01_D03_{name}_solution_STUDENT.md").write_text("\n".join(sol) + "\n",
                                                                                   encoding="utf-8")
        print("wrote", name, k, "items,", len(design), "design, keys", dict(sorted(keys.items())))


if __name__ == "__main__":
    write()
