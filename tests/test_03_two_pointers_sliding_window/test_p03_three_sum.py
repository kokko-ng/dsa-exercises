"""Tests for three_sum problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def three_sum():
    func = get_function("three_sum")
    if func is None:
        pytest.skip("Function 'three_sum' not registered.")
    return func


def normalize_triplets(triplets):
    """Sort each triplet and the list for comparison."""
    return sorted([sorted(t) for t in triplets])


class TestThreeSumBasic:
    def test_example_1(self, three_sum):
        result = three_sum([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        assert normalize_triplets(result) == normalize_triplets(expected)

    def test_no_solution(self, three_sum):
        assert three_sum([0, 1, 1]) == []

    def test_all_zeros(self, three_sum):
        result = three_sum([0, 0, 0])
        assert normalize_triplets(result) == [[0, 0, 0]]


class TestThreeSumEdgeCases:
    def test_multiple_solutions(self, three_sum):
        result = three_sum([-2, 0, 1, 1, 2])
        expected = [[-2, 0, 2], [-2, 1, 1]]
        assert normalize_triplets(result) == normalize_triplets(expected)

    def test_with_duplicates(self, three_sum):
        result = three_sum([-1, -1, -1, 2, 2])
        expected = [[-1, -1, 2]]
        assert normalize_triplets(result) == normalize_triplets(expected)

    def test_min_array(self, three_sum):
        result = three_sum([1, 2, 3])
        assert result == []


@pytest.mark.performance
class TestThreeSumPerformance:
    def test_large_input(self, three_sum):
        nums = list(range(-500, 501))

        start = time.time()
        result = three_sum(nums)
        elapsed = time.time() - start

        # Just verify it runs in reasonable time
        assert elapsed < 2.0
