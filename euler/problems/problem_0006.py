"""
The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""


from ..lib import square_sum, sum_squares


def main():
    return square_sum(range(1, 101)) - sum_squares(range(1, 101))


if __name__ == '__main__':  # pragma: no cover
    print(main())
