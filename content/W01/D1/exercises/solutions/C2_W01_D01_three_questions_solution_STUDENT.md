# Day 1 solution, E4. The three questions

### Question 1: the Student segment

```
count = 0
total = 0
for r in records:
    if r["segment"] == "Student":
        count = count + 1
        total = total + int(r["amount"])

print(count, total)
```

```
7 12945
```

Seven of the thirty orders are in the Student segment, and they total Rs 12,945.

### Question 2: the returned orders

```
count = 0
total = 0
for r in records:
    if r["status"] == "returned":
        count = count + 1
        total = total + int(r["amount"])

print(count, total)
```

```
7 13670
```

Seven orders were returned, and those returned orders total Rs 13,670.

This is the question that behaves differently from the other two. KR4200 is a returned order and its amount is the text `"4500"`, so question 2 walks straight into the record you fought with in the guided build. Without `int()` around the amount, this cell stops on the very first record. Questions 1 and 3 happen to miss that record, so they give the right answer today even without the conversion, and they would break the morning a second text amount arrives. Convert at the point of use every time and the question of which records happen to be tidy stops mattering.

### Question 3: delivered orders above Rs 2,000

```
count = 0
total = 0
for r in records:
    if r["status"] == "delivered":
        if int(r["amount"]) > 2000:
            count = count + 1
            total = total + int(r["amount"])

print(count, total)
```

```
6 15520
```

Six delivered orders are above Rs 2,000, and they total Rs 15,520.

Two conditions have to hold for a card to count here, so one `if` sits inside the other and the accumulators sit inside both. You can also join the two conditions on a single line with `and`, and you get the same six orders. The nested version is the one built out of the pieces you were handed today, and it makes the order of the two questions visible on screen.

### The overlap question

Your three counts are 7, 7 and 6, which come to 20, and there are thirty orders in the file. The three answers are three overlapping views of the same thirty records rather than three slices of them, so an order can be counted in more than one of them and plenty of orders are counted in none.

KR4221 is a Student order that was returned, so it lands in question 1 and in question 2. KR4214 is a Student order that was delivered at Rs 2,840, so it lands in question 1 and in question 3. No order lands in all three, because a single order cannot be both returned and delivered.

Notice what question 3 also tells you. There are 13 delivered orders and 13 orders above Rs 2,000, and only 6 orders sit in both groups at once. Those two thirteens were never the same thirteen orders.

### The answers to the fifteen items

**Answers: 1d 2b 3a 4c 5b 6d 7a 8c 9d 10b 11a 12c 13b 14d 15a**

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | d | KR4200 is a returned order and its amount is the text `"4500"`, so question 2 meets it. | a and b name the two questions whose conditions happen to exclude it today; c is true of the walk and false of the conversion, since only the qualifying records reach the addition. |
| 2 | b | The Student condition and the delivered condition both skip KR4200, so no comparison ever sees its text. | a invents a conversion the conditions do not do; c invents a rule Python does not have; d assumes two files where there is one. |
| 3 | a | The three questions ask three different things of the same thirty records, so an order can appear in two of them and plenty appear in none. | b assumes the three are a partition; c invents ten dropped records; d invents arithmetic that no rule produces. |
| 4 | c | KR4221 is Student and returned, so questions 1 and 2. KR4214 is Student and delivered above Rs 2,000, so questions 1 and 3. KR4200 is returned and not Student, so question 2 only. | a and b scramble the pairs; d puts KR4200 in question 3, which needs a delivered status it does not have. |
| 5 | b | Question 2 wants a returned order and question 3 wants a delivered one, and no order is both. | a and c describe orders that land in two answers rather than three; d is false, since KR4214 is a large Student order. |
| 6 | d | Two groups of the same size can share as few or as many members as the data happens to give. | a assumes double counting where there is overlap; b adds the two counts as though they were separate files; c reads a correlation out of six shared orders. |
| 7 | a | A count and a total with no group named will be read against whatever group the reader had in mind, which is usually the whole file. | b and c are two specific wrong readings the reader might land on, and neither is more likely than any other; d describes what a careful reader would ask for rather than what most readers assume. |
| 8 | c | It names the group, the denominator and the total, so nothing is left for the reader to supply. | a calls a size band revenue; b calls it collected money, which is delivered orders and a different thirteen; d calls it the order book, which is all thirty. |
| 9 | d | The quotes make the amount text, and Rs 4,500 is the largest amount in the file. | a and c misread the segment and the status, both of which are visible in the row; b misses the quotes, which is the whole point of putting the raw row on the page. |
| 10 | b | Seven of thirty is 23.3 percent. | a reads the count as a percentage; c is the delivered share of the file rounded; d is the share of the twenty orders your three answers happen to cover. |
| 11 | a | Rs 12,945 across seven orders is Rs 1,849.29. | b hands back the total; c divides by thirty rather than by seven; d is a plausible round number with nothing behind it. |
| 12 | c | The count, the total and the group name are what make a number readable by somebody who was not there. | a and d swap the total or the count for the order ids, which are evidence rather than an answer; b drops the count, which is the denominator every rate rests on. |
| 13 | b | Six accumulators in one loop is correct and cheap, and it couples the three answers, so a change to one means rerunning all three. | a is false, since a loop holds as many accumulators as you write; c misreads one walk as three; d ignores the coupling, which is a real cost when you are still deciding what each condition should say. |
| 14 | d | Two identical totals from two different conditions almost always means the second condition never made it into the code. | a is possible in principle and false here, since the delivered thirteen include orders below Rs 2,000; b would double both numbers rather than equalise them; c would leave the totals unchanged. |
| 15 | a | Every group total has to be at least its count times the smallest amount in that group, and that check catches a reset, a dropped condition and a missing record in one line. | b assumes the three answers partition the file, which item 3 has already settled; c is a coincidence; d assumes the three answers cover every order exactly once. |

### The hands-on picks

The running half is `notebooks/C2_W01_D01_ex1_hands_on_STUDENT.ipynb`, and its five markers are:

**Answers: 1b 2a 3a 4c 5b**

The executed twin is `C2_W01_D01_ex1_hands_on_solution_STUDENT.ipynb` in this folder.

### Where this pattern lives in production

Filter, count, total, then a sentence naming the group is the shape of most of the reporting work you will be asked for in your first year. The expensive mistake is not the arithmetic. It is a count that travels without the group it came from, which is how a returned-orders total ends up on a slide with the word revenue above it.
