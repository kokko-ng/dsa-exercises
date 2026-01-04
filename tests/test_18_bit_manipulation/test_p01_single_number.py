"""Tests for single_number problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def single_number():
    """Get the user's single_number implementation."""
    func = get_function("single_number")
    if func is None:
        pytest.skip("Function 'single_number' not registered. Run check(single_number) in notebook.")
    return func


class TestSingleNumberBasic:
    """Basic functionality tests."""

    def test_simple_case(self, single_number):
        result = single_number([2, 2, 1])
        assert result == 1

    def test_middle_unique(self, single_number):
        result = single_number([4, 1, 2, 1, 2])
        assert result == 4

    def test_single_element(self, single_number):
        result = single_number([1])
        assert result == 1

    def test_larger_numbers(self, single_number):
        result = single_number([100, 200, 100, 300, 200])
        assert result == 300

    def test_zeros_with_unique(self, single_number):
        result = single_number([0, 0, 5])
        assert result == 5


class TestSingleNumberEdgeCases:
    """Edge case tests."""

    def test_negative_numbers(self, single_number):
        result = single_number([-1, -1, -2])
        assert result == -2

    def test_mixed_signs(self, single_number):
        result = single_number([-1, 1, -1])
        assert result == 1

    def test_unique_at_start(self, single_number):
        result = single_number([5, 1, 1, 2, 2])
        assert result == 5

    def test_unique_at_end(self, single_number):
        result = single_number([1, 1, 2, 2, 5])
        assert result == 5

    def test_large_values(self, single_number):
        result = single_number([30000, -30000, 30000])
        assert result == -30000


@pytest.mark.performance
class TestSingleNumberPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, single_number):
        n = 30000
        nums = []
        for i in range(n):
            nums.extend([i, i])
        nums.append(n)  # The unique number

        start = time.time()
        result = single_number(nums)
        elapsed = time.time() - start

        assert result == n
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
