"""Tests for find_k_pairs_smallest_sums problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def find_k_pairs_smallest_sums():
    func = get_function("find_k_pairs_smallest_sums")
    if func is None:
        pytest.skip("Function 'find_k_pairs_smallest_sums' not registered.")
    return func


class TestFindKPairsSmallestSumsBasic:
    """Basic functionality tests."""

    def test_standard_case(self, find_k_pairs_smallest_sums):
        result = find_k_pairs_smallest_sums([1, 7, 11], [2, 4, 6], 3)
        # Expected: [[1,2],[1,4],[1,6]]
        assert len(result) == 3
        sums = [p[0] + p[1] for p in result]
        assert sums == sorted(sums)  # Sums should be non-decreasing

    def test_with_duplicates(self, find_k_pairs_smallest_sums):
        result = find_k_pairs_smallest_sums([1, 1, 2], [1, 2, 3], 2)
        assert len(result) == 2
        # First two pairs should have sum 2
        assert all(p[0] + p[1] == 2 for p in result)

    def test_k_equals_1(self, find_k_pairs_smallest_sums):
        result = find_k_pairs_smallest_sums([1, 2], [3, 4], 1)
        assert result == [[1, 3]]


class TestFindKPairsSmallestSumsEdgeCases:
    """Edge case tests."""

    def test_single_element_arrays(self, find_k_pairs_smallest_sums):
        result = find_k_pairs_smallest_sums([1], [2], 1)
        assert result == [[1, 2]]

    def test_k_larger_than_pairs(self, find_k_pairs_smallest_sums):
        result = find_k_pairs_smallest_sums([1, 2], [3], 5)
        # Only 2 pairs possible
        assert len(result) <= 2

    def test_negative_numbers(self, find_k_pairs_smallest_sums):
        result = find_k_pairs_smallest_sums([-1, 0, 1], [-2, -1, 0], 3)
        assert len(result) == 3


@pytest.mark.performance
class TestFindKPairsSmallestSumsPerformance:
    """Performance tests."""

    def test_large_input(self, find_k_pairs_smallest_sums):
        nums1 = list(range(1000))
        nums2 = list(range(1000))
        k = 1000

        start = time.time()
        result = find_k_pairs_smallest_sums(nums1, nums2, k)
        elapsed = time.time() - start

        assert len(result) == k
        assert elapsed < 1.0
