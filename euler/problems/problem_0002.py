from ..lib import even, fibonacci


def main():
    return sum(even(fibonacci(1, 2, limit=4000000, inclusive=True)))


if __name__ == '__main__':
    print(main())
