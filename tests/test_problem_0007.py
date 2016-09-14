from euler.lib import primes
from euler.problems.problem_0007 import main as problem


PROBLEM_TEXT = """
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""


def test_example():
    expected_prime = 13

    assert max(primes(terms=6)) == expected_prime


def test_answer():
    answer = problem()
    assert answer == 104743
