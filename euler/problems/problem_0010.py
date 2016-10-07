"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from ..lib import primes


def main():
    return sum(primes(limit=2000000))


if __name__ == '__main__':  # pragma: no cover
    print(main())
