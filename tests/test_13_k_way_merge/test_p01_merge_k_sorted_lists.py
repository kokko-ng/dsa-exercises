"""Tests for merge_k_sorted_lists problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def merge_k_sorted_lists():
    """Get the user's merge_k_sorted_lists implementation."""
    func = get_function("merge_k_sorted_lists")
    if func is None:
        pytest.skip("Function 'merge_k_sorted_lists' not registered.")
    return func


class TestMergeKSortedListsBasic:
    """Basic functionality tests."""

    def test_three_lists(self, merge_k_sorted_lists):
        result = merge_k_sorted_lists([[1, 4, 5], [1, 3, 4], [2, 6]])
        assert result == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_empty_input(self, merge_k_sorted_lists):
        assert merge_k_sorted_lists([]) == []

    def test_single_empty_list(self, merge_k_sorted_lists):
        assert merge_k_sorted_lists([[]]) == []

    def test_single_list(self, merge_k_sorted_lists):
        assert merge_k_sorted_lists([[1, 2, 3]]) == [1, 2, 3]

    def test_two_lists(self, merge_k_sorted_lists):
        result = merge_k_sorted_lists([[1, 3, 5], [2, 4, 6]])
        assert result == [1, 2, 3, 4, 5, 6]


class TestMergeKSortedListsEdgeCases:
    """Edge case tests."""

    def test_some_empty_lists(self, merge_k_sorted_lists):
        result = merge_k_sorted_lists([[], [1, 2], [], [3]])
        assert result == [1, 2, 3]

    def test_all_same_elements(self, merge_k_sorted_lists):
        result = merge_k_sorted_lists([[1, 1], [1, 1], [1, 1]])
        assert result == [1, 1, 1, 1, 1, 1]

    def test_negative_numbers(self, merge_k_sorted_lists):
        result = merge_k_sorted_lists([[-5, -3], [-4, -2], [-6, -1]])
        assert result == [-6, -5, -4, -3, -2, -1]


@pytest.mark.performance
class TestMergeKSortedListsPerformance:
    """Performance tests."""

    def test_large_input(self, merge_k_sorted_lists):
        # Create 100 lists, each with 100 elements
        lists = [list(range(i, i + 100)) for i in range(0, 10000, 100)]

        start = time.time()
        result = merge_k_sorted_lists(lists)
        elapsed = time.time() - start

        assert len(result) == 10000
        assert result == sorted(result)
        assert elapsed < 1.0
