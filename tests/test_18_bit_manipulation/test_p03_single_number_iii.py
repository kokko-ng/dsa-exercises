"""Tests for single_number_iii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def single_number_iii():
    """Get the user's single_number_iii implementation."""
    func = get_function("single_number_iii")
    if func is None:
        pytest.skip("Function 'single_number_iii' not registered. Run check(single_number_iii) in notebook.")
    return func


class TestSingleNumberIIIBasic:
    """Basic functionality tests."""

    def test_simple_case(self, single_number_iii):
        result = single_number_iii([1, 2, 1, 3, 2, 5])
        assert sorted(result) == [3, 5]

    def test_two_elements(self, single_number_iii):
        result = single_number_iii([-1, 0])
        assert sorted(result) == [-1, 0]

    def test_positive_pair(self, single_number_iii):
        result = single_number_iii([0, 1])
        assert sorted(result) == [0, 1]

    def test_with_duplicates(self, single_number_iii):
        result = single_number_iii([1, 1, 2, 2, 3, 4])
        assert sorted(result) == [3, 4]


class TestSingleNumberIIIEdgeCases:
    """Edge case tests."""

    def test_both_negative(self, single_number_iii):
        result = single_number_iii([-1, -2, 1, 1])
        assert sorted(result) == [-2, -1]

    def test_mixed_signs(self, single_number_iii):
        result = single_number_iii([-5, 5, 1, 1])
        assert sorted(result) == [-5, 5]

    def test_with_zero(self, single_number_iii):
        result = single_number_iii([0, 1, 2, 2])
        assert sorted(result) == [0, 1]

    def test_larger_numbers(self, single_number_iii):
        result = single_number_iii([1000000, 999999, 1, 1])
        assert sorted(result) == [999999, 1000000]

    def test_adjacent_unique(self, single_number_iii):
        result = single_number_iii([3, 4, 1, 1, 2, 2])
        assert sorted(result) == [3, 4]


@pytest.mark.performance
class TestSingleNumberIIIPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, single_number_iii):
        n = 15000
        nums = []
        for i in range(n):
            nums.extend([i, i])
        nums.extend([n, n + 1])  # The two unique numbers

        start = time.time()
        result = single_number_iii(nums)
        elapsed = time.time() - start

        assert sorted(result) == [n, n + 1]
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
