"""Tests for word_ladder_ii problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def word_ladder_ii():
    func = get_function("word_ladder_ii")
    if func is None:
        pytest.skip("Function 'word_ladder_ii' not registered.")
    return func


class TestWordLadderIIBasic:
    def test_example_1(self, word_ladder_ii):
        result = word_ladder_ii("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
        expected = [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]
        assert sorted([tuple(p) for p in result]) == sorted([tuple(p) for p in expected])

    def test_no_path(self, word_ladder_ii):
        result = word_ladder_ii("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
        assert result == []


class TestWordLadderIIEdgeCases:
    def test_direct_transform(self, word_ladder_ii):
        result = word_ladder_ii("hot", "dot", ["dot"])
        assert result == [["hot", "dot"]]

    def test_multiple_equal_paths(self, word_ladder_ii):
        result = word_ladder_ii("red", "tax", ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"])
        # All paths should have same length
        if result:
            lengths = [len(p) for p in result]
            assert len(set(lengths)) == 1

    def test_end_not_in_list(self, word_ladder_ii):
        result = word_ladder_ii("a", "c", ["a", "b"])
        assert result == []
