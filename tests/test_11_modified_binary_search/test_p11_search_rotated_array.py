"""Tests for search_rotated_array problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def search_rotated_array():
    func = get_function("search_rotated_array")
    if func is None:
        pytest.skip("Function 'search_rotated_array' not registered.")
    return func


class TestSearchRotatedArrayBasic:
    """Basic functionality tests."""

    def test_found_in_right_half(self, search_rotated_array):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_not_found(self, search_rotated_array):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_single_element_not_found(self, search_rotated_array):
        assert search_rotated_array([1], 0) == -1

    def test_found_in_left_half(self, search_rotated_array):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 5) == 1

    def test_not_rotated(self, search_rotated_array):
        assert search_rotated_array([1, 2, 3, 4, 5], 3) == 2


class TestSearchRotatedArrayEdgeCases:
    """Edge case tests."""

    def test_single_element_found(self, search_rotated_array):
        assert search_rotated_array([5], 5) == 0

    def test_two_elements_rotated(self, search_rotated_array):
        assert search_rotated_array([2, 1], 1) == 1

    def test_found_at_pivot(self, search_rotated_array):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 7) == 3

    def test_found_first_element(self, search_rotated_array):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 4) == 0

    def test_found_last_element(self, search_rotated_array):
        assert search_rotated_array([4, 5, 6, 7, 0, 1, 2], 2) == 6

    def test_large_rotation(self, search_rotated_array):
        assert search_rotated_array([3, 4, 5, 1, 2], 1) == 3


@pytest.mark.performance
class TestSearchRotatedArrayPerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_input(self, search_rotated_array):
        n = 1000000
        # Create rotated array
        pivot = n // 3
        nums = list(range(pivot, n)) + list(range(pivot))

        start = time.time()
        result = search_rotated_array(nums, 0)
        elapsed = time.time() - start

        assert result == n - pivot
        assert elapsed < 0.1, f"Solution too slow: {elapsed:.3f}s"
