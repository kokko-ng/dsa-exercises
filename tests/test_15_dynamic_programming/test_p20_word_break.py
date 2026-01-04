"""Tests for word_break problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_break():
    func = get_function("word_break")
    if func is None:
        pytest.skip("Function 'word_break' not registered.")
    return func


class TestWordBreakBasic:
    def test_example_1(self, word_break):
        assert word_break("leetcode", ["leet", "code"]) is True

    def test_example_2(self, word_break):
        assert word_break("applepenapple", ["apple", "pen"]) is True

    def test_example_3(self, word_break):
        assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) is False


class TestWordBreakEdgeCases:
    def test_single_word(self, word_break):
        assert word_break("a", ["a"]) is True

    def test_no_match(self, word_break):
        assert word_break("abc", ["d", "e", "f"]) is False

    def test_reuse_word(self, word_break):
        assert word_break("aaaa", ["a", "aa"]) is True


@pytest.mark.performance
class TestWordBreakPerformance:
    def test_large_input(self, word_break):
        s = "a" * 300
        word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa"]

        start = time.time()
        result = word_break(s, word_dict)
        elapsed = time.time() - start

        assert result is True
        assert elapsed < 2.0
