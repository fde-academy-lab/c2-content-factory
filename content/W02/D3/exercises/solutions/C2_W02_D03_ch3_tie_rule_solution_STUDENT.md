# Which answers hold in the chapter 3 set on how many a list ships at a tie and which rule the head of Retail-Plus asked for, and why?

Answers: 1b 2a 3d 4c 5b

Chapter 3 met the tie. On six invented members ROW_NUMBER gave 1 to 6, RANK 1, 1, 3, 4, 4, 6 and
DENSE_RANK 1, 1, 2, 3, 3, 4. On an invented top four with a tie at fourth the four rules shipped 4, 5,
5 and 3. On Kalpa, Retail-Core's top fifty shipped 50 under ROW_NUMBER, RANK and whole ties only and 52
under DENSE_RANK, because two ties inside the list, on Rs 4,540 and on Rs 4,120, left its numbers two
behind the members; nobody ties at Retail-Core's line, where the fiftieth member booked Rs 2,980 and the
51st Rs 2,950. The call is RANK, with its count and its reason in the report, and a hard cap is the fact
that makes ROW_NUMBER with a tiebreaker stated in advance honest. Counting the members at or above the
fiftieth member's figure reached RANK's count with no window. Two of the five items are design items: 4
and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. The head of
Retail-Plus defends every count to the tier's members, so a count you cannot explain in one sentence
is one the head cannot defend.

**The questions on the way.**

- Which idea does this set test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this set test?

A tie rule is a business choice about who is on a list, and each rule's count follows from where the
ties sit. The items ask for the three functions' numbers on a tie, the count each rule ships at a line,
the reason DENSE_RANK runs long when ties sit above the line, the rule and report that fit a hard cap,
and a route to the head's count that uses no window.

## Why is each key right, item by item?

### Q1. Which DENSE_RANK column comes back for the seven invented members?

Kind: predict the output, on invented numbers.

The key is b, "1, 1, 2, 3, 3, 3, 4". DENSE_RANK numbers the different spend figures: Rs 8,400 is the
first, Rs 7,950 the second, Rs 6,200 the third and Rs 5,100 the fourth, so X ends on 4 while standing
seventh among the members.

- a, "1, 1, 3, 4, 4, 4, 7": RANK's column, which skips the numbers a tie uses up.
- c, "1, 2, 3, 4, 5, 6, 7": ROW_NUMBER's column, which gives every member a number of their own.
- d, "1, 1, 2, 3, 3, 3, 7": dense numbers down to W and then X's place among the members; a dense
  number never jumps.

### Q2. How many members does each rule ship for a top five of the seven?

Kind: predict the number, on invented numbers.

The key is a, "5, 6, 7 and 3". ROW_NUMBER ships exactly five. RANK gives U, V and W fourth place, inside
the line, so six ship. DENSE_RANK's largest number is 4, so all seven ship. Under whole ties only, the
tie of U, V and W reaches place 4 + 3 - 1 = 6, past the line, so all three drop and R, S and T ship.

- b, "5, 6, 6 and 3": stops DENSE_RANK at six members, where its numbers reach only 4 and every member
  is inside five.
- c, "5, 5, 7 and 4": cuts RANK at five, where a tie inside the line ships whole, and keeps one of the
  tied three under whole ties only, which keeps a tie whole or not at all.
- d, "5, 6, 7 and 6": counts the tie that straddles the line as if it fitted.

### Q3. What explains DENSE_RANK's 42 on a Retail-Core top forty, and what does the head's rule ship?

Kind: spot the plausible wrong output.

The key is d, "The ties at 31 and 37 each cost DENSE_RANK a number, so its 40 lands on place 42; RANK
ships 40". Up to place 30 the dense numbers match the places. The pair on Rs 4,540 shares dense number
31, so place 33 is dense 32; the pair on Rs 4,120 shares another, so place 39 is dense 37 and place 40
dense 38, and dense 40 falls on place 42, C-0118 on Rs 3,590. RANK's fortieth is C-0108 on Rs 3,980, and
the 41st, C-0066, booked Rs 3,960, so RANK ships exactly forty. DENSE_RANK adds C-0066 and C-0118, two
calls nobody planned.

- a, "Two members tie at fortieth place, so both carry 40 under every rule, and RANK ships 42 as well":
  place 40 booked Rs 3,980 and place 41 Rs 3,960, so nobody ties at the line.
- b, "DENSE_RANK counts a member with two Q2 orders as two rows, and RANK ships 40, one row per member":
  every function here numbers one row per member; the orders column plays no part.
- c, "Places 41 and 42 tie with each other, and a tie always ships whole, so RANK ships 42 as well":
  places 41 and 42 booked Rs 3,960 and Rs 3,590.

### Q4. Which rule and which report fit thirty-one call slots for Retail-Core?

Kind: a design item, the fact that switches the rule, applied with its report.

The key is c, "ROW_NUMBER with more Q2 orders first, stated in advance: 31 ship, and the report names
C-0132". Thirty-one slots is a hard cap, so the list cannot stretch to hold the tie. A tiebreaker the
business states before the run, and can defend, keeps C-0044, who placed three Q2 orders, over C-0132,
who placed two, which suits a programme worried about how often members order. The report names
C-0132 and the reason, so they head next week's calls.

- a, "RANK, which ships 32 members, and the team finds a thirty-second slot somewhere later in the
  week": keeps both members and breaks the cap the item set.
- b, "Whole ties only, which ships 30, leaves both members on Rs 4,540 off and keeps one slot unused":
  drops two members who earned their places and wastes a call, the forty-nine the head refused, at a
  smaller line.
- d, "ROW_NUMBER with the customer id deciding: 31 ship, C-0044 stays on their lower id, nothing to
  report": the same thirty-one today, chosen by a reason nobody can defend, and C-0132 is never told
  why they were left off.

### Q5. Which route reaches the head's count for a top thirty-seven with no window, and what does it give?

Kind: a design item, the independent second route.

The key is b, "Count the members who booked at least the thirty-seventh member's Rs 4,120: 38". A sort
with `OFFSET 36` finds the thirty-seventh member's figure, Rs 4,120, and every member at or above it
counts. C-0121, at place 38, booked the same Rs 4,120, so C-0121 counts, exactly as RANK ships both members
of the tie. The route uses a sort and a comparison, so a slip in a window's PARTITION BY or ORDER BY
could not move it. In chapter 3 the same route gave Retail-Core's top fifty 50, at the fiftieth
member's Rs 2,980.

- a, "Count the different Q2 figures at or above the thirty-seventh member's Rs 4,120: 36": counts
  figures, DENSE_RANK's logic; places 1 to 38 hold 36 different figures.
- c, "Count the members who booked more than the thirty-seventh member's Rs 4,120: 36": "more than"
  drops both members on the line's own figure.
- d, "Rerun the list with `rank()` in a window and count the rows it ships: 38": the right number
  through a window, which the item rules out, since it shares the code it should check.

## Which wrong answer is worth arguing about?

Item 4, option d. It keeps the same thirty-one members as the key on this week's numbers, so a room
can argue that the result is what matters. The head of Retail-Plus has to say why C-0132 was left off,
and "their id was higher" is a reason no member accepts, while "C-0044 ordered more often this quarter"
is one the head can repeat. The report has to name who the cap left off, so
the member team can start next week with them.

## Where does this show up at work?

American Airlines gives its limited upgrade seats to AAdvantage members in a stated order: status
tier, then the type of upgrade, then Loyalty Points earned in the last 12 months, and "If the upgrade
type and 12-month Loyalty Point value are the same, we'll look at the booking code then date / time of
the request to determine priority" (aa.com, upgrades for status members, checked 1 October 2026). That
is item 4's hard cap with its tiebreaker written down in advance. In the Tokyo
2020 men's high jump final on 1 August 2021, Barshim of Qatar and Tamberi of
Italy both cleared 2.37 m and shared the gold, and Nedasekau of Belarus was placed third, with no
silver awarded (World Athletics results, checked 1 October 2026), which is RANK's 1, 1 and 3.
