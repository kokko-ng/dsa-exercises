"""Tests for minimum_subset_sum_difference problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def minimum_subset_sum_difference():
    func = get_function("minimum_subset_sum_difference")
    if func is None:
        pytest.skip("Function 'minimum_subset_sum_difference' not registered.")
    return func


class TestMinimumSubsetSumDifferenceBasic:
    def test_example_1(self, minimum_subset_sum_difference):
        assert minimum_subset_sum_difference([1, 6, 11, 5]) == 1

    def test_example_2(self, minimum_subset_sum_difference):
        assert minimum_subset_sum_difference([1, 2, 3, 4]) == 0


class TestMinimumSubsetSumDifferenceEdgeCases:
    def test_single_element(self, minimum_subset_sum_difference):
        assert minimum_subset_sum_difference([5]) == 5

    def test_two_equal(self, minimum_subset_sum_difference):
        assert minimum_subset_sum_difference([5, 5]) == 0

    def test_all_same(self, minimum_subset_sum_difference):
        assert minimum_subset_sum_difference([3, 3, 3, 3]) == 0


@pytest.mark.performance
class TestMinimumSubsetSumDifferencePerformance:
    def test_large_input(self, minimum_subset_sum_difference):
        nums = [i % 50 + 1 for i in range(50)]

        start = time.time()
        result = minimum_subset_sum_difference(nums)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 2.0
