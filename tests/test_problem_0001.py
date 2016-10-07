from euler.lib import multiples
from euler.problems.problem_0001 import main as problem


def test_one_factor():
    expected_multiples_list = [2, 4, 6, 8, 10]

    multiples_list = list(multiples((2,), limit=10, inclusive=True))
    assert multiples_list == expected_multiples_list


def test_example():
    expected_multiples_list = [3, 5, 6, 9]
    expected_sum = 23

    multiples_list = list(multiples((3, 5), limit=10, inclusive=False))
    assert multiples_list == expected_multiples_list
    assert sum(multiples_list) == expected_sum


def test_answer():
    answer = problem()
    assert answer == 233168
