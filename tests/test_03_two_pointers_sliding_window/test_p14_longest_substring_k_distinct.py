"""Tests for longest_substring_k_distinct problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def longest_substring_k_distinct():
    func = get_function("longest_substring_k_distinct")
    if func is None:
        pytest.skip("Function 'longest_substring_k_distinct' not registered.")
    return func


class TestLongestSubstringBasic:
    def test_example_1(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("eceba", 2) == 3

    def test_example_2(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("aa", 1) == 2


class TestLongestSubstringEdgeCases:
    def test_k_zero(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("abc", 0) == 0

    def test_k_greater_than_distinct(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("abc", 5) == 3

    def test_single_char(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("a", 1) == 1

    def test_all_same(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("aaaa", 1) == 4

    def test_empty_string(self, longest_substring_k_distinct):
        assert longest_substring_k_distinct("", 2) == 0


@pytest.mark.performance
class TestLongestSubstringPerformance:
    def test_large_input(self, longest_substring_k_distinct):
        s = "abcdef" * 10000

        start = time.time()
        result = longest_substring_k_distinct(s, 3)
        elapsed = time.time() - start

        assert result == 3
        assert elapsed < 1.0
