from euler.lib import primes
from euler.problems.problem_0007 import main as problem


def test_example():
    expected_prime = 13

    assert max(primes(terms=6)) == expected_prime


def test_answer():
    answer = problem()
    assert answer == 104743
