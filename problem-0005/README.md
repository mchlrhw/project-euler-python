I'm pretty happy with this solution, but the code relies on the prime code
from problem 3, so the next commit will probably be a restructure of this
package to avoid code duplication.

While trying to solve this I assumed that the product of all of the numbers
would give the least common multiple, but if you do that you overshoot because
some numbers have factors that are double counted. For example, the factors of
4 are (2, 2) and the factors of 8 are (2, 2, 2). This means that to accomodate
8 you need a number that has 2 ** 3 in its factors, but that already accounts
for the 2 ** 2 needed by 4. The solution therefore relies on the fact that if
you factorise all of the numbers in the set of numbers, you only have to count
factors that are either unique, or that have a higher power than any previous
number with the same base factor.

In practice I chose to produce the powers of the factors of each number using
a Counter object, which are then unpacked into a "signature" dict, which
represents the factorisation of the target LCM. It is possible to limit the
target to the lowest common multiple by only including a factor and its power
if it is either not in the dict, or if the power is greater than a factor
already in the dict. The LCM is then given by the recomposition of the factors
in its signature.
