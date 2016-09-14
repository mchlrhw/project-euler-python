from euler.lib import lcm
from euler.problems.problem_0005 import main as problem


PROBLEM_TEXT = """
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""


def test_example():
    expected_lcm = 2520

    assert lcm(limit=10, inclusive=True) == expected_lcm


def test_answer():
    answer = problem()
    assert answer == 232792560 
