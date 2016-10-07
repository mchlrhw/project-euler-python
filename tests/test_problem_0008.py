from euler.lib import product, sliding_window
from euler.problems.problem_0008 import main as problem
from euler.problems.problem_0008 import N


def test_example():
    expected_max_product = 5832

    max_product = max(
        product(int(c) for c in w) for w in sliding_window(N, size=4)
    )
    assert max_product == expected_max_product


def test_answer():
    answer = problem()
    assert answer == 23514624000
