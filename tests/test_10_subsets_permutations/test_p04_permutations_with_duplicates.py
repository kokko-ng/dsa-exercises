"""Tests for permutations_with_duplicates problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def permutations_with_duplicates():
    func = get_function("permutations_with_duplicates")
    if func is None:
        pytest.skip("Function 'permutations_with_duplicates' not registered.")
    return func


class TestPermutationsWithDuplicatesBasic:
    def test_example_1(self, permutations_with_duplicates):
        result = permutations_with_duplicates([1, 1, 2])
        expected = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
        assert len(result) == 3
        for perm in expected:
            assert perm in result

    def test_example_2(self, permutations_with_duplicates):
        result = permutations_with_duplicates([1, 2, 3])
        assert len(result) == 6

    def test_all_same(self, permutations_with_duplicates):
        result = permutations_with_duplicates([1, 1, 1])
        assert len(result) == 1
        assert result == [[1, 1, 1]]


class TestPermutationsWithDuplicatesEdgeCases:
    def test_two_duplicates(self, permutations_with_duplicates):
        result = permutations_with_duplicates([1, 1])
        assert len(result) == 1

    def test_single_element(self, permutations_with_duplicates):
        result = permutations_with_duplicates([5])
        assert result == [[5]]


@pytest.mark.performance
class TestPermutationsWithDuplicatesPerformance:
    def test_with_duplicates(self, permutations_with_duplicates):
        nums = [1, 1, 2, 2, 3, 3]

        start = time.time()
        result = permutations_with_duplicates(nums)
        elapsed = time.time() - start

        # 6! / (2! * 2! * 2!) = 720 / 8 = 90
        assert len(result) == 90
        assert elapsed < 1.0
