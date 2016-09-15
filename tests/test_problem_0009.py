from euler.lib import pythagorean_triplet
from euler.problems.problem_0009 import main as problem


PROBLEM_TEXT = """
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
    a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def test_example():
    expected_triplet = (3, 4, 5)

    triplet = pythagorean_triplet(5)
    assert triplet == expected_triplet


def test_answer():
    answer = problem()
    assert answer == 31875000
