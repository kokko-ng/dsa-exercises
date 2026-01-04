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
    """Basic functionality tests."""

    def test_three_arrays(self, merge_k_sorted_arrays):
        result = merge_k_sorted_arrays([[1, 4, 5], [1, 3, 4], [2, 6]])
        assert result == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_sequential_arrays(self, merge_k_sorted_arrays):
        result = merge_k_sorted_arrays([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]])
        assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def test_two_arrays(self, merge_k_sorted_arrays):
        result = merge_k_sorted_arrays([[1, 2], [3, 4]])
        assert result == [1, 2, 3, 4]


class TestMergeKSortedArraysEdgeCases:
    """Edge case tests."""

    def test_single_array(self, merge_k_sorted_arrays):
        assert merge_k_sorted_arrays([[1, 2, 3]]) == [1, 2, 3]

    def test_empty_arrays(self, merge_k_sorted_arrays):
        result = merge_k_sorted_arrays([[], [1, 2], []])
        assert result == [1, 2]

    def test_all_empty(self, merge_k_sorted_arrays):
        assert merge_k_sorted_arrays([[], [], []]) == []

    def test_single_elements(self, merge_k_sorted_arrays):
        result = merge_k_sorted_arrays([[3], [1], [2]])
        assert result == [1, 2, 3]


@pytest.mark.performance
class TestMergeKSortedArraysPerformance:
    """Performance tests."""

    def test_large_input(self, merge_k_sorted_arrays):
        arrays = [list(range(i, i + 100)) for i in range(0, 10000, 100)]

        start = time.time()
        result = merge_k_sorted_arrays(arrays)
        elapsed = time.time() - start

        assert len(result) == 10000
        assert result == sorted(result)
        assert elapsed < 1.0
