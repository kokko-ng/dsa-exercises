"""Tests for subsets_with_duplicates problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def subsets_with_duplicates():
    func = get_function("subsets_with_duplicates")
    if func is None:
        pytest.skip("Function 'subsets_with_duplicates' not registered.")
    return func


class TestSubsetsWithDuplicatesBasic:
    def test_example_1(self, subsets_with_duplicates):
        result = subsets_with_duplicates([1, 2, 2])
        expected = [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
        assert len(result) == len(expected)
        # Check each expected subset is in result (order may vary)
        result_sorted = [sorted(r) for r in result]
        for subset in expected:
            assert sorted(subset) in result_sorted

    def test_example_2(self, subsets_with_duplicates):
        result = subsets_with_duplicates([0])
        assert len(result) == 2

    def test_all_duplicates(self, subsets_with_duplicates):
        result = subsets_with_duplicates([1, 1, 1])
        expected = [[], [1], [1, 1], [1, 1, 1]]
        assert len(result) == 4


class TestSubsetsWithDuplicatesEdgeCases:
    def test_no_duplicates(self, subsets_with_duplicates):
        result = subsets_with_duplicates([1, 2, 3])
        assert len(result) == 8

    def test_two_pairs(self, subsets_with_duplicates):
        result = subsets_with_duplicates([1, 1, 2, 2])
        # Unique subsets: [], [1], [1,1], [2], [2,2], [1,2], [1,1,2], [1,2,2], [1,1,2,2]
        assert len(result) == 9


@pytest.mark.performance
class TestSubsetsWithDuplicatesPerformance:
    def test_large_with_duplicates(self, subsets_with_duplicates):
        nums = [1] * 5 + [2] * 5

        start = time.time()
        result = subsets_with_duplicates(nums)
        elapsed = time.time() - start

        assert len(result) > 0
        assert elapsed < 1.0
