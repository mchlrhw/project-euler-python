from euler.lib import square_sum, sum_squares
from euler.problems.problem_0006 import main as problem


def test_square_sum():
    assert square_sum(range(11)) == 3025


def test_sum_squares():
    assert sum_squares(range(11)) == 385


def test_example():
    expected_diff = 2640

    diff = square_sum(range(11)) - sum_squares(range(11))
    assert diff == expected_diff


def test_answer():
    answer = problem()
    assert answer == 25164150
