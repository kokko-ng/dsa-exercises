"""Tests for valid_anagram problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def valid_anagram():
    func = get_function("valid_anagram")
    if func is None:
        pytest.skip("Function 'valid_anagram' not registered.")
    return func


class TestValidAnagramBasic:
    def test_true_anagram(self, valid_anagram):
        assert valid_anagram("anagram", "nagaram") is True

    def test_not_anagram(self, valid_anagram):
        assert valid_anagram("rat", "car") is False

    def test_same_string(self, valid_anagram):
        assert valid_anagram("abc", "abc") is True

    def test_different_lengths(self, valid_anagram):
        assert valid_anagram("ab", "abc") is False

    def test_single_char(self, valid_anagram):
        assert valid_anagram("a", "a") is True


class TestValidAnagramEdgeCases:
    def test_empty_strings(self, valid_anagram):
        assert valid_anagram("", "") is True

    def test_repeated_chars(self, valid_anagram):
        assert valid_anagram("aabb", "abab") is True

    def test_same_chars_different_count(self, valid_anagram):
        assert valid_anagram("aab", "abb") is False

    def test_long_anagram(self, valid_anagram):
        s = "abcdefghijklmnopqrstuvwxyz" * 10
        t = s[::-1]
        assert valid_anagram(s, t) is True


@pytest.mark.performance
class TestValidAnagramPerformance:
    def test_large_input(self, valid_anagram):
        s = "abcdefghij" * 5000
        t = "jihgfedcba" * 5000

        start = time.time()
        result = valid_anagram(s, t)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 1.0
