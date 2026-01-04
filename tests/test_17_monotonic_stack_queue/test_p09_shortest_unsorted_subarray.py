"""Tests for shortest_unsorted_subarray problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def shortest_unsorted_subarray():
    """Get the user's shortest_unsorted_subarray implementation."""
    func = get_function("shortest_unsorted_subarray")
    if func is None:
        pytest.skip("Function 'shortest_unsorted_subarray' not registered. Run check(shortest_unsorted_subarray) in notebook.")
    return func


class TestShortestUnsortedSubarrayBasic:
    """Basic functionality tests."""

    def test_example_case(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([2, 6, 4, 8, 10, 9, 15])
        assert result == 5

    def test_already_sorted(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([1, 2, 3, 4])
        assert result == 0

    def test_single_element(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([1])
        assert result == 0

    def test_reversed(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([4, 3, 2, 1])
        assert result == 4

    def test_unsorted_at_end(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([1, 2, 3, 5, 4])
        assert result == 2


class TestShortestUnsortedSubarrayEdgeCases:
    """Edge case tests."""

    def test_two_elements_sorted(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([1, 2])
        assert result == 0

    def test_two_elements_unsorted(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([2, 1])
        assert result == 2

    def test_all_same(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([5, 5, 5, 5])
        assert result == 0

    def test_unsorted_at_start(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([3, 2, 1, 4, 5])
        assert result == 3

    def test_one_out_of_place(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([1, 3, 2, 4, 5])
        assert result == 2

    def test_negative_numbers(self, shortest_unsorted_subarray):
        result = shortest_unsorted_subarray([-5, -3, -4, -2, -1])
        assert result == 3


@pytest.mark.performance
class TestShortestUnsortedSubarrayPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, shortest_unsorted_subarray):
        n = 100000
        nums = list(range(n))
        nums[n // 2] = n  # One element out of place

        start = time.time()
        result = shortest_unsorted_subarray(nums)
        elapsed = time.time() - start

        assert result == n // 2
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
