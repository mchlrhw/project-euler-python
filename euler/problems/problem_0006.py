from ..lib import square_sum, sum_squares


def main():
    return square_sum(range(1, 101)) - sum_squares(range(1, 101))


if __name__ == '__main__':
    print(main())
