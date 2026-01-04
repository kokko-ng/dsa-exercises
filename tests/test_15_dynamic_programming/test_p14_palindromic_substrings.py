"""Tests for palindromic_substrings problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def palindromic_substrings():
    func = get_function("palindromic_substrings")
    if func is None:
        pytest.skip("Function 'palindromic_substrings' not registered.")
    return func


class TestPalindromicSubstringsBasic:
    def test_example_1(self, palindromic_substrings):
        assert palindromic_substrings("abc") == 3

    def test_example_2(self, palindromic_substrings):
        assert palindromic_substrings("aaa") == 6


class TestPalindromicSubstringsEdgeCases:
    def test_single_char(self, palindromic_substrings):
        assert palindromic_substrings("a") == 1

    def test_two_same(self, palindromic_substrings):
        assert palindromic_substrings("aa") == 3  # a, a, aa

    def test_two_different(self, palindromic_substrings):
        assert palindromic_substrings("ab") == 2  # a, b


@pytest.mark.performance
class TestPalindromicSubstringsPerformance:
    def test_large_input(self, palindromic_substrings):
        s = "a" * 1000

        start = time.time()
        result = palindromic_substrings(s)
        elapsed = time.time() - start

        assert result == 1000 * 1001 // 2  # n*(n+1)/2
        assert elapsed < 2.0
