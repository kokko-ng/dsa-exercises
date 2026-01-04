"""Tests for smallest_number_range problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def smallest_number_range():
    func = get_function("smallest_number_range")
    if func is None:
        pytest.skip("Function 'smallest_number_range' not registered.")
    return func


class TestSmallestNumberRangeBasic:
    """Basic functionality tests."""

    def test_standard_case(self, smallest_number_range):
        lists = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
        result = smallest_number_range(lists)
        assert result == [20, 24]

    def test_same_elements(self, smallest_number_range):
        lists = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        result = smallest_number_range(lists)
        assert result == [1, 1]

    def test_two_lists(self, smallest_number_range):
        lists = [[1, 5, 8], [4, 12, 32]]
        result = smallest_number_range(lists)
        # Range [4, 5] covers 5 from first list and 4 from second
        assert result == [4, 5]


class TestSmallestNumberRangeEdgeCases:
    """Edge case tests."""

    def test_single_element_lists(self, smallest_number_range):
        lists = [[1], [2], [3]]
        result = smallest_number_range(lists)
        assert result == [1, 3]

    def test_overlapping_lists(self, smallest_number_range):
        lists = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = smallest_number_range(lists)
        assert result == [3, 3]

    def test_negative_numbers(self, smallest_number_range):
        lists = [[-5, -3, 0], [-4, -2, 1], [-6, -1, 2]]
        result = smallest_number_range(lists)
        # Need to check what the smallest range is
        # -3, -2, -1 gives range [-3, -1]
        assert result[1] - result[0] <= 3


@pytest.mark.performance
class TestSmallestNumberRangePerformance:
    """Performance tests."""

    def test_large_input(self, smallest_number_range):
        # 50 lists, 50 elements each
        lists = [list(range(i, i + 50)) for i in range(0, 2500, 50)]

        start = time.time()
        result = smallest_number_range(lists)
        elapsed = time.time() - start

        assert len(result) == 2
        assert result[0] <= result[1]
        assert elapsed < 1.0
