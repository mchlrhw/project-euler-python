from itertools import combinations_with_replacement as combinations


def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


def products(digits, reverse=False):
    if reverse:
        pairs = combinations(
            range(
                int('9' * digits),
                int('9' * (digits - 1)),
                -1,
            ),
            2,
        )
    else:
        pairs = combinations(
            range(
                int('1' + ('0' * (digits - 1))),
                int('1' + ('0' * digits)),
            ),
            2,
        )
    product_gen = (a*b for a, b in pairs)
    for p in sorted(product_gen, reverse=reverse):
        yield p


def largest_palindrome_product(digits):
    for p in products(digits, reverse=True):
        if is_palindrome(str(p)):
            return p
