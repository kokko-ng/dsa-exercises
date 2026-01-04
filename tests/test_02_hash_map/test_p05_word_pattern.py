"""Tests for word_pattern problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_pattern():
    func = get_function("word_pattern")
    if func is None:
        pytest.skip("Function 'word_pattern' not registered.")
    return func


class TestWordPatternBasic:
    def test_example_1(self, word_pattern):
        assert word_pattern("abba", "dog cat cat dog") is True

    def test_example_2(self, word_pattern):
        assert word_pattern("abba", "dog cat cat fish") is False

    def test_example_3(self, word_pattern):
        assert word_pattern("aaaa", "dog cat cat dog") is False

    def test_simple_match(self, word_pattern):
        assert word_pattern("ab", "dog cat") is True


class TestWordPatternEdgeCases:
    def test_single_letter_word(self, word_pattern):
        assert word_pattern("a", "dog") is True

    def test_different_lengths(self, word_pattern):
        assert word_pattern("abc", "dog cat") is False

    def test_same_word_different_pattern(self, word_pattern):
        assert word_pattern("ab", "dog dog") is False

    def test_different_word_same_pattern(self, word_pattern):
        assert word_pattern("aa", "dog cat") is False

    def test_all_same(self, word_pattern):
        assert word_pattern("aaa", "dog dog dog") is True

    def test_bijection_required(self, word_pattern):
        # Pattern 'a' maps to 'dog', but 'b' also trying to map to 'dog'
        assert word_pattern("ab", "dog dog") is False
