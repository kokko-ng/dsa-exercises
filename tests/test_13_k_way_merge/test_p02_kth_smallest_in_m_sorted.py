"""Tests for kth_smallest_in_m_sorted problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def kth_smallest_in_m_sorted():
    func = get_function("kth_smallest_in_m_sorted")
    if func is None:
        pytest.skip("Function 'kth_smallest_in_m_sorted' not registered.")
    return func


class TestKthSmallestInMSortedBasic:
    """Basic functionality tests."""

    def test_standard_case(self, kth_smallest_in_m_sorted):
        lists = [[2, 6, 8], [3, 6, 7], [1, 3, 4]]
        assert kth_smallest_in_m_sorted(lists, 5) == 4

    def test_two_lists(self, kth_smallest_in_m_sorted):
        lists = [[5, 8, 9], [1, 7]]
        assert kth_smallest_in_m_sorted(lists, 3) == 7

    def test_k_equals_1(self, kth_smallest_in_m_sorted):
        lists = [[3, 5, 7], [1, 4, 6]]
        assert kth_smallest_in_m_sorted(lists, 1) == 1

    def test_k_equals_total(self, kth_smallest_in_m_sorted):
        lists = [[1, 2], [3, 4]]
        assert kth_smallest_in_m_sorted(lists, 4) == 4


class TestKthSmallestInMSortedEdgeCases:
    """Edge case tests."""

    def test_single_list(self, kth_smallest_in_m_sorted):
        assert kth_smallest_in_m_sorted([[1, 2, 3, 4, 5]], 3) == 3

    def test_single_element_lists(self, kth_smallest_in_m_sorted):
        lists = [[1], [2], [3]]
        assert kth_smallest_in_m_sorted(lists, 2) == 2

    def test_with_duplicates(self, kth_smallest_in_m_sorted):
        lists = [[1, 1, 2], [1, 2, 2]]
        assert kth_smallest_in_m_sorted(lists, 3) == 1


@pytest.mark.performance
class TestKthSmallestInMSortedPerformance:
    """Performance tests."""

    def test_large_input(self, kth_smallest_in_m_sorted):
        # 100 lists, 100 elements each
        lists = [list(range(i, i + 100)) for i in range(0, 10000, 100)]
        k = 5000

        start = time.time()
        result = kth_smallest_in_m_sorted(lists, k)
        elapsed = time.time() - start

        assert result == 4999
        assert elapsed < 1.0
