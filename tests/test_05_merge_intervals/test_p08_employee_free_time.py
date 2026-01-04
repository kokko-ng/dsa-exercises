"""Tests for employee_free_time problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def employee_free_time():
    """Get the user's employee_free_time implementation."""
    func = get_function("employee_free_time")
    if func is None:
        pytest.skip("Function 'employee_free_time' not registered. Run check(employee_free_time) in notebook.")
    return func


class TestEmployeeFreeTimeBasic:
    """Basic functionality tests."""

    def test_one_gap(self, employee_free_time):
        schedule = [[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]
        result = employee_free_time(schedule)
        assert result == [[3, 4]]

    def test_two_gaps(self, employee_free_time):
        schedule = [[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]
        result = employee_free_time(schedule)
        assert result == [[5, 6], [7, 9]]

    def test_no_gaps(self, employee_free_time):
        schedule = [[[1, 10]], [[2, 5]], [[6, 9]]]
        result = employee_free_time(schedule)
        assert result == []

    def test_single_employee(self, employee_free_time):
        schedule = [[[1, 3], [5, 7], [9, 11]]]
        result = employee_free_time(schedule)
        assert result == [[3, 5], [7, 9]]


class TestEmployeeFreeTimeEdgeCases:
    """Edge case tests."""

    def test_single_interval(self, employee_free_time):
        schedule = [[[1, 5]]]
        result = employee_free_time(schedule)
        assert result == []

    def test_adjacent_intervals(self, employee_free_time):
        schedule = [[[1, 2]], [[2, 3]], [[3, 4]]]
        result = employee_free_time(schedule)
        assert result == []

    def test_overlapping_intervals(self, employee_free_time):
        schedule = [[[1, 5]], [[4, 8]], [[7, 10]]]
        result = employee_free_time(schedule)
        assert result == []


@pytest.mark.performance
class TestEmployeeFreeTimePerformance:
    """Performance tests."""

    def test_large_input(self, employee_free_time):
        n_employees = 50
        n_intervals = 50
        schedule = [
            [[i * 4, i * 4 + 2] for i in range(j, j + n_intervals)]
            for j in range(n_employees)
        ]

        start = time.time()
        result = employee_free_time(schedule)
        elapsed = time.time() - start

        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
