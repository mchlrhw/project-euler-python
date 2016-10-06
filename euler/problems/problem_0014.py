from euler.lib import collatz_length


def main():
    n = 0
    greatest = 0
    for i in range(1, 1000000):
        ln = collatz_length(i)
        if ln >= greatest:
            n = i
            greatest = ln
    return n


if __name__ == '__main__':  # pragma: no cover
    print(main())
