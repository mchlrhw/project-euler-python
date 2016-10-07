"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
    a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from ..lib import is_factor, product, pythagorean_triplet


def main():
    target = 1000
    for c in range(1, target):
        t = pythagorean_triplet(c)
        s = sum(t)
        if s and is_factor(s, target):
            scalor = target // s
            t = (n*scalor for n in t)
            return product(t)


if __name__ == '__main__':  # pragma: no cover
    print(main())
