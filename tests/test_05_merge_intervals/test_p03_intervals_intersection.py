"""Tests for intervals_intersection problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def intervals_intersection():
    """Get the user's intervals_intersection implementation."""
    func = get_function("intervals_intersection")
    if func is None:
        pytest.skip("Function 'intervals_intersection' not registered. Run check(intervals_intersection) in notebook.")
    return func


class TestIntervalsIntersectionBasic:
    """Basic functionality tests."""

    def test_multiple_intersections(self, intervals_intersection):
        first = [[0, 2], [5, 10], [13, 23], [24, 25]]
        second = [[1, 5], [8, 12], [15, 24], [25, 26]]
        result = intervals_intersection(first, second)
        assert result == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    def test_one_empty(self, intervals_intersection):
        result = intervals_intersection([[1, 3], [5, 9]], [])
        assert result == []

    def test_no_intersection(self, intervals_intersection):
        result = intervals_intersection([[1, 2], [5, 6]], [[3, 4], [7, 8]])
        assert result == []

    def test_complete_overlap(self, intervals_intersection):
        result = intervals_intersection([[1, 10]], [[1, 10]])
        assert result == [[1, 10]]


class TestIntervalsIntersectionEdgeCases:
    """Edge case tests."""

    def test_both_empty(self, intervals_intersection):
        result = intervals_intersection([], [])
        assert result == []

    def test_single_point_intersection(self, intervals_intersection):
        result = intervals_intersection([[1, 3]], [[3, 5]])
        assert result == [[3, 3]]

    def test_nested_intervals(self, intervals_intersection):
        result = intervals_intersection([[0, 10]], [[2, 3], [5, 6], [8, 9]])
        assert result == [[2, 3], [5, 6], [8, 9]]

    def test_alternating_intervals(self, intervals_intersection):
        result = intervals_intersection([[0, 4], [7, 10]], [[2, 5], [8, 12]])
        assert result == [[2, 4], [8, 10]]


@pytest.mark.performance
class TestIntervalsIntersectionPerformance:
    """Performance tests."""

    def test_large_input(self, intervals_intersection):
        n = 5000
        first = [[i * 4, i * 4 + 2] for i in range(n)]
        second = [[i * 4 + 1, i * 4 + 3] for i in range(n)]

        start = time.time()
        result = intervals_intersection(first, second)
        elapsed = time.time() - start

        assert len(result) == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
