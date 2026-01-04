"""Tests for first_k_missing_positive problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def first_k_missing_positive():
    """Get the user's first_k_missing_positive implementation."""
    func = get_function("first_k_missing_positive")
    if func is None:
        pytest.skip("Function 'first_k_missing_positive' not registered. Run check(first_k_missing_positive) in notebook.")
    return func


class TestFirstKMissingPositiveBasic:
    """Basic functionality tests."""

    def test_with_negatives_and_duplicates(self, first_k_missing_positive):
        result = first_k_missing_positive([3, -1, 4, 5, 5], 3)
        assert result == [1, 2, 6]

    def test_missing_first(self, first_k_missing_positive):
        result = first_k_missing_positive([2, 3, 4], 3)
        assert result == [1, 5, 6]

    def test_all_negative(self, first_k_missing_positive):
        result = first_k_missing_positive([-2, -3, 4], 2)
        assert result == [1, 2]

    def test_sequential(self, first_k_missing_positive):
        result = first_k_missing_positive([1, 2, 3], 3)
        assert result == [4, 5, 6]


class TestFirstKMissingPositiveEdgeCases:
    """Edge case tests."""

    def test_single_element(self, first_k_missing_positive):
        result = first_k_missing_positive([1], 3)
        assert result == [2, 3, 4]

    def test_k_equals_one(self, first_k_missing_positive):
        result = first_k_missing_positive([2, 3, 4], 1)
        assert result == [1]

    def test_large_numbers(self, first_k_missing_positive):
        result = first_k_missing_positive([100, 200, 300], 3)
        assert result == [1, 2, 3]


@pytest.mark.performance
class TestFirstKMissingPositivePerformance:
    """Performance tests."""

    def test_large_input(self, first_k_missing_positive):
        n = 100000
        k = 100
        nums = list(range(2, n + 2))  # Missing 1

        start = time.time()
        result = first_k_missing_positive(nums, k)
        elapsed = time.time() - start

        assert result[0] == 1
        assert len(result) == k
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s"
