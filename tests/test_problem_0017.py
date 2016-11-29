import hypothesis.strategies as st

from hypothesis import assume, example, given

from euler.lib.names import int_to_english


def test_zero():
    integer = 0
    name = int_to_english(integer)

    assert name == 'ZERO'


def test_minus_zero():
    integer = -0
    name = int_to_english(integer)

    assert name == 'ZERO'


@given(integer=st.integers(max_value=-1))
def test_minus(integer):
    name = int_to_english(integer)

    assert name.startswith('MINUS ')


@given(
    integer_a=st.integers(min_value=20, max_value=90),
    integer_b=st.integers(min_value=1, max_value=9),
)
def test_hyphen(integer_a, integer_b):
    assume(integer_a % 10 == 0)

    name_a = int_to_english(integer_a)
    name_b = int_to_english(integer_b)

    name = int_to_english(integer_a + integer_b)

    first, sep, last = name.partition('-')
    assert first == name_a
    assert sep == '-'
    assert last == name_b


@given(
    integer_a=st.integers(min_value=100, max_value=900),
    integer_b=st.integers(min_value=1, max_value=99),
)
def test_and(integer_a, integer_b):
    assume(integer_a % 100 == 0)

    name_a = int_to_english(integer_a)
    name_b = int_to_english(integer_b)

    name = int_to_english(integer_a + integer_b)

    first, sep, last = name.partition(' AND ')
    assert first == name_a
    assert sep == ' AND '
    assert last == name_b
