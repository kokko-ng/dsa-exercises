"""Tests for subarray_sum_equals_k problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def subarray_sum_equals_k():
    func = get_function("subarray_sum_equals_k")
    if func is None:
        pytest.skip("Function 'subarray_sum_equals_k' not registered.")
    return func


class TestSubarraySumBasic:
    def test_example_1(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([1, 1, 1], 2) == 2

    def test_example_2(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([1, 2, 3], 3) == 2

    def test_single_element_match(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([5], 5) == 1


class TestSubarraySumEdgeCases:
    def test_single_element_no_match(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([5], 3) == 0

    def test_negative_numbers(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([1, -1, 1, -1], 0) == 4

    def test_all_zeros(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([0, 0, 0], 0) == 6

    def test_entire_array(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([1, 2, 3], 6) == 1

    def test_no_match(self, subarray_sum_equals_k):
        assert subarray_sum_equals_k([1, 2, 3], 10) == 0


@pytest.mark.performance
class TestSubarraySumPerformance:
    def test_large_input(self, subarray_sum_equals_k):
        nums = [1] * 20000
        k = 100

        start = time.time()
        result = subarray_sum_equals_k(nums, k)
        elapsed = time.time() - start

        # Number of subarrays of length 100 in array of 20000
        assert result == 19901
        assert elapsed < 1.0
