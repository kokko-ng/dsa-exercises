"""Tests for longest_palindromic_substring problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


def is_palindrome(s):
    return s == s[::-1]


@pytest.fixture
def longest_palindromic_substring():
    func = get_function("longest_palindromic_substring")
    if func is None:
        pytest.skip("Function 'longest_palindromic_substring' not registered.")
    return func


class TestLongestPalindromicSubstringBasic:
    def test_example_1(self, longest_palindromic_substring):
        result = longest_palindromic_substring("babad")
        assert result in ["bab", "aba"]
        assert is_palindrome(result)

    def test_example_2(self, longest_palindromic_substring):
        result = longest_palindromic_substring("cbbd")
        assert result == "bb"


class TestLongestPalindromicSubstringEdgeCases:
    def test_single_char(self, longest_palindromic_substring):
        assert longest_palindromic_substring("a") == "a"

    def test_all_same(self, longest_palindromic_substring):
        result = longest_palindromic_substring("aaaa")
        assert result == "aaaa"

    def test_no_palindrome(self, longest_palindromic_substring):
        result = longest_palindromic_substring("abcd")
        assert len(result) == 1


@pytest.mark.performance
class TestLongestPalindromicSubstringPerformance:
    def test_large_input(self, longest_palindromic_substring):
        s = "a" * 500 + "b" * 500

        start = time.time()
        result = longest_palindromic_substring(s)
        elapsed = time.time() - start

        assert is_palindrome(result)
        assert elapsed < 2.0
