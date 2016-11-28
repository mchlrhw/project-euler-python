from euler.lib import power_digit_sum
from euler.problems.problem_0016 import main as problem


def test_example():
    result = power_digit_sum(15)
    assert result == 26


def test_answer():
    answer = problem()
    assert answer == 1366
