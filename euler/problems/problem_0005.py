"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of
the numbers from 1 to 20?
"""


from ..lib import lcm


def main():
    return lcm(limit=20, inclusive=True)


if __name__ == '__main__':  # pragma: no cover
    print(main())
