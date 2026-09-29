# Solution: what is sales, and what is it made of?

Answers: 1b 2d 3a 4c 5a 6d 7b

## The idea being tested

"Sales" is three honest numbers on one file, and each answers a different question. Booked
revenue, Rs 5,44,810 on 30 orders, is what customers asked for. Not cancelled, Rs 5,35,760 on 26
orders, is what the business agreed to fulfil. Delivered, Rs 5,20,790 on 21 orders, is what reached
a customer and stayed. The trap is the first number reported as "sales" with no definition beside
it: 4 cancelled orders ride inside it, all 4 from store, and a growth baseline built on it counts
demand that never arrived. The check is a count by status before any sum, and the fix is the
definition written beside the number.

## Item by item

| Item | Key | Why it holds | Why the others fail |
|---|---|---|---|
| 1 | b | Rs 5,44,810 is booked revenue, and 4 of its 30 orders were cancelled, so it includes Rs 9,050 that never became a sale. | a: a median describes a typical order, and a total is a total. c: the returned orders are inside the Rs 5,44,810 already. d: the ask is about last quarter, and a quarter is the window the file holds. |
| 2 | d | Not cancelled keeps every order except the 4 cancelled ones: 30 less 4 is 26. | a: 21 is the delivered count, a stricter definition. b: 25 takes out the returns, which were not cancelled. c: 30 is every booked row, cancelled ones included. |
| 3 | a | Rs 5,44,810 less the Rs 9,050 of cancelled orders is Rs 5,35,760. | b takes out the returns in place of the cancellations. c is the delivered figure, which takes out both. d adds the cancelled rupees a second time. |
| 4 | c | Store booked 10 orders and 4 of them were cancelled, so a baseline on booked orders credits store with 4 orders in 10 that never arrived. | a: the rupees are small here, and the order count is what the baseline carries. b: a cancelled order is demand that was withdrawn, so counting it overstates. d: app and web had no cancellations at all. |
| 5 | a | The condition picks out the cancelled orders, which is why it printed their Rs 9,050; != keeps the other 26 and prints 535760. | b answers a different definition, delivered, and prints 520790. c prints thirty running lines and still sums the wrong orders. d changes the type of the total and leaves the wrong orders in it. |
| 6 | d | The line names its definition, its window and the orders behind it, so nobody at the board has to guess which "sales" it is. | a names no definition and no window. b gives the booked number with no definition and calls it sales. c labels the delivered figure "net of returns", and net of returns alone is Rs 5,29,840, so the label and the number disagree. |
| 7 | b | Revenue per customer is how often a customer buys times what each order is worth: orders per customer times revenue per order. | a multiplies into orders, which is the count of all orders. c multiplies a basket measure by a head count, which is no branch of the tree. d multiplies two rupee measures, which gives rupees squared and no metric at all. |

## The part worth arguing about

Item 6. Some will argue that the delivered figure is the most honest number and should be the one
Meera sees. It can be, and the argument is fine to have. What is not open is shipping any of the
three without its name and window, because a number without a definition invites a board member to
assume the largest one. The key wins because it is the only line a reader cannot misread.

**Kavya's review.** "I will accept any of the three definitions. I will not accept a number that
does not say which one it is."

## Where the pattern lives in production

Every retailer's finance team keeps gross merchandise value, net sales and recognised revenue as
separate lines, and the arguments in a quarterly review are very often two people quoting two of
them as "sales". Analysts at product companies meet it as bookings against revenue. The habit of a
count by status before a sum is the same habit that catches test orders and duplicate postings in a
warehouse table.

## Hands-on

Sections 1 and 2 of `notebooks/C2_W01_D01_01_what_sales_is_STUDENT.ipynb` print 26 orders and Rs 5,35,760
on the not-cancelled definition, and 21 orders and Rs 5,20,790 on delivered, which confirm Q2 and Q3.
