# Which answers hold in the guided build of the three ranking functions and the head of Retail-Plus's rule, and why?

Answers: 1d 2b 3a 4c 5b

The guided build put ROW_NUMBER, RANK and DENSE_RANK on one screen, first on six invented members, then
on an invented top four with a tie at the line, then on Retail-Core's top fifty, and closed on the
head of Retail-Plus's rule written as a sentence. The five items ask what each step returns before it
runs. None of them is a design item: the guided build is the one place in chapter 3 where the trainer
chooses every step, and the design items sit in the chapter set and the two cases.

**Who needs the answer.** You, after chapter 3, checking five letters. The head of Retail-Plus will ask
of any list which rule made its count, and the answer is one of the three functions and a sentence.

**The questions on the way.**

- Which idea does this exercise test?
- Why is each key right, item by item?
- Which wrong answer is worth arguing about?
- Where does this show up at work?

## Which idea does this exercise test?

The three functions read the same ORDER BY and differ only at a tie. ROW_NUMBER gives every row its own
number, RANK gives tied rows one number and skips the ones they use, and DENSE_RANK gives them one
number and skips nothing, so it numbers values. A list's count follows from which rule cut it and
where the ties sit, and the head's rule, RANK, ships a tie at the line whole and says so.

## Why is each key right, item by item?

### Q1. What does DENSE_RANK give the six invented members?

Kind: predict the output, on invented numbers. The key is d, "1, 1, 2, 3, 3, 4". The spend figures are
Rs 7,500, Rs 6,000, Rs 5,200 and Rs 4,100, four different values, so DENSE_RANK runs from 1 to 4: A and
B share 1, C is 2, D and E share 3 and F is 4, two below his place among the members.

- a, "1, 2, 3, 4, 5, 6": ROW_NUMBER's column, one number per member.
- b, "1, 1, 3, 4, 4, 6": RANK's column, which skips the numbers a tie uses up.
- c, "1, 1, 1, 2, 2, 3": puts C with A and B, as if every member above the first gap shared a number.

### Q2. How many members does each rule ship at an invented line of four?

Kind: predict the number, on invented numbers. The key is b, "4, 5, 5 and 3". ROW_NUMBER ships four and
leaves E off by the name. RANK gives D and E fourth place, inside the line, so five ship. DENSE_RANK
gives D and E the number 4 as well, so five ship. Whole ties only finds the tie of D and E reaching
place 4 + 2 - 1 = 5, past the line, and drops both: three ship.

- a, "4, 4, 4 and 4": treats the line as a fixed length whatever the rule, which only ROW_NUMBER keeps.
- c, "4, 5, 6 and 3": gives DENSE_RANK six, where F's number is 5 and outside the line.
- d, "4, 5, 5 and 5": lets whole ties only keep a tie that straddles the line, the one case it exists
  to drop.

### Q3. How many Retail-Core members does DENSE_RANK put on a top fifty, and why?

Kind: predict the number on Kalpa. The key is a, "52, since ties higher up the list each cost it a
number". Two pairs inside the list share a figure, Rs 4,540 at places 31 and 32 and Rs 4,120 at 37 and
38, so DENSE_RANK's numbers run two behind the members and its 50 lands on the 52nd member.

- b, "50, since nobody ties at Retail-Core's fiftieth place": true of the line, and it is RANK's count;
  DENSE_RANK's count depends on every tie above the line too.
- c, "51, since one tie inside the list costs it one number": there are two ties inside the list, so
  the numbers run two behind.
- d, "48, since each tie inside the list takes away one member": a tie takes away a number, so the list
  grows past fifty.

### Q4. Which statement about Retail-Core's line holds?

Kind: read the output. The key is c, "Nobody ties at fiftieth, and DENSE_RANK's 50 falls on C-0094, the
52nd member". The fiftieth member, C-0005, booked Rs 2,980 and the 51st, C-0092, Rs 2,950, so RANK and
ROW_NUMBER ship the same fifty; DENSE_RANK reaches 50 at C-0094, on Rs 2,910, and takes C-0092 and
C-0094 onto a list neither earned.

- a, "The two ties inside the list each push RANK one place further on, so RANK ships 52": RANK skips a
  number after each tie, so by place 50 its number is 50 again and it ships fifty.
- b, "DENSE_RANK's 50 falls on C-0092, the 51st member, so DENSE_RANK ships 51": C-0092 carries dense
  49; the 50 is C-0094's.
- d, "Nobody ties at fiftieth, so all four rules ship the same fifty members": three of them do, and
  DENSE_RANK ships 52.

### Q5. Which sentence goes to the head of Retail-Plus about Retail-Core's list?

Kind: choose the line. The key is b, "Retail-Core's list holds 50 under RANK; nobody ties at fiftieth,
where C-0005 booked Rs 2,980." It names the head's rule, the count it ships and the member at the line
with his figure, so the head can repeat it to a member who asks why he is fifty-first.

- a, "Retail-Core's list holds 52 under DENSE_RANK, which keeps every tie together, just as you asked.":
  sounds like the head's words and ships two members who tie with nobody.
- c, "Retail-Core's list holds 50 under ROW_NUMBER, cut by customer id, so it is the same size on every
  run.": the right count today by the rule the head questioned, which would drop a tied member by id.
- d, "Retail-Core's list holds 50 under whole ties only, so no tie anywhere on the list is ever
  split.": the count matches here, and the rule is the one that ships short of fifty when a tie sits on
  the line, which the head refused.

## Which wrong answer is worth arguing about?

Item 5, option d. On Retail-Core whole ties only ships the same fifty as RANK, so the sentence's number
is right, and a learner can argue that the rule does no harm. The head of Retail-Plus asked for a rule
that holds on every list, including any list where two members tie on the line, and that is where
whole ties only drops both and RANK keeps both. That is why the sentence to the head names the rule as
well as the count.

## Where does this show up at work?

Every interview that includes SQL asks some version of item 1 or item 2, usually as "RANK, DENSE_RANK
and ROW_NUMBER on a tie", and follows it with "your top ten came back with eleven rows; is it a bug?".
The answer is the tie rule working, said with the count and the members at the line.
