# tower_of_hanoi.py

### Number Theory Programming Problem CH 1.3 #1

List the moves in the tower of Hanoi puzzle. If you can, animate these moves

**_Tower of Hanoi_**
: includes three pegs and n (initially 8) rings of different sizes placed in order of size, with the largest on the
bottom, on one of the pegs. The goal of the puzzle is to move all of the rings, one at a time,
without ever placing a larger ring on top of a smaller ring, from the first peg to the second,
using the third as an auxiliary peg.

#### APROACH

- STEP 1: move n-1 disks to the auxiliary peg
- STEP 2: move nth disk to the destination peg
- STEP 3: move n-1 disks to the destination peg

- in practice, used recursion
- base case: if disk is smallest, then immedietely move to destination
- call tower_of_hanoi with disk = n-1, source = source, destination = aux, aux = destination
- move the disk to destination
- call tower_of_hanoi with disk = n-1, source = aux, destination = destination, aux = source

# cover_chessboard.py

### Number Theory Programming Problem CH 1.3 #2

Cover a 2<sup>n</sup> x 2<sup>n</sup> chessboard that is missing one square using L-shaped pieces (sides of length 2 and 1)

#### APROACH (made it more like a game)

- STEP 1: create the board
- STEP 2: create the pieces
- STEP 3: move the pieces
- STEP 4: rotate the pieces
- STEP 5: add highlighting, collision checking, etc
- STEP 6: check if we won

- to show that this works first consider that when we have 2<sup>n</sup> x 2<sup>n</sup> board that we have 2<sup>n</sup> x 2<sup>n</sup> -1 squares, which will always be divisible by 3 (since each piece takes up 3 squares we know that this means it's possible to fill the spaces)
- now algorithmically, start with the corners and make your way through the square. That way you make the square smaller as you go
- by strong induction we know that any smaller square missing a square can also be filled
  -continue working around the missing square

# egyptian_fraction.py

### Number Theory Programming Problem CH 1.3 #3

Given a rational number p/q, express p/q as an Egyptian fraction

**_Egyptian Fraction_**
: A unit fraction is a fraction of the form 1/n, where n is a positive integer. Because the
ancient Egyptians represented fractions as sums of distinct unit fractions, such sums are called
Egyptian fractions

#### APROACH

- till we reach our target(or within a certain precision)
- if 1/d is less than target
- set the new target -= 1/d and add d to list of sums
- this gives us the list of denominators where sum of (1/d) = the given target number

- added an extra feature to only take the fractional part of the number, in case the give number is greater than one
- for example, for pi, we get

  > $$ [3, |, 8,61,5014] = 3+ \frac{1}{8}+\frac{1}{61}+\frac{1}{5014}+ ...

- extra function that finds the fraction associated with a list of denominators of unit fractions
