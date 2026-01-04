"""Tests for kth_smallest_in_matrix problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def kth_smallest_in_matrix():
    func = get_function("kth_smallest_in_matrix")
    if func is None:
        pytest.skip("Function 'kth_smallest_in_matrix' not registered.")
    return func


class TestKthSmallestInMatrixBasic:
    """Basic functionality tests."""

    def test_standard_case(self, kth_smallest_in_matrix):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        assert kth_smallest_in_matrix(matrix, 8) == 13

    def test_single_element(self, kth_smallest_in_matrix):
        assert kth_smallest_in_matrix([[-5]], 1) == -5

    def test_k_equals_1(self, kth_smallest_in_matrix):
        matrix = [[1, 2], [3, 4]]
        assert kth_smallest_in_matrix(matrix, 1) == 1

    def test_k_equals_n_squared(self, kth_smallest_in_matrix):
        matrix = [[1, 2], [3, 4]]
        assert kth_smallest_in_matrix(matrix, 4) == 4


class TestKthSmallestInMatrixEdgeCases:
    """Edge case tests."""

    def test_all_same(self, kth_smallest_in_matrix):
        matrix = [[5, 5], [5, 5]]
        assert kth_smallest_in_matrix(matrix, 3) == 5

    def test_negative_numbers(self, kth_smallest_in_matrix):
        matrix = [[-5, -4], [-3, -2]]
        assert kth_smallest_in_matrix(matrix, 2) == -4

    def test_2x2_matrix(self, kth_smallest_in_matrix):
        matrix = [[1, 2], [1, 3]]
        assert kth_smallest_in_matrix(matrix, 2) == 1


@pytest.mark.performance
class TestKthSmallestInMatrixPerformance:
    """Performance tests."""

    def test_large_matrix(self, kth_smallest_in_matrix):
        n = 100
        matrix = [[i + j for j in range(n)] for i in range(n)]
        k = n * n // 2

        start = time.time()
        result = kth_smallest_in_matrix(matrix, k)
        elapsed = time.time() - start

        assert result >= 0
        assert elapsed < 1.0
