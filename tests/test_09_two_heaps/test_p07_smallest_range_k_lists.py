"""Tests for smallest_range_k_lists problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def smallest_range_k_lists():
    func = get_function("smallest_range_k_lists")
    if func is None:
        pytest.skip("Function 'smallest_range_k_lists' not registered.")
    return func


class TestSmallestRangeKListsBasic:
    def test_example_1(self, smallest_range_k_lists):
        nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        result = smallest_range_k_lists(nums)
        assert result == [20, 24]

    def test_example_2(self, smallest_range_k_lists):
        nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        result = smallest_range_k_lists(nums)
        assert result == [1, 1]

    def test_single_list(self, smallest_range_k_lists):
        nums = [[1, 2, 3]]
        result = smallest_range_k_lists(nums)
        assert result == [1, 1]


class TestSmallestRangeKListsEdgeCases:
    def test_single_element_lists(self, smallest_range_k_lists):
        nums = [[1], [2], [3]]
        result = smallest_range_k_lists(nums)
        assert result == [1, 3]

    def test_negative_values(self, smallest_range_k_lists):
        nums = [[-10, -5, 0], [-8, -3, 2], [-6, -1, 4]]
        result = smallest_range_k_lists(nums)
        # Should find smallest range covering all lists
        assert result[1] - result[0] >= 0


@pytest.mark.performance
class TestSmallestRangeKListsPerformance:
    def test_large_input(self, smallest_range_k_lists):
        # 50 lists, 50 elements each
        nums = [[i * 50 + j for j in range(50)] for i in range(50)]

        start = time.time()
        result = smallest_range_k_lists(nums)
        elapsed = time.time() - start

        assert len(result) == 2
        assert result[0] <= result[1]
        assert elapsed < 2.0
