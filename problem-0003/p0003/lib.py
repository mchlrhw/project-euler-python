from collections import Counter
from contextlib import suppress
from functools import lru_cache
from math import sqrt, ceil


@lru_cache(maxsize=None)
def is_prime(i):
    if i < 2:
        return False
    with suppress(StopIteration):
        next(prime_factors(i))
        return False
    return True


def primes(limit):
    for i in range(2, limit):
        if is_prime(i):
            yield i


def prime_factors(i):
    for prime in primes(ceil(sqrt(i + 1))):
        if i % prime == 0:
            yield prime
            remainder = i // prime
            if is_prime(remainder):
                yield remainder
            else:
                yield from prime_factors(remainder)
            break


def standard_notation(i):
    factors = prime_factors(i)
    c = Counter(factors)
    if not c:
        string = str(i)
    else:
        string = ' * '.join(
            '{}{}'.format(f, ('**{}'.format(p) if p > 1 else ''))
            for f, p in sorted(c.items())
        )
    return string


def largest_prime_factor(i):
    return max(set(prime_factors(i)))
