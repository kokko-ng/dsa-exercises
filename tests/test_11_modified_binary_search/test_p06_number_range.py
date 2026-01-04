"""Tests for number_range problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def number_range():
    func = get_function("number_range")
    if func is None:
        pytest.skip("Function 'number_range' not registered.")
    return func


class TestNumberRangeBasic:
    """Basic functionality tests."""

    def test_range_found(self, number_range):
        assert number_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]

    def test_not_found(self, number_range):
        assert number_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]

    def test_empty_array(self, number_range):
        assert number_range([], 0) == [-1, -1]

    def test_single_occurrence(self, number_range):
        assert number_range([1, 2, 3, 4, 5], 3) == [2, 2]

    def test_all_same(self, number_range):
        assert number_range([5, 5, 5, 5, 5], 5) == [0, 4]


class TestNumberRangeEdgeCases:
    """Edge case tests."""

    def test_single_element_found(self, number_range):
        assert number_range([5], 5) == [0, 0]

    def test_single_element_not_found(self, number_range):
        assert number_range([5], 3) == [-1, -1]

    def test_first_element(self, number_range):
        assert number_range([1, 1, 2, 3], 1) == [0, 1]

    def test_last_element(self, number_range):
        assert number_range([1, 2, 3, 3], 3) == [2, 3]

    def test_target_smaller_than_all(self, number_range):
        assert number_range([2, 3, 4], 1) == [-1, -1]

    def test_target_larger_than_all(self, number_range):
        assert number_range([2, 3, 4], 5) == [-1, -1]


@pytest.mark.performance
class TestNumberRangePerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_input(self, number_range):
        n = 1000000
        nums = [1] * (n // 2) + [2] * (n // 2)

        start = time.time()
        result = number_range(nums, 2)
        elapsed = time.time() - start

        assert result == [n // 2, n - 1]
        assert elapsed < 0.5, f"Solution too slow: {elapsed:.3f}s"
