import operator

from collections import Counter, defaultdict, deque, OrderedDict
from contextlib import suppress
from functools import reduce
from itertools import accumulate, combinations_with_replacement, count, islice
from math import sqrt

from .primes import factors, is_factor, is_prime, prime_factors, primes


COLLATZ_CACHE = {
    1: (1, 1),
}


def _populate_collatz_cache(n):
    subchain = OrderedDict()
    while n not in COLLATZ_CACHE.keys():
        nxt = (3*n + 1) if (n&1) else (n//2)
        subchain[n] = n = nxt

    base_ln = COLLATZ_CACHE[n][1]
    subchain = {
        n: (nxt, i+base_ln)
        for i, (n, nxt) in enumerate(reversed(subchain.items()), start=1)
    }
    COLLATZ_CACHE.update(subchain)


def collatz(n):
    """
    Generate the Collatz sequence for a given starting integer n
    """
    if n not in COLLATZ_CACHE:
        _populate_collatz_cache(n)

    while True:
        yield n
        if n == 1:
            break
        n, _ = COLLATZ_CACHE[n]


def collatz_length(n):
    """
    Return the length of the Collatz chain for a given starting integer n
    """
    if n not in COLLATZ_CACHE:
        _populate_collatz_cache(n)

    _, ln = COLLATZ_CACHE[n]
    return ln


def columns(matrix):
    """
    Shorcut for forming a generator over the columns of a matrix
    """
    return (c for c in transpose(matrix))


def diagonals(matrix, forward=True):
    """
    Iterate over the diagonals of a 2-D matrix
    """
    diags = defaultdict(deque)
    for i, row in enumerate(reversed(matrix)):
        if not forward:
            row = reversed(row)
        for j, n in enumerate(row):
            diags[i+j].appendleft(n)
    return (diag for _, diag in sorted(diags.items()))


def digits(count):
    """
    Generate all of the numbers with the specified digit count
    """
    return range(10**(count - 1), 10**count)


def even(seq):
    """
    Pull out the even terms of a sequence
    """
    return (n for n in seq if n % 2 == 0)


def fibonacci(a=1, b=1, terms=None, limit=None, inclusive=False):
    """
    Generate the fibonacci sequence

    The starting terms can be specified and the sequence will continue up to
    the specified term, or stop below the limit, whichever comes first. The
    limit can be made inclusive.
    If term and limit are not specified it will continue indefinitely.
    """
    i = 0
    if inclusive and limit is not None:
        limit += 1
    while True:
        if limit is not None and a >= limit:
            break
        elif terms is not None:
            if i >= terms:
                break
        yield a
        a, b = b, a+b
        i += 1


def is_palindrome(i):
    """
    Determine whether the argument is a palindrome
    """
    i_string = str(i)
    if i_string == i_string[::-1]:
        return True
    return False


def lcm(limit, inclusive=False):
    """
    Find the lowest common multiple of all numbers below the limit

    Can be made inclusive of the limit.
    """
    if inclusive:
        limit += 1
    signature = {}
    for i in range(limit):
        if is_prime(i):
            factors = Counter([i])
        else:
            factors = Counter(prime_factors(i))
        signature.update(
            {
                p: c
                for p, c in factors.items()
                if c > signature.get(p, 0)
            }
        )
    return product(p ** c for p, c in signature.items())


def multiples(factors, limit, inclusive=False):
    """
    Find the multiples of factors below a certain limit

    Can be made inclusive so that it finds the multiples up to and
    including the limit. Implemented by checking if any of the factors
    are a factor of every number up to the limit.
    """
    if inclusive:
        limit += 1
    for i in range(1, limit):
        if any(is_factor(f, i) for f in factors):
            yield i


def odd(seq):
    """
    Pull out the odd terms of a sequence
    """
    return (n for n in seq if n % 2 != 0)


def paths(n):
    """
    Calculate the paths through a lattice of size n*n
    """
    def get_moves(x, y):
        if x < n:
            yield (x+1, y)
        if y < n:
            yield (x, y+1)

    def count_paths(x, y):
        moves = get_moves(x, y)
        with suppress(StopIteration):
            move = next(moves)
            yield from count_paths(*move)
            move = next(moves)
            yield from count_paths(*move)
            yield 1

    start = (0, 0)
    path_count = 1 + sum(count_paths(*start))
    return path_count


def power_digit_sum(power, base=2):
    """
    Calculate the sum of the digits given by raising base to a certain power
    """
    return sum(int(d) for d in str(base**power))


def product(seq):
    """
    Calculate the product of a sequence

    The multiplicative equivalent of the builtin sum function.
    """
    return reduce(operator.mul, seq, 1)


def products(seq):
    """
    Generate the products of every pairwise combination of terms of a sequence
    """
    return (a*b for a, b in combinations_with_replacement(seq, 2))


def pythagorean_triplet(c):
    """
    Derive the pythagorean triplet belonging to a given hypotenuse

    Returns an empty tuple if the hypotenuse does not belong to a pythagorean
    triplet.
    """
    c_squared = c**2
    for a in range(1, c):
        b = sqrt(c_squared - (a**2))
        if b.is_integer():
            return (a, int(b), c)
    return tuple()


def rows(matrix):
    """
    Shortcut for forming a generator over the rows of a matrix
    """
    return (r for r in matrix)


def sliding_window(seq, size=1, bounded=False):
    """
    Generate succesive windows of a given size across a sequence

    The window will slide to the end of the sequence at which point it will
    reduce in size to zero as it runs out of terms. If the window is bigger
    than the sequence it will behave as if it is already at the end, i.e. it
    will start to tail off straight away.

    If stricter behaviour is required the bounded keyword can be set to True,
    in which case each window will contain exactly size number of terms; it
    will not tail off and must be smaller than or equal to the size of the
    sequence itself.
    """
    if bounded:
        seq = list(seq)
        seq_len = len(seq)
    for i, _ in enumerate(seq):
        window_limit = i + size
        if bounded and window_limit > seq_len:
            break
        yield islice(seq, i, i+size)


def squares(seq):
    """
    Generate squares for each term in a sequence
    """
    return (n**2 for n in seq)


def square_sum(seq):
    """
    Find the square of the sum of the terms of a sequence
    """
    return sum(seq)**2


def sum_squares(seq):
    """
    Find the sum of the squares of the terms of a sequence
    """
    return sum(squares(seq))


def transpose(matrix):
    """
    Transpose a 2-D matrix
    """
    return zip(*matrix)


def triangular_numbers(terms=None, limit=None, inclusive=False):
    """
    Generate the triangular numbers up to a given limit or term

    Can be made inclusive of the limit.
    """
    if limit and inclusive:
        limit += 1
    for i, n in enumerate(accumulate(count(1)), 1):
        limit_reached = limit is not None and n >= limit
        terms_reached = terms is not None and i > terms
        if limit_reached or terms_reached:
            break
        yield n
