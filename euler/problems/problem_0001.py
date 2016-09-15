from ..lib import multiples


def main():
    return sum(multiples((3, 5), limit=1000))


if __name__ == '__main__':  # pragma: no cover
    print(main())
