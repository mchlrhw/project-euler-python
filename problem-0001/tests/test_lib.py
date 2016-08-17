from p0001.lib import mult_of_3_and_5 as m35
from p0001.lib import sum_multiples


def test_m35_limit_10():
    multiples = list(m35(limit=10))
    assert multiples == [3, 5, 6, 9]


def test_m35_limit_100():
    multiples = list(m35(limit=100))
    assert 0 not in multiples
    assert 10 in multiples
    assert 12 in multiples
    assert 67 not in multiples
    assert 98 not in multiples
    assert 99 in multiples
    assert 100 not in multiples


def test_sum_m35_limit_10():
    s = sum_multiples(limit=10)
    assert s == 23
