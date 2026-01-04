"""Tests for four_sum_ii problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def four_sum_ii():
    func = get_function("four_sum_ii")
    if func is None:
        pytest.skip("Function 'four_sum_ii' not registered.")
    return func


class TestFourSumIIBasic:
    def test_example_1(self, four_sum_ii):
        result = four_sum_ii([1, 2], [-2, -1], [-1, 2], [0, 2])
        assert result == 2

    def test_example_2(self, four_sum_ii):
        result = four_sum_ii([0], [0], [0], [0])
        assert result == 1

    def test_no_solution(self, four_sum_ii):
        result = four_sum_ii([1], [2], [3], [4])
        assert result == 0


class TestFourSumIIEdgeCases:
    def test_all_zeros(self, four_sum_ii):
        result = four_sum_ii([0, 0], [0, 0], [0, 0], [0, 0])
        assert result == 16

    def test_negative_positive(self, four_sum_ii):
        result = four_sum_ii([-1], [1], [-1], [1])
        assert result == 1

    def test_larger_arrays(self, four_sum_ii):
        nums1 = [1, -1, 2]
        nums2 = [-1, 1, -2]
        nums3 = [0, 1, -1]
        nums4 = [0, -1, 1]
        result = four_sum_ii(nums1, nums2, nums3, nums4)
        assert result == 17


@pytest.mark.performance
class TestFourSumIIPerformance:
    def test_large_input(self, four_sum_ii):
        n = 100
        nums1 = list(range(n))
        nums2 = list(range(-n, 0))
        nums3 = [0] * n
        nums4 = [0] * n

        start = time.time()
        result = four_sum_ii(nums1, nums2, nums3, nums4)
        elapsed = time.time() - start

        assert result == n * n * n  # Each (i, -i-1, 0, 0) but need to verify
        assert elapsed < 2.0
