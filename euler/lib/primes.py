from collections import Counter
from contextlib import suppress
from functools import lru_cache
from math import sqrt


def is_factor(factor, i):
    """
    Determine if a number is a factor of another number

    Implemented using modulo arithmetic
    """
    if i % factor == 0:
        return True
    return False


@lru_cache(maxsize=None)
def is_prime(i):
    """
    Determine if a positive integer i is prime

    Short circuits 0 and 1 by always returning False; all integers greater
    than 1 are determined to be prime if they have no prime factors.
    The implementation relies on the prime_factors generator, which raises
    a StopIteration exception if it is empty. If it doesn't raise this
    exception we can infer that the number is composite and is therefore
    not prime.
    """
    if i < 2:
        return False
    with suppress(StopIteration):
        next(prime_factors(i))
        return False
    return True


def primes(terms=None, limit=None, inclusive=False):
    """
    Generate primes up to a given limit or term

    Tests each number from 2 to the limit for primality, yielding the number
    if it is prime. If terms is used in place of limit it will stop after
    generating that many terms. If neither is given it will generate primes
    indefinitely.
    The implementation relies on the is_prime function to test for primality.
    Can be made inclusive of the limit.
    """
    i = 0
    n = 2
    if inclusive and limit is not None:
        limit += 1
    while True:
        if limit is not None and n >= limit:
            break
        elif terms is not None:
            if i >= terms:
                break
        if is_prime(n):
            yield n
            i += 1
        n += 1


def prime_factors(i):
    """
    Generate the prime factors of an integer i

    Tests each prime up to the square root of i to see if it is a
    factor of i and, if it is, it yields the factor. It does not yield any
    anything if i is itself prime.
    The implementation relies on the primes_to generator and the is_prime
    function, as well as a recursive call to itself in the case of composite
    factors.
    """
    max_factor = int(sqrt(i))
    for prime in primes(limit=max_factor, inclusive=True):
        if is_factor(prime, i):
            yield prime
            remainder = i // prime
            if is_prime(remainder):
                yield remainder
            else:
                yield from prime_factors(remainder)
            break


def reduced_factors(i):
    """
    Reduce the factors of a number to their value and power
    """
    if i < 2 or is_prime(i):
        c = Counter()
        c[i] += 1
    else:
        factors = prime_factors(i)
        c = Counter(factors)
    return c


def standard_notation(i):
    """
    Represent a number as a string of its factors

    The string is of the form "a**pa * b**pb * ..." where a and b are factors
    and pa and pb are their respective powers.
    """
    r = reduced_factors(i)
    string = ' * '.join(
        '{}{}'.format(f, ('**{}'.format(p) if p > 1 else ''))
        for f, p in sorted(r.items())
    )
    return string
