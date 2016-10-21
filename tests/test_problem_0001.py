import hypothesis.strategies as st

from hypothesis import example, given

from euler.lib import multiples
from euler.problems.problem_0001 import main as problem


def evenly_divisible(multiples_list, factors):
    for m in multiples_list:
        for f in factors:
            if m % f == 0:
                yield True
                break
        else:
            yield False


@given(
    factors=st.lists(
        st.integers(min_value=1, max_value=10),
        min_size=1,
        max_size=10,
    ),
    limit=st.integers(min_value=1, max_value=100),
    inclusive=st.booleans(),
)
@example(
    factors=[3, 5],
    limit=10,
    inclusive=False,
)
def test_multiples(factors, limit, inclusive):
    multiples_list = list(multiples(factors, limit, inclusive))
    assert all(evenly_divisible(multiples_list, factors))
    if not inclusive:
        assert all(m < limit for m in multiples_list)
    else:
        assert all(m <= limit for m in multiples_list)
        if all(evenly_divisible([limit], factors)):
            assert limit in multiples_list


def test_example():
    expected_sum = 23

    multiples_list = list(multiples((3, 5), limit=10, inclusive=False))
    assert sum(multiples_list) == expected_sum


def test_answer():
    answer = problem()
    assert answer == 233168
