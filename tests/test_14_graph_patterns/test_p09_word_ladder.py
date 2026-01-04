"""Tests for word_ladder problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_ladder():
    func = get_function("word_ladder")
    if func is None:
        pytest.skip("Function 'word_ladder' not registered.")
    return func


class TestWordLadderBasic:
    def test_example_1(self, word_ladder):
        result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        assert result == 5

    def test_no_path(self, word_ladder):
        result = word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        assert result == 0

    def test_direct_transform(self, word_ladder):
        result = word_ladder("hot", "dot", ["dot"])
        assert result == 2


class TestWordLadderEdgeCases:
    def test_same_word(self, word_ladder):
        result = word_ladder("hit", "hit", ["hit"])
        assert result == 1 or result == 0  # Depends on interpretation

    def test_single_letter_words(self, word_ladder):
        result = word_ladder("a", "c", ["a", "b", "c"])
        assert result == 2

    def test_end_not_in_list(self, word_ladder):
        result = word_ladder("hit", "cog", ["hot", "dot", "dog"])
        assert result == 0


@pytest.mark.performance
class TestWordLadderPerformance:
    def test_large_word_list(self, word_ladder):
        # Generate a list of words
        words = ["".join([chr(ord('a') + (i + j) % 26) for j in range(4)])
                 for i in range(1000)]
        words = list(set(words))

        start = time.time()
        result = word_ladder("aaaa", "zzzz", words + ["zzzz"])
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 3.0
