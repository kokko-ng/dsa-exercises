"""Tests for two_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def two_sum():
    """Get the user's two_sum implementation."""
    func = get_function("two_sum")
    if func is None:
        pytest.skip("Function 'two_sum' not registered. Run check(two_sum) in notebook.")
    return func


class TestTwoSumBasic:
    """Basic functionality tests."""

    def test_simple_case(self, two_sum):
        result = two_sum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]

    def test_middle_elements(self, two_sum):
        result = two_sum([3, 2, 4], 6)
        assert sorted(result) == [1, 2]

    def test_duplicate_values(self, two_sum):
        result = two_sum([3, 3], 6)
        assert sorted(result) == [0, 1]

    def test_negative_numbers(self, two_sum):
        result = two_sum([-1, -2, -3, -4, -5], -8)
        assert sorted(result) == [2, 4]

    def test_mixed_signs(self, two_sum):
        result = two_sum([-3, 4, 3, 90], 0)
        assert sorted(result) == [0, 2]


class TestTwoSumEdgeCases:
    """Edge case tests."""

    def test_zeros(self, two_sum):
        result = two_sum([0, 4, 3, 0], 0)
        assert sorted(result) == [0, 3]

    def test_large_numbers(self, two_sum):
        result = two_sum([1000000000, 2, 1000000000], 2000000000)
        assert sorted(result) == [0, 2]

    def test_target_at_end(self, two_sum):
        result = two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19)
        assert sorted(result) == [8, 9]

    def test_negative_target(self, two_sum):
        result = two_sum([5, -10, 3, -6], -16)
        assert sorted(result) == [1, 3]


@pytest.mark.performance
class TestTwoSumPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, two_sum):
        n = 100000
        nums = list(range(n))
        target = n - 1 + n - 2

        start = time.time()
        result = two_sum(nums, target)
        elapsed = time.time() - start

        assert sorted(result) == [n - 2, n - 1]
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
