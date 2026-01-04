"""Tests for word_break_ii problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_break_ii():
    func = get_function("word_break_ii")
    if func is None:
        pytest.skip("Function 'word_break_ii' not registered.")
    return func


class TestWordBreakIIBasic:
    def test_example_1(self, word_break_ii):
        result = word_break_ii("catsanddog", ["cat", "cats", "and", "sand", "dog"])
        expected = ["cats and dog", "cat sand dog"]
        assert sorted(result) == sorted(expected)

    def test_example_2(self, word_break_ii):
        result = word_break_ii("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
        expected = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        assert sorted(result) == sorted(expected)


class TestWordBreakIIEdgeCases:
    def test_no_solution(self, word_break_ii):
        result = word_break_ii("catsandog", ["cats", "dog", "sand", "and", "cat"])
        assert result == []

    def test_single_word(self, word_break_ii):
        result = word_break_ii("a", ["a"])
        assert result == ["a"]

    def test_multiple_same_word(self, word_break_ii):
        result = word_break_ii("aa", ["a"])
        assert result == ["a a"]
