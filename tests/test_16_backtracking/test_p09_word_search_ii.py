"""Tests for word_search_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_search_ii():
    func = get_function("word_search_ii")
    if func is None:
        pytest.skip("Function 'word_search_ii' not registered.")
    return func


class TestWordSearchIIBasic:
    def test_example_1(self, word_search_ii):
        board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
        words = ["oath", "pea", "eat", "rain"]
        result = word_search_ii(board, words)
        assert sorted(result) == sorted(["eat", "oath"])

    def test_example_2(self, word_search_ii):
        board = [["a", "b"], ["c", "d"]]
        words = ["abcb"]
        result = word_search_ii(board, words)
        assert result == []


class TestWordSearchIIEdgeCases:
    def test_single_letter_words(self, word_search_ii):
        board = [["a", "b"], ["c", "d"]]
        words = ["a", "b", "c", "d", "e"]
        result = word_search_ii(board, words)
        assert sorted(result) == ["a", "b", "c", "d"]

    def test_no_matches(self, word_search_ii):
        board = [["a", "b"], ["c", "d"]]
        words = ["xyz", "pqr"]
        result = word_search_ii(board, words)
        assert result == []


@pytest.mark.performance
class TestWordSearchIIPerformance:
    def test_medium_input(self, word_search_ii):
        board = [["a"] * 6 for _ in range(6)]
        words = ["a", "aa", "aaa"]

        start = time.time()
        result = word_search_ii(board, words)
        elapsed = time.time() - start

        assert "a" in result
        assert elapsed < 2.0
