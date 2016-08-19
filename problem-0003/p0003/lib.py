import logging
import sys

from collections import Counter
from functools import lru_cache
from math import sqrt, ceil


log = logging.getLogger()
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler(sys.stdout))


@lru_cache(maxsize=None)
def is_prime(i):
    log.debug('Testing {} for primality'.format(i))
    for prime in primes(ceil(sqrt(i + 1))):
        log.debug('Factorising {} with {}'.format(i, prime))
        if i % prime == 0:
            tmplt = '{0} is a prime factor of {1}, so {1} is not prime'
            msg = tmplt.format(prime, i)
            log.debug(msg)
            return False
    log.debug('{} has no prime factors, so is prime'.format(i))
    return True


def primes(limit):
    log.debug('Finding primes below {}'.format(limit))
    for i in range(2, limit):
        if is_prime(i):
            yield i


def prime_factors(i):
    log.debug('Finding prime factors for {}'.format(i))
    for prime in primes(ceil(sqrt(i + 1))):
        log.debug('Testing if {} is factor of {}'.format(prime, i))
        if i % prime == 0:
            log.debug('{} is a factor!'.format(prime))
            yield prime
            remainder = i // prime
            log.debug('Remainder is {}'.format(remainder))
            if is_prime(remainder):
                log.debug('Remainder is prime!')
                yield remainder
            else:
                log.debug('Need to factorise {}'.format(remainder))
                yield from prime_factors(remainder)
                break


def reduced_string(factors):
    c = Counter(factors)
    reduced = ' * '.join(
        '{}{}'.format(f, ('**{}'.format(p) if p > 1 else ''))
        for f, p in sorted(c.items())
    )
    return reduced
