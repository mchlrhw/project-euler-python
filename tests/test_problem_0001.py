from euler.lib import multiples
from euler.problems.problem_0001 import main as problem


PROBLEM_TEXT = """
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def test_example():
    expected_multiples_list = [3, 5, 6, 9]
    expected_sum = 23

    multiples_list = list(multiples((3, 5), limit=10, inclusive=False))
    assert multiples_list == expected_multiples_list
    assert sum(multiples_list) == expected_sum


def test_answer():
    answer = problem()
    assert answer == 233168
