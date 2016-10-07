from euler.lib import even, fibonacci
from euler.problems.problem_0002 import main as problem


def test_even():
    expected_evens = [0, 2, 4, 6, 8, 10]

    evens = list(even(range(11)))
    assert evens == expected_evens


class TestFibonacci:

    def test_terms(self):
        expected_seq = [0, 1, 1, 2, 3, 5]

        seq = list(fibonacci(0, 1, terms=6))
        assert seq == expected_seq

    def test_limit(self):
        expected_seq = [0, 1, 1, 2, 3]

        seq = list(fibonacci(0, 1, limit=5))
        assert seq == expected_seq

    def test_inclusive_limit(self):
        expected_seq = [0, 1, 1, 2, 3, 5]

        seq = list(fibonacci(0, 1, limit=5, inclusive=True))
        assert seq == expected_seq


def test_example():
    expected_fib_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    expected_even_list = [2, 8, 34]
    expected_even_sum = 44

    fib_list = list(fibonacci(1, 2, terms=10))
    assert fib_list == expected_fib_list
    even_list = list(even(fib_list))
    assert even_list == expected_even_list
    even_sum = sum(even_list)
    assert even_sum == expected_even_sum


def test_answer():
    answer = problem()
    assert answer == 4613732
