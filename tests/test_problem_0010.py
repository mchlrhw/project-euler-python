from euler.lib import primes
from euler.problems.problem_0010 import main as problem


def test_example():
    expected_prime_sum = 17

    prime_sum = sum(primes(limit=10))
    assert prime_sum == expected_prime_sum


def test_answer():
    answer = problem()
    assert answer == 142913828922
