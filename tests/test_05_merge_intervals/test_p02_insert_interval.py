"""Tests for insert_interval problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def insert_interval():
    """Get the user's insert_interval implementation."""
    func = get_function("insert_interval")
    if func is None:
        pytest.skip("Function 'insert_interval' not registered. Run check(insert_interval) in notebook.")
    return func


class TestInsertIntervalBasic:
    """Basic functionality tests."""

    def test_merge_with_one(self, insert_interval):
        result = insert_interval([[1, 3], [6, 9]], [2, 5])
        assert result == [[1, 5], [6, 9]]

    def test_merge_with_multiple(self, insert_interval):
        result = insert_interval([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
        assert result == [[1, 2], [3, 10], [12, 16]]

    def test_no_merge_before(self, insert_interval):
        result = insert_interval([[3, 5], [6, 9]], [1, 2])
        assert result == [[1, 2], [3, 5], [6, 9]]

    def test_no_merge_after(self, insert_interval):
        result = insert_interval([[1, 2], [3, 5]], [6, 8])
        assert result == [[1, 2], [3, 5], [6, 8]]

    def test_no_merge_between(self, insert_interval):
        result = insert_interval([[1, 2], [5, 6]], [3, 4])
        assert result == [[1, 2], [3, 4], [5, 6]]


class TestInsertIntervalEdgeCases:
    """Edge case tests."""

    def test_empty_intervals(self, insert_interval):
        result = insert_interval([], [2, 5])
        assert result == [[2, 5]]

    def test_merge_all(self, insert_interval):
        result = insert_interval([[1, 2], [3, 4], [5, 6]], [0, 10])
        assert result == [[0, 10]]

    def test_touching_intervals(self, insert_interval):
        result = insert_interval([[1, 5]], [5, 7])
        assert result == [[1, 7]]

    def test_contained_interval(self, insert_interval):
        result = insert_interval([[1, 10]], [3, 5])
        assert result == [[1, 10]]


@pytest.mark.performance
class TestInsertIntervalPerformance:
    """Performance tests."""

    def test_large_input(self, insert_interval):
        n = 10000
        intervals = [[i * 3, i * 3 + 1] for i in range(n)]
        new_interval = [n * 3 // 2, n * 3 // 2 + 1]

        start = time.time()
        result = insert_interval(intervals, new_interval)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
