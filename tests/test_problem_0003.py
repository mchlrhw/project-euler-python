from euler.lib import prime_factors
from euler.problems.problem_0003 import main as problem


PROBLEM_TEXT = """
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def test_example():
    expected_factors = [5, 7, 13, 29]

    assert list(prime_factors(13195)) == expected_factors


def test_answer():
    answer = problem()
    assert answer == 6857
