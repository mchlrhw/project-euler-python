from euler.lib import digits, is_palindrome, products
from euler.problems.problem_0004 import main as problem


PROBLEM_TEXT = """
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


class TestPalindrome:

    def test_palindrome(self):
        assert is_palindrome(9009)

    def test_not_palindrome(self):
        assert not is_palindrome(42)


class TestDigits:

    def test_1_digit(self):
        expected_list = [
            1, 2, 3, 4, 5, 6, 7, 8, 9,
        ]

        assert list(digits(1)) == expected_list

    def test_2_digits(self):
        expected_list = [
            10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
            20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39,
            40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
            50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
            60, 61, 62, 63, 64, 65, 66, 67, 68, 69,
            70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
            80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
            90, 91, 92, 93, 94, 95, 96, 97, 98, 99,
        ]

        assert list(digits(2)) == expected_list


def test_products():
    expected_list = [
        1, 2, 3, 4, 5, 6, 7, 8, 9,
        4, 6, 8, 10, 12, 14, 16, 18,
        9, 12, 15, 18, 21, 24, 27,
        16, 20, 24, 28, 32, 36,
        25, 30, 35, 40, 45,
        36, 42, 48, 54,
        49, 56, 63,
        64, 72,
        81,
    ]

    assert list(products(digits(1))) == expected_list


def test_example():
    expected_largest = 9009

    largest = 0
    for p in products(digits(2)):
        if is_palindrome(p) and p > largest:
            largest = p
    assert largest == expected_largest


def test_answer():
    answer = problem()
    assert answer == 906609
