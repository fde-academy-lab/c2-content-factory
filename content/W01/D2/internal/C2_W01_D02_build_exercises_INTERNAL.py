"""Write the six chapter scenario sets and their solutions from one table, so a key never drifts.

Run from the repository root:
    python3 content/W01/D2/internal/C2_W01_D02_build_exercises_INTERNAL.py

A set's title is its chapter's full question from the day's question ladder, word for word. Beneath
it come the set's size and timing with the first terms explained, the stakeholder's words, what the
earlier chapters found with every number the items build on and every term they use, who needs the
answer, and the questions on the way (the items' own headings, in order), then the exhibit, so the set
is sat with nothing else open. Where an earlier finding is a planted record, the set restates the rule
the room drew from it and leaves the record unnamed. Chapters 1 to 3 never name the segment whose
orders per member fell, and never print its name at all, since the room finds it in its own run at
the end of chapter 3.

Each item carries its heading, a short question naming what the item asks without giving away its
key; its stem; four options; the key; why the key holds; why each other letter fails; the stem in one
line for the solution; and its kind. "design" is the best-fit approach, a sizing, the fact that would
switch it or the second route, and "scenario" is every other business item. Each solution opens on
its Answers line and then gives, item by item, the same heading, the stem in one line, the key with
why it holds and each other letter with why it fails, so it reads with nothing else open.

The options, the keys and every number are the ones merged on 30 September 2026; the provenance's
depth-loop table says why each is as it is. The script refuses to write a set whose answer string
has drifted from that, whose keys pile onto one position, whose key is the lone longest option, whose
heading or stem is not a question, whose heading carries a word that only one option uses when the
stem does not carry it too, or whose text carries a dash, the rupee glyph or a banned word.
"""
import collections
import importlib.util
import pathlib
import re

DAY = pathlib.Path(__file__).resolve().parents[1]
UNG = DAY / "exercises" / "unguided"
SOL = DAY / "exercises" / "solutions"
LETTERS = "abcd"
NUMBER_WORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six"}
STOP = {"which", "what", "when", "where", "does", "that", "this", "with", "from", "into", "have", "they",
        "their", "them", "then", "than", "your", "each", "every", "will", "would", "should", "about",
        "after", "before", "only", "still", "since", "once", "some", "there"}

# The house's banned words come from the gate itself, so this file never carries them as text.
_GATE = importlib.util.spec_from_file_location("verify", DAY.parents[2] / "scripts" / "verify.py")
_verify = importlib.util.module_from_spec(_GATE)
_GATE.loader.exec_module(_verify)
BANNED = [w for w in _verify.BANNED if " " not in w]

# The answer strings merged on 30 September 2026. A change here is a change of key, which the
# provenance must record before this table moves.
MERGED = {1: "1c 2b 3a 4d 5b 6c", 2: "1b 2d 3c 4a 5d 6b", 3: "1d 2a 3c 4b 5a 6d",
          4: "1b 2c 3d 4a 5b 6a", 5: "1c 2a 3b 4d 5b 6d", 6: "1c 2d 3b 4a 5d 6a"}

KAVYA = ("then compare your letters with the person beside you before Kavya's review. Kavya Nair is the "
         "senior analyst on Kalpa Retail's data team, and her review is the check that closes every chapter.")
RULES = ("Every item has one right answer. Decide first, then record the letter. An item marked Design asks "
         "for the best-fit approach, a sizing, the fact that would switch it, or the second route.")


def item(heading, stem, options, key, why, others, short, kind):
    return dict(heading=heading, stem=stem, options=options, key=key, why=why, others=others,
                short=short, kind=kind)


SETS = [
    dict(
        chapter=1, slug="ch1_is_the_drop_real",
        question="Did revenue really fall from Q1 to Q2, and by how much, once both sides cover the same weeks?",
        terms=("Kalpa Retail's financial year opens in April, so Q1 runs from April to June and Q2 from July "
               "to September."),
        quote=("Q2 was Rs 1.9 crore, Q1 was 2.1. Marketing says more customers. Prove it or disprove it.",
               "Meera Raghavan, CEO, Kalpa Retail"),
        so_far=("Revenue in every item is booked revenue: every order placed, at the price charged, before any "
                "cancellation or return. A quarter is closed once its last day has passed and no order can still "
                "land in it. Marketing has asked for Rs 12 crore to win new customers, on a slide whose Q2 figure "
                "is a tile on Marketing's dashboard, read on 15 September. Chapter 1 weighed four ways to size "
                "the fall: the closed quarters as totals; matched weeks, the same weeks of each quarter set side "
                "by side; a rate per day or per week, each side's revenue divided by the days or weeks its dates "
                "cover; and the same quarter last year. A second route reaches the same number by an "
                "independent method, one that could have disagreed with the first. Each order record carries "
                "its `order_date`, the day it was placed, and a `quarter` field that the export fills in."),
        who=("Meera Raghavan, the CEO, decides whether Marketing's Rs 12 crore acquisition request is urgent, "
             "and the request rests on a slide saying revenue fell 25.9 percent. Overstate the fall and crores "
             "move in a hurry on a lever nobody has checked; understate it and a real leak runs another quarter."),
        exhibit="The numbers every item refers to, in booked revenue on the export as it stands:",
        table="""| Window | Dates | Orders | Revenue |
|---|---|---|---|
| Q1, closed | 1 Apr to 30 Jun | 114 | Rs 2,10,00,000 |
| Q2, closed | 1 Jul to 30 Sep | 86 | Rs 1,87,00,000 |
| Q2 dashboard tile, cut on 15 September | 1 Jul to 15 Sep | 70 | Rs 1,55,59,950 |""",
        picture="""flowchart LR
    A["<b>1 Apr</b><br/>Q1 opens"] --> B["<b>1 Jul</b><br/>Q2 opens"]
    B --> C["<b>15 Sep</b><br/>the tile is cut"]
    C --> D["<b>30 Sep</b><br/>Q2 closes"]""",
        scenario=("Meera Raghavan, Kalpa Retail's CEO, asked whether revenue really fell from Q1, April to June, "
                  "to Q2, July to September, before she answers Marketing's request for Rs 12 crore to win new "
                  "customers. The request rests on a slide showing a fall of 25.9 percent. Revenue is booked "
                  "revenue, every order placed at the price charged before any cancellation or return: "
                  "Rs 2,10,00,000 in Q1 and Rs 1,87,00,000 in Q2, both quarters closed, against Rs 1,55,59,950 on "
                  "a dashboard tile read on 15 September."),
        items=[
            item("How far did revenue fall between the two closed quarters?",
                 "Meera asks how far revenue fell between the two closed quarters. Which figure goes in the reply?",
                 ["12.3 percent, the Rs 23,00,000 gap measured against Q2's total",
                  "9.5 percent, from the rounded Rs 1.9 crore against Rs 2.1 crore",
                  "11.0 percent, the Rs 23,00,000 gap measured against Q1's total",
                  "25.9 percent, the figure on the dashboard tile Marketing quotes"], "c",
                 "A change is measured against the quarter it starts from. Rs 23,00,000 over Rs 2,10,00,000 is "
                 "11.0 percent, on two closed quarters of 13 weeks each.",
                 {"a": "measuring the gap against Q2's total inflates the fall to 12.3 percent.",
                  "b": "the rounded crore figures lose Rs 3,00,000 of the gap.",
                  "d": "the tile stops on 15 September, so part of its fall comes from the shorter window."},
                 "Meera asks how far revenue fell between the two closed quarters, Rs 2,10,00,000 in Q1 and "
                 "Rs 1,87,00,000 in Q2.",
                 "scenario"),
            item("Why does Marketing's slide say revenue fell 25.9 percent?",
                 "Marketing's slide reads \"Q2 Rs 1,55,59,950 against Q1 Rs 2,10,00,000: revenue fell 25.9 "
                 "percent.\" What makes the slide unfit to act on?",
                 ["The percentage is computed on Q2's total, which overstates the fall",
                  "It sets about 11 weeks of Q2 against all 13 weeks of the closed Q1",
                  "It counts booked orders, where Finance would count delivered ones",
                  "It rounds both totals to the nearest lakh before dividing them"], "b",
                 "The tile runs from 1 July to 15 September, about 11 weeks, against Q1's 13, so two weeks are "
                 "missing from one side only, and Rs 12 crore would move on a gap that is mostly the calendar.",
                 {"a": "Rs 54,40,050 over Rs 2,10,00,000 is 25.9 percent, so the base is already Q1.",
                  "c": "both sides count booked orders, so the definition is the same on each.",
                  "d": "both totals are exact to the rupee."},
                 "Marketing's slide sets the Q2 dashboard tile, Rs 1,55,59,950 read on 15 September, against all "
                 "of Q1, Rs 2,10,00,000, and reports a fall of 25.9 percent.",
                 "scenario"),
            item("What does revenue per week give on 15 September, and what does it miss?",
                 "On 15 September, with Q2 still open, a colleague turns both sides of Marketing's slide into "
                 "revenue per week, each side divided by the weeks its dates cover. What does the rate give, and "
                 "what does it still miss?",
                 ["Minus 12.4 percent, and it still compares Q2's early weeks with the whole of Q1",
                  "Minus 25.9 percent, since dividing both sides by weeks leaves their ratio alone",
                  "Minus 11.0 percent, since a rate per week removes every difference in the windows",
                  "Minus 17.0 percent, the answer that matched weeks of each quarter would give"], "a",
                 "Rs 16,15,385 a week against Rs 14,14,541 is minus 12.4 percent. A rate evens out the length of "
                 "the two windows and leaves their position as it was, so Q2's first eleven weeks still stand "
                 "against all of Q1. While Q2 is open the same 11 weeks of each quarter fit better, and the two "
                 "disagree here (minus 17.0) because a few lakh-sized orders make weeks lumpy.",
                 {"b": "dividing one side by 13 and the other by 11 changes the ratio by 13 over 11.",
                  "c": "11.0 percent is the closed quarters' figure, which needs Q2 to have closed.",
                  "d": "the same weeks give minus 17.0 because Kalpa's weeks are lumpy, so the two methods "
                       "disagree on this file."},
                 "On 15 September, with Q2 still open, a colleague divides each side of Marketing's slide by the "
                 "weeks its dates cover.",
                 "design"),
            item("Which comparison answers Meera's question about the monsoon, and what does it need?",
                 "Both quarters have closed. Meera now asks: \"Is Q2 always weaker than Q1, because of the "
                 "monsoon?\" Which option answers her, and what does it need?",
                 ["Closed quarters again, since both are complete and compare like with like",
                  "A rate per day, since it removes the one-day gap between 91 and 92 days",
                  "The same 11 weeks of each quarter, since it also matches position",
                  "The same quarter last year, which needs last year's export to run"], "d",
                 "Only a comparison with the same season a year earlier takes the season out. The file holds "
                 "April to September of one year, so the answer needs a data request.",
                 {"a": "closed quarters fix the length, and the two quarters are still different seasons.",
                  "b": "a rate per day evens out the length of the quarters and leaves the season in.",
                  "c": "matched weeks fix the position inside a quarter, and Q1 and Q2 are still different "
                       "seasons."},
                 "With both quarters closed, Meera asks whether Q2 is always weaker than Q1 because of the "
                 "monsoon.",
                 "design"),
            item("In which order do the four moves that test the drop run?",
                 "Four moves answer \"is the drop real\": p) compute the change, q) find the first and last order "
                 "date of each window, r) state the definition and the window in the sentence to Meera, s) choose "
                 "closed quarters or matched weeks. Which order is right?",
                 ["s, q, p, r",
                  "q, s, p, r",
                  "q, p, s, r",
                  "q, s, r, p"], "b",
                 "Read the windows, choose a fair pair, compute the change, then state the definition and the "
                 "window in the sentence to Meera.",
                 {"a": "it chooses a pair before anyone has read the dates.",
                  "c": "it computes before choosing the fair pair, which is how the tile's number reached a "
                       "slide.",
                  "d": "it writes the sentence before the number it states exists."},
                 "Four moves test whether the drop is real: compute the change (p), find each window's first and "
                 "last order date (q), state the definition and the window to Meera (r), and choose closed "
                 "quarters or matched weeks (s).",
                 "scenario"),
            item("What does adding revenue by month prove when it matches the closed quarters?",
                 "The second route added revenue by the month in `order_date` and reached the same fall as the "
                 "closed quarters. What does agreement between the two routes prove?",
                 ["That monthly totals are a better headline for Meera than the quarters",
                  "That no order in the file carries a wrong amount or a missing field",
                  "That the quarter field and the dates give each quarter the same total",
                  "That the fall is real and needs no comparison with last year"], "c",
                 "The first route trusted the `quarter` field and the second read only the dates, and both give "
                 "each quarter the same total. That is agreement in aggregate: two mislabelled orders of equal "
                 "value could still cancel out, so an order-by-order check is the stronger proof.",
                 {"a": "the quarter stays the headline, and months are for questions inside a quarter.",
                  "b": "both routes read the same amounts, so a wrong amount would fool both.",
                  "d": "the season is still in the comparison, and only last year's Q2 takes it out."},
                 "The second route added revenue by the month in `order_date` and reached the same fall as the "
                 "first route, which added it by the `quarter` field.",
                 "design"),
        ]),
    dict(
        chapter=2, slug="ch2_which_branch",
        question=("Which branch of the revenue tree carries the Rs 23,00,000 fall: customers, how often they "
                  "buy, or what each order is worth?"),
        terms=("Monday's revenue tree splits revenue into three leaves, or branches, that multiply: revenue = "
               "customers x orders per customer x revenue per order. Customers are the distinct customer ids "
               "with an order in the quarter, orders per customer is orders over customers, and revenue per "
               "order is revenue over orders. Each leaf is read as a ratio, Q2's value over Q1's."),
        quote=("Are we losing customers, or are the ones we have buying less? Marketing says more customers.",
               "Meera Raghavan, CEO, Kalpa Retail"),
        so_far=("Chapter 1 confirmed the drop on two closed quarters of 13 weeks each: booked revenue, every "
                "order placed at the price charged before any cancellation or return, fell from Rs 2,10,00,000 "
                "to Rs 1,87,00,000, which is Rs 23,00,000 less and minus 11.0 percent. Frequency is another name "
                "for orders per customer. A bridge walks from Q1's revenue to Q2's one leaf at a time, in a "
                "stated order, and charges each leaf the rupees its own change moved; in the tree's order "
                "customers move first, then orders per customer, then revenue per order. A symmetric split "
                "shares the change among the leaves in proportion to each leaf's logarithmic change, so no "
                "order is chosen. An order may also record a `discount`, the rupees taken off its price."),
        who=("Meera Raghavan, the CEO, decides which owner gets the problem. Marketing owns customers; the "
             "owners of the paid membership tier and of the products own how often customers buy; "
             "merchandising, the team that chooses the range and the pack sizes, owns what each order is "
             "worth; and Finance with Marketing owns price. A wrong split sends crores to the wrong owner for "
             "a quarter, and Marketing's Rs 12 crore to a branch that may not have moved."),
        exhibit="The numbers every item refers to, in booked revenue on the export as it stands:",
        table="""| Branch | Q1 | Q2 | Ratio |
|---|---|---|---|
| Customers | 69 | 69 | 1.000 |
| Orders per customer | 1.65 | 1.25 | 0.754 |
| Revenue per order | Rs 1,84,211 | Rs 2,17,442 | 1.180 |
| Revenue | Rs 2,10,00,000 | Rs 1,87,00,000 | 0.890 |""",
        picture="""flowchart LR
    R["<b>revenue</b><br/>Rs 2.10 cr to Rs 1.87 cr"] --> C["<b>customers</b><br/>69 to 69"]
    R --> F["<b>orders per customer</b><br/>1.65 to 1.25"]
    R --> V["<b>revenue per order</b><br/>Rs 1,84,211 to Rs 2,17,442"]""",
        scenario=("Meera Raghavan, Kalpa Retail's CEO, asked which branch of Monday's revenue tree, revenue = "
                  "customers x orders per customer x revenue per order, carries the Rs 23,00,000 fall in booked "
                  "revenue from Q1 to Q2. Customers stood at 69 in both quarters, orders per customer went from "
                  "1.65 to 1.25, revenue per order from Rs 1,84,211 to Rs 2,17,442, and revenue from "
                  "Rs 2,10,00,000 to Rs 1,87,00,000."),
        items=[
            item("Which reading of the tree answers Marketing's call for more customers?",
                 "Marketing says the fall needs more customers. Which reading of the tree answers them?",
                 ["Customers fell with orders, 114 to 86, so acquisition is the branch to fund",
                  "Customers held at 69, so the fall sits in how often they buy",
                  "Revenue per order rose 18.0 percent, so the fall must sit with customers",
                  "The tree cannot answer until the four segments are split"], "b",
                 "Customers held at 69 in both quarters while orders per customer fell from 1.65 to 1.25, so "
                 "the branch Marketing wants to fund did not move.",
                 {"a": "114 and 86 are orders, rows counted as customers, which was Monday's trap.",
                  "c": "customers held, so a rise in order value cannot put the fall there.",
                  "d": "the tree answers Marketing's claim now, and the segments come in chapter 3."},
                 "Marketing says the fall needs more customers, and the tree shows 69 customers in each quarter, "
                 "114 orders against 86, and revenue per order up 18.0 percent.",
                 "scenario"),
            item("What is wrong with a 6.6 percent fall built from the leaves?",
                 "A colleague adds the leaf changes, minus 24.6 percent and plus 18.0 percent, and reports "
                 "revenue down 6.6 percent. What is wrong?",
                 ["Nothing: the customer leaf adds zero, so minus 24.6 and plus 18.0 net to minus 6.6",
                  "The customer leaf was left out of the sum, and it carries the missing 4.4 points",
                  "The two leaves should be averaged, which puts the fall at 3.3 percent",
                  "The leaves multiply: 0.754 times 1.180 is 0.890, a fall of 11.0 percent"], "d",
                 "Revenue is customers times orders per customer times revenue per order, so the ratios "
                 "multiply. Adding the percentages drops the part where two leaves moved together, the way "
                 "Monday's two 10 percent lifts were called 20 percent when together they make 21.",
                 {"a": "percentage changes on leaves do not add.",
                  "b": "the customer leaf is 1.000 and carries nothing.",
                  "c": "an average of two changes is no quantity in the tree."},
                 "A colleague adds the two leaf changes, minus 24.6 percent in orders per customer and plus 18.0 "
                 "percent in revenue per order, and reports revenue down 6.6 percent.",
                 "scenario"),
            item("Which split of the fall fits Meera, and which fits Finance?",
                 "Meera wants rupees per branch on one slide she can follow, and Finance will rebuild the same "
                 "split every month while two branches keep moving together. Which split fits which reader?",
                 ["The symmetric split for both, since any order of steps is a bias someone will argue",
                  "Leaf percentages for Meera, since she reads percentages, and the bridge for Finance",
                  "The bridge in tree order for Meera, order stated; the symmetric split for Finance",
                  "Customer by customer for both, since it names who moved before anyone adds them up"], "c",
                 "A CEO follows one leaf at a time, so Meera gets the bridge with its order written beside it. A "
                 "split rebuilt every month while two branches move together goes symmetric, so nobody argues "
                 "about the order.",
                 {"a": "Meera loses the one-step reading, and on this quarter every order gives the same verdict.",
                  "b": "percentages do not add, so Meera gets no rupees.",
                  "d": "69 rows before any total answer who moved, which is a different question from which "
                       "branch moved."},
                 "Meera wants rupees per branch on one slide she can follow, and Finance will rebuild the same "
                 "split every month while two branches keep moving together.",
                 "design"),
            item("What does the bridge's frequency step come to in the tree's order?",
                 "Customers stood at 69 in each quarter, orders per customer went from 1.652 to 1.246, and Q1's "
                 "revenue per order was Rs 1,84,211. In the tree's order, what does the bridge's frequency step "
                 "come to?",
                 ["Minus Rs 51,57,895: 69 customers times 0.406 fewer orders at Rs 1,84,211",
                  "Minus Rs 60,88,372: the same fall in frequency priced at Q2's Rs 2,17,442",
                  "Minus Rs 23,00,000, since frequency is the only branch of the three that fell",
                  "Minus Rs 28,57,895, since the order value step takes away the rest of it"], "a",
                 "In the tree's order frequency moves second, with customers already at Q2's 69 and order value "
                 "still at Q1's: 69 times minus 0.406 times Rs 1,84,211, which is 28 fewer orders at Q1's value.",
                 {"b": "pricing the change at Q2's value moves frequency after order value, which is the "
                       "reversed bridge.",
                  "c": "the fall is net of the order value step, which gave back Rs 28,57,895.",
                  "d": "that is the order value step, which added Rs 28,57,895 back."},
                 "With 69 customers in each quarter, orders per customer at 1.652 and then 1.246, and Q1's "
                 "revenue per order at Rs 1,84,211, the bridge in the tree's order moves frequency second.",
                 "design"),
            item("Why is the count of 43 orders without a discount unsafe?",
                 "A hurried count reads every missing discount as zero and finds 43 of Q2's 86 orders \"without "
                 "a discount\". Marketing wants the discount extended to them. Why is the premise unsafe?",
                 ["Q1 had 32 blanks as well, so the offer has to reach both quarters' blank orders",
                  "The 43 hold, but they should be counted by revenue, since orders differ in size",
                  "Blank and Rs 0 both mean no discount, so the 43 hold and only the offer's size is open",
                  "Only 17 of the 43 record Rs 0, and the other 26 never recorded the field"], "d",
                 "A blank is unknown. Reading it as zero files 26 unknown orders under \"no discount\", and the "
                 "extension then spends margin on orders that may already carry one.",
                 {"a": "it keeps reading the blanks as zeros, on more orders.",
                  "b": "changing the weights leaves the blanks read as zeros.",
                  "c": "that is the misreading itself: 26 of the 43 are blanks, which are unknown."},
                 "A hurried count reads every missing discount as zero, finds 43 of Q2's 86 orders without one, "
                 "and Marketing wants the discount extended to them.",
                 "scenario"),
            item("What does the symmetric split show beside the bridge?",
                 "The second route, a symmetric split that chooses no order at all, charged frequency minus "
                 "Rs 55,88,480. Set beside the bridge, what does it show?",
                 ["The bridge understated frequency, so its figure has to be corrected upwards",
                  "Frequency carries the fall either way; the rupees per branch depend on the method",
                  "The two agree to the rupee once the customers step is added back into the bridge",
                  "The gap between them is the customers branch, which only the symmetric split sees"], "b",
                 "An independent split that chooses no order puts the largest fall on the same branch. The "
                 "Rs 4,30,585 between the two frequency figures is the part where frequency and order value "
                 "moved together, which each method shares out in its own way.",
                 {"a": "neither figure is wrong, since the bridge charges the joint part, Rs 4,30,585, to the "
                       "leaf that moves second.",
                  "c": "the customers step is zero in both routes.",
                  "d": "customers held at 69, and the gap is the joint part of frequency and order value."},
                 "The second route, a symmetric split that chooses no order, charges frequency minus "
                 "Rs 55,88,480 against the bridge's minus Rs 51,57,895.",
                 "design"),
        ]),
    dict(
        chapter=3, slug="ch3_which_segment",
        question=("Which of the four customer segments carries the fall in orders per customer, measured the "
                  "same way for every segment and quarter?"),
        terms=("Orders per customer is orders over customers, one of the three branches of Monday's revenue "
               "tree, revenue = customers x orders per customer x revenue per order. Kalpa's customers sit in "
               "four segments. Two appear in the exhibit below: Retail-Core, shoppers who place many small "
               "orders, and Business, Kalpa's sales to companies, a few very large accounts whose every order "
               "runs to lakhs. The other two, the paid membership tier and Student, a segment of small discounted "
               "baskets, are left to your own run."),
        quote=("One of my members says the app's reorder button has been broken for six weeks. Is my tier the "
               "one slipping?", "The head of the paid membership tier, Kalpa Retail"),
        so_far=("Chapter 2 found where the fall sits: the same 69 customers placed 114 orders in Q1 and 86 in "
                "Q2, so orders per customer went from 1.65 to 1.25. Chapter 3 weighed three ways to compute the "
                "same numbers for eight groups, four segments in two quarters: copying the loop once per group, "
                "writing it once as a function, or one pass by key, a single loop that adds every order into a "
                "total kept for its quarter and segment. It wrote the tree once as `tree_for(rows)`, a function "
                "that takes any list of orders and gives its revenue, orders, customers and the two rates, "
                "and a second helper, `describe`, which gives a group's median order, the middle one once the "
                "orders are sorted, its smallest and largest order, and its range, the largest less the "
                "smallest. A roll-up turns the four segments' figures into one company figure. Anand Iyer, "
                "Kalpa's finance controller, keeps a summary table of these numbers."),
        who=("The head of the paid membership tier decides whether his tier needs rescuing. Renewals, the "
             "members who pay for another year, are the metric of his job, so orders per member is his number. "
             "A wrong answer costs a tier nobody protects, or a quarter spent fixing one that was fine."),
        exhibit=("The numbers every item refers to, as the projector showed them, in booked orders on the "
                 "export as it stands:"),
        table="""| Shown on the projector | Customers | Orders Q1, Q2 | Orders per customer Q1, Q2 |
|---|---|---|---|
| Retail-Core | 34 | 38, 36 | 1.12, 1.06 |
| Business | 11 | 20, 17 | 1.82, 1.55 |
| All customers | 69 | 114, 86 | 1.65, 1.25 |""",
        picture="""flowchart LR
    T["<b>orders per customer</b><br/>1.65 to 1.25"] --> A["<b>Retail-Core</b><br/>-5.3%"]
    T --> B["<b>Business</b><br/>-15.0%"]
    T --> C["<b>the rest</b><br/>your run"]""",
        scenario=("The head of Kalpa Retail's paid membership tier asked whether his tier is the one slipping, "
                  "after a member reported the app's reorder button broken for six weeks. Chapter 3 wrote "
                  "Monday's tree once as `tree_for(rows)`, ran it on each of the four customer segments in both "
                  "quarters, and rolled the segments back up to the company's orders per customer, 1.65 in Q1 "
                  "and 1.25 in Q2, from 114 and 86 orders by the same 69 customers."),
        items=[
            item("Which way should compute the same numbers for eight groups and for the asks due later today?",
                 "Copying the loop takes 72 lines and 8 places to edit, a function 21 lines and 1 place, and one "
                 "pass by key 14 lines and 1 place, shaped for these eight groups. A channel, a month and "
                 "delivered orders are asked for later today. Which is the best fit?",
                 ["Copy the loop per group, since each copy can be checked on its own",
                  "One pass by key, since it is the shortest code and reads the rows once",
                  "A spreadsheet, since eight groups are few enough to total by hand",
                  "A function, tree_for(rows), since each later subset is one more call"], "d",
                 "The later asks are new subsets of orders, and a function answers any list of orders with one "
                 "call; one pass by key would need a new loop for each new key.",
                 {"a": "eight places to edit when the definition changes, and one gets forgotten.",
                  "b": "it is the shortest today, and a channel or a month needs a new loop.",
                  "c": "a hand total cannot be rerun on delivered orders this afternoon."},
                 "Copying the loop takes 72 lines and 8 places to edit, a function 21 lines and 1 place, one pass "
                 "by key 14 lines and 1 place but shaped for these eight groups, and a channel, a month and "
                 "delivered orders are asked for later today.",
                 "design"),
            item("How many rows does filtering once per group read on 40 lakh orders?",
                 "Suppose next quarter's export holds 40 lakh orders, and Anand wants all 40 segment-and-month "
                 "groups every Monday. Filtering the export once per group and totalling each group reads how "
                 "many rows, against one pass by key?",
                 ["16 crore rows against 40 lakh, so one pass by key takes over",
                  "40 lakh either way, since each group's total reads only its own rows",
                  "16 crore against 40 lakh, and filtering stays, since each group is easy to check",
                  "1,600 rows against 200, the same gap as on today's file"], "a",
                 "Each filter reads the whole export, 40 times over, while one pass reads it once and fills every "
                 "group. That volume is the fact the chapter named for switching to one pass by key.",
                 {"b": "that holds only once something has split the rows by group, which is itself a pass by "
                       "key.",
                  "c": "one pass by key checks just as well group by group, and it reads the export once.",
                  "d": "that is today's 200-row file, where speed decides nothing."},
                 "Suppose next quarter's export holds 40 lakh orders and Anand wants all 40 segment-and-month "
                 "groups every Monday; the item sets filtering once per group against one pass by key.",
                 "design"),
            item("Why does Anand's summary table show a blank where the helper shows 1.65?",
                 "Anand's summary table shows a blank for Q1 orders per customer, although calling the helper that "
                 "computes it on its own in a cell shows 1.65 under it. What went wrong?",
                 ["The table was filled before the helper ran, so it still holds an old blank",
                  "The helper rounds 1.652 to 1.65, and the table will not take a rounded value",
                  "The helper printed its answer and returned nothing, so the table got None",
                  "The helper returned from inside its loop, before the last order was counted"], "c",
                 "`print` shows the value on screen and hands back None, so a table built from the call holds "
                 "None, which shows as a blank.",
                 {"a": "rerunning the table would fix that, and the blank stays.",
                  "b": "a table holds any number, rounded or not.",
                  "d": "an early return hands back a wrong number, never a blank."},
                 "Anand's summary table shows a blank for Q1 orders per customer, although the helper called on "
                 "its own in a cell shows 1.65.",
                 "scenario"),
            item("What does a weighted roll-up of the four segments give?",
                 "Averaged over the four segments, orders per customer reads 1.94 then 1.82, a fall of 6.0 "
                 "percent. The four segments hold 69 customers, who placed 114 orders in Q1 and 86 in Q2. What "
                 "does the roll-up with weights give?",
                 ["1.94 to 1.82, since the weights cancel out once all four segments are counted",
                  "1.65 to 1.25, a fall of 24.6 percent, so frequency is the branch after all",
                  "1.65 to 1.25, a fall of 32.0 percent, measured against the Q2 figure",
                  "0.61 to 0.80, total customers over total orders in each quarter"], "b",
                 "Total orders over total customers weights each segment by its customers: 114 over 69 and 86 "
                 "over 69, minus 24.6 percent, which reproduces chapter 2's figure.",
                 {"a": "weights cancel only when every segment is the same size.",
                  "c": "32.0 percent is the change measured against Q2.",
                  "d": "that is the reciprocal, customers per order."},
                 "Averaged over the four segments, orders per customer reads 1.94 then 1.82, minus 6.0 percent, "
                 "while the four segments hold 69 customers who placed 114 orders in Q1 and 86 in Q2.",
                 "scenario"),
            item("What happened to the typical Business order in Q2?",
                 "Business revenue fell Rs 22,29,720 on three fewer orders. `describe` shows the median Business "
                 "order barely moved while the range rose about 73 percent. What do you say about the typical "
                 "Business order?",
                 ["It held: one very large order stretched the range; the fall is three fewer orders",
                  "It grew, since a range up 73 percent means the middle of the orders moved up too",
                  "It shrank, since revenue fell by Rs 22 lakh while the count moved by only three",
                  "It is the mean here, since a median ignores the lakh-sized orders that matter most"], "a",
                 "The median is the typical order, and it barely moved. The range is set by the two extreme "
                 "orders, and one very large order widened it, while the rupee fall is three orders worth lakhs "
                 "each.",
                 {"b": "it reads a spread as a level.",
                  "c": "three orders at about Rs 10 lakh each come to about Rs 30 lakh, so the count carries the "
                       "fall.",
                  "d": "the mean is what one large order pulls, and the median is the typical order."},
                 "Business revenue fell Rs 22,29,720 on three fewer orders, and `describe` shows the median "
                 "Business order barely moved while the range rose about 73 percent.",
                 "scenario"),
            item("In which order does the roll-up of the four segments run?",
                 "Anand asks for the company's orders per customer rolled up from the four segments. Order the "
                 "steps: p) divide total orders by total customers, q) compute each segment's orders and "
                 "customers in each quarter, r) check the result against the company figure from chapter 2, "
                 "s) add the segments' orders and their customers. Which order is right?",
                 ["q, p, s, r",
                  "s, q, p, r",
                  "q, s, r, p",
                  "q, s, p, r"], "d",
                 "Compute each segment's counts, add them, divide the totals, then check that the roll-up "
                 "reproduces the company figure.",
                 {"a": "it divides before there are totals to divide.",
                  "b": "it adds counts that have not been computed yet.",
                  "c": "it checks a result before the result exists."},
                 "Anand asks for the company's orders per customer rolled up from the four segments, from four "
                 "steps: divide the totals (p), compute each segment's counts (q), check against chapter 2's "
                 "company figure (r), and add the segments' counts (s).",
                 "scenario"),
        ]),
    dict(
        chapter=4, slug="ch4_mix_or_rate",
        question=("Revenue per order rose 18 percent while revenue fell: did customers pay more, or did the mix "
                  "of orders change?"),
        terms=("Revenue per order is revenue over orders, one branch of Monday's revenue tree, and the blended "
               "figure is taken over every order of every segment together. Kalpa has four segments: "
               "Retail-Core, shoppers who place many small orders; Retail-Plus, the paid membership tier; "
               "Student, small discounted baskets; and Business, Kalpa's sales to companies, every order in "
               "lakhs. The first three are the consumer segments."),
        quote=("Revenue per order is up 18 percent. Our customers are happy to pay more. Put a price rise into "
               "the plan.", "The marketing lead, Kalpa Retail"),
        so_far=("Chapter 2 found the same 69 customers in both quarters, orders per customer down from 1.65 to "
                "1.25, and revenue per order up 18.0 percent, from Rs 1,84,211 to Rs 2,17,442, a rise of "
                "Rs 33,231, while booked revenue, every order placed at the price charged before any "
                "cancellation or return, fell 11.0 percent, from Rs 2,10,00,000 to Rs 1,87,00,000. "
                "Chapter 3's run of all four segments found orders per customer fell furthest in Retail-Plus, "
                "where the same 22 members placed 26 orders in Q2 against 51 in Q1. The mix is each segment's "
                "share of the quarter's orders, and a segment's rate is its own revenue per order. Splitting a "
                "change into mix and rate prices Q2's mix at each segment's Q1 rate: what that moves is the mix "
                "part, and the rest, the change inside the segments, is the rate part. A segment's median is its "
                "middle order once the orders are sorted, the typical order."),
        who=("Meera Raghavan, the CEO, and Finance decide whether a price rise goes into the plan, on "
             "Marketing's reading of the 18 percent. A wrong reading raises prices on customers who never paid "
             "more, and costs volume in the tier whose orders already halved."),
        exhibit="The numbers every item refers to, in booked orders on the export as it stands:",
        table="""| Segment | Share of orders Q1, Q2 | Revenue per order Q1 | Revenue per order Q2 |
|---|---|---|---|
| Retail-Core | 33.3%, 41.9% | Rs 2,117 | Rs 2,014 |
| Retail-Plus | 44.7%, 30.2% | Rs 2,815 | Rs 3,012 |
| Business | 17.5%, 19.8% | Rs 10,38,559 | Rs 10,90,674 |
| Student | 4.4%, 8.1% | Rs 962 | Rs 1,104 |
| All orders | 114, 86 orders | Rs 1,84,211 | Rs 2,17,442 |""",
        picture="""flowchart LR
    A["<b>Q1</b><br/>Rs 1,84,211"] --> M["<b>mix</b><br/>?"]
    M --> R["<b>rate</b><br/>?"]
    R --> D["<b>Q2</b><br/>Rs 2,17,442"]""",
        scenario=("The marketing lead read the 18.0 percent rise in Kalpa Retail's revenue per order, "
                  "Rs 1,84,211 in Q1 to Rs 2,17,442 in Q2, as customers happy to pay more, and asked for a price "
                  "rise in the plan. Revenue per order is blended over every segment; the mix is each segment's "
                  "share of orders, a segment's rate is its own revenue per order, and pricing Q2's mix at Q1's "
                  "rates separates the mix part of the Rs 33,231 rise from the rate part."),
        items=[
            item("Which reading of the table answers Marketing's price claim?",
                 "Marketing reads the blended rise of 18.0 percent as customers paying more. Which reading of "
                 "the table answers Marketing's price claim?",
                 ["Business rose 5.0 percent, so prices across the range can safely rise 5 percent",
                  "No segment rose 18 percent, so small member orders leaving the blend explain it",
                  "Student rose 14.8 percent, so the students' higher prices explain the blended rise",
                  "Retail-Core fell 4.9 percent, so its prices should be cut to win the orders back"], "b",
                 "The blend rose 18.0 percent while no segment rose that far, because Retail-Plus's small orders "
                 "fell from 44.7 to 30.2 percent of orders and Business's lakh-sized ones rose to 19.8 percent.",
                 {"a": "Business's own rise is 5 percent on its own orders and says nothing about consumer "
                       "prices.",
                  "c": "Student is 8 percent of orders at about a thousand rupees each, too small to move a "
                       "blend of lakhs.",
                  "d": "a fall inside Retail-Core says nothing about the blend's rise."},
                 "Marketing reads the 18.0 percent rise in blended revenue per order as customers paying more, "
                 "and the table gives each segment's share of orders and its revenue per order in both quarters.",
                 "scenario"),
            item("Which reading answers each of four questions about the rise?",
                 "Match each question to the reading that answers it: 1 how big is the rise, 2 did any segment "
                 "pay more, 3 how much of the rise is mix, 4 what is a typical order; P the per-segment rates, "
                 "Q the medians, R the blended change, S the mix-and-rate split. Which pairing holds?",
                 ["1R 2S 3P 4Q",
                  "1S 2P 3R 4Q",
                  "1R 2P 3S 4Q",
                  "1R 2P 3Q 4S"], "c",
                 "The blend gives the size of the rise, the per-segment rates say whether anyone paid more, the "
                 "split puts rupees on the mix, and the median is the typical order.",
                 {"a": "the split cannot say whether a given segment paid more, and the rates cannot size the "
                       "mix.",
                  "b": "the size of the rise is the blend itself, which the split only shares out.",
                  "d": "a median cannot size the mix, and the split says nothing about a typical order."},
                 "Four questions about the rise (its size, whether any segment paid more, how much of it is mix, "
                 "and the typical order) are matched to four readings: the per-segment rates (P), the medians "
                 "(Q), the blended change (R) and the mix-and-rate split (S).",
                 "design"),
            item("When would the per-segment table be enough without a mix split?",
                 "Which fact would make the per-segment table enough without a mix split?",
                 ["A rise in revenue per order larger than the 18 percent seen this quarter",
                  "Segments whose own rates all moved by less than the blend did",
                  "Four segments instead of two",
                  "Segments with similar order sizes, or shares that held still"], "d",
                 "Mix moves the blend only when segments differ in order size and their shares move. Without "
                 "either, the per-segment rates tell the whole story.",
                 {"a": "a bigger rise still needs splitting.",
                  "b": "that is this quarter, where the split was needed to put rupees on the gap.",
                  "c": "the number of segments does not decide whether mix matters."},
                 "Which fact would make the table of each segment's own revenue per order enough, with no mix "
                 "split needed?",
                 "design"),
            item("How much of the Rs 33,231 rise is mix?",
                 "Price Q2's order mix at each segment's Q1 revenue per order, using the table. What does revenue "
                 "per order come to, and how much of the Rs 33,231 rise is mix?",
                 ["Rs 2,07,112, so the mix is Rs 22,902 of the rise, about 69 percent",
                  "Rs 2,07,112, so the mix is Rs 10,330 of the rise, about 31 percent",
                  "Rs 1,93,414, so the mix is Rs 9,203 of the rise, about 28 percent",
                  "Rs 2,17,442, so the mix is all Rs 33,231 of the rise, every rupee"], "a",
                 "Business's share rose from 17.5 to 19.8 percent at about Rs 10.4 lakh an order, which lifts "
                 "the blend to Rs 2,07,112 with no segment's rate moving: Rs 22,902 of the Rs 33,231 rise.",
                 {"b": "Rs 10,330 is the rest, the rate part.",
                  "c": "that prices Q1's mix at Q2's rates, which isolates the rate part.",
                  "d": "Rs 2,17,442 is Q2's actual figure, mix and rate together."},
                 "Q2's order mix is priced at each segment's Q1 revenue per order, to find how much of the "
                 "Rs 33,231 rise, from Rs 1,84,211 to Rs 2,17,442, is mix.",
                 "design"),
            item("Which segment carries most of the rate part?",
                 "The rate part of the rise, what is left once the mix is priced, splits by segment. Which "
                 "segment carries most of it, and why does that matter for the price rise?",
                 ["Retail-Plus, so members did pay noticeably more for each order they placed",
                  "Business, since its lakh-sized orders dominate the rate part",
                  "Retail-Core, so everyday shoppers carry the rise",
                  "Student, whose rate rose most in percentage terms"], "b",
                 "Business's 17 orders each grew about Rs 52,000 on average, so almost all of the rate part is "
                 "Business, while the consumer segments moved by a few hundred rupees at most.",
                 {"a": "Retail-Plus's rise is about Rs 200 an order on 30 percent of orders, about Rs 60 of the "
                       "rate part.",
                  "c": "Retail-Core's rate fell.",
                  "d": "the largest percentage sits on the smallest orders, about Rs 11 of the rate part."},
                 "The rate part of the rise, what is left once the mix is priced, is split by segment to see "
                 "which carries most of it.",
                 "scenario"),
            item("What does a split into Business and everyone else put on the mix?",
                 "The envelope route, a sum small enough for the back of an envelope, treats Kalpa as two "
                 "groups: Business's share of orders rose from 17.5 to 19.8 percent, and a Q1 Business order was "
                 "worth Rs 10,36,125 more than a consumer order. What does it put on the mix, and what does that "
                 "show?",
                 ["About Rs 23,000, within 1 percent of the split, so the call holds however it is cut",
                  "About Rs 23,000, so the four-segment split was out by Rs 137 and needs correcting",
                  "About Rs 2,300, since a 2.2-point move in share moves the blend 2.2 percent at most",
                  "All Rs 33,231, since only Business's share moved while the consumer prices held"], "a",
                 "0.022 times Rs 10,36,125 is about Rs 23,000, against Rs 22,902 from four segments, so an "
                 "independent route that could have disagreed lands within one percent.",
                 {"b": "the two routes differ by what the consumer segments' own mix does, so a small gap is "
                       "expected and is no error.",
                  "c": "the change in share multiplies a gap of lakhs between a Business order and a consumer "
                       "one.",
                  "d": "the rate part, Rs 10,330, is Business's own orders growing, which the envelope leaves "
                       "out."},
                 "The envelope route treats Kalpa as Business and everyone else: Business's share of orders rose "
                 "from 17.5 to 19.8 percent, and a Q1 Business order was worth Rs 10,36,125 more than a consumer "
                 "order.",
                 "design"),
        ]),
    dict(
        chapter=5, slug="ch5_marketings_hypothesis",
        question=("Marketing says the flat count hides customers lost and replaced: were any lost, who slowed "
                  "instead, and which segment fell most?"),
        terms=("A customer is a distinct customer id with an order in the quarter, and churn is a customer who "
               "stops buying. Kalpa's consumer business is its three consumer segments together: Retail-Core, "
               "shoppers who place many small orders; Retail-Plus, the paid membership tier; and Student, small "
               "discounted baskets. Business, Kalpa's sales to companies, runs to lakhs an order."),
        quote=("A flat count can hide churn replaced by new customers. And Retail-Plus is Rs 65,250 out of a "
               "Rs 23 lakh fall.", "The marketing lead, Kalpa Retail"),
        so_far=("Chapter 2 counted 69 customers in each quarter while orders fell from 114 to 86, so orders per "
                "customer went from 1.65 to 1.25, and booked revenue, every order placed at the price charged "
                "before any cancellation or return, fell Rs 23 lakh, from Rs 2,10,00,000 to Rs 1,87,00,000. "
                "Chapter 3's run of the four segments found the steepest fall in orders per "
                "customer in Retail-Plus, where the same 22 members placed 26 orders in Q2 against 51 in Q1, and "
                "chapter 4 found that 25 of the 28 lost orders were Retail-Plus orders of about three thousand "
                "rupees each. Chapter 5 weighed four ways to test the churn claim: comparing the counts; "
                "comparing the two quarters' customer ids as sets, the id overlap; reading the customers one by "
                "one; and asking Marketing's CRM, its customer database, for sign-ups."),
        who=("Meera Raghavan, the CEO, decides whether to release the Rs 12 crore acquisition budget, which "
             "Marketing now rests on churn hiding in a flat count. A wrong answer spends crores replacing "
             "customers who never left, while the ones who slowed keep slowing."),
        exhibit="The numbers every item refers to, in booked orders on the export as it stands:",
        table="""| Measure | Value |
|---|---|
| Customer ids in Q1, in Q2 | 69, 69 |
| Customers who placed fewer orders in Q2 | 23 |
| Consumer revenue, Q1 to Q2 | Rs 2,28,820 to Rs 1,58,540 |
| Business revenue fall | Rs 22,29,720 on 3 fewer orders |""",
        picture="""flowchart LR
    A["<b>Marketing's claim</b><br/>a flat count hides churn"] --> B["<b>Marketing's ask</b><br/>Rs 12 crore for acquisition"]""",
        scenario=("The marketing lead pushed back three ways: a flat count of 69 customers can hide churn, "
                  "customers who stop buying, replaced by new ones; Retail-Plus, the paid membership tier, is "
                  "only Rs 65,250 of a Rs 23 lakh fall; and last quarter's summary script says Business fell "
                  "most. Meera Raghavan, Kalpa Retail's CEO, decides on the Rs 12 crore acquisition budget from "
                  "the answers."),
        items=[
            item("Which test can see churn behind a flat count, and when would it mislead?",
                 "Which test answers \"a flat count hides churn replaced by new customers\" most directly, and "
                 "what would make you distrust it?",
                 ["Count each quarter's customers by segment; a segment whose definition changed",
                  "Ask Marketing's CRM for sign-ups by month; a campaign that ran in both quarters",
                  "Compare the ids in both quarters, only in Q1 and only in Q2; one person with two ids",
                  "Compare the counts under a new definition of customer; a customer who changed segment"], "c",
                 "Only a comparison of ids names the lost and the new separately, since any count is net. If the "
                 "store and the app gave one person two ids, the comparison would invent churn until the ids "
                 "were joined.",
                 {"a": "a count per segment is still net inside each segment.",
                  "b": "sign-ups see new customers only, and from a second system.",
                  "d": "another count is still net."},
                 "Marketing claims a flat count hides churn replaced by new customers, and four tests are "
                 "offered, each with a reason to distrust it.",
                 "design"),
            item("When does a table of all 69 customers become the better fit?",
                 "Marketing's churn claim already has its answer in a few counts. When does a table of all 69 "
                 "customers, one row each, become the better fit?",
                 ["When the next question is who slowed, which three counts cannot name",
                  "When the export holds more than a few hundred customers in a quarter",
                  "When Marketing wants the result in rupees rather than in customers",
                  "When the ids come from two systems that each number customers apart"], "a",
                 "The three counts of the id overlap settle lost and new. The next question, who is buying less, "
                 "needs each customer's orders side by side.",
                 {"b": "a larger file makes the table longer to read and changes nothing about which question "
                       "it answers.",
                  "c": "rupees need order values, which neither test reads.",
                  "d": "split ids break both tests, and they need joining through the CRM first."},
                 "With Marketing's churn claim answered by the id overlap's three counts, the item asks when a "
                 "table of all 69 customers, one row each, becomes the better fit.",
                 "design"),
            item("Which reply answers Marketing on the 23 customers who ordered less?",
                 "Marketing concedes that nobody left, then adds: \"23 customers ordered less, and that is churn "
                 "in all but name.\" Which reply holds?",
                 ["They are right: a customer who orders less is halfway gone, so acquisition gets funded",
                  "Buying less is frequency: all 23 bought in Q2, so the lever is keeping them buying",
                  "Split the 23 by segment first, since churn hides inside segments until they are split",
                  "Leave the 23 out of the customer count, since customers who slow down distort it"], "b",
                 "Churn is a customer who stops buying, and all 23 bought in both quarters. Buying less is the "
                 "frequency branch, which retention work moves and new customers do not.",
                 {"a": "a customer who still buys has not churned, and acquisition adds new people while the 23 "
                       "stay at their slower pace.",
                  "c": "splitting by segment says where the slowing sits and leaves it slowing, which is still "
                       "frequency.",
                  "d": "the 23 are customers in both quarters, so dropping them changes the count and hides the "
                       "fall."},
                 "Marketing concedes that nobody left, then calls the 23 customers who ordered less churn in all "
                 "but name.",
                 "scenario"),
            item("Which fix keeps every segment in Meera's summary?",
                 "Last quarter's summary script prints `summary: {'Retail-Core': -5.3, 'Business': -15.0}` "
                 "because its helper, `pct_change`, returns a value only when the change is 30 percent or less. "
                 "Which fix to the logic keeps every segment in Meera's summary?",
                 ["Raise the threshold to 50 percent, so that fewer of the changes print",
                  "Print the change as well as returning it, so both appear on the screen",
                  "Filter with `if ch < 0`, so that a None is compared with zero as well",
                  "Always hand back a number, and mark large changes in a separate column"], "d",
                 "A function that always returns its number keeps every segment, and the flag no longer depends "
                 "on whether a value came back.",
                 {"a": "a larger change would still vanish.",
                  "b": "it still returns None past the threshold.",
                  "c": "comparing None with a number raises an error in Python 3."},
                 "Last quarter's script prints `summary: {'Retail-Core': -5.3, 'Business': -15.0}` because its "
                 "helper `pct_change` returns a value only when the change is 30 percent or less.",
                 "scenario"),
            item("Does the tier's Rs 65,250 matter in a Rs 23 lakh fall?",
                 "Marketing says Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall, so it does not matter. Using "
                 "the table, which reply holds?",
                 ["They are right in rupees, so the memo leads with Business and footnotes the tier",
                  "Retail-Plus is 93 percent of the consumer business's Rs 70,280 fall",
                  "The tier is 49 percent of the fall, since its orders per member fell 49 percent",
                  "The tier is 3 percent of the fall, so the reorder complaint can wait a quarter"], "b",
                 "Business orders run to lakhs, so a consumer segment is judged against the consumer business: "
                 "Rs 65,250 of the Rs 70,280 fall, 93 percent.",
                 {"a": "the Business rupees rest on three orders, and the behaviour sits in the tier.",
                  "c": "a fall in a rate is not a share of the rupee fall.",
                  "d": "judged against the whole company, a consumer segment always looks small."},
                 "Marketing says Retail-Plus is Rs 65,250 out of a Rs 23 lakh fall, so it does not matter, while "
                 "consumer revenue fell from Rs 2,28,820 to Rs 1,58,540.",
                 "scenario"),
            item("What does each customer's first and last order date add, and where does it stop?",
                 "The second route took each customer's first and last order date in the export and counted who "
                 "first ordered in Q2 or last ordered in Q1: 0 and 0. What does it add, and where does it stop?",
                 ["Nothing new, since it reads the same 69 ids the first route already compared",
                  "It proves that no customer has left Kalpa since the business opened",
                  "It shows which customers slowed, which the overlap cannot see",
                  "The same 0 and 0 from dates alone; new still means new since 1 April"], "d",
                 "It reaches the overlap's answer without the quarter field or any set arithmetic, so it could "
                 "have disagreed. A first order in this export is only the first since 1 April.",
                 {"a": "it reads the dates and never the quarter field, so a mislabelled quarter would split the "
                       "two routes.",
                  "b": "the export covers two quarters.",
                  "c": "who slowed needs each customer's order counts, the table of all 69 customers."},
                 "The second route took each customer's first and last order date in the export and counted who "
                 "first ordered in Q2 or last ordered in Q1: 0 and 0.",
                 "design"),
        ]),
    dict(
        chapter=6, slug="ch6_the_memo",
        question=("How much of the Retail-Plus fall can the broken reorder button explain, and what evidence "
                  "goes in Meera's memo?"),
        terms=("Retail-Plus is Kalpa's paid membership tier, and the reorder button is the button in Kalpa's "
               "app for placing an earlier order again. The member's complaint says the button has been "
               "broken for six weeks; read back from the week the complaint arrived, that puts the break on 25 "
               "August, an assumption every timing test here rests on."),
        quote=("It is the broken reorder button. One of my members says it has been broken for six weeks.",
               "The head of Retail-Plus, Kalpa Retail"),
        so_far=("The morning found booked revenue, every order placed at the price charged before any "
                "cancellation or return, down 11.0 percent between two closed quarters, from "
                "Rs 2,10,00,000 to Rs 1,87,00,000, with the same 69 customers buying in both and orders per "
                "customer down from 1.65 to 1.25. In Retail-Plus the same 22 members placed 26 orders in Q2 "
                "against 51 in Q1, and chapter 5 found 18 of the 23 customers who slowed were members. "
                "Retail-Core, shoppers who place many small orders, is the comparison segment, a segment the button "
                "cannot touch. A pace is orders per day or per week. "
                "A ceiling is the most a cause could explain, given what else was already moving. A hypothesis "
                "is a named cause stated with the evidence that would settle it."),
        who=("The head of Retail-Plus and engineering decide what to fix first, and Meera Raghavan, the CEO, "
             "decides what the board hears as the cause. Blame the button for everything and the tier keeps "
             "falling for a reason nobody looked for; dismiss it and members keep failing to reorder."),
        exhibit="The numbers every item refers to, Retail-Plus's booked orders on the export as it stands:",
        table="""| Retail-Plus window | Days | Orders | Orders per week |
|---|---|---|---|
| Q1, 1 Apr to 30 Jun | 91 | 51 | 3.92 |
| Q2, 1 Jul to 24 Aug | 55 | 18 | 2.29 |
| Q2, 25 Aug to 30 Sep | 37 | 8 | 1.51 |""",
        picture="""flowchart LR
    A["<b>1 Apr</b><br/>Q1 opens"] --> B["<b>1 Jul</b><br/>Q2 opens"]
    B --> C["<b>25 Aug</b><br/>the button breaks"]
    C --> D["<b>30 Sep</b><br/>Q2 closes"]""",
        scenario=("The head of Retail-Plus, Kalpa Retail's paid membership tier, blames the fall in his members' "
                  "orders on the app's reorder button, broken for six weeks by one member's account, which puts "
                  "the break on 25 August. The tier's members placed 51 orders in Q1, then 18 between 1 July and "
                  "24 August and 8 from 25 August to 30 September, and Meera Raghavan, the CEO, wants a memo on "
                  "what the data can and cannot say about the cause."),
        items=[
            item("Which plan of tests fits the memo due tonight?",
                 "The memo is due tonight. Four tests are on the table: A, before and after the break (the "
                 "tier's 77 orders, minutes); B, Retail-Core as a comparison (151 orders, minutes); C, the tier "
                 "by channel (77 orders, minutes); D, the app's reorder logs (a request, days away). Which plan "
                 "fits?",
                 ["D first, since it settles the question, then A to C if the logs run late",
                  "A alone, since timing already shows the fall began before the break",
                  "A, B and C tonight in that order, and the request for D sent today",
                  "B, C and D, since the complaint already dates the break for us"], "c",
                 "Each cheap test can rule a cause in or out tonight from the export already open, timing first "
                 "since a cause cannot come after its effect. Only the logs settle it, so the request for them "
                 "goes today and the memo does not wait for them.",
                 {"a": "the memo waits days while three tests sit unrun.",
                  "b": "timing caps the button and says nothing about the season or the channel.",
                  "d": "the complaint gives a date, and testing it against the fall's timing is the first test."},
                 "The memo is due tonight, and four tests are on the table: before and after the break (A), "
                 "Retail-Core as a comparison (B) and the tier by channel (C), each minutes on the export, and "
                 "the app's reorder logs (D), a request days away.",
                 "design"),
            item("What is wrong with the hurried memo's 25 orders?",
                 "The hurried memo says the button cost 25 orders and Rs 65,250. What is wrong with the figure?",
                 ["It uses booked orders instead of the delivered orders the board pack counts",
                  "It should be measured in members, 22 in both quarters, and not in orders",
                  "It counts only the 13 and 8 app orders, leaving out the web and the store",
                  "It charges the button with about eight weeks of losses from before it broke"], "d",
                 "Q1 against all of Q2 takes in 1 July to 24 August, when the tier's pace had already fallen to "
                 "2.29 orders a week.",
                 {"a": "the definition is the same in both quarters.",
                  "b": "orders are the right unit for a reorder button, and the members did not change.",
                  "c": "it counts every channel."},
                 "The hurried memo charges the button with 25 orders and Rs 65,250, the tier's whole fall from "
                 "Q1's 51 orders to Q2's 26.",
                 "scenario"),
            item("At most how many orders can the button explain?",
                 "The tier placed 18 orders in the 55 days before the break and 8 in the 37 days after it. At "
                 "most how many orders can the button explain?",
                 ["About 10, since 18 orders came before the break and 8 came after it",
                  "About 4: the pre-break pace gives about 12.1 in 37 days, and 8 came",
                  "About 25, the tier's whole fall from Q1's 51 orders to Q2's 26",
                  "About 12, the 12.1 orders the pre-break pace predicts after the break"], "b",
                 "18 orders in 55 days is 0.327 a day, about 12.1 in the 37 days after the break. The tier placed "
                 "8, so about 4.1 orders is the most the button can explain, and it is a ceiling, since anything "
                 "else still worsening would claim part of it.",
                 {"a": "it compares windows of 55 and 37 days, chapter 1's trap.",
                  "c": "it charges the button with the fall that came before it broke.",
                  "d": "12.1 is what was expected, and 8 of those came."},
                 "The tier placed 18 orders in the 55 days before the break and 8 in the 37 days after it.",
                 "design"),
            item("Which cause does Retail-Core's 95 percent rule out?",
                 "Retail-Core kept 95 percent of its Q1 orders and Retail-Plus 51 percent. Which cause does this "
                 "rule out?",
                 ["A season that hit every customer alike",
                  "Any change in the tier's benefits in July",
                  "The reorder button",
                  "A monsoon dip that hit members harder"], "a",
                 "A season that hit everyone would have moved Retail-Core too. A season that hit members harder "
                 "still fits, and last year's Q2 by segment tests it.",
                 {"b": "a change to the tier touches members only and fits the pattern.",
                  "c": "the comparison segment says nothing about the button.",
                  "d": "that version of the season survives the test."},
                 "Retail-Core kept 95 percent of its Q1 orders and Retail-Plus 51 percent.",
                 "scenario"),
            item("Which evidence goes with each of the memo's two hypotheses?",
                 "The memo names two hypotheses. Which pairing of hypothesis and evidence is right?",
                 ["The button with the tier's change log, and a July change with the app's reorder logs",
                  "The button with Retail-Core's orders by week, and a July change with the tier's channels",
                  "The button with the tier's renewals, and a July change with the app's release date",
                  "The button with the reorder logs, and a July change with the tier's change log"], "d",
                 "Each hypothesis is settled by data the export does not carry, and no two share their evidence: "
                 "the reorder logs test the button, and the tier's change log tests a change for members in "
                 "July.",
                 {"a": "the pairs are swapped.",
                  "b": "both are cuts of this export, which can cap a cause and cannot settle it.",
                  "c": "renewals and a release date each belong with the other hypothesis."},
                 "The memo names two hypotheses, the button after 25 August and a change for members in July, "
                 "and each needs its own evidence.",
                 "design"),
            item("What does a pace corrected by Retail-Core's change show?",
                 "The second route scales the tier's pre-break pace by Retail-Core's own change in pace across "
                 "the break, 0.946, before comparing with what the tier placed after it. What does it show?",
                 ["About 3.5 orders, inside the ceiling, as part of the dip hit Retail-Core too",
                  "About 11.5 orders, the button's full cost once the season is taken out",
                  "The ceiling was wrong, since the two routes differ by about 0.6 orders",
                  "The button explains nothing at all, since Retail-Core also slowed after 25 August"], "a",
                 "11.45 orders expected against 8 placed is about 3.5, an independent correction that lands "
                 "under the ceiling of about 4, which is what a ceiling predicts.",
                 {"b": "11.5 is the corrected expectation, of which 8 came.",
                  "c": "a lower figure from a stricter route is what a ceiling predicts, so it is no error.",
                  "d": "Retail-Core slowed about 5 percent, far less than the tier."},
                 "The second route scales the tier's pre-break pace by Retail-Core's own change in pace across "
                 "the break, 0.946, and compares it with the 8 orders the tier placed after the break.",
                 "design"),
        ]),
]


def words(text):
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) >= 4 and w not in STOP}


def heading_points(it):
    """Words in the heading that only one option uses and the stem does not carry."""
    head, stem = words(it["heading"]), words(it["stem"])
    found = []
    for n, opt in enumerate(it["options"]):
        own = words(opt) - set().union(*(words(o) for m, o in enumerate(it["options"]) if m != n))
        found += sorted((head & own) - stem)
    return found


def lone_longest(opts, key):
    lengths = [len(o) for o in opts]
    k = LETTERS.index(key)
    return lengths[k] == max(lengths) and lengths.count(max(lengths)) == 1


def clean(text, where):
    """Refuse a dash, the rupee glyph or a banned word anywhere a learner reads."""
    assert "\u2014" not in text and "\u2013" not in text, (where, "dash")
    assert "\u20b9" not in text, (where, "rupee glyph")
    for b in BANNED:
        flags = re.IGNORECASE if b[0].islower() else 0
        assert not re.search(r"\b" + b + r"\b", text, flags), (where, b)


def design_line(design, total):
    if not design:
        return f"None of the {NUMBER_WORDS[total].lower()} items is a design item."
    listed = ", ".join(str(d) for d in design[:-1]) + (" and " if len(design) > 1 else "") + str(design[-1])
    return f"{NUMBER_WORDS[len(design)]} of the {NUMBER_WORDS[total].lower()} items are design items: {listed}."


def write_set(s):
    n, items = s["chapter"], s["items"]
    k = len(items)
    design = [i + 1 for i, it in enumerate(items) if it["kind"] == "design"]
    answers = " ".join(f"{i + 1}{it['key']}" for i, it in enumerate(items))
    assert answers == MERGED[n], (n, answers, MERGED[n])
    keys = collections.Counter(it["key"] for it in items)
    assert max(keys.values()) <= k // 2, (n, keys)
    assert s["question"].endswith("?"), n

    stu = [f"# {s['question']}", "",
           f"Chapter {n} set, {k} items, about ten minutes alone after chapter {n}, {KAVYA} {s['terms']}", "",
           f"> \"{s['quote'][0]}\"", ">", f"> {s['quote'][1]}", "", s["so_far"], "",
           f"**Who needs the answer.** {s['who']}", "",
           "**The questions on the way.**", ""]
    stu += [f"- {it['heading']}" for it in items]
    stu += ["", s["exhibit"], "", s["table"], "", "```mermaid", s["picture"], "```", "", RULES, "",
            f"**What you post.** One line of {k} letters in item order, no spaces, in this shape:", "",
            "```", "Post exactly this shape: " + "x" * k, "```", "", "---"]

    sol = [f"# Solution: {s['question']}", "", f"Answers: {answers}", "", s["scenario"], "",
           design_line(design, k)]

    for i, it in enumerate(items, 1):
        opts, key = it["options"], it["key"]
        where = (n, i)
        assert len(opts) == 4 and key in LETTERS, where
        assert it["heading"].endswith("?") and it["stem"].rstrip().endswith("?"), where
        assert not heading_points(it), (where, heading_points(it))
        assert not lone_longest(opts, key), (where, [len(o) for o in opts])
        assert set(it["others"]) == set(LETTERS) - {key}, where
        head = f"### Q{i}. {it['heading']}" + (" (Design)" if it["kind"] == "design" else "")
        stu += ["", head, "", it["stem"], ""]
        stu += [f"{l}) {o}" for l, o in zip(LETTERS, opts)]
        sol += ["", head, "", it["short"], "",
                f"The key is {key}, \"{opts[LETTERS.index(key)]}\". {it['why']}", ""]
        sol += [f"- {l}, \"{o}\": {it['others'][l]}" for l, o in zip(LETTERS, opts) if l != key]

    student, solution = "\n".join(stu) + "\n", "\n".join(sol) + "\n"
    for text, name in ((student, "set"), (solution, "solution")):
        clean(text, (n, name))
        if n <= 3:
            # The room finds the segment in its own run at the end of chapter 3, so no file up to
            # chapter 3 prints the tier's name.
            assert "Retail-Plus" not in text, (n, name, "names the tier before chapter 4")
    (UNG / f"C2_W01_D02_{s['slug']}_STUDENT.md").write_text(student, encoding="utf-8")
    (SOL / f"C2_W01_D02_{s['slug']}_solution_STUDENT.md").write_text(solution, encoding="utf-8")
    return k, len(design)


if __name__ == "__main__":
    total = designs = 0
    for s in SETS:
        a, b = write_set(s)
        total += a
        designs += b
    print(f"{total} items across six chapter sets, {designs} of them design items")
