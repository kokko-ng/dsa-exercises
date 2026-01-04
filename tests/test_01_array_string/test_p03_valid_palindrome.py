"""Tests for valid_palindrome problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def valid_palindrome():
    func = get_function("valid_palindrome")
    if func is None:
        pytest.skip("Function 'valid_palindrome' not registered.")
    return func


class TestValidPalindromeBasic:
    def test_classic_palindrome(self, valid_palindrome):
        assert valid_palindrome("A man, a plan, a canal: Panama") is True

    def test_not_palindrome(self, valid_palindrome):
        assert valid_palindrome("race a car") is False

    def test_simple_palindrome(self, valid_palindrome):
        assert valid_palindrome("aba") is True

    def test_even_palindrome(self, valid_palindrome):
        assert valid_palindrome("abba") is True


class TestValidPalindromeEdgeCases:
    def test_empty_after_filter(self, valid_palindrome):
        assert valid_palindrome(" ") is True

    def test_single_char(self, valid_palindrome):
        assert valid_palindrome("a") is True

    def test_only_numbers(self, valid_palindrome):
        assert valid_palindrome("12321") is True

    def test_mixed_case(self, valid_palindrome):
        assert valid_palindrome("Aa") is True

    def test_special_chars_only(self, valid_palindrome):
        assert valid_palindrome(",.!?") is True

    def test_numbers_and_letters(self, valid_palindrome):
        assert valid_palindrome("0P") is False
