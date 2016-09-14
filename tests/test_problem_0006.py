from euler.lib import square_sum, sum_squares
from euler.problems.problem_0006 import main as problem


PROBLEM_TEXT = """
The sum of the squares of the first ten natural numbers is,
    12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def test_square_sum():
    assert square_sum(range(11)) == 3025


def test_sum_squares():
    assert sum_squares(range(11)) == 385


def test_example():
    expected_diff = 2640

    diff = square_sum(range(11)) - sum_squares(range(11))
    assert diff == expected_diff


def test_answer():
    answer = problem()
    assert answer == 25164150
