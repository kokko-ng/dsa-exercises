"""Tests for interval_list_intersections problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def interval_list_intersections():
    """Get the user's interval_list_intersections implementation."""
    func = get_function("interval_list_intersections")
    if func is None:
        pytest.skip("Function 'interval_list_intersections' not registered. Run check(interval_list_intersections) in notebook.")
    return func


class TestIntervalListIntersectionsBasic:
    """Basic functionality tests."""

    def test_multiple_intersections(self, interval_list_intersections):
        first = [[0, 2], [5, 10], [13, 23], [24, 25]]
        second = [[1, 5], [8, 12], [15, 24], [25, 26]]
        result = interval_list_intersections(first, second)
        assert result == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    def test_first_empty(self, interval_list_intersections):
        result = interval_list_intersections([], [[1, 2]])
        assert result == []

    def test_second_empty(self, interval_list_intersections):
        result = interval_list_intersections([[1, 2]], [])
        assert result == []

    def test_complete_overlap(self, interval_list_intersections):
        result = interval_list_intersections([[0, 10]], [[0, 10]])
        assert result == [[0, 10]]


class TestIntervalListIntersectionsEdgeCases:
    """Edge case tests."""

    def test_both_empty(self, interval_list_intersections):
        result = interval_list_intersections([], [])
        assert result == []

    def test_no_overlap(self, interval_list_intersections):
        result = interval_list_intersections([[1, 2], [5, 6]], [[3, 4], [7, 8]])
        assert result == []

    def test_point_intersection(self, interval_list_intersections):
        result = interval_list_intersections([[1, 5]], [[5, 10]])
        assert result == [[5, 5]]

    def test_contained_intervals(self, interval_list_intersections):
        result = interval_list_intersections([[0, 20]], [[2, 5], [10, 15]])
        assert result == [[2, 5], [10, 15]]


@pytest.mark.performance
class TestIntervalListIntersectionsPerformance:
    """Performance tests."""

    def test_large_input(self, interval_list_intersections):
        n = 5000
        first = [[i * 4, i * 4 + 2] for i in range(n)]
        second = [[i * 4 + 1, i * 4 + 3] for i in range(n)]

        start = time.time()
        result = interval_list_intersections(first, second)
        elapsed = time.time() - start

        assert len(result) == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
