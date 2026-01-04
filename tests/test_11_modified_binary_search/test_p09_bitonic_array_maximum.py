"""Tests for bitonic_array_maximum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def bitonic_array_maximum():
    func = get_function("bitonic_array_maximum")
    if func is None:
        pytest.skip("Function 'bitonic_array_maximum' not registered.")
    return func


class TestBitonicArrayMaximumBasic:
    """Basic functionality tests."""

    def test_peak_in_middle(self, bitonic_array_maximum):
        assert bitonic_array_maximum([1, 3, 8, 12, 4, 2]) == 12

    def test_peak_early(self, bitonic_array_maximum):
        assert bitonic_array_maximum([3, 8, 3, 1]) == 8

    def test_only_increasing(self, bitonic_array_maximum):
        assert bitonic_array_maximum([1, 3, 8, 12]) == 12

    def test_only_decreasing(self, bitonic_array_maximum):
        assert bitonic_array_maximum([12, 8, 3, 1]) == 12


class TestBitonicArrayMaximumEdgeCases:
    """Edge case tests."""

    def test_three_elements_peak_middle(self, bitonic_array_maximum):
        assert bitonic_array_maximum([1, 5, 2]) == 5

    def test_three_elements_increasing(self, bitonic_array_maximum):
        assert bitonic_array_maximum([1, 2, 3]) == 3

    def test_three_elements_decreasing(self, bitonic_array_maximum):
        assert bitonic_array_maximum([3, 2, 1]) == 3

    def test_peak_at_second_position(self, bitonic_array_maximum):
        assert bitonic_array_maximum([1, 100, 50, 25, 10]) == 100

    def test_peak_at_second_to_last(self, bitonic_array_maximum):
        assert bitonic_array_maximum([10, 25, 50, 100, 1]) == 100


@pytest.mark.performance
class TestBitonicArrayMaximumPerformance:
    """Performance tests - require O(log n) solution."""

    def test_large_input(self, bitonic_array_maximum):
        n = 1000000
        # Create bitonic array: 0, 1, 2, ..., n-1, n-2, ..., 1, 0
        nums = list(range(n)) + list(range(n - 2, -1, -1))

        start = time.time()
        result = bitonic_array_maximum(nums)
        elapsed = time.time() - start

        assert result == n - 1
        assert elapsed < 0.1, f"Solution too slow: {elapsed:.3f}s"
