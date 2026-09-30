# Round 2: the protect list and the lookup

Ten minutes, alone, at the end of round 2. Seven items on the list the head of Retail-Plus acts on
and the lookup the chief of staff types into. The solution opens at the close of the session.

Post exactly this shape, the letters in item order, no spaces: `xxxxxxx`

---

### Q1. The chief of staff types C-0195, a Retail-Plus member with no orders in the two quarters, and the sheet shows Rs 16,740 and rank 15. What went wrong?

a) The member's orders were summed across both quarters instead of Q2
b) An approximate match returned the nearest id below the one asked for
c) The protect list was ranked before the segment filter was applied
d) The ids are text, so the lookup compared them in the wrong order entirely

### Q2. Revenue sits in column E and ids in column A of the customer table. Which formula returns C-0195's revenue or the words "not in the table", and nothing else?

a) `=VLOOKUP("C-0195",A:E,5)`
b) `=INDEX(E:E,MATCH("C-0195",A:A,1))`
c) `=IFERROR(INDEX(E:E,MATCH("C-0195",A:A,0)),"not in the table")`
d) `=IFERROR(VLOOKUP("C-0195",$A$2:$E$301,5,TRUE),"not in the table")`

### Q3. In the room's Excel, which XLOOKUP prints the words "not in the table" for a missing id?

a) `=XLOOKUP(id,ids,revenue,"not in the table")`
b) `=XLOOKUP(id,ids,revenue)`
c) `=XLOOKUP(id,ids,revenue,,-1)`
d) `=XLOOKUP(id,ids,revenue,,1,"not in the table")`

### Q4. Filtered to Mumbai, the protect list shows 11 members, and the foot reads Rs 7,14,890. What is the foot doing?

a) Adding the eleven Mumbai members at their two-quarter revenue
b) Adding only the Mumbai members with an order in Q2
c) Adding all fifty members, whatever the filter hides
d) Adding every Mumbai customer in every segment

### Q5. Which foot adds only the rows on screen, whether a filter hid the others or somebody hid them by hand?

a) `=SUM(E12:E61)`
b) `=SUBTOTAL(9,E12:E61)`
c) `=SUMIF(C12:C61,"Mumbai",E12:E61)`
d) `=SUBTOTAL(109,E12:E61)`

### Q6. The fiftieth member spent Rs 8,580 and the fifty-first Rs 8,520. The head of Retail-Plus wants ties ranked the same. How many rows does the list ship?

a) 50, since no tie sits across the boundary
b) 49, since RANK leaves a gap after every tie
c) 51, since a tie rule always adds one
d) 48, since two members share a revenue

### Q7. Before the chief of staff uses the lookup on Monday, which test do you run first?

a) An id from the top of the list, to see the largest revenue
b) An id you know is missing, to see the lookup say so
c) An id typed in lower case, to see the match ignore case
d) The last id in the table, to see the range reaches it
