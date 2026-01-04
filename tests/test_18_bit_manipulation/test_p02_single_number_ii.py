"""Tests for single_number_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def single_number_ii():
    """Get the user's single_number_ii implementation."""
    func = get_function("single_number_ii")
    if func is None:
        pytest.skip("Function 'single_number_ii' not registered. Run check(single_number_ii) in notebook.")
    return func


class TestSingleNumberIIBasic:
    """Basic functionality tests."""

    def test_simple_case(self, single_number_ii):
        result = single_number_ii([2, 2, 3, 2])
        assert result == 3

    def test_longer_array(self, single_number_ii):
        result = single_number_ii([0, 1, 0, 1, 0, 1, 99])
        assert result == 99

    def test_single_at_start(self, single_number_ii):
        result = single_number_ii([5, 1, 1, 1])
        assert result == 5

    def test_single_at_end(self, single_number_ii):
        result = single_number_ii([1, 1, 1, 5])
        assert result == 5


class TestSingleNumberIIEdgeCases:
    """Edge case tests."""

    def test_negative_unique(self, single_number_ii):
        result = single_number_ii([1, 1, 1, -5])
        assert result == -5

    def test_all_negative(self, single_number_ii):
        result = single_number_ii([-2, -2, -2, -1])
        assert result == -1

    def test_zero_unique(self, single_number_ii):
        result = single_number_ii([1, 1, 1, 0])
        assert result == 0

    def test_mixed_signs(self, single_number_ii):
        result = single_number_ii([-1, -1, -1, 2, 2, 2, 5])
        assert result == 5

    def test_large_positive(self, single_number_ii):
        result = single_number_ii([2147483647, 1, 1, 1])
        assert result == 2147483647

    def test_large_negative(self, single_number_ii):
        result = single_number_ii([-2147483648, 1, 1, 1])
        assert result == -2147483648


@pytest.mark.performance
class TestSingleNumberIIPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, single_number_ii):
        n = 10000
        nums = []
        for i in range(n):
            nums.extend([i, i, i])
        nums.append(n)  # The unique number

        start = time.time()
        result = single_number_ii(nums)
        elapsed = time.time() - start

        assert result == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
