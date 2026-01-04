"""Tests for sum_of_subarray_minimums problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def sum_of_subarray_minimums():
    """Get the user's sum_of_subarray_minimums implementation."""
    func = get_function("sum_of_subarray_minimums")
    if func is None:
        pytest.skip("Function 'sum_of_subarray_minimums' not registered. Run check(sum_of_subarray_minimums) in notebook.")
    return func


class TestSumOfSubarrayMinimumsBasic:
    """Basic functionality tests."""

    def test_example_case(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([3, 1, 2, 4])
        assert result == 17

    def test_another_example(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([11, 81, 94, 43, 3])
        assert result == 444

    def test_increasing(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([1, 2, 3])
        # [1], [2], [3], [1,2], [2,3], [1,2,3] -> 1+2+3+1+2+1 = 10
        assert result == 10

    def test_decreasing(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([3, 2, 1])
        # [3], [2], [1], [3,2], [2,1], [3,2,1] -> 3+2+1+2+1+1 = 10
        assert result == 10

    def test_all_same(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([2, 2, 2])
        # [2], [2], [2], [2,2], [2,2], [2,2,2] -> 6 subarrays, each min is 2 = 12
        assert result == 12


class TestSumOfSubarrayMinimumsEdgeCases:
    """Edge case tests."""

    def test_single_element(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([5])
        assert result == 5

    def test_two_elements(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([1, 3])
        # [1], [3], [1,3] -> 1+3+1 = 5
        assert result == 5

    def test_duplicates(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([1, 1])
        # [1], [1], [1,1] -> 1+1+1 = 3
        assert result == 3

    def test_valley(self, sum_of_subarray_minimums):
        result = sum_of_subarray_minimums([3, 1, 3])
        # [3], [1], [3], [3,1], [1,3], [3,1,3] -> 3+1+3+1+1+1 = 10
        assert result == 10


@pytest.mark.performance
class TestSumOfSubarrayMinimumsPerformance:
    """Performance tests - require O(n) solution."""

    def test_large_input(self, sum_of_subarray_minimums):
        n = 30000
        arr = list(range(1, n + 1))

        start = time.time()
        result = sum_of_subarray_minimums(arr)
        elapsed = time.time() - start

        assert result > 0
        assert elapsed < 1.0, f"Solution too slow: {elapsed:.2f}s (should be < 1s)"
