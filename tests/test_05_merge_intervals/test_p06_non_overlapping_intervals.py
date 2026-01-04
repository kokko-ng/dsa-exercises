"""Tests for non_overlapping_intervals problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def non_overlapping_intervals():
    """Get the user's non_overlapping_intervals implementation."""
    func = get_function("non_overlapping_intervals")
    if func is None:
        pytest.skip("Function 'non_overlapping_intervals' not registered. Run check(non_overlapping_intervals) in notebook.")
    return func


class TestNonOverlappingIntervalsBasic:
    """Basic functionality tests."""

    def test_remove_one(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])
        assert result == 1

    def test_remove_two_duplicates(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 2], [1, 2], [1, 2]])
        assert result == 2

    def test_no_removal(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 2], [2, 3]])
        assert result == 0

    def test_all_overlap(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 4], [2, 5], [3, 6]])
        assert result == 2


class TestNonOverlappingIntervalsEdgeCases:
    """Edge case tests."""

    def test_single_interval(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 2]])
        assert result == 0

    def test_nested_intervals(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 10], [2, 3], [4, 5]])
        assert result == 1  # Remove the big one

    def test_touching_intervals(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[1, 2], [2, 3], [3, 4]])
        assert result == 0

    def test_negative_intervals(self, non_overlapping_intervals):
        result = non_overlapping_intervals([[-2, 0], [-1, 1], [0, 2]])
        assert result == 1


@pytest.mark.performance
class TestNonOverlappingIntervalsPerformance:
    """Performance tests."""

    def test_large_input(self, non_overlapping_intervals):
        n = 50000
        intervals = [[i, i + 2] for i in range(n)]

        start = time.time()
        result = non_overlapping_intervals(intervals)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
