from ..lib import primes


def main():
    return max(primes(terms=10001))


if __name__ == '__main__':  # pragma: no cover
    print(main())
