# diophantine_approx.py

### Number Theory Programming Problem CH 1.1 #1

Given a number α, find rational numbers p/q such that

> $$ |α - \frac{p}{q}| <= \frac{1}{q^2}

#### APROACH

- iterate on q, find the lowest integer p value that gives p/q = α
- calculate lower and upper bounds, this is our base p value
- now increment and if value found in between lower bound and upper bound add to list. Stop when greater than upper bound.
- now decrement and if value found in between lower bound and upper bound add to list. Stop when less than lower bound.

# spectrum_sequence.py

### Number Theory Programming Problem CH 1.1 #2

Given a number α, find its spectrum sequence (for n values)

**_spectrum sequence_**
: The spectrum sequence of a real number α is the sequence that has [nα] as its nth term.

#### APROACH

- simply find the floor of the integer for all integers 1<=d<=n --> a(d) = floor(dα)

# ulam_numbers.py

### Number Theory Programming Problem CH 1.1 #3

Find the first n Ulam numbers, where n is a positive integer.

**_The Ulam numbers U<sub>n</sub>_**
: We specify that U<sub>1</sub> = 1 and U<sub>2</sub> = 2.
For each successive integer m, m > 2, this integer is an Ulam number if and only if it can be written
uniquely as the sum of two distinct Ulam numbers.

#### APROACH

- grab the next integer say m(m=3 initially), and if we can construct this integer in more than one way then we don't add to list
- let a be the last value in the list- we have a target of m-a => binary search to get the target
- if found, increment count
- decrement m till we get to the half way point or if the count > 1
- if count = 1 then we have one distinct way to make this number so add to the list
