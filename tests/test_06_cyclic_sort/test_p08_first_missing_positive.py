"""Tests for first_missing_positive problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def first_missing_positive():
    """Get the user's first_missing_positive implementation."""
    func = get_function("first_missing_positive")
    if func is None:
        pytest.skip("Function 'first_missing_positive' not registered. Run check(first_missing_positive) in notebook.")
    return func


class TestFirstMissingPositiveBasic:
    """Basic functionality tests."""

    def test_with_zero(self, first_missing_positive):
        result = first_missing_positive([1, 2, 0])
        assert result == 3

    def test_with_negatives(self, first_missing_positive):
        result = first_missing_positive([3, 4, -1, 1])
        assert result == 2

    def test_all_large(self, first_missing_positive):
        result = first_missing_positive([7, 8, 9, 11, 12])
        assert result == 1

    def test_sequential(self, first_missing_positive):
        result = first_missing_positive([1, 2, 3, 4, 5])
        assert result == 6


class TestFirstMissingPositiveEdgeCases:
    """Edge case tests."""

    def test_single_one(self, first_missing_positive):
        result = first_missing_positive([1])
        assert result == 2

    def test_single_two(self, first_missing_positive):
        result = first_missing_positive([2])
        assert result == 1

    def test_duplicates(self, first_missing_positive):
        result = first_missing_positive([1, 1])
        assert result == 2

    def test_all_negative(self, first_missing_positive):
        result = first_missing_positive([-1, -2, -3])
        assert result == 1


@pytest.mark.performance
class TestFirstMissingPositivePerformance:
    """Performance tests."""

    def test_large_input(self, first_missing_positive):
        n = 100000
        nums = list(range(1, n + 1))

        start = time.time()
        result = first_missing_positive(nums)
        elapsed = time.time() - start

        assert result == n + 1
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"

    def test_large_with_gap(self, first_missing_positive):
        n = 100000
        nums = [1] + list(range(3, n + 3))

        start = time.time()
        result = first_missing_positive(nums)
        elapsed = time.time() - start

        assert result == 2
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
