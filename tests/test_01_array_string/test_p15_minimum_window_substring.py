"""Tests for minimum_window_substring problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_window_substring():
    func = get_function("minimum_window_substring")
    if func is None:
        pytest.skip("Function 'minimum_window_substring' not registered.")
    return func


class TestMinimumWindowSubstringBasic:
    def test_example_1(self, minimum_window_substring):
        assert minimum_window_substring("ADOBECODEBANC", "ABC") == "BANC"

    def test_exact_match(self, minimum_window_substring):
        assert minimum_window_substring("a", "a") == "a"

    def test_no_match(self, minimum_window_substring):
        assert minimum_window_substring("a", "aa") == ""


class TestMinimumWindowSubstringEdgeCases:
    def test_t_longer_than_s(self, minimum_window_substring):
        assert minimum_window_substring("ab", "abc") == ""

    def test_duplicate_chars_in_t(self, minimum_window_substring):
        assert minimum_window_substring("aa", "aa") == "aa"

    def test_t_at_start(self, minimum_window_substring):
        result = minimum_window_substring("ABC", "ABC")
        assert result == "ABC"

    def test_t_at_end(self, minimum_window_substring):
        result = minimum_window_substring("XYZABC", "ABC")
        assert result == "ABC"

    def test_case_sensitive(self, minimum_window_substring):
        assert minimum_window_substring("aA", "a") == "a"


@pytest.mark.performance
class TestMinimumWindowSubstringPerformance:
    def test_large_input(self, minimum_window_substring):
        s = "ABCDEFGHIJ" * 10000
        t = "JIHGFEDCBA"

        start = time.time()
        result = minimum_window_substring(s, t)
        elapsed = time.time() - start

        assert len(result) >= len(t)
        assert elapsed < 2.0
