"""Tests for merge_k_sorted_arrays problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def merge_k_sorted_arrays():
    func = get_function("merge_k_sorted_arrays")
    if func is None:
        pytest.skip("Function 'merge_k_sorted_arrays' not registered.")
    return func


class TestMergeKSortedArraysBasic:
    def test_example_1(self, merge_k_sorted_arrays):
        arrays = [[1, 4, 5], [1, 3, 4], [2, 6]]
        result = merge_k_sorted_arrays(arrays)
        assert result == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_example_2(self, merge_k_sorted_arrays):
        arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = merge_k_sorted_arrays(arrays)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_empty_arrays(self, merge_k_sorted_arrays):
        arrays = [[]]
        result = merge_k_sorted_arrays(arrays)
        assert result == []

    def test_single_array(self, merge_k_sorted_arrays):
        arrays = [[1, 2, 3]]
        result = merge_k_sorted_arrays(arrays)
        assert result == [1, 2, 3]


class TestMergeKSortedArraysEdgeCases:
    def test_mixed_empty(self, merge_k_sorted_arrays):
        arrays = [[], [1, 2], [], [3]]
        result = merge_k_sorted_arrays(arrays)
        assert result == [1, 2, 3]

    def test_negative_values(self, merge_k_sorted_arrays):
        arrays = [[-5, -3], [-4, -2], [-6, -1]]
        result = merge_k_sorted_arrays(arrays)
        assert result == [-6, -5, -4, -3, -2, -1]


@pytest.mark.performance
class TestMergeKSortedArraysPerformance:
    def test_large_input(self, merge_k_sorted_arrays):
        # 100 arrays, 100 elements each
        arrays = [[i * 100 + j for j in range(100)] for i in range(100)]

        start = time.time()
        result = merge_k_sorted_arrays(arrays)
        elapsed = time.time() - start

        assert len(result) == 10000
        assert result == sorted(result)
        assert elapsed < 2.0
