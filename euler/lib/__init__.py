import operator

from collections import Counter
from functools import reduce
from itertools import combinations_with_replacement, islice

from .primes import is_factor, is_prime, prime_factors


def digits(count):
    """
    Generate all of the numbers with the specified digit count
    """
    return range(
        int('1' + ('0' * (count - 1))),
        int('1' + ('0' * count)),
    )


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


def product(seq):
    """
    Calculate the product of a sequence

    The multiplicative equivalent of the builtin sum function.
    """
    return reduce(operator.mul, seq, 1)


def products(seq):
    """
    Generate the products of every pairwise combination of terms a sequence
    """
    return (a*b for a, b in combinations_with_replacement(seq, 2))


def sliding_window(seq, size=1):
    """
    Generate succesive windows of a given size across a sequence

    The window will slide to the end of the sequence at which point it will
    reduce in size to zero as it runs out of terms. If the window is bigger
    than the sequence it will behave as if it is already at the end, i.e. it
    will start to tail off straight away.
    """
    for i, _ in enumerate(seq):
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
