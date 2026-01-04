"""Tests for word_search problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_search():
    func = get_function("word_search")
    if func is None:
        pytest.skip("Function 'word_search' not registered.")
    return func


class TestWordSearchBasic:
    def test_example_1(self, word_search):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert word_search(board, "ABCCED") is True

    def test_example_2(self, word_search):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert word_search(board, "SEE") is True

    def test_example_3(self, word_search):
        board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        assert word_search(board, "ABCB") is False


class TestWordSearchEdgeCases:
    def test_single_cell(self, word_search):
        board = [["A"]]
        assert word_search(board, "A") is True
        assert word_search(board, "B") is False

    def test_word_not_exist(self, word_search):
        board = [["A", "B"], ["C", "D"]]
        assert word_search(board, "ABDC") is True
        assert word_search(board, "XYZ") is False

    def test_no_reuse(self, word_search):
        board = [["A", "B"], ["C", "D"]]
        assert word_search(board, "ABCD") is False  # Can't reuse cells
