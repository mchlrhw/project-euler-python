from collections import Counter
from contextlib import suppress
from itertools import count
from math import sqrt


def is_factor(factor, i):
    """
    Determine if a number is a factor of another number

    Implemented using modulo arithmetic
    """
    return i % factor == 0


def is_prime(i):
    """
    Determine if a positive integer i is prime

    Short circuits 0 and 1 (and any integer greater than 5 ending in anything
    other than 1, 3, 7 or 9) by always returning False; all other integers
    are determined to be prime if they have no prime factors.
    The implementation relies on the prime_factors generator, which raises
    a StopIteration exception if it is empty. If it doesn't raise this
    exception we can infer that the number is composite and is therefore
    not prime.
    """
    if i == 2 or i == 5:
        return True
    elif i < 2 or str(i)[-1] not in ('1', '3', '7', '9'):
        return False
    else:
        with suppress(StopIteration):
            next(prime_factors(i))
            return False
        return True


def primes(terms=None, limit=None, inclusive=False):
    """
    Generate primes up to a given limit or term

    An implementation of the Sieve of Eratosthenes with an optimisation that
    only considers odd candidates.
    Can be made inclusive of the limit.
    """
    composites = {}

    if inclusive and limit is not None:
        limit += 1

    def limit_reached(x):
        return limit is not None and x >= limit

    def terms_reached(y):
        return terms is not None and y >= terms

    t = 0
    if limit_reached(2) or terms_reached(t):
        return
    yield 2
    t += 1
    if terms_reached(t):
        return

    for i in count(start=3, step=2):
        if limit_reached(i) or terms_reached(t):
            return
        factor = composites.pop(i, None)
        if factor:
            new_composite = i + factor
            while new_composite in composites or not (new_composite & 1):
                new_composite += factor
            composites[new_composite] = factor
        else:
            t += 1
            composites[i**2] = i
            yield i


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
        if not is_factor(prime, i):
            continue
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
