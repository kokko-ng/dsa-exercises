"""Tests for kth_smallest_in_sorted_matrix problem."""
import pytest
import time
from dsa_helpers._function_registry import get as get_function


@pytest.fixture
def kth_smallest_in_sorted_matrix():
    func = get_function("kth_smallest_in_sorted_matrix")
    if func is None:
        pytest.skip("Function 'kth_smallest_in_sorted_matrix' not registered.")
    return func


class TestKthSmallestInSortedMatrixBasic:
    def test_example_1(self, kth_smallest_in_sorted_matrix):
        matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
        assert kth_smallest_in_sorted_matrix(matrix, 8) == 13

    def test_single_element(self, kth_smallest_in_sorted_matrix):
        matrix = [[-5]]
        assert kth_smallest_in_sorted_matrix(matrix, 1) == -5

    def test_k_equals_1(self, kth_smallest_in_sorted_matrix):
        matrix = [[1, 2], [3, 4]]
        assert kth_smallest_in_sorted_matrix(matrix, 1) == 1

    def test_k_equals_n_squared(self, kth_smallest_in_sorted_matrix):
        matrix = [[1, 2], [3, 4]]
        assert kth_smallest_in_sorted_matrix(matrix, 4) == 4


class TestKthSmallestInSortedMatrixEdgeCases:
    def test_negative_values(self, kth_smallest_in_sorted_matrix):
        matrix = [[-5, -4], [-3, -2]]
        assert kth_smallest_in_sorted_matrix(matrix, 3) == -3

    def test_duplicates(self, kth_smallest_in_sorted_matrix):
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        assert kth_smallest_in_sorted_matrix(matrix, 5) == 1


@pytest.mark.performance
class TestKthSmallestInSortedMatrixPerformance:
    def test_large_matrix(self, kth_smallest_in_sorted_matrix):
        n = 100
        matrix = [[i * n + j for j in range(n)] for i in range(n)]

        start = time.time()
        result = kth_smallest_in_sorted_matrix(matrix, n * n // 2)
        elapsed = time.time() - start

        assert result == n * n // 2 - 1
        assert elapsed < 2.0
