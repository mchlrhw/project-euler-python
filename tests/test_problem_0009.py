from euler.lib import pythagorean_triplet
from euler.problems.problem_0009 import main as problem


def test_example():
    expected_triplet = (3, 4, 5)

    triplet = pythagorean_triplet(5)
    assert triplet == expected_triplet


def test_answer():
    answer = problem()
    assert answer == 31875000
