"""Tests for minimum_size_subarray_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_size_subarray_sum():
    func = get_function("minimum_size_subarray_sum")
    if func is None:
        pytest.skip("Function 'minimum_size_subarray_sum' not registered.")
    return func


class TestMinSizeSubarrayBasic:
    def test_example_1(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(7, [2, 3, 1, 2, 4, 3]) == 2

    def test_example_2(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(4, [1, 4, 4]) == 1

    def test_example_3(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


class TestMinSizeSubarrayEdgeCases:
    def test_single_element_match(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(5, [5]) == 1

    def test_single_element_no_match(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(5, [4]) == 0

    def test_entire_array(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(15, [1, 2, 3, 4, 5]) == 5

    def test_first_element(self, minimum_size_subarray_sum):
        assert minimum_size_subarray_sum(5, [10, 1, 2, 3]) == 1


@pytest.mark.performance
class TestMinSizeSubarrayPerformance:
    def test_large_input(self, minimum_size_subarray_sum):
        nums = [1] * 100000
        target = 1000

        start = time.time()
        result = minimum_size_subarray_sum(target, nums)
        elapsed = time.time() - start

        assert result == 1000
        assert elapsed < 1.0
