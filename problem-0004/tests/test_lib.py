from p0004.lib import is_palindrome
from p0004.lib import largest_palindrome_product
from p0004.lib import products


class TestIsPalindrome:

    def test_palindrome(self):
        assert is_palindrome('racecar')

    def test_palindrome_number(self):
        assert is_palindrome('1331')

    def test_not_palindrome(self):
        assert not is_palindrome('car race')

    def test_not_palindrome_number(self):
        assert not is_palindrome('1337')


def test_largest_palindrome():
    assert largest_palindrome_product(2) == 9009
