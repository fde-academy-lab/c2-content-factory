# Solution: chapter 1, four readings of sales

Answers: 1b 2d 3a 4c 5b

## The idea being tested

"Sales" is three honest numbers on one file, and each answers a different question. Booked, Rs
5,44,810 on 30 orders, is what customers asked for. Not cancelled, Rs 5,35,760 on 26, is what left
the shelf. Delivered, Rs 5,20,790 on 21, is what stayed sold. The trap is the first number reported
as sales with no definition beside it: 4 cancelled orders ride inside it, all 4 from store. The
check is a count by status before any sum, and the fix is the definition written beside the number.
The two design items ask when each way of answering is the right one.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Rs 5,44,810 is booked revenue, and 4 of its 30 orders were cancelled, so it carries Rs 9,050 that never became a sale. | a: a median describes a typical order, and a total is a total. c: the returns are inside the Rs 5,44,810 already. d: the ask is about last quarter, which is the window the file holds. |
| 2 | d | The count by status comes first, since it is the check that catches cancelled orders; then the sums, then the definition beside the total, and the reconciliation last, since it is for the board. | a sums before counting, so the cancelled orders ride in unseen. b reconciles a figure that does not yet say what it is. c writes the definition before the count that tells you which definitions exist. |
| 3 | a | A first look needs every reading at once, which summing by status gives in one pass; the board needs the figure in the books, which only Finance can confirm. | b waits a day or more for a first look that needed an afternoon. c sends the undefined total, the chapter's trap. d is ten minutes at 30 rows and impossible at the full export, and a spreadsheet by hand is where typos hide. |
| 4 | c | The condition picks out the cancelled orders, which is why it printed their Rs 9,050; != keeps the other 26 and prints 535760. | a answers a stricter definition, delivered, and prints 520790. b prints thirty running lines and still sums the wrong orders. d changes the type of the total and leaves the wrong orders in it. |
| 5 | b | A new status becomes a new key with no new code; booked is the sum of every key and not cancelled is booked less one key, so both stay right. | a needs a new if in every reading the new status touches. c is wrong for the status route, which absorbs the new key. d moves the question to Finance and does not compute the readings at all. |

## The part worth arguing about

Item 3. Some will argue that Finance's figure should be the only one Meera ever sees. It should be
the one the board sees; for a first look the same afternoon, waiting for the books costs the
decision a day, and the bridge shows every gap the books will later confirm.

**Kavya's review.** "I will accept any of the three definitions. I will not accept a number that
does not say which one it is."

## Where the pattern lives in production

Reliance Retail reported gross revenue of Rs 90,408 crore and revenue from operations of Rs 79,745
crore for the same quarter to June 2026, and every retailer's finance team keeps booked, net and
recognised revenue on separate lines. Bookings against revenue is the same argument at a product
company.

## Hands-on

`notebooks/C2_W01_D01_01_four_readings_of_sales_STUDENT.ipynb` prints Rs 5,35,760 on the
not-cancelled definition and asserts the two routes agree, which confirms Q1 and Q5; its order of cells, count then sum, is Q2.
