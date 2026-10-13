# Which four lines make a number computable, and which line moved each reading?

*The register and the scholarship are invented for chapter 4, with every number in them. Uber's case is illustrative: the company is real, the situation and the data are synthetic, built for this class.*

**The example, in short.** One student's 60-day term (invented) holds 10 holidays, so 50 working
days: the student was present on 40, absent on 8 and on medical leave for 2. In the term's last 20
working days the student was present on 14, absent on 4 and on medical leave for 2. Four honest
clerks read 80.0, 66.7, 83.3 and 84.0 percent from the register, and a fifth, reading only the last
20 working days, reads 70.0.

**Who needs the answer.** The principal who prints one figure on a transfer certificate, the
scholarship that reads it, and Uber's city analyst, who must write the same four lines for trips per
peak online hour before the city head reads it.

**The questions on the way.** Which line differs between two clerks' numbers? What should the
certificate print for a scholarship's rule? Which window should Uber's page carry?

Q1 is called aloud at the end of chapter 4, with the trainer; Q2 and Q3 are sat in the practice lab.
Every item has one right answer. Items marked **Design** ask for the best-fit approach, the fact that
would switch it, or the second route that would confirm a number.

```
Post exactly this shape: xxx
```

---

## Which line differs between two clerks' numbers?

A number is computable once four lines are written: the **numerator**, what is counted on top; the
**denominator**, what it is divided by; the **window**, the stretch of time the count covers; and
the **exclusions**, what leaves both counts, with the date of any change.

### Q1. Two clerks print 80.0 and 84.0 percent from the same register. Which line differs between their two definitions?

a) The numerator: what is counted on top

b) The denominator: what the count is divided by

c) The window: which stretch of days is read

d) The exclusions: which days leave both of the counts

---

## What should the certificate print for the scholarship?

A scholarship (invented) asks for attendance of 75 percent or more over the whole term, and its rule
leaves medical leave out of both counts.

### Q2. What does the certificate print under the scholarship's rule, and does the student qualify?

a) 80.0 percent, and the student qualifies

b) 66.7 percent, and the student does not qualify

c) 83.3 percent, and the student qualifies

d) 70.0 percent, and the student does not qualify

---

## Which window should Uber's page carry?

At Uber's Hyderabad scheme (illustrative) the city analyst compares trips per peak online hour
before and after the launch on Monday 31 August 2026, and must write the window line before anyone
reads the comparison.

### Q3. Design. Which window should the page carry for the before and after comparison?

a) Six whole weeks on each side, so every weekday's peaks count once

b) The launch day against the day before, where the change is sharpest

c) The whole year so far, since a longer window always holds more data

d) The last week after against the first week before, the furthest apart

---

## Where do you check your calls?

Notebook 04, `notebooks/C2_W04_D01_04_numerator_denominator_window_exclusions_STUDENT.ipynb`,
computes all five readings with `attendance(days, top, bottom)` and checks each against a direct
count. Notebook 08, `notebooks/C2_W04_D01_08_denominators_on_full_data_STUDENT.ipynb`, writes the
four lines for all 12,860 driver-weeks. Then post your three letters.
