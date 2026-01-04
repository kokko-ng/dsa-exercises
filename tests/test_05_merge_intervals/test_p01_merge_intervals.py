"""Tests for merge_intervals problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def merge_intervals():
    """Get the user's merge_intervals implementation."""
    func = get_function("merge_intervals")
    if func is None:
        pytest.skip("Function 'merge_intervals' not registered. Run check(merge_intervals) in notebook.")
    return func


class TestMergeIntervalsBasic:
    """Basic functionality tests."""

    def test_overlapping_intervals(self, merge_intervals):
        result = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
        assert result == [[1, 6], [8, 10], [15, 18]]

    def test_touching_intervals(self, merge_intervals):
        result = merge_intervals([[1, 4], [4, 5]])
        assert result == [[1, 5]]

    def test_no_overlap(self, merge_intervals):
        result = merge_intervals([[1, 2], [3, 4], [5, 6]])
        assert result == [[1, 2], [3, 4], [5, 6]]

    def test_all_overlap(self, merge_intervals):
        result = merge_intervals([[1, 10], [2, 6], [3, 5], [7, 9]])
        assert result == [[1, 10]]

    def test_single_interval(self, merge_intervals):
        result = merge_intervals([[1, 5]])
        assert result == [[1, 5]]


class TestMergeIntervalsEdgeCases:
    """Edge case tests."""

    def test_unsorted_input(self, merge_intervals):
        result = merge_intervals([[3, 5], [1, 4]])
        assert result == [[1, 5]]

    def test_nested_intervals(self, merge_intervals):
        result = merge_intervals([[1, 10], [2, 3], [4, 5], [6, 7]])
        assert result == [[1, 10]]

    def test_identical_intervals(self, merge_intervals):
        result = merge_intervals([[1, 3], [1, 3], [1, 3]])
        assert result == [[1, 3]]

    def test_chain_merge(self, merge_intervals):
        result = merge_intervals([[1, 2], [2, 3], [3, 4], [4, 5]])
        assert result == [[1, 5]]


@pytest.mark.performance
class TestMergeIntervalsPerformance:
    """Performance tests."""

    def test_large_input(self, merge_intervals):
        n = 10000
        intervals = [[i, i + 2] for i in range(0, n * 2, 2)]

        start = time.time()
        result = merge_intervals(intervals)
        elapsed = time.time() - start

        assert len(result) == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
