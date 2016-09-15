from euler.lib import primes
from euler.problems.problem_0010 import main as problem


PROBLEM_TEXT = """
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def test_example():
    expected_prime_sum = 17

    prime_sum = sum(primes(limit=10))
    assert prime_sum == expected_prime_sum


def test_answer():
    answer = problem()
    assert answer == 142913828922
