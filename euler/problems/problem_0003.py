"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


from ..lib import prime_factors


def main():
    return max(prime_factors(600851475143))


if __name__ == '__main__':  # pragma: no cover
    print(main())
