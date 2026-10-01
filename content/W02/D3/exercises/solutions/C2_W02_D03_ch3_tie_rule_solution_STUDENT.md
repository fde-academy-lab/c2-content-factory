# Which answers hold in the chapter 3 set on how many a list ships when two members tie at fiftieth place and which rule the head of Retail-Plus asked for, and why?

Answers: 1b 2a 3d 4c 5b

Chapter 3 met the tie. On six invented members ROW_NUMBER gave 1 to 6, RANK 1, 1, 3, 4, 4, 6 and
DENSE_RANK 1, 1, 2, 3, 3, 4. On an invented top four with a tie at fourth the four rules shipped 4, 5,
5 and 3. On Kalpa, Retail-Core's top fifty shipped 50 under ROW_NUMBER, RANK and whole ties only and 52
under DENSE_RANK, because two ties inside the list, on Rs 4,540 and on Rs 4,120, left its numbers two
behind the members. Nobody ties at Retail-Core's line, the last place its list keeps, where the
fiftieth member booked Rs 2,980 and the 51st Rs 2,950. The call is RANK, with its count and its reason
in the report, and a hard cap is the fact that makes ROW_NUMBER with a tiebreaker stated in advance
honest. Counting the members at or above the fiftieth member's figure reached RANK's count with no
window. Two of the five items are design items: 4 and 5.

**Who needs the answer.** You need it to check your five letters after the lab or tonight. The head of
Retail-Plus defends every count to the tier's members, so a count you cannot explain in one sentence
is one the head cannot defend.

**The questions on the way.**

- What does the tie-rule set test about how many members a list ships?
- Why is each tie-rule key right, and each other letter wrong?
- Why is item 4's hard cap worth arguing about?
- Where do real companies decide who goes first when two customers are equal?

## What does the tie-rule set test about how many members a list ships?

A tie rule is a business choice about who is on a list, and each rule's count follows from where the
ties sit. The items ask what a DENSE_RANK number says about a member, the count each rule ships at a
line, the reason DENSE_RANK runs long when ties sit above the line, the business fact that would make
whole ties only the right rule, and a route to the head's count that uses no window.

## Why is each tie-rule key right, and each other letter wrong?

### Q1. Which number does DENSE_RANK give X, and what does that number tell the head?

This item asks you to predict a number on invented members and say what it means.

The key is b, "4, since only three distinct amounts sit above X's". DENSE_RANK gives each new spend
figure the next number and skips nothing: Rs 8,400 is 1, Rs 7,950 is 2, Rs 6,200 is 3 and X's Rs 5,100
is 4. X's 4 therefore says that three distinct amounts sit above X's, and those three amounts belong to
six members.

- Option a, "7, since six members in all spent more than X did", gives a true reason and RANK's number;
  DENSE_RANK gives X 4.
- Option c, "4, since only three members in all spent more than X", gives the right number and the
  wrong reading: R, S, T, U, V and W, six members, spent more than X, on three amounts. Reading a dense
  number as a count of members is the mistake that sends a DENSE_RANK list past its line.
- Option d, "7, since X stands seventh of the seven members ranked", gives X's place among the members,
  which DENSE_RANK does not number.

### Q2. How many members does each rule ship for a top five of the seven?

This item asks you to predict a count on invented members.

The key is a, "5, 6, 7 and 3". ROW_NUMBER ships exactly five, cutting the tie of U, V and W by
whatever else its ORDER BY names, or arbitrarily if nothing does. RANK gives U, V and W fourth place, inside the line, so six ship. DENSE_RANK's largest
number is 4, so all seven ship. Under whole ties only, the tie of U, V and W reaches place 4 + 3 - 1 = 6,
past the line, so all three drop and R, S and T ship.

- Option b, "5, 6, 6 and 3", stops DENSE_RANK at six members, where its numbers reach only 4 and every
  member sits inside five.
- Option c, "5, 5, 7 and 4", cuts RANK at five, where a tie inside the line ships whole, and keeps one of
  the tied three under whole ties only, which keeps a tie whole or not at all.
- Option d, "5, 6, 7 and 6", counts the tie that straddles the line as if it fitted.

### Q3. What explains DENSE_RANK's 42 on a Retail-Core top forty, and what does the head's rule ship?

This item asks you to spot a plausible wrong output and name its cause.

The key is d, "The ties at 31 and 37 each cost DENSE_RANK a number, so its 40 is at place 42; RANK ships
40". Up to place 30 the dense numbers match the places. The pair on Rs 4,540 shares dense number 31, so
place 33 is dense 32; the pair on Rs 4,120 shares another, so place 39 is dense 37 and place 40 dense
38, and dense 40 falls on place 42, C-0118 on Rs 3,590. RANK's fortieth is C-0108 on Rs 3,980, and the
41st, C-0066, booked Rs 3,960, so RANK ships exactly forty. DENSE_RANK adds C-0066 and C-0118, two calls
nobody planned.

- Option a, "Two members tie at fortieth place, so both carry 40 under every rule, and RANK ships 42 as
  well", misreads the table: place 40 booked Rs 3,980 and place 41 Rs 3,960, so nobody ties at the line.
- Option b, "Every tie above the line adds one member to any list that keeps ties, so RANK ships 42 as
  well", is true of DENSE_RANK only. RANK keeps both members of each tie and then skips the numbers they
  used, so by place 33 its number matches the place again; only a tie at the line itself lengthens a
  RANK list.
- Option c, "Places 41 and 42 tie with each other, and DENSE_RANK keeps a tie whole, while RANK ships
  40", gets RANK's count right and the cause wrong: places 41 and 42 booked Rs 3,960 and Rs 3,590, two
  different amounts.

### Q4. Which fact would make whole ties only the right rule for Retail-Core's list?

This is a design item: it asks for the fact that would switch the rule to whole ties only, a fact the
chapter did not name, and the key joins two conditions.

The key is c, "The budget pays for fifty offers at most, and equal spend must get an equal offer". Each
condition removes one of the other rules. RANK keeps equal spend together and can ship more than fifty when a tie
straddles the line, which the budget forbids. ROW_NUMBER keeps to fifty and breaks a tie by whatever
else its ORDER BY names, or arbitrarily if nothing does, so two members on the same figure get
different offers, which the second condition forbids. Whole ties only
never ships past the line and never splits a tie, so it is the one rule that keeps both, at the price
of offers left unspent: on a Retail-Core top thirty-one, where C-0044 and C-0132 share place 31 on
Rs 4,540, it ships 30, where RANK ships 32 and ROW_NUMBER 31.

- Option a, "The member team has fifty call slots this week and cannot make a fifty-first call", is a
  hard cap alone, the chapter's own switch, and it points to ROW_NUMBER with a tiebreaker stated in
  advance, which fills every slot. Whole ties only would leave a slot empty and drop both members of
  any tie that straddles the line.
- Option b, "Retail-Core has no tie at fiftieth, so whole ties only ships the same fifty as RANK", is
  true this quarter and makes the two rules agree today. On any list where a tie straddles the line,
  whole ties only ships forty-nine, the list the head refused.
- Option d, "The head wants every member who booked at least the fiftieth member's figure", describes
  RANK's list, which keeps a tie at the line by keeping both members, where whole ties only drops both.

### Q5. Which route reaches the head's count for a top thirty-seven with no window, and what does it give?

This is a design item: it asks for an independent second route, a different way to the same count, and
the number it gives.

The key is b, "Count the members who booked at least as much as the thirty-seventh member: 38". A sort
with `OFFSET 36` finds the thirty-seventh member's figure, Rs 4,120, and every member at or above it
counts. C-0121, at place 38, booked the same Rs 4,120, so C-0121 counts, exactly as RANK ships both
members of the tie. The route uses a sort and a comparison, so a slip in a window's PARTITION BY or
ORDER BY could not move it. In chapter 3 the same route gave Retail-Core's top fifty 50, at the
fiftieth member's Rs 2,980.

- Option a, "Count the members holding one of the thirty-seven highest distinct figures: 39", counts by
  distinct amount, which is DENSE_RANK's logic: the thirty-seventh distinct amount is Rs 4,070, at place
  39, so the count is DENSE_RANK's 39.
- Option c, "Count the members who booked more than the thirty-seventh member booked: 36", drops both
  members on the thirty-seventh member's own figure, which gives the count whole ties only ships.
- Option d, "Sort the members by Q2 revenue, keep thirty-seven with LIMIT and count them: 37", keeps
  exactly thirty-seven whatever the tie, which is ROW_NUMBER's count, and cuts C-0121, who booked the
  same as C-0060.

## Why is item 4's hard cap worth arguing about?

Item 4's option a, fifty call slots with no fifty-first, is the switch chapter 3 named for ROW_NUMBER,
so a learner who remembers the chapter reaches for it, and whole ties only does keep to fifty. A cap on
its own does not make whole ties only right, because it wastes a slot whenever a tie straddles the line
and drops both members of the tie when the cap had room for one of them; a tiebreaker stated in advance
fills the slot with a reason the head can repeat. Whole ties only becomes the right rule when the
business also promises equal treatment to equal spend, which is the second half of the key.

## Where do real companies decide who goes first when two customers are equal?

American Airlines gives its limited upgrade seats to AAdvantage members in a stated order: status
tier, then the type of upgrade, then Loyalty Points earned in the last 12 months, and "If the upgrade
type and 12-month Loyalty Point value are the same, we'll look at the booking code then date / time of
the request to determine priority" (aa.com, upgrades for status members, checked 1 October 2026). That
is a hard cap with its tiebreaker written down in advance, the chapter's own case for ROW_NUMBER. In the
Tokyo 2020 men's high jump final on 1 August 2021, Barshim of Qatar and Tamberi of Italy both cleared
2.37 m and shared the gold, and Nedasekau of Belarus was placed third, with no silver awarded (World
Athletics results, checked 1 October 2026), which is RANK's 1, 1 and 3.
