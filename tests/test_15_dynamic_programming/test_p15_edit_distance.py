"""Tests for edit_distance problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def edit_distance():
    func = get_function("edit_distance")
    if func is None:
        pytest.skip("Function 'edit_distance' not registered.")
    return func


class TestEditDistanceBasic:
    def test_example_1(self, edit_distance):
        assert edit_distance("horse", "ros") == 3

    def test_example_2(self, edit_distance):
        assert edit_distance("intention", "execution") == 5


class TestEditDistanceEdgeCases:
    def test_empty_strings(self, edit_distance):
        assert edit_distance("", "") == 0

    def test_one_empty(self, edit_distance):
        assert edit_distance("abc", "") == 3
        assert edit_distance("", "abc") == 3

    def test_same_strings(self, edit_distance):
        assert edit_distance("abc", "abc") == 0

    def test_single_char(self, edit_distance):
        assert edit_distance("a", "b") == 1


@pytest.mark.performance
class TestEditDistancePerformance:
    def test_large_input(self, edit_distance):
        word1 = "a" * 200
        word2 = "b" * 200

        start = time.time()
        result = edit_distance(word1, word2)
        elapsed = time.time() - start

        assert result == 200
        assert elapsed < 2.0
