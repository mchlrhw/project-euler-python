"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
"""


from euler.lib import power_digit_sum


def main():
    return power_digit_sum(1000)


if __name__ == '__main__':  # pragma: no cover
    print(main())
