"""Tests for longest_substring_without_repeating problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_substring_without_repeating():
    func = get_function("longest_substring_without_repeating")
    if func is None:
        pytest.skip("Function 'longest_substring_without_repeating' not registered.")
    return func


class TestLongestSubstringBasic:
    def test_example_1(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("abcabcbb") == 3

    def test_all_same(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("bbbbb") == 1

    def test_example_3(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("pwwkew") == 3


class TestLongestSubstringEdgeCases:
    def test_empty_string(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("") == 0

    def test_single_char(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("a") == 1

    def test_all_unique(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("abcdef") == 6

    def test_with_spaces(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("ab cd") == 5

    def test_with_numbers(self, longest_substring_without_repeating):
        assert longest_substring_without_repeating("a1b2c3") == 6


@pytest.mark.performance
class TestLongestSubstringPerformance:
    def test_large_input(self, longest_substring_without_repeating):
        # Long string with repeating pattern
        s = "abcdefghij" * 5000

        start = time.time()
        result = longest_substring_without_repeating(s)
        elapsed = time.time() - start

        assert result == 10
        assert elapsed < 1.0
