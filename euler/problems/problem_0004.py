"""
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit
numbers.
"""


from ..lib import digits, is_palindrome, products


def main():
    largest = 0
    for p in products(digits(3)):
        if is_palindrome(p) and p > largest:
            largest = p
    return largest


if __name__ == '__main__':  # pragma: no cover
    print(main())
