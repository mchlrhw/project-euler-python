from ..lib import digits, is_palindrome, products


def main():
    largest = 0
    for p in products(digits(3)):
        if is_palindrome(p) and p > largest:
            largest = p
    return largest


if __name__ == '__main__':  # pragma: no cover
    print(main())
