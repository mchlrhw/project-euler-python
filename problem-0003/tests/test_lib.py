from p0003.lib import is_prime
from p0003.lib import largest_prime_factor
from p0003.lib import primes
from p0003.lib import prime_factors
from p0003.lib import standard_notation


class TestIsPrime:

    def test_0(self):
        assert is_prime(0) is False

    def test_1(self):
        assert is_prime(1) is False

    def test_2(self):
        assert is_prime(2) is True

    def test_3(self):
        assert is_prime(3) is True

    def test_4(self):
        assert is_prime(4) is False


def test_primes():
    assert list(primes(10)) == [2, 3, 5, 7]


class TestPrimeFactors:

    def test_2(self):
        assert list(prime_factors(2)) == []

    def test_4(self):
        assert list(prime_factors(4)) == [2, 2]

    def test_8(self):
        assert list(prime_factors(8)) == [2, 2, 2]

    def test_10(self):
        assert list(prime_factors(10)) == [2, 5]

    def test_13195(self):
        assert list(prime_factors(13195)) == [5, 7, 13, 29]


def test_largest_prime_factor():
    assert largest_prime_factor(13195) == 29


class TestStandardNotation:

    def test_0(self):
        assert standard_notation(0) == '0'

    def test_1(self):
        assert standard_notation(1) == '1'

    def test_2(self):
        assert standard_notation(2) == '2'

    def test_4(self):
        assert standard_notation(4) == '2**2'

    def test_8(self):
        assert standard_notation(8) == '2**3'

    def test_10(self):
        assert standard_notation(10) == '2 * 5'

    def test_100(self):
        assert standard_notation(100) == '2**2 * 5**2'

    def test_13195(self):
        assert standard_notation(13195) == '5 * 7 * 13 * 29'
