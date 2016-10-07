from euler.lib import prime_factors
from euler.problems.problem_0003 import main as problem


def test_example():
    expected_factors = [5, 7, 13, 29]

    assert list(prime_factors(13195)) == expected_factors


def test_answer():
    answer = problem()
    assert answer == 6857
