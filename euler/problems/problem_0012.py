from euler.lib import factors, triangular_numbers


def main():
    for i in triangular_numbers():
        if len(list(factors(i))) > 500:
            return i


if __name__ == '__main__':  # pragma: no cover
    print(main())
