# Which answers hold in the guided build of the three ranking functions and the head of Retail-Plus's rule, and why?

Answers: 1b 2d 3a 4c 5b

The guided build set ROW_NUMBER, RANK and DENSE_RANK side by side, first on an invented top four with a
tie at the line, the last place a list keeps, then on six invented members, then on Retail-Core's top
fifty, and closed on the sentence the head of Retail-Plus reads. The five items ask what each step
returns before it runs, and this file also carries what each step prints. None of them is a design
item: the guided build is the one place in chapter 3 where the trainer chooses every step, and the
design items sit in the chapter set and the two cases.

**Who needs the answer.** You need it after chapter 3, to check five letters. The head of Retail-Plus
will ask of any list which rule made its count, and the answer is one of the three functions and a
sentence.

**The questions on the way.**

- What does the guided build test about how three functions number one tie?
- Why is each guided-build key right, and each other letter wrong?
- Why is item 5's sentence under whole ties only worth arguing about?
- Where does reading a tie rule from a list's count matter at work?

## What does the guided build test about how three functions number one tie?

The three functions read the same ORDER BY and differ only at a tie. ROW_NUMBER gives every row its own
number and breaks a tie by whatever else the ORDER BY names, or arbitrarily if nothing does. RANK gives
tied rows one number and skips the ones they use, and DENSE_RANK gives them one number and skips
nothing, so it numbers distinct values. A list's count follows from which rule cut it and where the
ties sit, and the head's rule, RANK, ships a tie at the line whole and says so.

## Why is each guided-build key right, and each other letter wrong?

### Q1. How many members does each rule ship on an invented top four?

This item asks you to predict four counts on invented numbers.

The key is b, "4, 5, 5 and 3". Step 1 prints one row reading 4, 5, 5 and 3. ROW_NUMBER ships four and
leaves E off, since it breaks a tie by whatever else its ORDER BY names, here the member's name, or
arbitrarily if nothing does. RANK gives D and E fourth place, inside the line, so five ship.
DENSE_RANK gives D and E the number 4 as well, so five ship. Whole ties only finds the tie of D and E reaching place
4 + 2 - 1 = 5, past the line, and drops both, so three ship: the forty-nine the head of Retail-Plus
warned about, at a top four.

- Option a, "4, 4, 4 and 4", treats the list as a fixed length whatever the rule, which only ROW_NUMBER
  keeps.
- Option c, "4, 5, 6 and 3", gives DENSE_RANK six, where F's number is 5 and outside the line.
- Option d, "4, 5, 5 and 5", lets whole ties only keep a tie that straddles the line, the one case it
  exists to drop.

### Q2. What does DENSE_RANK give the six invented members?

This item asks you to predict a column on invented numbers.

The key is d, "1, 1, 2, 3, 3, 4". The spend figures are Rs 7,500, Rs 6,000, Rs 5,200 and Rs 4,100, four
distinct values, so DENSE_RANK runs from 1 to 4: A and B share 1, C is 2, D and E share 3 and F is 4.
Step 2 prints `row_number` 1 to 6, with A ahead of B only because the ORDER BY names the member after
the spend and A sorts first; `rank` gives A and B 1 and skips 2, as a race reports a shared first
place; and `dense_rank` never skips, so F's 4 sits two below F's place among the members, 6.

- Option a, "1, 2, 3, 4, 5, 6", is ROW_NUMBER's column, one number per member.
- Option b, "1, 1, 3, 4, 4, 6", is RANK's column, which skips the numbers a tie uses up.
- Option c, "1, 1, 1, 2, 2, 3", puts C with A and B, as if every member above the first gap shared a
  number.

### Q3. How many Retail-Core members does DENSE_RANK put on a top fifty, and why?

This item asks you to predict a count on Kalpa's data with its reason.

The key is a, "52, since ties higher up the list each cost it a number". Step 3 prints 50, 50, 52 and
50 for ROW_NUMBER, RANK, DENSE_RANK and whole ties only. Two pairs inside the list share a figure,
C-0044 and C-0132 on Rs 4,540 at places 31 and 32, and C-0060 and C-0121 on Rs 4,120 at places 37 and
38, so DENSE_RANK's numbers run two behind the members and its 50 lands on the 52nd member.

- Option b, "50, since nobody ties at Retail-Core's fiftieth place", is true of the line and is RANK's
  count; DENSE_RANK's count depends on every tie above the line too.
- Option c, "51, since one tie inside the list costs it one number", misses one of the two ties inside
  the list, so the numbers run two behind.
- Option d, "48, since each tie inside the list takes away one member", has the effect backwards: a tie
  takes away a number, so the list grows past fifty.

### Q4. Which statement about Retail-Core's fiftieth place holds?

This item asks you to read the output of the two blocks that print the members at the line.

The key is c, "Nobody ties at fiftieth, so RANK and ROW_NUMBER ship the same fifty members". Block
`c3_core_line` prints places 46 to 54:

| Place | RANK | DENSE_RANK | Member | Q2 revenue |
|---|---|---|---|---|
| 46 | 46 | 44 | C-0007 | Rs 3,100 |
| 47 | 47 | 45 | C-0127 | Rs 3,030 |
| 48 | 48 | 46 | C-0054 | Rs 3,000 |
| 49 | 49 | 47 | C-0072 | Rs 2,990 |
| 50 | 50 | 48 | C-0005 | Rs 2,980 |
| 51 | 51 | 49 | C-0092 | Rs 2,950 |
| 52 | 52 | 50 | C-0094 | Rs 2,910 |
| 53 | 53 | 51 | C-0048 | Rs 2,870 |
| 54 | 54 | 52 | C-0074 | Rs 2,810 |

The fiftieth member, C-0005, booked Rs 2,980 and the 51st, C-0092, Rs 2,950, so RANK and ROW_NUMBER cut
at the same member and ship the same fifty. Block `c3_core_ties` lists the two pairs inside the first
fifty, on Rs 4,540 at places 31 and 32 and on Rs 4,120 at places 37 and 38.

- Option a, "Two members tie at fiftieth, so RANK ships 51 and ROW_NUMBER drops one by id", misreads
  places 50 and 51, which booked Rs 2,980 and Rs 2,950.
- Option b, "Nobody ties at fiftieth, so DENSE_RANK ships the same fifty members as RANK", forgets the
  ties higher up: DENSE_RANK's 50 falls on C-0094, the 52nd member, so it ships 52.
- Option d, "C-0092 ties with C-0005 at fiftieth, so whole ties only ships forty-nine", reads two
  different figures as one; whole ties only ships fifty here.

### Q5. Which sentence goes to the head of Retail-Plus about Retail-Core's list?

This item asks you to choose the sentence the head reads beside the list.

The key is b, "Retail-Core's list holds 50 under RANK; nobody ties at fiftieth, where C-0005 booked
Rs 2,980." It names the head's rule, the count it ships and the member at the line with their figure,
so the head can repeat it to a member who asks why they are fifty-first.

- Option a, "Retail-Core's list holds 52 under DENSE_RANK, which keeps every tie together, just as you
  asked.", sounds like the head's words and ships two members who tie with nobody.
- Option c, "Retail-Core's list holds 50 under ROW_NUMBER, cut by customer id, so it is the same each
  run.", gives the right count today by the rule the head questioned, which would drop a tied member by
  id.
- Option d, "Retail-Core's list holds 50 under whole ties only, so no tie anywhere on the list is ever
  split.", gives a count that matches here by the rule that ships short of fifty when a tie sits on the
  line, which the head refused.

## Why is item 5's sentence under whole ties only worth arguing about?

Item 5's option d, the sentence naming whole ties only, carries the right number for Retail-Core, since
whole ties only ships the same fifty as RANK there, and a learner can argue that the rule does no harm.
The head of Retail-Plus asked for a rule that holds on every list, including any list where two members
tie on the line, and that is where whole ties only drops both and RANK keeps both. That is why the
sentence to the head names the rule as well as the count.

## Where does reading a tie rule from a list's count matter at work?

Every ranked report that is cut at a number meets a tie sooner or later. A top ten that comes back with
eleven rows is a tie rule at work, and the analyst who can say which rule cut the list, how many it
ships and which members stand at the line answers the stakeholder before the list is questioned.
