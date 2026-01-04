"""Tests for next_greater_element problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def next_greater_element():
    """Get the user's next_greater_element implementation."""
    func = get_function("next_greater_element")
    if func is None:
        pytest.skip("Function 'next_greater_element' not registered. Run check(next_greater_element) in notebook.")
    return func


class TestNextGreaterElementBasic:
    """Basic functionality tests."""

    def test_mixed_values(self, next_greater_element):
        result = next_greater_element([4, 5, 2, 25])
        assert result == [5, 25, 25, -1]

    def test_decreasing_then_up(self, next_greater_element):
        result = next_greater_element([13, 7, 6, 12])
        assert result == [-1, 12, 12, -1]

    def test_increasing_sequence(self, next_greater_element):
        result = next_greater_element([1, 2, 3, 4])
        assert result == [2, 3, 4, -1]

    def test_decreasing_sequence(self, next_greater_element):
        result = next_greater_element([4, 3, 2, 1])
        assert result == [-1, -1, -1, -1]

    def test_all_same(self, next_greater_element):
        result = next_greater_element([5, 5, 5, 5])
        assert result == [-1, -1, -1, -1]


class TestNextGreaterElementEdgeCases:
    """Edge case tests."""

    def test_single_element(self, next_greater_element):
        result = next_greater_element([42])
        assert result == [-1]

    def test_two_elements_increasing(self, next_greater_element):
        result = next_greater_element([1, 2])
        assert result == [2, -1]

    def test_two_elements_decreasing(self, next_greater_element):
        result = next_greater_element([2, 1])
        assert result == [-1, -1]

    def test_negative_numbers(self, next_greater_element):
        result = next_greater_element([-5, -3, -1, 0])
        assert result == [-3, -1, 0, -1]

    def test_mixed_positive_negative(self, next_greater_element):
        result = next_greater_element([-2, 1, -1, 2])
        assert result == [1, 2, 2, -1]


@pytest.mark.performance
class TestNextGreaterElementPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, next_greater_element):
        n = 100000
        nums = list(range(n, 0, -1))  # Decreasing sequence

        start = time.time()
        result = next_greater_element(nums)
        elapsed = time.time() - start

        assert result == [-1] * n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
