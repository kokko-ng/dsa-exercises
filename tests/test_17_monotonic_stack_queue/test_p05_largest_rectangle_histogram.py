"""Tests for largest_rectangle_histogram problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def largest_rectangle_histogram():
    """Get the user's largest_rectangle_histogram implementation."""
    func = get_function("largest_rectangle_histogram")
    if func is None:
        pytest.skip("Function 'largest_rectangle_histogram' not registered. Run check(largest_rectangle_histogram) in notebook.")
    return func


class TestLargestRectangleHistogramBasic:
    """Basic functionality tests."""

    def test_example_case(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([2, 1, 5, 6, 2, 3])
        assert result == 10

    def test_two_bars(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([2, 4])
        assert result == 4

    def test_complex_histogram(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([6, 2, 5, 4, 5, 1, 6])
        assert result == 12

    def test_increasing(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([1, 2, 3, 4, 5])
        assert result == 9  # 3 * 3

    def test_decreasing(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([5, 4, 3, 2, 1])
        assert result == 9  # 3 * 3


class TestLargestRectangleHistogramEdgeCases:
    """Edge case tests."""

    def test_single_bar(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([5])
        assert result == 5

    def test_all_same_height(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([3, 3, 3, 3])
        assert result == 12

    def test_with_zeros(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([2, 0, 2])
        assert result == 2

    def test_tall_single_bar(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([1, 1, 100, 1, 1])
        assert result == 100

    def test_plateau(self, largest_rectangle_histogram):
        result = largest_rectangle_histogram([1, 2, 3, 3, 3, 2, 1])
        assert result == 9  # 3 * 3


@pytest.mark.performance
class TestLargestRectangleHistogramPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, largest_rectangle_histogram):
        n = 100000
        heights = [1] * n

        start = time.time()
        result = largest_rectangle_histogram(heights)
        elapsed = time.time() - start

        assert result == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
