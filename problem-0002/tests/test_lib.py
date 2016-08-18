from p0002.lib import fib
from p0002.lib import evens


def test_fib_to_8():
    terms = list(fib(limit=8))
    assert terms == [1, 2, 3, 5]


def test_fib_to_100():
    terms = list(fib(limit=100))
    assert terms == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_evens():
    numbers = list(evens((1, 2, 3, 4, 5, 6, 7, 8, 9)))
    assert numbers == [2, 4, 6, 8]
