"""Tests for median_of_sorted_arrays problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def median_of_sorted_arrays():
    func = get_function("median_of_sorted_arrays")
    if func is None:
        pytest.skip("Function 'median_of_sorted_arrays' not registered.")
    return func


class TestMedianOfSortedArraysBasic:
    """Basic functionality tests."""

    def test_odd_total(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1, 3], [2])
        assert result == 2.0

    def test_even_total(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1, 2], [3, 4])
        assert result == 2.5

    def test_same_size_arrays(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1, 2, 3], [4, 5, 6])
        assert result == 3.5

    def test_different_sizes(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1], [2, 3, 4, 5, 6])
        assert result == 3.5


class TestMedianOfSortedArraysEdgeCases:
    """Edge case tests."""

    def test_one_empty(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([], [1, 2, 3])
        assert result == 2.0

    def test_both_single_element(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1], [2])
        assert result == 1.5

    def test_negative_numbers(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([-5, -3, -1], [-2, 0, 2])
        assert result == -1.5

    def test_overlapping_ranges(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1, 3, 5], [2, 4, 6])
        assert result == 3.5

    def test_non_overlapping(self, median_of_sorted_arrays):
        result = median_of_sorted_arrays([1, 2], [5, 6])
        assert result == 3.5


@pytest.mark.performance
class TestMedianOfSortedArraysPerformance:
    """Performance tests - require O(log(m+n)) solution."""

    def test_large_input(self, median_of_sorted_arrays):
        nums1 = list(range(0, 10000, 2))  # Even numbers
        nums2 = list(range(1, 10000, 2))  # Odd numbers

        start = time.time()
        result = median_of_sorted_arrays(nums1, nums2)
        elapsed = time.time() - start

        assert result == 4999.5
        assert elapsed < 0.1  # Should be very fast with O(log n)
