from functools import lru_cache
from math import sqrt, ceil


@lru_cache(maxsize=None)
def is_prime(i):
    for prime in primes(ceil(sqrt(i))):
        if i % prime == 0:
            return False
    return True


def primes(limit):
    for i in range(limit):
        if i <= 1:
            continue
        if is_prime(i):
            yield i


def prime_factors(i):
    for prime in primes(ceil(sqrt(i)) + 1):
        if i % prime == 0:
            yield prime
            remainder = i // prime
            if is_prime(remainder):
                yield remainder
            else:
                yield from prime_factors(remainder)
