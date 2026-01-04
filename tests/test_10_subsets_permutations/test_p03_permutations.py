"""Tests for permutations problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def permutations():
    func = get_function("permutations")
    if func is None:
        pytest.skip("Function 'permutations' not registered.")
    return func


class TestPermutationsBasic:
    def test_example_1(self, permutations):
        result = permutations([1, 2, 3])
        expected = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        assert len(result) == 6
        for perm in expected:
            assert perm in result

    def test_example_2(self, permutations):
        result = permutations([0, 1])
        assert len(result) == 2
        assert [0, 1] in result
        assert [1, 0] in result

    def test_example_3(self, permutations):
        result = permutations([1])
        assert result == [[1]]


class TestPermutationsEdgeCases:
    def test_two_elements(self, permutations):
        result = permutations([1, 2])
        assert len(result) == 2

    def test_factorial_count(self, permutations):
        # 4! = 24
        result = permutations([1, 2, 3, 4])
        assert len(result) == 24


@pytest.mark.performance
class TestPermutationsPerformance:
    def test_six_elements(self, permutations):
        nums = list(range(6))

        start = time.time()
        result = permutations(nums)
        elapsed = time.time() - start

        assert len(result) == 720  # 6!
        assert elapsed < 1.0
