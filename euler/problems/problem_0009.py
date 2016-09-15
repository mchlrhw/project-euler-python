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
