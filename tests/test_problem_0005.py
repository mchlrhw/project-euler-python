from euler.lib import lcm
from euler.problems.problem_0005 import main as problem


def test_example():
    expected_lcm = 2520

    assert lcm(limit=10, inclusive=True) == expected_lcm


def test_answer():
    answer = problem()
    assert answer == 232792560 
