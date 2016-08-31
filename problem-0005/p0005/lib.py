import operator

from collections import Counter, defaultdict
from contextlib import suppress
from functools import lru_cache, reduce
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


def lcm(limit):
    signature = {}
    for i in range(limit + 1):
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
    return reduce(operator.mul, (p ** c for p, c in signature.items()), 1)
