"""Tests for merge_sorted_arrays problem."""
import pytest
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def merge_sorted_arrays():
    func = get_function("merge_sorted_arrays")
    if func is None:
        pytest.skip("Function 'merge_sorted_arrays' not registered.")
    return func


class TestMergeSortedArraysBasic:
    def test_standard_merge(self, merge_sorted_arrays):
        nums1 = [1, 2, 3, 0, 0, 0]
        merge_sorted_arrays(nums1, 3, [2, 5, 6], 3)
        assert nums1 == [1, 2, 2, 3, 5, 6]

    def test_nums2_smaller(self, merge_sorted_arrays):
        nums1 = [4, 5, 6, 0, 0, 0]
        merge_sorted_arrays(nums1, 3, [1, 2, 3], 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]

    def test_nums2_larger(self, merge_sorted_arrays):
        nums1 = [1, 2, 3, 0, 0, 0]
        merge_sorted_arrays(nums1, 3, [4, 5, 6], 3)
        assert nums1 == [1, 2, 3, 4, 5, 6]


class TestMergeSortedArraysEdgeCases:
    def test_empty_nums2(self, merge_sorted_arrays):
        nums1 = [1]
        merge_sorted_arrays(nums1, 1, [], 0)
        assert nums1 == [1]

    def test_empty_nums1(self, merge_sorted_arrays):
        nums1 = [0]
        merge_sorted_arrays(nums1, 0, [1], 1)
        assert nums1 == [1]

    def test_single_elements(self, merge_sorted_arrays):
        nums1 = [2, 0]
        merge_sorted_arrays(nums1, 1, [1], 1)
        assert nums1 == [1, 2]

    def test_duplicates(self, merge_sorted_arrays):
        nums1 = [1, 2, 3, 0, 0, 0]
        merge_sorted_arrays(nums1, 3, [1, 2, 3], 3)
        assert nums1 == [1, 1, 2, 2, 3, 3]
