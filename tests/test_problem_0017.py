import pytest
import hypothesis.strategies as st

from hypothesis import assume, example, given

from euler.lib.names import HugeInt, int_to_english
from euler.lib.names import letter_count, MAX_INT, MIN_INT
from euler.problems.problem_0017 import main as problem


def test_zero():
    integer = 0
    name = int_to_english(integer)

    assert name == 'ZERO'


def test_minus_zero():
    integer = -0
    name = int_to_english(integer)

    assert name == 'ZERO'


@pytest.mark.parametrize(
    'integer, expected_name',
    [
        (11, 'ELEVEN'),
        (12, 'TWELVE'),
        (13, 'THIRTEEN'),
        (14, 'FOURTEEN'),
        (15, 'FIFTEEN'),
        (16, 'SIXTEEN'),
        (17, 'SEVENTEEN'),
        (18, 'EIGHTEEN'),
        (19, 'NINETEEN'),
    ],
)
def test_teens(integer, expected_name):
    name = int_to_english(integer)

    assert name == expected_name


@pytest.mark.parametrize(
    'integer, expected_name',
    [
        (10, 'TEN'),
        (20, 'TWENTY'),
        (30, 'THIRTY'),
        (40, 'FORTY'),
        (50, 'FIFTY'),
        (60, 'SIXTY'),
        (70, 'SEVENTY'),
        (80, 'EIGHTY'),
        (90, 'NINETY'),
    ],
)
def test_tys(integer, expected_name):
    name = int_to_english(integer)

    assert name == expected_name


@given(
    integer=st.integers(
        min_value=MIN_INT,
        max_value=-1,
    )
)
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


@given(integer=st.integers(min_value=MIN_INT, max_value=MAX_INT))
def test_manageable_int(integer):
    name = int_to_english(integer)

    assert name != ''


@given(integer=st.integers(min_value=MAX_INT+1))
def test_huge_int(integer):
    with pytest.raises(HugeInt):
        int_to_english(integer)


@given(
    st.one_of(
        st.complex_numbers(),
        st.floats(),
        st.text(),
    )
)
def test_invalid_input(not_an_integer):
    with pytest.raises(RuntimeError):
        int_to_english(not_an_integer)


@pytest.mark.parametrize(
    'integer, expected_count',
    [
        (342, 23),
        (115, 20),
    ],
)
def test_example(integer, expected_count):
    name = int_to_english(integer)
    count = letter_count(name)

    assert count == expected_count


def test_answer():
    answer = problem()

    assert answer == 21124
