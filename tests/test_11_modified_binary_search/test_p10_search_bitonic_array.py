"""Tests for search_bitonic_array problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def search_bitonic_array():
    func = get_function("search_bitonic_array")
    if func is None:
        pytest.skip("Function 'search_bitonic_array' not registered.")
    return func


class TestSearchBitonicArrayBasic:
    """Basic functionality tests."""

    def test_found_in_decreasing(self, search_bitonic_array):
        assert search_bitonic_array([1, 3, 8, 4, 3], 4) == 3

    def test_found_at_peak(self, search_bitonic_array):
        assert search_bitonic_array([3, 8, 3, 1], 8) == 1

    def test_found_in_increasing(self, search_bitonic_array):
        assert search_bitonic_array([1, 3, 8, 12], 3) == 1

    def test_found_only_decreasing(self, search_bitonic_array):
        assert search_bitonic_array([10, 9, 8], 10) == 0

    def test_not_found(self, search_bitonic_array):
        assert search_bitonic_array([1, 3, 8, 4, 3], 5) == -1


class TestSearchBitonicArrayEdgeCases:
    """Edge case tests."""

    def test_three_elements_found_first(self, search_bitonic_array):
        assert search_bitonic_array([1, 5, 2], 1) == 0

    def test_three_elements_found_peak(self, search_bitonic_array):
        assert search_bitonic_array([1, 5, 2], 5) == 1

    def test_three_elements_found_last(self, search_bitonic_array):
        assert search_bitonic_array([1, 5, 2], 2) == 2

    def test_target_larger_than_peak(self, search_bitonic_array):
        assert search_bitonic_array([1, 3, 8, 4, 2], 10) == -1

    def test_found_at_first(self, search_bitonic_array):
        assert search_bitonic_array([1, 3, 8, 4, 2], 1) == 0

    def test_found_at_last(self, search_bitonic_array):
        assert search_bitonic_array([1, 3, 8, 4, 2], 2) == 4


@pytest.mark.performance
class TestSearchBitonicArrayPerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_input(self, search_bitonic_array):
        n = 500000
        # Create bitonic array
        nums = list(range(n)) + list(range(n - 2, -1, -1))

        start = time.time()
        result = search_bitonic_array(nums, n - 1)
        elapsed = time.time() - start

        assert result == n - 1
        assert elapsed < 0.1
