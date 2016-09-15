from ..lib import primes


def main():
    return sum(primes(limit=2000000))


if __name__ == '__main__':  # pragma: no cover
    print(main())
