"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10001st prime number?
"""


from ..lib import primes


def main():
    return max(primes(terms=10001))


if __name__ == '__main__':  # pragma: no cover
    print(main())
