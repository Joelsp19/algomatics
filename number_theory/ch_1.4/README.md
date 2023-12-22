# fib.py

### Number Theory Programming Problem CH 1.4 #1,#2,#3:

Find the first n terms of Fibonacci sequence
Find the first n terms of Lucas sequence
Find the Zeckendorf representation of a postive integer n

**_Fibonacci Sequence_**
: F(1) = 1, F(2) = 1, F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> for n>=3

**_Lucas Sequence_**
: L(1) = 1, L(2) = 3, L<sub>n</sub> = L<sub>n-1</sub> + L<sub>n-2</sub> for n>=3

**_Zeckendorf Representation_**
: is the unique expression of this integer as the
sum of distinct Fibonacci numbers, where no two of these Fibonacci numbers are consecutive
terms in the Fibonacci sequence and where the term F<sub>1</sub>=1 is not used (but the term F<sub>2</sub>=1 may
be used)

#### APROACH

- for Fib and Lucas : use a for loop and add to list the next value, then change the first,second = second,next (pass in the initialy first and second value)

- For Zeckendorf:
  - find fib till we pass this value
  - subtract that value(last in list) then use as target
  - keep going down till we find that value or less
  - subtract and make as target
  - continue till target = 0 (or if index = 1)

-defined a Fib function that finds all Fib numbers less than a limit
